# _ MarkOpUnit2_GG_rule.py ____________________________________________________________________________
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
class MarkOpUnit2_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 5)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_pns(parent)

      self.obj142=metarial(parent)
      self.obj142.preAction( self.LHS.CREATE )
      self.obj142.isGraphObjectVisual = True

      if(hasattr(self.obj142, '_setHierarchicalLink')):
        self.obj142._setHierarchicalLink(False)

      # MaxFlow
      self.obj142.MaxFlow.setNone()

      # price
      self.obj142.price.setNone()

      # Name
      self.obj142.Name.setValue('')
      self.obj142.Name.setNone()

      # ReqFlow
      self.obj142.ReqFlow.setNone()

      self.obj142.GGLabel.setValue(1)
      self.obj142.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(40.0,40.0,self.obj142)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj142.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj142)
      self.obj142.postAction( self.LHS.CREATE )

      self.obj143=metarial(parent)
      self.obj143.preAction( self.LHS.CREATE )
      self.obj143.isGraphObjectVisual = True

      if(hasattr(self.obj143, '_setHierarchicalLink')):
        self.obj143._setHierarchicalLink(False)

      # MaxFlow
      self.obj143.MaxFlow.setNone()

      # price
      self.obj143.price.setNone()

      # Name
      self.obj143.Name.setValue('')
      self.obj143.Name.setNone()

      # ReqFlow
      self.obj143.ReqFlow.setNone()

      self.obj143.GGLabel.setValue(3)
      self.obj143.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(360.0,160.0,self.obj143)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj143.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj143)
      self.obj143.postAction( self.LHS.CREATE )

      self.obj144=operatingUnit(parent)
      self.obj144.preAction( self.LHS.CREATE )
      self.obj144.isGraphObjectVisual = True

      if(hasattr(self.obj144, '_setHierarchicalLink')):
        self.obj144._setHierarchicalLink(False)

      # OperCostProp
      self.obj144.OperCostProp.setNone()

      # name
      self.obj144.name.setValue('')
      self.obj144.name.setNone()

      # OperCostFix
      self.obj144.OperCostFix.setNone()

      self.obj144.GGLabel.setValue(2)
      self.obj144.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(180.0,100.0,self.obj144)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj144.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj144)
      self.obj144.postAction( self.LHS.CREATE )

      self.obj145=intoMaterial(parent)
      self.obj145.preAction( self.LHS.CREATE )
      self.obj145.isGraphObjectVisual = True

      if(hasattr(self.obj145, '_setHierarchicalLink')):
        self.obj145._setHierarchicalLink(False)

      # rate
      self.obj145.rate.setNone()

      self.obj145.GGLabel.setValue(5)
      self.obj145.graphClass_= graph_intoMaterial
      if parent.genGraphics:
         new_obj = graph_intoMaterial(248.75,168.5,self.obj145)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj145.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj145)
      self.obj145.postAction( self.LHS.CREATE )

      self.obj146=fromMaterial(parent)
      self.obj146.preAction( self.LHS.CREATE )
      self.obj146.isGraphObjectVisual = True

      if(hasattr(self.obj146, '_setHierarchicalLink')):
        self.obj146._setHierarchicalLink(False)

      # rate
      self.obj146.rate.setNone()

      self.obj146.GGLabel.setValue(4)
      self.obj146.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(175.0,68.75,self.obj146)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj146.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj146)
      self.obj146.postAction( self.LHS.CREATE )

      self.obj142.out_connections_.append(self.obj146)
      self.obj146.in_connections_.append(self.obj142)
      self.obj142.graphObject_.pendingConnections.append((self.obj142.graphObject_.tag, self.obj146.graphObject_.tag, [86.0, 50.0, 146.5, 53.5, 175.0, 68.75], 2, True))
      self.obj144.out_connections_.append(self.obj145)
      self.obj145.in_connections_.append(self.obj144)
      self.obj144.graphObject_.pendingConnections.append((self.obj144.graphObject_.tag, self.obj145.graphObject_.tag, [199.0, 118.0, 207.0, 147.5, 248.75, 168.5], 2, True))
      self.obj145.out_connections_.append(self.obj143)
      self.obj143.in_connections_.append(self.obj145)
      self.obj145.graphObject_.pendingConnections.append((self.obj145.graphObject_.tag, self.obj143.graphObject_.tag, [366.0, 202.0, 290.5, 189.5, 248.75, 168.5], 2, True))
      self.obj146.out_connections_.append(self.obj144)
      self.obj144.in_connections_.append(self.obj146)
      self.obj146.graphObject_.pendingConnections.append((self.obj146.graphObject_.tag, self.obj144.graphObject_.tag, [200.0, 111.0, 203.5, 84.0, 175.0, 68.75], 2, True))

      self.RHS = ASG_pns(parent)

      self.obj148=metarial(parent)
      self.obj148.preAction( self.RHS.CREATE )
      self.obj148.isGraphObjectVisual = True

      if(hasattr(self.obj148, '_setHierarchicalLink')):
        self.obj148._setHierarchicalLink(False)

      # MaxFlow
      self.obj148.MaxFlow.setNone()

      # price
      self.obj148.price.setNone()

      # Name
      self.obj148.Name.setValue('')
      self.obj148.Name.setNone()

      # ReqFlow
      self.obj148.ReqFlow.setNone()

      self.obj148.GGLabel.setValue(1)
      self.obj148.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(40.0,40.0,self.obj148)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj148.graphObject_ = new_obj
      self.obj1480= AttrCalc()
      self.obj1480.Copy=ATOM3Boolean()
      self.obj1480.Copy.setValue(('Copy from LHS', 1))
      self.obj1480.Copy.config = 0
      self.obj1480.Specify=ATOM3Constraint()
      self.obj1480.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj148.GGset2Any['MaxFlow']= self.obj1480
      self.obj1481= AttrCalc()
      self.obj1481.Copy=ATOM3Boolean()
      self.obj1481.Copy.setValue(('Copy from LHS', 1))
      self.obj1481.Copy.config = 0
      self.obj1481.Specify=ATOM3Constraint()
      self.obj1481.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj148.GGset2Any['price']= self.obj1481
      self.obj1482= AttrCalc()
      self.obj1482.Copy=ATOM3Boolean()
      self.obj1482.Copy.setValue(('Copy from LHS', 1))
      self.obj1482.Copy.config = 0
      self.obj1482.Specify=ATOM3Constraint()
      self.obj1482.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj148.GGset2Any['Name']= self.obj1482
      self.obj1483= AttrCalc()
      self.obj1483.Copy=ATOM3Boolean()
      self.obj1483.Copy.setValue(('Copy from LHS', 1))
      self.obj1483.Copy.config = 0
      self.obj1483.Specify=ATOM3Constraint()
      self.obj1483.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj148.GGset2Any['ReqFlow']= self.obj1483

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj148)
      self.obj148.postAction( self.RHS.CREATE )

      self.obj149=metarial(parent)
      self.obj149.preAction( self.RHS.CREATE )
      self.obj149.isGraphObjectVisual = True

      if(hasattr(self.obj149, '_setHierarchicalLink')):
        self.obj149._setHierarchicalLink(False)

      # MaxFlow
      self.obj149.MaxFlow.setNone()

      # price
      self.obj149.price.setNone()

      # Name
      self.obj149.Name.setValue('')
      self.obj149.Name.setNone()

      # ReqFlow
      self.obj149.ReqFlow.setNone()

      self.obj149.GGLabel.setValue(3)
      self.obj149.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(360.0,160.0,self.obj149)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj149.graphObject_ = new_obj
      self.obj1490= AttrCalc()
      self.obj1490.Copy=ATOM3Boolean()
      self.obj1490.Copy.setValue(('Copy from LHS', 1))
      self.obj1490.Copy.config = 0
      self.obj1490.Specify=ATOM3Constraint()
      self.obj1490.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj149.GGset2Any['MaxFlow']= self.obj1490
      self.obj1491= AttrCalc()
      self.obj1491.Copy=ATOM3Boolean()
      self.obj1491.Copy.setValue(('Copy from LHS', 1))
      self.obj1491.Copy.config = 0
      self.obj1491.Specify=ATOM3Constraint()
      self.obj1491.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj149.GGset2Any['price']= self.obj1491
      self.obj1492= AttrCalc()
      self.obj1492.Copy=ATOM3Boolean()
      self.obj1492.Copy.setValue(('Copy from LHS', 1))
      self.obj1492.Copy.config = 0
      self.obj1492.Specify=ATOM3Constraint()
      self.obj1492.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj149.GGset2Any['Name']= self.obj1492
      self.obj1493= AttrCalc()
      self.obj1493.Copy=ATOM3Boolean()
      self.obj1493.Copy.setValue(('Copy from LHS', 1))
      self.obj1493.Copy.config = 0
      self.obj1493.Specify=ATOM3Constraint()
      self.obj1493.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj149.GGset2Any['ReqFlow']= self.obj1493

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj149)
      self.obj149.postAction( self.RHS.CREATE )

      self.obj150=operatingUnit(parent)
      self.obj150.preAction( self.RHS.CREATE )
      self.obj150.isGraphObjectVisual = True

      if(hasattr(self.obj150, '_setHierarchicalLink')):
        self.obj150._setHierarchicalLink(False)

      # OperCostProp
      self.obj150.OperCostProp.setNone()

      # name
      self.obj150.name.setValue('')
      self.obj150.name.setNone()

      # OperCostFix
      self.obj150.OperCostFix.setNone()

      self.obj150.GGLabel.setValue(2)
      self.obj150.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(180.0,100.0,self.obj150)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj150.graphObject_ = new_obj
      self.obj1500= AttrCalc()
      self.obj1500.Copy=ATOM3Boolean()
      self.obj1500.Copy.setValue(('Copy from LHS', 1))
      self.obj1500.Copy.config = 0
      self.obj1500.Specify=ATOM3Constraint()
      self.obj1500.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj150.GGset2Any['OperCostProp']= self.obj1500
      self.obj1501= AttrCalc()
      self.obj1501.Copy=ATOM3Boolean()
      self.obj1501.Copy.setValue(('Copy from LHS', 1))
      self.obj1501.Copy.config = 0
      self.obj1501.Specify=ATOM3Constraint()
      self.obj1501.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj150.GGset2Any['name']= self.obj1501
      self.obj1502= AttrCalc()
      self.obj1502.Copy=ATOM3Boolean()
      self.obj1502.Copy.setValue(('Copy from LHS', 1))
      self.obj1502.Copy.config = 0
      self.obj1502.Specify=ATOM3Constraint()
      self.obj1502.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj150.GGset2Any['OperCostFix']= self.obj1502

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj150)
      self.obj150.postAction( self.RHS.CREATE )

      self.obj151=intoMaterial(parent)
      self.obj151.preAction( self.RHS.CREATE )
      self.obj151.isGraphObjectVisual = True

      if(hasattr(self.obj151, '_setHierarchicalLink')):
        self.obj151._setHierarchicalLink(False)

      # rate
      self.obj151.rate.setNone()

      self.obj151.GGLabel.setValue(5)
      self.obj151.graphClass_= graph_intoMaterial
      if parent.genGraphics:
         new_obj = graph_intoMaterial(210.75,161.5,self.obj151)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['Text Scale'] = 0.68
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj151.graphObject_ = new_obj
      self.obj1510= AttrCalc()
      self.obj1510.Copy=ATOM3Boolean()
      self.obj1510.Copy.setValue(('Copy from LHS', 1))
      self.obj1510.Copy.config = 0
      self.obj1510.Specify=ATOM3Constraint()
      self.obj1510.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj151.GGset2Any['rate']= self.obj1510

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj151)
      self.obj151.postAction( self.RHS.CREATE )

      self.obj152=fromMaterial(parent)
      self.obj152.preAction( self.RHS.CREATE )
      self.obj152.isGraphObjectVisual = True

      if(hasattr(self.obj152, '_setHierarchicalLink')):
        self.obj152._setHierarchicalLink(False)

      # rate
      self.obj152.rate.setNone()

      self.obj152.GGLabel.setValue(4)
      self.obj152.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(175.0,68.75,self.obj152)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj152.graphObject_ = new_obj
      self.obj1520= AttrCalc()
      self.obj1520.Copy=ATOM3Boolean()
      self.obj1520.Copy.setValue(('Copy from LHS', 1))
      self.obj1520.Copy.config = 0
      self.obj1520.Specify=ATOM3Constraint()
      self.obj1520.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj152.GGset2Any['rate']= self.obj1520

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj152)
      self.obj152.postAction( self.RHS.CREATE )

      self.obj148.out_connections_.append(self.obj152)
      self.obj152.in_connections_.append(self.obj148)
      self.obj148.graphObject_.pendingConnections.append((self.obj148.graphObject_.tag, self.obj152.graphObject_.tag, [86.0, 50.0, 175.0, 68.75], 2, 0))
      self.obj150.out_connections_.append(self.obj151)
      self.obj151.in_connections_.append(self.obj150)
      self.obj150.graphObject_.pendingConnections.append((self.obj150.graphObject_.tag, self.obj151.graphObject_.tag, [233.0, 108.0, 210.75, 161.5], 2, 0))
      self.obj151.out_connections_.append(self.obj149)
      self.obj149.in_connections_.append(self.obj151)
      self.obj151.graphObject_.pendingConnections.append((self.obj151.graphObject_.tag, self.obj149.graphObject_.tag, [370.0, 165.0, 248.75, 168.5], 2, 0))
      self.obj152.out_connections_.append(self.obj150)
      self.obj150.in_connections_.append(self.obj152)
      self.obj152.graphObject_.pendingConnections.append((self.obj152.graphObject_.tag, self.obj150.graphObject_.tag, [230.0, 101.0, 175.0, 68.75], 2, 0))

   def condition(self, graphID, isograph, atom3i):
      opUnit = self.getMatched(graphID, self.LHS.nodeWithLabel(2)) 
      return not ( hasattr(opUnit,"rat") )
      
      

   def action(self, graphID, isograph, atom3i):
      input = self.getMatched(graphID, self.LHS.nodeWithLabel(4))
      output = self.getMatched(graphID, self.LHS.nodeWithLabel(5))
      
      op = self.getMatched(graphID, self.LHS.nodeWithLabel(2))
      op.rat = input.rate.getValue()/output.rate.getValue()
      print op.name.getValue()+":"+str(op.rat)
      
      

