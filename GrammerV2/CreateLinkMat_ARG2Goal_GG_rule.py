# _ CreateLinkMat_ARG2Goal_GG_rule.py ____________________________________________________________________________
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
class CreateLinkMat_ARG2Goal_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 19)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_omacss(parent)
      self.LHS.merge(ASG_pns2(parent))
      self.LHS.merge(ASG_GenericGraph(parent))

      self.obj1106=Role(parent)
      self.obj1106.preAction( self.LHS.CREATE )
      self.obj1106.isGraphObjectVisual = True

      if(hasattr(self.obj1106, '_setHierarchicalLink')):
        self.obj1106._setHierarchicalLink(False)

      # name
      self.obj1106.name.setValue('')
      self.obj1106.name.setNone()

      self.obj1106.GGLabel.setValue(1)
      self.obj1106.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(80.0,20.0,self.obj1106)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1106.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1106)
      self.obj1106.postAction( self.LHS.CREATE )

      self.obj1107=Goal(parent)
      self.obj1107.preAction( self.LHS.CREATE )
      self.obj1107.isGraphObjectVisual = True

      if(hasattr(self.obj1107, '_setHierarchicalLink')):
        self.obj1107._setHierarchicalLink(False)

      # name
      self.obj1107.name.setValue('')
      self.obj1107.name.setNone()

      self.obj1107.GGLabel.setValue(2)
      self.obj1107.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(100.0,180.0,self.obj1107)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1107.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1107)
      self.obj1107.postAction( self.LHS.CREATE )

      self.obj1108=achieve(parent)
      self.obj1108.preAction( self.LHS.CREATE )
      self.obj1108.isGraphObjectVisual = True

      if(hasattr(self.obj1108, '_setHierarchicalLink')):
        self.obj1108._setHierarchicalLink(False)

      # rate
      self.obj1108.rate.setNone()

      self.obj1108.GGLabel.setValue(3)
      self.obj1108.graphClass_= graph_achieve
      if parent.genGraphics:
         new_obj = graph_achieve(113.5,123.5,self.obj1108)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1108.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1108)
      self.obj1108.postAction( self.LHS.CREATE )

      self.obj1109=operatingUnit(parent)
      self.obj1109.preAction( self.LHS.CREATE )
      self.obj1109.isGraphObjectVisual = True

      if(hasattr(self.obj1109, '_setHierarchicalLink')):
        self.obj1109._setHierarchicalLink(False)

      # name
      self.obj1109.name.setValue('')
      self.obj1109.name.setNone()

      self.obj1109.GGLabel.setValue(5)
      self.obj1109.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(280.0,100.0,self.obj1109)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1109.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1109)
      self.obj1109.postAction( self.LHS.CREATE )

      self.obj1110=metarial(parent)
      self.obj1110.preAction( self.LHS.CREATE )
      self.obj1110.isGraphObjectVisual = True

      if(hasattr(self.obj1110, '_setHierarchicalLink')):
        self.obj1110._setHierarchicalLink(False)

      # Name
      self.obj1110.Name.setValue('')
      self.obj1110.Name.setNone()

      self.obj1110.GGLabel.setValue(4)
      self.obj1110.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(280.0,20.0,self.obj1110)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1110.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1110)
      self.obj1110.postAction( self.LHS.CREATE )

      self.obj1111=metarial(parent)
      self.obj1111.preAction( self.LHS.CREATE )
      self.obj1111.isGraphObjectVisual = True

      if(hasattr(self.obj1111, '_setHierarchicalLink')):
        self.obj1111._setHierarchicalLink(False)

      # Name
      self.obj1111.Name.setValue('')
      self.obj1111.Name.setNone()

      self.obj1111.GGLabel.setValue(6)
      self.obj1111.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(320.0,220.0,self.obj1111)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1111.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1111)
      self.obj1111.postAction( self.LHS.CREATE )

      self.obj1112=fromMaterial(parent)
      self.obj1112.preAction( self.LHS.CREATE )
      self.obj1112.isGraphObjectVisual = True

      if(hasattr(self.obj1112, '_setHierarchicalLink')):
        self.obj1112._setHierarchicalLink(False)

      # rate
      self.obj1112.rate.setNone()

      self.obj1112.GGLabel.setValue(8)
      self.obj1112.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(298.785046729,89.2105263158,self.obj1112)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1112.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1112)
      self.obj1112.postAction( self.LHS.CREATE )

      self.obj1113=GenericGraphEdge(parent)
      self.obj1113.preAction( self.LHS.CREATE )
      self.obj1113.isGraphObjectVisual = True

      if(hasattr(self.obj1113, '_setHierarchicalLink')):
        self.obj1113._setHierarchicalLink(False)

      self.obj1113.GGLabel.setValue(7)
      self.obj1113.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(198.0,23.0,self.obj1113)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1113.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1113)
      self.obj1113.postAction( self.LHS.CREATE )

      self.obj1114=GenericGraphEdge(parent)
      self.obj1114.preAction( self.LHS.CREATE )
      self.obj1114.isGraphObjectVisual = True

      if(hasattr(self.obj1114, '_setHierarchicalLink')):
        self.obj1114._setHierarchicalLink(False)

      self.obj1114.GGLabel.setValue(9)
      self.obj1114.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(228.0,227.5,self.obj1114)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1114.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1114)
      self.obj1114.postAction( self.LHS.CREATE )

      self.obj1106.out_connections_.append(self.obj1108)
      self.obj1108.in_connections_.append(self.obj1106)
      self.obj1106.graphObject_.pendingConnections.append((self.obj1106.graphObject_.tag, self.obj1108.graphObject_.tag, [104.0, 66.0, 113.5, 123.5], 0, True))
      self.obj1106.out_connections_.append(self.obj1113)
      self.obj1113.in_connections_.append(self.obj1106)
      self.obj1106.graphObject_.pendingConnections.append((self.obj1106.graphObject_.tag, self.obj1113.graphObject_.tag, [104.0, 21.0, 198.0, 23.0], 0, True))
      self.obj1107.out_connections_.append(self.obj1114)
      self.obj1114.in_connections_.append(self.obj1107)
      self.obj1107.graphObject_.pendingConnections.append((self.obj1107.graphObject_.tag, self.obj1114.graphObject_.tag, [124.0, 230.0, 228.0, 227.5], 0, True))
      self.obj1108.out_connections_.append(self.obj1107)
      self.obj1107.in_connections_.append(self.obj1108)
      self.obj1108.graphObject_.pendingConnections.append((self.obj1108.graphObject_.tag, self.obj1107.graphObject_.tag, [123.0, 181.0, 113.5, 123.5], 0, True))
      self.obj1110.out_connections_.append(self.obj1112)
      self.obj1112.in_connections_.append(self.obj1110)
      self.obj1110.graphObject_.pendingConnections.append((self.obj1110.graphObject_.tag, self.obj1112.graphObject_.tag, [304.0, 70.0, 298.78504672897196, 89.21052631578948], 0, True))
      self.obj1112.out_connections_.append(self.obj1109)
      self.obj1109.in_connections_.append(self.obj1112)
      self.obj1112.graphObject_.pendingConnections.append((self.obj1112.graphObject_.tag, self.obj1109.graphObject_.tag, [293.5700934579439, 108.42105263157895, 298.78504672897196, 89.21052631578948], 0, True))
      self.obj1113.out_connections_.append(self.obj1110)
      self.obj1110.in_connections_.append(self.obj1113)
      self.obj1113.graphObject_.pendingConnections.append((self.obj1113.graphObject_.tag, self.obj1110.graphObject_.tag, [292.0, 25.0, 198.0, 23.0], 0, True))
      self.obj1114.out_connections_.append(self.obj1111)
      self.obj1111.in_connections_.append(self.obj1114)
      self.obj1114.graphObject_.pendingConnections.append((self.obj1114.graphObject_.tag, self.obj1111.graphObject_.tag, [332.0, 225.0, 228.0, 227.5], 0, True))

      self.RHS = ASG_omacss(parent)
      self.RHS.merge(ASG_pns2(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj1118=Role(parent)
      self.obj1118.preAction( self.RHS.CREATE )
      self.obj1118.isGraphObjectVisual = True

      if(hasattr(self.obj1118, '_setHierarchicalLink')):
        self.obj1118._setHierarchicalLink(False)

      # name
      self.obj1118.name.setValue('')
      self.obj1118.name.setNone()

      self.obj1118.GGLabel.setValue(1)
      self.obj1118.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(100.0,40.0,self.obj1118)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1118.graphObject_ = new_obj
      self.obj11180= AttrCalc()
      self.obj11180.Copy=ATOM3Boolean()
      self.obj11180.Copy.setValue(('Copy from LHS', 1))
      self.obj11180.Copy.config = 0
      self.obj11180.Specify=ATOM3Constraint()
      self.obj11180.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1118.GGset2Any['name']= self.obj11180

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1118)
      self.obj1118.postAction( self.RHS.CREATE )

      self.obj1119=Goal(parent)
      self.obj1119.preAction( self.RHS.CREATE )
      self.obj1119.isGraphObjectVisual = True

      if(hasattr(self.obj1119, '_setHierarchicalLink')):
        self.obj1119._setHierarchicalLink(False)

      # name
      self.obj1119.name.setValue('')
      self.obj1119.name.setNone()

      self.obj1119.GGLabel.setValue(2)
      self.obj1119.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(120.0,160.0,self.obj1119)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1119.graphObject_ = new_obj
      self.obj11190= AttrCalc()
      self.obj11190.Copy=ATOM3Boolean()
      self.obj11190.Copy.setValue(('Copy from LHS', 1))
      self.obj11190.Copy.config = 0
      self.obj11190.Specify=ATOM3Constraint()
      self.obj11190.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1119.GGset2Any['name']= self.obj11190

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1119)
      self.obj1119.postAction( self.RHS.CREATE )

      self.obj1120=achieve(parent)
      self.obj1120.preAction( self.RHS.CREATE )
      self.obj1120.isGraphObjectVisual = True

      if(hasattr(self.obj1120, '_setHierarchicalLink')):
        self.obj1120._setHierarchicalLink(False)

      # rate
      self.obj1120.rate.setValue(0.0)

      self.obj1120.GGLabel.setValue(3)
      self.obj1120.graphClass_= graph_achieve
      if parent.genGraphics:
         new_obj = graph_achieve(133.5,123.5,self.obj1120)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1120.graphObject_ = new_obj
      self.obj11200= AttrCalc()
      self.obj11200.Copy=ATOM3Boolean()
      self.obj11200.Copy.setValue(('Copy from LHS', 1))
      self.obj11200.Copy.config = 0
      self.obj11200.Specify=ATOM3Constraint()
      self.obj11200.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1120.GGset2Any['rate']= self.obj11200

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1120)
      self.obj1120.postAction( self.RHS.CREATE )

      self.obj1121=operatingUnit(parent)
      self.obj1121.preAction( self.RHS.CREATE )
      self.obj1121.isGraphObjectVisual = True

      if(hasattr(self.obj1121, '_setHierarchicalLink')):
        self.obj1121._setHierarchicalLink(False)

      # name
      self.obj1121.name.setValue('')
      self.obj1121.name.setNone()

      self.obj1121.GGLabel.setValue(5)
      self.obj1121.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(280.0,120.0,self.obj1121)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1121.graphObject_ = new_obj
      self.obj11210= AttrCalc()
      self.obj11210.Copy=ATOM3Boolean()
      self.obj11210.Copy.setValue(('Copy from LHS', 1))
      self.obj11210.Copy.config = 0
      self.obj11210.Specify=ATOM3Constraint()
      self.obj11210.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1121.GGset2Any['name']= self.obj11210

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1121)
      self.obj1121.postAction( self.RHS.CREATE )

      self.obj1122=metarial(parent)
      self.obj1122.preAction( self.RHS.CREATE )
      self.obj1122.isGraphObjectVisual = True

      if(hasattr(self.obj1122, '_setHierarchicalLink')):
        self.obj1122._setHierarchicalLink(False)

      # Name
      self.obj1122.Name.setValue('')
      self.obj1122.Name.setNone()

      self.obj1122.GGLabel.setValue(4)
      self.obj1122.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(280.0,40.0,self.obj1122)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1122.graphObject_ = new_obj
      self.obj11220= AttrCalc()
      self.obj11220.Copy=ATOM3Boolean()
      self.obj11220.Copy.setValue(('Copy from LHS', 1))
      self.obj11220.Copy.config = 0
      self.obj11220.Specify=ATOM3Constraint()
      self.obj11220.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1122.GGset2Any['Name']= self.obj11220

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1122)
      self.obj1122.postAction( self.RHS.CREATE )

      self.obj1123=metarial(parent)
      self.obj1123.preAction( self.RHS.CREATE )
      self.obj1123.isGraphObjectVisual = True

      if(hasattr(self.obj1123, '_setHierarchicalLink')):
        self.obj1123._setHierarchicalLink(False)

      # Name
      self.obj1123.Name.setValue('')
      self.obj1123.Name.setNone()

      self.obj1123.GGLabel.setValue(6)
      self.obj1123.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(280.0,200.0,self.obj1123)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1123.graphObject_ = new_obj
      self.obj11230= AttrCalc()
      self.obj11230.Copy=ATOM3Boolean()
      self.obj11230.Copy.setValue(('Copy from LHS', 1))
      self.obj11230.Copy.config = 0
      self.obj11230.Specify=ATOM3Constraint()
      self.obj11230.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1123.GGset2Any['Name']= self.obj11230

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1123)
      self.obj1123.postAction( self.RHS.CREATE )

      self.obj1124=fromMaterial(parent)
      self.obj1124.preAction( self.RHS.CREATE )
      self.obj1124.isGraphObjectVisual = True

      if(hasattr(self.obj1124, '_setHierarchicalLink')):
        self.obj1124._setHierarchicalLink(False)

      # rate
      self.obj1124.rate.setValue(0.0)

      self.obj1124.GGLabel.setValue(8)
      self.obj1124.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(298.785046729,109.210526316,self.obj1124)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1124.graphObject_ = new_obj
      self.obj11240= AttrCalc()
      self.obj11240.Copy=ATOM3Boolean()
      self.obj11240.Copy.setValue(('Copy from LHS', 1))
      self.obj11240.Copy.config = 0
      self.obj11240.Specify=ATOM3Constraint()
      self.obj11240.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1124.GGset2Any['rate']= self.obj11240

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1124)
      self.obj1124.postAction( self.RHS.CREATE )

      self.obj1125=intoMaterial(parent)
      self.obj1125.preAction( self.RHS.CREATE )
      self.obj1125.isGraphObjectVisual = True

      if(hasattr(self.obj1125, '_setHierarchicalLink')):
        self.obj1125._setHierarchicalLink(False)

      # rate
      self.obj1125.rate.setValue(0.0)

      self.obj1125.GGLabel.setValue(10)
      self.obj1125.graphClass_= graph_intoMaterial
      if parent.genGraphics:
         new_obj = graph_intoMaterial(301.093457944,168.263157895,self.obj1125)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1125.graphObject_ = new_obj
      self.obj11250= AttrCalc()
      self.obj11250.Copy=ATOM3Boolean()
      self.obj11250.Copy.setValue(('Copy from LHS', 0))
      self.obj11250.Copy.config = 0
      self.obj11250.Specify=ATOM3Constraint()
      self.obj11250.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(3)).rate.getValue()\n'))
      self.obj1125.GGset2Any['rate']= self.obj11250

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1125)
      self.obj1125.postAction( self.RHS.CREATE )

      self.obj1126=GenericGraphEdge(parent)
      self.obj1126.preAction( self.RHS.CREATE )
      self.obj1126.isGraphObjectVisual = True

      if(hasattr(self.obj1126, '_setHierarchicalLink')):
        self.obj1126._setHierarchicalLink(False)

      self.obj1126.GGLabel.setValue(7)
      self.obj1126.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(208.0,43.0,self.obj1126)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1126.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1126)
      self.obj1126.postAction( self.RHS.CREATE )

      self.obj1127=GenericGraphEdge(parent)
      self.obj1127.preAction( self.RHS.CREATE )
      self.obj1127.isGraphObjectVisual = True

      if(hasattr(self.obj1127, '_setHierarchicalLink')):
        self.obj1127._setHierarchicalLink(False)

      self.obj1127.GGLabel.setValue(9)
      self.obj1127.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(223.0,207.5,self.obj1127)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1127.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1127)
      self.obj1127.postAction( self.RHS.CREATE )

      self.obj1118.out_connections_.append(self.obj1120)
      self.obj1120.in_connections_.append(self.obj1118)
      self.obj1118.graphObject_.pendingConnections.append((self.obj1118.graphObject_.tag, self.obj1120.graphObject_.tag, [124.0, 86.0, 133.5, 123.5], 0, True))
      self.obj1118.out_connections_.append(self.obj1126)
      self.obj1126.in_connections_.append(self.obj1118)
      self.obj1118.graphObject_.pendingConnections.append((self.obj1118.graphObject_.tag, self.obj1126.graphObject_.tag, [124.0, 41.0, 208.0, 43.0], 0, True))
      self.obj1119.out_connections_.append(self.obj1127)
      self.obj1127.in_connections_.append(self.obj1119)
      self.obj1119.graphObject_.pendingConnections.append((self.obj1119.graphObject_.tag, self.obj1127.graphObject_.tag, [154.0, 210.0, 223.0, 207.5], 0, True))
      self.obj1120.out_connections_.append(self.obj1119)
      self.obj1119.in_connections_.append(self.obj1120)
      self.obj1120.graphObject_.pendingConnections.append((self.obj1120.graphObject_.tag, self.obj1119.graphObject_.tag, [143.0, 161.0, 133.5, 123.5], 0, True))
      self.obj1121.out_connections_.append(self.obj1125)
      self.obj1125.in_connections_.append(self.obj1121)
      self.obj1121.graphObject_.pendingConnections.append((self.obj1121.graphObject_.tag, self.obj1125.graphObject_.tag, [295.1869158878505, 135.5263157894737, 301.0934579439253, 168.26315789473685], 0, True))
      self.obj1122.out_connections_.append(self.obj1124)
      self.obj1124.in_connections_.append(self.obj1122)
      self.obj1122.graphObject_.pendingConnections.append((self.obj1122.graphObject_.tag, self.obj1124.graphObject_.tag, [304.0, 90.0, 298.78504672897196, 109.21052631578948], 0, True))
      self.obj1124.out_connections_.append(self.obj1121)
      self.obj1121.in_connections_.append(self.obj1124)
      self.obj1124.graphObject_.pendingConnections.append((self.obj1124.graphObject_.tag, self.obj1121.graphObject_.tag, [293.5700934579439, 128.42105263157896, 298.78504672897196, 109.21052631578948], 0, True))
      self.obj1125.out_connections_.append(self.obj1123)
      self.obj1123.in_connections_.append(self.obj1125)
      self.obj1125.graphObject_.pendingConnections.append((self.obj1125.graphObject_.tag, self.obj1123.graphObject_.tag, [307.0, 201.0, 301.0934579439253, 168.26315789473685], 0, True))
      self.obj1126.out_connections_.append(self.obj1122)
      self.obj1122.in_connections_.append(self.obj1126)
      self.obj1126.graphObject_.pendingConnections.append((self.obj1126.graphObject_.tag, self.obj1122.graphObject_.tag, [292.0, 45.0, 208.0, 43.0], 0, True))
      self.obj1127.out_connections_.append(self.obj1123)
      self.obj1123.in_connections_.append(self.obj1127)
      self.obj1127.graphObject_.pendingConnections.append((self.obj1127.graphObject_.tag, self.obj1123.graphObject_.tag, [292.0, 205.0, 223.0, 207.5], 2, 0))

   def condition(self, graphID, isograph, atom3i):
      print '======> Link Aux Condition'# _ Agent2Raw_GG_rule.py _
      aRg = self.getMatched ( graphID , self.LHS.nodeWithLabel(4) )
      nameARG = aRg.Name.getValue()
      g = self.getMatched ( graphID , self.LHS.nodeWithLabel(6) )
      # test if nameARG  end with name of Goal 
      print  nameARG +' END WITH '+g.Name.getValue()
      print nameARG.endswith( g.Name.getValue() )
      if nameARG.endswith( g.Name.getValue() ) and not hasattr(aRg,'LinkAux'): 
       return True
      else : 
       return False
      
      

   def action(self, graphID, isograph, atom3i):
      print '======> Link Aux Action'
      aRg = self.getMatched ( graphID , self.LHS.nodeWithLabel(4) )
      aRg.LinkAux = True 
      
      

