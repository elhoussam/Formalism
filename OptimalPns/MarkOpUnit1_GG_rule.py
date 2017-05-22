# _ MarkOpUnit1_GG_rule.py ____________________________________________________________________________
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
class MarkOpUnit1_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 3)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_pns(parent)

      self.obj127=rawMaterial(parent)
      self.obj127.preAction( self.LHS.CREATE )
      self.obj127.isGraphObjectVisual = True

      if(hasattr(self.obj127, '_setHierarchicalLink')):
        self.obj127._setHierarchicalLink(False)

      # MaxFlow
      self.obj127.MaxFlow.setNone()

      # price
      self.obj127.price.setNone()

      # Name
      self.obj127.Name.setValue('')
      self.obj127.Name.setNone()

      # ReqFlow
      self.obj127.ReqFlow.setNone()

      self.obj127.GGLabel.setValue(1)
      self.obj127.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(40.0,20.0,self.obj127)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj127.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj127)
      self.obj127.postAction( self.LHS.CREATE )

      self.obj128=metarial(parent)
      self.obj128.preAction( self.LHS.CREATE )
      self.obj128.isGraphObjectVisual = True

      if(hasattr(self.obj128, '_setHierarchicalLink')):
        self.obj128._setHierarchicalLink(False)

      # MaxFlow
      self.obj128.MaxFlow.setNone()

      # price
      self.obj128.price.setNone()

      # Name
      self.obj128.Name.setValue('')
      self.obj128.Name.setNone()

      # ReqFlow
      self.obj128.ReqFlow.setNone()

      self.obj128.GGLabel.setValue(3)
      self.obj128.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(360.0,140.0,self.obj128)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj128.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj128)
      self.obj128.postAction( self.LHS.CREATE )

      self.obj129=operatingUnit(parent)
      self.obj129.preAction( self.LHS.CREATE )
      self.obj129.isGraphObjectVisual = True

      if(hasattr(self.obj129, '_setHierarchicalLink')):
        self.obj129._setHierarchicalLink(False)

      # OperCostProp
      self.obj129.OperCostProp.setNone()

      # name
      self.obj129.name.setValue('')
      self.obj129.name.setNone()

      # OperCostFix
      self.obj129.OperCostFix.setNone()

      self.obj129.GGLabel.setValue(2)
      self.obj129.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(180.0,100.0,self.obj129)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj129.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj129)
      self.obj129.postAction( self.LHS.CREATE )

      self.obj130=fromRaw(parent)
      self.obj130.preAction( self.LHS.CREATE )
      self.obj130.isGraphObjectVisual = True

      if(hasattr(self.obj130, '_setHierarchicalLink')):
        self.obj130._setHierarchicalLink(False)

      # rate
      self.obj130.rate.setNone()

      self.obj130.GGLabel.setValue(4)
      self.obj130.graphClass_= graph_fromRaw
      if parent.genGraphics:
         new_obj = graph_fromRaw(183.0,77.75,self.obj130)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj130.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj130)
      self.obj130.postAction( self.LHS.CREATE )

      self.obj131=intoMaterial(parent)
      self.obj131.preAction( self.LHS.CREATE )
      self.obj131.isGraphObjectVisual = True

      if(hasattr(self.obj131, '_setHierarchicalLink')):
        self.obj131._setHierarchicalLink(False)

      # rate
      self.obj131.rate.setNone()

      self.obj131.GGLabel.setValue(5)
      self.obj131.graphClass_= graph_intoMaterial
      if parent.genGraphics:
         new_obj = graph_intoMaterial(258.75,158.0,self.obj131)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj131.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj131)
      self.obj131.postAction( self.LHS.CREATE )

      self.obj127.out_connections_.append(self.obj130)
      self.obj130.in_connections_.append(self.obj127)
      self.obj127.graphObject_.pendingConnections.append((self.obj127.graphObject_.tag, self.obj130.graphObject_.tag, [64.0, 76.0, 144.0, 69.0, 183.0, 77.75], 2, True))
      self.obj129.out_connections_.append(self.obj131)
      self.obj131.in_connections_.append(self.obj129)
      self.obj129.graphObject_.pendingConnections.append((self.obj129.graphObject_.tag, self.obj131.graphObject_.tag, [199.0, 118.0, 222.0, 142.0, 258.75, 158.0], 2, True))
      self.obj130.out_connections_.append(self.obj129)
      self.obj129.in_connections_.append(self.obj130)
      self.obj130.graphObject_.pendingConnections.append((self.obj130.graphObject_.tag, self.obj129.graphObject_.tag, [200.0, 111.0, 222.0, 86.5, 183.0, 77.75], 2, True))
      self.obj131.out_connections_.append(self.obj128)
      self.obj128.in_connections_.append(self.obj131)
      self.obj131.graphObject_.pendingConnections.append((self.obj131.graphObject_.tag, self.obj128.graphObject_.tag, [366.0, 182.0, 295.5, 174.0, 258.75, 158.0], 2, True))

      self.RHS = ASG_pns(parent)

      self.obj133=rawMaterial(parent)
      self.obj133.preAction( self.RHS.CREATE )
      self.obj133.isGraphObjectVisual = True

      if(hasattr(self.obj133, '_setHierarchicalLink')):
        self.obj133._setHierarchicalLink(False)

      # MaxFlow
      self.obj133.MaxFlow.setNone()

      # price
      self.obj133.price.setNone()

      # Name
      self.obj133.Name.setValue('')
      self.obj133.Name.setNone()

      # ReqFlow
      self.obj133.ReqFlow.setNone()

      self.obj133.GGLabel.setValue(1)
      self.obj133.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(40.0,20.0,self.obj133)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj133.graphObject_ = new_obj
      self.obj1330= AttrCalc()
      self.obj1330.Copy=ATOM3Boolean()
      self.obj1330.Copy.setValue(('Copy from LHS', 1))
      self.obj1330.Copy.config = 0
      self.obj1330.Specify=ATOM3Constraint()
      self.obj1330.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj133.GGset2Any['MaxFlow']= self.obj1330
      self.obj1331= AttrCalc()
      self.obj1331.Copy=ATOM3Boolean()
      self.obj1331.Copy.setValue(('Copy from LHS', 1))
      self.obj1331.Copy.config = 0
      self.obj1331.Specify=ATOM3Constraint()
      self.obj1331.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj133.GGset2Any['price']= self.obj1331
      self.obj1332= AttrCalc()
      self.obj1332.Copy=ATOM3Boolean()
      self.obj1332.Copy.setValue(('Copy from LHS', 1))
      self.obj1332.Copy.config = 0
      self.obj1332.Specify=ATOM3Constraint()
      self.obj1332.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj133.GGset2Any['Name']= self.obj1332
      self.obj1333= AttrCalc()
      self.obj1333.Copy=ATOM3Boolean()
      self.obj1333.Copy.setValue(('Copy from LHS', 1))
      self.obj1333.Copy.config = 0
      self.obj1333.Specify=ATOM3Constraint()
      self.obj1333.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj133.GGset2Any['ReqFlow']= self.obj1333

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj133)
      self.obj133.postAction( self.RHS.CREATE )

      self.obj134=metarial(parent)
      self.obj134.preAction( self.RHS.CREATE )
      self.obj134.isGraphObjectVisual = True

      if(hasattr(self.obj134, '_setHierarchicalLink')):
        self.obj134._setHierarchicalLink(False)

      # MaxFlow
      self.obj134.MaxFlow.setNone()

      # price
      self.obj134.price.setNone()

      # Name
      self.obj134.Name.setValue('')
      self.obj134.Name.setNone()

      # ReqFlow
      self.obj134.ReqFlow.setNone()

      self.obj134.GGLabel.setValue(3)
      self.obj134.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(360.0,140.0,self.obj134)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj134.graphObject_ = new_obj
      self.obj1340= AttrCalc()
      self.obj1340.Copy=ATOM3Boolean()
      self.obj1340.Copy.setValue(('Copy from LHS', 1))
      self.obj1340.Copy.config = 0
      self.obj1340.Specify=ATOM3Constraint()
      self.obj1340.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj134.GGset2Any['MaxFlow']= self.obj1340
      self.obj1341= AttrCalc()
      self.obj1341.Copy=ATOM3Boolean()
      self.obj1341.Copy.setValue(('Copy from LHS', 1))
      self.obj1341.Copy.config = 0
      self.obj1341.Specify=ATOM3Constraint()
      self.obj1341.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj134.GGset2Any['price']= self.obj1341
      self.obj1342= AttrCalc()
      self.obj1342.Copy=ATOM3Boolean()
      self.obj1342.Copy.setValue(('Copy from LHS', 1))
      self.obj1342.Copy.config = 0
      self.obj1342.Specify=ATOM3Constraint()
      self.obj1342.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj134.GGset2Any['Name']= self.obj1342
      self.obj1343= AttrCalc()
      self.obj1343.Copy=ATOM3Boolean()
      self.obj1343.Copy.setValue(('Copy from LHS', 1))
      self.obj1343.Copy.config = 0
      self.obj1343.Specify=ATOM3Constraint()
      self.obj1343.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj134.GGset2Any['ReqFlow']= self.obj1343

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj134)
      self.obj134.postAction( self.RHS.CREATE )

      self.obj135=operatingUnit(parent)
      self.obj135.preAction( self.RHS.CREATE )
      self.obj135.isGraphObjectVisual = True

      if(hasattr(self.obj135, '_setHierarchicalLink')):
        self.obj135._setHierarchicalLink(False)

      # OperCostProp
      self.obj135.OperCostProp.setNone()

      # name
      self.obj135.name.setValue('')
      self.obj135.name.setNone()

      # OperCostFix
      self.obj135.OperCostFix.setNone()

      self.obj135.GGLabel.setValue(2)
      self.obj135.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(180.0,100.0,self.obj135)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj135.graphObject_ = new_obj
      self.obj1350= AttrCalc()
      self.obj1350.Copy=ATOM3Boolean()
      self.obj1350.Copy.setValue(('Copy from LHS', 1))
      self.obj1350.Copy.config = 0
      self.obj1350.Specify=ATOM3Constraint()
      self.obj1350.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj135.GGset2Any['OperCostProp']= self.obj1350
      self.obj1351= AttrCalc()
      self.obj1351.Copy=ATOM3Boolean()
      self.obj1351.Copy.setValue(('Copy from LHS', 1))
      self.obj1351.Copy.config = 0
      self.obj1351.Specify=ATOM3Constraint()
      self.obj1351.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj135.GGset2Any['name']= self.obj1351
      self.obj1352= AttrCalc()
      self.obj1352.Copy=ATOM3Boolean()
      self.obj1352.Copy.setValue(('Copy from LHS', 1))
      self.obj1352.Copy.config = 0
      self.obj1352.Specify=ATOM3Constraint()
      self.obj1352.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj135.GGset2Any['OperCostFix']= self.obj1352

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj135)
      self.obj135.postAction( self.RHS.CREATE )

      self.obj136=fromRaw(parent)
      self.obj136.preAction( self.RHS.CREATE )
      self.obj136.isGraphObjectVisual = True

      if(hasattr(self.obj136, '_setHierarchicalLink')):
        self.obj136._setHierarchicalLink(False)

      # rate
      self.obj136.rate.setNone()

      self.obj136.GGLabel.setValue(4)
      self.obj136.graphClass_= graph_fromRaw
      if parent.genGraphics:
         new_obj = graph_fromRaw(183.0,77.75,self.obj136)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj136.graphObject_ = new_obj
      self.obj1360= AttrCalc()
      self.obj1360.Copy=ATOM3Boolean()
      self.obj1360.Copy.setValue(('Copy from LHS', 1))
      self.obj1360.Copy.config = 0
      self.obj1360.Specify=ATOM3Constraint()
      self.obj1360.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj136.GGset2Any['rate']= self.obj1360

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj136)
      self.obj136.postAction( self.RHS.CREATE )

      self.obj137=intoMaterial(parent)
      self.obj137.preAction( self.RHS.CREATE )
      self.obj137.isGraphObjectVisual = True

      if(hasattr(self.obj137, '_setHierarchicalLink')):
        self.obj137._setHierarchicalLink(False)

      # rate
      self.obj137.rate.setNone()

      self.obj137.GGLabel.setValue(5)
      self.obj137.graphClass_= graph_intoMaterial
      if parent.genGraphics:
         new_obj = graph_intoMaterial(258.75,158.0,self.obj137)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj137.graphObject_ = new_obj
      self.obj1370= AttrCalc()
      self.obj1370.Copy=ATOM3Boolean()
      self.obj1370.Copy.setValue(('Copy from LHS', 1))
      self.obj1370.Copy.config = 0
      self.obj1370.Specify=ATOM3Constraint()
      self.obj1370.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj137.GGset2Any['rate']= self.obj1370

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj137)
      self.obj137.postAction( self.RHS.CREATE )

      self.obj133.out_connections_.append(self.obj136)
      self.obj136.in_connections_.append(self.obj133)
      self.obj133.graphObject_.pendingConnections.append((self.obj133.graphObject_.tag, self.obj136.graphObject_.tag, [64.0, 70.0, 183.0, 77.75], 2, 0))
      self.obj135.out_connections_.append(self.obj137)
      self.obj137.in_connections_.append(self.obj135)
      self.obj135.graphObject_.pendingConnections.append((self.obj135.graphObject_.tag, self.obj137.graphObject_.tag, [233.0, 108.0, 258.75, 158.0], 2, 0))
      self.obj136.out_connections_.append(self.obj135)
      self.obj135.in_connections_.append(self.obj136)
      self.obj136.graphObject_.pendingConnections.append((self.obj136.graphObject_.tag, self.obj135.graphObject_.tag, [230.0, 101.0, 183.0, 77.75], 2, 0))
      self.obj137.out_connections_.append(self.obj134)
      self.obj134.in_connections_.append(self.obj137)
      self.obj137.graphObject_.pendingConnections.append((self.obj137.graphObject_.tag, self.obj134.graphObject_.tag, [366.0, 182.0, 258.75, 158.0], 2, 0))

   def condition(self, graphID, isograph, atom3i):
      opUnit = self.getMatched(graphID, self.LHS.nodeWithLabel(2)) 
      return not ( hasattr(opUnit,"rat") )
      
      

   def action(self, graphID, isograph, atom3i):
      input = self.getMatched(graphID, self.LHS.nodeWithLabel(4))
      output = self.getMatched(graphID, self.LHS.nodeWithLabel(5))
      
      op = self.getMatched(graphID, self.LHS.nodeWithLabel(2))
      op.rat = input.rate.getValue()/output.rate.getValue()
      print op.name.getValue()+":"+str(op.rat)
      
      

