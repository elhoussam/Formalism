# _ AssignCost4AR_GG_rule.py ____________________________________________________________________________
# File generated automatically by ATOM3. Graph Grammar Rule
# ___________________________________________________________________________________________
from GGrule import *
from Capabilitie import *
from rawMaterial import *
from GenericGraphEdge import *
from Goal import *
from ASG_pns import *
from operatingUnit import *
from metarial import *
from GenericGraphNode import *
from product import *
from Agent import *
from fromMaterial import *
from CapableOf import *
from intoProduct import *
from Role import *
from fromRaw import *
from intoMaterial import *
from ASG_GenericGraph import *
from ASG_omacs import *
from require import *
from achieve import *
from posses import *
class AssignCost4AR_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 23)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_pns(parent)
      self.LHS.merge(ASG_omacs(parent))
      self.LHS.merge(ASG_GenericGraph(parent))

      self.obj795=operatingUnit(parent)
      self.obj795.preAction( self.LHS.CREATE )
      self.obj795.isGraphObjectVisual = True

      if(hasattr(self.obj795, '_setHierarchicalLink')):
        self.obj795._setHierarchicalLink(False)

      # OperCostProp
      self.obj795.OperCostProp.setNone()

      # name
      self.obj795.name.setValue('')
      self.obj795.name.setNone()

      # OperCostFix
      self.obj795.OperCostFix.setNone()

      self.obj795.GGLabel.setValue(4)
      self.obj795.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(280.0,120.0,self.obj795)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj795.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj795)
      self.obj795.postAction( self.LHS.CREATE )

      self.obj796=CapableOf(parent)
      self.obj796.preAction( self.LHS.CREATE )
      self.obj796.isGraphObjectVisual = True

      if(hasattr(self.obj796, '_setHierarchicalLink')):
        self.obj796._setHierarchicalLink(False)

      # rate
      self.obj796.rate.setNone()

      self.obj796.GGLabel.setValue(5)
      self.obj796.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(160.5,121.5,self.obj796)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj796.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj796)
      self.obj796.postAction( self.LHS.CREATE )

      self.obj797=Agent(parent)
      self.obj797.preAction( self.LHS.CREATE )
      self.obj797.isGraphObjectVisual = True

      if(hasattr(self.obj797, '_setHierarchicalLink')):
        self.obj797._setHierarchicalLink(False)

      # price
      self.obj797.price.setNone()

      # name
      self.obj797.name.setValue('')
      self.obj797.name.setNone()

      self.obj797.GGLabel.setValue(1)
      self.obj797.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(120.0,40.0,self.obj797)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj797.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj797)
      self.obj797.postAction( self.LHS.CREATE )

      self.obj798=Role(parent)
      self.obj798.preAction( self.LHS.CREATE )
      self.obj798.isGraphObjectVisual = True

      if(hasattr(self.obj798, '_setHierarchicalLink')):
        self.obj798._setHierarchicalLink(False)

      # name
      self.obj798.name.setValue('')
      self.obj798.name.setNone()

      self.obj798.GGLabel.setValue(2)
      self.obj798.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(140.0,140.0,self.obj798)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj798.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj798)
      self.obj798.postAction( self.LHS.CREATE )

      self.obj799=GenericGraphEdge(parent)
      self.obj799.preAction( self.LHS.CREATE )
      self.obj799.isGraphObjectVisual = True

      if(hasattr(self.obj799, '_setHierarchicalLink')):
        self.obj799._setHierarchicalLink(False)

      self.obj799.GGLabel.setValue(3)
      self.obj799.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(264.75,85.25,self.obj799)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj799.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj799)
      self.obj799.postAction( self.LHS.CREATE )

      self.obj796.out_connections_.append(self.obj798)
      self.obj798.in_connections_.append(self.obj796)
      self.obj796.graphObject_.pendingConnections.append((self.obj796.graphObject_.tag, self.obj798.graphObject_.tag, [164.0, 141.0, 160.5, 121.5], 0, True))
      self.obj797.out_connections_.append(self.obj799)
      self.obj799.in_connections_.append(self.obj797)
      self.obj797.graphObject_.pendingConnections.append((self.obj797.graphObject_.tag, self.obj799.graphObject_.tag, [145.0, 102.0, 226.0, 83.0, 264.75, 85.25], 2, True))
      self.obj797.out_connections_.append(self.obj796)
      self.obj796.in_connections_.append(self.obj797)
      self.obj797.graphObject_.pendingConnections.append((self.obj797.graphObject_.tag, self.obj796.graphObject_.tag, [157.0, 102.0, 160.5, 121.5], 0, True))
      self.obj799.out_connections_.append(self.obj795)
      self.obj795.in_connections_.append(self.obj799)
      self.obj799.graphObject_.pendingConnections.append((self.obj799.graphObject_.tag, self.obj795.graphObject_.tag, [300.0, 121.0, 264.75, 85.25], 2, 0))

      self.RHS = ASG_pns(parent)
      self.RHS.merge(ASG_omacs(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj803=operatingUnit(parent)
      self.obj803.preAction( self.RHS.CREATE )
      self.obj803.isGraphObjectVisual = True

      if(hasattr(self.obj803, '_setHierarchicalLink')):
        self.obj803._setHierarchicalLink(False)

      # OperCostProp
      self.obj803.OperCostProp.setNone()

      # name
      self.obj803.name.setValue('')
      self.obj803.name.setNone()

      # OperCostFix
      self.obj803.OperCostFix.setNone()

      self.obj803.GGLabel.setValue(4)
      self.obj803.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(280.0,120.0,self.obj803)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj803.graphObject_ = new_obj
      self.obj8030= AttrCalc()
      self.obj8030.Copy=ATOM3Boolean()
      self.obj8030.Copy.setValue(('Copy from LHS', 0))
      self.obj8030.Copy.config = 0
      self.obj8030.Specify=ATOM3Constraint()
      self.obj8030.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'a = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) ).name.getValue()\nb = self.getMatched ( graphID , self.LHS.nodeWithLabel(2) ).name.getValue()\nreturn self.graphRewritingSystem.Dictag[ a ][b]\n\n'))
      self.obj803.GGset2Any['OperCostProp']= self.obj8030
      self.obj8031= AttrCalc()
      self.obj8031.Copy=ATOM3Boolean()
      self.obj8031.Copy.setValue(('Copy from LHS', 1))
      self.obj8031.Copy.config = 0
      self.obj8031.Specify=ATOM3Constraint()
      self.obj8031.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj803.GGset2Any['name']= self.obj8031
      self.obj8032= AttrCalc()
      self.obj8032.Copy=ATOM3Boolean()
      self.obj8032.Copy.setValue(('Copy from LHS', 0))
      self.obj8032.Copy.config = 0
      self.obj8032.Specify=ATOM3Constraint()
      self.obj8032.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj803.GGset2Any['OperCostFix']= self.obj8032

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj803)
      self.obj803.postAction( self.RHS.CREATE )

      self.obj804=CapableOf(parent)
      self.obj804.preAction( self.RHS.CREATE )
      self.obj804.isGraphObjectVisual = True

      if(hasattr(self.obj804, '_setHierarchicalLink')):
        self.obj804._setHierarchicalLink(False)

      # rate
      self.obj804.rate.setNone()

      self.obj804.GGLabel.setValue(5)
      self.obj804.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(160.5,121.5,self.obj804)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj804.graphObject_ = new_obj
      self.obj8040= AttrCalc()
      self.obj8040.Copy=ATOM3Boolean()
      self.obj8040.Copy.setValue(('Copy from LHS', 1))
      self.obj8040.Copy.config = 0
      self.obj8040.Specify=ATOM3Constraint()
      self.obj8040.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj804.GGset2Any['rate']= self.obj8040

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj804)
      self.obj804.postAction( self.RHS.CREATE )

      self.obj805=Agent(parent)
      self.obj805.preAction( self.RHS.CREATE )
      self.obj805.isGraphObjectVisual = True

      if(hasattr(self.obj805, '_setHierarchicalLink')):
        self.obj805._setHierarchicalLink(False)

      # price
      self.obj805.price.setNone()

      # name
      self.obj805.name.setValue('')
      self.obj805.name.setNone()

      self.obj805.GGLabel.setValue(1)
      self.obj805.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(120.0,40.0,self.obj805)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj805.graphObject_ = new_obj
      self.obj8050= AttrCalc()
      self.obj8050.Copy=ATOM3Boolean()
      self.obj8050.Copy.setValue(('Copy from LHS', 1))
      self.obj8050.Copy.config = 0
      self.obj8050.Specify=ATOM3Constraint()
      self.obj8050.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj805.GGset2Any['price']= self.obj8050
      self.obj8051= AttrCalc()
      self.obj8051.Copy=ATOM3Boolean()
      self.obj8051.Copy.setValue(('Copy from LHS', 1))
      self.obj8051.Copy.config = 0
      self.obj8051.Specify=ATOM3Constraint()
      self.obj8051.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj805.GGset2Any['name']= self.obj8051

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj805)
      self.obj805.postAction( self.RHS.CREATE )

      self.obj806=Role(parent)
      self.obj806.preAction( self.RHS.CREATE )
      self.obj806.isGraphObjectVisual = True

      if(hasattr(self.obj806, '_setHierarchicalLink')):
        self.obj806._setHierarchicalLink(False)

      # name
      self.obj806.name.setValue('')
      self.obj806.name.setNone()

      self.obj806.GGLabel.setValue(2)
      self.obj806.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(140.0,140.0,self.obj806)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj806.graphObject_ = new_obj
      self.obj8060= AttrCalc()
      self.obj8060.Copy=ATOM3Boolean()
      self.obj8060.Copy.setValue(('Copy from LHS', 1))
      self.obj8060.Copy.config = 0
      self.obj8060.Specify=ATOM3Constraint()
      self.obj8060.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj806.GGset2Any['name']= self.obj8060

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj806)
      self.obj806.postAction( self.RHS.CREATE )

      self.obj807=GenericGraphEdge(parent)
      self.obj807.preAction( self.RHS.CREATE )
      self.obj807.isGraphObjectVisual = True

      if(hasattr(self.obj807, '_setHierarchicalLink')):
        self.obj807._setHierarchicalLink(False)

      self.obj807.GGLabel.setValue(3)
      self.obj807.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(264.75,85.25,self.obj807)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj807.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj807)
      self.obj807.postAction( self.RHS.CREATE )

      self.obj804.out_connections_.append(self.obj806)
      self.obj806.in_connections_.append(self.obj804)
      self.obj804.graphObject_.pendingConnections.append((self.obj804.graphObject_.tag, self.obj806.graphObject_.tag, [171.0, 140.0, 160.5, 121.5], 2, 0))
      self.obj805.out_connections_.append(self.obj807)
      self.obj807.in_connections_.append(self.obj805)
      self.obj805.graphObject_.pendingConnections.append((self.obj805.graphObject_.tag, self.obj807.graphObject_.tag, [157.0, 102.0, 264.75, 85.25], 2, 0))
      self.obj805.out_connections_.append(self.obj804)
      self.obj804.in_connections_.append(self.obj805)
      self.obj805.graphObject_.pendingConnections.append((self.obj805.graphObject_.tag, self.obj804.graphObject_.tag, [157.0, 102.0, 160.5, 121.5], 2, 0))
      self.obj807.out_connections_.append(self.obj803)
      self.obj803.in_connections_.append(self.obj807)
      self.obj807.graphObject_.pendingConnections.append((self.obj807.graphObject_.tag, self.obj803.graphObject_.tag, [300.0, 121.0, 264.75, 85.25], 2, 0))

   def condition(self, graphID, isograph, atom3i):
      AR = self.getMatched(graphID, self.LHS.nodeWithLabel(4))
      return not ( hasattr(AR, "AssignCost" ) )
      
      

   def action(self, graphID, isograph, atom3i):
      AR = self.getMatched(graphID, self.LHS.nodeWithLabel(4))
      AR.AssignCost=True
      print '######################## Assign Cost for '+AR.name.getValue()
      
      

