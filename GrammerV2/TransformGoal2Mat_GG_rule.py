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

      self.obj1025=Goal(parent)
      self.obj1025.preAction( self.LHS.CREATE )
      self.obj1025.isGraphObjectVisual = True

      if(hasattr(self.obj1025, '_setHierarchicalLink')):
        self.obj1025._setHierarchicalLink(False)

      # name
      self.obj1025.name.setValue('')
      self.obj1025.name.setNone()

      self.obj1025.GGLabel.setValue(1)
      self.obj1025.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(100.0,80.0,self.obj1025)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1025.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1025)
      self.obj1025.postAction( self.LHS.CREATE )


      self.RHS = ASG_omacss(parent)
      self.RHS.merge(ASG_pns2(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj1029=Goal(parent)
      self.obj1029.preAction( self.RHS.CREATE )
      self.obj1029.isGraphObjectVisual = True

      if(hasattr(self.obj1029, '_setHierarchicalLink')):
        self.obj1029._setHierarchicalLink(False)

      # name
      self.obj1029.name.setValue('')
      self.obj1029.name.setNone()

      self.obj1029.GGLabel.setValue(1)
      self.obj1029.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(60.0,80.0,self.obj1029)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1029.graphObject_ = new_obj
      self.obj10290= AttrCalc()
      self.obj10290.Copy=ATOM3Boolean()
      self.obj10290.Copy.setValue(('Copy from LHS', 1))
      self.obj10290.Copy.config = 0
      self.obj10290.Specify=ATOM3Constraint()
      self.obj10290.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1029.GGset2Any['name']= self.obj10290

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1029)
      self.obj1029.postAction( self.RHS.CREATE )

      self.obj1030=metarial(parent)
      self.obj1030.preAction( self.RHS.CREATE )
      self.obj1030.isGraphObjectVisual = True

      if(hasattr(self.obj1030, '_setHierarchicalLink')):
        self.obj1030._setHierarchicalLink(False)

      # Name
      self.obj1030.Name.setValue('')
      self.obj1030.Name.setNone()

      self.obj1030.GGLabel.setValue(3)
      self.obj1030.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(220.0,80.0,self.obj1030)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1030.graphObject_ = new_obj
      self.obj10300= AttrCalc()
      self.obj10300.Copy=ATOM3Boolean()
      self.obj10300.Copy.setValue(('Copy from LHS', 0))
      self.obj10300.Copy.config = 0
      self.obj10300.Specify=ATOM3Constraint()
      self.obj10300.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()\n'))
      self.obj1030.GGset2Any['Name']= self.obj10300

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1030)
      self.obj1030.postAction( self.RHS.CREATE )

      self.obj1031=GenericGraphEdge(parent)
      self.obj1031.preAction( self.RHS.CREATE )
      self.obj1031.isGraphObjectVisual = True

      if(hasattr(self.obj1031, '_setHierarchicalLink')):
        self.obj1031._setHierarchicalLink(False)

      self.obj1031.GGLabel.setValue(4)
      self.obj1031.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(162.0,127.0,self.obj1031)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1031.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1031)
      self.obj1031.postAction( self.RHS.CREATE )

      self.obj1029.out_connections_.append(self.obj1031)
      self.obj1031.in_connections_.append(self.obj1029)
      self.obj1029.graphObject_.pendingConnections.append((self.obj1029.graphObject_.tag, self.obj1031.graphObject_.tag, [94.0, 130.0, 162.0, 127.0], 0, True))
      self.obj1031.out_connections_.append(self.obj1030)
      self.obj1030.in_connections_.append(self.obj1031)
      self.obj1031.graphObject_.pendingConnections.append((self.obj1031.graphObject_.tag, self.obj1030.graphObject_.tag, [230.0, 124.0, 162.0, 127.0], 0, True))

   def condition(self, graphID, isograph, atom3i):
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      return not hasattr(node, "Goal2Mat")
      

   def action(self, graphID, isograph, atom3i):
      node = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) )
      node.Goal2Mat = True
      
      

