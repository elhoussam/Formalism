# _ RemoveCap_GG_rule.py ____________________________________________________________________________
# File generated automatically by ATOM3. Graph Grammar Rule
# ___________________________________________________________________________________________
from GGrule import *
from Capabilitie import *
from rawMaterial import *
from Goal import *
from ASG_pns import *
from operatingUnit import *
from metarial import *
from product import *
from Agent import *
from fromMaterial import *
from CapableOf import *
from intoProduct import *
from Role import *
from fromRaw import *
from intoMaterial import *
from ASG_omacs import *
from require import *
from achieve import *
from posses import *
class RemoveCap_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 27)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_pns(parent)
      self.LHS.merge(ASG_omacs(parent))

      self.obj1841=Capabilitie(parent)
      self.obj1841.preAction( self.LHS.CREATE )
      self.obj1841.isGraphObjectVisual = True

      if(hasattr(self.obj1841, '_setHierarchicalLink')):
        self.obj1841._setHierarchicalLink(False)

      # name
      self.obj1841.name.setValue('')
      self.obj1841.name.setNone()

      self.obj1841.GGLabel.setValue(1)
      self.obj1841.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(220.0,80.0,self.obj1841)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1841.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1841)
      self.obj1841.postAction( self.LHS.CREATE )


      self.RHS = ASG_pns(parent)


   def condition(self, graphID, isograph, atom3i):
      return self.graphRewritingSystem.finalStat > 20 
      

   def action(self, graphID, isograph, atom3i):
      pass

