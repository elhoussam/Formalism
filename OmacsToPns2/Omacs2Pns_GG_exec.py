# _ Omacs2Pns_GG_exec.py ____________________________________________________________________________
# Omacs2Pns : a class that subclasifies GraphGrammar. File generated automatically by ATOM3.
# ___________________________________________________________________________________________
from GraphGrammar import *
from Agent2RoleLink1_GG_rule import *
from Agent2RoleLink2_GG_rule import *
from Agent2RoleLink3_GG_rule import *
from CollectInf1_GG_rule import *
from CollectInf2_GG_rule import *
from CollectInf3_GG_rule import *
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
      GraphGrammar.__init__(self, [Agent2RoleLink1_GG_rule(parent) , Agent2RoleLink2_GG_rule(parent) , Agent2RoleLink3_GG_rule(parent) , CollectInf1_GG_rule(parent) , CollectInf2_GG_rule(parent) , CollectInf3_GG_rule(parent) , TransAgent2Raw_GG_rule(parent) , TransLinkAR2OpUnit_GG_rule(parent) , TransGoal2Mat_GG_rule(parent) , CreatLinkRaw2AR_GG_rule(parent) , CreateFinalStat_GG_rule(parent) , CreateLinkMatr2OAF_GG_rule(parent) , CreateMat_ARG_GG_rule(parent) , CreateLinkMat_ARG2Goal_GG_rule(parent) , CreateLinkAR2Mat_GG_rule(parent) , AssignPrice4Raw_GG_rule(parent) , AssignCost4AR_GG_rule(parent) , RemoveGoal_GG_rule(parent) , RemoveAgent_GG_rule(parent) , RemoveCap_GG_rule(parent) , RemoveRole_GG_rule(parent)])
   def initialAction(self, graph):
      print 'Version 1Hahaha '
      self.rewritingSystem.finalStat = 0
      self.rewritingSystem.Dictag = {}
      self.rewritingSystem.Dictro = {}
       
      
      

   def finalAction(self, graph):
      pass

importedModules = ['Agent2RoleLink1_GG_rule', 'Agent2RoleLink2_GG_rule', 'Agent2RoleLink3_GG_rule', 'CollectInf1_GG_rule', 'CollectInf2_GG_rule', 'CollectInf3_GG_rule', 'TransAgent2Raw_GG_rule', 'TransLinkAR2OpUnit_GG_rule', 'TransGoal2Mat_GG_rule', 'CreatLinkRaw2AR_GG_rule', 'CreateFinalStat_GG_rule', 'CreateLinkMatr2OAF_GG_rule', 'CreateMat_ARG_GG_rule', 'CreateLinkMat_ARG2Goal_GG_rule', 'CreateLinkAR2Mat_GG_rule', 'AssignPrice4Raw_GG_rule', 'AssignCost4AR_GG_rule', 'RemoveGoal_GG_rule', 'RemoveAgent_GG_rule', 'RemoveCap_GG_rule', 'RemoveRole_GG_rule']

