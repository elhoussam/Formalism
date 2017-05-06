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

      self.obj547=Agent(parent)
      self.obj547.preAction( self.LHS.CREATE )
      self.obj547.isGraphObjectVisual = True

      if(hasattr(self.obj547, '_setHierarchicalLink')):
        self.obj547._setHierarchicalLink(False)

      # price
      self.obj547.price.setNone()

      # name
      self.obj547.name.setValue('')
      self.obj547.name.setNone()

      self.obj547.GGLabel.setValue(1)
      self.obj547.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(100.0,20.0,self.obj547)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj547.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj547)
      self.obj547.postAction( self.LHS.CREATE )

      self.obj548=Capabilitie(parent)
      self.obj548.preAction( self.LHS.CREATE )
      self.obj548.isGraphObjectVisual = True

      if(hasattr(self.obj548, '_setHierarchicalLink')):
        self.obj548._setHierarchicalLink(False)

      # name
      self.obj548.name.setValue('')
      self.obj548.name.setNone()

      self.obj548.GGLabel.setValue(3)
      self.obj548.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(340.0,40.0,self.obj548)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj548.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj548)
      self.obj548.postAction( self.LHS.CREATE )

      self.obj549=Capabilitie(parent)
      self.obj549.preAction( self.LHS.CREATE )
      self.obj549.isGraphObjectVisual = True

      if(hasattr(self.obj549, '_setHierarchicalLink')):
        self.obj549._setHierarchicalLink(False)

      # name
      self.obj549.name.setValue('')
      self.obj549.name.setNone()

      self.obj549.GGLabel.setValue(4)
      self.obj549.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(140.0,160.0,self.obj549)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj549.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj549)
      self.obj549.postAction( self.LHS.CREATE )

      self.obj550=Role(parent)
      self.obj550.preAction( self.LHS.CREATE )
      self.obj550.isGraphObjectVisual = True

      if(hasattr(self.obj550, '_setHierarchicalLink')):
        self.obj550._setHierarchicalLink(False)

      # name
      self.obj550.name.setValue('')
      self.obj550.name.setNone()

      self.obj550.GGLabel.setValue(2)
      self.obj550.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(300.0,140.0,self.obj550)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj550.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj550)
      self.obj550.postAction( self.LHS.CREATE )

      self.obj551=posses(parent)
      self.obj551.preAction( self.LHS.CREATE )
      self.obj551.isGraphObjectVisual = True

      if(hasattr(self.obj551, '_setHierarchicalLink')):
        self.obj551._setHierarchicalLink(False)

      # rate
      self.obj551.rate.setNone()

      self.obj551.GGLabel.setValue(5)
      self.obj551.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(143.0,120.5,self.obj551)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj551.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj551)
      self.obj551.postAction( self.LHS.CREATE )

      self.obj552=CapableOf(parent)
      self.obj552.preAction( self.LHS.CREATE )
      self.obj552.isGraphObjectVisual = True

      if(hasattr(self.obj552, '_setHierarchicalLink')):
        self.obj552._setHierarchicalLink(False)

      # rate
      self.obj552.rate.setNone()

      self.obj552.GGLabel.setValue(8)
      self.obj552.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(224.5,111.5,self.obj552)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj552.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj552)
      self.obj552.postAction( self.LHS.CREATE )

      self.obj553=require(parent)
      self.obj553.preAction( self.LHS.CREATE )
      self.obj553.isGraphObjectVisual = True

      if(hasattr(self.obj553, '_setHierarchicalLink')):
        self.obj553._setHierarchicalLink(False)

      self.obj553.GGLabel.setValue(7)
      self.obj553.graphClass_= graph_require
      if parent.genGraphics:
         new_obj = graph_require(242.5,192.5,self.obj553)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj553.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj553)
      self.obj553.postAction( self.LHS.CREATE )

      self.obj554=require(parent)
      self.obj554.preAction( self.LHS.CREATE )
      self.obj554.isGraphObjectVisual = True

      if(hasattr(self.obj554, '_setHierarchicalLink')):
        self.obj554._setHierarchicalLink(False)

      self.obj554.GGLabel.setValue(9)
      self.obj554.graphClass_= graph_require
      if parent.genGraphics:
         new_obj = graph_require(351.0,111.5,self.obj554)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj554.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj554)
      self.obj554.postAction( self.LHS.CREATE )

      self.obj547.out_connections_.append(self.obj551)
      self.obj551.in_connections_.append(self.obj547)
      self.obj547.graphObject_.pendingConnections.append((self.obj547.graphObject_.tag, self.obj551.graphObject_.tag, [137.0, 82.0, 143.0, 120.5], 2, 0))
      self.obj547.out_connections_.append(self.obj552)
      self.obj552.in_connections_.append(self.obj547)
      self.obj547.graphObject_.pendingConnections.append((self.obj547.graphObject_.tag, self.obj552.graphObject_.tag, [125.0, 82.0, 224.5, 111.5], 0, True))
      self.obj550.out_connections_.append(self.obj553)
      self.obj553.in_connections_.append(self.obj550)
      self.obj550.graphObject_.pendingConnections.append((self.obj550.graphObject_.tag, self.obj553.graphObject_.tag, [324.0, 186.0, 242.5, 192.5], 0, True))
      self.obj550.out_connections_.append(self.obj554)
      self.obj554.in_connections_.append(self.obj550)
      self.obj550.graphObject_.pendingConnections.append((self.obj550.graphObject_.tag, self.obj554.graphObject_.tag, [331.0, 140.0, 351.0, 111.5], 0, True))
      self.obj551.out_connections_.append(self.obj549)
      self.obj549.in_connections_.append(self.obj551)
      self.obj551.graphObject_.pendingConnections.append((self.obj551.graphObject_.tag, self.obj549.graphObject_.tag, [161.0, 159.0, 143.0, 120.5], 0, True))
      self.obj552.out_connections_.append(self.obj550)
      self.obj550.in_connections_.append(self.obj552)
      self.obj552.graphObject_.pendingConnections.append((self.obj552.graphObject_.tag, self.obj550.graphObject_.tag, [324.0, 141.0, 224.5, 111.5], 0, True))
      self.obj553.out_connections_.append(self.obj549)
      self.obj549.in_connections_.append(self.obj553)
      self.obj553.graphObject_.pendingConnections.append((self.obj553.graphObject_.tag, self.obj549.graphObject_.tag, [161.0, 199.0, 242.5, 192.5], 0, True))
      self.obj554.out_connections_.append(self.obj548)
      self.obj548.in_connections_.append(self.obj554)
      self.obj554.graphObject_.pendingConnections.append((self.obj554.graphObject_.tag, self.obj548.graphObject_.tag, [371.0, 83.0, 351.0, 111.5], 0, True))

      self.RHS = ASG_omacs(parent)

      self.obj556=Agent(parent)
      self.obj556.preAction( self.RHS.CREATE )
      self.obj556.isGraphObjectVisual = True

      if(hasattr(self.obj556, '_setHierarchicalLink')):
        self.obj556._setHierarchicalLink(False)

      # price
      self.obj556.price.setNone()

      # name
      self.obj556.name.setValue('')
      self.obj556.name.setNone()

      self.obj556.GGLabel.setValue(1)
      self.obj556.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(100.0,20.0,self.obj556)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj556.graphObject_ = new_obj
      self.obj5560= AttrCalc()
      self.obj5560.Copy=ATOM3Boolean()
      self.obj5560.Copy.setValue(('Copy from LHS', 1))
      self.obj5560.Copy.config = 0
      self.obj5560.Specify=ATOM3Constraint()
      self.obj5560.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj556.GGset2Any['price']= self.obj5560
      self.obj5561= AttrCalc()
      self.obj5561.Copy=ATOM3Boolean()
      self.obj5561.Copy.setValue(('Copy from LHS', 1))
      self.obj5561.Copy.config = 0
      self.obj5561.Specify=ATOM3Constraint()
      self.obj5561.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj556.GGset2Any['name']= self.obj5561

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj556)
      self.obj556.postAction( self.RHS.CREATE )

      self.obj557=Capabilitie(parent)
      self.obj557.preAction( self.RHS.CREATE )
      self.obj557.isGraphObjectVisual = True

      if(hasattr(self.obj557, '_setHierarchicalLink')):
        self.obj557._setHierarchicalLink(False)

      # name
      self.obj557.name.setValue('')
      self.obj557.name.setNone()

      self.obj557.GGLabel.setValue(3)
      self.obj557.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(340.0,40.0,self.obj557)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj557.graphObject_ = new_obj
      self.obj5570= AttrCalc()
      self.obj5570.Copy=ATOM3Boolean()
      self.obj5570.Copy.setValue(('Copy from LHS', 1))
      self.obj5570.Copy.config = 0
      self.obj5570.Specify=ATOM3Constraint()
      self.obj5570.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj557.GGset2Any['name']= self.obj5570

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj557)
      self.obj557.postAction( self.RHS.CREATE )

      self.obj558=Capabilitie(parent)
      self.obj558.preAction( self.RHS.CREATE )
      self.obj558.isGraphObjectVisual = True

      if(hasattr(self.obj558, '_setHierarchicalLink')):
        self.obj558._setHierarchicalLink(False)

      # name
      self.obj558.name.setValue('')
      self.obj558.name.setNone()

      self.obj558.GGLabel.setValue(4)
      self.obj558.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(140.0,160.0,self.obj558)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj558.graphObject_ = new_obj
      self.obj5580= AttrCalc()
      self.obj5580.Copy=ATOM3Boolean()
      self.obj5580.Copy.setValue(('Copy from LHS', 1))
      self.obj5580.Copy.config = 0
      self.obj5580.Specify=ATOM3Constraint()
      self.obj5580.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj558.GGset2Any['name']= self.obj5580

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj558)
      self.obj558.postAction( self.RHS.CREATE )

      self.obj559=Role(parent)
      self.obj559.preAction( self.RHS.CREATE )
      self.obj559.isGraphObjectVisual = True

      if(hasattr(self.obj559, '_setHierarchicalLink')):
        self.obj559._setHierarchicalLink(False)

      # name
      self.obj559.name.setValue('')
      self.obj559.name.setNone()

      self.obj559.GGLabel.setValue(2)
      self.obj559.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(300.0,140.0,self.obj559)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj559.graphObject_ = new_obj
      self.obj5590= AttrCalc()
      self.obj5590.Copy=ATOM3Boolean()
      self.obj5590.Copy.setValue(('Copy from LHS', 1))
      self.obj5590.Copy.config = 0
      self.obj5590.Specify=ATOM3Constraint()
      self.obj5590.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj559.GGset2Any['name']= self.obj5590

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj559)
      self.obj559.postAction( self.RHS.CREATE )

      self.obj560=posses(parent)
      self.obj560.preAction( self.RHS.CREATE )
      self.obj560.isGraphObjectVisual = True

      if(hasattr(self.obj560, '_setHierarchicalLink')):
        self.obj560._setHierarchicalLink(False)

      # rate
      self.obj560.rate.setNone()

      self.obj560.GGLabel.setValue(5)
      self.obj560.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(143.0,120.5,self.obj560)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj560.graphObject_ = new_obj
      self.obj5600= AttrCalc()
      self.obj5600.Copy=ATOM3Boolean()
      self.obj5600.Copy.setValue(('Copy from LHS', 1))
      self.obj5600.Copy.config = 0
      self.obj5600.Specify=ATOM3Constraint()
      self.obj5600.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj560.GGset2Any['rate']= self.obj5600

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj560)
      self.obj560.postAction( self.RHS.CREATE )

      self.obj561=require(parent)
      self.obj561.preAction( self.RHS.CREATE )
      self.obj561.isGraphObjectVisual = True

      if(hasattr(self.obj561, '_setHierarchicalLink')):
        self.obj561._setHierarchicalLink(False)

      self.obj561.GGLabel.setValue(7)
      self.obj561.graphClass_= graph_require
      if parent.genGraphics:
         new_obj = graph_require(242.5,192.5,self.obj561)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj561.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj561)
      self.obj561.postAction( self.RHS.CREATE )

      self.obj562=require(parent)
      self.obj562.preAction( self.RHS.CREATE )
      self.obj562.isGraphObjectVisual = True

      if(hasattr(self.obj562, '_setHierarchicalLink')):
        self.obj562._setHierarchicalLink(False)

      self.obj562.GGLabel.setValue(9)
      self.obj562.graphClass_= graph_require
      if parent.genGraphics:
         new_obj = graph_require(351.0,111.5,self.obj562)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj562.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj562)
      self.obj562.postAction( self.RHS.CREATE )

      self.obj556.out_connections_.append(self.obj560)
      self.obj560.in_connections_.append(self.obj556)
      self.obj556.graphObject_.pendingConnections.append((self.obj556.graphObject_.tag, self.obj560.graphObject_.tag, [137.0, 82.0, 143.0, 120.5], 2, 0))
      self.obj559.out_connections_.append(self.obj561)
      self.obj561.in_connections_.append(self.obj559)
      self.obj559.graphObject_.pendingConnections.append((self.obj559.graphObject_.tag, self.obj561.graphObject_.tag, [331.0, 185.0, 242.5, 192.5], 2, 0))
      self.obj559.out_connections_.append(self.obj562)
      self.obj562.in_connections_.append(self.obj559)
      self.obj559.graphObject_.pendingConnections.append((self.obj559.graphObject_.tag, self.obj562.graphObject_.tag, [331.0, 140.0, 351.0, 111.5], 0, True))
      self.obj560.out_connections_.append(self.obj558)
      self.obj558.in_connections_.append(self.obj560)
      self.obj560.graphObject_.pendingConnections.append((self.obj560.graphObject_.tag, self.obj558.graphObject_.tag, [171.0, 163.0, 143.0, 120.5], 2, 0))
      self.obj561.out_connections_.append(self.obj558)
      self.obj558.in_connections_.append(self.obj561)
      self.obj561.graphObject_.pendingConnections.append((self.obj561.graphObject_.tag, self.obj558.graphObject_.tag, [171.0, 203.0, 242.5, 192.5], 2, 0))
      self.obj562.out_connections_.append(self.obj557)
      self.obj557.in_connections_.append(self.obj562)
      self.obj562.graphObject_.pendingConnections.append((self.obj562.graphObject_.tag, self.obj557.graphObject_.tag, [371.0, 83.0, 351.0, 111.5], 0, True))

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
      
      
      
      

