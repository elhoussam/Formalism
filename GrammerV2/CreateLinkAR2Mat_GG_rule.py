# _ CreateLinkAR2Mat_GG_rule.py ____________________________________________________________________________
# File generated automatically by ATOM3. Graph Grammar Rule
# ___________________________________________________________________________________________
from GGrule import *
from CapableOf import *
from GenericGraphEdge import *
from Goal import *
from ASG_omacss import *
from intoProduct import *
from operatingUnit import *
from metarial import *
from rawMaterial import *
from Agent import *
from fromMaterial import *
from Capabilitie import *
from Role import *
from requir import *
from fromRaw import *
from ASG_pns2 import *
from intoMaterial import *
from ASG_GenericGraph import *
from product import *
from GenericGraphNode import *
from achieve import *
from posses import *
class CreateLinkAR2Mat_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 20)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_omacss(parent)
      self.LHS.merge(ASG_pns2(parent))
      self.LHS.merge(ASG_GenericGraph(parent))

      self.obj1134=Agent(parent)
      self.obj1134.preAction( self.LHS.CREATE )
      self.obj1134.isGraphObjectVisual = True

      if(hasattr(self.obj1134, '_setHierarchicalLink')):
        self.obj1134._setHierarchicalLink(False)

      # price
      self.obj1134.price.setNone()

      # name
      self.obj1134.name.setValue('')
      self.obj1134.name.setNone()

      self.obj1134.GGLabel.setValue(1)
      self.obj1134.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(40.0,20.0,self.obj1134)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1134.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1134)
      self.obj1134.postAction( self.LHS.CREATE )

      self.obj1135=Role(parent)
      self.obj1135.preAction( self.LHS.CREATE )
      self.obj1135.isGraphObjectVisual = True

      if(hasattr(self.obj1135, '_setHierarchicalLink')):
        self.obj1135._setHierarchicalLink(False)

      # name
      self.obj1135.name.setValue('')
      self.obj1135.name.setNone()

      self.obj1135.GGLabel.setValue(2)
      self.obj1135.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(60.0,140.0,self.obj1135)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1135.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1135)
      self.obj1135.postAction( self.LHS.CREATE )

      self.obj1136=CapableOf(parent)
      self.obj1136.preAction( self.LHS.CREATE )
      self.obj1136.isGraphObjectVisual = True

      if(hasattr(self.obj1136, '_setHierarchicalLink')):
        self.obj1136._setHierarchicalLink(False)

      self.obj1136.GGLabel.setValue(3)
      self.obj1136.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(74.5,111.5,self.obj1136)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1136.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1136)
      self.obj1136.postAction( self.LHS.CREATE )

      self.obj1137=rawMaterial(parent)
      self.obj1137.preAction( self.LHS.CREATE )
      self.obj1137.isGraphObjectVisual = True

      if(hasattr(self.obj1137, '_setHierarchicalLink')):
        self.obj1137._setHierarchicalLink(False)

      # Name
      self.obj1137.Name.setValue('')
      self.obj1137.Name.setNone()

      self.obj1137.GGLabel.setValue(6)
      self.obj1137.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(240.0,20.0,self.obj1137)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1137.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1137)
      self.obj1137.postAction( self.LHS.CREATE )

      self.obj1138=operatingUnit(parent)
      self.obj1138.preAction( self.LHS.CREATE )
      self.obj1138.isGraphObjectVisual = True

      if(hasattr(self.obj1138, '_setHierarchicalLink')):
        self.obj1138._setHierarchicalLink(False)

      # name
      self.obj1138.name.setValue('')
      self.obj1138.name.setNone()

      self.obj1138.GGLabel.setValue(12)
      self.obj1138.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(320.0,240.0,self.obj1138)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1138.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1138)
      self.obj1138.postAction( self.LHS.CREATE )

      self.obj1139=operatingUnit(parent)
      self.obj1139.preAction( self.LHS.CREATE )
      self.obj1139.isGraphObjectVisual = True

      if(hasattr(self.obj1139, '_setHierarchicalLink')):
        self.obj1139._setHierarchicalLink(False)

      # name
      self.obj1139.name.setValue('')
      self.obj1139.name.setNone()

      self.obj1139.GGLabel.setValue(7)
      self.obj1139.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(320.0,100.0,self.obj1139)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1139.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1139)
      self.obj1139.postAction( self.LHS.CREATE )

      self.obj1140=metarial(parent)
      self.obj1140.preAction( self.LHS.CREATE )
      self.obj1140.isGraphObjectVisual = True

      if(hasattr(self.obj1140, '_setHierarchicalLink')):
        self.obj1140._setHierarchicalLink(False)

      # Name
      self.obj1140.Name.setValue('')
      self.obj1140.Name.setNone()

      self.obj1140.GGLabel.setValue(11)
      self.obj1140.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(240.0,160.0,self.obj1140)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1140.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1140)
      self.obj1140.postAction( self.LHS.CREATE )

      self.obj1141=fromMaterial(parent)
      self.obj1141.preAction( self.LHS.CREATE )
      self.obj1141.isGraphObjectVisual = True

      if(hasattr(self.obj1141, '_setHierarchicalLink')):
        self.obj1141._setHierarchicalLink(False)

      # rate
      self.obj1141.rate.setNone()

      self.obj1141.GGLabel.setValue(14)
      self.obj1141.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(340.0,197.0,self.obj1141)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1141.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1141)
      self.obj1141.postAction( self.LHS.CREATE )

      self.obj1142=fromRaw(parent)
      self.obj1142.preAction( self.LHS.CREATE )
      self.obj1142.isGraphObjectVisual = True

      if(hasattr(self.obj1142, '_setHierarchicalLink')):
        self.obj1142._setHierarchicalLink(False)

      # rate
      self.obj1142.rate.setNone()

      self.obj1142.GGLabel.setValue(9)
      self.obj1142.graphClass_= graph_fromRaw
      if parent.genGraphics:
         new_obj = graph_fromRaw(329.081775701,37.1184210526,self.obj1142)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1142.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1142)
      self.obj1142.postAction( self.LHS.CREATE )

      self.obj1143=GenericGraphEdge(parent)
      self.obj1143.preAction( self.LHS.CREATE )
      self.obj1143.isGraphObjectVisual = True

      if(hasattr(self.obj1143, '_setHierarchicalLink')):
        self.obj1143._setHierarchicalLink(False)

      self.obj1143.GGLabel.setValue(13)
      self.obj1143.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(167.0,195.0,self.obj1143)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1143.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1143)
      self.obj1143.postAction( self.LHS.CREATE )

      self.obj1144=GenericGraphEdge(parent)
      self.obj1144.preAction( self.LHS.CREATE )
      self.obj1144.isGraphObjectVisual = True

      if(hasattr(self.obj1144, '_setHierarchicalLink')):
        self.obj1144._setHierarchicalLink(False)

      self.obj1144.GGLabel.setValue(10)
      self.obj1144.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(288.198598131,95.0,self.obj1144)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1144.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1144)
      self.obj1144.postAction( self.LHS.CREATE )

      self.obj1145=GenericGraphEdge(parent)
      self.obj1145.preAction( self.LHS.CREATE )
      self.obj1145.isGraphObjectVisual = True

      if(hasattr(self.obj1145, '_setHierarchicalLink')):
        self.obj1145._setHierarchicalLink(False)

      self.obj1145.GGLabel.setValue(15)
      self.obj1145.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(170.5,76.0,self.obj1145)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1145.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1145)
      self.obj1145.postAction( self.LHS.CREATE )

      self.obj1134.out_connections_.append(self.obj1136)
      self.obj1136.in_connections_.append(self.obj1134)
      self.obj1134.graphObject_.pendingConnections.append((self.obj1134.graphObject_.tag, self.obj1136.graphObject_.tag, [65.0, 82.0, 74.5, 111.5], 0, True))
      self.obj1134.out_connections_.append(self.obj1144)
      self.obj1144.in_connections_.append(self.obj1134)
      self.obj1134.graphObject_.pendingConnections.append((self.obj1134.graphObject_.tag, self.obj1144.graphObject_.tag, [77.0, 82.0, 216.5, 96.5, 288.1985981308411, 95.0], 2, True))
      self.obj1134.out_connections_.append(self.obj1145)
      self.obj1145.in_connections_.append(self.obj1134)
      self.obj1134.graphObject_.pendingConnections.append((self.obj1134.graphObject_.tag, self.obj1145.graphObject_.tag, [77.0, 82.0, 170.5, 76.0], 0, True))
      self.obj1135.out_connections_.append(self.obj1143)
      self.obj1143.in_connections_.append(self.obj1135)
      self.obj1135.graphObject_.pendingConnections.append((self.obj1135.graphObject_.tag, self.obj1143.graphObject_.tag, [84.0, 186.0, 167.0, 195.0], 0, True))
      self.obj1136.out_connections_.append(self.obj1135)
      self.obj1135.in_connections_.append(self.obj1136)
      self.obj1136.graphObject_.pendingConnections.append((self.obj1136.graphObject_.tag, self.obj1135.graphObject_.tag, [91.0, 140.0, 74.5, 111.5], 2, 0))
      self.obj1137.out_connections_.append(self.obj1142)
      self.obj1142.in_connections_.append(self.obj1137)
      self.obj1137.graphObject_.pendingConnections.append((self.obj1137.graphObject_.tag, self.obj1142.graphObject_.tag, [264.0, 73.0, 299.5, 33.5, 329.0817757009346, 37.118421052631575], 2, True))
      self.obj1140.out_connections_.append(self.obj1141)
      self.obj1141.in_connections_.append(self.obj1140)
      self.obj1140.graphObject_.pendingConnections.append((self.obj1140.graphObject_.tag, self.obj1141.graphObject_.tag, [281.0, 167.0, 372.0, 226.0, 328.0, 153.0], 2, True))
      self.obj1141.out_connections_.append(self.obj1138)
      self.obj1138.in_connections_.append(self.obj1141)
      self.obj1141.graphObject_.pendingConnections.append((self.obj1141.graphObject_.tag, self.obj1138.graphObject_.tag, [333.5700934579439, 248.42105263157896, 296.0, 124.0, 328.0, 153.0], 2, True))
      self.obj1142.out_connections_.append(self.obj1139)
      self.obj1139.in_connections_.append(self.obj1142)
      self.obj1142.graphObject_.pendingConnections.append((self.obj1142.graphObject_.tag, self.obj1139.graphObject_.tag, [362.32710280373834, 107.47368421052629, 358.6635514018692, 40.73684210526314, 329.0817757009346, 37.118421052631575], 2, True))
      self.obj1143.out_connections_.append(self.obj1140)
      self.obj1140.in_connections_.append(self.obj1143)
      self.obj1143.graphObject_.pendingConnections.append((self.obj1143.graphObject_.tag, self.obj1140.graphObject_.tag, [250.0, 204.0, 167.0, 195.0], 2, 0))
      self.obj1144.out_connections_.append(self.obj1139)
      self.obj1139.in_connections_.append(self.obj1144)
      self.obj1144.graphObject_.pendingConnections.append((self.obj1144.graphObject_.tag, self.obj1139.graphObject_.tag, [335.1869158878505, 115.5263157894737, 288.198598131, 95.0], 2, 0))
      self.obj1145.out_connections_.append(self.obj1137)
      self.obj1137.in_connections_.append(self.obj1145)
      self.obj1145.graphObject_.pendingConnections.append((self.obj1145.graphObject_.tag, self.obj1137.graphObject_.tag, [264.0, 70.0, 170.5, 76.0], 2, 0))

      self.RHS = ASG_omacss(parent)
      self.RHS.merge(ASG_pns2(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj1149=Agent(parent)
      self.obj1149.preAction( self.RHS.CREATE )
      self.obj1149.isGraphObjectVisual = True

      if(hasattr(self.obj1149, '_setHierarchicalLink')):
        self.obj1149._setHierarchicalLink(False)

      # price
      self.obj1149.price.setValue(0)

      # name
      self.obj1149.name.setValue('')
      self.obj1149.name.setNone()

      self.obj1149.GGLabel.setValue(1)
      self.obj1149.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(60.0,20.0,self.obj1149)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1149.graphObject_ = new_obj
      self.obj11490= AttrCalc()
      self.obj11490.Copy=ATOM3Boolean()
      self.obj11490.Copy.setValue(('Copy from LHS', 1))
      self.obj11490.Copy.config = 0
      self.obj11490.Specify=ATOM3Constraint()
      self.obj11490.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1149.GGset2Any['price']= self.obj11490
      self.obj11491= AttrCalc()
      self.obj11491.Copy=ATOM3Boolean()
      self.obj11491.Copy.setValue(('Copy from LHS', 1))
      self.obj11491.Copy.config = 0
      self.obj11491.Specify=ATOM3Constraint()
      self.obj11491.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1149.GGset2Any['name']= self.obj11491

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1149)
      self.obj1149.postAction( self.RHS.CREATE )

      self.obj1150=Role(parent)
      self.obj1150.preAction( self.RHS.CREATE )
      self.obj1150.isGraphObjectVisual = True

      if(hasattr(self.obj1150, '_setHierarchicalLink')):
        self.obj1150._setHierarchicalLink(False)

      # name
      self.obj1150.name.setValue('')
      self.obj1150.name.setNone()

      self.obj1150.GGLabel.setValue(2)
      self.obj1150.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(80.0,160.0,self.obj1150)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1150.graphObject_ = new_obj
      self.obj11500= AttrCalc()
      self.obj11500.Copy=ATOM3Boolean()
      self.obj11500.Copy.setValue(('Copy from LHS', 1))
      self.obj11500.Copy.config = 0
      self.obj11500.Specify=ATOM3Constraint()
      self.obj11500.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1150.GGset2Any['name']= self.obj11500

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1150)
      self.obj1150.postAction( self.RHS.CREATE )

      self.obj1151=CapableOf(parent)
      self.obj1151.preAction( self.RHS.CREATE )
      self.obj1151.isGraphObjectVisual = True

      if(hasattr(self.obj1151, '_setHierarchicalLink')):
        self.obj1151._setHierarchicalLink(False)

      self.obj1151.GGLabel.setValue(3)
      self.obj1151.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(104.5,111.5,self.obj1151)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1151.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1151)
      self.obj1151.postAction( self.RHS.CREATE )

      self.obj1152=rawMaterial(parent)
      self.obj1152.preAction( self.RHS.CREATE )
      self.obj1152.isGraphObjectVisual = True

      if(hasattr(self.obj1152, '_setHierarchicalLink')):
        self.obj1152._setHierarchicalLink(False)

      # Name
      self.obj1152.Name.setValue('')
      self.obj1152.Name.setNone()

      self.obj1152.GGLabel.setValue(6)
      self.obj1152.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(300.0,20.0,self.obj1152)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1152.graphObject_ = new_obj
      self.obj11520= AttrCalc()
      self.obj11520.Copy=ATOM3Boolean()
      self.obj11520.Copy.setValue(('Copy from LHS', 1))
      self.obj11520.Copy.config = 0
      self.obj11520.Specify=ATOM3Constraint()
      self.obj11520.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1152.GGset2Any['Name']= self.obj11520

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1152)
      self.obj1152.postAction( self.RHS.CREATE )

      self.obj1153=operatingUnit(parent)
      self.obj1153.preAction( self.RHS.CREATE )
      self.obj1153.isGraphObjectVisual = True

      if(hasattr(self.obj1153, '_setHierarchicalLink')):
        self.obj1153._setHierarchicalLink(False)

      # name
      self.obj1153.name.setValue('')
      self.obj1153.name.setNone()

      self.obj1153.GGLabel.setValue(7)
      self.obj1153.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(300.0,100.0,self.obj1153)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1153.graphObject_ = new_obj
      self.obj11530= AttrCalc()
      self.obj11530.Copy=ATOM3Boolean()
      self.obj11530.Copy.setValue(('Copy from LHS', 1))
      self.obj11530.Copy.config = 0
      self.obj11530.Specify=ATOM3Constraint()
      self.obj11530.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1153.GGset2Any['name']= self.obj11530

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1153)
      self.obj1153.postAction( self.RHS.CREATE )

      self.obj1154=operatingUnit(parent)
      self.obj1154.preAction( self.RHS.CREATE )
      self.obj1154.isGraphObjectVisual = True

      if(hasattr(self.obj1154, '_setHierarchicalLink')):
        self.obj1154._setHierarchicalLink(False)

      # name
      self.obj1154.name.setValue('')
      self.obj1154.name.setNone()

      self.obj1154.GGLabel.setValue(12)
      self.obj1154.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(240.0,260.0,self.obj1154)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1154.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1154)
      self.obj1154.postAction( self.RHS.CREATE )

      self.obj1155=metarial(parent)
      self.obj1155.preAction( self.RHS.CREATE )
      self.obj1155.isGraphObjectVisual = True

      if(hasattr(self.obj1155, '_setHierarchicalLink')):
        self.obj1155._setHierarchicalLink(False)

      # Name
      self.obj1155.Name.setValue('')
      self.obj1155.Name.setNone()

      self.obj1155.GGLabel.setValue(11)
      self.obj1155.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(320.0,160.0,self.obj1155)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1155.graphObject_ = new_obj
      self.obj11550= AttrCalc()
      self.obj11550.Copy=ATOM3Boolean()
      self.obj11550.Copy.setValue(('Copy from LHS', 1))
      self.obj11550.Copy.config = 0
      self.obj11550.Specify=ATOM3Constraint()
      self.obj11550.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1155.GGset2Any['Name']= self.obj11550

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1155)
      self.obj1155.postAction( self.RHS.CREATE )

      self.obj1156=fromMaterial(parent)
      self.obj1156.preAction( self.RHS.CREATE )
      self.obj1156.isGraphObjectVisual = True

      if(hasattr(self.obj1156, '_setHierarchicalLink')):
        self.obj1156._setHierarchicalLink(False)

      # rate
      self.obj1156.rate.setValue(0.0)

      self.obj1156.GGLabel.setValue(14)
      self.obj1156.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(317.285046729,218.710526316,self.obj1156)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1156.graphObject_ = new_obj
      self.obj11560= AttrCalc()
      self.obj11560.Copy=ATOM3Boolean()
      self.obj11560.Copy.setValue(('Copy from LHS', 1))
      self.obj11560.Copy.config = 0
      self.obj11560.Specify=ATOM3Constraint()
      self.obj11560.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1156.GGset2Any['rate']= self.obj11560

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1156)
      self.obj1156.postAction( self.RHS.CREATE )

      self.obj1157=fromRaw(parent)
      self.obj1157.preAction( self.RHS.CREATE )
      self.obj1157.isGraphObjectVisual = True

      if(hasattr(self.obj1157, '_setHierarchicalLink')):
        self.obj1157._setHierarchicalLink(False)

      # rate
      self.obj1157.rate.setValue(0.0)

      self.obj1157.GGLabel.setValue(9)
      self.obj1157.graphClass_= graph_fromRaw
      if parent.genGraphics:
         new_obj = graph_fromRaw(318.285046729,90.7105263158,self.obj1157)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1157.graphObject_ = new_obj
      self.obj11570= AttrCalc()
      self.obj11570.Copy=ATOM3Boolean()
      self.obj11570.Copy.setValue(('Copy from LHS', 1))
      self.obj11570.Copy.config = 0
      self.obj11570.Specify=ATOM3Constraint()
      self.obj11570.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1157.GGset2Any['rate']= self.obj11570

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1157)
      self.obj1157.postAction( self.RHS.CREATE )

      self.obj1158=intoMaterial(parent)
      self.obj1158.preAction( self.RHS.CREATE )
      self.obj1158.isGraphObjectVisual = True

      if(hasattr(self.obj1158, '_setHierarchicalLink')):
        self.obj1158._setHierarchicalLink(False)

      # rate
      self.obj1158.rate.setValue(0.0)

      self.obj1158.GGLabel.setValue(16)
      self.obj1158.graphClass_= graph_intoMaterial
      if parent.genGraphics:
         new_obj = graph_intoMaterial(322.093457944,135.263157895,self.obj1158)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1158.graphObject_ = new_obj
      self.obj11580= AttrCalc()
      self.obj11580.Copy=ATOM3Boolean()
      self.obj11580.Copy.setValue(('Copy from LHS', 0))
      self.obj11580.Copy.config = 0
      self.obj11580.Specify=ATOM3Constraint()
      self.obj11580.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1158.GGset2Any['rate']= self.obj11580

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1158)
      self.obj1158.postAction( self.RHS.CREATE )

      self.obj1159=GenericGraphEdge(parent)
      self.obj1159.preAction( self.RHS.CREATE )
      self.obj1159.isGraphObjectVisual = True

      if(hasattr(self.obj1159, '_setHierarchicalLink')):
        self.obj1159._setHierarchicalLink(False)

      self.obj1159.GGLabel.setValue(10)
      self.obj1159.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(199.285046729,85.2105263158,self.obj1159)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1159.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1159)
      self.obj1159.postAction( self.RHS.CREATE )

      self.obj1160=GenericGraphEdge(parent)
      self.obj1160.preAction( self.RHS.CREATE )
      self.obj1160.isGraphObjectVisual = True

      if(hasattr(self.obj1160, '_setHierarchicalLink')):
        self.obj1160._setHierarchicalLink(False)

      self.obj1160.GGLabel.setValue(13)
      self.obj1160.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(208.0,174.0,self.obj1160)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1160.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1160)
      self.obj1160.postAction( self.RHS.CREATE )

      self.obj1161=GenericGraphEdge(parent)
      self.obj1161.preAction( self.RHS.CREATE )
      self.obj1161.isGraphObjectVisual = True

      if(hasattr(self.obj1161, '_setHierarchicalLink')):
        self.obj1161._setHierarchicalLink(False)

      self.obj1161.GGLabel.setValue(15)
      self.obj1161.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(229.5,47.0,self.obj1161)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1161.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1161)
      self.obj1161.postAction( self.RHS.CREATE )

      self.obj1149.out_connections_.append(self.obj1151)
      self.obj1151.in_connections_.append(self.obj1149)
      self.obj1149.graphObject_.pendingConnections.append((self.obj1149.graphObject_.tag, self.obj1151.graphObject_.tag, [85.0, 82.0, 104.5, 111.5], 0, True))
      self.obj1149.out_connections_.append(self.obj1159)
      self.obj1159.in_connections_.append(self.obj1149)
      self.obj1149.graphObject_.pendingConnections.append((self.obj1149.graphObject_.tag, self.obj1159.graphObject_.tag, [85.0, 82.0, 199.28504672897196, 85.21052631578948], 0, True))
      self.obj1149.out_connections_.append(self.obj1161)
      self.obj1161.in_connections_.append(self.obj1149)
      self.obj1149.graphObject_.pendingConnections.append((self.obj1149.graphObject_.tag, self.obj1161.graphObject_.tag, [97.0, 82.0, 229.5, 47.0], 0, True))
      self.obj1150.out_connections_.append(self.obj1160)
      self.obj1160.in_connections_.append(self.obj1150)
      self.obj1150.graphObject_.pendingConnections.append((self.obj1150.graphObject_.tag, self.obj1160.graphObject_.tag, [104.0, 161.0, 208.0, 174.0], 0, True))
      self.obj1151.out_connections_.append(self.obj1150)
      self.obj1150.in_connections_.append(self.obj1151)
      self.obj1151.graphObject_.pendingConnections.append((self.obj1151.graphObject_.tag, self.obj1150.graphObject_.tag, [111.0, 160.0, 104.5, 111.5], 2, 0))
      self.obj1152.out_connections_.append(self.obj1157)
      self.obj1157.in_connections_.append(self.obj1152)
      self.obj1152.graphObject_.pendingConnections.append((self.obj1152.graphObject_.tag, self.obj1157.graphObject_.tag, [324.0, 73.0, 318.28504672897196, 90.71052631578948], 0, True))
      self.obj1153.out_connections_.append(self.obj1158)
      self.obj1158.in_connections_.append(self.obj1153)
      self.obj1153.graphObject_.pendingConnections.append((self.obj1153.graphObject_.tag, self.obj1158.graphObject_.tag, [315.1869158878505, 115.5263157894737, 322.0934579439253, 135.26315789473685], 0, True))
      self.obj1155.out_connections_.append(self.obj1156)
      self.obj1156.in_connections_.append(self.obj1155)
      self.obj1155.graphObject_.pendingConnections.append((self.obj1155.graphObject_.tag, self.obj1156.graphObject_.tag, [357.0, 205.0, 317.28504672897196, 218.71052631578948], 0, True))
      self.obj1156.out_connections_.append(self.obj1154)
      self.obj1154.in_connections_.append(self.obj1156)
      self.obj1156.graphObject_.pendingConnections.append((self.obj1156.graphObject_.tag, self.obj1154.graphObject_.tag, [253.57009345794393, 248.42105263157896, 315.28504672897196, 206.71052631578948], 0, True))
      self.obj1157.out_connections_.append(self.obj1153)
      self.obj1153.in_connections_.append(self.obj1157)
      self.obj1157.graphObject_.pendingConnections.append((self.obj1157.graphObject_.tag, self.obj1153.graphObject_.tag, [314.5700934579439, 108.42105263157895, 319.28504672897196, 90.71052631578948], 0, True))
      self.obj1158.out_connections_.append(self.obj1155)
      self.obj1155.in_connections_.append(self.obj1158)
      self.obj1158.graphObject_.pendingConnections.append((self.obj1158.graphObject_.tag, self.obj1155.graphObject_.tag, [347.0, 161.0, 311.0934579439253, 128.26315789473685], 0, True))
      self.obj1159.out_connections_.append(self.obj1153)
      self.obj1153.in_connections_.append(self.obj1159)
      self.obj1159.graphObject_.pendingConnections.append((self.obj1159.graphObject_.tag, self.obj1153.graphObject_.tag, [314.5700934579439, 108.42105263157895, 199.285046729, 85.2105263158], 2, 0))
      self.obj1160.out_connections_.append(self.obj1155)
      self.obj1155.in_connections_.append(self.obj1160)
      self.obj1160.graphObject_.pendingConnections.append((self.obj1160.graphObject_.tag, self.obj1155.graphObject_.tag, [332.0, 165.0, 208.0, 143.0], 2, 0))
      self.obj1161.out_connections_.append(self.obj1152)
      self.obj1152.in_connections_.append(self.obj1161)
      self.obj1161.graphObject_.pendingConnections.append((self.obj1161.graphObject_.tag, self.obj1152.graphObject_.tag, [324.0, 70.0, 210.5, 76.0], 0, True))

   def condition(self, graphID, isograph, atom3i):
      
      node7 = self.getMatched(graphID, self.LHS.nodeWithLabel(7))
      
      node11 = self.getMatched(graphID, self.LHS.nodeWithLabel(11))
      node1 = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      
      print node7.name.getValue()+' in '+ node11.Name.getValue() 
      print node7.name.getValue() in  node11.Name.getValue()
      print 'Rule 20 '
      
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
      
      

