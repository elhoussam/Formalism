# _ RemoveRole_GG_rule.py ____________________________________________________________________________
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
class RemoveRole_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 28)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_pns(parent)
      self.LHS.merge(ASG_omacs(parent))
      self.LHS.merge(ASG_GenericGraph(parent))

      self.obj848=metarial(parent)
      self.obj848.preAction( self.LHS.CREATE )
      self.obj848.isGraphObjectVisual = True

      if(hasattr(self.obj848, '_setHierarchicalLink')):
        self.obj848._setHierarchicalLink(False)

      # MaxFlow
      self.obj848.MaxFlow.setNone()

      # price
      self.obj848.price.setValue(0)

      # Name
      self.obj848.Name.setValue('')
      self.obj848.Name.setNone()

      # ReqFlow
      self.obj848.ReqFlow.setNone()

      self.obj848.GGLabel.setValue(2)
      self.obj848.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(280.0,40.0,self.obj848)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj848.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj848)
      self.obj848.postAction( self.LHS.CREATE )

      self.obj849=operatingUnit(parent)
      self.obj849.preAction( self.LHS.CREATE )
      self.obj849.isGraphObjectVisual = True

      if(hasattr(self.obj849, '_setHierarchicalLink')):
        self.obj849._setHierarchicalLink(False)

      # OperCostProp
      self.obj849.OperCostProp.setNone()

      # name
      self.obj849.name.setValue('')
      self.obj849.name.setNone()

      # OperCostFix
      self.obj849.OperCostFix.setNone()

      self.obj849.GGLabel.setValue(3)
      self.obj849.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(300.0,140.0,self.obj849)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj849.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj849)
      self.obj849.postAction( self.LHS.CREATE )

      self.obj850=fromMaterial(parent)
      self.obj850.preAction( self.LHS.CREATE )
      self.obj850.isGraphObjectVisual = True

      if(hasattr(self.obj850, '_setHierarchicalLink')):
        self.obj850._setHierarchicalLink(False)

      # rate
      self.obj850.rate.setNone()

      self.obj850.GGLabel.setValue(4)
      self.obj850.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(342.75,113.75,self.obj850)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj850.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj850)
      self.obj850.postAction( self.LHS.CREATE )

      self.obj851=Role(parent)
      self.obj851.preAction( self.LHS.CREATE )
      self.obj851.isGraphObjectVisual = True

      if(hasattr(self.obj851, '_setHierarchicalLink')):
        self.obj851._setHierarchicalLink(False)

      # name
      self.obj851.name.setValue('')
      self.obj851.name.setNone()

      self.obj851.GGLabel.setValue(1)
      self.obj851.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(80.0,60.0,self.obj851)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj851.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj851)
      self.obj851.postAction( self.LHS.CREATE )

      self.obj852=GenericGraphEdge(parent)
      self.obj852.preAction( self.LHS.CREATE )
      self.obj852.isGraphObjectVisual = True

      if(hasattr(self.obj852, '_setHierarchicalLink')):
        self.obj852._setHierarchicalLink(False)

      self.obj852.GGLabel.setValue(5)
      self.obj852.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(195.0,71.5,self.obj852)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj852.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj852)
      self.obj852.postAction( self.LHS.CREATE )

      self.obj848.out_connections_.append(self.obj850)
      self.obj850.in_connections_.append(self.obj848)
      self.obj848.graphObject_.pendingConnections.append((self.obj848.graphObject_.tag, self.obj850.graphObject_.tag, [321.0, 82.0, 335.5, 96.5, 342.75, 113.75], 2, True))
      self.obj850.out_connections_.append(self.obj849)
      self.obj849.in_connections_.append(self.obj850)
      self.obj850.graphObject_.pendingConnections.append((self.obj850.graphObject_.tag, self.obj849.graphObject_.tag, [350.0, 151.0, 350.0, 131.0, 342.75, 113.75], 2, True))
      self.obj851.out_connections_.append(self.obj852)
      self.obj852.in_connections_.append(self.obj851)
      self.obj851.graphObject_.pendingConnections.append((self.obj851.graphObject_.tag, self.obj852.graphObject_.tag, [104.0, 61.0, 195.0, 71.5], 0, True))
      self.obj852.out_connections_.append(self.obj848)
      self.obj848.in_connections_.append(self.obj852)
      self.obj852.graphObject_.pendingConnections.append((self.obj852.graphObject_.tag, self.obj848.graphObject_.tag, [286.0, 82.0, 195.0, 71.5], 0, True))

      self.RHS = ASG_pns(parent)

      self.obj854=metarial(parent)
      self.obj854.preAction( self.RHS.CREATE )
      self.obj854.isGraphObjectVisual = True

      if(hasattr(self.obj854, '_setHierarchicalLink')):
        self.obj854._setHierarchicalLink(False)

      # MaxFlow
      self.obj854.MaxFlow.setValue(999999)

      # price
      self.obj854.price.setValue(0)

      # Name
      self.obj854.Name.setValue('')
      self.obj854.Name.setNone()

      # ReqFlow
      self.obj854.ReqFlow.setValue(0)

      self.obj854.GGLabel.setValue(2)
      self.obj854.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(160.0,40.0,self.obj854)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj854.graphObject_ = new_obj
      self.obj8540= AttrCalc()
      self.obj8540.Copy=ATOM3Boolean()
      self.obj8540.Copy.setValue(('Copy from LHS', 1))
      self.obj8540.Copy.config = 0
      self.obj8540.Specify=ATOM3Constraint()
      self.obj8540.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj854.GGset2Any['MaxFlow']= self.obj8540
      self.obj8541= AttrCalc()
      self.obj8541.Copy=ATOM3Boolean()
      self.obj8541.Copy.setValue(('Copy from LHS', 1))
      self.obj8541.Copy.config = 0
      self.obj8541.Specify=ATOM3Constraint()
      self.obj8541.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj854.GGset2Any['Name']= self.obj8541
      self.obj8542= AttrCalc()
      self.obj8542.Copy=ATOM3Boolean()
      self.obj8542.Copy.setValue(('Copy from LHS', 1))
      self.obj8542.Copy.config = 0
      self.obj8542.Specify=ATOM3Constraint()
      self.obj8542.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj854.GGset2Any['ReqFlow']= self.obj8542

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj854)
      self.obj854.postAction( self.RHS.CREATE )

      self.obj855=operatingUnit(parent)
      self.obj855.preAction( self.RHS.CREATE )
      self.obj855.isGraphObjectVisual = True

      if(hasattr(self.obj855, '_setHierarchicalLink')):
        self.obj855._setHierarchicalLink(False)

      # OperCostProp
      self.obj855.OperCostProp.setValue(0.0)

      # name
      self.obj855.name.setValue('')
      self.obj855.name.setNone()

      # OperCostFix
      self.obj855.OperCostFix.setValue(0.0)

      self.obj855.GGLabel.setValue(3)
      self.obj855.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(200.0,140.0,self.obj855)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj855.graphObject_ = new_obj
      self.obj8550= AttrCalc()
      self.obj8550.Copy=ATOM3Boolean()
      self.obj8550.Copy.setValue(('Copy from LHS', 1))
      self.obj8550.Copy.config = 0
      self.obj8550.Specify=ATOM3Constraint()
      self.obj8550.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj855.GGset2Any['OperCostProp']= self.obj8550
      self.obj8551= AttrCalc()
      self.obj8551.Copy=ATOM3Boolean()
      self.obj8551.Copy.setValue(('Copy from LHS', 1))
      self.obj8551.Copy.config = 0
      self.obj8551.Specify=ATOM3Constraint()
      self.obj8551.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj855.GGset2Any['name']= self.obj8551
      self.obj8552= AttrCalc()
      self.obj8552.Copy=ATOM3Boolean()
      self.obj8552.Copy.setValue(('Copy from LHS', 1))
      self.obj8552.Copy.config = 0
      self.obj8552.Specify=ATOM3Constraint()
      self.obj8552.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj855.GGset2Any['OperCostFix']= self.obj8552

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj855)
      self.obj855.postAction( self.RHS.CREATE )

      self.obj856=fromMaterial(parent)
      self.obj856.preAction( self.RHS.CREATE )
      self.obj856.isGraphObjectVisual = True

      if(hasattr(self.obj856, '_setHierarchicalLink')):
        self.obj856._setHierarchicalLink(False)

      # rate
      self.obj856.rate.setValue(0.0)

      self.obj856.GGLabel.setValue(4)
      self.obj856.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(238.75,106.25,self.obj856)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj856.graphObject_ = new_obj
      self.obj8560= AttrCalc()
      self.obj8560.Copy=ATOM3Boolean()
      self.obj8560.Copy.setValue(('Copy from LHS', 1))
      self.obj8560.Copy.config = 0
      self.obj8560.Specify=ATOM3Constraint()
      self.obj8560.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj856.GGset2Any['rate']= self.obj8560

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj856)
      self.obj856.postAction( self.RHS.CREATE )

      self.obj854.out_connections_.append(self.obj856)
      self.obj856.in_connections_.append(self.obj854)
      self.obj854.graphObject_.pendingConnections.append((self.obj854.graphObject_.tag, self.obj856.graphObject_.tag, [201.0, 82.0, 226.5, 89.0, 238.75, 106.25], 2, True))
      self.obj856.out_connections_.append(self.obj855)
      self.obj855.in_connections_.append(self.obj856)
      self.obj856.graphObject_.pendingConnections.append((self.obj856.graphObject_.tag, self.obj855.graphObject_.tag, [250.0, 151.0, 251.0, 123.5, 238.75, 106.25], 2, True))

   def condition(self, graphID, isograph, atom3i):
      return self.graphRewritingSystem.finalStat > 20 
      

   def action(self, graphID, isograph, atom3i):
      pass

