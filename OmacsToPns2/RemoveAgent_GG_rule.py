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

      self.obj825=rawMaterial(parent)
      self.obj825.preAction( self.LHS.CREATE )
      self.obj825.isGraphObjectVisual = True

      if(hasattr(self.obj825, '_setHierarchicalLink')):
        self.obj825._setHierarchicalLink(False)

      # MaxFlow
      self.obj825.MaxFlow.setNone()

      # price
      self.obj825.price.setNone()

      # Name
      self.obj825.Name.setValue('')
      self.obj825.Name.setNone()

      # ReqFlow
      self.obj825.ReqFlow.setNone()

      self.obj825.GGLabel.setValue(2)
      self.obj825.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(260.0,40.0,self.obj825)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj825.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj825)
      self.obj825.postAction( self.LHS.CREATE )

      self.obj826=operatingUnit(parent)
      self.obj826.preAction( self.LHS.CREATE )
      self.obj826.isGraphObjectVisual = True

      if(hasattr(self.obj826, '_setHierarchicalLink')):
        self.obj826._setHierarchicalLink(False)

      # OperCostProp
      self.obj826.OperCostProp.setNone()

      # name
      self.obj826.name.setValue('')
      self.obj826.name.setNone()

      # OperCostFix
      self.obj826.OperCostFix.setNone()

      self.obj826.GGLabel.setValue(3)
      self.obj826.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(280.0,140.0,self.obj826)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj826.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj826)
      self.obj826.postAction( self.LHS.CREATE )

      self.obj827=fromRaw(parent)
      self.obj827.preAction( self.LHS.CREATE )
      self.obj827.isGraphObjectVisual = True

      if(hasattr(self.obj827, '_setHierarchicalLink')):
        self.obj827._setHierarchicalLink(False)

      # rate
      self.obj827.rate.setNone()

      self.obj827.GGLabel.setValue(5)
      self.obj827.graphClass_= graph_fromRaw
      if parent.genGraphics:
         new_obj = graph_fromRaw(292.0,123.5,self.obj827)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj827.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj827)
      self.obj827.postAction( self.LHS.CREATE )

      self.obj828=Agent(parent)
      self.obj828.preAction( self.LHS.CREATE )
      self.obj828.isGraphObjectVisual = True

      if(hasattr(self.obj828, '_setHierarchicalLink')):
        self.obj828._setHierarchicalLink(False)

      # price
      self.obj828.price.setNone()

      # name
      self.obj828.name.setValue('')
      self.obj828.name.setNone()

      self.obj828.GGLabel.setValue(1)
      self.obj828.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(60.0,60.0,self.obj828)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj828.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj828)
      self.obj828.postAction( self.LHS.CREATE )

      self.obj829=GenericGraphEdge(parent)
      self.obj829.preAction( self.LHS.CREATE )
      self.obj829.isGraphObjectVisual = True

      if(hasattr(self.obj829, '_setHierarchicalLink')):
        self.obj829._setHierarchicalLink(False)

      self.obj829.GGLabel.setValue(4)
      self.obj829.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(184.5,109.0,self.obj829)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj829.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj829)
      self.obj829.postAction( self.LHS.CREATE )

      self.obj830=GenericGraphEdge(parent)
      self.obj830.preAction( self.LHS.CREATE )
      self.obj830.isGraphObjectVisual = True

      if(hasattr(self.obj830, '_setHierarchicalLink')):
        self.obj830._setHierarchicalLink(False)

      self.obj830.GGLabel.setValue(6)
      self.obj830.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(159.0,150.5,self.obj830)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj830.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj830)
      self.obj830.postAction( self.LHS.CREATE )

      self.obj825.out_connections_.append(self.obj827)
      self.obj827.in_connections_.append(self.obj825)
      self.obj825.graphObject_.pendingConnections.append((self.obj825.graphObject_.tag, self.obj827.graphObject_.tag, [284.0, 96.0, 292.0, 123.5], 0, True))
      self.obj827.out_connections_.append(self.obj826)
      self.obj826.in_connections_.append(self.obj827)
      self.obj827.graphObject_.pendingConnections.append((self.obj827.graphObject_.tag, self.obj826.graphObject_.tag, [300.0, 151.0, 292.0, 123.5], 0, True))
      self.obj828.out_connections_.append(self.obj829)
      self.obj829.in_connections_.append(self.obj828)
      self.obj828.graphObject_.pendingConnections.append((self.obj828.graphObject_.tag, self.obj829.graphObject_.tag, [85.0, 122.0, 184.5, 109.0], 0, True))
      self.obj828.out_connections_.append(self.obj830)
      self.obj830.in_connections_.append(self.obj828)
      self.obj828.graphObject_.pendingConnections.append((self.obj828.graphObject_.tag, self.obj830.graphObject_.tag, [85.0, 122.0, 105.5, 141.5, 159.0, 150.5], 2, True))
      self.obj829.out_connections_.append(self.obj825)
      self.obj825.in_connections_.append(self.obj829)
      self.obj829.graphObject_.pendingConnections.append((self.obj829.graphObject_.tag, self.obj825.graphObject_.tag, [284.0, 96.0, 184.5, 109.0], 0, True))
      self.obj830.out_connections_.append(self.obj826)
      self.obj826.in_connections_.append(self.obj830)
      self.obj830.graphObject_.pendingConnections.append((self.obj830.graphObject_.tag, self.obj826.graphObject_.tag, [299.0, 158.0, 212.5, 159.5, 159.0, 150.5], 2, True))

      self.RHS = ASG_pns(parent)

      self.obj832=rawMaterial(parent)
      self.obj832.preAction( self.RHS.CREATE )
      self.obj832.isGraphObjectVisual = True

      if(hasattr(self.obj832, '_setHierarchicalLink')):
        self.obj832._setHierarchicalLink(False)

      # MaxFlow
      self.obj832.MaxFlow.setValue(999999)

      # price
      self.obj832.price.setValue(0)

      # Name
      self.obj832.Name.setValue('')
      self.obj832.Name.setNone()

      # ReqFlow
      self.obj832.ReqFlow.setValue(0)

      self.obj832.GGLabel.setValue(2)
      self.obj832.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(160.0,40.0,self.obj832)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['Text Scale'] = 1.0
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj832.graphObject_ = new_obj
      self.obj8320= AttrCalc()
      self.obj8320.Copy=ATOM3Boolean()
      self.obj8320.Copy.setValue(('Copy from LHS', 1))
      self.obj8320.Copy.config = 0
      self.obj8320.Specify=ATOM3Constraint()
      self.obj8320.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj832.GGset2Any['MaxFlow']= self.obj8320
      self.obj8321= AttrCalc()
      self.obj8321.Copy=ATOM3Boolean()
      self.obj8321.Copy.setValue(('Copy from LHS', 0))
      self.obj8321.Copy.config = 0
      self.obj8321.Specify=ATOM3Constraint()
      self.obj8321.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).price.getValue()\n'))
      self.obj832.GGset2Any['price']= self.obj8321
      self.obj8322= AttrCalc()
      self.obj8322.Copy=ATOM3Boolean()
      self.obj8322.Copy.setValue(('Copy from LHS', 1))
      self.obj8322.Copy.config = 0
      self.obj8322.Specify=ATOM3Constraint()
      self.obj8322.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj832.GGset2Any['Name']= self.obj8322
      self.obj8323= AttrCalc()
      self.obj8323.Copy=ATOM3Boolean()
      self.obj8323.Copy.setValue(('Copy from LHS', 1))
      self.obj8323.Copy.config = 0
      self.obj8323.Specify=ATOM3Constraint()
      self.obj8323.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj832.GGset2Any['ReqFlow']= self.obj8323

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj832)
      self.obj832.postAction( self.RHS.CREATE )

      self.obj833=operatingUnit(parent)
      self.obj833.preAction( self.RHS.CREATE )
      self.obj833.isGraphObjectVisual = True

      if(hasattr(self.obj833, '_setHierarchicalLink')):
        self.obj833._setHierarchicalLink(False)

      # OperCostProp
      self.obj833.OperCostProp.setValue(0.0)

      # name
      self.obj833.name.setValue('')
      self.obj833.name.setNone()

      # OperCostFix
      self.obj833.OperCostFix.setValue(0.0)

      self.obj833.GGLabel.setValue(3)
      self.obj833.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(120.0,160.0,self.obj833)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj833.graphObject_ = new_obj
      self.obj8330= AttrCalc()
      self.obj8330.Copy=ATOM3Boolean()
      self.obj8330.Copy.setValue(('Copy from LHS', 1))
      self.obj8330.Copy.config = 0
      self.obj8330.Specify=ATOM3Constraint()
      self.obj8330.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj833.GGset2Any['OperCostProp']= self.obj8330
      self.obj8331= AttrCalc()
      self.obj8331.Copy=ATOM3Boolean()
      self.obj8331.Copy.setValue(('Copy from LHS', 1))
      self.obj8331.Copy.config = 0
      self.obj8331.Specify=ATOM3Constraint()
      self.obj8331.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj833.GGset2Any['name']= self.obj8331
      self.obj8332= AttrCalc()
      self.obj8332.Copy=ATOM3Boolean()
      self.obj8332.Copy.setValue(('Copy from LHS', 1))
      self.obj8332.Copy.config = 0
      self.obj8332.Specify=ATOM3Constraint()
      self.obj8332.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj833.GGset2Any['OperCostFix']= self.obj8332

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj833)
      self.obj833.postAction( self.RHS.CREATE )

      self.obj834=fromRaw(parent)
      self.obj834.preAction( self.RHS.CREATE )
      self.obj834.isGraphObjectVisual = True

      if(hasattr(self.obj834, '_setHierarchicalLink')):
        self.obj834._setHierarchicalLink(False)

      # rate
      self.obj834.rate.setValue(0.0)

      self.obj834.GGLabel.setValue(5)
      self.obj834.graphClass_= graph_fromRaw
      if parent.genGraphics:
         new_obj = graph_fromRaw(177.0,133.5,self.obj834)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj834.graphObject_ = new_obj
      self.obj8340= AttrCalc()
      self.obj8340.Copy=ATOM3Boolean()
      self.obj8340.Copy.setValue(('Copy from LHS', 1))
      self.obj8340.Copy.config = 0
      self.obj8340.Specify=ATOM3Constraint()
      self.obj8340.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj834.GGset2Any['rate']= self.obj8340

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj834)
      self.obj834.postAction( self.RHS.CREATE )

      self.obj832.out_connections_.append(self.obj834)
      self.obj834.in_connections_.append(self.obj832)
      self.obj832.graphObject_.pendingConnections.append((self.obj832.graphObject_.tag, self.obj834.graphObject_.tag, [184.0, 96.0, 177.0, 133.5], 0, True))
      self.obj834.out_connections_.append(self.obj833)
      self.obj833.in_connections_.append(self.obj834)
      self.obj834.graphObject_.pendingConnections.append((self.obj834.graphObject_.tag, self.obj833.graphObject_.tag, [170.0, 171.0, 177.0, 133.5], 0, True))

   def condition(self, graphID, isograph, atom3i):
      return self.graphRewritingSystem.finalStat > 20 
      

   def action(self, graphID, isograph, atom3i):
      pass

