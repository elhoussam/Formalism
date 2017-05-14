# _ RemoveRole2_GG_rule.py ____________________________________________________________________________
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
class RemoveRole2_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 29)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_omacs(parent)

      self.obj2255=Role(parent)
      self.obj2255.preAction( self.LHS.CREATE )
      self.obj2255.isGraphObjectVisual = True

      if(hasattr(self.obj2255, '_setHierarchicalLink')):
        self.obj2255._setHierarchicalLink(False)

      # name
      self.obj2255.name.setValue('')
      self.obj2255.name.setNone()

      self.obj2255.GGLabel.setValue(1)
      self.obj2255.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(100.0,60.0,self.obj2255)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj2255.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj2255)
      self.obj2255.postAction( self.LHS.CREATE )


      self.RHS = ASG_omacs(parent)


   def condition(self, graphID, isograph, atom3i):
      return self.graphRewritingSystem.finalStat > 20 
      

   def action(self, graphID, isograph, atom3i):
      pass

