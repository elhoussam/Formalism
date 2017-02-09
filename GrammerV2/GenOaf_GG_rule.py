# _ GenOaf_GG_rule.py ____________________________________________________________________________
# File generated automatically by ATOM3. Graph Grammar Rule
# ___________________________________________________________________________________________
from GGrule import *
from rawMaterial import *
from intoProduct import *
from operatingUnit import *
from metarial import *
from product import *
from fromMaterial import *
from fromRaw import *
from ASG_pns2 import *
from intoMaterial import *
class GenOaf_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 50)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_pns2(parent)


      self.RHS = ASG_pns2(parent)

      self.obj160=product(parent)
      self.obj160.preAction( self.RHS.CREATE )
      self.obj160.isGraphObjectVisual = True

      if(hasattr(self.obj160, '_setHierarchicalLink')):
        self.obj160._setHierarchicalLink(False)

      # Name
      self.obj160.Name.setValue('')
      self.obj160.Name.setNone()

      self.obj160.GGLabel.setValue(1)
      self.obj160.graphClass_= graph_product
      if parent.genGraphics:
         new_obj = graph_product(200.0,100.0,self.obj160)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj160.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj160)
      self.obj160.postAction( self.RHS.CREATE )


   def condition(self, graphID, isograph, atom3i):
      # If you want to apply this rule at most once on asingle host graph node, 
      # then uncomment the next two lines. Change the default GG label (1) if needed.
      
      # Make sure to enable the ACTION code as well
      # And to use the same label & unique name in the ACTION
      # WARNING: _uniqueName22 is not guaranteed to be unique (so change it, be safe!)
      
      #node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      #return not hasattr(node, "_uniqueName22")
      return self.graphRewritingSystem.Start == 0
      
      

   def action(self, graphID, isograph, atom3i):
      # If you want to apply this rule at most once on asingle host graph node, 
      # then uncomment the next two lines. Change the default GG label (1) if needed.
      
      # Make sure to enable the CONDITION code as well
      # And to use the same label & unique name in the ACTION
      # WARNING: _uniqueName22 is not guaranteed to be unique (so change it, be safe!)
      
      #node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      #node._uniqueName22 = True
       self.graphRewritingSystem.Start = 1
      
      

