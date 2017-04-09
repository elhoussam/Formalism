# _ CreateLinkMat_ARG2Goal_GG_rule.py ____________________________________________________________________________
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
class CreateLinkMat_ARG2Goal_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 19)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_pns(parent)
      self.LHS.merge(ASG_omacs(parent))
      self.LHS.merge(ASG_GenericGraph(parent))

      self.obj246=metarial(parent)
      self.obj246.preAction( self.LHS.CREATE )
      self.obj246.isGraphObjectVisual = True

      if(hasattr(self.obj246, '_setHierarchicalLink')):
        self.obj246._setHierarchicalLink(False)

      # MaxFlow
      self.obj246.MaxFlow.setNone()

      # price
      self.obj246.price.setValue(0)

      # Name
      self.obj246.Name.setValue('')
      self.obj246.Name.setNone()

      # ReqFlow
      self.obj246.ReqFlow.setNone()

      self.obj246.GGLabel.setValue(4)
      self.obj246.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(240.0,20.0,self.obj246)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj246.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj246)
      self.obj246.postAction( self.LHS.CREATE )

      self.obj247=metarial(parent)
      self.obj247.preAction( self.LHS.CREATE )
      self.obj247.isGraphObjectVisual = True

      if(hasattr(self.obj247, '_setHierarchicalLink')):
        self.obj247._setHierarchicalLink(False)

      # MaxFlow
      self.obj247.MaxFlow.setNone()

      # price
      self.obj247.price.setValue(0)

      # Name
      self.obj247.Name.setValue('')
      self.obj247.Name.setNone()

      # ReqFlow
      self.obj247.ReqFlow.setNone()

      self.obj247.GGLabel.setValue(6)
      self.obj247.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(240.0,240.0,self.obj247)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj247.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj247)
      self.obj247.postAction( self.LHS.CREATE )

      self.obj248=operatingUnit(parent)
      self.obj248.preAction( self.LHS.CREATE )
      self.obj248.isGraphObjectVisual = True

      if(hasattr(self.obj248, '_setHierarchicalLink')):
        self.obj248._setHierarchicalLink(False)

      # OperCostProp
      self.obj248.OperCostProp.setNone()

      # name
      self.obj248.name.setValue('')
      self.obj248.name.setNone()

      # OperCostFix
      self.obj248.OperCostFix.setNone()

      self.obj248.GGLabel.setValue(5)
      self.obj248.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(240.0,140.0,self.obj248)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj248.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj248)
      self.obj248.postAction( self.LHS.CREATE )

      self.obj249=fromMaterial(parent)
      self.obj249.preAction( self.LHS.CREATE )
      self.obj249.isGraphObjectVisual = True

      if(hasattr(self.obj249, '_setHierarchicalLink')):
        self.obj249._setHierarchicalLink(False)

      # rate
      self.obj249.rate.setNone()

      self.obj249.GGLabel.setValue(8)
      self.obj249.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(265.0,100.0,self.obj249)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj249.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj249)
      self.obj249.postAction( self.LHS.CREATE )

      self.obj250=Goal(parent)
      self.obj250.preAction( self.LHS.CREATE )
      self.obj250.isGraphObjectVisual = True

      if(hasattr(self.obj250, '_setHierarchicalLink')):
        self.obj250._setHierarchicalLink(False)

      # name
      self.obj250.name.setValue('')
      self.obj250.name.setNone()

      self.obj250.GGLabel.setValue(2)
      self.obj250.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(60.0,220.0,self.obj250)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj250.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj250)
      self.obj250.postAction( self.LHS.CREATE )

      self.obj251=Role(parent)
      self.obj251.preAction( self.LHS.CREATE )
      self.obj251.isGraphObjectVisual = True

      if(hasattr(self.obj251, '_setHierarchicalLink')):
        self.obj251._setHierarchicalLink(False)

      # name
      self.obj251.name.setValue('')
      self.obj251.name.setNone()

      self.obj251.GGLabel.setValue(1)
      self.obj251.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(60.0,40.0,self.obj251)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj251.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj251)
      self.obj251.postAction( self.LHS.CREATE )

      self.obj252=achieve(parent)
      self.obj252.preAction( self.LHS.CREATE )
      self.obj252.isGraphObjectVisual = True

      if(hasattr(self.obj252, '_setHierarchicalLink')):
        self.obj252._setHierarchicalLink(False)

      # rate
      self.obj252.rate.setNone()

      self.obj252.GGLabel.setValue(3)
      self.obj252.graphClass_= graph_achieve
      if parent.genGraphics:
         new_obj = graph_achieve(97.5,137.5,self.obj252)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj252.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj252)
      self.obj252.postAction( self.LHS.CREATE )

      self.obj253=GenericGraphEdge(parent)
      self.obj253.preAction( self.LHS.CREATE )
      self.obj253.isGraphObjectVisual = True

      if(hasattr(self.obj253, '_setHierarchicalLink')):
        self.obj253._setHierarchicalLink(False)

      self.obj253.GGLabel.setValue(7)
      self.obj253.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(215.0,41.5,self.obj253)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj253.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj253)
      self.obj253.postAction( self.LHS.CREATE )

      self.obj254=GenericGraphEdge(parent)
      self.obj254.preAction( self.LHS.CREATE )
      self.obj254.isGraphObjectVisual = True

      if(hasattr(self.obj254, '_setHierarchicalLink')):
        self.obj254._setHierarchicalLink(False)

      self.obj254.GGLabel.setValue(9)
      self.obj254.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(185.0,276.0,self.obj254)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj254.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj254)
      self.obj254.postAction( self.LHS.CREATE )

      self.obj246.out_connections_.append(self.obj249)
      self.obj249.in_connections_.append(self.obj246)
      self.obj246.graphObject_.pendingConnections.append((self.obj246.graphObject_.tag, self.obj249.graphObject_.tag, [264.0, 69.0, 265.0, 100.0], 0, True))
      self.obj249.out_connections_.append(self.obj248)
      self.obj248.in_connections_.append(self.obj249)
      self.obj249.graphObject_.pendingConnections.append((self.obj249.graphObject_.tag, self.obj248.graphObject_.tag, [260.0, 151.0, 352.0, 90.0], 0, True))
      self.obj250.out_connections_.append(self.obj254)
      self.obj254.in_connections_.append(self.obj250)
      self.obj250.graphObject_.pendingConnections.append((self.obj250.graphObject_.tag, self.obj254.graphObject_.tag, [84.0, 270.0, 185.0, 276.0], 0, True))
      self.obj251.out_connections_.append(self.obj252)
      self.obj252.in_connections_.append(self.obj251)
      self.obj251.graphObject_.pendingConnections.append((self.obj251.graphObject_.tag, self.obj252.graphObject_.tag, [84.0, 86.0, 97.5, 137.5], 0, True))
      self.obj251.out_connections_.append(self.obj253)
      self.obj253.in_connections_.append(self.obj251)
      self.obj251.graphObject_.pendingConnections.append((self.obj251.graphObject_.tag, self.obj253.graphObject_.tag, [84.0, 41.0, 215.0, 41.5], 0, True))
      self.obj252.out_connections_.append(self.obj250)
      self.obj250.in_connections_.append(self.obj252)
      self.obj252.graphObject_.pendingConnections.append((self.obj252.graphObject_.tag, self.obj250.graphObject_.tag, [83.0, 221.0, 93.5, 143.5], 0, True))
      self.obj253.out_connections_.append(self.obj246)
      self.obj246.in_connections_.append(self.obj253)
      self.obj253.graphObject_.pendingConnections.append((self.obj253.graphObject_.tag, self.obj246.graphObject_.tag, [246.0, 62.0, 215.0, 41.5], 0, True))
      self.obj254.out_connections_.append(self.obj247)
      self.obj247.in_connections_.append(self.obj254)
      self.obj254.graphObject_.pendingConnections.append((self.obj254.graphObject_.tag, self.obj247.graphObject_.tag, [246.0, 282.0, 185.0, 276.0], 0, True))

      self.RHS = ASG_pns(parent)
      self.RHS.merge(ASG_omacs(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj258=metarial(parent)
      self.obj258.preAction( self.RHS.CREATE )
      self.obj258.isGraphObjectVisual = True

      if(hasattr(self.obj258, '_setHierarchicalLink')):
        self.obj258._setHierarchicalLink(False)

      # MaxFlow
      self.obj258.MaxFlow.setNone()

      # price
      self.obj258.price.setValue(0)

      # Name
      self.obj258.Name.setValue('')
      self.obj258.Name.setNone()

      # ReqFlow
      self.obj258.ReqFlow.setNone()

      self.obj258.GGLabel.setValue(4)
      self.obj258.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(280.0,20.0,self.obj258)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj258.graphObject_ = new_obj
      self.obj2580= AttrCalc()
      self.obj2580.Copy=ATOM3Boolean()
      self.obj2580.Copy.setValue(('Copy from LHS', 1))
      self.obj2580.Copy.config = 0
      self.obj2580.Specify=ATOM3Constraint()
      self.obj2580.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj258.GGset2Any['MaxFlow']= self.obj2580
      self.obj2581= AttrCalc()
      self.obj2581.Copy=ATOM3Boolean()
      self.obj2581.Copy.setValue(('Copy from LHS', 1))
      self.obj2581.Copy.config = 0
      self.obj2581.Specify=ATOM3Constraint()
      self.obj2581.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj258.GGset2Any['Name']= self.obj2581
      self.obj2582= AttrCalc()
      self.obj2582.Copy=ATOM3Boolean()
      self.obj2582.Copy.setValue(('Copy from LHS', 1))
      self.obj2582.Copy.config = 0
      self.obj2582.Specify=ATOM3Constraint()
      self.obj2582.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj258.GGset2Any['ReqFlow']= self.obj2582

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj258)
      self.obj258.postAction( self.RHS.CREATE )

      self.obj259=metarial(parent)
      self.obj259.preAction( self.RHS.CREATE )
      self.obj259.isGraphObjectVisual = True

      if(hasattr(self.obj259, '_setHierarchicalLink')):
        self.obj259._setHierarchicalLink(False)

      # MaxFlow
      self.obj259.MaxFlow.setNone()

      # price
      self.obj259.price.setValue(0)

      # Name
      self.obj259.Name.setValue('')
      self.obj259.Name.setNone()

      # ReqFlow
      self.obj259.ReqFlow.setNone()

      self.obj259.GGLabel.setValue(6)
      self.obj259.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(280.0,240.0,self.obj259)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj259.graphObject_ = new_obj
      self.obj2590= AttrCalc()
      self.obj2590.Copy=ATOM3Boolean()
      self.obj2590.Copy.setValue(('Copy from LHS', 1))
      self.obj2590.Copy.config = 0
      self.obj2590.Specify=ATOM3Constraint()
      self.obj2590.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj259.GGset2Any['MaxFlow']= self.obj2590
      self.obj2591= AttrCalc()
      self.obj2591.Copy=ATOM3Boolean()
      self.obj2591.Copy.setValue(('Copy from LHS', 1))
      self.obj2591.Copy.config = 0
      self.obj2591.Specify=ATOM3Constraint()
      self.obj2591.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj259.GGset2Any['Name']= self.obj2591
      self.obj2592= AttrCalc()
      self.obj2592.Copy=ATOM3Boolean()
      self.obj2592.Copy.setValue(('Copy from LHS', 1))
      self.obj2592.Copy.config = 0
      self.obj2592.Specify=ATOM3Constraint()
      self.obj2592.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj259.GGset2Any['ReqFlow']= self.obj2592

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj259)
      self.obj259.postAction( self.RHS.CREATE )

      self.obj260=operatingUnit(parent)
      self.obj260.preAction( self.RHS.CREATE )
      self.obj260.isGraphObjectVisual = True

      if(hasattr(self.obj260, '_setHierarchicalLink')):
        self.obj260._setHierarchicalLink(False)

      # OperCostProp
      self.obj260.OperCostProp.setNone()

      # name
      self.obj260.name.setValue('')
      self.obj260.name.setNone()

      # OperCostFix
      self.obj260.OperCostFix.setNone()

      self.obj260.GGLabel.setValue(5)
      self.obj260.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(280.0,140.0,self.obj260)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj260.graphObject_ = new_obj
      self.obj2600= AttrCalc()
      self.obj2600.Copy=ATOM3Boolean()
      self.obj2600.Copy.setValue(('Copy from LHS', 1))
      self.obj2600.Copy.config = 0
      self.obj2600.Specify=ATOM3Constraint()
      self.obj2600.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj260.GGset2Any['OperCostProp']= self.obj2600
      self.obj2601= AttrCalc()
      self.obj2601.Copy=ATOM3Boolean()
      self.obj2601.Copy.setValue(('Copy from LHS', 1))
      self.obj2601.Copy.config = 0
      self.obj2601.Specify=ATOM3Constraint()
      self.obj2601.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj260.GGset2Any['name']= self.obj2601
      self.obj2602= AttrCalc()
      self.obj2602.Copy=ATOM3Boolean()
      self.obj2602.Copy.setValue(('Copy from LHS', 1))
      self.obj2602.Copy.config = 0
      self.obj2602.Specify=ATOM3Constraint()
      self.obj2602.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj260.GGset2Any['OperCostFix']= self.obj2602

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj260)
      self.obj260.postAction( self.RHS.CREATE )

      self.obj261=intoMaterial(parent)
      self.obj261.preAction( self.RHS.CREATE )
      self.obj261.isGraphObjectVisual = True

      if(hasattr(self.obj261, '_setHierarchicalLink')):
        self.obj261._setHierarchicalLink(False)

      # rate
      self.obj261.rate.setValue(0.0)

      self.obj261.GGLabel.setValue(10)
      self.obj261.graphClass_= graph_intoMaterial
      if parent.genGraphics:
         new_obj = graph_intoMaterial(315.25,202.5,self.obj261)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj261.graphObject_ = new_obj
      self.obj2610= AttrCalc()
      self.obj2610.Copy=ATOM3Boolean()
      self.obj2610.Copy.setValue(('Copy from LHS', 0))
      self.obj2610.Copy.config = 0
      self.obj2610.Specify=ATOM3Constraint()
      self.obj2610.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(3)).rate.getValue()\n\n\n\n\n\n\n\n\n\n'))
      self.obj261.GGset2Any['rate']= self.obj2610

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj261)
      self.obj261.postAction( self.RHS.CREATE )

      self.obj262=fromMaterial(parent)
      self.obj262.preAction( self.RHS.CREATE )
      self.obj262.isGraphObjectVisual = True

      if(hasattr(self.obj262, '_setHierarchicalLink')):
        self.obj262._setHierarchicalLink(False)

      # rate
      self.obj262.rate.setNone()

      self.obj262.GGLabel.setValue(8)
      self.obj262.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(323.0,83.0,self.obj262)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj262.graphObject_ = new_obj
      self.obj2620= AttrCalc()
      self.obj2620.Copy=ATOM3Boolean()
      self.obj2620.Copy.setValue(('Copy from LHS', 1))
      self.obj2620.Copy.config = 0
      self.obj2620.Specify=ATOM3Constraint()
      self.obj2620.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj262.GGset2Any['rate']= self.obj2620

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj262)
      self.obj262.postAction( self.RHS.CREATE )

      self.obj263=Goal(parent)
      self.obj263.preAction( self.RHS.CREATE )
      self.obj263.isGraphObjectVisual = True

      if(hasattr(self.obj263, '_setHierarchicalLink')):
        self.obj263._setHierarchicalLink(False)

      # name
      self.obj263.name.setValue('')
      self.obj263.name.setNone()

      self.obj263.GGLabel.setValue(2)
      self.obj263.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(60.0,220.0,self.obj263)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj263.graphObject_ = new_obj
      self.obj2630= AttrCalc()
      self.obj2630.Copy=ATOM3Boolean()
      self.obj2630.Copy.setValue(('Copy from LHS', 1))
      self.obj2630.Copy.config = 0
      self.obj2630.Specify=ATOM3Constraint()
      self.obj2630.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj263.GGset2Any['name']= self.obj2630

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj263)
      self.obj263.postAction( self.RHS.CREATE )

      self.obj264=Role(parent)
      self.obj264.preAction( self.RHS.CREATE )
      self.obj264.isGraphObjectVisual = True

      if(hasattr(self.obj264, '_setHierarchicalLink')):
        self.obj264._setHierarchicalLink(False)

      # name
      self.obj264.name.setValue('')
      self.obj264.name.setNone()

      self.obj264.GGLabel.setValue(1)
      self.obj264.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(60.0,40.0,self.obj264)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj264.graphObject_ = new_obj
      self.obj2640= AttrCalc()
      self.obj2640.Copy=ATOM3Boolean()
      self.obj2640.Copy.setValue(('Copy from LHS', 1))
      self.obj2640.Copy.config = 0
      self.obj2640.Specify=ATOM3Constraint()
      self.obj2640.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj264.GGset2Any['name']= self.obj2640

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj264)
      self.obj264.postAction( self.RHS.CREATE )

      self.obj265=achieve(parent)
      self.obj265.preAction( self.RHS.CREATE )
      self.obj265.isGraphObjectVisual = True

      if(hasattr(self.obj265, '_setHierarchicalLink')):
        self.obj265._setHierarchicalLink(False)

      # rate
      self.obj265.rate.setNone()

      self.obj265.GGLabel.setValue(3)
      self.obj265.graphClass_= graph_achieve
      if parent.genGraphics:
         new_obj = graph_achieve(93.5,143.5,self.obj265)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj265.graphObject_ = new_obj
      self.obj2650= AttrCalc()
      self.obj2650.Copy=ATOM3Boolean()
      self.obj2650.Copy.setValue(('Copy from LHS', 1))
      self.obj2650.Copy.config = 0
      self.obj2650.Specify=ATOM3Constraint()
      self.obj2650.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj265.GGset2Any['rate']= self.obj2650

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj265)
      self.obj265.postAction( self.RHS.CREATE )

      self.obj266=GenericGraphEdge(parent)
      self.obj266.preAction( self.RHS.CREATE )
      self.obj266.isGraphObjectVisual = True

      if(hasattr(self.obj266, '_setHierarchicalLink')):
        self.obj266._setHierarchicalLink(False)

      self.obj266.GGLabel.setValue(7)
      self.obj266.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(215.0,41.5,self.obj266)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj266.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj266)
      self.obj266.postAction( self.RHS.CREATE )

      self.obj267=GenericGraphEdge(parent)
      self.obj267.preAction( self.RHS.CREATE )
      self.obj267.isGraphObjectVisual = True

      if(hasattr(self.obj267, '_setHierarchicalLink')):
        self.obj267._setHierarchicalLink(False)

      self.obj267.GGLabel.setValue(9)
      self.obj267.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(185.0,276.0,self.obj267)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj267.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj267)
      self.obj267.postAction( self.RHS.CREATE )

      self.obj258.out_connections_.append(self.obj262)
      self.obj262.in_connections_.append(self.obj258)
      self.obj258.graphObject_.pendingConnections.append((self.obj258.graphObject_.tag, self.obj262.graphObject_.tag, [284.0, 69.0, 323.0, 83.0], 2, 0))
      self.obj260.out_connections_.append(self.obj261)
      self.obj261.in_connections_.append(self.obj260)
      self.obj260.graphObject_.pendingConnections.append((self.obj260.graphObject_.tag, self.obj261.graphObject_.tag, [333.0, 148.0, 332.0, 167.0, 371.25, 179.5], 2, True))
      self.obj261.out_connections_.append(self.obj259)
      self.obj259.in_connections_.append(self.obj261)
      self.obj261.graphObject_.pendingConnections.append((self.obj261.graphObject_.tag, self.obj259.graphObject_.tag, [326.0, 250.0, 354.5, 215.0, 371.25, 179.5], 2, True))
      self.obj262.out_connections_.append(self.obj260)
      self.obj260.in_connections_.append(self.obj262)
      self.obj262.graphObject_.pendingConnections.append((self.obj262.graphObject_.tag, self.obj260.graphObject_.tag, [333.0, 148.0, 352.0, 90.0], 2, 0))
      self.obj263.out_connections_.append(self.obj267)
      self.obj267.in_connections_.append(self.obj263)
      self.obj263.graphObject_.pendingConnections.append((self.obj263.graphObject_.tag, self.obj267.graphObject_.tag, [94.0, 270.0, 185.0, 276.0], 2, 0))
      self.obj264.out_connections_.append(self.obj265)
      self.obj265.in_connections_.append(self.obj264)
      self.obj264.graphObject_.pendingConnections.append((self.obj264.graphObject_.tag, self.obj265.graphObject_.tag, [91.0, 85.0, 93.5, 143.5], 2, 0))
      self.obj264.out_connections_.append(self.obj266)
      self.obj266.in_connections_.append(self.obj264)
      self.obj264.graphObject_.pendingConnections.append((self.obj264.graphObject_.tag, self.obj266.graphObject_.tag, [91.0, 40.0, 215.0, 41.5], 2, 0))
      self.obj265.out_connections_.append(self.obj263)
      self.obj263.in_connections_.append(self.obj265)
      self.obj265.graphObject_.pendingConnections.append((self.obj265.graphObject_.tag, self.obj263.graphObject_.tag, [93.0, 221.0, 93.5, 143.5], 2, 0))
      self.obj266.out_connections_.append(self.obj258)
      self.obj258.in_connections_.append(self.obj266)
      self.obj266.graphObject_.pendingConnections.append((self.obj266.graphObject_.tag, self.obj258.graphObject_.tag, [266.0, 62.0, 215.0, 41.5], 2, 0))
      self.obj267.out_connections_.append(self.obj259)
      self.obj259.in_connections_.append(self.obj267)
      self.obj267.graphObject_.pendingConnections.append((self.obj267.graphObject_.tag, self.obj259.graphObject_.tag, [286.0, 282.0, 185.0, 276.0], 2, 0))

   def condition(self, graphID, isograph, atom3i):
      print '======> Link Aux Condition'# _ Agent2Raw_GG_rule.py _
      aRg = self.getMatched ( graphID , self.LHS.nodeWithLabel(4) )
      nameARG = aRg.Name.getValue()
      g = self.getMatched ( graphID , self.LHS.nodeWithLabel(6) )
      # test if nameARG  end with name of Goal 
      print  nameARG +' END WITH '+g.Name.getValue()
      print nameARG.endswith( g.Name.getValue() )
      if nameARG.endswith( g.Name.getValue() ) and not hasattr(aRg,'LinkAux'): 
       print 'Real True'
       return True
      else : 
       print 'Real False'
       return False
      
      

   def action(self, graphID, isograph, atom3i):
      print '======> Link Aux Action'
      aRg = self.getMatched ( graphID , self.LHS.nodeWithLabel(4) )
      aRg.LinkAux = True 
      
      

