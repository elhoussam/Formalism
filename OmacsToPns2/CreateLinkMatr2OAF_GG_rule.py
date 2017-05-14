# _ CreateLinkMatr2OAF_GG_rule.py ____________________________________________________________________________
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
class CreateLinkMatr2OAF_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 15)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_pns(parent)
      self.LHS.merge(ASG_omacs(parent))
      self.LHS.merge(ASG_GenericGraph(parent))

      self.obj1677=product(parent)
      self.obj1677.preAction( self.LHS.CREATE )
      self.obj1677.isGraphObjectVisual = True

      if(hasattr(self.obj1677, '_setHierarchicalLink')):
        self.obj1677._setHierarchicalLink(False)

      # MaxFlow
      self.obj1677.MaxFlow.setNone()

      # price
      self.obj1677.price.setValue(0)

      # Name
      self.obj1677.Name.setValue('')
      self.obj1677.Name.setNone()

      # ReqFlow
      self.obj1677.ReqFlow.setNone()

      self.obj1677.GGLabel.setValue(5)
      self.obj1677.graphClass_= graph_product
      if parent.genGraphics:
         new_obj = graph_product(280.0,220.0,self.obj1677)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1677.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1677)
      self.obj1677.postAction( self.LHS.CREATE )

      self.obj1678=metarial(parent)
      self.obj1678.preAction( self.LHS.CREATE )
      self.obj1678.isGraphObjectVisual = True

      if(hasattr(self.obj1678, '_setHierarchicalLink')):
        self.obj1678._setHierarchicalLink(False)

      # MaxFlow
      self.obj1678.MaxFlow.setNone()

      # price
      self.obj1678.price.setValue(0)

      # Name
      self.obj1678.Name.setValue('')
      self.obj1678.Name.setNone()

      # ReqFlow
      self.obj1678.ReqFlow.setNone()

      self.obj1678.GGLabel.setValue(3)
      self.obj1678.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(320.0,40.0,self.obj1678)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1678.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1678)
      self.obj1678.postAction( self.LHS.CREATE )

      self.obj1679=Goal(parent)
      self.obj1679.preAction( self.LHS.CREATE )
      self.obj1679.isGraphObjectVisual = True

      if(hasattr(self.obj1679, '_setHierarchicalLink')):
        self.obj1679._setHierarchicalLink(False)

      # name
      self.obj1679.name.setValue('')
      self.obj1679.name.setNone()

      self.obj1679.GGLabel.setValue(2)
      self.obj1679.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(180.0,60.0,self.obj1679)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1679.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1679)
      self.obj1679.postAction( self.LHS.CREATE )

      self.obj1680=GenericGraphEdge(parent)
      self.obj1680.preAction( self.LHS.CREATE )
      self.obj1680.isGraphObjectVisual = True

      if(hasattr(self.obj1680, '_setHierarchicalLink')):
        self.obj1680._setHierarchicalLink(False)

      self.obj1680.GGLabel.setValue(4)
      self.obj1680.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(264.5,71.5,self.obj1680)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1680.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1680)
      self.obj1680.postAction( self.LHS.CREATE )

      self.obj1679.out_connections_.append(self.obj1680)
      self.obj1680.in_connections_.append(self.obj1679)
      self.obj1679.graphObject_.pendingConnections.append((self.obj1679.graphObject_.tag, self.obj1680.graphObject_.tag, [203.0, 61.0, 264.5, 71.5], 0, True))
      self.obj1680.out_connections_.append(self.obj1678)
      self.obj1678.in_connections_.append(self.obj1680)
      self.obj1680.graphObject_.pendingConnections.append((self.obj1680.graphObject_.tag, self.obj1678.graphObject_.tag, [326.0, 82.0, 264.5, 71.5], 0, True))

      self.RHS = ASG_pns(parent)
      self.RHS.merge(ASG_omacs(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj1684=product(parent)
      self.obj1684.preAction( self.RHS.CREATE )
      self.obj1684.isGraphObjectVisual = True

      if(hasattr(self.obj1684, '_setHierarchicalLink')):
        self.obj1684._setHierarchicalLink(False)

      # MaxFlow
      self.obj1684.MaxFlow.setNone()

      # price
      self.obj1684.price.setValue(0)

      # Name
      self.obj1684.Name.setValue('')
      self.obj1684.Name.setNone()

      # ReqFlow
      self.obj1684.ReqFlow.setNone()

      self.obj1684.GGLabel.setValue(5)
      self.obj1684.graphClass_= graph_product
      if parent.genGraphics:
         new_obj = graph_product(280.0,220.0,self.obj1684)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1684.graphObject_ = new_obj
      self.obj16840= AttrCalc()
      self.obj16840.Copy=ATOM3Boolean()
      self.obj16840.Copy.setValue(('Copy from LHS', 1))
      self.obj16840.Copy.config = 0
      self.obj16840.Specify=ATOM3Constraint()
      self.obj16840.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1684.GGset2Any['MaxFlow']= self.obj16840
      self.obj16841= AttrCalc()
      self.obj16841.Copy=ATOM3Boolean()
      self.obj16841.Copy.setValue(('Copy from LHS', 1))
      self.obj16841.Copy.config = 0
      self.obj16841.Specify=ATOM3Constraint()
      self.obj16841.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1684.GGset2Any['Name']= self.obj16841
      self.obj16842= AttrCalc()
      self.obj16842.Copy=ATOM3Boolean()
      self.obj16842.Copy.setValue(('Copy from LHS', 1))
      self.obj16842.Copy.config = 0
      self.obj16842.Specify=ATOM3Constraint()
      self.obj16842.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1684.GGset2Any['ReqFlow']= self.obj16842

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1684)
      self.obj1684.postAction( self.RHS.CREATE )

      self.obj1685=metarial(parent)
      self.obj1685.preAction( self.RHS.CREATE )
      self.obj1685.isGraphObjectVisual = True

      if(hasattr(self.obj1685, '_setHierarchicalLink')):
        self.obj1685._setHierarchicalLink(False)

      # MaxFlow
      self.obj1685.MaxFlow.setNone()

      # price
      self.obj1685.price.setValue(0)

      # Name
      self.obj1685.Name.setValue('')
      self.obj1685.Name.setNone()

      # ReqFlow
      self.obj1685.ReqFlow.setNone()

      self.obj1685.GGLabel.setValue(3)
      self.obj1685.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(320.0,40.0,self.obj1685)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1685.graphObject_ = new_obj
      self.obj16850= AttrCalc()
      self.obj16850.Copy=ATOM3Boolean()
      self.obj16850.Copy.setValue(('Copy from LHS', 1))
      self.obj16850.Copy.config = 0
      self.obj16850.Specify=ATOM3Constraint()
      self.obj16850.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1685.GGset2Any['MaxFlow']= self.obj16850
      self.obj16851= AttrCalc()
      self.obj16851.Copy=ATOM3Boolean()
      self.obj16851.Copy.setValue(('Copy from LHS', 1))
      self.obj16851.Copy.config = 0
      self.obj16851.Specify=ATOM3Constraint()
      self.obj16851.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1685.GGset2Any['Name']= self.obj16851
      self.obj16852= AttrCalc()
      self.obj16852.Copy=ATOM3Boolean()
      self.obj16852.Copy.setValue(('Copy from LHS', 1))
      self.obj16852.Copy.config = 0
      self.obj16852.Specify=ATOM3Constraint()
      self.obj16852.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1685.GGset2Any['ReqFlow']= self.obj16852

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1685)
      self.obj1685.postAction( self.RHS.CREATE )

      self.obj1686=operatingUnit(parent)
      self.obj1686.preAction( self.RHS.CREATE )
      self.obj1686.isGraphObjectVisual = True

      if(hasattr(self.obj1686, '_setHierarchicalLink')):
        self.obj1686._setHierarchicalLink(False)

      # OperCostProp
      self.obj1686.OperCostProp.setValue(1.0)

      # name
      self.obj1686.name.setValue('')
      self.obj1686.name.setNone()

      # OperCostFix
      self.obj1686.OperCostFix.setValue(2.0)

      self.obj1686.GGLabel.setValue(7)
      self.obj1686.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(320.0,140.0,self.obj1686)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1686.graphObject_ = new_obj
      self.obj16860= AttrCalc()
      self.obj16860.Copy=ATOM3Boolean()
      self.obj16860.Copy.setValue(('Copy from LHS', 0))
      self.obj16860.Copy.config = 0
      self.obj16860.Specify=ATOM3Constraint()
      self.obj16860.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1686.GGset2Any['OperCostProp']= self.obj16860
      self.obj16861= AttrCalc()
      self.obj16861.Copy=ATOM3Boolean()
      self.obj16861.Copy.setValue(('Copy from LHS', 0))
      self.obj16861.Copy.config = 0
      self.obj16861.Specify=ATOM3Constraint()
      self.obj16861.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(2)).name.getValue()+\' OAF\'\n'))
      self.obj1686.GGset2Any['name']= self.obj16861
      self.obj16862= AttrCalc()
      self.obj16862.Copy=ATOM3Boolean()
      self.obj16862.Copy.setValue(('Copy from LHS', 0))
      self.obj16862.Copy.config = 0
      self.obj16862.Specify=ATOM3Constraint()
      self.obj16862.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1686.GGset2Any['OperCostFix']= self.obj16862

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1686)
      self.obj1686.postAction( self.RHS.CREATE )

      self.obj1687=intoProduct(parent)
      self.obj1687.preAction( self.RHS.CREATE )
      self.obj1687.isGraphObjectVisual = True

      if(hasattr(self.obj1687, '_setHierarchicalLink')):
        self.obj1687._setHierarchicalLink(False)

      # rate
      self.obj1687.rate.setValue(1.0)

      self.obj1687.GGLabel.setValue(9)
      self.obj1687.graphClass_= graph_intoProduct
      if parent.genGraphics:
         new_obj = graph_intoProduct(322.0,179.0,self.obj1687)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1687.graphObject_ = new_obj
      self.obj16870= AttrCalc()
      self.obj16870.Copy=ATOM3Boolean()
      self.obj16870.Copy.setValue(('Copy from LHS', 0))
      self.obj16870.Copy.config = 0
      self.obj16870.Specify=ATOM3Constraint()
      self.obj16870.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1687.GGset2Any['rate']= self.obj16870

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1687)
      self.obj1687.postAction( self.RHS.CREATE )

      self.obj1688=fromMaterial(parent)
      self.obj1688.preAction( self.RHS.CREATE )
      self.obj1688.isGraphObjectVisual = True

      if(hasattr(self.obj1688, '_setHierarchicalLink')):
        self.obj1688._setHierarchicalLink(False)

      # rate
      self.obj1688.rate.setValue(1.0)

      self.obj1688.GGLabel.setValue(8)
      self.obj1688.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(342.0,110.0,self.obj1688)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1688.graphObject_ = new_obj
      self.obj16880= AttrCalc()
      self.obj16880.Copy=ATOM3Boolean()
      self.obj16880.Copy.setValue(('Copy from LHS', 0))
      self.obj16880.Copy.config = 0
      self.obj16880.Specify=ATOM3Constraint()
      self.obj16880.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1688.GGset2Any['rate']= self.obj16880

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1688)
      self.obj1688.postAction( self.RHS.CREATE )

      self.obj1689=Goal(parent)
      self.obj1689.preAction( self.RHS.CREATE )
      self.obj1689.isGraphObjectVisual = True

      if(hasattr(self.obj1689, '_setHierarchicalLink')):
        self.obj1689._setHierarchicalLink(False)

      # name
      self.obj1689.name.setValue('')
      self.obj1689.name.setNone()

      self.obj1689.GGLabel.setValue(2)
      self.obj1689.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(180.0,60.0,self.obj1689)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1689.graphObject_ = new_obj
      self.obj16890= AttrCalc()
      self.obj16890.Copy=ATOM3Boolean()
      self.obj16890.Copy.setValue(('Copy from LHS', 1))
      self.obj16890.Copy.config = 0
      self.obj16890.Specify=ATOM3Constraint()
      self.obj16890.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1689.GGset2Any['name']= self.obj16890

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1689)
      self.obj1689.postAction( self.RHS.CREATE )

      self.obj1690=GenericGraphEdge(parent)
      self.obj1690.preAction( self.RHS.CREATE )
      self.obj1690.isGraphObjectVisual = True

      if(hasattr(self.obj1690, '_setHierarchicalLink')):
        self.obj1690._setHierarchicalLink(False)

      self.obj1690.GGLabel.setValue(4)
      self.obj1690.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(264.5,71.5,self.obj1690)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1690.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1690)
      self.obj1690.postAction( self.RHS.CREATE )

      self.obj1685.out_connections_.append(self.obj1688)
      self.obj1688.in_connections_.append(self.obj1685)
      self.obj1685.graphObject_.pendingConnections.append((self.obj1685.graphObject_.tag, self.obj1688.graphObject_.tag, [244.0, 89.0, 342.0, 110.0], 0, True))
      self.obj1686.out_connections_.append(self.obj1687)
      self.obj1687.in_connections_.append(self.obj1686)
      self.obj1686.graphObject_.pendingConnections.append((self.obj1686.graphObject_.tag, self.obj1687.graphObject_.tag, [339.0, 158.0, 322.0, 179.0], 0, True))
      self.obj1687.out_connections_.append(self.obj1684)
      self.obj1684.in_connections_.append(self.obj1687)
      self.obj1687.graphObject_.pendingConnections.append((self.obj1687.graphObject_.tag, self.obj1684.graphObject_.tag, [305.0, 220.0, 322.0, 179.0], 0, True))
      self.obj1688.out_connections_.append(self.obj1686)
      self.obj1686.in_connections_.append(self.obj1688)
      self.obj1688.graphObject_.pendingConnections.append((self.obj1688.graphObject_.tag, self.obj1686.graphObject_.tag, [340.0, 151.0, 342.0, 110.0], 0, True))
      self.obj1689.out_connections_.append(self.obj1690)
      self.obj1690.in_connections_.append(self.obj1689)
      self.obj1689.graphObject_.pendingConnections.append((self.obj1689.graphObject_.tag, self.obj1690.graphObject_.tag, [93.0, 61.0, 264.5, 71.5], 2, 0))
      self.obj1690.out_connections_.append(self.obj1685)
      self.obj1685.in_connections_.append(self.obj1690)
      self.obj1690.graphObject_.pendingConnections.append((self.obj1690.graphObject_.tag, self.obj1685.graphObject_.tag, [226.0, 82.0, 264.5, 71.5], 2, 0))

   def condition(self, graphID, isograph, atom3i):
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(3))
      return not hasattr(node, "link2oaf")
      

   def action(self, graphID, isograph, atom3i):
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(3))
      node.link2oaf = True
      
      

