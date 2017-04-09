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

      self.obj353=rawMaterial(parent)
      self.obj353.preAction( self.LHS.CREATE )
      self.obj353.isGraphObjectVisual = True

      if(hasattr(self.obj353, '_setHierarchicalLink')):
        self.obj353._setHierarchicalLink(False)

      # MaxFlow
      self.obj353.MaxFlow.setNone()

      # price
      self.obj353.price.setNone()

      # Name
      self.obj353.Name.setValue('')
      self.obj353.Name.setNone()

      # ReqFlow
      self.obj353.ReqFlow.setNone()

      self.obj353.GGLabel.setValue(2)
      self.obj353.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(260.0,40.0,self.obj353)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj353.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj353)
      self.obj353.postAction( self.LHS.CREATE )

      self.obj354=operatingUnit(parent)
      self.obj354.preAction( self.LHS.CREATE )
      self.obj354.isGraphObjectVisual = True

      if(hasattr(self.obj354, '_setHierarchicalLink')):
        self.obj354._setHierarchicalLink(False)

      # OperCostProp
      self.obj354.OperCostProp.setNone()

      # name
      self.obj354.name.setValue('')
      self.obj354.name.setNone()

      # OperCostFix
      self.obj354.OperCostFix.setNone()

      self.obj354.GGLabel.setValue(3)
      self.obj354.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(280.0,140.0,self.obj354)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj354.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj354)
      self.obj354.postAction( self.LHS.CREATE )

      self.obj355=fromRaw(parent)
      self.obj355.preAction( self.LHS.CREATE )
      self.obj355.isGraphObjectVisual = True

      if(hasattr(self.obj355, '_setHierarchicalLink')):
        self.obj355._setHierarchicalLink(False)

      # rate
      self.obj355.rate.setNone()

      self.obj355.GGLabel.setValue(5)
      self.obj355.graphClass_= graph_fromRaw
      if parent.genGraphics:
         new_obj = graph_fromRaw(292.0,123.5,self.obj355)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj355.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj355)
      self.obj355.postAction( self.LHS.CREATE )

      self.obj356=Agent(parent)
      self.obj356.preAction( self.LHS.CREATE )
      self.obj356.isGraphObjectVisual = True

      if(hasattr(self.obj356, '_setHierarchicalLink')):
        self.obj356._setHierarchicalLink(False)

      # price
      self.obj356.price.setNone()

      # name
      self.obj356.name.setValue('')
      self.obj356.name.setNone()

      self.obj356.GGLabel.setValue(1)
      self.obj356.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(60.0,60.0,self.obj356)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj356.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj356)
      self.obj356.postAction( self.LHS.CREATE )

      self.obj357=GenericGraphEdge(parent)
      self.obj357.preAction( self.LHS.CREATE )
      self.obj357.isGraphObjectVisual = True

      if(hasattr(self.obj357, '_setHierarchicalLink')):
        self.obj357._setHierarchicalLink(False)

      self.obj357.GGLabel.setValue(4)
      self.obj357.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(184.5,109.0,self.obj357)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj357.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj357)
      self.obj357.postAction( self.LHS.CREATE )

      self.obj358=GenericGraphEdge(parent)
      self.obj358.preAction( self.LHS.CREATE )
      self.obj358.isGraphObjectVisual = True

      if(hasattr(self.obj358, '_setHierarchicalLink')):
        self.obj358._setHierarchicalLink(False)

      self.obj358.GGLabel.setValue(6)
      self.obj358.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(159.0,150.5,self.obj358)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj358.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj358)
      self.obj358.postAction( self.LHS.CREATE )

      self.obj353.out_connections_.append(self.obj355)
      self.obj355.in_connections_.append(self.obj353)
      self.obj353.graphObject_.pendingConnections.append((self.obj353.graphObject_.tag, self.obj355.graphObject_.tag, [284.0, 96.0, 292.0, 123.5], 0, True))
      self.obj355.out_connections_.append(self.obj354)
      self.obj354.in_connections_.append(self.obj355)
      self.obj355.graphObject_.pendingConnections.append((self.obj355.graphObject_.tag, self.obj354.graphObject_.tag, [300.0, 151.0, 292.0, 123.5], 0, True))
      self.obj356.out_connections_.append(self.obj357)
      self.obj357.in_connections_.append(self.obj356)
      self.obj356.graphObject_.pendingConnections.append((self.obj356.graphObject_.tag, self.obj357.graphObject_.tag, [85.0, 122.0, 184.5, 109.0], 0, True))
      self.obj356.out_connections_.append(self.obj358)
      self.obj358.in_connections_.append(self.obj356)
      self.obj356.graphObject_.pendingConnections.append((self.obj356.graphObject_.tag, self.obj358.graphObject_.tag, [85.0, 122.0, 105.5, 141.5, 159.0, 150.5], 2, True))
      self.obj357.out_connections_.append(self.obj353)
      self.obj353.in_connections_.append(self.obj357)
      self.obj357.graphObject_.pendingConnections.append((self.obj357.graphObject_.tag, self.obj353.graphObject_.tag, [284.0, 96.0, 184.5, 109.0], 0, True))
      self.obj358.out_connections_.append(self.obj354)
      self.obj354.in_connections_.append(self.obj358)
      self.obj358.graphObject_.pendingConnections.append((self.obj358.graphObject_.tag, self.obj354.graphObject_.tag, [299.0, 158.0, 212.5, 159.5, 159.0, 150.5], 2, True))

      self.RHS = ASG_pns(parent)

      self.obj360=rawMaterial(parent)
      self.obj360.preAction( self.RHS.CREATE )
      self.obj360.isGraphObjectVisual = True

      if(hasattr(self.obj360, '_setHierarchicalLink')):
        self.obj360._setHierarchicalLink(False)

      # MaxFlow
      self.obj360.MaxFlow.setValue(999999)

      # price
      self.obj360.price.setValue(0)

      # Name
      self.obj360.Name.setValue('')
      self.obj360.Name.setNone()

      # ReqFlow
      self.obj360.ReqFlow.setValue(0)

      self.obj360.GGLabel.setValue(2)
      self.obj360.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(160.0,40.0,self.obj360)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['Text Scale'] = 1.0
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj360.graphObject_ = new_obj
      self.obj3600= AttrCalc()
      self.obj3600.Copy=ATOM3Boolean()
      self.obj3600.Copy.setValue(('Copy from LHS', 1))
      self.obj3600.Copy.config = 0
      self.obj3600.Specify=ATOM3Constraint()
      self.obj3600.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj360.GGset2Any['MaxFlow']= self.obj3600
      self.obj3601= AttrCalc()
      self.obj3601.Copy=ATOM3Boolean()
      self.obj3601.Copy.setValue(('Copy from LHS', 0))
      self.obj3601.Copy.config = 0
      self.obj3601.Specify=ATOM3Constraint()
      self.obj3601.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).price.getValue()\n'))
      self.obj360.GGset2Any['price']= self.obj3601
      self.obj3602= AttrCalc()
      self.obj3602.Copy=ATOM3Boolean()
      self.obj3602.Copy.setValue(('Copy from LHS', 1))
      self.obj3602.Copy.config = 0
      self.obj3602.Specify=ATOM3Constraint()
      self.obj3602.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj360.GGset2Any['Name']= self.obj3602
      self.obj3603= AttrCalc()
      self.obj3603.Copy=ATOM3Boolean()
      self.obj3603.Copy.setValue(('Copy from LHS', 1))
      self.obj3603.Copy.config = 0
      self.obj3603.Specify=ATOM3Constraint()
      self.obj3603.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj360.GGset2Any['ReqFlow']= self.obj3603

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj360)
      self.obj360.postAction( self.RHS.CREATE )

      self.obj361=operatingUnit(parent)
      self.obj361.preAction( self.RHS.CREATE )
      self.obj361.isGraphObjectVisual = True

      if(hasattr(self.obj361, '_setHierarchicalLink')):
        self.obj361._setHierarchicalLink(False)

      # OperCostProp
      self.obj361.OperCostProp.setValue(0.0)

      # name
      self.obj361.name.setValue('')
      self.obj361.name.setNone()

      # OperCostFix
      self.obj361.OperCostFix.setValue(0.0)

      self.obj361.GGLabel.setValue(3)
      self.obj361.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(120.0,160.0,self.obj361)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj361.graphObject_ = new_obj
      self.obj3610= AttrCalc()
      self.obj3610.Copy=ATOM3Boolean()
      self.obj3610.Copy.setValue(('Copy from LHS', 1))
      self.obj3610.Copy.config = 0
      self.obj3610.Specify=ATOM3Constraint()
      self.obj3610.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj361.GGset2Any['OperCostProp']= self.obj3610
      self.obj3611= AttrCalc()
      self.obj3611.Copy=ATOM3Boolean()
      self.obj3611.Copy.setValue(('Copy from LHS', 1))
      self.obj3611.Copy.config = 0
      self.obj3611.Specify=ATOM3Constraint()
      self.obj3611.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj361.GGset2Any['name']= self.obj3611
      self.obj3612= AttrCalc()
      self.obj3612.Copy=ATOM3Boolean()
      self.obj3612.Copy.setValue(('Copy from LHS', 1))
      self.obj3612.Copy.config = 0
      self.obj3612.Specify=ATOM3Constraint()
      self.obj3612.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj361.GGset2Any['OperCostFix']= self.obj3612

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj361)
      self.obj361.postAction( self.RHS.CREATE )

      self.obj362=fromRaw(parent)
      self.obj362.preAction( self.RHS.CREATE )
      self.obj362.isGraphObjectVisual = True

      if(hasattr(self.obj362, '_setHierarchicalLink')):
        self.obj362._setHierarchicalLink(False)

      # rate
      self.obj362.rate.setValue(0.0)

      self.obj362.GGLabel.setValue(5)
      self.obj362.graphClass_= graph_fromRaw
      if parent.genGraphics:
         new_obj = graph_fromRaw(177.0,133.5,self.obj362)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj362.graphObject_ = new_obj
      self.obj3620= AttrCalc()
      self.obj3620.Copy=ATOM3Boolean()
      self.obj3620.Copy.setValue(('Copy from LHS', 1))
      self.obj3620.Copy.config = 0
      self.obj3620.Specify=ATOM3Constraint()
      self.obj3620.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj362.GGset2Any['rate']= self.obj3620

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj362)
      self.obj362.postAction( self.RHS.CREATE )

      self.obj360.out_connections_.append(self.obj362)
      self.obj362.in_connections_.append(self.obj360)
      self.obj360.graphObject_.pendingConnections.append((self.obj360.graphObject_.tag, self.obj362.graphObject_.tag, [184.0, 96.0, 177.0, 133.5], 0, True))
      self.obj362.out_connections_.append(self.obj361)
      self.obj361.in_connections_.append(self.obj362)
      self.obj362.graphObject_.pendingConnections.append((self.obj362.graphObject_.tag, self.obj361.graphObject_.tag, [170.0, 171.0, 177.0, 133.5], 0, True))

   def condition(self, graphID, isograph, atom3i):
      return self.graphRewritingSystem.finalStat > 20 
      

   def action(self, graphID, isograph, atom3i):
      pass

