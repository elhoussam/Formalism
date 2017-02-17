# _ RemoveRolez_GG_rule.py ____________________________________________________________________________
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
class RemoveRolez_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 24)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_omacss(parent)
      self.LHS.merge(ASG_pns2(parent))
      self.LHS.merge(ASG_GenericGraph(parent))

      self.obj1203=Role(parent)
      self.obj1203.preAction( self.LHS.CREATE )
      self.obj1203.isGraphObjectVisual = True

      if(hasattr(self.obj1203, '_setHierarchicalLink')):
        self.obj1203._setHierarchicalLink(False)

      # name
      self.obj1203.name.setValue('')
      self.obj1203.name.setNone()

      self.obj1203.GGLabel.setValue(1)
      self.obj1203.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(60.0,60.0,self.obj1203)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1203.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1203)
      self.obj1203.postAction( self.LHS.CREATE )

      self.obj1204=operatingUnit(parent)
      self.obj1204.preAction( self.LHS.CREATE )
      self.obj1204.isGraphObjectVisual = True

      if(hasattr(self.obj1204, '_setHierarchicalLink')):
        self.obj1204._setHierarchicalLink(False)

      # name
      self.obj1204.name.setValue('')
      self.obj1204.name.setNone()

      self.obj1204.GGLabel.setValue(2)
      self.obj1204.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(260.0,160.0,self.obj1204)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1204.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1204)
      self.obj1204.postAction( self.LHS.CREATE )

      self.obj1205=metarial(parent)
      self.obj1205.preAction( self.LHS.CREATE )
      self.obj1205.isGraphObjectVisual = True

      if(hasattr(self.obj1205, '_setHierarchicalLink')):
        self.obj1205._setHierarchicalLink(False)

      # Name
      self.obj1205.Name.setValue('')
      self.obj1205.Name.setNone()

      self.obj1205.GGLabel.setValue(5)
      self.obj1205.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(260.0,60.0,self.obj1205)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1205.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1205)
      self.obj1205.postAction( self.LHS.CREATE )

      self.obj1206=fromMaterial(parent)
      self.obj1206.preAction( self.LHS.CREATE )
      self.obj1206.isGraphObjectVisual = True

      if(hasattr(self.obj1206, '_setHierarchicalLink')):
        self.obj1206._setHierarchicalLink(False)

      # rate
      self.obj1206.rate.setNone()

      self.obj1206.GGLabel.setValue(3)
      self.obj1206.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(288.785046729,139.210526316,self.obj1206)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1206.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1206)
      self.obj1206.postAction( self.LHS.CREATE )

      self.obj1205.out_connections_.append(self.obj1206)
      self.obj1206.in_connections_.append(self.obj1205)
      self.obj1205.graphObject_.pendingConnections.append((self.obj1205.graphObject_.tag, self.obj1206.graphObject_.tag, [284.0, 110.0, 288.78504672897196, 139.21052631578948], 0, True))
      self.obj1206.out_connections_.append(self.obj1204)
      self.obj1204.in_connections_.append(self.obj1206)
      self.obj1206.graphObject_.pendingConnections.append((self.obj1206.graphObject_.tag, self.obj1204.graphObject_.tag, [273.5700934579439, 168.42105263157896, 288.78504672897196, 139.21052631578948], 0, True))

      self.RHS = ASG_omacss(parent)
      self.RHS.merge(ASG_pns2(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj1210=operatingUnit(parent)
      self.obj1210.preAction( self.RHS.CREATE )
      self.obj1210.isGraphObjectVisual = True

      if(hasattr(self.obj1210, '_setHierarchicalLink')):
        self.obj1210._setHierarchicalLink(False)

      # name
      self.obj1210.name.setValue('')
      self.obj1210.name.setNone()

      self.obj1210.GGLabel.setValue(2)
      self.obj1210.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(240.0,160.0,self.obj1210)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1210.graphObject_ = new_obj
      self.obj12100= AttrCalc()
      self.obj12100.Copy=ATOM3Boolean()
      self.obj12100.Copy.setValue(('Copy from LHS', 1))
      self.obj12100.Copy.config = 0
      self.obj12100.Specify=ATOM3Constraint()
      self.obj12100.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1210.GGset2Any['name']= self.obj12100

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1210)
      self.obj1210.postAction( self.RHS.CREATE )

      self.obj1211=metarial(parent)
      self.obj1211.preAction( self.RHS.CREATE )
      self.obj1211.isGraphObjectVisual = True

      if(hasattr(self.obj1211, '_setHierarchicalLink')):
        self.obj1211._setHierarchicalLink(False)

      # Name
      self.obj1211.Name.setValue('')
      self.obj1211.Name.setNone()

      self.obj1211.GGLabel.setValue(5)
      self.obj1211.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(240.0,40.0,self.obj1211)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1211.graphObject_ = new_obj
      self.obj12110= AttrCalc()
      self.obj12110.Copy=ATOM3Boolean()
      self.obj12110.Copy.setValue(('Copy from LHS', 1))
      self.obj12110.Copy.config = 0
      self.obj12110.Specify=ATOM3Constraint()
      self.obj12110.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1211.GGset2Any['Name']= self.obj12110

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1211)
      self.obj1211.postAction( self.RHS.CREATE )

      self.obj1212=fromMaterial(parent)
      self.obj1212.preAction( self.RHS.CREATE )
      self.obj1212.isGraphObjectVisual = True

      if(hasattr(self.obj1212, '_setHierarchicalLink')):
        self.obj1212._setHierarchicalLink(False)

      # rate
      self.obj1212.rate.setValue(0.0)

      self.obj1212.GGLabel.setValue(3)
      self.obj1212.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(258.785046729,129.210526316,self.obj1212)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1212.graphObject_ = new_obj
      self.obj12120= AttrCalc()
      self.obj12120.Copy=ATOM3Boolean()
      self.obj12120.Copy.setValue(('Copy from LHS', 1))
      self.obj12120.Copy.config = 0
      self.obj12120.Specify=ATOM3Constraint()
      self.obj12120.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1212.GGset2Any['rate']= self.obj12120

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1212)
      self.obj1212.postAction( self.RHS.CREATE )

      self.obj1211.out_connections_.append(self.obj1212)
      self.obj1212.in_connections_.append(self.obj1211)
      self.obj1211.graphObject_.pendingConnections.append((self.obj1211.graphObject_.tag, self.obj1212.graphObject_.tag, [264.0, 90.0, 258.78504672897196, 129.21052631578948], 0, True))
      self.obj1212.out_connections_.append(self.obj1210)
      self.obj1210.in_connections_.append(self.obj1212)
      self.obj1212.graphObject_.pendingConnections.append((self.obj1212.graphObject_.tag, self.obj1210.graphObject_.tag, [253.57009345794393, 168.42105263157896, 258.78504672897196, 129.21052631578948], 0, True))

   def condition(self, graphID, isograph, atom3i):
      return self.graphRewritingSystem.finalStat > 20 
      
      

   def action(self, graphID, isograph, atom3i):
      pass

