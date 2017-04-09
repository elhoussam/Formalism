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

      self.obj75=Agent(parent)
      self.obj75.preAction( self.LHS.CREATE )
      self.obj75.isGraphObjectVisual = True

      if(hasattr(self.obj75, '_setHierarchicalLink')):
        self.obj75._setHierarchicalLink(False)

      # price
      self.obj75.price.setNone()

      # name
      self.obj75.name.setValue('')
      self.obj75.name.setNone()

      self.obj75.GGLabel.setValue(1)
      self.obj75.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(80.0,20.0,self.obj75)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj75.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj75)
      self.obj75.postAction( self.LHS.CREATE )

      self.obj76=Capabilitie(parent)
      self.obj76.preAction( self.LHS.CREATE )
      self.obj76.isGraphObjectVisual = True

      if(hasattr(self.obj76, '_setHierarchicalLink')):
        self.obj76._setHierarchicalLink(False)

      # name
      self.obj76.name.setValue('')
      self.obj76.name.setNone()

      self.obj76.GGLabel.setValue(2)
      self.obj76.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(160.0,180.0,self.obj76)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj76.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj76)
      self.obj76.postAction( self.LHS.CREATE )

      self.obj77=Role(parent)
      self.obj77.preAction( self.LHS.CREATE )
      self.obj77.isGraphObjectVisual = True

      if(hasattr(self.obj77, '_setHierarchicalLink')):
        self.obj77._setHierarchicalLink(False)

      # name
      self.obj77.name.setValue('')
      self.obj77.name.setNone()

      self.obj77.GGLabel.setValue(3)
      self.obj77.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(280.0,40.0,self.obj77)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj77.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj77)
      self.obj77.postAction( self.LHS.CREATE )

      self.obj78=posses(parent)
      self.obj78.preAction( self.LHS.CREATE )
      self.obj78.isGraphObjectVisual = True

      if(hasattr(self.obj78, '_setHierarchicalLink')):
        self.obj78._setHierarchicalLink(False)

      # rate
      self.obj78.rate.setNone()

      self.obj78.GGLabel.setValue(4)
      self.obj78.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(143.0,130.5,self.obj78)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj78.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj78)
      self.obj78.postAction( self.LHS.CREATE )

      self.obj79=require(parent)
      self.obj79.preAction( self.LHS.CREATE )
      self.obj79.isGraphObjectVisual = True

      if(hasattr(self.obj79, '_setHierarchicalLink')):
        self.obj79._setHierarchicalLink(False)

      self.obj79.GGLabel.setValue(5)
      self.obj79.graphClass_= graph_require
      if parent.genGraphics:
         new_obj = graph_require(242.5,132.5,self.obj79)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj79.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj79)
      self.obj79.postAction( self.LHS.CREATE )

      self.obj75.out_connections_.append(self.obj78)
      self.obj78.in_connections_.append(self.obj75)
      self.obj75.graphObject_.pendingConnections.append((self.obj75.graphObject_.tag, self.obj78.graphObject_.tag, [105.0, 82.0, 143.0, 130.5], 0, True))
      self.obj77.out_connections_.append(self.obj79)
      self.obj79.in_connections_.append(self.obj77)
      self.obj77.graphObject_.pendingConnections.append((self.obj77.graphObject_.tag, self.obj79.graphObject_.tag, [304.0, 86.0, 242.5, 132.5], 0, True))
      self.obj78.out_connections_.append(self.obj76)
      self.obj76.in_connections_.append(self.obj78)
      self.obj78.graphObject_.pendingConnections.append((self.obj78.graphObject_.tag, self.obj76.graphObject_.tag, [181.0, 179.0, 143.0, 130.5], 0, True))
      self.obj79.out_connections_.append(self.obj76)
      self.obj76.in_connections_.append(self.obj79)
      self.obj79.graphObject_.pendingConnections.append((self.obj79.graphObject_.tag, self.obj76.graphObject_.tag, [181.0, 179.0, 242.5, 132.5], 0, True))

      self.RHS = ASG_omacs(parent)

      self.obj81=Agent(parent)
      self.obj81.preAction( self.RHS.CREATE )
      self.obj81.isGraphObjectVisual = True

      if(hasattr(self.obj81, '_setHierarchicalLink')):
        self.obj81._setHierarchicalLink(False)

      # price
      self.obj81.price.setNone()

      # name
      self.obj81.name.setValue('')
      self.obj81.name.setNone()

      self.obj81.GGLabel.setValue(1)
      self.obj81.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(80.0,20.0,self.obj81)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj81.graphObject_ = new_obj
      self.obj810= AttrCalc()
      self.obj810.Copy=ATOM3Boolean()
      self.obj810.Copy.setValue(('Copy from LHS', 1))
      self.obj810.Copy.config = 0
      self.obj810.Specify=ATOM3Constraint()
      self.obj810.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj81.GGset2Any['price']= self.obj810
      self.obj811= AttrCalc()
      self.obj811.Copy=ATOM3Boolean()
      self.obj811.Copy.setValue(('Copy from LHS', 1))
      self.obj811.Copy.config = 0
      self.obj811.Specify=ATOM3Constraint()
      self.obj811.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj81.GGset2Any['name']= self.obj811

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj81)
      self.obj81.postAction( self.RHS.CREATE )

      self.obj82=Capabilitie(parent)
      self.obj82.preAction( self.RHS.CREATE )
      self.obj82.isGraphObjectVisual = True

      if(hasattr(self.obj82, '_setHierarchicalLink')):
        self.obj82._setHierarchicalLink(False)

      # name
      self.obj82.name.setValue('')
      self.obj82.name.setNone()

      self.obj82.GGLabel.setValue(2)
      self.obj82.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(160.0,180.0,self.obj82)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj82.graphObject_ = new_obj
      self.obj820= AttrCalc()
      self.obj820.Copy=ATOM3Boolean()
      self.obj820.Copy.setValue(('Copy from LHS', 1))
      self.obj820.Copy.config = 0
      self.obj820.Specify=ATOM3Constraint()
      self.obj820.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj82.GGset2Any['name']= self.obj820

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj82)
      self.obj82.postAction( self.RHS.CREATE )

      self.obj83=Role(parent)
      self.obj83.preAction( self.RHS.CREATE )
      self.obj83.isGraphObjectVisual = True

      if(hasattr(self.obj83, '_setHierarchicalLink')):
        self.obj83._setHierarchicalLink(False)

      # name
      self.obj83.name.setValue('')
      self.obj83.name.setNone()

      self.obj83.GGLabel.setValue(3)
      self.obj83.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(280.0,40.0,self.obj83)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj83.graphObject_ = new_obj
      self.obj830= AttrCalc()
      self.obj830.Copy=ATOM3Boolean()
      self.obj830.Copy.setValue(('Copy from LHS', 1))
      self.obj830.Copy.config = 0
      self.obj830.Specify=ATOM3Constraint()
      self.obj830.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj83.GGset2Any['name']= self.obj830

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj83)
      self.obj83.postAction( self.RHS.CREATE )

      self.obj84=posses(parent)
      self.obj84.preAction( self.RHS.CREATE )
      self.obj84.isGraphObjectVisual = True

      if(hasattr(self.obj84, '_setHierarchicalLink')):
        self.obj84._setHierarchicalLink(False)

      # rate
      self.obj84.rate.setNone()

      self.obj84.GGLabel.setValue(4)
      self.obj84.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(143.0,130.5,self.obj84)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj84.graphObject_ = new_obj
      self.obj840= AttrCalc()
      self.obj840.Copy=ATOM3Boolean()
      self.obj840.Copy.setValue(('Copy from LHS', 1))
      self.obj840.Copy.config = 0
      self.obj840.Specify=ATOM3Constraint()
      self.obj840.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj84.GGset2Any['rate']= self.obj840

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj84)
      self.obj84.postAction( self.RHS.CREATE )

      self.obj85=CapableOf(parent)
      self.obj85.preAction( self.RHS.CREATE )
      self.obj85.isGraphObjectVisual = True

      if(hasattr(self.obj85, '_setHierarchicalLink')):
        self.obj85._setHierarchicalLink(False)

      # rate
      self.obj85.rate.setValue(0.0)

      self.obj85.GGLabel.setValue(7)
      self.obj85.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(214.0,83.5,self.obj85)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj85.graphObject_ = new_obj
      self.obj850= AttrCalc()
      self.obj850.Copy=ATOM3Boolean()
      self.obj850.Copy.setValue(('Copy from LHS', 1))
      self.obj850.Copy.config = 0
      self.obj850.Specify=ATOM3Constraint()
      self.obj850.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj85.GGset2Any['rate']= self.obj850

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj85)
      self.obj85.postAction( self.RHS.CREATE )

      self.obj86=require(parent)
      self.obj86.preAction( self.RHS.CREATE )
      self.obj86.isGraphObjectVisual = True

      if(hasattr(self.obj86, '_setHierarchicalLink')):
        self.obj86._setHierarchicalLink(False)

      self.obj86.GGLabel.setValue(5)
      self.obj86.graphClass_= graph_require
      if parent.genGraphics:
         new_obj = graph_require(242.5,132.5,self.obj86)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj86.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj86)
      self.obj86.postAction( self.RHS.CREATE )

      self.obj81.out_connections_.append(self.obj84)
      self.obj84.in_connections_.append(self.obj81)
      self.obj81.graphObject_.pendingConnections.append((self.obj81.graphObject_.tag, self.obj84.graphObject_.tag, [117.0, 82.0, 143.0, 130.5], 2, 0))
      self.obj81.out_connections_.append(self.obj85)
      self.obj85.in_connections_.append(self.obj81)
      self.obj81.graphObject_.pendingConnections.append((self.obj81.graphObject_.tag, self.obj85.graphObject_.tag, [117.0, 82.0, 214.0, 83.5], 0, True))
      self.obj83.out_connections_.append(self.obj86)
      self.obj86.in_connections_.append(self.obj83)
      self.obj83.graphObject_.pendingConnections.append((self.obj83.graphObject_.tag, self.obj86.graphObject_.tag, [311.0, 85.0, 242.5, 132.5], 2, 0))
      self.obj84.out_connections_.append(self.obj82)
      self.obj82.in_connections_.append(self.obj84)
      self.obj84.graphObject_.pendingConnections.append((self.obj84.graphObject_.tag, self.obj82.graphObject_.tag, [191.0, 183.0, 143.0, 130.5], 2, 0))
      self.obj85.out_connections_.append(self.obj83)
      self.obj83.in_connections_.append(self.obj85)
      self.obj85.graphObject_.pendingConnections.append((self.obj85.graphObject_.tag, self.obj83.graphObject_.tag, [311.0, 85.0, 214.0, 83.5], 0, True))
      self.obj86.out_connections_.append(self.obj82)
      self.obj82.in_connections_.append(self.obj86)
      self.obj86.graphObject_.pendingConnections.append((self.obj86.graphObject_.tag, self.obj82.graphObject_.tag, [191.0, 183.0, 242.5, 132.5], 2, 0))

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
      

