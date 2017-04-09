# _ Omacs2Pns_GG_exec.py ____________________________________________________________________________
# Omacs2Pns : a class that subclasifies GraphGrammar. File generated automatically by ATOM3.
# ___________________________________________________________________________________________
from GraphGrammar import *
from Agent2RoleLink1_GG_rule import *
from Agent2RoleLink2_GG_rule import *
from Agent2RoleLink3_GG_rule import *
from TransAgent2Raw_GG_rule import *
from TransLinkAR2OpUnit_GG_rule import *
from TransGoal2Mat_GG_rule import *
from CreatLinkRaw2AR_GG_rule import *
from CreateFinalStat_GG_rule import *
from CreateLinkMatr2OAF_GG_rule import *
from CreateMat_ARG_GG_rule import *
from CreateLinkMat_ARG2Goal_GG_rule import *
from CreateLinkAR2Mat_GG_rule import *
from AssignPrice4Raw_GG_rule import *
from AssignCost4AR_GG_rule import *
from RemoveGoal_GG_rule import *
from RemoveAgent_GG_rule import *
from RemoveCap_GG_rule import *
from RemoveRole_GG_rule import *
class Omacs2Pns_GG_exec (GraphGrammar):
   def __init__ (self, parent):
      GraphGrammar.__init__(self, [Agent2RoleLink1_GG_rule(parent) , Agent2RoleLink2_GG_rule(parent) , Agent2RoleLink3_GG_rule(parent) , TransAgent2Raw_GG_rule(parent) , TransLinkAR2OpUnit_GG_rule(parent) , TransGoal2Mat_GG_rule(parent) , CreatLinkRaw2AR_GG_rule(parent) , CreateFinalStat_GG_rule(parent) , CreateLinkMatr2OAF_GG_rule(parent) , CreateMat_ARG_GG_rule(parent) , CreateLinkMat_ARG2Goal_GG_rule(parent) , CreateLinkAR2Mat_GG_rule(parent) , AssignPrice4Raw_GG_rule(parent) , AssignCost4AR_GG_rule(parent) , RemoveGoal_GG_rule(parent) , RemoveAgent_GG_rule(parent) , RemoveCap_GG_rule(parent) , RemoveRole_GG_rule(parent)])
   def initialAction(self, graph):
      print 'Version 1Hahaha '
      self.rewritingSystem.finalStat = 0
      self.rewritingSystem.Dictag = {}
      self.rewritingSystem.Dictro = {}
      AgentDict = {}
      AgentDict2 = {}
      RoleDict = {} 
      RoleDict2 = {} 
      Posses  = {}
      Achiev = {}
      atom3i = self.rewritingSystem.parent
      for nodeType in atom3i.ASGroot.listNodes.keys():
         for node in atom3i.ASGroot.listNodes[nodeType]:
             if node.__class__.__name__ == 'Agent' : 
                 nodeName = node.name.getValue()
                 AgentDict[nodeName]={} 
                 AgentDict2[nodeName]=[]
                 for link in node.out_connections_ : 
                     if hasattr(link,'rate') :
                         for nodes in link.out_connections_ :
      
                            AgentDict[nodeName][nodes.name.getValue()]=link.rate.getValue()
                            AgentDict2[nodeName].append(nodes.name.getValue())
                 #AgentDict[nodeName]= AgentDict[nodeName]/ len(node.out_connections_)
             elif node.__class__.__name__ == 'Role' :
                 nodeName = node.name.getValue()
                 RoleDict[nodeName]={} 
                 RoleDict2[nodeName]=[]
                 lisst = RoleDict[nodeName]
                 for link in node.out_connections_ : 
                     for nodes in link.out_connections_ :
                         if hasattr(link,'rate'):        RoleDict[nodeName][nodes.name.getValue()]=link.rate.getValue()
                         else :  RoleDict2[nodeName].append(nodes.name.getValue())
      
                               #lisst.append( {nodes.name.getValue():link.rate.getValue()} ) 
                 #RoleDict[nodeName] = lisst  
      
      print '[DicAG]Agent Dict for his Value  : '+str(AgentDict)
      print 'Agent dict 2 '+str(AgentDict2)
      print 'Role Dict for his Value  : '+str(RoleDict)
      print 'Role Dict2 for his Value  : '+str(RoleDict2)
       # all these line new 
      for key , val in AgentDict2.items() :
         val.sort()
      for key , val in RoleDict2.items() :
         val.sort()
      for key , val in AgentDict2.items() :
          for key2 , val2 in RoleDict2.items() :
              v = ''.join(val)
              v2 = ''.join(val2)
              if  v2 in v : 
                 s = 0
                 #print str(key) +' Can Play '+str(key2)
                 for i in val2 : 
                     #if type(AgentDict[key]).__name__ != 'float':
                     #print '  '+str(i)   
                     s+=AgentDict[key][i] 
                 AgentDict[key][key2] = s/len(val2)
                 Posses[str(key)+' '+str(key2)]=s*len(val2) #Just Equation for the cost of OpUnit
                 print key + ' :'+key2+' Can Achiev '+str(RoleDict[key2])
      
                 #print 'AgentDict : '+str(AgentDict)	 
      for key , val in AgentDict2.items() :
           print str(key) +' Rate '+str( AgentDict[key] )		
       
      print Posses
      self.rewritingSystem.Dictag = AgentDict
      self.rewritingSystem.Dictro = RoleDict
      ##
      
      

   def finalAction(self, graph):
      pass

importedModules = ['Agent2RoleLink1_GG_rule', 'Agent2RoleLink2_GG_rule', 'Agent2RoleLink3_GG_rule', 'TransAgent2Raw_GG_rule', 'TransLinkAR2OpUnit_GG_rule', 'TransGoal2Mat_GG_rule', 'CreatLinkRaw2AR_GG_rule', 'CreateFinalStat_GG_rule', 'CreateLinkMatr2OAF_GG_rule', 'CreateMat_ARG_GG_rule', 'CreateLinkMat_ARG2Goal_GG_rule', 'CreateLinkAR2Mat_GG_rule', 'AssignPrice4Raw_GG_rule', 'AssignCost4AR_GG_rule', 'RemoveGoal_GG_rule', 'RemoveAgent_GG_rule', 'RemoveCap_GG_rule', 'RemoveRole_GG_rule']

