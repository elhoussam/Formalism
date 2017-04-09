# _ Agent2RoleLink3_GG_rule.py ____________________________________________________________________________
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
class Agent2RoleLink3_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 3)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_omacs(parent)

      self.obj114=Agent(parent)
      self.obj114.preAction( self.LHS.CREATE )
      self.obj114.isGraphObjectVisual = True

      if(hasattr(self.obj114, '_setHierarchicalLink')):
        self.obj114._setHierarchicalLink(False)

      # price
      self.obj114.price.setNone()

      # name
      self.obj114.name.setValue('')
      self.obj114.name.setNone()

      self.obj114.GGLabel.setValue(1)
      self.obj114.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(100.0,20.0,self.obj114)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj114.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj114)
      self.obj114.postAction( self.LHS.CREATE )

      self.obj115=Capabilitie(parent)
      self.obj115.preAction( self.LHS.CREATE )
      self.obj115.isGraphObjectVisual = True

      if(hasattr(self.obj115, '_setHierarchicalLink')):
        self.obj115._setHierarchicalLink(False)

      # name
      self.obj115.name.setValue('')
      self.obj115.name.setNone()

      self.obj115.GGLabel.setValue(3)
      self.obj115.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(340.0,40.0,self.obj115)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj115.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj115)
      self.obj115.postAction( self.LHS.CREATE )

      self.obj116=Capabilitie(parent)
      self.obj116.preAction( self.LHS.CREATE )
      self.obj116.isGraphObjectVisual = True

      if(hasattr(self.obj116, '_setHierarchicalLink')):
        self.obj116._setHierarchicalLink(False)

      # name
      self.obj116.name.setValue('')
      self.obj116.name.setNone()

      self.obj116.GGLabel.setValue(4)
      self.obj116.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(140.0,160.0,self.obj116)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj116.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj116)
      self.obj116.postAction( self.LHS.CREATE )

      self.obj117=Role(parent)
      self.obj117.preAction( self.LHS.CREATE )
      self.obj117.isGraphObjectVisual = True

      if(hasattr(self.obj117, '_setHierarchicalLink')):
        self.obj117._setHierarchicalLink(False)

      # name
      self.obj117.name.setValue('')
      self.obj117.name.setNone()

      self.obj117.GGLabel.setValue(2)
      self.obj117.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(300.0,140.0,self.obj117)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj117.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj117)
      self.obj117.postAction( self.LHS.CREATE )

      self.obj118=posses(parent)
      self.obj118.preAction( self.LHS.CREATE )
      self.obj118.isGraphObjectVisual = True

      if(hasattr(self.obj118, '_setHierarchicalLink')):
        self.obj118._setHierarchicalLink(False)

      # rate
      self.obj118.rate.setNone()

      self.obj118.GGLabel.setValue(5)
      self.obj118.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(143.0,120.5,self.obj118)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj118.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj118)
      self.obj118.postAction( self.LHS.CREATE )

      self.obj119=CapableOf(parent)
      self.obj119.preAction( self.LHS.CREATE )
      self.obj119.isGraphObjectVisual = True

      if(hasattr(self.obj119, '_setHierarchicalLink')):
        self.obj119._setHierarchicalLink(False)

      # rate
      self.obj119.rate.setNone()

      self.obj119.GGLabel.setValue(8)
      self.obj119.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(224.5,111.5,self.obj119)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj119.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj119)
      self.obj119.postAction( self.LHS.CREATE )

      self.obj120=require(parent)
      self.obj120.preAction( self.LHS.CREATE )
      self.obj120.isGraphObjectVisual = True

      if(hasattr(self.obj120, '_setHierarchicalLink')):
        self.obj120._setHierarchicalLink(False)

      self.obj120.GGLabel.setValue(7)
      self.obj120.graphClass_= graph_require
      if parent.genGraphics:
         new_obj = graph_require(242.5,192.5,self.obj120)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj120.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj120)
      self.obj120.postAction( self.LHS.CREATE )

      self.obj121=require(parent)
      self.obj121.preAction( self.LHS.CREATE )
      self.obj121.isGraphObjectVisual = True

      if(hasattr(self.obj121, '_setHierarchicalLink')):
        self.obj121._setHierarchicalLink(False)

      self.obj121.GGLabel.setValue(9)
      self.obj121.graphClass_= graph_require
      if parent.genGraphics:
         new_obj = graph_require(351.0,111.5,self.obj121)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj121.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj121)
      self.obj121.postAction( self.LHS.CREATE )

      self.obj114.out_connections_.append(self.obj118)
      self.obj118.in_connections_.append(self.obj114)
      self.obj114.graphObject_.pendingConnections.append((self.obj114.graphObject_.tag, self.obj118.graphObject_.tag, [137.0, 82.0, 143.0, 120.5], 2, 0))
      self.obj114.out_connections_.append(self.obj119)
      self.obj119.in_connections_.append(self.obj114)
      self.obj114.graphObject_.pendingConnections.append((self.obj114.graphObject_.tag, self.obj119.graphObject_.tag, [125.0, 82.0, 224.5, 111.5], 0, True))
      self.obj117.out_connections_.append(self.obj120)
      self.obj120.in_connections_.append(self.obj117)
      self.obj117.graphObject_.pendingConnections.append((self.obj117.graphObject_.tag, self.obj120.graphObject_.tag, [324.0, 186.0, 242.5, 192.5], 0, True))
      self.obj117.out_connections_.append(self.obj121)
      self.obj121.in_connections_.append(self.obj117)
      self.obj117.graphObject_.pendingConnections.append((self.obj117.graphObject_.tag, self.obj121.graphObject_.tag, [331.0, 140.0, 351.0, 111.5], 0, True))
      self.obj118.out_connections_.append(self.obj116)
      self.obj116.in_connections_.append(self.obj118)
      self.obj118.graphObject_.pendingConnections.append((self.obj118.graphObject_.tag, self.obj116.graphObject_.tag, [161.0, 159.0, 143.0, 120.5], 0, True))
      self.obj119.out_connections_.append(self.obj117)
      self.obj117.in_connections_.append(self.obj119)
      self.obj119.graphObject_.pendingConnections.append((self.obj119.graphObject_.tag, self.obj117.graphObject_.tag, [324.0, 141.0, 224.5, 111.5], 0, True))
      self.obj120.out_connections_.append(self.obj116)
      self.obj116.in_connections_.append(self.obj120)
      self.obj120.graphObject_.pendingConnections.append((self.obj120.graphObject_.tag, self.obj116.graphObject_.tag, [161.0, 199.0, 242.5, 192.5], 0, True))
      self.obj121.out_connections_.append(self.obj115)
      self.obj115.in_connections_.append(self.obj121)
      self.obj121.graphObject_.pendingConnections.append((self.obj121.graphObject_.tag, self.obj115.graphObject_.tag, [371.0, 83.0, 351.0, 111.5], 0, True))

      self.RHS = ASG_omacs(parent)

      self.obj123=Agent(parent)
      self.obj123.preAction( self.RHS.CREATE )
      self.obj123.isGraphObjectVisual = True

      if(hasattr(self.obj123, '_setHierarchicalLink')):
        self.obj123._setHierarchicalLink(False)

      # price
      self.obj123.price.setNone()

      # name
      self.obj123.name.setValue('')
      self.obj123.name.setNone()

      self.obj123.GGLabel.setValue(1)
      self.obj123.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(100.0,20.0,self.obj123)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj123.graphObject_ = new_obj
      self.obj1230= AttrCalc()
      self.obj1230.Copy=ATOM3Boolean()
      self.obj1230.Copy.setValue(('Copy from LHS', 1))
      self.obj1230.Copy.config = 0
      self.obj1230.Specify=ATOM3Constraint()
      self.obj1230.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj123.GGset2Any['price']= self.obj1230
      self.obj1231= AttrCalc()
      self.obj1231.Copy=ATOM3Boolean()
      self.obj1231.Copy.setValue(('Copy from LHS', 1))
      self.obj1231.Copy.config = 0
      self.obj1231.Specify=ATOM3Constraint()
      self.obj1231.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj123.GGset2Any['name']= self.obj1231

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj123)
      self.obj123.postAction( self.RHS.CREATE )

      self.obj124=Capabilitie(parent)
      self.obj124.preAction( self.RHS.CREATE )
      self.obj124.isGraphObjectVisual = True

      if(hasattr(self.obj124, '_setHierarchicalLink')):
        self.obj124._setHierarchicalLink(False)

      # name
      self.obj124.name.setValue('')
      self.obj124.name.setNone()

      self.obj124.GGLabel.setValue(3)
      self.obj124.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(340.0,40.0,self.obj124)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj124.graphObject_ = new_obj
      self.obj1240= AttrCalc()
      self.obj1240.Copy=ATOM3Boolean()
      self.obj1240.Copy.setValue(('Copy from LHS', 1))
      self.obj1240.Copy.config = 0
      self.obj1240.Specify=ATOM3Constraint()
      self.obj1240.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj124.GGset2Any['name']= self.obj1240

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj124)
      self.obj124.postAction( self.RHS.CREATE )

      self.obj125=Capabilitie(parent)
      self.obj125.preAction( self.RHS.CREATE )
      self.obj125.isGraphObjectVisual = True

      if(hasattr(self.obj125, '_setHierarchicalLink')):
        self.obj125._setHierarchicalLink(False)

      # name
      self.obj125.name.setValue('')
      self.obj125.name.setNone()

      self.obj125.GGLabel.setValue(4)
      self.obj125.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(140.0,160.0,self.obj125)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj125.graphObject_ = new_obj
      self.obj1250= AttrCalc()
      self.obj1250.Copy=ATOM3Boolean()
      self.obj1250.Copy.setValue(('Copy from LHS', 1))
      self.obj1250.Copy.config = 0
      self.obj1250.Specify=ATOM3Constraint()
      self.obj1250.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj125.GGset2Any['name']= self.obj1250

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj125)
      self.obj125.postAction( self.RHS.CREATE )

      self.obj126=Role(parent)
      self.obj126.preAction( self.RHS.CREATE )
      self.obj126.isGraphObjectVisual = True

      if(hasattr(self.obj126, '_setHierarchicalLink')):
        self.obj126._setHierarchicalLink(False)

      # name
      self.obj126.name.setValue('')
      self.obj126.name.setNone()

      self.obj126.GGLabel.setValue(2)
      self.obj126.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(300.0,140.0,self.obj126)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj126.graphObject_ = new_obj
      self.obj1260= AttrCalc()
      self.obj1260.Copy=ATOM3Boolean()
      self.obj1260.Copy.setValue(('Copy from LHS', 1))
      self.obj1260.Copy.config = 0
      self.obj1260.Specify=ATOM3Constraint()
      self.obj1260.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj126.GGset2Any['name']= self.obj1260

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj126)
      self.obj126.postAction( self.RHS.CREATE )

      self.obj127=posses(parent)
      self.obj127.preAction( self.RHS.CREATE )
      self.obj127.isGraphObjectVisual = True

      if(hasattr(self.obj127, '_setHierarchicalLink')):
        self.obj127._setHierarchicalLink(False)

      # rate
      self.obj127.rate.setNone()

      self.obj127.GGLabel.setValue(5)
      self.obj127.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(143.0,120.5,self.obj127)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj127.graphObject_ = new_obj
      self.obj1270= AttrCalc()
      self.obj1270.Copy=ATOM3Boolean()
      self.obj1270.Copy.setValue(('Copy from LHS', 1))
      self.obj1270.Copy.config = 0
      self.obj1270.Specify=ATOM3Constraint()
      self.obj1270.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj127.GGset2Any['rate']= self.obj1270

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj127)
      self.obj127.postAction( self.RHS.CREATE )

      self.obj128=require(parent)
      self.obj128.preAction( self.RHS.CREATE )
      self.obj128.isGraphObjectVisual = True

      if(hasattr(self.obj128, '_setHierarchicalLink')):
        self.obj128._setHierarchicalLink(False)

      self.obj128.GGLabel.setValue(7)
      self.obj128.graphClass_= graph_require
      if parent.genGraphics:
         new_obj = graph_require(242.5,192.5,self.obj128)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj128.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj128)
      self.obj128.postAction( self.RHS.CREATE )

      self.obj129=require(parent)
      self.obj129.preAction( self.RHS.CREATE )
      self.obj129.isGraphObjectVisual = True

      if(hasattr(self.obj129, '_setHierarchicalLink')):
        self.obj129._setHierarchicalLink(False)

      self.obj129.GGLabel.setValue(9)
      self.obj129.graphClass_= graph_require
      if parent.genGraphics:
         new_obj = graph_require(351.0,111.5,self.obj129)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj129.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj129)
      self.obj129.postAction( self.RHS.CREATE )

      self.obj123.out_connections_.append(self.obj127)
      self.obj127.in_connections_.append(self.obj123)
      self.obj123.graphObject_.pendingConnections.append((self.obj123.graphObject_.tag, self.obj127.graphObject_.tag, [137.0, 82.0, 143.0, 120.5], 2, 0))
      self.obj126.out_connections_.append(self.obj128)
      self.obj128.in_connections_.append(self.obj126)
      self.obj126.graphObject_.pendingConnections.append((self.obj126.graphObject_.tag, self.obj128.graphObject_.tag, [331.0, 185.0, 242.5, 192.5], 2, 0))
      self.obj126.out_connections_.append(self.obj129)
      self.obj129.in_connections_.append(self.obj126)
      self.obj126.graphObject_.pendingConnections.append((self.obj126.graphObject_.tag, self.obj129.graphObject_.tag, [331.0, 140.0, 351.0, 111.5], 0, True))
      self.obj127.out_connections_.append(self.obj125)
      self.obj125.in_connections_.append(self.obj127)
      self.obj127.graphObject_.pendingConnections.append((self.obj127.graphObject_.tag, self.obj125.graphObject_.tag, [171.0, 163.0, 143.0, 120.5], 2, 0))
      self.obj128.out_connections_.append(self.obj125)
      self.obj125.in_connections_.append(self.obj128)
      self.obj128.graphObject_.pendingConnections.append((self.obj128.graphObject_.tag, self.obj125.graphObject_.tag, [171.0, 203.0, 242.5, 192.5], 2, 0))
      self.obj129.out_connections_.append(self.obj124)
      self.obj124.in_connections_.append(self.obj129)
      self.obj129.graphObject_.pendingConnections.append((self.obj129.graphObject_.tag, self.obj124.graphObject_.tag, [371.0, 83.0, 351.0, 111.5], 0, True))

   def condition(self, graphID, isograph, atom3i):
      agent = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      role  = self.getMatched(graphID, self.LHS.nodeWithLabel(2))
      c1 = self.getMatched(graphID, self.LHS.nodeWithLabel(3))
      c2 = self.getMatched(graphID, self.LHS.nodeWithLabel(4))
      
      return not ( hasattr(c1,  agent.name.getValue() ) and 
      hasattr(c1,  role.name.getValue() ) and
      hasattr(c2,  agent.name.getValue() ) and  hasattr(c2, role.name.getValue() ) )
      

   def action(self, graphID, isograph, atom3i):
      agent = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      c1 = self.getMatched(graphID, self.LHS.nodeWithLabel(4))
      c2 = self.getMatched(graphID, self.LHS.nodeWithLabel(3))
      role = self.getMatched(graphID, self.LHS.nodeWithLabel(2))
      
      setattr( c1 ,  agent.name.getValue() , True )
      setattr( c1 ,  role.name.getValue() , True )
      
      setattr( c2 ,  agent.name.getValue() , True )
      setattr( c2 ,  role.name.getValue() , True )
      print' Eli : ('+agent.name.getValue()+','+c1.name.getValue()+','+c2.name.getValue()+','+role.name.getValue()+')'
      
      

