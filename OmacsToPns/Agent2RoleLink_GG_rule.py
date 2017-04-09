# _ Agent2RoleLink_GG_rule.py ____________________________________________________________________________
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
class Agent2RoleLink_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 1)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_omacs(parent)

      self.obj128=Agent(parent)
      self.obj128.preAction( self.LHS.CREATE )
      self.obj128.isGraphObjectVisual = True

      if(hasattr(self.obj128, '_setHierarchicalLink')):
        self.obj128._setHierarchicalLink(False)

      # price
      self.obj128.price.setNone()

      # name
      self.obj128.name.setValue('')
      self.obj128.name.setNone()

      self.obj128.GGLabel.setValue(1)
      self.obj128.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(80.0,20.0,self.obj128)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj128.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj128)
      self.obj128.postAction( self.LHS.CREATE )

      self.obj129=Capabilitie(parent)
      self.obj129.preAction( self.LHS.CREATE )
      self.obj129.isGraphObjectVisual = True

      if(hasattr(self.obj129, '_setHierarchicalLink')):
        self.obj129._setHierarchicalLink(False)

      # name
      self.obj129.name.setValue('')
      self.obj129.name.setNone()

      self.obj129.GGLabel.setValue(2)
      self.obj129.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(160.0,180.0,self.obj129)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj129.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj129)
      self.obj129.postAction( self.LHS.CREATE )

      self.obj130=Role(parent)
      self.obj130.preAction( self.LHS.CREATE )
      self.obj130.isGraphObjectVisual = True

      if(hasattr(self.obj130, '_setHierarchicalLink')):
        self.obj130._setHierarchicalLink(False)

      # name
      self.obj130.name.setValue('')
      self.obj130.name.setNone()

      self.obj130.GGLabel.setValue(3)
      self.obj130.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(280.0,40.0,self.obj130)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj130.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj130)
      self.obj130.postAction( self.LHS.CREATE )

      self.obj131=posses(parent)
      self.obj131.preAction( self.LHS.CREATE )
      self.obj131.isGraphObjectVisual = True

      if(hasattr(self.obj131, '_setHierarchicalLink')):
        self.obj131._setHierarchicalLink(False)

      # rate
      self.obj131.rate.setNone()

      self.obj131.GGLabel.setValue(4)
      self.obj131.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(143.0,130.5,self.obj131)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj131.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj131)
      self.obj131.postAction( self.LHS.CREATE )

      self.obj134=require(parent)
      self.obj134.preAction( self.LHS.CREATE )
      self.obj134.isGraphObjectVisual = True

      if(hasattr(self.obj134, '_setHierarchicalLink')):
        self.obj134._setHierarchicalLink(False)

      self.obj134.GGLabel.setValue(5)
      self.obj134.graphClass_= graph_require
      if parent.genGraphics:
         new_obj = graph_require(242.5,132.5,self.obj134)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj134.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj134)
      self.obj134.postAction( self.LHS.CREATE )

      self.obj128.out_connections_.append(self.obj131)
      self.obj131.in_connections_.append(self.obj128)
      self.obj128.graphObject_.pendingConnections.append((self.obj128.graphObject_.tag, self.obj131.graphObject_.tag, [105.0, 82.0, 143.0, 130.5], 0, True))
      self.obj130.out_connections_.append(self.obj134)
      self.obj134.in_connections_.append(self.obj130)
      self.obj130.graphObject_.pendingConnections.append((self.obj130.graphObject_.tag, self.obj134.graphObject_.tag, [304.0, 86.0, 242.5, 132.5], 0, True))
      self.obj131.out_connections_.append(self.obj129)
      self.obj129.in_connections_.append(self.obj131)
      self.obj131.graphObject_.pendingConnections.append((self.obj131.graphObject_.tag, self.obj129.graphObject_.tag, [181.0, 179.0, 143.0, 130.5], 0, True))
      self.obj134.out_connections_.append(self.obj129)
      self.obj129.in_connections_.append(self.obj134)
      self.obj134.graphObject_.pendingConnections.append((self.obj134.graphObject_.tag, self.obj129.graphObject_.tag, [181.0, 179.0, 242.5, 132.5], 0, True))

      self.RHS = ASG_omacs(parent)

      self.obj128=Agent(parent)
      self.obj128.preAction( self.RHS.CREATE )
      self.obj128.isGraphObjectVisual = True

      if(hasattr(self.obj128, '_setHierarchicalLink')):
        self.obj128._setHierarchicalLink(False)

      # price
      self.obj128.price.setNone()

      # name
      self.obj128.name.setValue('')
      self.obj128.name.setNone()

      self.obj128.GGLabel.setValue(1)
      self.obj128.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(80.0,20.0,self.obj128)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj128.graphObject_ = new_obj
      self.obj1280= AttrCalc()
      self.obj1280.Copy=ATOM3Boolean()
      self.obj1280.Copy.setValue(('Copy from LHS', 1))
      self.obj1280.Copy.config = 0
      self.obj1280.Specify=ATOM3Constraint()
      self.obj1280.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj128.GGset2Any['price']= self.obj1280
      self.obj1281= AttrCalc()
      self.obj1281.Copy=ATOM3Boolean()
      self.obj1281.Copy.setValue(('Copy from LHS', 1))
      self.obj1281.Copy.config = 0
      self.obj1281.Specify=ATOM3Constraint()
      self.obj1281.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj128.GGset2Any['name']= self.obj1281

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj128)
      self.obj128.postAction( self.RHS.CREATE )

      self.obj129=Capabilitie(parent)
      self.obj129.preAction( self.RHS.CREATE )
      self.obj129.isGraphObjectVisual = True

      if(hasattr(self.obj129, '_setHierarchicalLink')):
        self.obj129._setHierarchicalLink(False)

      # name
      self.obj129.name.setValue('')
      self.obj129.name.setNone()

      self.obj129.GGLabel.setValue(2)
      self.obj129.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(160.0,180.0,self.obj129)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj129.graphObject_ = new_obj
      self.obj1290= AttrCalc()
      self.obj1290.Copy=ATOM3Boolean()
      self.obj1290.Copy.setValue(('Copy from LHS', 1))
      self.obj1290.Copy.config = 0
      self.obj1290.Specify=ATOM3Constraint()
      self.obj1290.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj129.GGset2Any['name']= self.obj1290

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj129)
      self.obj129.postAction( self.RHS.CREATE )

      self.obj130=Role(parent)
      self.obj130.preAction( self.RHS.CREATE )
      self.obj130.isGraphObjectVisual = True

      if(hasattr(self.obj130, '_setHierarchicalLink')):
        self.obj130._setHierarchicalLink(False)

      # name
      self.obj130.name.setValue('')
      self.obj130.name.setNone()

      self.obj130.GGLabel.setValue(3)
      self.obj130.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(280.0,40.0,self.obj130)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj130.graphObject_ = new_obj
      self.obj1300= AttrCalc()
      self.obj1300.Copy=ATOM3Boolean()
      self.obj1300.Copy.setValue(('Copy from LHS', 1))
      self.obj1300.Copy.config = 0
      self.obj1300.Specify=ATOM3Constraint()
      self.obj1300.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj130.GGset2Any['name']= self.obj1300

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj130)
      self.obj130.postAction( self.RHS.CREATE )

      self.obj131=posses(parent)
      self.obj131.preAction( self.RHS.CREATE )
      self.obj131.isGraphObjectVisual = True

      if(hasattr(self.obj131, '_setHierarchicalLink')):
        self.obj131._setHierarchicalLink(False)

      # rate
      self.obj131.rate.setNone()

      self.obj131.GGLabel.setValue(4)
      self.obj131.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(143.0,130.5,self.obj131)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj131.graphObject_ = new_obj
      self.obj1310= AttrCalc()
      self.obj1310.Copy=ATOM3Boolean()
      self.obj1310.Copy.setValue(('Copy from LHS', 1))
      self.obj1310.Copy.config = 0
      self.obj1310.Specify=ATOM3Constraint()
      self.obj1310.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj131.GGset2Any['rate']= self.obj1310

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj131)
      self.obj131.postAction( self.RHS.CREATE )

      self.obj148=CapableOf(parent)
      self.obj148.preAction( self.RHS.CREATE )
      self.obj148.isGraphObjectVisual = True

      if(hasattr(self.obj148, '_setHierarchicalLink')):
        self.obj148._setHierarchicalLink(False)

      self.obj148.GGLabel.setValue(7)
      self.obj148.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(214.0,83.5,self.obj148)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj148.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj148)
      self.obj148.postAction( self.RHS.CREATE )

      self.obj134=require(parent)
      self.obj134.preAction( self.RHS.CREATE )
      self.obj134.isGraphObjectVisual = True

      if(hasattr(self.obj134, '_setHierarchicalLink')):
        self.obj134._setHierarchicalLink(False)

      self.obj134.GGLabel.setValue(5)
      self.obj134.graphClass_= graph_require
      if parent.genGraphics:
         new_obj = graph_require(242.5,132.5,self.obj134)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj134.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj134)
      self.obj134.postAction( self.RHS.CREATE )

      self.obj128.out_connections_.append(self.obj131)
      self.obj131.in_connections_.append(self.obj128)
      self.obj128.graphObject_.pendingConnections.append((self.obj128.graphObject_.tag, self.obj131.graphObject_.tag, [117.0, 82.0, 143.0, 130.5], 2, 0))
      self.obj128.out_connections_.append(self.obj148)
      self.obj148.in_connections_.append(self.obj128)
      self.obj128.graphObject_.pendingConnections.append((self.obj128.graphObject_.tag, self.obj148.graphObject_.tag, [117.0, 82.0, 214.0, 83.5], 0, True))
      self.obj130.out_connections_.append(self.obj134)
      self.obj134.in_connections_.append(self.obj130)
      self.obj130.graphObject_.pendingConnections.append((self.obj130.graphObject_.tag, self.obj134.graphObject_.tag, [311.0, 85.0, 242.5, 132.5], 2, 0))
      self.obj131.out_connections_.append(self.obj129)
      self.obj129.in_connections_.append(self.obj131)
      self.obj131.graphObject_.pendingConnections.append((self.obj131.graphObject_.tag, self.obj129.graphObject_.tag, [191.0, 183.0, 143.0, 130.5], 2, 0))
      self.obj148.out_connections_.append(self.obj130)
      self.obj130.in_connections_.append(self.obj148)
      self.obj148.graphObject_.pendingConnections.append((self.obj148.graphObject_.tag, self.obj130.graphObject_.tag, [311.0, 85.0, 214.0, 83.5], 0, True))
      self.obj134.out_connections_.append(self.obj129)
      self.obj129.in_connections_.append(self.obj134)
      self.obj134.graphObject_.pendingConnections.append((self.obj134.graphObject_.tag, self.obj129.graphObject_.tag, [191.0, 183.0, 242.5, 132.5], 2, 0))

   def condition(self, graphID, isograph, atom3i):
      agent = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      
      role = self.getMatched(graphID, self.LHS.nodeWithLabel(3))
      return not ( hasattr(agent, role.name.getValue()) and hasattr(role, agent.name.getValue() ) )
      

   def action(self, graphID, isograph, atom3i):
      agent = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) )
      
      c1 = self.getMatched ( graphID , self.LHS.nodeWithLabel(2) )
      role = self.getMatched ( graphID , self.LHS.nodeWithLabel(3) )
      setattr(agent ,role.name.getValue(),True )
      setattr(role ,agent.name.getValue(),True )
      
      setattr( c1 ,  agent.name.getValue() , True )
      setattr( c1 ,  role.name.getValue() , True )
      
      print 'connCt ('+agent.name.getValue()+','+role.name.getValue()+')'
      

