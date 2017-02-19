# _ linkAgent2Role1_GG_rule.py ____________________________________________________________________________
# File generated automatically by ATOM3. Graph Grammar Rule
# ___________________________________________________________________________________________
from GGrule import *
from CapableOf import *
from Goal import *
from ASG_omacss import *
from Agent import *
from Capabilitie import *
from Role import *
from requir import *
from achieve import *
from posses import *
class linkAgent2Role1_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 1)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_omacss(parent)

      self.obj138=Agent(parent)
      self.obj138.preAction( self.LHS.CREATE )
      self.obj138.isGraphObjectVisual = True

      if(hasattr(self.obj138, '_setHierarchicalLink')):
        self.obj138._setHierarchicalLink(False)

      # price
      self.obj138.price.setValue(0)

      # name
      self.obj138.name.setValue('')
      self.obj138.name.setNone()

      self.obj138.GGLabel.setValue(1)
      self.obj138.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(80.0,40.0,self.obj138)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj138.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj138)
      self.obj138.postAction( self.LHS.CREATE )

      self.obj139=Capabilitie(parent)
      self.obj139.preAction( self.LHS.CREATE )
      self.obj139.isGraphObjectVisual = True

      if(hasattr(self.obj139, '_setHierarchicalLink')):
        self.obj139._setHierarchicalLink(False)

      # name
      self.obj139.name.setValue('')
      self.obj139.name.setNone()

      self.obj139.GGLabel.setValue(2)
      self.obj139.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(200.0,200.0,self.obj139)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj139.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj139)
      self.obj139.postAction( self.LHS.CREATE )

      self.obj140=Role(parent)
      self.obj140.preAction( self.LHS.CREATE )
      self.obj140.isGraphObjectVisual = True

      if(hasattr(self.obj140, '_setHierarchicalLink')):
        self.obj140._setHierarchicalLink(False)

      # name
      self.obj140.name.setValue('')
      self.obj140.name.setNone()

      self.obj140.GGLabel.setValue(3)
      self.obj140.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(320.0,60.0,self.obj140)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj140.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj140)
      self.obj140.postAction( self.LHS.CREATE )

      self.obj141=posses(parent)
      self.obj141.preAction( self.LHS.CREATE )
      self.obj141.isGraphObjectVisual = True

      if(hasattr(self.obj141, '_setHierarchicalLink')):
        self.obj141._setHierarchicalLink(False)

      # rate
      self.obj141.rate.setNone()

      self.obj141.GGLabel.setValue(4)
      self.obj141.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(163.0,150.5,self.obj141)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj141.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj141)
      self.obj141.postAction( self.LHS.CREATE )

      self.obj142=requir(parent)
      self.obj142.preAction( self.LHS.CREATE )
      self.obj142.isGraphObjectVisual = True

      if(hasattr(self.obj142, '_setHierarchicalLink')):
        self.obj142._setHierarchicalLink(False)

      self.obj142.GGLabel.setValue(5)
      self.obj142.graphClass_= graph_requir
      if parent.genGraphics:
         new_obj = graph_requir(282.5,152.5,self.obj142)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj142.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj142)
      self.obj142.postAction( self.LHS.CREATE )

      self.obj138.out_connections_.append(self.obj141)
      self.obj141.in_connections_.append(self.obj138)
      self.obj138.graphObject_.pendingConnections.append((self.obj138.graphObject_.tag, self.obj141.graphObject_.tag, [105.0, 102.0, 163.0, 150.5], 0, True))
      self.obj140.out_connections_.append(self.obj142)
      self.obj142.in_connections_.append(self.obj140)
      self.obj140.graphObject_.pendingConnections.append((self.obj140.graphObject_.tag, self.obj142.graphObject_.tag, [344.0, 106.0, 282.5, 152.5], 0, True))
      self.obj141.out_connections_.append(self.obj139)
      self.obj139.in_connections_.append(self.obj141)
      self.obj141.graphObject_.pendingConnections.append((self.obj141.graphObject_.tag, self.obj139.graphObject_.tag, [221.0, 199.0, 163.0, 150.5], 0, True))
      self.obj142.out_connections_.append(self.obj139)
      self.obj139.in_connections_.append(self.obj142)
      self.obj142.graphObject_.pendingConnections.append((self.obj142.graphObject_.tag, self.obj139.graphObject_.tag, [221.0, 199.0, 282.5, 152.5], 0, True))

      self.RHS = ASG_omacss(parent)

      self.obj144=Agent(parent)
      self.obj144.preAction( self.RHS.CREATE )
      self.obj144.isGraphObjectVisual = True

      if(hasattr(self.obj144, '_setHierarchicalLink')):
        self.obj144._setHierarchicalLink(False)

      # price
      self.obj144.price.setValue(0)

      # name
      self.obj144.name.setValue('')
      self.obj144.name.setNone()

      self.obj144.GGLabel.setValue(1)
      self.obj144.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(80.0,40.0,self.obj144)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj144.graphObject_ = new_obj
      self.obj1440= AttrCalc()
      self.obj1440.Copy=ATOM3Boolean()
      self.obj1440.Copy.setValue(('Copy from LHS', 1))
      self.obj1440.Copy.config = 0
      self.obj1440.Specify=ATOM3Constraint()
      self.obj1440.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj144.GGset2Any['price']= self.obj1440
      self.obj1441= AttrCalc()
      self.obj1441.Copy=ATOM3Boolean()
      self.obj1441.Copy.setValue(('Copy from LHS', 1))
      self.obj1441.Copy.config = 0
      self.obj1441.Specify=ATOM3Constraint()
      self.obj1441.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj144.GGset2Any['name']= self.obj1441

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj144)
      self.obj144.postAction( self.RHS.CREATE )

      self.obj145=Capabilitie(parent)
      self.obj145.preAction( self.RHS.CREATE )
      self.obj145.isGraphObjectVisual = True

      if(hasattr(self.obj145, '_setHierarchicalLink')):
        self.obj145._setHierarchicalLink(False)

      # name
      self.obj145.name.setValue('')
      self.obj145.name.setNone()

      self.obj145.GGLabel.setValue(2)
      self.obj145.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(200.0,200.0,self.obj145)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj145.graphObject_ = new_obj
      self.obj1450= AttrCalc()
      self.obj1450.Copy=ATOM3Boolean()
      self.obj1450.Copy.setValue(('Copy from LHS', 1))
      self.obj1450.Copy.config = 0
      self.obj1450.Specify=ATOM3Constraint()
      self.obj1450.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj145.GGset2Any['name']= self.obj1450

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj145)
      self.obj145.postAction( self.RHS.CREATE )

      self.obj146=Role(parent)
      self.obj146.preAction( self.RHS.CREATE )
      self.obj146.isGraphObjectVisual = True

      if(hasattr(self.obj146, '_setHierarchicalLink')):
        self.obj146._setHierarchicalLink(False)

      # name
      self.obj146.name.setValue('')
      self.obj146.name.setNone()

      self.obj146.GGLabel.setValue(3)
      self.obj146.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(320.0,60.0,self.obj146)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj146.graphObject_ = new_obj
      self.obj1460= AttrCalc()
      self.obj1460.Copy=ATOM3Boolean()
      self.obj1460.Copy.setValue(('Copy from LHS', 1))
      self.obj1460.Copy.config = 0
      self.obj1460.Specify=ATOM3Constraint()
      self.obj1460.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj146.GGset2Any['name']= self.obj1460

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj146)
      self.obj146.postAction( self.RHS.CREATE )

      self.obj147=posses(parent)
      self.obj147.preAction( self.RHS.CREATE )
      self.obj147.isGraphObjectVisual = True

      if(hasattr(self.obj147, '_setHierarchicalLink')):
        self.obj147._setHierarchicalLink(False)

      # rate
      self.obj147.rate.setValue(0.0)

      self.obj147.GGLabel.setValue(4)
      self.obj147.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(163.0,150.5,self.obj147)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj147.graphObject_ = new_obj
      self.obj1470= AttrCalc()
      self.obj1470.Copy=ATOM3Boolean()
      self.obj1470.Copy.setValue(('Copy from LHS', 1))
      self.obj1470.Copy.config = 0
      self.obj1470.Specify=ATOM3Constraint()
      self.obj1470.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj147.GGset2Any['rate']= self.obj1470

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj147)
      self.obj147.postAction( self.RHS.CREATE )

      self.obj148=CapableOf(parent)
      self.obj148.preAction( self.RHS.CREATE )
      self.obj148.isGraphObjectVisual = True

      if(hasattr(self.obj148, '_setHierarchicalLink')):
        self.obj148._setHierarchicalLink(False)

      self.obj148.GGLabel.setValue(7)
      self.obj148.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(233.5,74.0,self.obj148)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj148.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj148)
      self.obj148.postAction( self.RHS.CREATE )

      self.obj149=requir(parent)
      self.obj149.preAction( self.RHS.CREATE )
      self.obj149.isGraphObjectVisual = True

      if(hasattr(self.obj149, '_setHierarchicalLink')):
        self.obj149._setHierarchicalLink(False)

      self.obj149.GGLabel.setValue(5)
      self.obj149.graphClass_= graph_requir
      if parent.genGraphics:
         new_obj = graph_requir(282.5,152.5,self.obj149)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj149.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj149)
      self.obj149.postAction( self.RHS.CREATE )

      self.obj144.out_connections_.append(self.obj147)
      self.obj147.in_connections_.append(self.obj144)
      self.obj144.graphObject_.pendingConnections.append((self.obj144.graphObject_.tag, self.obj147.graphObject_.tag, [117.0, 102.0, 163.0, 150.5], 2, 0))
      self.obj144.out_connections_.append(self.obj148)
      self.obj148.in_connections_.append(self.obj144)
      self.obj144.graphObject_.pendingConnections.append((self.obj144.graphObject_.tag, self.obj148.graphObject_.tag, [117.0, 102.0, 175.0, 84.5, 233.5, 74.0], 2, True))
      self.obj146.out_connections_.append(self.obj149)
      self.obj149.in_connections_.append(self.obj146)
      self.obj146.graphObject_.pendingConnections.append((self.obj146.graphObject_.tag, self.obj149.graphObject_.tag, [351.0, 105.0, 282.5, 152.5], 2, 0))
      self.obj147.out_connections_.append(self.obj145)
      self.obj145.in_connections_.append(self.obj147)
      self.obj147.graphObject_.pendingConnections.append((self.obj147.graphObject_.tag, self.obj145.graphObject_.tag, [231.0, 203.0, 163.0, 150.5], 2, 0))
      self.obj148.out_connections_.append(self.obj146)
      self.obj146.in_connections_.append(self.obj148)
      self.obj148.graphObject_.pendingConnections.append((self.obj148.graphObject_.tag, self.obj146.graphObject_.tag, [351.0, 60.0, 292.0, 63.5, 233.5, 74.0], 2, True))
      self.obj149.out_connections_.append(self.obj145)
      self.obj145.in_connections_.append(self.obj149)
      self.obj149.graphObject_.pendingConnections.append((self.obj149.graphObject_.tag, self.obj145.graphObject_.tag, [231.0, 203.0, 282.5, 152.5], 2, 0))

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
      
      

