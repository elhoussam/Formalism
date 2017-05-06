# _ Agent2RoleLink1_GG_rule.py ____________________________________________________________________________
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
class Agent2RoleLink1_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 1)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_omacs(parent)

      self.obj508=Agent(parent)
      self.obj508.preAction( self.LHS.CREATE )
      self.obj508.isGraphObjectVisual = True

      if(hasattr(self.obj508, '_setHierarchicalLink')):
        self.obj508._setHierarchicalLink(False)

      # price
      self.obj508.price.setNone()

      # name
      self.obj508.name.setValue('')
      self.obj508.name.setNone()

      self.obj508.GGLabel.setValue(1)
      self.obj508.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(80.0,20.0,self.obj508)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj508.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj508)
      self.obj508.postAction( self.LHS.CREATE )

      self.obj509=Capabilitie(parent)
      self.obj509.preAction( self.LHS.CREATE )
      self.obj509.isGraphObjectVisual = True

      if(hasattr(self.obj509, '_setHierarchicalLink')):
        self.obj509._setHierarchicalLink(False)

      # name
      self.obj509.name.setValue('')
      self.obj509.name.setNone()

      self.obj509.GGLabel.setValue(2)
      self.obj509.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(160.0,180.0,self.obj509)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj509.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj509)
      self.obj509.postAction( self.LHS.CREATE )

      self.obj510=Role(parent)
      self.obj510.preAction( self.LHS.CREATE )
      self.obj510.isGraphObjectVisual = True

      if(hasattr(self.obj510, '_setHierarchicalLink')):
        self.obj510._setHierarchicalLink(False)

      # name
      self.obj510.name.setValue('')
      self.obj510.name.setNone()

      self.obj510.GGLabel.setValue(3)
      self.obj510.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(280.0,40.0,self.obj510)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj510.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj510)
      self.obj510.postAction( self.LHS.CREATE )

      self.obj511=posses(parent)
      self.obj511.preAction( self.LHS.CREATE )
      self.obj511.isGraphObjectVisual = True

      if(hasattr(self.obj511, '_setHierarchicalLink')):
        self.obj511._setHierarchicalLink(False)

      # rate
      self.obj511.rate.setNone()

      self.obj511.GGLabel.setValue(4)
      self.obj511.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(143.0,130.5,self.obj511)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj511.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj511)
      self.obj511.postAction( self.LHS.CREATE )

      self.obj512=require(parent)
      self.obj512.preAction( self.LHS.CREATE )
      self.obj512.isGraphObjectVisual = True

      if(hasattr(self.obj512, '_setHierarchicalLink')):
        self.obj512._setHierarchicalLink(False)

      self.obj512.GGLabel.setValue(5)
      self.obj512.graphClass_= graph_require
      if parent.genGraphics:
         new_obj = graph_require(242.5,132.5,self.obj512)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj512.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj512)
      self.obj512.postAction( self.LHS.CREATE )

      self.obj508.out_connections_.append(self.obj511)
      self.obj511.in_connections_.append(self.obj508)
      self.obj508.graphObject_.pendingConnections.append((self.obj508.graphObject_.tag, self.obj511.graphObject_.tag, [105.0, 82.0, 143.0, 130.5], 0, True))
      self.obj510.out_connections_.append(self.obj512)
      self.obj512.in_connections_.append(self.obj510)
      self.obj510.graphObject_.pendingConnections.append((self.obj510.graphObject_.tag, self.obj512.graphObject_.tag, [304.0, 86.0, 242.5, 132.5], 0, True))
      self.obj511.out_connections_.append(self.obj509)
      self.obj509.in_connections_.append(self.obj511)
      self.obj511.graphObject_.pendingConnections.append((self.obj511.graphObject_.tag, self.obj509.graphObject_.tag, [181.0, 179.0, 143.0, 130.5], 0, True))
      self.obj512.out_connections_.append(self.obj509)
      self.obj509.in_connections_.append(self.obj512)
      self.obj512.graphObject_.pendingConnections.append((self.obj512.graphObject_.tag, self.obj509.graphObject_.tag, [181.0, 179.0, 242.5, 132.5], 0, True))

      self.RHS = ASG_omacs(parent)

      self.obj514=Agent(parent)
      self.obj514.preAction( self.RHS.CREATE )
      self.obj514.isGraphObjectVisual = True

      if(hasattr(self.obj514, '_setHierarchicalLink')):
        self.obj514._setHierarchicalLink(False)

      # price
      self.obj514.price.setNone()

      # name
      self.obj514.name.setValue('')
      self.obj514.name.setNone()

      self.obj514.GGLabel.setValue(1)
      self.obj514.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(80.0,20.0,self.obj514)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj514.graphObject_ = new_obj
      self.obj5140= AttrCalc()
      self.obj5140.Copy=ATOM3Boolean()
      self.obj5140.Copy.setValue(('Copy from LHS', 1))
      self.obj5140.Copy.config = 0
      self.obj5140.Specify=ATOM3Constraint()
      self.obj5140.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj514.GGset2Any['price']= self.obj5140
      self.obj5141= AttrCalc()
      self.obj5141.Copy=ATOM3Boolean()
      self.obj5141.Copy.setValue(('Copy from LHS', 1))
      self.obj5141.Copy.config = 0
      self.obj5141.Specify=ATOM3Constraint()
      self.obj5141.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj514.GGset2Any['name']= self.obj5141

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj514)
      self.obj514.postAction( self.RHS.CREATE )

      self.obj515=Capabilitie(parent)
      self.obj515.preAction( self.RHS.CREATE )
      self.obj515.isGraphObjectVisual = True

      if(hasattr(self.obj515, '_setHierarchicalLink')):
        self.obj515._setHierarchicalLink(False)

      # name
      self.obj515.name.setValue('')
      self.obj515.name.setNone()

      self.obj515.GGLabel.setValue(2)
      self.obj515.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(160.0,180.0,self.obj515)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj515.graphObject_ = new_obj
      self.obj5150= AttrCalc()
      self.obj5150.Copy=ATOM3Boolean()
      self.obj5150.Copy.setValue(('Copy from LHS', 1))
      self.obj5150.Copy.config = 0
      self.obj5150.Specify=ATOM3Constraint()
      self.obj5150.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj515.GGset2Any['name']= self.obj5150

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj515)
      self.obj515.postAction( self.RHS.CREATE )

      self.obj516=Role(parent)
      self.obj516.preAction( self.RHS.CREATE )
      self.obj516.isGraphObjectVisual = True

      if(hasattr(self.obj516, '_setHierarchicalLink')):
        self.obj516._setHierarchicalLink(False)

      # name
      self.obj516.name.setValue('')
      self.obj516.name.setNone()

      self.obj516.GGLabel.setValue(3)
      self.obj516.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(280.0,40.0,self.obj516)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj516.graphObject_ = new_obj
      self.obj5160= AttrCalc()
      self.obj5160.Copy=ATOM3Boolean()
      self.obj5160.Copy.setValue(('Copy from LHS', 1))
      self.obj5160.Copy.config = 0
      self.obj5160.Specify=ATOM3Constraint()
      self.obj5160.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj516.GGset2Any['name']= self.obj5160

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj516)
      self.obj516.postAction( self.RHS.CREATE )

      self.obj517=posses(parent)
      self.obj517.preAction( self.RHS.CREATE )
      self.obj517.isGraphObjectVisual = True

      if(hasattr(self.obj517, '_setHierarchicalLink')):
        self.obj517._setHierarchicalLink(False)

      # rate
      self.obj517.rate.setNone()

      self.obj517.GGLabel.setValue(4)
      self.obj517.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(143.0,130.5,self.obj517)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj517.graphObject_ = new_obj
      self.obj5170= AttrCalc()
      self.obj5170.Copy=ATOM3Boolean()
      self.obj5170.Copy.setValue(('Copy from LHS', 1))
      self.obj5170.Copy.config = 0
      self.obj5170.Specify=ATOM3Constraint()
      self.obj5170.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj517.GGset2Any['rate']= self.obj5170

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj517)
      self.obj517.postAction( self.RHS.CREATE )

      self.obj518=CapableOf(parent)
      self.obj518.preAction( self.RHS.CREATE )
      self.obj518.isGraphObjectVisual = True

      if(hasattr(self.obj518, '_setHierarchicalLink')):
        self.obj518._setHierarchicalLink(False)

      # rate
      self.obj518.rate.setValue(0.0)

      self.obj518.GGLabel.setValue(7)
      self.obj518.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(214.0,83.5,self.obj518)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj518.graphObject_ = new_obj
      self.obj5180= AttrCalc()
      self.obj5180.Copy=ATOM3Boolean()
      self.obj5180.Copy.setValue(('Copy from LHS', 1))
      self.obj5180.Copy.config = 0
      self.obj5180.Specify=ATOM3Constraint()
      self.obj5180.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj518.GGset2Any['rate']= self.obj5180

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj518)
      self.obj518.postAction( self.RHS.CREATE )

      self.obj519=require(parent)
      self.obj519.preAction( self.RHS.CREATE )
      self.obj519.isGraphObjectVisual = True

      if(hasattr(self.obj519, '_setHierarchicalLink')):
        self.obj519._setHierarchicalLink(False)

      self.obj519.GGLabel.setValue(5)
      self.obj519.graphClass_= graph_require
      if parent.genGraphics:
         new_obj = graph_require(242.5,132.5,self.obj519)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj519.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj519)
      self.obj519.postAction( self.RHS.CREATE )

      self.obj514.out_connections_.append(self.obj517)
      self.obj517.in_connections_.append(self.obj514)
      self.obj514.graphObject_.pendingConnections.append((self.obj514.graphObject_.tag, self.obj517.graphObject_.tag, [117.0, 82.0, 143.0, 130.5], 2, 0))
      self.obj514.out_connections_.append(self.obj518)
      self.obj518.in_connections_.append(self.obj514)
      self.obj514.graphObject_.pendingConnections.append((self.obj514.graphObject_.tag, self.obj518.graphObject_.tag, [117.0, 82.0, 214.0, 83.5], 0, True))
      self.obj516.out_connections_.append(self.obj519)
      self.obj519.in_connections_.append(self.obj516)
      self.obj516.graphObject_.pendingConnections.append((self.obj516.graphObject_.tag, self.obj519.graphObject_.tag, [311.0, 85.0, 242.5, 132.5], 2, 0))
      self.obj517.out_connections_.append(self.obj515)
      self.obj515.in_connections_.append(self.obj517)
      self.obj517.graphObject_.pendingConnections.append((self.obj517.graphObject_.tag, self.obj515.graphObject_.tag, [191.0, 183.0, 143.0, 130.5], 2, 0))
      self.obj518.out_connections_.append(self.obj516)
      self.obj516.in_connections_.append(self.obj518)
      self.obj518.graphObject_.pendingConnections.append((self.obj518.graphObject_.tag, self.obj516.graphObject_.tag, [311.0, 85.0, 214.0, 83.5], 0, True))
      self.obj519.out_connections_.append(self.obj515)
      self.obj515.in_connections_.append(self.obj519)
      self.obj519.graphObject_.pendingConnections.append((self.obj519.graphObject_.tag, self.obj515.graphObject_.tag, [191.0, 183.0, 242.5, 132.5], 2, 0))

   def condition(self, graphID, isograph, atom3i):
      agent = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      
      role = self.getMatched(graphID, self.LHS.nodeWithLabel(3))
      return not ( hasattr(agent, role.name.getValue()) and hasattr(role, agent.name.getValue() ) )
      
      

   def action(self, graphID, isograph, atom3i):
      ag = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) )
      c1 = self.getMatched ( graphID , self.LHS.nodeWithLabel(2) )
      role = self.getMatched ( graphID , self.LHS.nodeWithLabel(3) )
      setattr(ag ,role.name.getValue(),True )
      setattr(role ,ag.name.getValue(),True )
      
      setattr( c1 ,  ag.name.getValue() , True )
      setattr( c1 ,  role.name.getValue() , True )
      
      print 'connCt ('+ag.name.getValue()+','+role.name.getValue()+')'
      if not (ag.name.getValue() in self.graphRewritingSystem.Dictag.keys() ) :
       self.graphRewritingSystem.Dictag[ag.name.getValue()] = {}
      if not (c1.name.getValue() in self.graphRewritingSystem.Dictag[ag.name.getValue()].keys() ) :
       self.graphRewritingSystem.Dictag[ag.name.getValue()][c1.name.getValue()]=0
      if not (role.name.getValue() in self.graphRewritingSystem.Dictag[ag.name.getValue()].keys() ) :
       self.graphRewritingSystem.Dictag[ag.name.getValue()][role.name.getValue()]=0   
      
      self.graphRewritingSystem.Dictag[ag.name.getValue()]['nb']=0
      
      print str( self.graphRewritingSystem.Dictag )
      
      

