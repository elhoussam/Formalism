# _ CreateFinalStat_GG_rule.py ____________________________________________________________________________
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
from intoProduct import *
from operatingUnit import *
from metarial import *
from rawMaterial import *
from fromMaterial import *
from fromRaw import *
from ASG_pns2 import *
from intoMaterial import *
from product import *
class CreateFinalStat_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 13)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_omacss(parent)


      self.RHS = ASG_omacss(parent)
      self.RHS.merge(ASG_pns2(parent))

      self.obj261=product(parent)
      self.obj261.preAction( self.RHS.CREATE )
      self.obj261.isGraphObjectVisual = True

      if(hasattr(self.obj261, '_setHierarchicalLink')):
        self.obj261._setHierarchicalLink(False)

      # Name
      self.obj261.Name.setValue('OAF')

      self.obj261.GGLabel.setValue(1)
      self.obj261.graphClass_= graph_product
      if parent.genGraphics:
         new_obj = graph_product(180.0,40.0,self.obj261)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj261.graphObject_ = new_obj
      self.obj2610= AttrCalc()
      self.obj2610.Copy=ATOM3Boolean()
      self.obj2610.Copy.setValue(('Copy from LHS', 0))
      self.obj2610.Copy.config = 0
      self.obj2610.Specify=ATOM3Constraint()
      self.obj2610.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj261.GGset2Any['Name']= self.obj2610

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj261)
      self.obj261.postAction( self.RHS.CREATE )


   def condition(self, graphID, isograph, atom3i):
      return self.graphRewritingSystem.finalStat == 0
      
      
      
      
      
      
      

   def action(self, graphID, isograph, atom3i):
      self.graphRewritingSystem.finalStat = 1 
      
      
      
      
      
      
      
      
      
      

