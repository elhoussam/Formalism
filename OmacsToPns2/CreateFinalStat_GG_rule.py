# _ CreateFinalStat_GG_rule.py ____________________________________________________________________________
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
class CreateFinalStat_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 13)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_pns(parent)


      self.RHS = ASG_pns(parent)

      self.obj1670=product(parent)
      self.obj1670.preAction( self.RHS.CREATE )
      self.obj1670.isGraphObjectVisual = True

      if(hasattr(self.obj1670, '_setHierarchicalLink')):
        self.obj1670._setHierarchicalLink(False)

      # MaxFlow
      self.obj1670.MaxFlow.setValue(999999)

      # price
      self.obj1670.price.setValue(0)

      # Name
      self.obj1670.Name.setValue('OAF')

      # ReqFlow
      self.obj1670.ReqFlow.setValue(0)

      self.obj1670.GGLabel.setValue(1)
      self.obj1670.graphClass_= graph_product
      if parent.genGraphics:
         new_obj = graph_product(100.0,80.0,self.obj1670)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1670.graphObject_ = new_obj
      self.obj16700= AttrCalc()
      self.obj16700.Copy=ATOM3Boolean()
      self.obj16700.Copy.setValue(('Copy from LHS', 1))
      self.obj16700.Copy.config = 0
      self.obj16700.Specify=ATOM3Constraint()
      self.obj16700.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1670.GGset2Any['MaxFlow']= self.obj16700
      self.obj16701= AttrCalc()
      self.obj16701.Copy=ATOM3Boolean()
      self.obj16701.Copy.setValue(('Copy from LHS', 0))
      self.obj16701.Copy.config = 0
      self.obj16701.Specify=ATOM3Constraint()
      self.obj16701.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1670.GGset2Any['Name']= self.obj16701
      self.obj16702= AttrCalc()
      self.obj16702.Copy=ATOM3Boolean()
      self.obj16702.Copy.setValue(('Copy from LHS', 1))
      self.obj16702.Copy.config = 0
      self.obj16702.Specify=ATOM3Constraint()
      self.obj16702.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1670.GGset2Any['ReqFlow']= self.obj16702

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1670)
      self.obj1670.postAction( self.RHS.CREATE )


   def condition(self, graphID, isograph, atom3i):
      return self.graphRewritingSystem.finalStat == 0
      

   def action(self, graphID, isograph, atom3i):
      self.graphRewritingSystem.finalStat = 1 
      

