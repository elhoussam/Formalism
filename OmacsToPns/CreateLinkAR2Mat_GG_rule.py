# _ CreateLinkAR2Mat_GG_rule.py ____________________________________________________________________________
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
class CreateLinkAR2Mat_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 21)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_pns(parent)
      self.LHS.merge(ASG_omacs(parent))
      self.LHS.merge(ASG_GenericGraph(parent))

      self.obj274=rawMaterial(parent)
      self.obj274.preAction( self.LHS.CREATE )
      self.obj274.isGraphObjectVisual = True

      if(hasattr(self.obj274, '_setHierarchicalLink')):
        self.obj274._setHierarchicalLink(False)

      # MaxFlow
      self.obj274.MaxFlow.setNone()

      # price
      self.obj274.price.setValue(0)

      # Name
      self.obj274.Name.setValue('')
      self.obj274.Name.setNone()

      # ReqFlow
      self.obj274.ReqFlow.setNone()

      self.obj274.GGLabel.setValue(6)
      self.obj274.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(240.0,0.0,self.obj274)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj274.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj274)
      self.obj274.postAction( self.LHS.CREATE )

      self.obj275=metarial(parent)
      self.obj275.preAction( self.LHS.CREATE )
      self.obj275.isGraphObjectVisual = True

      if(hasattr(self.obj275, '_setHierarchicalLink')):
        self.obj275._setHierarchicalLink(False)

      # MaxFlow
      self.obj275.MaxFlow.setNone()

      # price
      self.obj275.price.setValue(0)

      # Name
      self.obj275.Name.setValue('')
      self.obj275.Name.setNone()

      # ReqFlow
      self.obj275.ReqFlow.setNone()

      self.obj275.GGLabel.setValue(11)
      self.obj275.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(260.0,200.0,self.obj275)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj275.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj275)
      self.obj275.postAction( self.LHS.CREATE )

      self.obj276=operatingUnit(parent)
      self.obj276.preAction( self.LHS.CREATE )
      self.obj276.isGraphObjectVisual = True

      if(hasattr(self.obj276, '_setHierarchicalLink')):
        self.obj276._setHierarchicalLink(False)

      # OperCostProp
      self.obj276.OperCostProp.setNone()

      # name
      self.obj276.name.setValue('')
      self.obj276.name.setNone()

      # OperCostFix
      self.obj276.OperCostFix.setNone()

      self.obj276.GGLabel.setValue(7)
      self.obj276.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(280.0,100.0,self.obj276)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj276.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj276)
      self.obj276.postAction( self.LHS.CREATE )

      self.obj277=operatingUnit(parent)
      self.obj277.preAction( self.LHS.CREATE )
      self.obj277.isGraphObjectVisual = True

      if(hasattr(self.obj277, '_setHierarchicalLink')):
        self.obj277._setHierarchicalLink(False)

      # OperCostProp
      self.obj277.OperCostProp.setNone()

      # name
      self.obj277.name.setValue('')
      self.obj277.name.setNone()

      # OperCostFix
      self.obj277.OperCostFix.setNone()

      self.obj277.GGLabel.setValue(12)
      self.obj277.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(360.0,260.0,self.obj277)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj277.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj277)
      self.obj277.postAction( self.LHS.CREATE )

      self.obj278=fromRaw(parent)
      self.obj278.preAction( self.LHS.CREATE )
      self.obj278.isGraphObjectVisual = True

      if(hasattr(self.obj278, '_setHierarchicalLink')):
        self.obj278._setHierarchicalLink(False)

      # rate
      self.obj278.rate.setNone()

      self.obj278.GGLabel.setValue(8)
      self.obj278.graphClass_= graph_fromRaw
      if parent.genGraphics:
         new_obj = graph_fromRaw(311.5,63.25,self.obj278)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj278.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj278)
      self.obj278.postAction( self.LHS.CREATE )

      self.obj279=fromMaterial(parent)
      self.obj279.preAction( self.LHS.CREATE )
      self.obj279.isGraphObjectVisual = True

      if(hasattr(self.obj279, '_setHierarchicalLink')):
        self.obj279._setHierarchicalLink(False)

      # rate
      self.obj279.rate.setNone()

      self.obj279.GGLabel.setValue(14)
      self.obj279.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(379.5,235.25,self.obj279)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj279.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj279)
      self.obj279.postAction( self.LHS.CREATE )

      self.obj280=CapableOf(parent)
      self.obj280.preAction( self.LHS.CREATE )
      self.obj280.isGraphObjectVisual = True

      if(hasattr(self.obj280, '_setHierarchicalLink')):
        self.obj280._setHierarchicalLink(False)

      # rate
      self.obj280.rate.setNone()

      self.obj280.GGLabel.setValue(3)
      self.obj280.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(84.5,131.5,self.obj280)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj280.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj280)
      self.obj280.postAction( self.LHS.CREATE )

      self.obj281=Agent(parent)
      self.obj281.preAction( self.LHS.CREATE )
      self.obj281.isGraphObjectVisual = True

      if(hasattr(self.obj281, '_setHierarchicalLink')):
        self.obj281._setHierarchicalLink(False)

      # price
      self.obj281.price.setNone()

      # name
      self.obj281.name.setValue('')
      self.obj281.name.setNone()

      self.obj281.GGLabel.setValue(1)
      self.obj281.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(60.0,20.0,self.obj281)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj281.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj281)
      self.obj281.postAction( self.LHS.CREATE )

      self.obj282=Role(parent)
      self.obj282.preAction( self.LHS.CREATE )
      self.obj282.isGraphObjectVisual = True

      if(hasattr(self.obj282, '_setHierarchicalLink')):
        self.obj282._setHierarchicalLink(False)

      # name
      self.obj282.name.setValue('')
      self.obj282.name.setNone()

      self.obj282.GGLabel.setValue(2)
      self.obj282.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(60.0,180.0,self.obj282)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj282.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj282)
      self.obj282.postAction( self.LHS.CREATE )

      self.obj283=GenericGraphEdge(parent)
      self.obj283.preAction( self.LHS.CREATE )
      self.obj283.isGraphObjectVisual = True

      if(hasattr(self.obj283, '_setHierarchicalLink')):
        self.obj283._setHierarchicalLink(False)

      self.obj283.GGLabel.setValue(15)
      self.obj283.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(174.5,69.0,self.obj283)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj283.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj283)
      self.obj283.postAction( self.LHS.CREATE )

      self.obj284=GenericGraphEdge(parent)
      self.obj284.preAction( self.LHS.CREATE )
      self.obj284.isGraphObjectVisual = True

      if(hasattr(self.obj284, '_setHierarchicalLink')):
        self.obj284._setHierarchicalLink(False)

      self.obj284.GGLabel.setValue(10)
      self.obj284.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(245.75,97.25,self.obj284)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj284.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj284)
      self.obj284.postAction( self.LHS.CREATE )

      self.obj285=GenericGraphEdge(parent)
      self.obj285.preAction( self.LHS.CREATE )
      self.obj285.isGraphObjectVisual = True

      if(hasattr(self.obj285, '_setHierarchicalLink')):
        self.obj285._setHierarchicalLink(False)

      self.obj285.GGLabel.setValue(13)
      self.obj285.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(175.0,234.0,self.obj285)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj285.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj285)
      self.obj285.postAction( self.LHS.CREATE )

      self.obj274.out_connections_.append(self.obj278)
      self.obj278.in_connections_.append(self.obj274)
      self.obj274.graphObject_.pendingConnections.append((self.obj274.graphObject_.tag, self.obj278.graphObject_.tag, [264.0, 56.0, 295.0, 49.5, 311.5, 63.25], 2, True))
      self.obj275.out_connections_.append(self.obj279)
      self.obj279.in_connections_.append(self.obj275)
      self.obj275.graphObject_.pendingConnections.append((self.obj275.graphObject_.tag, self.obj279.graphObject_.tag, [306.0, 210.0, 353.5, 220.0, 379.5, 235.25], 2, True))
      self.obj278.out_connections_.append(self.obj276)
      self.obj276.in_connections_.append(self.obj278)
      self.obj278.graphObject_.pendingConnections.append((self.obj278.graphObject_.tag, self.obj276.graphObject_.tag, [330.0, 111.0, 328.0, 77.0, 311.5, 63.25], 2, True))
      self.obj279.out_connections_.append(self.obj277)
      self.obj277.in_connections_.append(self.obj279)
      self.obj279.graphObject_.pendingConnections.append((self.obj279.graphObject_.tag, self.obj277.graphObject_.tag, [410.0, 271.0, 405.5, 250.5, 379.5, 235.25], 2, True))
      self.obj280.out_connections_.append(self.obj282)
      self.obj282.in_connections_.append(self.obj280)
      self.obj280.graphObject_.pendingConnections.append((self.obj280.graphObject_.tag, self.obj282.graphObject_.tag, [84.0, 181.0, 84.5, 131.5], 0, True))
      self.obj281.out_connections_.append(self.obj280)
      self.obj280.in_connections_.append(self.obj281)
      self.obj281.graphObject_.pendingConnections.append((self.obj281.graphObject_.tag, self.obj280.graphObject_.tag, [85.0, 82.0, 84.5, 131.5], 0, True))
      self.obj281.out_connections_.append(self.obj283)
      self.obj283.in_connections_.append(self.obj281)
      self.obj281.graphObject_.pendingConnections.append((self.obj281.graphObject_.tag, self.obj283.graphObject_.tag, [85.0, 82.0, 174.5, 69.0], 0, True))
      self.obj281.out_connections_.append(self.obj284)
      self.obj284.in_connections_.append(self.obj281)
      self.obj281.graphObject_.pendingConnections.append((self.obj281.graphObject_.tag, self.obj284.graphObject_.tag, [85.0, 82.0, 192.0, 90.0, 245.75, 97.25], 2, True))
      self.obj282.out_connections_.append(self.obj285)
      self.obj285.in_connections_.append(self.obj282)
      self.obj282.graphObject_.pendingConnections.append((self.obj282.graphObject_.tag, self.obj285.graphObject_.tag, [84.0, 226.0, 175.0, 234.0], 0, True))
      self.obj283.out_connections_.append(self.obj274)
      self.obj274.in_connections_.append(self.obj283)
      self.obj283.graphObject_.pendingConnections.append((self.obj283.graphObject_.tag, self.obj274.graphObject_.tag, [264.0, 56.0, 174.5, 69.0], 0, True))
      self.obj284.out_connections_.append(self.obj276)
      self.obj276.in_connections_.append(self.obj284)
      self.obj284.graphObject_.pendingConnections.append((self.obj284.graphObject_.tag, self.obj276.graphObject_.tag, [300.0, 111.0, 299.5, 104.5, 245.75, 97.25], 2, True))
      self.obj285.out_connections_.append(self.obj275)
      self.obj275.in_connections_.append(self.obj285)
      self.obj285.graphObject_.pendingConnections.append((self.obj285.graphObject_.tag, self.obj275.graphObject_.tag, [266.0, 242.0, 175.0, 234.0], 0, True))

      self.RHS = ASG_pns(parent)
      self.RHS.merge(ASG_omacs(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj289=rawMaterial(parent)
      self.obj289.preAction( self.RHS.CREATE )
      self.obj289.isGraphObjectVisual = True

      if(hasattr(self.obj289, '_setHierarchicalLink')):
        self.obj289._setHierarchicalLink(False)

      # MaxFlow
      self.obj289.MaxFlow.setNone()

      # price
      self.obj289.price.setValue(0)

      # Name
      self.obj289.Name.setValue('')
      self.obj289.Name.setNone()

      # ReqFlow
      self.obj289.ReqFlow.setNone()

      self.obj289.GGLabel.setValue(6)
      self.obj289.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(240.0,0.0,self.obj289)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj289.graphObject_ = new_obj
      self.obj2890= AttrCalc()
      self.obj2890.Copy=ATOM3Boolean()
      self.obj2890.Copy.setValue(('Copy from LHS', 1))
      self.obj2890.Copy.config = 0
      self.obj2890.Specify=ATOM3Constraint()
      self.obj2890.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj289.GGset2Any['MaxFlow']= self.obj2890
      self.obj2891= AttrCalc()
      self.obj2891.Copy=ATOM3Boolean()
      self.obj2891.Copy.setValue(('Copy from LHS', 1))
      self.obj2891.Copy.config = 0
      self.obj2891.Specify=ATOM3Constraint()
      self.obj2891.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj289.GGset2Any['Name']= self.obj2891
      self.obj2892= AttrCalc()
      self.obj2892.Copy=ATOM3Boolean()
      self.obj2892.Copy.setValue(('Copy from LHS', 1))
      self.obj2892.Copy.config = 0
      self.obj2892.Specify=ATOM3Constraint()
      self.obj2892.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj289.GGset2Any['ReqFlow']= self.obj2892

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj289)
      self.obj289.postAction( self.RHS.CREATE )

      self.obj290=metarial(parent)
      self.obj290.preAction( self.RHS.CREATE )
      self.obj290.isGraphObjectVisual = True

      if(hasattr(self.obj290, '_setHierarchicalLink')):
        self.obj290._setHierarchicalLink(False)

      # MaxFlow
      self.obj290.MaxFlow.setNone()

      # price
      self.obj290.price.setValue(0)

      # Name
      self.obj290.Name.setValue('')
      self.obj290.Name.setNone()

      # ReqFlow
      self.obj290.ReqFlow.setNone()

      self.obj290.GGLabel.setValue(11)
      self.obj290.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(260.0,200.0,self.obj290)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj290.graphObject_ = new_obj
      self.obj2900= AttrCalc()
      self.obj2900.Copy=ATOM3Boolean()
      self.obj2900.Copy.setValue(('Copy from LHS', 1))
      self.obj2900.Copy.config = 0
      self.obj2900.Specify=ATOM3Constraint()
      self.obj2900.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj290.GGset2Any['MaxFlow']= self.obj2900
      self.obj2901= AttrCalc()
      self.obj2901.Copy=ATOM3Boolean()
      self.obj2901.Copy.setValue(('Copy from LHS', 1))
      self.obj2901.Copy.config = 0
      self.obj2901.Specify=ATOM3Constraint()
      self.obj2901.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj290.GGset2Any['Name']= self.obj2901
      self.obj2902= AttrCalc()
      self.obj2902.Copy=ATOM3Boolean()
      self.obj2902.Copy.setValue(('Copy from LHS', 1))
      self.obj2902.Copy.config = 0
      self.obj2902.Specify=ATOM3Constraint()
      self.obj2902.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj290.GGset2Any['ReqFlow']= self.obj2902

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj290)
      self.obj290.postAction( self.RHS.CREATE )

      self.obj291=operatingUnit(parent)
      self.obj291.preAction( self.RHS.CREATE )
      self.obj291.isGraphObjectVisual = True

      if(hasattr(self.obj291, '_setHierarchicalLink')):
        self.obj291._setHierarchicalLink(False)

      # OperCostProp
      self.obj291.OperCostProp.setNone()

      # name
      self.obj291.name.setValue('')
      self.obj291.name.setNone()

      # OperCostFix
      self.obj291.OperCostFix.setNone()

      self.obj291.GGLabel.setValue(7)
      self.obj291.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(280.0,100.0,self.obj291)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj291.graphObject_ = new_obj
      self.obj2910= AttrCalc()
      self.obj2910.Copy=ATOM3Boolean()
      self.obj2910.Copy.setValue(('Copy from LHS', 1))
      self.obj2910.Copy.config = 0
      self.obj2910.Specify=ATOM3Constraint()
      self.obj2910.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj291.GGset2Any['OperCostProp']= self.obj2910
      self.obj2911= AttrCalc()
      self.obj2911.Copy=ATOM3Boolean()
      self.obj2911.Copy.setValue(('Copy from LHS', 1))
      self.obj2911.Copy.config = 0
      self.obj2911.Specify=ATOM3Constraint()
      self.obj2911.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj291.GGset2Any['name']= self.obj2911
      self.obj2912= AttrCalc()
      self.obj2912.Copy=ATOM3Boolean()
      self.obj2912.Copy.setValue(('Copy from LHS', 1))
      self.obj2912.Copy.config = 0
      self.obj2912.Specify=ATOM3Constraint()
      self.obj2912.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj291.GGset2Any['OperCostFix']= self.obj2912

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj291)
      self.obj291.postAction( self.RHS.CREATE )

      self.obj292=operatingUnit(parent)
      self.obj292.preAction( self.RHS.CREATE )
      self.obj292.isGraphObjectVisual = True

      if(hasattr(self.obj292, '_setHierarchicalLink')):
        self.obj292._setHierarchicalLink(False)

      # OperCostProp
      self.obj292.OperCostProp.setNone()

      # name
      self.obj292.name.setValue('')
      self.obj292.name.setNone()

      # OperCostFix
      self.obj292.OperCostFix.setNone()

      self.obj292.GGLabel.setValue(12)
      self.obj292.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(360.0,260.0,self.obj292)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj292.graphObject_ = new_obj
      self.obj2920= AttrCalc()
      self.obj2920.Copy=ATOM3Boolean()
      self.obj2920.Copy.setValue(('Copy from LHS', 1))
      self.obj2920.Copy.config = 0
      self.obj2920.Specify=ATOM3Constraint()
      self.obj2920.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj292.GGset2Any['OperCostProp']= self.obj2920
      self.obj2921= AttrCalc()
      self.obj2921.Copy=ATOM3Boolean()
      self.obj2921.Copy.setValue(('Copy from LHS', 1))
      self.obj2921.Copy.config = 0
      self.obj2921.Specify=ATOM3Constraint()
      self.obj2921.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj292.GGset2Any['name']= self.obj2921
      self.obj2922= AttrCalc()
      self.obj2922.Copy=ATOM3Boolean()
      self.obj2922.Copy.setValue(('Copy from LHS', 1))
      self.obj2922.Copy.config = 0
      self.obj2922.Specify=ATOM3Constraint()
      self.obj2922.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj292.GGset2Any['OperCostFix']= self.obj2922

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj292)
      self.obj292.postAction( self.RHS.CREATE )

      self.obj293=fromRaw(parent)
      self.obj293.preAction( self.RHS.CREATE )
      self.obj293.isGraphObjectVisual = True

      if(hasattr(self.obj293, '_setHierarchicalLink')):
        self.obj293._setHierarchicalLink(False)

      # rate
      self.obj293.rate.setNone()

      self.obj293.GGLabel.setValue(8)
      self.obj293.graphClass_= graph_fromRaw
      if parent.genGraphics:
         new_obj = graph_fromRaw(311.5,63.25,self.obj293)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj293.graphObject_ = new_obj
      self.obj2930= AttrCalc()
      self.obj2930.Copy=ATOM3Boolean()
      self.obj2930.Copy.setValue(('Copy from LHS', 1))
      self.obj2930.Copy.config = 0
      self.obj2930.Specify=ATOM3Constraint()
      self.obj2930.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj293.GGset2Any['rate']= self.obj2930

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj293)
      self.obj293.postAction( self.RHS.CREATE )

      self.obj294=intoMaterial(parent)
      self.obj294.preAction( self.RHS.CREATE )
      self.obj294.isGraphObjectVisual = True

      if(hasattr(self.obj294, '_setHierarchicalLink')):
        self.obj294._setHierarchicalLink(False)

      # rate
      self.obj294.rate.setValue(0.0)

      self.obj294.GGLabel.setValue(17)
      self.obj294.graphClass_= graph_intoMaterial
      if parent.genGraphics:
         new_obj = graph_intoMaterial(324.25,167.5,self.obj294)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj294.graphObject_ = new_obj
      self.obj2940= AttrCalc()
      self.obj2940.Copy=ATOM3Boolean()
      self.obj2940.Copy.setValue(('Copy from LHS', 0))
      self.obj2940.Copy.config = 0
      self.obj2940.Specify=ATOM3Constraint()
      self.obj2940.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'a = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) ).name.getValue()\nb = self.getMatched ( graphID , self.LHS.nodeWithLabel(2) ).name.getValue()\nreturn self.graphRewritingSystem.Dictag[ a ][b]\n\n'))
      self.obj294.GGset2Any['rate']= self.obj2940

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj294)
      self.obj294.postAction( self.RHS.CREATE )

      self.obj295=fromMaterial(parent)
      self.obj295.preAction( self.RHS.CREATE )
      self.obj295.isGraphObjectVisual = True

      if(hasattr(self.obj295, '_setHierarchicalLink')):
        self.obj295._setHierarchicalLink(False)

      # rate
      self.obj295.rate.setNone()

      self.obj295.GGLabel.setValue(14)
      self.obj295.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(379.5,235.25,self.obj295)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj295.graphObject_ = new_obj
      self.obj2950= AttrCalc()
      self.obj2950.Copy=ATOM3Boolean()
      self.obj2950.Copy.setValue(('Copy from LHS', 1))
      self.obj2950.Copy.config = 0
      self.obj2950.Specify=ATOM3Constraint()
      self.obj2950.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj295.GGset2Any['rate']= self.obj2950

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj295)
      self.obj295.postAction( self.RHS.CREATE )

      self.obj296=CapableOf(parent)
      self.obj296.preAction( self.RHS.CREATE )
      self.obj296.isGraphObjectVisual = True

      if(hasattr(self.obj296, '_setHierarchicalLink')):
        self.obj296._setHierarchicalLink(False)

      # rate
      self.obj296.rate.setNone()

      self.obj296.GGLabel.setValue(3)
      self.obj296.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(84.5,131.5,self.obj296)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj296.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj296)
      self.obj296.postAction( self.RHS.CREATE )

      self.obj297=Agent(parent)
      self.obj297.preAction( self.RHS.CREATE )
      self.obj297.isGraphObjectVisual = True

      if(hasattr(self.obj297, '_setHierarchicalLink')):
        self.obj297._setHierarchicalLink(False)

      # price
      self.obj297.price.setNone()

      # name
      self.obj297.name.setValue('')
      self.obj297.name.setNone()

      self.obj297.GGLabel.setValue(1)
      self.obj297.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(60.0,20.0,self.obj297)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj297.graphObject_ = new_obj
      self.obj2970= AttrCalc()
      self.obj2970.Copy=ATOM3Boolean()
      self.obj2970.Copy.setValue(('Copy from LHS', 1))
      self.obj2970.Copy.config = 0
      self.obj2970.Specify=ATOM3Constraint()
      self.obj2970.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj297.GGset2Any['price']= self.obj2970
      self.obj2971= AttrCalc()
      self.obj2971.Copy=ATOM3Boolean()
      self.obj2971.Copy.setValue(('Copy from LHS', 1))
      self.obj2971.Copy.config = 0
      self.obj2971.Specify=ATOM3Constraint()
      self.obj2971.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj297.GGset2Any['name']= self.obj2971

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj297)
      self.obj297.postAction( self.RHS.CREATE )

      self.obj298=Role(parent)
      self.obj298.preAction( self.RHS.CREATE )
      self.obj298.isGraphObjectVisual = True

      if(hasattr(self.obj298, '_setHierarchicalLink')):
        self.obj298._setHierarchicalLink(False)

      # name
      self.obj298.name.setValue('')
      self.obj298.name.setNone()

      self.obj298.GGLabel.setValue(2)
      self.obj298.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(60.0,180.0,self.obj298)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj298.graphObject_ = new_obj
      self.obj2980= AttrCalc()
      self.obj2980.Copy=ATOM3Boolean()
      self.obj2980.Copy.setValue(('Copy from LHS', 1))
      self.obj2980.Copy.config = 0
      self.obj2980.Specify=ATOM3Constraint()
      self.obj2980.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj298.GGset2Any['name']= self.obj2980

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj298)
      self.obj298.postAction( self.RHS.CREATE )

      self.obj299=GenericGraphEdge(parent)
      self.obj299.preAction( self.RHS.CREATE )
      self.obj299.isGraphObjectVisual = True

      if(hasattr(self.obj299, '_setHierarchicalLink')):
        self.obj299._setHierarchicalLink(False)

      self.obj299.GGLabel.setValue(15)
      self.obj299.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(174.5,69.0,self.obj299)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj299.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj299)
      self.obj299.postAction( self.RHS.CREATE )

      self.obj300=GenericGraphEdge(parent)
      self.obj300.preAction( self.RHS.CREATE )
      self.obj300.isGraphObjectVisual = True

      if(hasattr(self.obj300, '_setHierarchicalLink')):
        self.obj300._setHierarchicalLink(False)

      self.obj300.GGLabel.setValue(10)
      self.obj300.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(245.75,97.25,self.obj300)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj300.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj300)
      self.obj300.postAction( self.RHS.CREATE )

      self.obj301=GenericGraphEdge(parent)
      self.obj301.preAction( self.RHS.CREATE )
      self.obj301.isGraphObjectVisual = True

      if(hasattr(self.obj301, '_setHierarchicalLink')):
        self.obj301._setHierarchicalLink(False)

      self.obj301.GGLabel.setValue(13)
      self.obj301.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(175.0,234.0,self.obj301)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj301.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj301)
      self.obj301.postAction( self.RHS.CREATE )

      self.obj289.out_connections_.append(self.obj293)
      self.obj293.in_connections_.append(self.obj289)
      self.obj289.graphObject_.pendingConnections.append((self.obj289.graphObject_.tag, self.obj293.graphObject_.tag, [264.0, 50.0, 311.5, 63.25], 2, 0))
      self.obj290.out_connections_.append(self.obj295)
      self.obj295.in_connections_.append(self.obj290)
      self.obj290.graphObject_.pendingConnections.append((self.obj290.graphObject_.tag, self.obj295.graphObject_.tag, [306.0, 210.0, 379.5, 235.25], 2, 0))
      self.obj291.out_connections_.append(self.obj294)
      self.obj294.in_connections_.append(self.obj291)
      self.obj291.graphObject_.pendingConnections.append((self.obj291.graphObject_.tag, self.obj294.graphObject_.tag, [333.0, 108.0, 331.0, 142.0, 324.25, 167.5], 2, True))
      self.obj293.out_connections_.append(self.obj291)
      self.obj291.in_connections_.append(self.obj293)
      self.obj293.graphObject_.pendingConnections.append((self.obj293.graphObject_.tag, self.obj291.graphObject_.tag, [330.0, 101.0, 311.5, 63.25], 2, 0))
      self.obj294.out_connections_.append(self.obj290)
      self.obj290.in_connections_.append(self.obj294)
      self.obj294.graphObject_.pendingConnections.append((self.obj294.graphObject_.tag, self.obj290.graphObject_.tag, [306.0, 210.0, 317.5, 193.0, 324.25, 167.5], 2, True))
      self.obj295.out_connections_.append(self.obj292)
      self.obj292.in_connections_.append(self.obj295)
      self.obj295.graphObject_.pendingConnections.append((self.obj295.graphObject_.tag, self.obj292.graphObject_.tag, [413.0, 268.0, 379.5, 235.25], 2, 0))
      self.obj296.out_connections_.append(self.obj298)
      self.obj298.in_connections_.append(self.obj296)
      self.obj296.graphObject_.pendingConnections.append((self.obj296.graphObject_.tag, self.obj298.graphObject_.tag, [91.0, 180.0, 84.5, 131.5], 2, 0))
      self.obj297.out_connections_.append(self.obj296)
      self.obj296.in_connections_.append(self.obj297)
      self.obj297.graphObject_.pendingConnections.append((self.obj297.graphObject_.tag, self.obj296.graphObject_.tag, [97.0, 82.0, 84.5, 131.5], 2, 0))
      self.obj297.out_connections_.append(self.obj299)
      self.obj299.in_connections_.append(self.obj297)
      self.obj297.graphObject_.pendingConnections.append((self.obj297.graphObject_.tag, self.obj299.graphObject_.tag, [97.0, 82.0, 174.5, 69.0], 2, 0))
      self.obj297.out_connections_.append(self.obj300)
      self.obj300.in_connections_.append(self.obj297)
      self.obj297.graphObject_.pendingConnections.append((self.obj297.graphObject_.tag, self.obj300.graphObject_.tag, [97.0, 82.0, 245.75, 97.25], 2, 0))
      self.obj298.out_connections_.append(self.obj301)
      self.obj301.in_connections_.append(self.obj298)
      self.obj298.graphObject_.pendingConnections.append((self.obj298.graphObject_.tag, self.obj301.graphObject_.tag, [91.0, 225.0, 175.0, 234.0], 2, 0))
      self.obj299.out_connections_.append(self.obj289)
      self.obj289.in_connections_.append(self.obj299)
      self.obj299.graphObject_.pendingConnections.append((self.obj299.graphObject_.tag, self.obj289.graphObject_.tag, [264.0, 50.0, 174.5, 69.0], 2, 0))
      self.obj300.out_connections_.append(self.obj291)
      self.obj291.in_connections_.append(self.obj300)
      self.obj300.graphObject_.pendingConnections.append((self.obj300.graphObject_.tag, self.obj291.graphObject_.tag, [300.0, 101.0, 245.75, 97.25], 2, 0))
      self.obj301.out_connections_.append(self.obj290)
      self.obj290.in_connections_.append(self.obj301)
      self.obj301.graphObject_.pendingConnections.append((self.obj301.graphObject_.tag, self.obj290.graphObject_.tag, [266.0, 242.0, 175.0, 234.0], 2, 0))

   def condition(self, graphID, isograph, atom3i):
      print 'Rule 21 '
      node7 = self.getMatched(graphID, self.LHS.nodeWithLabel(7))
      
      node11 = self.getMatched(graphID, self.LHS.nodeWithLabel(11))
      node1 = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      
      print node7.name.getValue()+' in '+ node11.Name.getValue() 
      print node7.name.getValue() in  node11.Name.getValue()
      
      
      test = not ( hasattr(node11, "linkAux2") and hasattr(node7, "linkAux2") )
      print test
      if test : 
       return (node7.name.getValue() in node11.Name.getValue() )
      else : 
       return False
      
      

   def action(self, graphID, isograph, atom3i):
      # code action of rule
      node = self.getMatched ( graphID , self.LHS.nodeWithLabel(7) )
      node.linkAux2 = True 
      node = self.getMatched ( graphID , self.LHS.nodeWithLabel(11) )
      node.linkAux2 = True 
      self.graphRewritingSystem.finalStat = 21
      
      

