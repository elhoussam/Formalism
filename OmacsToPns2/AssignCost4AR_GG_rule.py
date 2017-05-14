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

      self.obj1796=operatingUnit(parent)
      self.obj1796.preAction( self.LHS.CREATE )
      self.obj1796.isGraphObjectVisual = True

      if(hasattr(self.obj1796, '_setHierarchicalLink')):
        self.obj1796._setHierarchicalLink(False)

      # OperCostProp
      self.obj1796.OperCostProp.setNone()

      # name
      self.obj1796.name.setValue('')
      self.obj1796.name.setNone()

      # OperCostFix
      self.obj1796.OperCostFix.setNone()

      self.obj1796.GGLabel.setValue(4)
      self.obj1796.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(280.0,120.0,self.obj1796)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1796.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1796)
      self.obj1796.postAction( self.LHS.CREATE )

      self.obj1797=CapableOf(parent)
      self.obj1797.preAction( self.LHS.CREATE )
      self.obj1797.isGraphObjectVisual = True

      if(hasattr(self.obj1797, '_setHierarchicalLink')):
        self.obj1797._setHierarchicalLink(False)

      # rate
      self.obj1797.rate.setNone()

      self.obj1797.GGLabel.setValue(5)
      self.obj1797.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(160.5,121.5,self.obj1797)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1797.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1797)
      self.obj1797.postAction( self.LHS.CREATE )

      self.obj1798=Agent(parent)
      self.obj1798.preAction( self.LHS.CREATE )
      self.obj1798.isGraphObjectVisual = True

      if(hasattr(self.obj1798, '_setHierarchicalLink')):
        self.obj1798._setHierarchicalLink(False)

      # price
      self.obj1798.price.setNone()

      # name
      self.obj1798.name.setValue('')
      self.obj1798.name.setNone()

      self.obj1798.GGLabel.setValue(1)
      self.obj1798.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(120.0,40.0,self.obj1798)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1798.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1798)
      self.obj1798.postAction( self.LHS.CREATE )

      self.obj1799=Role(parent)
      self.obj1799.preAction( self.LHS.CREATE )
      self.obj1799.isGraphObjectVisual = True

      if(hasattr(self.obj1799, '_setHierarchicalLink')):
        self.obj1799._setHierarchicalLink(False)

      # name
      self.obj1799.name.setValue('')
      self.obj1799.name.setNone()

      self.obj1799.GGLabel.setValue(2)
      self.obj1799.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(140.0,140.0,self.obj1799)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1799.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1799)
      self.obj1799.postAction( self.LHS.CREATE )

      self.obj1800=GenericGraphEdge(parent)
      self.obj1800.preAction( self.LHS.CREATE )
      self.obj1800.isGraphObjectVisual = True

      if(hasattr(self.obj1800, '_setHierarchicalLink')):
        self.obj1800._setHierarchicalLink(False)

      self.obj1800.GGLabel.setValue(3)
      self.obj1800.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(264.75,85.25,self.obj1800)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1800.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1800)
      self.obj1800.postAction( self.LHS.CREATE )

      self.obj1797.out_connections_.append(self.obj1799)
      self.obj1799.in_connections_.append(self.obj1797)
      self.obj1797.graphObject_.pendingConnections.append((self.obj1797.graphObject_.tag, self.obj1799.graphObject_.tag, [164.0, 141.0, 160.5, 121.5], 0, True))
      self.obj1798.out_connections_.append(self.obj1800)
      self.obj1800.in_connections_.append(self.obj1798)
      self.obj1798.graphObject_.pendingConnections.append((self.obj1798.graphObject_.tag, self.obj1800.graphObject_.tag, [145.0, 102.0, 226.0, 83.0, 264.75, 85.25], 2, True))
      self.obj1798.out_connections_.append(self.obj1797)
      self.obj1797.in_connections_.append(self.obj1798)
      self.obj1798.graphObject_.pendingConnections.append((self.obj1798.graphObject_.tag, self.obj1797.graphObject_.tag, [157.0, 102.0, 160.5, 121.5], 0, True))
      self.obj1800.out_connections_.append(self.obj1796)
      self.obj1796.in_connections_.append(self.obj1800)
      self.obj1800.graphObject_.pendingConnections.append((self.obj1800.graphObject_.tag, self.obj1796.graphObject_.tag, [300.0, 121.0, 264.75, 85.25], 2, 0))

      self.RHS = ASG_pns(parent)
      self.RHS.merge(ASG_omacs(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj1804=operatingUnit(parent)
      self.obj1804.preAction( self.RHS.CREATE )
      self.obj1804.isGraphObjectVisual = True

      if(hasattr(self.obj1804, '_setHierarchicalLink')):
        self.obj1804._setHierarchicalLink(False)

      # OperCostProp
      self.obj1804.OperCostProp.setNone()

      # name
      self.obj1804.name.setValue('')
      self.obj1804.name.setNone()

      # OperCostFix
      self.obj1804.OperCostFix.setNone()

      self.obj1804.GGLabel.setValue(4)
      self.obj1804.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(280.0,120.0,self.obj1804)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1804.graphObject_ = new_obj
      self.obj18040= AttrCalc()
      self.obj18040.Copy=ATOM3Boolean()
      self.obj18040.Copy.setValue(('Copy from LHS', 0))
      self.obj18040.Copy.config = 0
      self.obj18040.Specify=ATOM3Constraint()
      self.obj18040.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'a = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) ).name.getValue()\nb = self.getMatched ( graphID , self.LHS.nodeWithLabel(2) ).name.getValue()\nreturn self.graphRewritingSystem.Dictag[ a ][b]\n\n'))
      self.obj1804.GGset2Any['OperCostProp']= self.obj18040
      self.obj18041= AttrCalc()
      self.obj18041.Copy=ATOM3Boolean()
      self.obj18041.Copy.setValue(('Copy from LHS', 1))
      self.obj18041.Copy.config = 0
      self.obj18041.Specify=ATOM3Constraint()
      self.obj18041.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1804.GGset2Any['name']= self.obj18041
      self.obj18042= AttrCalc()
      self.obj18042.Copy=ATOM3Boolean()
      self.obj18042.Copy.setValue(('Copy from LHS', 0))
      self.obj18042.Copy.config = 0
      self.obj18042.Specify=ATOM3Constraint()
      self.obj18042.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1804.GGset2Any['OperCostFix']= self.obj18042

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1804)
      self.obj1804.postAction( self.RHS.CREATE )

      self.obj1805=CapableOf(parent)
      self.obj1805.preAction( self.RHS.CREATE )
      self.obj1805.isGraphObjectVisual = True

      if(hasattr(self.obj1805, '_setHierarchicalLink')):
        self.obj1805._setHierarchicalLink(False)

      # rate
      self.obj1805.rate.setNone()

      self.obj1805.GGLabel.setValue(5)
      self.obj1805.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(160.5,121.5,self.obj1805)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1805.graphObject_ = new_obj
      self.obj18050= AttrCalc()
      self.obj18050.Copy=ATOM3Boolean()
      self.obj18050.Copy.setValue(('Copy from LHS', 1))
      self.obj18050.Copy.config = 0
      self.obj18050.Specify=ATOM3Constraint()
      self.obj18050.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1805.GGset2Any['rate']= self.obj18050

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1805)
      self.obj1805.postAction( self.RHS.CREATE )

      self.obj1806=Agent(parent)
      self.obj1806.preAction( self.RHS.CREATE )
      self.obj1806.isGraphObjectVisual = True

      if(hasattr(self.obj1806, '_setHierarchicalLink')):
        self.obj1806._setHierarchicalLink(False)

      # price
      self.obj1806.price.setNone()

      # name
      self.obj1806.name.setValue('')
      self.obj1806.name.setNone()

      self.obj1806.GGLabel.setValue(1)
      self.obj1806.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(120.0,40.0,self.obj1806)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1806.graphObject_ = new_obj
      self.obj18060= AttrCalc()
      self.obj18060.Copy=ATOM3Boolean()
      self.obj18060.Copy.setValue(('Copy from LHS', 1))
      self.obj18060.Copy.config = 0
      self.obj18060.Specify=ATOM3Constraint()
      self.obj18060.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1806.GGset2Any['price']= self.obj18060
      self.obj18061= AttrCalc()
      self.obj18061.Copy=ATOM3Boolean()
      self.obj18061.Copy.setValue(('Copy from LHS', 1))
      self.obj18061.Copy.config = 0
      self.obj18061.Specify=ATOM3Constraint()
      self.obj18061.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1806.GGset2Any['name']= self.obj18061

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1806)
      self.obj1806.postAction( self.RHS.CREATE )

      self.obj1807=Role(parent)
      self.obj1807.preAction( self.RHS.CREATE )
      self.obj1807.isGraphObjectVisual = True

      if(hasattr(self.obj1807, '_setHierarchicalLink')):
        self.obj1807._setHierarchicalLink(False)

      # name
      self.obj1807.name.setValue('')
      self.obj1807.name.setNone()

      self.obj1807.GGLabel.setValue(2)
      self.obj1807.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(140.0,140.0,self.obj1807)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1807.graphObject_ = new_obj
      self.obj18070= AttrCalc()
      self.obj18070.Copy=ATOM3Boolean()
      self.obj18070.Copy.setValue(('Copy from LHS', 1))
      self.obj18070.Copy.config = 0
      self.obj18070.Specify=ATOM3Constraint()
      self.obj18070.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1807.GGset2Any['name']= self.obj18070

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1807)
      self.obj1807.postAction( self.RHS.CREATE )

      self.obj1808=GenericGraphEdge(parent)
      self.obj1808.preAction( self.RHS.CREATE )
      self.obj1808.isGraphObjectVisual = True

      if(hasattr(self.obj1808, '_setHierarchicalLink')):
        self.obj1808._setHierarchicalLink(False)

      self.obj1808.GGLabel.setValue(3)
      self.obj1808.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(264.75,85.25,self.obj1808)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1808.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1808)
      self.obj1808.postAction( self.RHS.CREATE )

      self.obj1805.out_connections_.append(self.obj1807)
      self.obj1807.in_connections_.append(self.obj1805)
      self.obj1805.graphObject_.pendingConnections.append((self.obj1805.graphObject_.tag, self.obj1807.graphObject_.tag, [171.0, 140.0, 160.5, 121.5], 2, 0))
      self.obj1806.out_connections_.append(self.obj1808)
      self.obj1808.in_connections_.append(self.obj1806)
      self.obj1806.graphObject_.pendingConnections.append((self.obj1806.graphObject_.tag, self.obj1808.graphObject_.tag, [157.0, 102.0, 264.75, 85.25], 2, 0))
      self.obj1806.out_connections_.append(self.obj1805)
      self.obj1805.in_connections_.append(self.obj1806)
      self.obj1806.graphObject_.pendingConnections.append((self.obj1806.graphObject_.tag, self.obj1805.graphObject_.tag, [157.0, 102.0, 160.5, 121.5], 2, 0))
      self.obj1808.out_connections_.append(self.obj1804)
      self.obj1804.in_connections_.append(self.obj1808)
      self.obj1808.graphObject_.pendingConnections.append((self.obj1808.graphObject_.tag, self.obj1804.graphObject_.tag, [300.0, 121.0, 264.75, 85.25], 2, 0))

   def condition(self, graphID, isograph, atom3i):
      AR = self.getMatched(graphID, self.LHS.nodeWithLabel(4))
      return not ( hasattr(AR, "AssignCost" ) )
      
      

   def action(self, graphID, isograph, atom3i):
      AR = self.getMatched(graphID, self.LHS.nodeWithLabel(4))
      AR.AssignCost=True
      print '######################## Assign Cost for '+AR.name.getValue()
      
      

