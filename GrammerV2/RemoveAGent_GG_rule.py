# _ RemoveAGent_GG_rule.py ____________________________________________________________________________
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
class RemoveAGent_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 22)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_omacss(parent)
      self.LHS.merge(ASG_pns2(parent))
      self.LHS.merge(ASG_GenericGraph(parent))

      self.obj1180=Agent(parent)
      self.obj1180.preAction( self.LHS.CREATE )
      self.obj1180.isGraphObjectVisual = True

      if(hasattr(self.obj1180, '_setHierarchicalLink')):
        self.obj1180._setHierarchicalLink(False)

      # price
      self.obj1180.price.setNone()

      # name
      self.obj1180.name.setValue('')
      self.obj1180.name.setNone()

      self.obj1180.GGLabel.setValue(1)
      self.obj1180.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(100.0,60.0,self.obj1180)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1180.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1180)
      self.obj1180.postAction( self.LHS.CREATE )

      self.obj1181=rawMaterial(parent)
      self.obj1181.preAction( self.LHS.CREATE )
      self.obj1181.isGraphObjectVisual = True

      if(hasattr(self.obj1181, '_setHierarchicalLink')):
        self.obj1181._setHierarchicalLink(False)

      # Name
      self.obj1181.Name.setValue('')
      self.obj1181.Name.setNone()

      self.obj1181.GGLabel.setValue(2)
      self.obj1181.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(280.0,20.0,self.obj1181)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1181.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1181)
      self.obj1181.postAction( self.LHS.CREATE )

      self.obj1182=operatingUnit(parent)
      self.obj1182.preAction( self.LHS.CREATE )
      self.obj1182.isGraphObjectVisual = True

      if(hasattr(self.obj1182, '_setHierarchicalLink')):
        self.obj1182._setHierarchicalLink(False)

      # name
      self.obj1182.name.setValue('')
      self.obj1182.name.setNone()

      self.obj1182.GGLabel.setValue(3)
      self.obj1182.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(280.0,140.0,self.obj1182)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1182.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1182)
      self.obj1182.postAction( self.LHS.CREATE )

      self.obj1183=fromRaw(parent)
      self.obj1183.preAction( self.LHS.CREATE )
      self.obj1183.isGraphObjectVisual = True

      if(hasattr(self.obj1183, '_setHierarchicalLink')):
        self.obj1183._setHierarchicalLink(False)

      # rate
      self.obj1183.rate.setNone()

      self.obj1183.GGLabel.setValue(6)
      self.obj1183.graphClass_= graph_fromRaw
      if parent.genGraphics:
         new_obj = graph_fromRaw(298.785046729,110.710526316,self.obj1183)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1183.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1183)
      self.obj1183.postAction( self.LHS.CREATE )

      self.obj1184=GenericGraphEdge(parent)
      self.obj1184.preAction( self.LHS.CREATE )
      self.obj1184.isGraphObjectVisual = True

      if(hasattr(self.obj1184, '_setHierarchicalLink')):
        self.obj1184._setHierarchicalLink(False)

      self.obj1184.GGLabel.setValue(4)
      self.obj1184.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(220.5,97.5,self.obj1184)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1184.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1184)
      self.obj1184.postAction( self.LHS.CREATE )

      self.obj1185=GenericGraphEdge(parent)
      self.obj1185.preAction( self.LHS.CREATE )
      self.obj1185.isGraphObjectVisual = True

      if(hasattr(self.obj1185, '_setHierarchicalLink')):
        self.obj1185._setHierarchicalLink(False)

      self.obj1185.GGLabel.setValue(5)
      self.obj1185.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(215.285046729,135.210526316,self.obj1185)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1185.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1185)
      self.obj1185.postAction( self.LHS.CREATE )

      self.obj1180.out_connections_.append(self.obj1184)
      self.obj1184.in_connections_.append(self.obj1180)
      self.obj1180.graphObject_.pendingConnections.append((self.obj1180.graphObject_.tag, self.obj1184.graphObject_.tag, [137.0, 122.0, 220.5, 97.5], 0, True))
      self.obj1180.out_connections_.append(self.obj1185)
      self.obj1185.in_connections_.append(self.obj1180)
      self.obj1180.graphObject_.pendingConnections.append((self.obj1180.graphObject_.tag, self.obj1185.graphObject_.tag, [137.0, 122.0, 215.285046729, 135.210526316], 2, 0))
      self.obj1181.out_connections_.append(self.obj1183)
      self.obj1183.in_connections_.append(self.obj1181)
      self.obj1181.graphObject_.pendingConnections.append((self.obj1181.graphObject_.tag, self.obj1183.graphObject_.tag, [304.0, 73.0, 298.78504672897196, 110.71052631578948], 0, True))
      self.obj1183.out_connections_.append(self.obj1182)
      self.obj1182.in_connections_.append(self.obj1183)
      self.obj1183.graphObject_.pendingConnections.append((self.obj1183.graphObject_.tag, self.obj1182.graphObject_.tag, [293.5700934579439, 148.42105263157896, 298.78504672897196, 110.71052631578948], 0, True))
      self.obj1184.out_connections_.append(self.obj1181)
      self.obj1181.in_connections_.append(self.obj1184)
      self.obj1184.graphObject_.pendingConnections.append((self.obj1184.graphObject_.tag, self.obj1181.graphObject_.tag, [304.0, 73.0, 220.5, 97.5], 0, True))
      self.obj1185.out_connections_.append(self.obj1182)
      self.obj1182.in_connections_.append(self.obj1185)
      self.obj1185.graphObject_.pendingConnections.append((self.obj1185.graphObject_.tag, self.obj1182.graphObject_.tag, [294.5700934579439, 148.42105263157896, 215.285046729, 135.210526316], 2, 0))

      self.RHS = ASG_omacss(parent)
      self.RHS.merge(ASG_pns2(parent))

      self.obj1188=rawMaterial(parent)
      self.obj1188.preAction( self.RHS.CREATE )
      self.obj1188.isGraphObjectVisual = True

      if(hasattr(self.obj1188, '_setHierarchicalLink')):
        self.obj1188._setHierarchicalLink(False)

      # Name
      self.obj1188.Name.setValue('')
      self.obj1188.Name.setNone()

      self.obj1188.GGLabel.setValue(2)
      self.obj1188.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(200.0,20.0,self.obj1188)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1188.graphObject_ = new_obj
      self.obj11880= AttrCalc()
      self.obj11880.Copy=ATOM3Boolean()
      self.obj11880.Copy.setValue(('Copy from LHS', 1))
      self.obj11880.Copy.config = 0
      self.obj11880.Specify=ATOM3Constraint()
      self.obj11880.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1188.GGset2Any['Name']= self.obj11880

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1188)
      self.obj1188.postAction( self.RHS.CREATE )

      self.obj1189=operatingUnit(parent)
      self.obj1189.preAction( self.RHS.CREATE )
      self.obj1189.isGraphObjectVisual = True

      if(hasattr(self.obj1189, '_setHierarchicalLink')):
        self.obj1189._setHierarchicalLink(False)

      # name
      self.obj1189.name.setValue('')
      self.obj1189.name.setNone()

      self.obj1189.GGLabel.setValue(3)
      self.obj1189.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(200.0,160.0,self.obj1189)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1189.graphObject_ = new_obj
      self.obj11890= AttrCalc()
      self.obj11890.Copy=ATOM3Boolean()
      self.obj11890.Copy.setValue(('Copy from LHS', 1))
      self.obj11890.Copy.config = 0
      self.obj11890.Specify=ATOM3Constraint()
      self.obj11890.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1189.GGset2Any['name']= self.obj11890

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1189)
      self.obj1189.postAction( self.RHS.CREATE )

      self.obj1190=fromRaw(parent)
      self.obj1190.preAction( self.RHS.CREATE )
      self.obj1190.isGraphObjectVisual = True

      if(hasattr(self.obj1190, '_setHierarchicalLink')):
        self.obj1190._setHierarchicalLink(False)

      # rate
      self.obj1190.rate.setValue(0.0)

      self.obj1190.GGLabel.setValue(6)
      self.obj1190.graphClass_= graph_fromRaw
      if parent.genGraphics:
         new_obj = graph_fromRaw(228.785046729,120.710526316,self.obj1190)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1190.graphObject_ = new_obj
      self.obj11900= AttrCalc()
      self.obj11900.Copy=ATOM3Boolean()
      self.obj11900.Copy.setValue(('Copy from LHS', 1))
      self.obj11900.Copy.config = 0
      self.obj11900.Specify=ATOM3Constraint()
      self.obj11900.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1190.GGset2Any['rate']= self.obj11900

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1190)
      self.obj1190.postAction( self.RHS.CREATE )

      self.obj1188.out_connections_.append(self.obj1190)
      self.obj1190.in_connections_.append(self.obj1188)
      self.obj1188.graphObject_.pendingConnections.append((self.obj1188.graphObject_.tag, self.obj1190.graphObject_.tag, [224.0, 73.0, 228.78504672897196, 120.71052631578948], 0, True))
      self.obj1190.out_connections_.append(self.obj1189)
      self.obj1189.in_connections_.append(self.obj1190)
      self.obj1190.graphObject_.pendingConnections.append((self.obj1190.graphObject_.tag, self.obj1189.graphObject_.tag, [213.57009345794393, 168.42105263157896, 228.78504672897196, 120.71052631578948], 0, True))

   def condition(self, graphID, isograph, atom3i):
      return self.graphRewritingSystem.finalStat > 20 
      

   def action(self, graphID, isograph, atom3i):
      pass

