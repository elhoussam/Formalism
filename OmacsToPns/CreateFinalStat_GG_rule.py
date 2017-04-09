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

      self.obj197=product(parent)
      self.obj197.preAction( self.RHS.CREATE )
      self.obj197.isGraphObjectVisual = True

      if(hasattr(self.obj197, '_setHierarchicalLink')):
        self.obj197._setHierarchicalLink(False)

      # MaxFlow
      self.obj197.MaxFlow.setValue(999999)

      # price
      self.obj197.price.setValue(0)

      # Name
      self.obj197.Name.setValue('OAF')

      # ReqFlow
      self.obj197.ReqFlow.setValue(0)

      self.obj197.GGLabel.setValue(1)
      self.obj197.graphClass_= graph_product
      if parent.genGraphics:
         new_obj = graph_product(100.0,80.0,self.obj197)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj197.graphObject_ = new_obj
      self.obj1970= AttrCalc()
      self.obj1970.Copy=ATOM3Boolean()
      self.obj1970.Copy.setValue(('Copy from LHS', 1))
      self.obj1970.Copy.config = 0
      self.obj1970.Specify=ATOM3Constraint()
      self.obj1970.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj197.GGset2Any['MaxFlow']= self.obj1970
      self.obj1971= AttrCalc()
      self.obj1971.Copy=ATOM3Boolean()
      self.obj1971.Copy.setValue(('Copy from LHS', 0))
      self.obj1971.Copy.config = 0
      self.obj1971.Specify=ATOM3Constraint()
      self.obj1971.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj197.GGset2Any['Name']= self.obj1971
      self.obj1972= AttrCalc()
      self.obj1972.Copy=ATOM3Boolean()
      self.obj1972.Copy.setValue(('Copy from LHS', 1))
      self.obj1972.Copy.config = 0
      self.obj1972.Specify=ATOM3Constraint()
      self.obj1972.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj197.GGset2Any['ReqFlow']= self.obj1972

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj197)
      self.obj197.postAction( self.RHS.CREATE )


   def condition(self, graphID, isograph, atom3i):
      return self.graphRewritingSystem.finalStat == 0
      

   def action(self, graphID, isograph, atom3i):
      self.graphRewritingSystem.finalStat = 1 
      

