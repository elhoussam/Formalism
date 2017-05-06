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

      self.obj669=product(parent)
      self.obj669.preAction( self.RHS.CREATE )
      self.obj669.isGraphObjectVisual = True

      if(hasattr(self.obj669, '_setHierarchicalLink')):
        self.obj669._setHierarchicalLink(False)

      # MaxFlow
      self.obj669.MaxFlow.setValue(999999)

      # price
      self.obj669.price.setValue(0)

      # Name
      self.obj669.Name.setValue('OAF')

      # ReqFlow
      self.obj669.ReqFlow.setValue(0)

      self.obj669.GGLabel.setValue(1)
      self.obj669.graphClass_= graph_product
      if parent.genGraphics:
         new_obj = graph_product(100.0,80.0,self.obj669)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj669.graphObject_ = new_obj
      self.obj6690= AttrCalc()
      self.obj6690.Copy=ATOM3Boolean()
      self.obj6690.Copy.setValue(('Copy from LHS', 1))
      self.obj6690.Copy.config = 0
      self.obj6690.Specify=ATOM3Constraint()
      self.obj6690.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj669.GGset2Any['MaxFlow']= self.obj6690
      self.obj6691= AttrCalc()
      self.obj6691.Copy=ATOM3Boolean()
      self.obj6691.Copy.setValue(('Copy from LHS', 0))
      self.obj6691.Copy.config = 0
      self.obj6691.Specify=ATOM3Constraint()
      self.obj6691.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj669.GGset2Any['Name']= self.obj6691
      self.obj6692= AttrCalc()
      self.obj6692.Copy=ATOM3Boolean()
      self.obj6692.Copy.setValue(('Copy from LHS', 1))
      self.obj6692.Copy.config = 0
      self.obj6692.Specify=ATOM3Constraint()
      self.obj6692.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj669.GGset2Any['ReqFlow']= self.obj6692

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj669)
      self.obj669.postAction( self.RHS.CREATE )


   def condition(self, graphID, isograph, atom3i):
      return self.graphRewritingSystem.finalStat == 0
      

   def action(self, graphID, isograph, atom3i):
      self.graphRewritingSystem.finalStat = 1 
      

