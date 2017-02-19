# _ TransformGoal2Mat_GG_rule.py ____________________________________________________________________________
# File generated automatically by ATOM3. Graph Grammar Rule
# ___________________________________________________________________________________________
from GGrule import *
from CapableOf import *
from Goal import *
from ASG_omacss import *
from Agent import *
from Capabilitie import *
from Role import *
from requir import *
from achieve import *
from posses import *
from GenericGraphEdge import *
from intoProduct import *
from operatingUnit import *
from metarial import *
from rawMaterial import *
from fromMaterial import *
from fromRaw import *
from ASG_pns2 import *
from intoMaterial import *
from ASG_GenericGraph import *
from product import *
from GenericGraphNode import *
class TransformGoal2Mat_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 9)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_omacss(parent)

      self.obj228=Goal(parent)
      self.obj228.preAction( self.LHS.CREATE )
      self.obj228.isGraphObjectVisual = True

      if(hasattr(self.obj228, '_setHierarchicalLink')):
        self.obj228._setHierarchicalLink(False)

      # name
      self.obj228.name.setValue('')
      self.obj228.name.setNone()

      self.obj228.GGLabel.setValue(1)
      self.obj228.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(100.0,80.0,self.obj228)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj228.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj228)
      self.obj228.postAction( self.LHS.CREATE )


      self.RHS = ASG_omacss(parent)
      self.RHS.merge(ASG_pns2(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj232=Goal(parent)
      self.obj232.preAction( self.RHS.CREATE )
      self.obj232.isGraphObjectVisual = True

      if(hasattr(self.obj232, '_setHierarchicalLink')):
        self.obj232._setHierarchicalLink(False)

      # name
      self.obj232.name.setValue('')
      self.obj232.name.setNone()

      self.obj232.GGLabel.setValue(1)
      self.obj232.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(60.0,80.0,self.obj232)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj232.graphObject_ = new_obj
      self.obj2320= AttrCalc()
      self.obj2320.Copy=ATOM3Boolean()
      self.obj2320.Copy.setValue(('Copy from LHS', 1))
      self.obj2320.Copy.config = 0
      self.obj2320.Specify=ATOM3Constraint()
      self.obj2320.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj232.GGset2Any['name']= self.obj2320

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj232)
      self.obj232.postAction( self.RHS.CREATE )

      self.obj233=metarial(parent)
      self.obj233.preAction( self.RHS.CREATE )
      self.obj233.isGraphObjectVisual = True

      if(hasattr(self.obj233, '_setHierarchicalLink')):
        self.obj233._setHierarchicalLink(False)

      # Name
      self.obj233.Name.setValue('')
      self.obj233.Name.setNone()

      self.obj233.GGLabel.setValue(3)
      self.obj233.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(220.0,80.0,self.obj233)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj233.graphObject_ = new_obj
      self.obj2330= AttrCalc()
      self.obj2330.Copy=ATOM3Boolean()
      self.obj2330.Copy.setValue(('Copy from LHS', 0))
      self.obj2330.Copy.config = 0
      self.obj2330.Specify=ATOM3Constraint()
      self.obj2330.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()\n'))
      self.obj233.GGset2Any['Name']= self.obj2330

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj233)
      self.obj233.postAction( self.RHS.CREATE )

      self.obj234=GenericGraphEdge(parent)
      self.obj234.preAction( self.RHS.CREATE )
      self.obj234.isGraphObjectVisual = True

      if(hasattr(self.obj234, '_setHierarchicalLink')):
        self.obj234._setHierarchicalLink(False)

      self.obj234.GGLabel.setValue(4)
      self.obj234.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(162.0,127.0,self.obj234)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj234.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj234)
      self.obj234.postAction( self.RHS.CREATE )

      self.obj232.out_connections_.append(self.obj234)
      self.obj234.in_connections_.append(self.obj232)
      self.obj232.graphObject_.pendingConnections.append((self.obj232.graphObject_.tag, self.obj234.graphObject_.tag, [94.0, 130.0, 162.0, 127.0], 0, True))
      self.obj234.out_connections_.append(self.obj233)
      self.obj233.in_connections_.append(self.obj234)
      self.obj234.graphObject_.pendingConnections.append((self.obj234.graphObject_.tag, self.obj233.graphObject_.tag, [230.0, 124.0, 162.0, 127.0], 0, True))

   def condition(self, graphID, isograph, atom3i):
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      return not hasattr(node, "Goal2Mat")
      

   def action(self, graphID, isograph, atom3i):
      node = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) )
      node.Goal2Mat = True
      
      

