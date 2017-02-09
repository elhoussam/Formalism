# _ Omacs2Pns_GG_exec.py ____________________________________________________________________________
# Omacs2Pns : a class that subclasifies GraphGrammar. File generated automatically by ATOM3.
# ___________________________________________________________________________________________
from GraphGrammar import *
from OpUnit4AR_GG_rule import *
from Agent2Raw_GG_rule import *
from Goal2Matr_GG_rule import *
from LinkRaw2AR_GG_rule import *
from GenAux1_GG_rule import *
from LinkAux1_GG_rule import *
from GenOaf_GG_rule import *
from OpUnit4M_OAF_GG_rule import *
class Omacs2Pns_GG_exec (GraphGrammar):
   def __init__ (self, parent):
      GraphGrammar.__init__(self, [OpUnit4AR_GG_rule(parent) , Agent2Raw_GG_rule(parent) , Goal2Matr_GG_rule(parent) , LinkRaw2AR_GG_rule(parent) , GenAux1_GG_rule(parent) , LinkAux1_GG_rule(parent) , GenOaf_GG_rule(parent) , OpUnit4M_OAF_GG_rule(parent)])
   def initialAction(self, graph):
      # Template code for an initial action (a full host graph traversal)
      
      #idInt = 0
      #for nodeType in graph.listNodes.keys():
      #    for node in graph.listNodes[nodeType]:
      #      # Prints the class name of all nodes in graph
      #      print node.__class__.__name__ 
      #
      #      # This part assumes that *ALL* nodes in graph have ATOM3 Integer 
      #      # attribute called "id" and that this attribute is in the visual icon
      #      # NOTE: setGenValue() sets the semantic value, updates visually, and
      #      # catches attribute name errors and displays correct alternatives
      #      node.setGenValue('id', idInt)
      #      idInt += 1
      self.rewritingSystem.Start = 0 
      
      

   def finalAction(self, graph):
      pass

importedModules = ['OpUnit4AR_GG_rule', 'Agent2Raw_GG_rule', 'Goal2Matr_GG_rule', 'LinkRaw2AR_GG_rule', 'GenAux1_GG_rule', 'LinkAux1_GG_rule', 'GenOaf_GG_rule', 'OpUnit4M_OAF_GG_rule']

