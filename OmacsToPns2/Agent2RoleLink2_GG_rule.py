# _ Agent2RoleLink2_GG_rule.py ____________________________________________________________________________
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
class Agent2RoleLink2_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 2)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_omacs(parent)

      self.obj1525=Agent(parent)
      self.obj1525.preAction( self.LHS.CREATE )
      self.obj1525.isGraphObjectVisual = True

      if(hasattr(self.obj1525, '_setHierarchicalLink')):
        self.obj1525._setHierarchicalLink(False)

      # price
      self.obj1525.price.setNone()

      # name
      self.obj1525.name.setValue('')
      self.obj1525.name.setNone()

      self.obj1525.GGLabel.setValue(1)
      self.obj1525.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(60.0,20.0,self.obj1525)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1525.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1525)
      self.obj1525.postAction( self.LHS.CREATE )

      self.obj1526=Capabilitie(parent)
      self.obj1526.preAction( self.LHS.CREATE )
      self.obj1526.isGraphObjectVisual = True

      if(hasattr(self.obj1526, '_setHierarchicalLink')):
        self.obj1526._setHierarchicalLink(False)

      # name
      self.obj1526.name.setValue('')
      self.obj1526.name.setNone()

      self.obj1526.GGLabel.setValue(2)
      self.obj1526.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(80.0,180.0,self.obj1526)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1526.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1526)
      self.obj1526.postAction( self.LHS.CREATE )

      self.obj1527=Capabilitie(parent)
      self.obj1527.preAction( self.LHS.CREATE )
      self.obj1527.isGraphObjectVisual = True

      if(hasattr(self.obj1527, '_setHierarchicalLink')):
        self.obj1527._setHierarchicalLink(False)

      # name
      self.obj1527.name.setValue('')
      self.obj1527.name.setNone()

      self.obj1527.GGLabel.setValue(3)
      self.obj1527.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(300.0,20.0,self.obj1527)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1527.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1527)
      self.obj1527.postAction( self.LHS.CREATE )

      self.obj1528=Role(parent)
      self.obj1528.preAction( self.LHS.CREATE )
      self.obj1528.isGraphObjectVisual = True

      if(hasattr(self.obj1528, '_setHierarchicalLink')):
        self.obj1528._setHierarchicalLink(False)

      # name
      self.obj1528.name.setValue('')
      self.obj1528.name.setNone()

      self.obj1528.GGLabel.setValue(4)
      self.obj1528.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(320.0,180.0,self.obj1528)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1528.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1528)
      self.obj1528.postAction( self.LHS.CREATE )

      self.obj1529=posses(parent)
      self.obj1529.preAction( self.LHS.CREATE )
      self.obj1529.isGraphObjectVisual = True

      if(hasattr(self.obj1529, '_setHierarchicalLink')):
        self.obj1529._setHierarchicalLink(False)

      # rate
      self.obj1529.rate.setNone()

      self.obj1529.GGLabel.setValue(5)
      self.obj1529.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(203.0,70.5,self.obj1529)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1529.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1529)
      self.obj1529.postAction( self.LHS.CREATE )

      self.obj1530=posses(parent)
      self.obj1530.preAction( self.LHS.CREATE )
      self.obj1530.isGraphObjectVisual = True

      if(hasattr(self.obj1530, '_setHierarchicalLink')):
        self.obj1530._setHierarchicalLink(False)

      # rate
      self.obj1530.rate.setNone()

      self.obj1530.GGLabel.setValue(6)
      self.obj1530.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(93.0,130.5,self.obj1530)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1530.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1530)
      self.obj1530.postAction( self.LHS.CREATE )

      self.obj1531=CapableOf(parent)
      self.obj1531.preAction( self.LHS.CREATE )
      self.obj1531.isGraphObjectVisual = True

      if(hasattr(self.obj1531, '_setHierarchicalLink')):
        self.obj1531._setHierarchicalLink(False)

      # rate
      self.obj1531.rate.setNone()

      self.obj1531.GGLabel.setValue(9)
      self.obj1531.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(209.5,129.5,self.obj1531)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1531.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1531)
      self.obj1531.postAction( self.LHS.CREATE )

      self.obj1532=require(parent)
      self.obj1532.preAction( self.LHS.CREATE )
      self.obj1532.isGraphObjectVisual = True

      if(hasattr(self.obj1532, '_setHierarchicalLink')):
        self.obj1532._setHierarchicalLink(False)

      self.obj1532.GGLabel.setValue(7)
      self.obj1532.graphClass_= graph_require
      if parent.genGraphics:
         new_obj = graph_require(222.5,180.0,self.obj1532)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1532.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1532)
      self.obj1532.postAction( self.LHS.CREATE )

      self.obj1533=require(parent)
      self.obj1533.preAction( self.LHS.CREATE )
      self.obj1533.isGraphObjectVisual = True

      if(hasattr(self.obj1533, '_setHierarchicalLink')):
        self.obj1533._setHierarchicalLink(False)

      self.obj1533.GGLabel.setValue(8)
      self.obj1533.graphClass_= graph_require
      if parent.genGraphics:
         new_obj = graph_require(332.5,120.0,self.obj1533)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1533.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1533)
      self.obj1533.postAction( self.LHS.CREATE )

      self.obj1525.out_connections_.append(self.obj1529)
      self.obj1529.in_connections_.append(self.obj1525)
      self.obj1525.out_connections_.append(self.obj1530)
      self.obj1530.in_connections_.append(self.obj1525)
      self.obj1525.graphObject_.pendingConnections.append((self.obj1525.graphObject_.tag, self.obj1530.graphObject_.tag, [85.0, 82.0, 93.0, 130.5], 0, True))
      self.obj1525.out_connections_.append(self.obj1531)
      self.obj1531.in_connections_.append(self.obj1525)
      self.obj1525.graphObject_.pendingConnections.append((self.obj1525.graphObject_.tag, self.obj1531.graphObject_.tag, [85.0, 82.0, 163.0, 138.0, 209.5, 129.5], 2, True))
      self.obj1528.out_connections_.append(self.obj1532)
      self.obj1532.in_connections_.append(self.obj1528)
      self.obj1528.graphObject_.pendingConnections.append((self.obj1528.graphObject_.tag, self.obj1532.graphObject_.tag, [344.0, 181.0, 222.5, 180.0], 0, True))
      self.obj1528.out_connections_.append(self.obj1533)
      self.obj1533.in_connections_.append(self.obj1528)
      self.obj1528.graphObject_.pendingConnections.append((self.obj1528.graphObject_.tag, self.obj1533.graphObject_.tag, [344.0, 181.0, 332.5, 120.0], 0, True))
      self.obj1529.out_connections_.append(self.obj1527)
      self.obj1527.in_connections_.append(self.obj1529)
      self.obj1529.graphObject_.pendingConnections.append((self.obj1529.graphObject_.tag, self.obj1527.graphObject_.tag, [321.0, 59.0, 203.0, 70.5], 0, True))
      self.obj1530.out_connections_.append(self.obj1526)
      self.obj1526.in_connections_.append(self.obj1530)
      self.obj1530.graphObject_.pendingConnections.append((self.obj1530.graphObject_.tag, self.obj1526.graphObject_.tag, [101.0, 179.0, 93.0, 130.5], 0, True))
      self.obj1531.out_connections_.append(self.obj1528)
      self.obj1528.in_connections_.append(self.obj1531)
      self.obj1531.graphObject_.pendingConnections.append((self.obj1531.graphObject_.tag, self.obj1528.graphObject_.tag, [344.0, 181.0, 256.0, 121.0, 209.5, 129.5], 2, True))
      self.obj1532.out_connections_.append(self.obj1526)
      self.obj1526.in_connections_.append(self.obj1532)
      self.obj1532.graphObject_.pendingConnections.append((self.obj1532.graphObject_.tag, self.obj1526.graphObject_.tag, [101.0, 179.0, 222.5, 180.0], 0, True))
      self.obj1533.out_connections_.append(self.obj1527)
      self.obj1527.in_connections_.append(self.obj1533)

      self.RHS = ASG_omacs(parent)

      self.obj1535=Agent(parent)
      self.obj1535.preAction( self.RHS.CREATE )
      self.obj1535.isGraphObjectVisual = True

      if(hasattr(self.obj1535, '_setHierarchicalLink')):
        self.obj1535._setHierarchicalLink(False)

      # price
      self.obj1535.price.setNone()

      # name
      self.obj1535.name.setValue('')
      self.obj1535.name.setNone()

      self.obj1535.GGLabel.setValue(1)
      self.obj1535.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(60.0,20.0,self.obj1535)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1535.graphObject_ = new_obj
      self.obj15350= AttrCalc()
      self.obj15350.Copy=ATOM3Boolean()
      self.obj15350.Copy.setValue(('Copy from LHS', 1))
      self.obj15350.Copy.config = 0
      self.obj15350.Specify=ATOM3Constraint()
      self.obj15350.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1535.GGset2Any['price']= self.obj15350
      self.obj15351= AttrCalc()
      self.obj15351.Copy=ATOM3Boolean()
      self.obj15351.Copy.setValue(('Copy from LHS', 1))
      self.obj15351.Copy.config = 0
      self.obj15351.Specify=ATOM3Constraint()
      self.obj15351.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1535.GGset2Any['name']= self.obj15351

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1535)
      self.obj1535.postAction( self.RHS.CREATE )

      self.obj1536=Capabilitie(parent)
      self.obj1536.preAction( self.RHS.CREATE )
      self.obj1536.isGraphObjectVisual = True

      if(hasattr(self.obj1536, '_setHierarchicalLink')):
        self.obj1536._setHierarchicalLink(False)

      # name
      self.obj1536.name.setValue('')
      self.obj1536.name.setNone()

      self.obj1536.GGLabel.setValue(2)
      self.obj1536.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(80.0,180.0,self.obj1536)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1536.graphObject_ = new_obj
      self.obj15360= AttrCalc()
      self.obj15360.Copy=ATOM3Boolean()
      self.obj15360.Copy.setValue(('Copy from LHS', 1))
      self.obj15360.Copy.config = 0
      self.obj15360.Specify=ATOM3Constraint()
      self.obj15360.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1536.GGset2Any['name']= self.obj15360

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1536)
      self.obj1536.postAction( self.RHS.CREATE )

      self.obj1537=Capabilitie(parent)
      self.obj1537.preAction( self.RHS.CREATE )
      self.obj1537.isGraphObjectVisual = True

      if(hasattr(self.obj1537, '_setHierarchicalLink')):
        self.obj1537._setHierarchicalLink(False)

      # name
      self.obj1537.name.setValue('')
      self.obj1537.name.setNone()

      self.obj1537.GGLabel.setValue(3)
      self.obj1537.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(300.0,20.0,self.obj1537)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1537.graphObject_ = new_obj
      self.obj15370= AttrCalc()
      self.obj15370.Copy=ATOM3Boolean()
      self.obj15370.Copy.setValue(('Copy from LHS', 1))
      self.obj15370.Copy.config = 0
      self.obj15370.Specify=ATOM3Constraint()
      self.obj15370.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1537.GGset2Any['name']= self.obj15370

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1537)
      self.obj1537.postAction( self.RHS.CREATE )

      self.obj1538=Role(parent)
      self.obj1538.preAction( self.RHS.CREATE )
      self.obj1538.isGraphObjectVisual = True

      if(hasattr(self.obj1538, '_setHierarchicalLink')):
        self.obj1538._setHierarchicalLink(False)

      # name
      self.obj1538.name.setValue('')
      self.obj1538.name.setNone()

      self.obj1538.GGLabel.setValue(4)
      self.obj1538.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(320.0,180.0,self.obj1538)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1538.graphObject_ = new_obj
      self.obj15380= AttrCalc()
      self.obj15380.Copy=ATOM3Boolean()
      self.obj15380.Copy.setValue(('Copy from LHS', 1))
      self.obj15380.Copy.config = 0
      self.obj15380.Specify=ATOM3Constraint()
      self.obj15380.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1538.GGset2Any['name']= self.obj15380

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1538)
      self.obj1538.postAction( self.RHS.CREATE )

      self.obj1539=posses(parent)
      self.obj1539.preAction( self.RHS.CREATE )
      self.obj1539.isGraphObjectVisual = True

      if(hasattr(self.obj1539, '_setHierarchicalLink')):
        self.obj1539._setHierarchicalLink(False)

      # rate
      self.obj1539.rate.setNone()

      self.obj1539.GGLabel.setValue(5)
      self.obj1539.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(203.0,70.5,self.obj1539)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1539.graphObject_ = new_obj
      self.obj15390= AttrCalc()
      self.obj15390.Copy=ATOM3Boolean()
      self.obj15390.Copy.setValue(('Copy from LHS', 1))
      self.obj15390.Copy.config = 0
      self.obj15390.Specify=ATOM3Constraint()
      self.obj15390.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1539.GGset2Any['rate']= self.obj15390

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1539)
      self.obj1539.postAction( self.RHS.CREATE )

      self.obj1540=posses(parent)
      self.obj1540.preAction( self.RHS.CREATE )
      self.obj1540.isGraphObjectVisual = True

      if(hasattr(self.obj1540, '_setHierarchicalLink')):
        self.obj1540._setHierarchicalLink(False)

      # rate
      self.obj1540.rate.setNone()

      self.obj1540.GGLabel.setValue(6)
      self.obj1540.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(93.0,130.5,self.obj1540)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1540.graphObject_ = new_obj
      self.obj15400= AttrCalc()
      self.obj15400.Copy=ATOM3Boolean()
      self.obj15400.Copy.setValue(('Copy from LHS', 1))
      self.obj15400.Copy.config = 0
      self.obj15400.Specify=ATOM3Constraint()
      self.obj15400.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1540.GGset2Any['rate']= self.obj15400

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1540)
      self.obj1540.postAction( self.RHS.CREATE )

      self.obj1541=CapableOf(parent)
      self.obj1541.preAction( self.RHS.CREATE )
      self.obj1541.isGraphObjectVisual = True

      if(hasattr(self.obj1541, '_setHierarchicalLink')):
        self.obj1541._setHierarchicalLink(False)

      # rate
      self.obj1541.rate.setValue(0.0)

      self.obj1541.GGLabel.setValue(9)
      self.obj1541.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(209.5,129.5,self.obj1541)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1541.graphObject_ = new_obj
      self.obj15410= AttrCalc()
      self.obj15410.Copy=ATOM3Boolean()
      self.obj15410.Copy.setValue(('Copy from LHS', 1))
      self.obj15410.Copy.config = 0
      self.obj15410.Specify=ATOM3Constraint()
      self.obj15410.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1541.GGset2Any['rate']= self.obj15410

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1541)
      self.obj1541.postAction( self.RHS.CREATE )

      self.obj1542=require(parent)
      self.obj1542.preAction( self.RHS.CREATE )
      self.obj1542.isGraphObjectVisual = True

      if(hasattr(self.obj1542, '_setHierarchicalLink')):
        self.obj1542._setHierarchicalLink(False)

      self.obj1542.GGLabel.setValue(7)
      self.obj1542.graphClass_= graph_require
      if parent.genGraphics:
         new_obj = graph_require(222.5,180.0,self.obj1542)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1542.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1542)
      self.obj1542.postAction( self.RHS.CREATE )

      self.obj1543=require(parent)
      self.obj1543.preAction( self.RHS.CREATE )
      self.obj1543.isGraphObjectVisual = True

      if(hasattr(self.obj1543, '_setHierarchicalLink')):
        self.obj1543._setHierarchicalLink(False)

      self.obj1543.GGLabel.setValue(8)
      self.obj1543.graphClass_= graph_require
      if parent.genGraphics:
         new_obj = graph_require(332.5,120.0,self.obj1543)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1543.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1543)
      self.obj1543.postAction( self.RHS.CREATE )

      self.obj1535.out_connections_.append(self.obj1539)
      self.obj1539.in_connections_.append(self.obj1535)
      self.obj1535.out_connections_.append(self.obj1540)
      self.obj1540.in_connections_.append(self.obj1535)
      self.obj1535.graphObject_.pendingConnections.append((self.obj1535.graphObject_.tag, self.obj1540.graphObject_.tag, [97.0, 82.0, 93.0, 130.5], 2, 0))
      self.obj1535.out_connections_.append(self.obj1541)
      self.obj1541.in_connections_.append(self.obj1535)
      self.obj1535.graphObject_.pendingConnections.append((self.obj1535.graphObject_.tag, self.obj1541.graphObject_.tag, [97.0, 82.0, 209.5, 129.5], 2, 0))
      self.obj1538.out_connections_.append(self.obj1542)
      self.obj1542.in_connections_.append(self.obj1538)
      self.obj1538.graphObject_.pendingConnections.append((self.obj1538.graphObject_.tag, self.obj1542.graphObject_.tag, [351.0, 180.0, 222.5, 180.0], 2, 0))
      self.obj1538.out_connections_.append(self.obj1543)
      self.obj1543.in_connections_.append(self.obj1538)
      self.obj1538.graphObject_.pendingConnections.append((self.obj1538.graphObject_.tag, self.obj1543.graphObject_.tag, [351.0, 180.0, 332.5, 120.0], 2, 0))
      self.obj1539.out_connections_.append(self.obj1537)
      self.obj1537.in_connections_.append(self.obj1539)
      self.obj1539.graphObject_.pendingConnections.append((self.obj1539.graphObject_.tag, self.obj1537.graphObject_.tag, [331.0, 63.0, 203.0, 70.5], 2, 0))
      self.obj1540.out_connections_.append(self.obj1536)
      self.obj1536.in_connections_.append(self.obj1540)
      self.obj1540.graphObject_.pendingConnections.append((self.obj1540.graphObject_.tag, self.obj1536.graphObject_.tag, [111.0, 183.0, 93.0, 130.5], 2, 0))
      self.obj1541.out_connections_.append(self.obj1538)
      self.obj1538.in_connections_.append(self.obj1541)
      self.obj1541.graphObject_.pendingConnections.append((self.obj1541.graphObject_.tag, self.obj1538.graphObject_.tag, [351.0, 180.0, 209.5, 129.5], 2, 0))
      self.obj1542.out_connections_.append(self.obj1536)
      self.obj1536.in_connections_.append(self.obj1542)
      self.obj1542.graphObject_.pendingConnections.append((self.obj1542.graphObject_.tag, self.obj1536.graphObject_.tag, [111.0, 183.0, 222.5, 180.0], 2, 0))
      self.obj1543.out_connections_.append(self.obj1537)
      self.obj1537.in_connections_.append(self.obj1543)

   def condition(self, graphID, isograph, atom3i):
      
      agent = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      c1 = self.getMatched(graphID, self.LHS.nodeWithLabel(2))
      c2 = self.getMatched(graphID, self.LHS.nodeWithLabel(3))
      role = self.getMatched(graphID, self.LHS.nodeWithLabel(4))
      
      return not ( hasattr(c1, agent.name.getValue() ) and 
      hasattr(c1, role.name.getValue() ) and
      hasattr(c2, agent.name.getValue() ) and  hasattr(c2,  role.name.getValue()  ) )
      

   def action(self, graphID, isograph, atom3i):
      agent = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      c1 = self.getMatched(graphID, self.LHS.nodeWithLabel(2))
      c2 = self.getMatched(graphID, self.LHS.nodeWithLabel(3))
      role = self.getMatched(graphID, self.LHS.nodeWithLabel(4))
      
      setattr( c1 ,  agent.name.getValue() , True )
      setattr( c1 ,  role.name.getValue() , True )
      
      setattr( c2 ,  agent.name.getValue() , True )
      setattr( c2 ,  role.name.getValue() , True )
      print' Mark :('+agent.name.getValue()+','+c1.name.getValue()+','+c2.name.getValue()+','+role.name.getValue()+')'
      
      

