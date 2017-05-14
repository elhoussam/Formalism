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

      self.obj1548=Agent(parent)
      self.obj1548.preAction( self.LHS.CREATE )
      self.obj1548.isGraphObjectVisual = True

      if(hasattr(self.obj1548, '_setHierarchicalLink')):
        self.obj1548._setHierarchicalLink(False)

      # price
      self.obj1548.price.setNone()

      # name
      self.obj1548.name.setValue('')
      self.obj1548.name.setNone()

      self.obj1548.GGLabel.setValue(1)
      self.obj1548.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(100.0,20.0,self.obj1548)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1548.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1548)
      self.obj1548.postAction( self.LHS.CREATE )

      self.obj1549=Capabilitie(parent)
      self.obj1549.preAction( self.LHS.CREATE )
      self.obj1549.isGraphObjectVisual = True

      if(hasattr(self.obj1549, '_setHierarchicalLink')):
        self.obj1549._setHierarchicalLink(False)

      # name
      self.obj1549.name.setValue('')
      self.obj1549.name.setNone()

      self.obj1549.GGLabel.setValue(3)
      self.obj1549.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(340.0,40.0,self.obj1549)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1549.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1549)
      self.obj1549.postAction( self.LHS.CREATE )

      self.obj1550=Capabilitie(parent)
      self.obj1550.preAction( self.LHS.CREATE )
      self.obj1550.isGraphObjectVisual = True

      if(hasattr(self.obj1550, '_setHierarchicalLink')):
        self.obj1550._setHierarchicalLink(False)

      # name
      self.obj1550.name.setValue('')
      self.obj1550.name.setNone()

      self.obj1550.GGLabel.setValue(4)
      self.obj1550.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(140.0,160.0,self.obj1550)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1550.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1550)
      self.obj1550.postAction( self.LHS.CREATE )

      self.obj1551=Role(parent)
      self.obj1551.preAction( self.LHS.CREATE )
      self.obj1551.isGraphObjectVisual = True

      if(hasattr(self.obj1551, '_setHierarchicalLink')):
        self.obj1551._setHierarchicalLink(False)

      # name
      self.obj1551.name.setValue('')
      self.obj1551.name.setNone()

      self.obj1551.GGLabel.setValue(2)
      self.obj1551.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(300.0,140.0,self.obj1551)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1551.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1551)
      self.obj1551.postAction( self.LHS.CREATE )

      self.obj1552=posses(parent)
      self.obj1552.preAction( self.LHS.CREATE )
      self.obj1552.isGraphObjectVisual = True

      if(hasattr(self.obj1552, '_setHierarchicalLink')):
        self.obj1552._setHierarchicalLink(False)

      # rate
      self.obj1552.rate.setNone()

      self.obj1552.GGLabel.setValue(5)
      self.obj1552.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(143.0,120.5,self.obj1552)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1552.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1552)
      self.obj1552.postAction( self.LHS.CREATE )

      self.obj1553=CapableOf(parent)
      self.obj1553.preAction( self.LHS.CREATE )
      self.obj1553.isGraphObjectVisual = True

      if(hasattr(self.obj1553, '_setHierarchicalLink')):
        self.obj1553._setHierarchicalLink(False)

      # rate
      self.obj1553.rate.setNone()

      self.obj1553.GGLabel.setValue(8)
      self.obj1553.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(224.5,111.5,self.obj1553)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1553.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1553)
      self.obj1553.postAction( self.LHS.CREATE )

      self.obj1554=require(parent)
      self.obj1554.preAction( self.LHS.CREATE )
      self.obj1554.isGraphObjectVisual = True

      if(hasattr(self.obj1554, '_setHierarchicalLink')):
        self.obj1554._setHierarchicalLink(False)

      self.obj1554.GGLabel.setValue(7)
      self.obj1554.graphClass_= graph_require
      if parent.genGraphics:
         new_obj = graph_require(242.5,192.5,self.obj1554)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1554.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1554)
      self.obj1554.postAction( self.LHS.CREATE )

      self.obj1555=require(parent)
      self.obj1555.preAction( self.LHS.CREATE )
      self.obj1555.isGraphObjectVisual = True

      if(hasattr(self.obj1555, '_setHierarchicalLink')):
        self.obj1555._setHierarchicalLink(False)

      self.obj1555.GGLabel.setValue(9)
      self.obj1555.graphClass_= graph_require
      if parent.genGraphics:
         new_obj = graph_require(351.0,111.5,self.obj1555)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1555.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1555)
      self.obj1555.postAction( self.LHS.CREATE )

      self.obj1548.out_connections_.append(self.obj1552)
      self.obj1552.in_connections_.append(self.obj1548)
      self.obj1548.graphObject_.pendingConnections.append((self.obj1548.graphObject_.tag, self.obj1552.graphObject_.tag, [137.0, 82.0, 143.0, 120.5], 2, 0))
      self.obj1548.out_connections_.append(self.obj1553)
      self.obj1553.in_connections_.append(self.obj1548)
      self.obj1548.graphObject_.pendingConnections.append((self.obj1548.graphObject_.tag, self.obj1553.graphObject_.tag, [125.0, 82.0, 224.5, 111.5], 0, True))
      self.obj1551.out_connections_.append(self.obj1554)
      self.obj1554.in_connections_.append(self.obj1551)
      self.obj1551.graphObject_.pendingConnections.append((self.obj1551.graphObject_.tag, self.obj1554.graphObject_.tag, [324.0, 186.0, 242.5, 192.5], 0, True))
      self.obj1551.out_connections_.append(self.obj1555)
      self.obj1555.in_connections_.append(self.obj1551)
      self.obj1551.graphObject_.pendingConnections.append((self.obj1551.graphObject_.tag, self.obj1555.graphObject_.tag, [331.0, 140.0, 351.0, 111.5], 0, True))
      self.obj1552.out_connections_.append(self.obj1550)
      self.obj1550.in_connections_.append(self.obj1552)
      self.obj1552.graphObject_.pendingConnections.append((self.obj1552.graphObject_.tag, self.obj1550.graphObject_.tag, [161.0, 159.0, 143.0, 120.5], 0, True))
      self.obj1553.out_connections_.append(self.obj1551)
      self.obj1551.in_connections_.append(self.obj1553)
      self.obj1553.graphObject_.pendingConnections.append((self.obj1553.graphObject_.tag, self.obj1551.graphObject_.tag, [324.0, 141.0, 224.5, 111.5], 0, True))
      self.obj1554.out_connections_.append(self.obj1550)
      self.obj1550.in_connections_.append(self.obj1554)
      self.obj1554.graphObject_.pendingConnections.append((self.obj1554.graphObject_.tag, self.obj1550.graphObject_.tag, [161.0, 199.0, 242.5, 192.5], 0, True))
      self.obj1555.out_connections_.append(self.obj1549)
      self.obj1549.in_connections_.append(self.obj1555)
      self.obj1555.graphObject_.pendingConnections.append((self.obj1555.graphObject_.tag, self.obj1549.graphObject_.tag, [371.0, 83.0, 351.0, 111.5], 0, True))

      self.RHS = ASG_omacs(parent)

      self.obj1557=Agent(parent)
      self.obj1557.preAction( self.RHS.CREATE )
      self.obj1557.isGraphObjectVisual = True

      if(hasattr(self.obj1557, '_setHierarchicalLink')):
        self.obj1557._setHierarchicalLink(False)

      # price
      self.obj1557.price.setNone()

      # name
      self.obj1557.name.setValue('')
      self.obj1557.name.setNone()

      self.obj1557.GGLabel.setValue(1)
      self.obj1557.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(100.0,20.0,self.obj1557)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1557.graphObject_ = new_obj
      self.obj15570= AttrCalc()
      self.obj15570.Copy=ATOM3Boolean()
      self.obj15570.Copy.setValue(('Copy from LHS', 1))
      self.obj15570.Copy.config = 0
      self.obj15570.Specify=ATOM3Constraint()
      self.obj15570.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1557.GGset2Any['price']= self.obj15570
      self.obj15571= AttrCalc()
      self.obj15571.Copy=ATOM3Boolean()
      self.obj15571.Copy.setValue(('Copy from LHS', 1))
      self.obj15571.Copy.config = 0
      self.obj15571.Specify=ATOM3Constraint()
      self.obj15571.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1557.GGset2Any['name']= self.obj15571

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1557)
      self.obj1557.postAction( self.RHS.CREATE )

      self.obj1558=Capabilitie(parent)
      self.obj1558.preAction( self.RHS.CREATE )
      self.obj1558.isGraphObjectVisual = True

      if(hasattr(self.obj1558, '_setHierarchicalLink')):
        self.obj1558._setHierarchicalLink(False)

      # name
      self.obj1558.name.setValue('')
      self.obj1558.name.setNone()

      self.obj1558.GGLabel.setValue(3)
      self.obj1558.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(340.0,40.0,self.obj1558)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1558.graphObject_ = new_obj
      self.obj15580= AttrCalc()
      self.obj15580.Copy=ATOM3Boolean()
      self.obj15580.Copy.setValue(('Copy from LHS', 1))
      self.obj15580.Copy.config = 0
      self.obj15580.Specify=ATOM3Constraint()
      self.obj15580.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1558.GGset2Any['name']= self.obj15580

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1558)
      self.obj1558.postAction( self.RHS.CREATE )

      self.obj1559=Capabilitie(parent)
      self.obj1559.preAction( self.RHS.CREATE )
      self.obj1559.isGraphObjectVisual = True

      if(hasattr(self.obj1559, '_setHierarchicalLink')):
        self.obj1559._setHierarchicalLink(False)

      # name
      self.obj1559.name.setValue('')
      self.obj1559.name.setNone()

      self.obj1559.GGLabel.setValue(4)
      self.obj1559.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(140.0,160.0,self.obj1559)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1559.graphObject_ = new_obj
      self.obj15590= AttrCalc()
      self.obj15590.Copy=ATOM3Boolean()
      self.obj15590.Copy.setValue(('Copy from LHS', 1))
      self.obj15590.Copy.config = 0
      self.obj15590.Specify=ATOM3Constraint()
      self.obj15590.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1559.GGset2Any['name']= self.obj15590

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1559)
      self.obj1559.postAction( self.RHS.CREATE )

      self.obj1560=Role(parent)
      self.obj1560.preAction( self.RHS.CREATE )
      self.obj1560.isGraphObjectVisual = True

      if(hasattr(self.obj1560, '_setHierarchicalLink')):
        self.obj1560._setHierarchicalLink(False)

      # name
      self.obj1560.name.setValue('')
      self.obj1560.name.setNone()

      self.obj1560.GGLabel.setValue(2)
      self.obj1560.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(300.0,140.0,self.obj1560)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1560.graphObject_ = new_obj
      self.obj15600= AttrCalc()
      self.obj15600.Copy=ATOM3Boolean()
      self.obj15600.Copy.setValue(('Copy from LHS', 1))
      self.obj15600.Copy.config = 0
      self.obj15600.Specify=ATOM3Constraint()
      self.obj15600.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1560.GGset2Any['name']= self.obj15600

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1560)
      self.obj1560.postAction( self.RHS.CREATE )

      self.obj1561=posses(parent)
      self.obj1561.preAction( self.RHS.CREATE )
      self.obj1561.isGraphObjectVisual = True

      if(hasattr(self.obj1561, '_setHierarchicalLink')):
        self.obj1561._setHierarchicalLink(False)

      # rate
      self.obj1561.rate.setNone()

      self.obj1561.GGLabel.setValue(5)
      self.obj1561.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(143.0,120.5,self.obj1561)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1561.graphObject_ = new_obj
      self.obj15610= AttrCalc()
      self.obj15610.Copy=ATOM3Boolean()
      self.obj15610.Copy.setValue(('Copy from LHS', 1))
      self.obj15610.Copy.config = 0
      self.obj15610.Specify=ATOM3Constraint()
      self.obj15610.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1561.GGset2Any['rate']= self.obj15610

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1561)
      self.obj1561.postAction( self.RHS.CREATE )

      self.obj1562=require(parent)
      self.obj1562.preAction( self.RHS.CREATE )
      self.obj1562.isGraphObjectVisual = True

      if(hasattr(self.obj1562, '_setHierarchicalLink')):
        self.obj1562._setHierarchicalLink(False)

      self.obj1562.GGLabel.setValue(7)
      self.obj1562.graphClass_= graph_require
      if parent.genGraphics:
         new_obj = graph_require(242.5,192.5,self.obj1562)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1562.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1562)
      self.obj1562.postAction( self.RHS.CREATE )

      self.obj1563=require(parent)
      self.obj1563.preAction( self.RHS.CREATE )
      self.obj1563.isGraphObjectVisual = True

      if(hasattr(self.obj1563, '_setHierarchicalLink')):
        self.obj1563._setHierarchicalLink(False)

      self.obj1563.GGLabel.setValue(9)
      self.obj1563.graphClass_= graph_require
      if parent.genGraphics:
         new_obj = graph_require(351.0,111.5,self.obj1563)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1563.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1563)
      self.obj1563.postAction( self.RHS.CREATE )

      self.obj1557.out_connections_.append(self.obj1561)
      self.obj1561.in_connections_.append(self.obj1557)
      self.obj1557.graphObject_.pendingConnections.append((self.obj1557.graphObject_.tag, self.obj1561.graphObject_.tag, [137.0, 82.0, 143.0, 120.5], 2, 0))
      self.obj1560.out_connections_.append(self.obj1562)
      self.obj1562.in_connections_.append(self.obj1560)
      self.obj1560.graphObject_.pendingConnections.append((self.obj1560.graphObject_.tag, self.obj1562.graphObject_.tag, [331.0, 185.0, 242.5, 192.5], 2, 0))
      self.obj1560.out_connections_.append(self.obj1563)
      self.obj1563.in_connections_.append(self.obj1560)
      self.obj1560.graphObject_.pendingConnections.append((self.obj1560.graphObject_.tag, self.obj1563.graphObject_.tag, [331.0, 140.0, 351.0, 111.5], 0, True))
      self.obj1561.out_connections_.append(self.obj1559)
      self.obj1559.in_connections_.append(self.obj1561)
      self.obj1561.graphObject_.pendingConnections.append((self.obj1561.graphObject_.tag, self.obj1559.graphObject_.tag, [171.0, 163.0, 143.0, 120.5], 2, 0))
      self.obj1562.out_connections_.append(self.obj1559)
      self.obj1559.in_connections_.append(self.obj1562)
      self.obj1562.graphObject_.pendingConnections.append((self.obj1562.graphObject_.tag, self.obj1559.graphObject_.tag, [171.0, 203.0, 242.5, 192.5], 2, 0))
      self.obj1563.out_connections_.append(self.obj1558)
      self.obj1558.in_connections_.append(self.obj1563)
      self.obj1563.graphObject_.pendingConnections.append((self.obj1563.graphObject_.tag, self.obj1558.graphObject_.tag, [371.0, 83.0, 351.0, 111.5], 0, True))

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
      
      
      
      

