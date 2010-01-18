from django.conf import settings 
from django.http import HttpResponse

import os
import yaml
from dialogues.models import *

from Overhearer.DMLib.DialogueManager import DialogueManager

try:
    # 2.6 will have a json module in the stdlib
    import json
except ImportError:
    try:
        # simplejson is the thing from which json was derived anyway...
        import simplejson as json
    except ImportError:
        print "No suitable json library found"

# maintain the list of ongoing dialogues
currDialogues = []

def getDialogueById(dialogueId):
  """docstring for __getDialogueById"""
  if dialogueId:
    for dialogue in currDialogues:
      if dialogue.id == dialogueId:
        return dialogue
  return None

def check_validity(config):
    """check the validity of Config"""
    if config.has_key("context") and config.has_key("parser_dir") and config.has_key("kbase") and config.has_key("actuator_dir") and config.has_key("executor") and config.has_key("responders"):
        if len(config["responders"]) > 0:
            return True
    return False


def dialoguesHandler(request):
    if request.method == "GET":
        response = []
        for dialogue in currDialogues:
            response.append(dialogue.id)
        return HttpResponse(json.dumps(response), mimetype='application/json')
    elif request.method == "POST":
        response = {}
        data = json.loads(request.raw_post_data)
        id = data.get("id", "")
        if id:
            # check whether the id exists in database
            if getDialogueById(id):
                response["status"] = "error"
                response["message"] = "the dialogue already exists!"
                return HttpResponse(json.dumps(response), mimetype='application/json')
            # check whether the id exists in database
            try:
                dialogue = Dialogue.objects.get(dlgId=id)
                # TODO load the dialogue from the database
            except Dialogue.DoesNotExist:
                pass
        participants = data.get("participants", [])
        if participants:
            f = open(os.path.join(settings.PROJECT_PATH, settings.CONTEXT, 'config.yaml'))
            config = yaml.load(f)
            f.close()
            if config and check_validity(config):
                dialogue = DialogueManager(config, id)
                participants_added = []
                for participant in participants:
                    if dialogue.addParticipant(participant):
                        participants_added.append(participant)
                # if more than the total number of dialogues, pop out the first dialogue
                if len(currDialogues) >= settings.DIALOGUE_NUM:
                    currDialogues.pop(0)
                currDialogues.append(dialogue)
                response["status"] = "success"
                response["dialogueId"] = dialogue.id
                if settings.PERSISTENCE:
                    dlg = Dialogue(dlgId=dialogue.id, name=data.get("name", ""), description=data.get("description", ""), context=settings.CONTEXT)
                    for i, participant in enumerate(participants_added):
                        pId = participant.get("id", "")
                        username = participant.get("name", "")
                        try:
                            p = Participant.objects.get(pId=pId)
                        except Participant.DoesNotExist:
                            p = Participant(pId=pId, username=username)
                            p.save()
                        # only add the first participant as creator when creating the dialogue
                        if i == 0:
                            dlg.creator = p
                            dlg.save()
                        dlg.participants.add(p)
                    for responder in dialogue.getResponders():
                        resp_model = Responder(dialogue=dlg, respId=responder.get("id", ""), type=responder.get("type", ""), name=responder.get("name", ""))
                        resp_model.save()
                    dlg.save()
            else:
                response["status"] = "error"
                response["message"] = "no config file is found or the config file is invalid!"
        else:
            response["status"] = "error"
            response["message"] = "the dialogue must involves at least one participant!"
        return HttpResponse(json.dumps(response), mimetype='application/json')
    
def messagesHandler(request, dlgId):
    if request.method == "GET":
        return HttpResponse("Hello, world. You're at the messagesHandler index.")
    elif request.method == "POST":    
        response = {}
        dialogue = getDialogueById(dlgId)
        if dialogue:
            data = json.loads(request.raw_post_data)
            response = dialogue.process(data)
        else: 
            response["status"] = "error"
            response["message"] = "the dialogue (%s) does not exists!" % dlgId
        if settings.PERSISTENCE:
            dlg = Dialogue.objects.get(dlgId=dlgId)
            msg = Message(dialogue=dlg, content=data.get("message", ""))
            if type(response) == list:
                msg.status = "success"
            else:
                msg.status = response.get("status", "")
            pId = data.get("speakerId", "")
            try:
                p = Participant.objects.get(pId=pId)
                msg.author = p
            except Participant.DoesNotExist:
                pass
            msg.save()
            if msg.status == "success":
                msg.pgxml = dialogue.getPlanGraphXML()
                for dlg_response in response:
                    respId = dlg_response.get("id", "")
                    if respId:
                        try:
                            responder = Responder.objects.get(dialogue=dlg, respId=respId)
                            resp = Response(message=msg, responder=responder, preview=dlg_response.get("preview", ""), explanation=dlg_response.get("explanation", ""))
                            content = dialogue.getResponseContent(respId).get("content", "")
                            if content:
                                resp.content = content
                            resp.save()
                        except Responder.DoesNotExist:
                            pass    
                msg.save()        
        return HttpResponse(json.dumps(response), mimetype='application/json')


def participantsHandler(request, dlgId):
    if request.method == "GET":
        return HttpResponse("Hello, world. You're at the participantsHandler.")
    elif request.method == "POST":
        response = {}
        dialogue = getDialogueById(dlgId)
        if dialogue:
            participant = json.loads(request.raw_post_data)
            if dialogue.addParticipant(participant):
                if settings.PERSISTENCE:
                    pId = participant.get("id", "")
                    username = participant.get("name", "")
                    try:
                        p = Participant.objects.get(pId=pId)
                    except Participant.DoesNotExist:
                        p = Participant(pId=pId, username=username)
                        p.save()
                    try:
                        dlg = Dialogue.objects.get(dlgId=dlgId)
                        dlg.participants.add(p)
                        response["status"] = "success"
                        response["participant"] = {
                            "id" : pId
                        }
                    except Dialogue.DoesNotExist:
                        response["status"] = "error"
                        response["message"] = "the dialogue (%s) does not exists!" % dlgId
            else:
                response["status"] = "error"
                response["message"] = "the participant cannot be added!"
        else: 
            response["status"] = "error"
            response["message"] = "the dialogue (%s) does not exists!" % dlgId
        return HttpResponse(json.dumps(response), mimetype='application/json')

def plangraphHandler(request, dlgId):
    if request.method == "GET":
        dialogue = getDialogueById(dlgId)
        if dialogue:
            return HttpResponse(dialogue.getPlanGraphXML(), mimetype='text/xml')
        else:
            response = {}
            response["status"] = "error"
            response["message"] = "the dialogue (%s) does not exists!" % dlgId
            return HttpResponse(json.dumps(response), mimetype='application/json')

def responsesHandler(request, dlgId):
    if request.method == "GET":
        dialogue = getDialogueById(dlgId)
        if dialogue:
            response = dialogue.getCurrentResponses()
        else:
            response = {}
            response["status"] = "error"
            response["message"] = "the dialogue (%s) does not exists!" % dlgId
        return HttpResponse(json.dumps(response), mimetype='application/json')

def responseHandler(request, dlgId, respId):
    if request.method == "GET":
        dialogue = getDialogueById(dlgId)
        if dialogue:
            response = dialogue.getResponseContent(respId)
            if response.get("status", "") == "error":
                return HttpResponse(json.dumps(response), mimetype='application/json')
            elif response["type"] == "map":
                return HttpResponse(response.get("content", ""), mimetype='text/xml')
            elif response["type"] == "text":
                return HttpResponse(response.get("content", ""), mimetype='text/plain')
        else:
            response = {}
            response["status"] = "error"
            response["message"] = "the dialogue (%s) does not exists!" % dlgId
            return HttpResponse(json.dumps(response), mimetype='application/json')
            
def dialogueHandler(request, dlgId):
    return HttpResponse("Hello, world. You're at the dialogueHandler index.")

def messageHandler(request, dlgId, msgId):
    return HttpResponse("Hello, world. You're at the messageHandler index.")

def participantHandler(request, pId):
    return HttpResponse("Hello, world. You're at the participantHandler index.")




