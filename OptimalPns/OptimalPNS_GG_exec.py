# _ OptimalPNS_GG_exec.py ____________________________________________________________________________
# OptimalPNS : a class that subclasifies GraphGrammar. File generated automatically by ATOM3.
# ___________________________________________________________________________________________
from GraphGrammar import *
from ComputeSol_GG_rule import *
from SeparateClasses_GG_rule import *
from MarkOpUnit1_GG_rule import *
from MarkOpUnit2_GG_rule import *
class OptimalPNS_GG_exec (GraphGrammar):
   def __init__ (self, parent):
      GraphGrammar.__init__(self, [ComputeSol_GG_rule(parent) , SeparateClasses_GG_rule(parent) , MarkOpUnit1_GG_rule(parent) , MarkOpUnit2_GG_rule(parent)])
   def initialAction(self, graph):
      self.rewritingSystem.finalStat = 0
      global nSolution 
      nSolution = 0
      global Agentdict
      global Agentnode
      global dictWord
      global ind
      ind = 0
      dictWord= {}
      Agentdict = {}
      Agentnode = {}
      
      

   def finalAction(self, graph):
      # import needed packages
      import OptimalPNS_GG_exec 
      import math 
      # print our data Struct
      print OptimalPNS_GG_exec.Agentdict 
      totalSolution = 0 
      # start extract information from data Struct
      for key in OptimalPNS_GG_exec.Agentdict.keys() :
       totalSolution += math.pow(2, OptimalPNS_GG_exec.Agentdict[key] ) -1
      print "Finish "+str( totalSolution ) 
      
      

importedModules = ['ComputeSol_GG_rule', 'SeparateClasses_GG_rule', 'MarkOpUnit1_GG_rule', 'MarkOpUnit2_GG_rule']

