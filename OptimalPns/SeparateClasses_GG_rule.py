# _ SeparateClasses_GG_rule.py ____________________________________________________________________________
# File generated automatically by ATOM3. Graph Grammar Rule
# ___________________________________________________________________________________________
from GGrule import *
from rawMaterial import *
from ASG_pns import *
from operatingUnit import *
from metarial import *
from product import *
from fromMaterial import *
from intoProduct import *
from fromRaw import *
from intoMaterial import *
class SeparateClasses_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 2)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_pns(parent)


      self.RHS = ASG_pns(parent)


   def condition(self, graphID, isograph, atom3i):
      return self.graphRewritingSystem.finalStat == 0
      

   def action(self, graphID, isograph, atom3i):
      # import needed packages
      import OptimalPNS_GG_exec 
      import itertools
      # print our data Struct
      print OptimalPNS_GG_exec.Agentdict
      print OptimalPNS_GG_exec.Agentnode
      print OptimalPNS_GG_exec.dictWord
      localcounter = 1
      # start extract information from data Struct
      for key in OptimalPNS_GG_exec.Agentdict.keys() : 
       listStuf = OptimalPNS_GG_exec.Agentnode[key]
       print key
       for L in range(1, len(listStuf)+1):
        for subset in itertools.combinations(listStuf, L):
         print(subset)
         list2 = [] #list( subset )
         for T in subset :
          list2.append( OptimalPNS_GG_exec.dictWord[T] ) # remplate all keys with corresp node name
         print str(localcounter)+":"+str(list2)
         localcounter+=1 
      self.graphRewritingSystem.finalStat = 1 
      
      

