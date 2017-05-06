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

      self.obj524=Agent(parent)
      self.obj524.preAction( self.LHS.CREATE )
      self.obj524.isGraphObjectVisual = True

      if(hasattr(self.obj524, '_setHierarchicalLink')):
        self.obj524._setHierarchicalLink(False)

      # price
      self.obj524.price.setNone()

      # name
      self.obj524.name.setValue('')
      self.obj524.name.setNone()

      self.obj524.GGLabel.setValue(1)
      self.obj524.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(60.0,20.0,self.obj524)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj524.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj524)
      self.obj524.postAction( self.LHS.CREATE )

      self.obj525=Capabilitie(parent)
      self.obj525.preAction( self.LHS.CREATE )
      self.obj525.isGraphObjectVisual = True

      if(hasattr(self.obj525, '_setHierarchicalLink')):
        self.obj525._setHierarchicalLink(False)

      # name
      self.obj525.name.setValue('')
      self.obj525.name.setNone()

      self.obj525.GGLabel.setValue(2)
      self.obj525.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(80.0,180.0,self.obj525)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj525.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj525)
      self.obj525.postAction( self.LHS.CREATE )

      self.obj526=Capabilitie(parent)
      self.obj526.preAction( self.LHS.CREATE )
      self.obj526.isGraphObjectVisual = True

      if(hasattr(self.obj526, '_setHierarchicalLink')):
        self.obj526._setHierarchicalLink(False)

      # name
      self.obj526.name.setValue('')
      self.obj526.name.setNone()

      self.obj526.GGLabel.setValue(3)
      self.obj526.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(300.0,20.0,self.obj526)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj526.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj526)
      self.obj526.postAction( self.LHS.CREATE )

      self.obj527=Role(parent)
      self.obj527.preAction( self.LHS.CREATE )
      self.obj527.isGraphObjectVisual = True

      if(hasattr(self.obj527, '_setHierarchicalLink')):
        self.obj527._setHierarchicalLink(False)

      # name
      self.obj527.name.setValue('')
      self.obj527.name.setNone()

      self.obj527.GGLabel.setValue(4)
      self.obj527.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(320.0,180.0,self.obj527)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj527.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj527)
      self.obj527.postAction( self.LHS.CREATE )

      self.obj528=posses(parent)
      self.obj528.preAction( self.LHS.CREATE )
      self.obj528.isGraphObjectVisual = True

      if(hasattr(self.obj528, '_setHierarchicalLink')):
        self.obj528._setHierarchicalLink(False)

      # rate
      self.obj528.rate.setNone()

      self.obj528.GGLabel.setValue(5)
      self.obj528.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(203.0,70.5,self.obj528)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj528.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj528)
      self.obj528.postAction( self.LHS.CREATE )

      self.obj529=posses(parent)
      self.obj529.preAction( self.LHS.CREATE )
      self.obj529.isGraphObjectVisual = True

      if(hasattr(self.obj529, '_setHierarchicalLink')):
        self.obj529._setHierarchicalLink(False)

      # rate
      self.obj529.rate.setNone()

      self.obj529.GGLabel.setValue(6)
      self.obj529.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(93.0,130.5,self.obj529)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj529.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj529)
      self.obj529.postAction( self.LHS.CREATE )

      self.obj530=CapableOf(parent)
      self.obj530.preAction( self.LHS.CREATE )
      self.obj530.isGraphObjectVisual = True

      if(hasattr(self.obj530, '_setHierarchicalLink')):
        self.obj530._setHierarchicalLink(False)

      # rate
      self.obj530.rate.setNone()

      self.obj530.GGLabel.setValue(9)
      self.obj530.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(209.5,129.5,self.obj530)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj530.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj530)
      self.obj530.postAction( self.LHS.CREATE )

      self.obj531=require(parent)
      self.obj531.preAction( self.LHS.CREATE )
      self.obj531.isGraphObjectVisual = True

      if(hasattr(self.obj531, '_setHierarchicalLink')):
        self.obj531._setHierarchicalLink(False)

      self.obj531.GGLabel.setValue(7)
      self.obj531.graphClass_= graph_require
      if parent.genGraphics:
         new_obj = graph_require(222.5,180.0,self.obj531)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj531.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj531)
      self.obj531.postAction( self.LHS.CREATE )

      self.obj532=require(parent)
      self.obj532.preAction( self.LHS.CREATE )
      self.obj532.isGraphObjectVisual = True

      if(hasattr(self.obj532, '_setHierarchicalLink')):
        self.obj532._setHierarchicalLink(False)

      self.obj532.GGLabel.setValue(8)
      self.obj532.graphClass_= graph_require
      if parent.genGraphics:
         new_obj = graph_require(332.5,120.0,self.obj532)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj532.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj532)
      self.obj532.postAction( self.LHS.CREATE )

      self.obj524.out_connections_.append(self.obj528)
      self.obj528.in_connections_.append(self.obj524)
      self.obj524.out_connections_.append(self.obj529)
      self.obj529.in_connections_.append(self.obj524)
      self.obj524.graphObject_.pendingConnections.append((self.obj524.graphObject_.tag, self.obj529.graphObject_.tag, [85.0, 82.0, 93.0, 130.5], 0, True))
      self.obj524.out_connections_.append(self.obj530)
      self.obj530.in_connections_.append(self.obj524)
      self.obj524.graphObject_.pendingConnections.append((self.obj524.graphObject_.tag, self.obj530.graphObject_.tag, [85.0, 82.0, 163.0, 138.0, 209.5, 129.5], 2, True))
      self.obj527.out_connections_.append(self.obj531)
      self.obj531.in_connections_.append(self.obj527)
      self.obj527.graphObject_.pendingConnections.append((self.obj527.graphObject_.tag, self.obj531.graphObject_.tag, [344.0, 181.0, 222.5, 180.0], 0, True))
      self.obj527.out_connections_.append(self.obj532)
      self.obj532.in_connections_.append(self.obj527)
      self.obj527.graphObject_.pendingConnections.append((self.obj527.graphObject_.tag, self.obj532.graphObject_.tag, [344.0, 181.0, 332.5, 120.0], 0, True))
      self.obj528.out_connections_.append(self.obj526)
      self.obj526.in_connections_.append(self.obj528)
      self.obj528.graphObject_.pendingConnections.append((self.obj528.graphObject_.tag, self.obj526.graphObject_.tag, [321.0, 59.0, 203.0, 70.5], 0, True))
      self.obj529.out_connections_.append(self.obj525)
      self.obj525.in_connections_.append(self.obj529)
      self.obj529.graphObject_.pendingConnections.append((self.obj529.graphObject_.tag, self.obj525.graphObject_.tag, [101.0, 179.0, 93.0, 130.5], 0, True))
      self.obj530.out_connections_.append(self.obj527)
      self.obj527.in_connections_.append(self.obj530)
      self.obj530.graphObject_.pendingConnections.append((self.obj530.graphObject_.tag, self.obj527.graphObject_.tag, [344.0, 181.0, 256.0, 121.0, 209.5, 129.5], 2, True))
      self.obj531.out_connections_.append(self.obj525)
      self.obj525.in_connections_.append(self.obj531)
      self.obj531.graphObject_.pendingConnections.append((self.obj531.graphObject_.tag, self.obj525.graphObject_.tag, [101.0, 179.0, 222.5, 180.0], 0, True))
      self.obj532.out_connections_.append(self.obj526)
      self.obj526.in_connections_.append(self.obj532)

      self.RHS = ASG_omacs(parent)

      self.obj534=Agent(parent)
      self.obj534.preAction( self.RHS.CREATE )
      self.obj534.isGraphObjectVisual = True

      if(hasattr(self.obj534, '_setHierarchicalLink')):
        self.obj534._setHierarchicalLink(False)

      # price
      self.obj534.price.setNone()

      # name
      self.obj534.name.setValue('')
      self.obj534.name.setNone()

      self.obj534.GGLabel.setValue(1)
      self.obj534.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(60.0,20.0,self.obj534)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj534.graphObject_ = new_obj
      self.obj5340= AttrCalc()
      self.obj5340.Copy=ATOM3Boolean()
      self.obj5340.Copy.setValue(('Copy from LHS', 1))
      self.obj5340.Copy.config = 0
      self.obj5340.Specify=ATOM3Constraint()
      self.obj5340.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj534.GGset2Any['price']= self.obj5340
      self.obj5341= AttrCalc()
      self.obj5341.Copy=ATOM3Boolean()
      self.obj5341.Copy.setValue(('Copy from LHS', 1))
      self.obj5341.Copy.config = 0
      self.obj5341.Specify=ATOM3Constraint()
      self.obj5341.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj534.GGset2Any['name']= self.obj5341

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj534)
      self.obj534.postAction( self.RHS.CREATE )

      self.obj535=Capabilitie(parent)
      self.obj535.preAction( self.RHS.CREATE )
      self.obj535.isGraphObjectVisual = True

      if(hasattr(self.obj535, '_setHierarchicalLink')):
        self.obj535._setHierarchicalLink(False)

      # name
      self.obj535.name.setValue('')
      self.obj535.name.setNone()

      self.obj535.GGLabel.setValue(2)
      self.obj535.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(80.0,180.0,self.obj535)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj535.graphObject_ = new_obj
      self.obj5350= AttrCalc()
      self.obj5350.Copy=ATOM3Boolean()
      self.obj5350.Copy.setValue(('Copy from LHS', 1))
      self.obj5350.Copy.config = 0
      self.obj5350.Specify=ATOM3Constraint()
      self.obj5350.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj535.GGset2Any['name']= self.obj5350

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj535)
      self.obj535.postAction( self.RHS.CREATE )

      self.obj536=Capabilitie(parent)
      self.obj536.preAction( self.RHS.CREATE )
      self.obj536.isGraphObjectVisual = True

      if(hasattr(self.obj536, '_setHierarchicalLink')):
        self.obj536._setHierarchicalLink(False)

      # name
      self.obj536.name.setValue('')
      self.obj536.name.setNone()

      self.obj536.GGLabel.setValue(3)
      self.obj536.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(300.0,20.0,self.obj536)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj536.graphObject_ = new_obj
      self.obj5360= AttrCalc()
      self.obj5360.Copy=ATOM3Boolean()
      self.obj5360.Copy.setValue(('Copy from LHS', 1))
      self.obj5360.Copy.config = 0
      self.obj5360.Specify=ATOM3Constraint()
      self.obj5360.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj536.GGset2Any['name']= self.obj5360

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj536)
      self.obj536.postAction( self.RHS.CREATE )

      self.obj537=Role(parent)
      self.obj537.preAction( self.RHS.CREATE )
      self.obj537.isGraphObjectVisual = True

      if(hasattr(self.obj537, '_setHierarchicalLink')):
        self.obj537._setHierarchicalLink(False)

      # name
      self.obj537.name.setValue('')
      self.obj537.name.setNone()

      self.obj537.GGLabel.setValue(4)
      self.obj537.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(320.0,180.0,self.obj537)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj537.graphObject_ = new_obj
      self.obj5370= AttrCalc()
      self.obj5370.Copy=ATOM3Boolean()
      self.obj5370.Copy.setValue(('Copy from LHS', 1))
      self.obj5370.Copy.config = 0
      self.obj5370.Specify=ATOM3Constraint()
      self.obj5370.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj537.GGset2Any['name']= self.obj5370

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj537)
      self.obj537.postAction( self.RHS.CREATE )

      self.obj538=posses(parent)
      self.obj538.preAction( self.RHS.CREATE )
      self.obj538.isGraphObjectVisual = True

      if(hasattr(self.obj538, '_setHierarchicalLink')):
        self.obj538._setHierarchicalLink(False)

      # rate
      self.obj538.rate.setNone()

      self.obj538.GGLabel.setValue(5)
      self.obj538.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(203.0,70.5,self.obj538)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj538.graphObject_ = new_obj
      self.obj5380= AttrCalc()
      self.obj5380.Copy=ATOM3Boolean()
      self.obj5380.Copy.setValue(('Copy from LHS', 1))
      self.obj5380.Copy.config = 0
      self.obj5380.Specify=ATOM3Constraint()
      self.obj5380.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj538.GGset2Any['rate']= self.obj5380

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj538)
      self.obj538.postAction( self.RHS.CREATE )

      self.obj539=posses(parent)
      self.obj539.preAction( self.RHS.CREATE )
      self.obj539.isGraphObjectVisual = True

      if(hasattr(self.obj539, '_setHierarchicalLink')):
        self.obj539._setHierarchicalLink(False)

      # rate
      self.obj539.rate.setNone()

      self.obj539.GGLabel.setValue(6)
      self.obj539.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(93.0,130.5,self.obj539)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj539.graphObject_ = new_obj
      self.obj5390= AttrCalc()
      self.obj5390.Copy=ATOM3Boolean()
      self.obj5390.Copy.setValue(('Copy from LHS', 1))
      self.obj5390.Copy.config = 0
      self.obj5390.Specify=ATOM3Constraint()
      self.obj5390.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj539.GGset2Any['rate']= self.obj5390

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj539)
      self.obj539.postAction( self.RHS.CREATE )

      self.obj540=CapableOf(parent)
      self.obj540.preAction( self.RHS.CREATE )
      self.obj540.isGraphObjectVisual = True

      if(hasattr(self.obj540, '_setHierarchicalLink')):
        self.obj540._setHierarchicalLink(False)

      # rate
      self.obj540.rate.setValue(0.0)

      self.obj540.GGLabel.setValue(9)
      self.obj540.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(209.5,129.5,self.obj540)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj540.graphObject_ = new_obj
      self.obj5400= AttrCalc()
      self.obj5400.Copy=ATOM3Boolean()
      self.obj5400.Copy.setValue(('Copy from LHS', 1))
      self.obj5400.Copy.config = 0
      self.obj5400.Specify=ATOM3Constraint()
      self.obj5400.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj540.GGset2Any['rate']= self.obj5400

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj540)
      self.obj540.postAction( self.RHS.CREATE )

      self.obj541=require(parent)
      self.obj541.preAction( self.RHS.CREATE )
      self.obj541.isGraphObjectVisual = True

      if(hasattr(self.obj541, '_setHierarchicalLink')):
        self.obj541._setHierarchicalLink(False)

      self.obj541.GGLabel.setValue(7)
      self.obj541.graphClass_= graph_require
      if parent.genGraphics:
         new_obj = graph_require(222.5,180.0,self.obj541)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj541.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj541)
      self.obj541.postAction( self.RHS.CREATE )

      self.obj542=require(parent)
      self.obj542.preAction( self.RHS.CREATE )
      self.obj542.isGraphObjectVisual = True

      if(hasattr(self.obj542, '_setHierarchicalLink')):
        self.obj542._setHierarchicalLink(False)

      self.obj542.GGLabel.setValue(8)
      self.obj542.graphClass_= graph_require
      if parent.genGraphics:
         new_obj = graph_require(332.5,120.0,self.obj542)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj542.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj542)
      self.obj542.postAction( self.RHS.CREATE )

      self.obj534.out_connections_.append(self.obj538)
      self.obj538.in_connections_.append(self.obj534)
      self.obj534.out_connections_.append(self.obj539)
      self.obj539.in_connections_.append(self.obj534)
      self.obj534.graphObject_.pendingConnections.append((self.obj534.graphObject_.tag, self.obj539.graphObject_.tag, [97.0, 82.0, 93.0, 130.5], 2, 0))
      self.obj534.out_connections_.append(self.obj540)
      self.obj540.in_connections_.append(self.obj534)
      self.obj534.graphObject_.pendingConnections.append((self.obj534.graphObject_.tag, self.obj540.graphObject_.tag, [97.0, 82.0, 209.5, 129.5], 2, 0))
      self.obj537.out_connections_.append(self.obj541)
      self.obj541.in_connections_.append(self.obj537)
      self.obj537.graphObject_.pendingConnections.append((self.obj537.graphObject_.tag, self.obj541.graphObject_.tag, [351.0, 180.0, 222.5, 180.0], 2, 0))
      self.obj537.out_connections_.append(self.obj542)
      self.obj542.in_connections_.append(self.obj537)
      self.obj537.graphObject_.pendingConnections.append((self.obj537.graphObject_.tag, self.obj542.graphObject_.tag, [351.0, 180.0, 332.5, 120.0], 2, 0))
      self.obj538.out_connections_.append(self.obj536)
      self.obj536.in_connections_.append(self.obj538)
      self.obj538.graphObject_.pendingConnections.append((self.obj538.graphObject_.tag, self.obj536.graphObject_.tag, [331.0, 63.0, 203.0, 70.5], 2, 0))
      self.obj539.out_connections_.append(self.obj535)
      self.obj535.in_connections_.append(self.obj539)
      self.obj539.graphObject_.pendingConnections.append((self.obj539.graphObject_.tag, self.obj535.graphObject_.tag, [111.0, 183.0, 93.0, 130.5], 2, 0))
      self.obj540.out_connections_.append(self.obj537)
      self.obj537.in_connections_.append(self.obj540)
      self.obj540.graphObject_.pendingConnections.append((self.obj540.graphObject_.tag, self.obj537.graphObject_.tag, [351.0, 180.0, 209.5, 129.5], 2, 0))
      self.obj541.out_connections_.append(self.obj535)
      self.obj535.in_connections_.append(self.obj541)
      self.obj541.graphObject_.pendingConnections.append((self.obj541.graphObject_.tag, self.obj535.graphObject_.tag, [111.0, 183.0, 222.5, 180.0], 2, 0))
      self.obj542.out_connections_.append(self.obj536)
      self.obj536.in_connections_.append(self.obj542)

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
      
      

