# _ RemoveCap_GG_rule.py ____________________________________________________________________________
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
class RemoveCap_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 27)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_omacss(parent)

      self.obj431=Capabilitie(parent)
      self.obj431.preAction( self.LHS.CREATE )
      self.obj431.isGraphObjectVisual = True

      if(hasattr(self.obj431, '_setHierarchicalLink')):
        self.obj431._setHierarchicalLink(False)

      # name
      self.obj431.name.setValue('')
      self.obj431.name.setNone()

      self.obj431.GGLabel.setValue(1)
      self.obj431.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(200.0,100.0,self.obj431)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj431.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj431)
      self.obj431.postAction( self.LHS.CREATE )


      self.RHS = ASG_omacss(parent)


   def condition(self, graphID, isograph, atom3i):
      return self.graphRewritingSystem.finalStat > 20 
      
      

   def action(self, graphID, isograph, atom3i):
      pass

