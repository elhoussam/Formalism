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

      self.obj1509=Agent(parent)
      self.obj1509.preAction( self.LHS.CREATE )
      self.obj1509.isGraphObjectVisual = True

      if(hasattr(self.obj1509, '_setHierarchicalLink')):
        self.obj1509._setHierarchicalLink(False)

      # price
      self.obj1509.price.setNone()

      # name
      self.obj1509.name.setValue('')
      self.obj1509.name.setNone()

      self.obj1509.GGLabel.setValue(1)
      self.obj1509.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(80.0,20.0,self.obj1509)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1509.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1509)
      self.obj1509.postAction( self.LHS.CREATE )

      self.obj1510=Capabilitie(parent)
      self.obj1510.preAction( self.LHS.CREATE )
      self.obj1510.isGraphObjectVisual = True

      if(hasattr(self.obj1510, '_setHierarchicalLink')):
        self.obj1510._setHierarchicalLink(False)

      # name
      self.obj1510.name.setValue('')
      self.obj1510.name.setNone()

      self.obj1510.GGLabel.setValue(2)
      self.obj1510.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(160.0,180.0,self.obj1510)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1510.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1510)
      self.obj1510.postAction( self.LHS.CREATE )

      self.obj1511=Role(parent)
      self.obj1511.preAction( self.LHS.CREATE )
      self.obj1511.isGraphObjectVisual = True

      if(hasattr(self.obj1511, '_setHierarchicalLink')):
        self.obj1511._setHierarchicalLink(False)

      # name
      self.obj1511.name.setValue('')
      self.obj1511.name.setNone()

      self.obj1511.GGLabel.setValue(3)
      self.obj1511.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(280.0,40.0,self.obj1511)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1511.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1511)
      self.obj1511.postAction( self.LHS.CREATE )

      self.obj1512=posses(parent)
      self.obj1512.preAction( self.LHS.CREATE )
      self.obj1512.isGraphObjectVisual = True

      if(hasattr(self.obj1512, '_setHierarchicalLink')):
        self.obj1512._setHierarchicalLink(False)

      # rate
      self.obj1512.rate.setNone()

      self.obj1512.GGLabel.setValue(4)
      self.obj1512.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(143.0,130.5,self.obj1512)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1512.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1512)
      self.obj1512.postAction( self.LHS.CREATE )

      self.obj1513=require(parent)
      self.obj1513.preAction( self.LHS.CREATE )
      self.obj1513.isGraphObjectVisual = True

      if(hasattr(self.obj1513, '_setHierarchicalLink')):
        self.obj1513._setHierarchicalLink(False)

      self.obj1513.GGLabel.setValue(5)
      self.obj1513.graphClass_= graph_require
      if parent.genGraphics:
         new_obj = graph_require(242.5,132.5,self.obj1513)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1513.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1513)
      self.obj1513.postAction( self.LHS.CREATE )

      self.obj1509.out_connections_.append(self.obj1512)
      self.obj1512.in_connections_.append(self.obj1509)
      self.obj1509.graphObject_.pendingConnections.append((self.obj1509.graphObject_.tag, self.obj1512.graphObject_.tag, [105.0, 82.0, 143.0, 130.5], 0, True))
      self.obj1511.out_connections_.append(self.obj1513)
      self.obj1513.in_connections_.append(self.obj1511)
      self.obj1511.graphObject_.pendingConnections.append((self.obj1511.graphObject_.tag, self.obj1513.graphObject_.tag, [304.0, 86.0, 242.5, 132.5], 0, True))
      self.obj1512.out_connections_.append(self.obj1510)
      self.obj1510.in_connections_.append(self.obj1512)
      self.obj1512.graphObject_.pendingConnections.append((self.obj1512.graphObject_.tag, self.obj1510.graphObject_.tag, [181.0, 179.0, 143.0, 130.5], 0, True))
      self.obj1513.out_connections_.append(self.obj1510)
      self.obj1510.in_connections_.append(self.obj1513)
      self.obj1513.graphObject_.pendingConnections.append((self.obj1513.graphObject_.tag, self.obj1510.graphObject_.tag, [181.0, 179.0, 242.5, 132.5], 0, True))

      self.RHS = ASG_omacs(parent)

      self.obj1515=Agent(parent)
      self.obj1515.preAction( self.RHS.CREATE )
      self.obj1515.isGraphObjectVisual = True

      if(hasattr(self.obj1515, '_setHierarchicalLink')):
        self.obj1515._setHierarchicalLink(False)

      # price
      self.obj1515.price.setNone()

      # name
      self.obj1515.name.setValue('')
      self.obj1515.name.setNone()

      self.obj1515.GGLabel.setValue(1)
      self.obj1515.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(80.0,20.0,self.obj1515)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1515.graphObject_ = new_obj
      self.obj15150= AttrCalc()
      self.obj15150.Copy=ATOM3Boolean()
      self.obj15150.Copy.setValue(('Copy from LHS', 1))
      self.obj15150.Copy.config = 0
      self.obj15150.Specify=ATOM3Constraint()
      self.obj15150.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1515.GGset2Any['price']= self.obj15150
      self.obj15151= AttrCalc()
      self.obj15151.Copy=ATOM3Boolean()
      self.obj15151.Copy.setValue(('Copy from LHS', 1))
      self.obj15151.Copy.config = 0
      self.obj15151.Specify=ATOM3Constraint()
      self.obj15151.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1515.GGset2Any['name']= self.obj15151

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1515)
      self.obj1515.postAction( self.RHS.CREATE )

      self.obj1516=Capabilitie(parent)
      self.obj1516.preAction( self.RHS.CREATE )
      self.obj1516.isGraphObjectVisual = True

      if(hasattr(self.obj1516, '_setHierarchicalLink')):
        self.obj1516._setHierarchicalLink(False)

      # name
      self.obj1516.name.setValue('')
      self.obj1516.name.setNone()

      self.obj1516.GGLabel.setValue(2)
      self.obj1516.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(160.0,180.0,self.obj1516)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1516.graphObject_ = new_obj
      self.obj15160= AttrCalc()
      self.obj15160.Copy=ATOM3Boolean()
      self.obj15160.Copy.setValue(('Copy from LHS', 1))
      self.obj15160.Copy.config = 0
      self.obj15160.Specify=ATOM3Constraint()
      self.obj15160.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1516.GGset2Any['name']= self.obj15160

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1516)
      self.obj1516.postAction( self.RHS.CREATE )

      self.obj1517=Role(parent)
      self.obj1517.preAction( self.RHS.CREATE )
      self.obj1517.isGraphObjectVisual = True

      if(hasattr(self.obj1517, '_setHierarchicalLink')):
        self.obj1517._setHierarchicalLink(False)

      # name
      self.obj1517.name.setValue('')
      self.obj1517.name.setNone()

      self.obj1517.GGLabel.setValue(3)
      self.obj1517.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(280.0,40.0,self.obj1517)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1517.graphObject_ = new_obj
      self.obj15170= AttrCalc()
      self.obj15170.Copy=ATOM3Boolean()
      self.obj15170.Copy.setValue(('Copy from LHS', 1))
      self.obj15170.Copy.config = 0
      self.obj15170.Specify=ATOM3Constraint()
      self.obj15170.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1517.GGset2Any['name']= self.obj15170

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1517)
      self.obj1517.postAction( self.RHS.CREATE )

      self.obj1518=posses(parent)
      self.obj1518.preAction( self.RHS.CREATE )
      self.obj1518.isGraphObjectVisual = True

      if(hasattr(self.obj1518, '_setHierarchicalLink')):
        self.obj1518._setHierarchicalLink(False)

      # rate
      self.obj1518.rate.setNone()

      self.obj1518.GGLabel.setValue(4)
      self.obj1518.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(143.0,130.5,self.obj1518)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1518.graphObject_ = new_obj
      self.obj15180= AttrCalc()
      self.obj15180.Copy=ATOM3Boolean()
      self.obj15180.Copy.setValue(('Copy from LHS', 1))
      self.obj15180.Copy.config = 0
      self.obj15180.Specify=ATOM3Constraint()
      self.obj15180.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1518.GGset2Any['rate']= self.obj15180

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1518)
      self.obj1518.postAction( self.RHS.CREATE )

      self.obj1519=CapableOf(parent)
      self.obj1519.preAction( self.RHS.CREATE )
      self.obj1519.isGraphObjectVisual = True

      if(hasattr(self.obj1519, '_setHierarchicalLink')):
        self.obj1519._setHierarchicalLink(False)

      # rate
      self.obj1519.rate.setValue(0.0)

      self.obj1519.GGLabel.setValue(7)
      self.obj1519.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(214.0,83.5,self.obj1519)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1519.graphObject_ = new_obj
      self.obj15190= AttrCalc()
      self.obj15190.Copy=ATOM3Boolean()
      self.obj15190.Copy.setValue(('Copy from LHS', 1))
      self.obj15190.Copy.config = 0
      self.obj15190.Specify=ATOM3Constraint()
      self.obj15190.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1519.GGset2Any['rate']= self.obj15190

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1519)
      self.obj1519.postAction( self.RHS.CREATE )

      self.obj1520=require(parent)
      self.obj1520.preAction( self.RHS.CREATE )
      self.obj1520.isGraphObjectVisual = True

      if(hasattr(self.obj1520, '_setHierarchicalLink')):
        self.obj1520._setHierarchicalLink(False)

      self.obj1520.GGLabel.setValue(5)
      self.obj1520.graphClass_= graph_require
      if parent.genGraphics:
         new_obj = graph_require(242.5,132.5,self.obj1520)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1520.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1520)
      self.obj1520.postAction( self.RHS.CREATE )

      self.obj1515.out_connections_.append(self.obj1518)
      self.obj1518.in_connections_.append(self.obj1515)
      self.obj1515.graphObject_.pendingConnections.append((self.obj1515.graphObject_.tag, self.obj1518.graphObject_.tag, [117.0, 82.0, 143.0, 130.5], 2, 0))
      self.obj1515.out_connections_.append(self.obj1519)
      self.obj1519.in_connections_.append(self.obj1515)
      self.obj1515.graphObject_.pendingConnections.append((self.obj1515.graphObject_.tag, self.obj1519.graphObject_.tag, [117.0, 82.0, 214.0, 83.5], 0, True))
      self.obj1517.out_connections_.append(self.obj1520)
      self.obj1520.in_connections_.append(self.obj1517)
      self.obj1517.graphObject_.pendingConnections.append((self.obj1517.graphObject_.tag, self.obj1520.graphObject_.tag, [311.0, 85.0, 242.5, 132.5], 2, 0))
      self.obj1518.out_connections_.append(self.obj1516)
      self.obj1516.in_connections_.append(self.obj1518)
      self.obj1518.graphObject_.pendingConnections.append((self.obj1518.graphObject_.tag, self.obj1516.graphObject_.tag, [191.0, 183.0, 143.0, 130.5], 2, 0))
      self.obj1519.out_connections_.append(self.obj1517)
      self.obj1517.in_connections_.append(self.obj1519)
      self.obj1519.graphObject_.pendingConnections.append((self.obj1519.graphObject_.tag, self.obj1517.graphObject_.tag, [311.0, 85.0, 214.0, 83.5], 0, True))
      self.obj1520.out_connections_.append(self.obj1516)
      self.obj1516.in_connections_.append(self.obj1520)
      self.obj1520.graphObject_.pendingConnections.append((self.obj1520.graphObject_.tag, self.obj1516.graphObject_.tag, [191.0, 183.0, 242.5, 132.5], 2, 0))

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
      
      

