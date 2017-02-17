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

      self.obj935=Agent(parent)
      self.obj935.preAction( self.LHS.CREATE )
      self.obj935.isGraphObjectVisual = True

      if(hasattr(self.obj935, '_setHierarchicalLink')):
        self.obj935._setHierarchicalLink(False)

      # price
      self.obj935.price.setValue(0)

      # name
      self.obj935.name.setValue('')
      self.obj935.name.setNone()

      self.obj935.GGLabel.setValue(1)
      self.obj935.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(80.0,40.0,self.obj935)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj935.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj935)
      self.obj935.postAction( self.LHS.CREATE )

      self.obj936=Capabilitie(parent)
      self.obj936.preAction( self.LHS.CREATE )
      self.obj936.isGraphObjectVisual = True

      if(hasattr(self.obj936, '_setHierarchicalLink')):
        self.obj936._setHierarchicalLink(False)

      # name
      self.obj936.name.setValue('')
      self.obj936.name.setNone()

      self.obj936.GGLabel.setValue(2)
      self.obj936.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(200.0,200.0,self.obj936)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj936.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj936)
      self.obj936.postAction( self.LHS.CREATE )

      self.obj937=Role(parent)
      self.obj937.preAction( self.LHS.CREATE )
      self.obj937.isGraphObjectVisual = True

      if(hasattr(self.obj937, '_setHierarchicalLink')):
        self.obj937._setHierarchicalLink(False)

      # name
      self.obj937.name.setValue('')
      self.obj937.name.setNone()

      self.obj937.GGLabel.setValue(3)
      self.obj937.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(320.0,60.0,self.obj937)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj937.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj937)
      self.obj937.postAction( self.LHS.CREATE )

      self.obj938=posses(parent)
      self.obj938.preAction( self.LHS.CREATE )
      self.obj938.isGraphObjectVisual = True

      if(hasattr(self.obj938, '_setHierarchicalLink')):
        self.obj938._setHierarchicalLink(False)

      # rate
      self.obj938.rate.setValue(0.0)

      self.obj938.GGLabel.setValue(4)
      self.obj938.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(163.0,150.5,self.obj938)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj938.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj938)
      self.obj938.postAction( self.LHS.CREATE )

      self.obj939=requir(parent)
      self.obj939.preAction( self.LHS.CREATE )
      self.obj939.isGraphObjectVisual = True

      if(hasattr(self.obj939, '_setHierarchicalLink')):
        self.obj939._setHierarchicalLink(False)

      self.obj939.GGLabel.setValue(5)
      self.obj939.graphClass_= graph_requir
      if parent.genGraphics:
         new_obj = graph_requir(282.5,152.5,self.obj939)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj939.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj939)
      self.obj939.postAction( self.LHS.CREATE )

      self.obj935.out_connections_.append(self.obj938)
      self.obj938.in_connections_.append(self.obj935)
      self.obj935.graphObject_.pendingConnections.append((self.obj935.graphObject_.tag, self.obj938.graphObject_.tag, [105.0, 102.0, 163.0, 150.5], 0, True))
      self.obj937.out_connections_.append(self.obj939)
      self.obj939.in_connections_.append(self.obj937)
      self.obj937.graphObject_.pendingConnections.append((self.obj937.graphObject_.tag, self.obj939.graphObject_.tag, [344.0, 106.0, 282.5, 152.5], 0, True))
      self.obj938.out_connections_.append(self.obj936)
      self.obj936.in_connections_.append(self.obj938)
      self.obj938.graphObject_.pendingConnections.append((self.obj938.graphObject_.tag, self.obj936.graphObject_.tag, [221.0, 199.0, 163.0, 150.5], 0, True))
      self.obj939.out_connections_.append(self.obj936)
      self.obj936.in_connections_.append(self.obj939)
      self.obj939.graphObject_.pendingConnections.append((self.obj939.graphObject_.tag, self.obj936.graphObject_.tag, [221.0, 199.0, 282.5, 152.5], 0, True))

      self.RHS = ASG_omacss(parent)

      self.obj941=Agent(parent)
      self.obj941.preAction( self.RHS.CREATE )
      self.obj941.isGraphObjectVisual = True

      if(hasattr(self.obj941, '_setHierarchicalLink')):
        self.obj941._setHierarchicalLink(False)

      # price
      self.obj941.price.setValue(0)

      # name
      self.obj941.name.setValue('')
      self.obj941.name.setNone()

      self.obj941.GGLabel.setValue(1)
      self.obj941.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(80.0,40.0,self.obj941)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj941.graphObject_ = new_obj
      self.obj9410= AttrCalc()
      self.obj9410.Copy=ATOM3Boolean()
      self.obj9410.Copy.setValue(('Copy from LHS', 1))
      self.obj9410.Copy.config = 0
      self.obj9410.Specify=ATOM3Constraint()
      self.obj9410.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj941.GGset2Any['price']= self.obj9410
      self.obj9411= AttrCalc()
      self.obj9411.Copy=ATOM3Boolean()
      self.obj9411.Copy.setValue(('Copy from LHS', 1))
      self.obj9411.Copy.config = 0
      self.obj9411.Specify=ATOM3Constraint()
      self.obj9411.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj941.GGset2Any['name']= self.obj9411

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj941)
      self.obj941.postAction( self.RHS.CREATE )

      self.obj942=Capabilitie(parent)
      self.obj942.preAction( self.RHS.CREATE )
      self.obj942.isGraphObjectVisual = True

      if(hasattr(self.obj942, '_setHierarchicalLink')):
        self.obj942._setHierarchicalLink(False)

      # name
      self.obj942.name.setValue('')
      self.obj942.name.setNone()

      self.obj942.GGLabel.setValue(2)
      self.obj942.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(200.0,200.0,self.obj942)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj942.graphObject_ = new_obj
      self.obj9420= AttrCalc()
      self.obj9420.Copy=ATOM3Boolean()
      self.obj9420.Copy.setValue(('Copy from LHS', 1))
      self.obj9420.Copy.config = 0
      self.obj9420.Specify=ATOM3Constraint()
      self.obj9420.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj942.GGset2Any['name']= self.obj9420

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj942)
      self.obj942.postAction( self.RHS.CREATE )

      self.obj943=Role(parent)
      self.obj943.preAction( self.RHS.CREATE )
      self.obj943.isGraphObjectVisual = True

      if(hasattr(self.obj943, '_setHierarchicalLink')):
        self.obj943._setHierarchicalLink(False)

      # name
      self.obj943.name.setValue('')
      self.obj943.name.setNone()

      self.obj943.GGLabel.setValue(3)
      self.obj943.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(320.0,60.0,self.obj943)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj943.graphObject_ = new_obj
      self.obj9430= AttrCalc()
      self.obj9430.Copy=ATOM3Boolean()
      self.obj9430.Copy.setValue(('Copy from LHS', 1))
      self.obj9430.Copy.config = 0
      self.obj9430.Specify=ATOM3Constraint()
      self.obj9430.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj943.GGset2Any['name']= self.obj9430

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj943)
      self.obj943.postAction( self.RHS.CREATE )

      self.obj944=posses(parent)
      self.obj944.preAction( self.RHS.CREATE )
      self.obj944.isGraphObjectVisual = True

      if(hasattr(self.obj944, '_setHierarchicalLink')):
        self.obj944._setHierarchicalLink(False)

      # rate
      self.obj944.rate.setValue(0.0)

      self.obj944.GGLabel.setValue(4)
      self.obj944.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(163.0,150.5,self.obj944)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj944.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj944)
      self.obj944.postAction( self.RHS.CREATE )

      self.obj945=CapableOf(parent)
      self.obj945.preAction( self.RHS.CREATE )
      self.obj945.isGraphObjectVisual = True

      if(hasattr(self.obj945, '_setHierarchicalLink')):
        self.obj945._setHierarchicalLink(False)

      self.obj945.GGLabel.setValue(7)
      self.obj945.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(233.5,74.0,self.obj945)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj945.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj945)
      self.obj945.postAction( self.RHS.CREATE )

      self.obj946=requir(parent)
      self.obj946.preAction( self.RHS.CREATE )
      self.obj946.isGraphObjectVisual = True

      if(hasattr(self.obj946, '_setHierarchicalLink')):
        self.obj946._setHierarchicalLink(False)

      self.obj946.GGLabel.setValue(5)
      self.obj946.graphClass_= graph_requir
      if parent.genGraphics:
         new_obj = graph_requir(282.5,152.5,self.obj946)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj946.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj946)
      self.obj946.postAction( self.RHS.CREATE )

      self.obj941.out_connections_.append(self.obj944)
      self.obj944.in_connections_.append(self.obj941)
      self.obj941.graphObject_.pendingConnections.append((self.obj941.graphObject_.tag, self.obj944.graphObject_.tag, [117.0, 102.0, 163.0, 150.5], 2, 0))
      self.obj941.out_connections_.append(self.obj945)
      self.obj945.in_connections_.append(self.obj941)
      self.obj941.graphObject_.pendingConnections.append((self.obj941.graphObject_.tag, self.obj945.graphObject_.tag, [117.0, 102.0, 175.0, 84.5, 233.5, 74.0], 2, True))
      self.obj943.out_connections_.append(self.obj946)
      self.obj946.in_connections_.append(self.obj943)
      self.obj943.graphObject_.pendingConnections.append((self.obj943.graphObject_.tag, self.obj946.graphObject_.tag, [351.0, 105.0, 282.5, 152.5], 2, 0))
      self.obj944.out_connections_.append(self.obj942)
      self.obj942.in_connections_.append(self.obj944)
      self.obj944.graphObject_.pendingConnections.append((self.obj944.graphObject_.tag, self.obj942.graphObject_.tag, [231.0, 203.0, 163.0, 150.5], 2, 0))
      self.obj945.out_connections_.append(self.obj943)
      self.obj943.in_connections_.append(self.obj945)
      self.obj945.graphObject_.pendingConnections.append((self.obj945.graphObject_.tag, self.obj943.graphObject_.tag, [351.0, 60.0, 292.0, 63.5, 233.5, 74.0], 2, True))
      self.obj946.out_connections_.append(self.obj942)
      self.obj942.in_connections_.append(self.obj946)
      self.obj946.graphObject_.pendingConnections.append((self.obj946.graphObject_.tag, self.obj942.graphObject_.tag, [231.0, 203.0, 282.5, 152.5], 2, 0))

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
      
      

