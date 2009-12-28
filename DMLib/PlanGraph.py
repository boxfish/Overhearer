#!/usr/bin/env python
# encoding: utf-8
"""
Plan Graph Model

Created by Bo Yu on 2009-12-11.
"""
__author__ = 'byu@ist.psu.edu (Bo Yu)'

import sys
import os
import xml.dom.minidom as minidom
import copy

from MentalState import *
from MapControl import *
from KnowledgeBase import *
from Agent import *
import BasicActions

class PlanGraph():
  """model the plan graph"""
  def __init__(self, kb, mapCtrl):
    self.properties = ("root", "focus", "agenda")
    self.kb = kb
    self.mapCtrl = mapCtrl
    self.root = None
    self.focus = []
    self.agenda = []
  
  def __repr__(self):
    """docstring for __repr__"""
    return "(" + ",".join(["%s=%s" % (attr, getattr(self, attr)) for attr in self.properties if hasattr(self, attr)] ) + ")"
  
  def parsePhrases(self, phrases, speakerId):
    """parse phrases to tempPlans"""
    tempPlans = self.kb.parsePhrases(phrases)
    # add the speaker as agent to the tempPlans
    for plan in tempPlans:
      agent = Agent(speakerId)
      # set the default mental states of the speaker, may be changed when the conversation is developed
      # By default, the system believes that the speaker intends that they perform the action
      agent.mentalState.intention = int_intendThat
      if plan.complexity == "complex":
        # By default, the system believes that the speaker believes that they have a recipe of the action
        agent.mentalState.execStatus = exec_hasRecipe
      else:
        # By default, the system believes that the speaker believes that they can bring about the action
        agent.mentalState.execStatus = exec_canBringAbout
      plan.agents.append(agent)
      plan.initiator = speakerId
    return tempPlans
  
  def explain(self, tempPlans):
    """docstring for __explain"""
    self.focus = []
    hasAction = False
    for plan in tempPlans:
      if plan.actionType == "ACTION":
        speakerId = plan.initiator
        explainedPlan = self.__explainPlanGraph(plan)
        if explainedPlan:
          self.focus.append(explainedPlan)
          explainedPlan.updateMentalStates(speakerId)
          hasAction = True
          break
    for plan in tempPlans:
      if plan.actionType != "ACTION":
        speakerId = plan.initiator
        explainedPlan = self.__explainPlanGraph(plan)
        if explainedPlan:
            explainedPlan.updateMentalStates(speakerId)
            if not hasAction:
              self.focus.append(explainedPlan)
    return self.focus

  def __explainPlanGraph(self, tempPlan):
    """docstring for __explainPlan"""
    if self.root == None:
      # current planGraph is empty
      if tempPlan.actionType == "ACTION":
        # Initiation of a new plan, set the tempPlan as the Root
        self.root = tempPlan
        return tempPlan
      else:
        return None
    else:
      return self.__explainPlanNode(self.root, tempPlan)
  
  def __explainPlanNode(self, plan, tempPlan):
    currentPlan = None
    if tempPlan.actionName == plan.actionName:
      # 1. if tempPlan is same as the current plan, update the current plan using tempPlan
      if plan.actionType == "ID_PARA" and plan.refPhrase:  
        hasFound = False
        for subPlan in plan.parent.subPlans:
          if subPlan.refPhrase == tempPlan.refPhrase:
            explainedPlan = copy.copy(subPlan)
            hasFound = True
            break
        if hasFound:
          # The current plan has same reference with tempPlan
          plan.parent.subPlans = []
          plan.parent.values = []
          plan.parent.subPlans.append(explainedPlan)
        else:
          # The current plan has differnt reference from tempPlan
          tempPlan.parent = plan.parent
          plan.parent.subPlans.append(tempPlan)
          return tempPlan
      else:
        plan.refPhrase = tempPlan.refPhrase
        plan.refType = tempPlan.refType
        plan.refId = tempPlan.refId
        explainedPlan = plan
      tempAgent = tempPlan.agents[0]
      exists = False
      for agent in explainedPlan.agents:
        if agent.id == tempAgent.id:
          agent.mentalState = tempAgent.mentalState
          exists = True
          break
      if not exists:
        explainedPlan.agents.append(tempAgent)
        if len(explainedPlan.agents) == 1:
          plan.initiator = tempAgent.id      
      return explainedPlan    
    if plan.complexity == "complex":
      if plan.mentalState.execStatus == exec_noRecipe:
        # the plan has not been elaborated
        selectedRecipe = self.kb.selectRecipe(plan.actionName)
        if selectedRecipe and plan.parseRecipe(selectedRecipe):
            plan.mentalState.execStatus = exec_hasRecipe
        else:
          return None
      # 2. explain the tempPlan in the Parameters
      paramsRdy = True
      for param in plan.params:
        currentPlan = self.__explainParamNode(param, tempPlan)
        if currentPlan:
          return currentPlan
        if param.status == param_status_notReady or param.status == param_status_fail:
          paramsRdy = False
      if not paramsRdy:
        # If parameters are not ready, don't bother explaining in following subactions
        return None
      # 3. explain the tempPlan in SubPlans
      for subPlan in plan.subPlans:
        if subPlan.mentalState.execStatus != exec_noRecipe:
          # the subplan has been elaborated
          currentPlan = self.__explainPlanNode(subPlan, tempPlan)
          if currentPlan:
            return currentPlan
        else:
          # the subplan has not been elaborated
          subPlanClone = copy.copy(subPlan)
          currentPlan = self.__explainPlanNode(subPlanClone, tempPlan)
          if currentPlan:
            subPlan = subPlanClone
            return currentPlan
      # 4. explain the tempPlan in Optional SubPlans
      for subOptPlan in plan.subOptPlans:
        subOptPlanClone = copy.copy(subOptPlan)
        currentPlan = self.__explainPlanNode(subOptPlanClone, tempPlan)
        if currentPlan:
          plan.subPlans.append(subOptPlanClone)
          plan.subOptPlans.remove(subOptPlan)
          return currentPlan    
    return currentPlan

  def __explainParamNode(self, param, tempPlan):
    """docstring for __explainParamNode"""
    currentPlan = None
    # 1. explain the tempPlan in SubPlans
    for subPlan in param.subPlans:
      currentPlan = self.__explainPlanNode(subPlan, tempPlan)
      if currentPlan:
        return currentPlan
    # 2. explain the tempPlan in optional SubPlans
    for subOptPlan in param.subOptPlans:
      subOptPlanClone = copy.copy(subOptPlan)
      currentPlan = self.__explainPlanNode(subOptPlanClone, tempPlan)
      if currentPlan:
        param.subPlans.append(subOptPlanClone)
        param.subOptPlans.remove(subOptPlan)
        return currentPlan
    return currentPlan

  def elaborate(self):
    """docstring for __elaborate"""
    self.agenda = []
    for plan in self.focus:
      self.__elaboratePlanNode(plan)

  def __elaboratePlanNode(self, plan):
    """docstring for __elaboratePlanNode"""
    isIntended = False
    for agent in plan.agents:
      if agent.mentalState.intention == int_intendThat:
        isIntended = True
        break
    if plan.mentalState.intention == int_intendThat:
      isIntended = True
    if isIntended:
      if plan.complexity == "complex":
        # assume the system be cooperative
        plan.mentalState.intention = int_intendThat
        if plan.mentalState.execStatus == exec_noRecipe:
          recipe = self.kb.selectRecipe(plan.actionName)
          if recipe:
            plan.parseRecipe(recipe)
            plan.mentalState.execStatus = exec_hasRecipe
        missingParams = False
        if plan.mentalState.execStatus != exec_paramReady:
          for param in plan.params:
            self.__elaborateParamNode(param)
            if param.status == param_status_notReady or param.status == param_status_fail:
              missingParams = True
        if not missingParams:
          for subPlan in plan.subPlans:
            subPlan.mentalState.intention = int_intendThat
            self.__elaboratePlanNode(subPlan)
      else:
        plan.mentalState.intention = int_intendTo
        self.agenda.append(plan)
        BasicActions.execute(plan, self.mapCtrl)
              
  def __elaborateParamNode(self, param):
    """docstring for __elaborateParamNode"""
    for subPlan in param.subPlans:
      self.__elaboratePlanNode(subPlan)
      
  def saveXML(self):
    doc = minidom.Document()
    pgNode = doc.createElement("planGraph")
    doc.appendChild(pgNode)
    agentsNode = doc.createElement("agents")
    pgNode.appendChild(agentsNode)
    for agent in self.root.agents:
      agentNode = doc.createElement("agent")
      agentNode.setAttribute("id", agent.id)
      agentsNode.appendChild(agentNode)
    rootNode = doc.createElement("root")
    pgNode.appendChild(rootNode)
    rootNode.appendChild(self.root.saveXML(doc))
    #return doc.toprettyxml(indent="  ")
    return doc.toxml()
    
class PlanNode():
  """docstring for PlanNode"""
  def __init__(self):
    self.properties = ("phrase", "actionName", "alias", "actionType", "complexity", "refType", "refPhrase", "refId", "parent", "subPlans", "subOptPlans", "params", "agents", "initiator", "mentalState", "recipeXML", "isOpt")
    self.phrase = ""
    self.actionName = ""
    self.alias = ""
    self.actionType = ""
    self.compexity = ""
    self.refType = ""
    self.refPhrase = ""
    self.refId = None
    self.parent = None
    self.subPlans = []
    self.subOptPlans = []
    self.params = []
    self.agents = []
    self.initiator = ""
    self.mentalState = MentalState()
    self.recipeXML = ""
    self.isOpt = True
    
  def __repr__(self):
    """docstring for __repr__"""
    return "(" + ",".join(["%s=%s" % (attr, getattr(self, attr)) for attr in self.properties if hasattr(self, attr)] ) + ")"
  
  def updateMentalStates(self, agentId):
    """docstring for __updateMentalStates"""
    exists = False
    currAgent = None
    for agent in self.agents:
      if agent.id == agentId:
        if agent.mentalState.intention != int_intendTo and agent.mentalState.intention != int_intendThat:
          return
        exists = True
        break
    if not exists:
      return
    # Assumption 1: If the agent intends that they perform an action, by default it also intends that they perform the parent action
    # Assumption 2: If the agent intends that they perform an action, by default it belives that the parameters of the parent action is rdy  
    parent = self.parent
    while parent:
      if isinstance(parent, PlanNode):
        exists = False
        for agent in parent.agents:
          if agent.id == agentId:
            agent.mentalState.intention = int_intendThat
            agent.mentalState.execStatus = exec_paramReady
            exists = True
            break
        if not exists:
          newAgent = Agent(agentId)
          newAgent.mentalState.intention = int_intendThat
          newAgent.mentalState.execStatus = exec_paramReady
          parent.agents.append(newAgent)
          if len(parent.agents) == 1:
            parent.initiator = agentId
      else:
        exists = False
        parent = parent.parent
        for agent in parent.agents:
          if agent.id == agentId:
            agent.mentalState.intention = int_intendThat
            agent.mentalState.execStatus = exec_hasRecipe
            exists = True
            break
        if not exists:
          newAgent = Agent(agentId)
          newAgent.mentalState.intention = int_intendThat
          newAgent.mentalState.execStatus = exec_hasRecipe
          parent.agents.append(newAgent)
          if len(parent.agents) == 1:
            parent.initiator = agentId
      parent = parent.parent

  def parseRecipe(self, recipe):
    """docstring for __parseRecipe"""
    xmldoc = minidom.parseString(recipe).documentElement
    docActionName = str(xmldoc.getElementsByTagName("RECIPE")[0].attributes["Name"].value)
    if not self.actionName:
      self.actionName = docActionName
    elif self.actionName != docActionName:
      return False
    self.recipeXML = recipe
    self.complexity = str(xmldoc.getElementsByTagName("RECIPE")[0].attributes["Type"].value).lower()
    # processing parameters
    paramDocNodes = xmldoc.getElementsByTagName("PARA")
    for paramDoc in paramDocNodes:
      param = ParamNode()
      param.loadRecipeXML(paramDoc)
      param.parent = self
      self.params.append(param)
    # processing subactions
    actionDocNodes = xmldoc.getElementsByTagName("SUBACT")
    for actionDoc in actionDocNodes:
      subPlan = PlanNode()
      subPlan.loadRecipeXML(actionDoc)
      subPlan.actionType = "ACTION"
      subPlan.parent = self
      if not subPlan.isOpt:
        self.subPlans.append(subPlan)
      else:
        self.subOptPlans.append(subPlan)
    return True
  
  def loadRecipeXML(self, actionDoc):
    """docstring for __loadPlanNode"""
    self.actionName = str(actionDoc.attributes["Name"].value)
    self.complexity = str(actionDoc.attributes["Type"].value).lower()
    if actionDoc.attributes.has_key("Optional"):
      self.isOpt = (str(actionDoc.attributes["Optional"].value) == "true")
    else:
      self.isOpt = True
                   
  def saveXML(self, doc):
    """docstring for saveXML"""
    actionNode = doc.createElement("action")
    actionNode.setAttribute("name", self.actionName)
    actionNode.setAttribute("type", self.actionType)
    actionNode.setAttribute("complexity", self.complexity)
    actionNode.setAttribute("phrase", self.phrase)
    actionNode.setAttribute("status", exec_status[self.mentalState.execStatus])
    beliefsNode = doc.createElement("beliefs")
    actionNode.appendChild(beliefsNode)
    intentionsNode = doc.createElement("intentions")
    actionNode.appendChild(intentionsNode)
    for agent in self.agents:
      beliefNode = doc.createElement("belief")
      beliefNode.setAttribute("agentId", agent.id)
      beliefNode.appendChild(doc.createTextNode(exec_status[agent.mentalState.execStatus]))
      beliefsNode.appendChild(beliefNode)
      intentionNode = doc.createElement("intention")
      intentionNode.setAttribute("agentId", agent.id)
      intentionNode.appendChild(doc.createTextNode(int_status[agent.mentalState.intention]))
      intentionsNode.appendChild(intentionNode)
    paramsNode = doc.createElement("parameters")
    actionNode.appendChild(paramsNode)
    for param in self.params:
      paramsNode.appendChild(param.saveXML(doc))
    subActionsNode = doc.createElement("subActions")
    actionNode.appendChild(subActionsNode)
    for subAction in self.subPlans:
      subActionsNode.appendChild(subAction.saveXML(doc))
    subOptActionsNode = doc.createElement("subOptActions")
    actionNode.appendChild(subOptActionsNode)
    for subOptAction in self.subOptPlans:
      subOptActionsNode.appendChild(subOptAction.saveXML(doc))
    return actionNode
    
  def searchParamByName(self, paramName):
    """docstring for searchParamByName"""
    parent = self.parent
    while parent:
      if isinstance(parent, PlanNode):
        for param in parent.params:
          if param.name == paramName:
            return param
      parent = parent.parent
    return None
    
class ParamNode():
  """docstring for ParamNode"""
  def __init__(self):
    self.properties = ("name", "type", "values", "multiple", "status", "parent", "subPlans", "subOptPlans")
    self.name = ""
    self.type = param_type_unknown
    self.values = []
    self.multiple = False
    self.status = param_status_notReady
    self.parent = None
    self.subPlans = []
    self.subOptPlans = []

  def __repr__(self):
    """docstring for __repr__"""
    return "(" + ",".join(["%s=%s" % (attr, getattr(self, attr)) for attr in self.properties if hasattr(self, attr)] ) + ")"
    
  def loadRecipeXML(self, paramDoc):
    """docstring for loadRecipeXML"""
    self.name = str(paramDoc.attributes["Name"].value)
    strParaType = str(paramDoc.attributes["Type"].value)
    if strParaType == "GeoType":
      self.type = param_type_geoType
    elif strParaType == "Integer":
      self.type = param_type_int
    elif strParaType == "Real":
      self.type = param_type_real
    elif strParaType == "String":
      self.type = param_type_text
    else:
      self.type = param_type_unknown  
    self.multiple = (str(paramDoc.attributes["Multiple"].value) == "true")
    for childNode in paramDoc.childNodes:
      if hasattr(childNode,"tagName") and childNode.tagName == "ID_PARA":
        subPlan = PlanNode()
        subPlan.loadRecipeXML(childNode)
        subPlan.actionType = "ID_PARA"
        subPlan.parent = self
        self.subOptPlans.append(subPlan)        
  
  def saveXML(self, doc):
    """docstring for saveXML"""
    paramNode = doc.createElement("parameter")
    paramNode.setAttribute("name", self.name)
    paramNode.setAttribute("type", param_type[self.type])
    paramNode.setAttribute("status", param_status[self.status])
    subActionsNode = doc.createElement("subActions")
    paramNode.appendChild(subActionsNode)
    for subAction in self.subPlans:
      subActionsNode.appendChild(subAction.saveXML(doc))
    subOptActionsNode = doc.createElement("subOptActions")
    paramNode.appendChild(subOptActionsNode)
    for subOptAction in self.subOptPlans:
      subOptActionsNode.appendChild(subOptAction.saveXML(doc))
    return paramNode
  
def main():
  pass
  
if __name__ == '__main__':
	main()