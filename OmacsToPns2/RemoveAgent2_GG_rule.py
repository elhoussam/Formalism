# _ RemoveAgent2_GG_rule.py ____________________________________________________________________________
# File generated automatically by ATOM3. Graph Grammar Rule
# ___________________________________________________________________________________________
from GGrule import *
from CapableOf import *
from Goal import *
from require import *
from Agent import *
from Capabilitie import *
from Role import *
from ASG_omacs import *
from achieve import *
from posses import *
class RemoveAgent2_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 30)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_omacs(parent)

      self.obj2423=Agent(parent)
      self.obj2423.preAction( self.LHS.CREATE )
      self.obj2423.isGraphObjectVisual = True

      if(hasattr(self.obj2423, '_setHierarchicalLink')):
        self.obj2423._setHierarchicalLink(False)

      # price
      self.obj2423.price.setNone()

      # name
      self.obj2423.name.setValue('')
      self.obj2423.name.setNone()

      self.obj2423.GGLabel.setValue(1)
      self.obj2423.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(160.0,60.0,self.obj2423)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj2423.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj2423)
      self.obj2423.postAction( self.LHS.CREATE )


      self.RHS = ASG_omacs(parent)


   def condition(self, graphID, isograph, atom3i):
      return self.graphRewritingSystem.finalStat > 20 
      

   def action(self, graphID, isograph, atom3i):
      pass

