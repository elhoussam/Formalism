# _ RemoveAgent_GG_rule.py ____________________________________________________________________________
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
class RemoveAgent_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 26)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_pns(parent)
      self.LHS.merge(ASG_omacs(parent))
      self.LHS.merge(ASG_GenericGraph(parent))

      self.obj1826=rawMaterial(parent)
      self.obj1826.preAction( self.LHS.CREATE )
      self.obj1826.isGraphObjectVisual = True

      if(hasattr(self.obj1826, '_setHierarchicalLink')):
        self.obj1826._setHierarchicalLink(False)

      # MaxFlow
      self.obj1826.MaxFlow.setNone()

      # price
      self.obj1826.price.setNone()

      # Name
      self.obj1826.Name.setValue('')
      self.obj1826.Name.setNone()

      # ReqFlow
      self.obj1826.ReqFlow.setNone()

      self.obj1826.GGLabel.setValue(2)
      self.obj1826.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(260.0,40.0,self.obj1826)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1826.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1826)
      self.obj1826.postAction( self.LHS.CREATE )

      self.obj1827=operatingUnit(parent)
      self.obj1827.preAction( self.LHS.CREATE )
      self.obj1827.isGraphObjectVisual = True

      if(hasattr(self.obj1827, '_setHierarchicalLink')):
        self.obj1827._setHierarchicalLink(False)

      # OperCostProp
      self.obj1827.OperCostProp.setNone()

      # name
      self.obj1827.name.setValue('')
      self.obj1827.name.setNone()

      # OperCostFix
      self.obj1827.OperCostFix.setNone()

      self.obj1827.GGLabel.setValue(3)
      self.obj1827.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(280.0,140.0,self.obj1827)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1827.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1827)
      self.obj1827.postAction( self.LHS.CREATE )

      self.obj1828=fromRaw(parent)
      self.obj1828.preAction( self.LHS.CREATE )
      self.obj1828.isGraphObjectVisual = True

      if(hasattr(self.obj1828, '_setHierarchicalLink')):
        self.obj1828._setHierarchicalLink(False)

      # rate
      self.obj1828.rate.setNone()

      self.obj1828.GGLabel.setValue(5)
      self.obj1828.graphClass_= graph_fromRaw
      if parent.genGraphics:
         new_obj = graph_fromRaw(292.0,123.5,self.obj1828)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1828.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1828)
      self.obj1828.postAction( self.LHS.CREATE )

      self.obj1829=Agent(parent)
      self.obj1829.preAction( self.LHS.CREATE )
      self.obj1829.isGraphObjectVisual = True

      if(hasattr(self.obj1829, '_setHierarchicalLink')):
        self.obj1829._setHierarchicalLink(False)

      # price
      self.obj1829.price.setNone()

      # name
      self.obj1829.name.setValue('')
      self.obj1829.name.setNone()

      self.obj1829.GGLabel.setValue(1)
      self.obj1829.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(60.0,60.0,self.obj1829)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1829.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1829)
      self.obj1829.postAction( self.LHS.CREATE )

      self.obj1830=GenericGraphEdge(parent)
      self.obj1830.preAction( self.LHS.CREATE )
      self.obj1830.isGraphObjectVisual = True

      if(hasattr(self.obj1830, '_setHierarchicalLink')):
        self.obj1830._setHierarchicalLink(False)

      self.obj1830.GGLabel.setValue(4)
      self.obj1830.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(184.5,109.0,self.obj1830)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1830.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1830)
      self.obj1830.postAction( self.LHS.CREATE )

      self.obj1831=GenericGraphEdge(parent)
      self.obj1831.preAction( self.LHS.CREATE )
      self.obj1831.isGraphObjectVisual = True

      if(hasattr(self.obj1831, '_setHierarchicalLink')):
        self.obj1831._setHierarchicalLink(False)

      self.obj1831.GGLabel.setValue(6)
      self.obj1831.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(159.0,150.5,self.obj1831)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1831.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1831)
      self.obj1831.postAction( self.LHS.CREATE )

      self.obj1826.out_connections_.append(self.obj1828)
      self.obj1828.in_connections_.append(self.obj1826)
      self.obj1826.graphObject_.pendingConnections.append((self.obj1826.graphObject_.tag, self.obj1828.graphObject_.tag, [284.0, 96.0, 292.0, 123.5], 0, True))
      self.obj1828.out_connections_.append(self.obj1827)
      self.obj1827.in_connections_.append(self.obj1828)
      self.obj1828.graphObject_.pendingConnections.append((self.obj1828.graphObject_.tag, self.obj1827.graphObject_.tag, [300.0, 151.0, 292.0, 123.5], 0, True))
      self.obj1829.out_connections_.append(self.obj1830)
      self.obj1830.in_connections_.append(self.obj1829)
      self.obj1829.graphObject_.pendingConnections.append((self.obj1829.graphObject_.tag, self.obj1830.graphObject_.tag, [85.0, 122.0, 184.5, 109.0], 0, True))
      self.obj1829.out_connections_.append(self.obj1831)
      self.obj1831.in_connections_.append(self.obj1829)
      self.obj1829.graphObject_.pendingConnections.append((self.obj1829.graphObject_.tag, self.obj1831.graphObject_.tag, [85.0, 122.0, 105.5, 141.5, 159.0, 150.5], 2, True))
      self.obj1830.out_connections_.append(self.obj1826)
      self.obj1826.in_connections_.append(self.obj1830)
      self.obj1830.graphObject_.pendingConnections.append((self.obj1830.graphObject_.tag, self.obj1826.graphObject_.tag, [284.0, 96.0, 184.5, 109.0], 0, True))
      self.obj1831.out_connections_.append(self.obj1827)
      self.obj1827.in_connections_.append(self.obj1831)
      self.obj1831.graphObject_.pendingConnections.append((self.obj1831.graphObject_.tag, self.obj1827.graphObject_.tag, [299.0, 158.0, 212.5, 159.5, 159.0, 150.5], 2, True))

      self.RHS = ASG_pns(parent)

      self.obj1833=rawMaterial(parent)
      self.obj1833.preAction( self.RHS.CREATE )
      self.obj1833.isGraphObjectVisual = True

      if(hasattr(self.obj1833, '_setHierarchicalLink')):
        self.obj1833._setHierarchicalLink(False)

      # MaxFlow
      self.obj1833.MaxFlow.setValue(999999)

      # price
      self.obj1833.price.setValue(0)

      # Name
      self.obj1833.Name.setValue('')
      self.obj1833.Name.setNone()

      # ReqFlow
      self.obj1833.ReqFlow.setValue(0)

      self.obj1833.GGLabel.setValue(2)
      self.obj1833.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(160.0,40.0,self.obj1833)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['Text Scale'] = 1.0
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1833.graphObject_ = new_obj
      self.obj18330= AttrCalc()
      self.obj18330.Copy=ATOM3Boolean()
      self.obj18330.Copy.setValue(('Copy from LHS', 1))
      self.obj18330.Copy.config = 0
      self.obj18330.Specify=ATOM3Constraint()
      self.obj18330.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1833.GGset2Any['MaxFlow']= self.obj18330
      self.obj18331= AttrCalc()
      self.obj18331.Copy=ATOM3Boolean()
      self.obj18331.Copy.setValue(('Copy from LHS', 0))
      self.obj18331.Copy.config = 0
      self.obj18331.Specify=ATOM3Constraint()
      self.obj18331.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).price.getValue()\n'))
      self.obj1833.GGset2Any['price']= self.obj18331
      self.obj18332= AttrCalc()
      self.obj18332.Copy=ATOM3Boolean()
      self.obj18332.Copy.setValue(('Copy from LHS', 1))
      self.obj18332.Copy.config = 0
      self.obj18332.Specify=ATOM3Constraint()
      self.obj18332.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1833.GGset2Any['Name']= self.obj18332
      self.obj18333= AttrCalc()
      self.obj18333.Copy=ATOM3Boolean()
      self.obj18333.Copy.setValue(('Copy from LHS', 1))
      self.obj18333.Copy.config = 0
      self.obj18333.Specify=ATOM3Constraint()
      self.obj18333.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1833.GGset2Any['ReqFlow']= self.obj18333

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1833)
      self.obj1833.postAction( self.RHS.CREATE )

      self.obj1834=operatingUnit(parent)
      self.obj1834.preAction( self.RHS.CREATE )
      self.obj1834.isGraphObjectVisual = True

      if(hasattr(self.obj1834, '_setHierarchicalLink')):
        self.obj1834._setHierarchicalLink(False)

      # OperCostProp
      self.obj1834.OperCostProp.setValue(0.0)

      # name
      self.obj1834.name.setValue('')
      self.obj1834.name.setNone()

      # OperCostFix
      self.obj1834.OperCostFix.setValue(0.0)

      self.obj1834.GGLabel.setValue(3)
      self.obj1834.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(120.0,160.0,self.obj1834)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1834.graphObject_ = new_obj
      self.obj18340= AttrCalc()
      self.obj18340.Copy=ATOM3Boolean()
      self.obj18340.Copy.setValue(('Copy from LHS', 1))
      self.obj18340.Copy.config = 0
      self.obj18340.Specify=ATOM3Constraint()
      self.obj18340.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1834.GGset2Any['OperCostProp']= self.obj18340
      self.obj18341= AttrCalc()
      self.obj18341.Copy=ATOM3Boolean()
      self.obj18341.Copy.setValue(('Copy from LHS', 1))
      self.obj18341.Copy.config = 0
      self.obj18341.Specify=ATOM3Constraint()
      self.obj18341.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1834.GGset2Any['name']= self.obj18341
      self.obj18342= AttrCalc()
      self.obj18342.Copy=ATOM3Boolean()
      self.obj18342.Copy.setValue(('Copy from LHS', 1))
      self.obj18342.Copy.config = 0
      self.obj18342.Specify=ATOM3Constraint()
      self.obj18342.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1834.GGset2Any['OperCostFix']= self.obj18342

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1834)
      self.obj1834.postAction( self.RHS.CREATE )

      self.obj1835=fromRaw(parent)
      self.obj1835.preAction( self.RHS.CREATE )
      self.obj1835.isGraphObjectVisual = True

      if(hasattr(self.obj1835, '_setHierarchicalLink')):
        self.obj1835._setHierarchicalLink(False)

      # rate
      self.obj1835.rate.setValue(0.0)

      self.obj1835.GGLabel.setValue(5)
      self.obj1835.graphClass_= graph_fromRaw
      if parent.genGraphics:
         new_obj = graph_fromRaw(177.0,133.5,self.obj1835)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1835.graphObject_ = new_obj
      self.obj18350= AttrCalc()
      self.obj18350.Copy=ATOM3Boolean()
      self.obj18350.Copy.setValue(('Copy from LHS', 1))
      self.obj18350.Copy.config = 0
      self.obj18350.Specify=ATOM3Constraint()
      self.obj18350.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1835.GGset2Any['rate']= self.obj18350

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1835)
      self.obj1835.postAction( self.RHS.CREATE )

      self.obj1833.out_connections_.append(self.obj1835)
      self.obj1835.in_connections_.append(self.obj1833)
      self.obj1833.graphObject_.pendingConnections.append((self.obj1833.graphObject_.tag, self.obj1835.graphObject_.tag, [184.0, 96.0, 177.0, 133.5], 0, True))
      self.obj1835.out_connections_.append(self.obj1834)
      self.obj1834.in_connections_.append(self.obj1835)
      self.obj1835.graphObject_.pendingConnections.append((self.obj1835.graphObject_.tag, self.obj1834.graphObject_.tag, [170.0, 171.0, 177.0, 133.5], 0, True))

   def condition(self, graphID, isograph, atom3i):
      return self.graphRewritingSystem.finalStat > 20 
      

   def action(self, graphID, isograph, atom3i):
      pass

