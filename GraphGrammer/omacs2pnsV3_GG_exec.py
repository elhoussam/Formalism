# _ omacs2pnsV3_GG_exec.py ____________________________________________________________________________
# omacs2pnsV3 : a class that subclasifies GraphGrammar. File generated automatically by ATOM3.
# ___________________________________________________________________________________________
from GraphGrammar import *
from linkAgent2Role1_GG_rule import *
from linkAgent2Role2_GG_rule import *
from linkAgent2Role3_GG_rule import *
from TransformAGent2Raw_GG_rule import *
from TransformLinkAR2OpUnit_GG_rule import *
from TransformGoal2Mat_GG_rule import *
from CreatLinkRaw2AR_GG_rule import *
from CreateFinalStat_GG_rule import *
from CreateLinkMatr2OAF_GG_rule import *
from CreateMat_ARG_GG_rule import *
from CreateLinkMat_ARG2Goal_GG_rule import *
from CreateLinkAR2Mat_GG_rule import *
from AssigneValuestoLinks1_GG_rule import *
from RemoveGoals_GG_rule import *
from RemoveAGent_GG_rule import *
from RemoveCap_GG_rule import *
from RemoveRolez_GG_rule import *
class omacs2pnsV3_GG_exec (GraphGrammar):
   def __init__ (self, parent):
      GraphGrammar.__init__(self, [linkAgent2Role1_GG_rule(parent) , linkAgent2Role2_GG_rule(parent) , linkAgent2Role3_GG_rule(parent) , TransformAGent2Raw_GG_rule(parent) , TransformLinkAR2OpUnit_GG_rule(parent) , TransformGoal2Mat_GG_rule(parent) , CreatLinkRaw2AR_GG_rule(parent) , CreateFinalStat_GG_rule(parent) , CreateLinkMatr2OAF_GG_rule(parent) , CreateMat_ARG_GG_rule(parent) , CreateLinkMat_ARG2Goal_GG_rule(parent) , CreateLinkAR2Mat_GG_rule(parent) , AssigneValuestoLinks1_GG_rule(parent) , RemoveGoals_GG_rule(parent) , RemoveAGent_GG_rule(parent) , RemoveCap_GG_rule(parent) , RemoveRolez_GG_rule(parent)])
   def initialAction(self, graph):
      print 'Version 19:02 '
      self.rewritingSystem.finalStat = 0
      self.rewritingSystem.Dictag = {}
      self.rewritingSystem.Dictro = {}
      AgentDict = {}
      RoleDict = {} 
      atom3i = self.rewritingSystem.parent
      for nodeType in atom3i.ASGroot.listNodes.keys():
         for node in atom3i.ASGroot.listNodes[nodeType]:
             if node.__class__.__name__ == 'Agent' : 
                 nodeName = node.name.getValue()
                 AgentDict[nodeName]=0  
                 for link in node.out_connections_ : 
                     if hasattr(link,'rate') : 
                         AgentDict[nodeName] += link.rate.getValue()   
                 AgentDict[nodeName]= AgentDict[nodeName]/ len(node.out_connections_)
             elif node.__class__.__name__ == 'Role' :
                 nodeName = node.name.getValue()
                 RoleDict[nodeName]={} 
                 lisst = RoleDict[nodeName]
                 for link in node.out_connections_ : 
                     if hasattr(link,'rate') :
                         for nodes in link.out_connections_ :  
                          RoleDict[nodeName][nodes.name.getValue()]=link.rate.getValue()
                             #lisst.append( {nodes.name.getValue():link.rate.getValue()} ) 
                 #RoleDict[nodeName] = lisst  
      
      print 'Agent Dict for his Value  : '+str(AgentDict)
      print 'Role Dict for his Value  : '+str(RoleDict)
      
      self.rewritingSystem.Dictag = AgentDict
      self.rewritingSystem.Dictro = RoleDict
      
      

   def finalAction(self, graph):
      pass

importedModules = ['linkAgent2Role1_GG_rule', 'linkAgent2Role2_GG_rule', 'linkAgent2Role3_GG_rule', 'TransformAGent2Raw_GG_rule', 'TransformLinkAR2OpUnit_GG_rule', 'TransformGoal2Mat_GG_rule', 'CreatLinkRaw2AR_GG_rule', 'CreateFinalStat_GG_rule', 'CreateLinkMatr2OAF_GG_rule', 'CreateMat_ARG_GG_rule', 'CreateLinkMat_ARG2Goal_GG_rule', 'CreateLinkAR2Mat_GG_rule', 'AssigneValuestoLinks1_GG_rule', 'RemoveGoals_GG_rule', 'RemoveAGent_GG_rule', 'RemoveCap_GG_rule', 'RemoveRolez_GG_rule']
