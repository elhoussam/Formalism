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

      self.obj376=metarial(parent)
      self.obj376.preAction( self.LHS.CREATE )
      self.obj376.isGraphObjectVisual = True

      if(hasattr(self.obj376, '_setHierarchicalLink')):
        self.obj376._setHierarchicalLink(False)

      # MaxFlow
      self.obj376.MaxFlow.setNone()

      # price
      self.obj376.price.setValue(0)

      # Name
      self.obj376.Name.setValue('')
      self.obj376.Name.setNone()

      # ReqFlow
      self.obj376.ReqFlow.setNone()

      self.obj376.GGLabel.setValue(2)
      self.obj376.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(280.0,40.0,self.obj376)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj376.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj376)
      self.obj376.postAction( self.LHS.CREATE )

      self.obj377=operatingUnit(parent)
      self.obj377.preAction( self.LHS.CREATE )
      self.obj377.isGraphObjectVisual = True

      if(hasattr(self.obj377, '_setHierarchicalLink')):
        self.obj377._setHierarchicalLink(False)

      # OperCostProp
      self.obj377.OperCostProp.setNone()

      # name
      self.obj377.name.setValue('')
      self.obj377.name.setNone()

      # OperCostFix
      self.obj377.OperCostFix.setNone()

      self.obj377.GGLabel.setValue(3)
      self.obj377.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(300.0,140.0,self.obj377)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj377.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj377)
      self.obj377.postAction( self.LHS.CREATE )

      self.obj378=fromMaterial(parent)
      self.obj378.preAction( self.LHS.CREATE )
      self.obj378.isGraphObjectVisual = True

      if(hasattr(self.obj378, '_setHierarchicalLink')):
        self.obj378._setHierarchicalLink(False)

      # rate
      self.obj378.rate.setNone()

      self.obj378.GGLabel.setValue(4)
      self.obj378.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(342.75,113.75,self.obj378)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj378.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj378)
      self.obj378.postAction( self.LHS.CREATE )

      self.obj379=Role(parent)
      self.obj379.preAction( self.LHS.CREATE )
      self.obj379.isGraphObjectVisual = True

      if(hasattr(self.obj379, '_setHierarchicalLink')):
        self.obj379._setHierarchicalLink(False)

      # name
      self.obj379.name.setValue('')
      self.obj379.name.setNone()

      self.obj379.GGLabel.setValue(1)
      self.obj379.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(80.0,60.0,self.obj379)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj379.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj379)
      self.obj379.postAction( self.LHS.CREATE )

      self.obj380=GenericGraphEdge(parent)
      self.obj380.preAction( self.LHS.CREATE )
      self.obj380.isGraphObjectVisual = True

      if(hasattr(self.obj380, '_setHierarchicalLink')):
        self.obj380._setHierarchicalLink(False)

      self.obj380.GGLabel.setValue(5)
      self.obj380.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(195.0,71.5,self.obj380)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj380.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj380)
      self.obj380.postAction( self.LHS.CREATE )

      self.obj376.out_connections_.append(self.obj378)
      self.obj378.in_connections_.append(self.obj376)
      self.obj376.graphObject_.pendingConnections.append((self.obj376.graphObject_.tag, self.obj378.graphObject_.tag, [321.0, 82.0, 335.5, 96.5, 342.75, 113.75], 2, True))
      self.obj378.out_connections_.append(self.obj377)
      self.obj377.in_connections_.append(self.obj378)
      self.obj378.graphObject_.pendingConnections.append((self.obj378.graphObject_.tag, self.obj377.graphObject_.tag, [350.0, 151.0, 350.0, 131.0, 342.75, 113.75], 2, True))
      self.obj379.out_connections_.append(self.obj380)
      self.obj380.in_connections_.append(self.obj379)
      self.obj379.graphObject_.pendingConnections.append((self.obj379.graphObject_.tag, self.obj380.graphObject_.tag, [104.0, 61.0, 195.0, 71.5], 0, True))
      self.obj380.out_connections_.append(self.obj376)
      self.obj376.in_connections_.append(self.obj380)
      self.obj380.graphObject_.pendingConnections.append((self.obj380.graphObject_.tag, self.obj376.graphObject_.tag, [286.0, 82.0, 195.0, 71.5], 0, True))

      self.RHS = ASG_pns(parent)

      self.obj382=metarial(parent)
      self.obj382.preAction( self.RHS.CREATE )
      self.obj382.isGraphObjectVisual = True

      if(hasattr(self.obj382, '_setHierarchicalLink')):
        self.obj382._setHierarchicalLink(False)

      # MaxFlow
      self.obj382.MaxFlow.setValue(999999)

      # price
      self.obj382.price.setValue(0)

      # Name
      self.obj382.Name.setValue('')
      self.obj382.Name.setNone()

      # ReqFlow
      self.obj382.ReqFlow.setValue(0)

      self.obj382.GGLabel.setValue(2)
      self.obj382.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(160.0,40.0,self.obj382)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj382.graphObject_ = new_obj
      self.obj3820= AttrCalc()
      self.obj3820.Copy=ATOM3Boolean()
      self.obj3820.Copy.setValue(('Copy from LHS', 1))
      self.obj3820.Copy.config = 0
      self.obj3820.Specify=ATOM3Constraint()
      self.obj3820.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj382.GGset2Any['MaxFlow']= self.obj3820
      self.obj3821= AttrCalc()
      self.obj3821.Copy=ATOM3Boolean()
      self.obj3821.Copy.setValue(('Copy from LHS', 1))
      self.obj3821.Copy.config = 0
      self.obj3821.Specify=ATOM3Constraint()
      self.obj3821.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj382.GGset2Any['Name']= self.obj3821
      self.obj3822= AttrCalc()
      self.obj3822.Copy=ATOM3Boolean()
      self.obj3822.Copy.setValue(('Copy from LHS', 1))
      self.obj3822.Copy.config = 0
      self.obj3822.Specify=ATOM3Constraint()
      self.obj3822.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj382.GGset2Any['ReqFlow']= self.obj3822

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj382)
      self.obj382.postAction( self.RHS.CREATE )

      self.obj383=operatingUnit(parent)
      self.obj383.preAction( self.RHS.CREATE )
      self.obj383.isGraphObjectVisual = True

      if(hasattr(self.obj383, '_setHierarchicalLink')):
        self.obj383._setHierarchicalLink(False)

      # OperCostProp
      self.obj383.OperCostProp.setValue(0.0)

      # name
      self.obj383.name.setValue('')
      self.obj383.name.setNone()

      # OperCostFix
      self.obj383.OperCostFix.setValue(0.0)

      self.obj383.GGLabel.setValue(3)
      self.obj383.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(200.0,140.0,self.obj383)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj383.graphObject_ = new_obj
      self.obj3830= AttrCalc()
      self.obj3830.Copy=ATOM3Boolean()
      self.obj3830.Copy.setValue(('Copy from LHS', 1))
      self.obj3830.Copy.config = 0
      self.obj3830.Specify=ATOM3Constraint()
      self.obj3830.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj383.GGset2Any['OperCostProp']= self.obj3830
      self.obj3831= AttrCalc()
      self.obj3831.Copy=ATOM3Boolean()
      self.obj3831.Copy.setValue(('Copy from LHS', 1))
      self.obj3831.Copy.config = 0
      self.obj3831.Specify=ATOM3Constraint()
      self.obj3831.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj383.GGset2Any['name']= self.obj3831
      self.obj3832= AttrCalc()
      self.obj3832.Copy=ATOM3Boolean()
      self.obj3832.Copy.setValue(('Copy from LHS', 1))
      self.obj3832.Copy.config = 0
      self.obj3832.Specify=ATOM3Constraint()
      self.obj3832.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj383.GGset2Any['OperCostFix']= self.obj3832

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj383)
      self.obj383.postAction( self.RHS.CREATE )

      self.obj384=fromMaterial(parent)
      self.obj384.preAction( self.RHS.CREATE )
      self.obj384.isGraphObjectVisual = True

      if(hasattr(self.obj384, '_setHierarchicalLink')):
        self.obj384._setHierarchicalLink(False)

      # rate
      self.obj384.rate.setValue(0.0)

      self.obj384.GGLabel.setValue(4)
      self.obj384.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(238.75,106.25,self.obj384)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj384.graphObject_ = new_obj
      self.obj3840= AttrCalc()
      self.obj3840.Copy=ATOM3Boolean()
      self.obj3840.Copy.setValue(('Copy from LHS', 1))
      self.obj3840.Copy.config = 0
      self.obj3840.Specify=ATOM3Constraint()
      self.obj3840.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj384.GGset2Any['rate']= self.obj3840

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj384)
      self.obj384.postAction( self.RHS.CREATE )

      self.obj382.out_connections_.append(self.obj384)
      self.obj384.in_connections_.append(self.obj382)
      self.obj382.graphObject_.pendingConnections.append((self.obj382.graphObject_.tag, self.obj384.graphObject_.tag, [201.0, 82.0, 226.5, 89.0, 238.75, 106.25], 2, True))
      self.obj384.out_connections_.append(self.obj383)
      self.obj383.in_connections_.append(self.obj384)
      self.obj384.graphObject_.pendingConnections.append((self.obj384.graphObject_.tag, self.obj383.graphObject_.tag, [250.0, 151.0, 251.0, 123.5, 238.75, 106.25], 2, True))

   def condition(self, graphID, isograph, atom3i):
      return self.graphRewritingSystem.finalStat > 20 
      

   def action(self, graphID, isograph, atom3i):
      pass

