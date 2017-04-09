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

      self.obj91=Agent(parent)
      self.obj91.preAction( self.LHS.CREATE )
      self.obj91.isGraphObjectVisual = True

      if(hasattr(self.obj91, '_setHierarchicalLink')):
        self.obj91._setHierarchicalLink(False)

      # price
      self.obj91.price.setNone()

      # name
      self.obj91.name.setValue('')
      self.obj91.name.setNone()

      self.obj91.GGLabel.setValue(1)
      self.obj91.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(60.0,20.0,self.obj91)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj91.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj91)
      self.obj91.postAction( self.LHS.CREATE )

      self.obj92=Capabilitie(parent)
      self.obj92.preAction( self.LHS.CREATE )
      self.obj92.isGraphObjectVisual = True

      if(hasattr(self.obj92, '_setHierarchicalLink')):
        self.obj92._setHierarchicalLink(False)

      # name
      self.obj92.name.setValue('')
      self.obj92.name.setNone()

      self.obj92.GGLabel.setValue(2)
      self.obj92.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(80.0,180.0,self.obj92)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj92.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj92)
      self.obj92.postAction( self.LHS.CREATE )

      self.obj93=Capabilitie(parent)
      self.obj93.preAction( self.LHS.CREATE )
      self.obj93.isGraphObjectVisual = True

      if(hasattr(self.obj93, '_setHierarchicalLink')):
        self.obj93._setHierarchicalLink(False)

      # name
      self.obj93.name.setValue('')
      self.obj93.name.setNone()

      self.obj93.GGLabel.setValue(3)
      self.obj93.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(300.0,20.0,self.obj93)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj93.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj93)
      self.obj93.postAction( self.LHS.CREATE )

      self.obj94=Role(parent)
      self.obj94.preAction( self.LHS.CREATE )
      self.obj94.isGraphObjectVisual = True

      if(hasattr(self.obj94, '_setHierarchicalLink')):
        self.obj94._setHierarchicalLink(False)

      # name
      self.obj94.name.setValue('')
      self.obj94.name.setNone()

      self.obj94.GGLabel.setValue(4)
      self.obj94.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(320.0,180.0,self.obj94)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj94.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj94)
      self.obj94.postAction( self.LHS.CREATE )

      self.obj95=posses(parent)
      self.obj95.preAction( self.LHS.CREATE )
      self.obj95.isGraphObjectVisual = True

      if(hasattr(self.obj95, '_setHierarchicalLink')):
        self.obj95._setHierarchicalLink(False)

      # rate
      self.obj95.rate.setNone()

      self.obj95.GGLabel.setValue(5)
      self.obj95.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(203.0,70.5,self.obj95)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj95.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj95)
      self.obj95.postAction( self.LHS.CREATE )

      self.obj96=posses(parent)
      self.obj96.preAction( self.LHS.CREATE )
      self.obj96.isGraphObjectVisual = True

      if(hasattr(self.obj96, '_setHierarchicalLink')):
        self.obj96._setHierarchicalLink(False)

      # rate
      self.obj96.rate.setNone()

      self.obj96.GGLabel.setValue(6)
      self.obj96.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(93.0,130.5,self.obj96)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj96.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj96)
      self.obj96.postAction( self.LHS.CREATE )

      self.obj97=CapableOf(parent)
      self.obj97.preAction( self.LHS.CREATE )
      self.obj97.isGraphObjectVisual = True

      if(hasattr(self.obj97, '_setHierarchicalLink')):
        self.obj97._setHierarchicalLink(False)

      # rate
      self.obj97.rate.setNone()

      self.obj97.GGLabel.setValue(9)
      self.obj97.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(209.5,129.5,self.obj97)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj97.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj97)
      self.obj97.postAction( self.LHS.CREATE )

      self.obj98=require(parent)
      self.obj98.preAction( self.LHS.CREATE )
      self.obj98.isGraphObjectVisual = True

      if(hasattr(self.obj98, '_setHierarchicalLink')):
        self.obj98._setHierarchicalLink(False)

      self.obj98.GGLabel.setValue(7)
      self.obj98.graphClass_= graph_require
      if parent.genGraphics:
         new_obj = graph_require(222.5,180.0,self.obj98)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj98.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj98)
      self.obj98.postAction( self.LHS.CREATE )

      self.obj99=require(parent)
      self.obj99.preAction( self.LHS.CREATE )
      self.obj99.isGraphObjectVisual = True

      if(hasattr(self.obj99, '_setHierarchicalLink')):
        self.obj99._setHierarchicalLink(False)

      self.obj99.GGLabel.setValue(8)
      self.obj99.graphClass_= graph_require
      if parent.genGraphics:
         new_obj = graph_require(332.5,120.0,self.obj99)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj99.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj99)
      self.obj99.postAction( self.LHS.CREATE )

      self.obj91.out_connections_.append(self.obj95)
      self.obj95.in_connections_.append(self.obj91)
      self.obj91.out_connections_.append(self.obj96)
      self.obj96.in_connections_.append(self.obj91)
      self.obj91.graphObject_.pendingConnections.append((self.obj91.graphObject_.tag, self.obj96.graphObject_.tag, [85.0, 82.0, 93.0, 130.5], 0, True))
      self.obj91.out_connections_.append(self.obj97)
      self.obj97.in_connections_.append(self.obj91)
      self.obj91.graphObject_.pendingConnections.append((self.obj91.graphObject_.tag, self.obj97.graphObject_.tag, [85.0, 82.0, 163.0, 138.0, 209.5, 129.5], 2, True))
      self.obj94.out_connections_.append(self.obj98)
      self.obj98.in_connections_.append(self.obj94)
      self.obj94.graphObject_.pendingConnections.append((self.obj94.graphObject_.tag, self.obj98.graphObject_.tag, [344.0, 181.0, 222.5, 180.0], 0, True))
      self.obj94.out_connections_.append(self.obj99)
      self.obj99.in_connections_.append(self.obj94)
      self.obj94.graphObject_.pendingConnections.append((self.obj94.graphObject_.tag, self.obj99.graphObject_.tag, [344.0, 181.0, 332.5, 120.0], 0, True))
      self.obj95.out_connections_.append(self.obj93)
      self.obj93.in_connections_.append(self.obj95)
      self.obj95.graphObject_.pendingConnections.append((self.obj95.graphObject_.tag, self.obj93.graphObject_.tag, [321.0, 59.0, 203.0, 70.5], 0, True))
      self.obj96.out_connections_.append(self.obj92)
      self.obj92.in_connections_.append(self.obj96)
      self.obj96.graphObject_.pendingConnections.append((self.obj96.graphObject_.tag, self.obj92.graphObject_.tag, [101.0, 179.0, 93.0, 130.5], 0, True))
      self.obj97.out_connections_.append(self.obj94)
      self.obj94.in_connections_.append(self.obj97)
      self.obj97.graphObject_.pendingConnections.append((self.obj97.graphObject_.tag, self.obj94.graphObject_.tag, [344.0, 181.0, 256.0, 121.0, 209.5, 129.5], 2, True))
      self.obj98.out_connections_.append(self.obj92)
      self.obj92.in_connections_.append(self.obj98)
      self.obj98.graphObject_.pendingConnections.append((self.obj98.graphObject_.tag, self.obj92.graphObject_.tag, [101.0, 179.0, 222.5, 180.0], 0, True))
      self.obj99.out_connections_.append(self.obj93)
      self.obj93.in_connections_.append(self.obj99)

      self.RHS = ASG_omacs(parent)

      self.obj101=Agent(parent)
      self.obj101.preAction( self.RHS.CREATE )
      self.obj101.isGraphObjectVisual = True

      if(hasattr(self.obj101, '_setHierarchicalLink')):
        self.obj101._setHierarchicalLink(False)

      # price
      self.obj101.price.setNone()

      # name
      self.obj101.name.setValue('')
      self.obj101.name.setNone()

      self.obj101.GGLabel.setValue(1)
      self.obj101.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(60.0,20.0,self.obj101)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj101.graphObject_ = new_obj
      self.obj1010= AttrCalc()
      self.obj1010.Copy=ATOM3Boolean()
      self.obj1010.Copy.setValue(('Copy from LHS', 1))
      self.obj1010.Copy.config = 0
      self.obj1010.Specify=ATOM3Constraint()
      self.obj1010.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj101.GGset2Any['price']= self.obj1010
      self.obj1011= AttrCalc()
      self.obj1011.Copy=ATOM3Boolean()
      self.obj1011.Copy.setValue(('Copy from LHS', 1))
      self.obj1011.Copy.config = 0
      self.obj1011.Specify=ATOM3Constraint()
      self.obj1011.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj101.GGset2Any['name']= self.obj1011

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj101)
      self.obj101.postAction( self.RHS.CREATE )

      self.obj102=Capabilitie(parent)
      self.obj102.preAction( self.RHS.CREATE )
      self.obj102.isGraphObjectVisual = True

      if(hasattr(self.obj102, '_setHierarchicalLink')):
        self.obj102._setHierarchicalLink(False)

      # name
      self.obj102.name.setValue('')
      self.obj102.name.setNone()

      self.obj102.GGLabel.setValue(2)
      self.obj102.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(80.0,180.0,self.obj102)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj102.graphObject_ = new_obj
      self.obj1020= AttrCalc()
      self.obj1020.Copy=ATOM3Boolean()
      self.obj1020.Copy.setValue(('Copy from LHS', 1))
      self.obj1020.Copy.config = 0
      self.obj1020.Specify=ATOM3Constraint()
      self.obj1020.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj102.GGset2Any['name']= self.obj1020

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj102)
      self.obj102.postAction( self.RHS.CREATE )

      self.obj103=Capabilitie(parent)
      self.obj103.preAction( self.RHS.CREATE )
      self.obj103.isGraphObjectVisual = True

      if(hasattr(self.obj103, '_setHierarchicalLink')):
        self.obj103._setHierarchicalLink(False)

      # name
      self.obj103.name.setValue('')
      self.obj103.name.setNone()

      self.obj103.GGLabel.setValue(3)
      self.obj103.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(300.0,20.0,self.obj103)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj103.graphObject_ = new_obj
      self.obj1030= AttrCalc()
      self.obj1030.Copy=ATOM3Boolean()
      self.obj1030.Copy.setValue(('Copy from LHS', 1))
      self.obj1030.Copy.config = 0
      self.obj1030.Specify=ATOM3Constraint()
      self.obj1030.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj103.GGset2Any['name']= self.obj1030

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj103)
      self.obj103.postAction( self.RHS.CREATE )

      self.obj104=Role(parent)
      self.obj104.preAction( self.RHS.CREATE )
      self.obj104.isGraphObjectVisual = True

      if(hasattr(self.obj104, '_setHierarchicalLink')):
        self.obj104._setHierarchicalLink(False)

      # name
      self.obj104.name.setValue('')
      self.obj104.name.setNone()

      self.obj104.GGLabel.setValue(4)
      self.obj104.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(320.0,180.0,self.obj104)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj104.graphObject_ = new_obj
      self.obj1040= AttrCalc()
      self.obj1040.Copy=ATOM3Boolean()
      self.obj1040.Copy.setValue(('Copy from LHS', 1))
      self.obj1040.Copy.config = 0
      self.obj1040.Specify=ATOM3Constraint()
      self.obj1040.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj104.GGset2Any['name']= self.obj1040

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj104)
      self.obj104.postAction( self.RHS.CREATE )

      self.obj105=posses(parent)
      self.obj105.preAction( self.RHS.CREATE )
      self.obj105.isGraphObjectVisual = True

      if(hasattr(self.obj105, '_setHierarchicalLink')):
        self.obj105._setHierarchicalLink(False)

      # rate
      self.obj105.rate.setNone()

      self.obj105.GGLabel.setValue(5)
      self.obj105.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(203.0,70.5,self.obj105)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj105.graphObject_ = new_obj
      self.obj1050= AttrCalc()
      self.obj1050.Copy=ATOM3Boolean()
      self.obj1050.Copy.setValue(('Copy from LHS', 1))
      self.obj1050.Copy.config = 0
      self.obj1050.Specify=ATOM3Constraint()
      self.obj1050.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj105.GGset2Any['rate']= self.obj1050

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj105)
      self.obj105.postAction( self.RHS.CREATE )

      self.obj106=posses(parent)
      self.obj106.preAction( self.RHS.CREATE )
      self.obj106.isGraphObjectVisual = True

      if(hasattr(self.obj106, '_setHierarchicalLink')):
        self.obj106._setHierarchicalLink(False)

      # rate
      self.obj106.rate.setNone()

      self.obj106.GGLabel.setValue(6)
      self.obj106.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(93.0,130.5,self.obj106)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj106.graphObject_ = new_obj
      self.obj1060= AttrCalc()
      self.obj1060.Copy=ATOM3Boolean()
      self.obj1060.Copy.setValue(('Copy from LHS', 1))
      self.obj1060.Copy.config = 0
      self.obj1060.Specify=ATOM3Constraint()
      self.obj1060.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj106.GGset2Any['rate']= self.obj1060

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj106)
      self.obj106.postAction( self.RHS.CREATE )

      self.obj107=CapableOf(parent)
      self.obj107.preAction( self.RHS.CREATE )
      self.obj107.isGraphObjectVisual = True

      if(hasattr(self.obj107, '_setHierarchicalLink')):
        self.obj107._setHierarchicalLink(False)

      # rate
      self.obj107.rate.setValue(0.0)

      self.obj107.GGLabel.setValue(9)
      self.obj107.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(209.5,129.5,self.obj107)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj107.graphObject_ = new_obj
      self.obj1070= AttrCalc()
      self.obj1070.Copy=ATOM3Boolean()
      self.obj1070.Copy.setValue(('Copy from LHS', 1))
      self.obj1070.Copy.config = 0
      self.obj1070.Specify=ATOM3Constraint()
      self.obj1070.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj107.GGset2Any['rate']= self.obj1070

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj107)
      self.obj107.postAction( self.RHS.CREATE )

      self.obj108=require(parent)
      self.obj108.preAction( self.RHS.CREATE )
      self.obj108.isGraphObjectVisual = True

      if(hasattr(self.obj108, '_setHierarchicalLink')):
        self.obj108._setHierarchicalLink(False)

      self.obj108.GGLabel.setValue(7)
      self.obj108.graphClass_= graph_require
      if parent.genGraphics:
         new_obj = graph_require(222.5,180.0,self.obj108)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj108.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj108)
      self.obj108.postAction( self.RHS.CREATE )

      self.obj109=require(parent)
      self.obj109.preAction( self.RHS.CREATE )
      self.obj109.isGraphObjectVisual = True

      if(hasattr(self.obj109, '_setHierarchicalLink')):
        self.obj109._setHierarchicalLink(False)

      self.obj109.GGLabel.setValue(8)
      self.obj109.graphClass_= graph_require
      if parent.genGraphics:
         new_obj = graph_require(332.5,120.0,self.obj109)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj109.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj109)
      self.obj109.postAction( self.RHS.CREATE )

      self.obj101.out_connections_.append(self.obj105)
      self.obj105.in_connections_.append(self.obj101)
      self.obj101.out_connections_.append(self.obj106)
      self.obj106.in_connections_.append(self.obj101)
      self.obj101.graphObject_.pendingConnections.append((self.obj101.graphObject_.tag, self.obj106.graphObject_.tag, [97.0, 82.0, 93.0, 130.5], 2, 0))
      self.obj101.out_connections_.append(self.obj107)
      self.obj107.in_connections_.append(self.obj101)
      self.obj101.graphObject_.pendingConnections.append((self.obj101.graphObject_.tag, self.obj107.graphObject_.tag, [97.0, 82.0, 209.5, 129.5], 2, 0))
      self.obj104.out_connections_.append(self.obj108)
      self.obj108.in_connections_.append(self.obj104)
      self.obj104.graphObject_.pendingConnections.append((self.obj104.graphObject_.tag, self.obj108.graphObject_.tag, [351.0, 180.0, 222.5, 180.0], 2, 0))
      self.obj104.out_connections_.append(self.obj109)
      self.obj109.in_connections_.append(self.obj104)
      self.obj104.graphObject_.pendingConnections.append((self.obj104.graphObject_.tag, self.obj109.graphObject_.tag, [351.0, 180.0, 332.5, 120.0], 2, 0))
      self.obj105.out_connections_.append(self.obj103)
      self.obj103.in_connections_.append(self.obj105)
      self.obj105.graphObject_.pendingConnections.append((self.obj105.graphObject_.tag, self.obj103.graphObject_.tag, [331.0, 63.0, 203.0, 70.5], 2, 0))
      self.obj106.out_connections_.append(self.obj102)
      self.obj102.in_connections_.append(self.obj106)
      self.obj106.graphObject_.pendingConnections.append((self.obj106.graphObject_.tag, self.obj102.graphObject_.tag, [111.0, 183.0, 93.0, 130.5], 2, 0))
      self.obj107.out_connections_.append(self.obj104)
      self.obj104.in_connections_.append(self.obj107)
      self.obj107.graphObject_.pendingConnections.append((self.obj107.graphObject_.tag, self.obj104.graphObject_.tag, [351.0, 180.0, 209.5, 129.5], 2, 0))
      self.obj108.out_connections_.append(self.obj102)
      self.obj102.in_connections_.append(self.obj108)
      self.obj108.graphObject_.pendingConnections.append((self.obj108.graphObject_.tag, self.obj102.graphObject_.tag, [111.0, 183.0, 222.5, 180.0], 2, 0))
      self.obj109.out_connections_.append(self.obj103)
      self.obj103.in_connections_.append(self.obj109)

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
      
      

