from django.db import models

class Participant(models.Model):
    pId = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=50)
    
class Dialogue(models.Model):
    dlgId = models.CharField(max_length=50, unique=True)
    creator = models.ForeignKey(Participant, related_name="dialogue_created") #User who initated the dialogue
    name = models.CharField(max_length=150)
    description = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    participants = models.ManyToManyField(Participant, related_name="dialogue_participated")
    context = models.CharField(max_length=150)

class Message(models.Model):
    dialogue = models.ForeignKey(Dialogue, related_name="message_included")
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Participant, related_name="message_authored") #User who created the message
    status = models.CharField(max_length=10)
    pgxml = models.TextField()

class Responder(models.Model):
    dialogue = models.ForeignKey(Dialogue, related_name="responder_included")
    respId = models.CharField(max_length=10)    # the order of responder in the current dialogue
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=10)
    
class Response(models.Model):
    message = models.ForeignKey(Message, related_name="responses_related")
    responder = models.ForeignKey(Responder, related_name="responses_generated")
    created_time = models.DateTimeField(auto_now_add=True)
    preview = models.TextField()
    explanation = models.TextField()
    content = models.TextField()