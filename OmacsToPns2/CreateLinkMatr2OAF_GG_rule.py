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

      self.obj676=product(parent)
      self.obj676.preAction( self.LHS.CREATE )
      self.obj676.isGraphObjectVisual = True

      if(hasattr(self.obj676, '_setHierarchicalLink')):
        self.obj676._setHierarchicalLink(False)

      # MaxFlow
      self.obj676.MaxFlow.setNone()

      # price
      self.obj676.price.setValue(0)

      # Name
      self.obj676.Name.setValue('')
      self.obj676.Name.setNone()

      # ReqFlow
      self.obj676.ReqFlow.setNone()

      self.obj676.GGLabel.setValue(5)
      self.obj676.graphClass_= graph_product
      if parent.genGraphics:
         new_obj = graph_product(280.0,220.0,self.obj676)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj676.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj676)
      self.obj676.postAction( self.LHS.CREATE )

      self.obj677=metarial(parent)
      self.obj677.preAction( self.LHS.CREATE )
      self.obj677.isGraphObjectVisual = True

      if(hasattr(self.obj677, '_setHierarchicalLink')):
        self.obj677._setHierarchicalLink(False)

      # MaxFlow
      self.obj677.MaxFlow.setNone()

      # price
      self.obj677.price.setValue(0)

      # Name
      self.obj677.Name.setValue('')
      self.obj677.Name.setNone()

      # ReqFlow
      self.obj677.ReqFlow.setNone()

      self.obj677.GGLabel.setValue(3)
      self.obj677.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(320.0,40.0,self.obj677)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj677.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj677)
      self.obj677.postAction( self.LHS.CREATE )

      self.obj678=Goal(parent)
      self.obj678.preAction( self.LHS.CREATE )
      self.obj678.isGraphObjectVisual = True

      if(hasattr(self.obj678, '_setHierarchicalLink')):
        self.obj678._setHierarchicalLink(False)

      # name
      self.obj678.name.setValue('')
      self.obj678.name.setNone()

      self.obj678.GGLabel.setValue(2)
      self.obj678.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(180.0,60.0,self.obj678)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj678.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj678)
      self.obj678.postAction( self.LHS.CREATE )

      self.obj679=GenericGraphEdge(parent)
      self.obj679.preAction( self.LHS.CREATE )
      self.obj679.isGraphObjectVisual = True

      if(hasattr(self.obj679, '_setHierarchicalLink')):
        self.obj679._setHierarchicalLink(False)

      self.obj679.GGLabel.setValue(4)
      self.obj679.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(264.5,71.5,self.obj679)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj679.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj679)
      self.obj679.postAction( self.LHS.CREATE )

      self.obj678.out_connections_.append(self.obj679)
      self.obj679.in_connections_.append(self.obj678)
      self.obj678.graphObject_.pendingConnections.append((self.obj678.graphObject_.tag, self.obj679.graphObject_.tag, [203.0, 61.0, 264.5, 71.5], 0, True))
      self.obj679.out_connections_.append(self.obj677)
      self.obj677.in_connections_.append(self.obj679)
      self.obj679.graphObject_.pendingConnections.append((self.obj679.graphObject_.tag, self.obj677.graphObject_.tag, [326.0, 82.0, 264.5, 71.5], 0, True))

      self.RHS = ASG_pns(parent)
      self.RHS.merge(ASG_omacs(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj683=product(parent)
      self.obj683.preAction( self.RHS.CREATE )
      self.obj683.isGraphObjectVisual = True

      if(hasattr(self.obj683, '_setHierarchicalLink')):
        self.obj683._setHierarchicalLink(False)

      # MaxFlow
      self.obj683.MaxFlow.setNone()

      # price
      self.obj683.price.setValue(0)

      # Name
      self.obj683.Name.setValue('')
      self.obj683.Name.setNone()

      # ReqFlow
      self.obj683.ReqFlow.setNone()

      self.obj683.GGLabel.setValue(5)
      self.obj683.graphClass_= graph_product
      if parent.genGraphics:
         new_obj = graph_product(280.0,220.0,self.obj683)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj683.graphObject_ = new_obj
      self.obj6830= AttrCalc()
      self.obj6830.Copy=ATOM3Boolean()
      self.obj6830.Copy.setValue(('Copy from LHS', 1))
      self.obj6830.Copy.config = 0
      self.obj6830.Specify=ATOM3Constraint()
      self.obj6830.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj683.GGset2Any['MaxFlow']= self.obj6830
      self.obj6831= AttrCalc()
      self.obj6831.Copy=ATOM3Boolean()
      self.obj6831.Copy.setValue(('Copy from LHS', 1))
      self.obj6831.Copy.config = 0
      self.obj6831.Specify=ATOM3Constraint()
      self.obj6831.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj683.GGset2Any['Name']= self.obj6831
      self.obj6832= AttrCalc()
      self.obj6832.Copy=ATOM3Boolean()
      self.obj6832.Copy.setValue(('Copy from LHS', 1))
      self.obj6832.Copy.config = 0
      self.obj6832.Specify=ATOM3Constraint()
      self.obj6832.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj683.GGset2Any['ReqFlow']= self.obj6832

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj683)
      self.obj683.postAction( self.RHS.CREATE )

      self.obj684=metarial(parent)
      self.obj684.preAction( self.RHS.CREATE )
      self.obj684.isGraphObjectVisual = True

      if(hasattr(self.obj684, '_setHierarchicalLink')):
        self.obj684._setHierarchicalLink(False)

      # MaxFlow
      self.obj684.MaxFlow.setNone()

      # price
      self.obj684.price.setValue(0)

      # Name
      self.obj684.Name.setValue('')
      self.obj684.Name.setNone()

      # ReqFlow
      self.obj684.ReqFlow.setNone()

      self.obj684.GGLabel.setValue(3)
      self.obj684.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(320.0,40.0,self.obj684)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj684.graphObject_ = new_obj
      self.obj6840= AttrCalc()
      self.obj6840.Copy=ATOM3Boolean()
      self.obj6840.Copy.setValue(('Copy from LHS', 1))
      self.obj6840.Copy.config = 0
      self.obj6840.Specify=ATOM3Constraint()
      self.obj6840.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj684.GGset2Any['MaxFlow']= self.obj6840
      self.obj6841= AttrCalc()
      self.obj6841.Copy=ATOM3Boolean()
      self.obj6841.Copy.setValue(('Copy from LHS', 1))
      self.obj6841.Copy.config = 0
      self.obj6841.Specify=ATOM3Constraint()
      self.obj6841.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj684.GGset2Any['Name']= self.obj6841
      self.obj6842= AttrCalc()
      self.obj6842.Copy=ATOM3Boolean()
      self.obj6842.Copy.setValue(('Copy from LHS', 1))
      self.obj6842.Copy.config = 0
      self.obj6842.Specify=ATOM3Constraint()
      self.obj6842.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj684.GGset2Any['ReqFlow']= self.obj6842

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj684)
      self.obj684.postAction( self.RHS.CREATE )

      self.obj685=operatingUnit(parent)
      self.obj685.preAction( self.RHS.CREATE )
      self.obj685.isGraphObjectVisual = True

      if(hasattr(self.obj685, '_setHierarchicalLink')):
        self.obj685._setHierarchicalLink(False)

      # OperCostProp
      self.obj685.OperCostProp.setValue(1.0)

      # name
      self.obj685.name.setValue('')
      self.obj685.name.setNone()

      # OperCostFix
      self.obj685.OperCostFix.setValue(2.0)

      self.obj685.GGLabel.setValue(7)
      self.obj685.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(320.0,140.0,self.obj685)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj685.graphObject_ = new_obj
      self.obj6850= AttrCalc()
      self.obj6850.Copy=ATOM3Boolean()
      self.obj6850.Copy.setValue(('Copy from LHS', 0))
      self.obj6850.Copy.config = 0
      self.obj6850.Specify=ATOM3Constraint()
      self.obj6850.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj685.GGset2Any['OperCostProp']= self.obj6850
      self.obj6851= AttrCalc()
      self.obj6851.Copy=ATOM3Boolean()
      self.obj6851.Copy.setValue(('Copy from LHS', 0))
      self.obj6851.Copy.config = 0
      self.obj6851.Specify=ATOM3Constraint()
      self.obj6851.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(2)).name.getValue()+\' OAF\'\n'))
      self.obj685.GGset2Any['name']= self.obj6851
      self.obj6852= AttrCalc()
      self.obj6852.Copy=ATOM3Boolean()
      self.obj6852.Copy.setValue(('Copy from LHS', 0))
      self.obj6852.Copy.config = 0
      self.obj6852.Specify=ATOM3Constraint()
      self.obj6852.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj685.GGset2Any['OperCostFix']= self.obj6852

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj685)
      self.obj685.postAction( self.RHS.CREATE )

      self.obj686=intoProduct(parent)
      self.obj686.preAction( self.RHS.CREATE )
      self.obj686.isGraphObjectVisual = True

      if(hasattr(self.obj686, '_setHierarchicalLink')):
        self.obj686._setHierarchicalLink(False)

      # rate
      self.obj686.rate.setValue(1.0)

      self.obj686.GGLabel.setValue(9)
      self.obj686.graphClass_= graph_intoProduct
      if parent.genGraphics:
         new_obj = graph_intoProduct(322.0,179.0,self.obj686)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj686.graphObject_ = new_obj
      self.obj6860= AttrCalc()
      self.obj6860.Copy=ATOM3Boolean()
      self.obj6860.Copy.setValue(('Copy from LHS', 0))
      self.obj6860.Copy.config = 0
      self.obj6860.Specify=ATOM3Constraint()
      self.obj6860.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj686.GGset2Any['rate']= self.obj6860

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj686)
      self.obj686.postAction( self.RHS.CREATE )

      self.obj687=fromMaterial(parent)
      self.obj687.preAction( self.RHS.CREATE )
      self.obj687.isGraphObjectVisual = True

      if(hasattr(self.obj687, '_setHierarchicalLink')):
        self.obj687._setHierarchicalLink(False)

      # rate
      self.obj687.rate.setValue(1.0)

      self.obj687.GGLabel.setValue(8)
      self.obj687.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(342.0,110.0,self.obj687)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj687.graphObject_ = new_obj
      self.obj6870= AttrCalc()
      self.obj6870.Copy=ATOM3Boolean()
      self.obj6870.Copy.setValue(('Copy from LHS', 0))
      self.obj6870.Copy.config = 0
      self.obj6870.Specify=ATOM3Constraint()
      self.obj6870.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj687.GGset2Any['rate']= self.obj6870

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj687)
      self.obj687.postAction( self.RHS.CREATE )

      self.obj688=Goal(parent)
      self.obj688.preAction( self.RHS.CREATE )
      self.obj688.isGraphObjectVisual = True

      if(hasattr(self.obj688, '_setHierarchicalLink')):
        self.obj688._setHierarchicalLink(False)

      # name
      self.obj688.name.setValue('')
      self.obj688.name.setNone()

      self.obj688.GGLabel.setValue(2)
      self.obj688.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(180.0,60.0,self.obj688)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj688.graphObject_ = new_obj
      self.obj6880= AttrCalc()
      self.obj6880.Copy=ATOM3Boolean()
      self.obj6880.Copy.setValue(('Copy from LHS', 1))
      self.obj6880.Copy.config = 0
      self.obj6880.Specify=ATOM3Constraint()
      self.obj6880.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj688.GGset2Any['name']= self.obj6880

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj688)
      self.obj688.postAction( self.RHS.CREATE )

      self.obj689=GenericGraphEdge(parent)
      self.obj689.preAction( self.RHS.CREATE )
      self.obj689.isGraphObjectVisual = True

      if(hasattr(self.obj689, '_setHierarchicalLink')):
        self.obj689._setHierarchicalLink(False)

      self.obj689.GGLabel.setValue(4)
      self.obj689.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(264.5,71.5,self.obj689)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj689.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj689)
      self.obj689.postAction( self.RHS.CREATE )

      self.obj684.out_connections_.append(self.obj687)
      self.obj687.in_connections_.append(self.obj684)
      self.obj684.graphObject_.pendingConnections.append((self.obj684.graphObject_.tag, self.obj687.graphObject_.tag, [244.0, 89.0, 342.0, 110.0], 0, True))
      self.obj685.out_connections_.append(self.obj686)
      self.obj686.in_connections_.append(self.obj685)
      self.obj685.graphObject_.pendingConnections.append((self.obj685.graphObject_.tag, self.obj686.graphObject_.tag, [339.0, 158.0, 322.0, 179.0], 0, True))
      self.obj686.out_connections_.append(self.obj683)
      self.obj683.in_connections_.append(self.obj686)
      self.obj686.graphObject_.pendingConnections.append((self.obj686.graphObject_.tag, self.obj683.graphObject_.tag, [305.0, 220.0, 322.0, 179.0], 0, True))
      self.obj687.out_connections_.append(self.obj685)
      self.obj685.in_connections_.append(self.obj687)
      self.obj687.graphObject_.pendingConnections.append((self.obj687.graphObject_.tag, self.obj685.graphObject_.tag, [340.0, 151.0, 342.0, 110.0], 0, True))
      self.obj688.out_connections_.append(self.obj689)
      self.obj689.in_connections_.append(self.obj688)
      self.obj688.graphObject_.pendingConnections.append((self.obj688.graphObject_.tag, self.obj689.graphObject_.tag, [93.0, 61.0, 264.5, 71.5], 2, 0))
      self.obj689.out_connections_.append(self.obj684)
      self.obj684.in_connections_.append(self.obj689)
      self.obj689.graphObject_.pendingConnections.append((self.obj689.graphObject_.tag, self.obj684.graphObject_.tag, [226.0, 82.0, 264.5, 71.5], 2, 0))

   def condition(self, graphID, isograph, atom3i):
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(3))
      return not hasattr(node, "link2oaf")
      

   def action(self, graphID, isograph, atom3i):
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(3))
      node.link2oaf = True
      
      

