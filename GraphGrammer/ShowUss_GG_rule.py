# _ ShowUss_GG_rule.py ____________________________________________________________________________
# File generated automatically by ATOM3. Graph Grammar Rule
# ___________________________________________________________________________________________
from GGrule import *
from CapableOf import *
from Goal import *
from ASG_omacss import *
from Agent import *
from Capabilitie import *
from Role import *
from requir import *
from achieve import *
from posses import *
class ShowUss_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 1)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_omacss(parent)


      self.RHS = ASG_omacss(parent)


   def condition(self, graphID, isograph, atom3i):
      atom3i = self.rewritingSystem.parent
      for nodeType in atom3i.ASGroot.listNodes.keys():
         for node in atom3i.ASGroot.listNodes[nodeType]:
             if hasattr( node , 'name' ) : 
                print node.name.getValue()
             else 
                print node.Name.getValue()
      

   def action(self, graphID, isograph, atom3i):
      pass

