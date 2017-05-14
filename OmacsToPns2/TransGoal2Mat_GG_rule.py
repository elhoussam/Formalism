# _ TransGoal2Mat_GG_rule.py ____________________________________________________________________________
# File generated automatically by ATOM3. Graph Grammar Rule
# ___________________________________________________________________________________________
from GGrule import *
from Capabilitie import *
from rawMaterial import *
from Goal import *
from ASG_pns import *
from operatingUnit import *
from metarial import *
from product import *
from Agent import *
from fromMaterial import *
from CapableOf import *
from intoProduct import *
from Role import *
from fromRaw import *
from intoMaterial import *
from ASG_omacs import *
from require import *
from achieve import *
from posses import *
from GenericGraphEdge import *
from GenericGraphNode import *
from ASG_GenericGraph import *
class TransGoal2Mat_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 11)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_pns(parent)
      self.LHS.merge(ASG_omacs(parent))

      self.obj1638=Goal(parent)
      self.obj1638.preAction( self.LHS.CREATE )
      self.obj1638.isGraphObjectVisual = True

      if(hasattr(self.obj1638, '_setHierarchicalLink')):
        self.obj1638._setHierarchicalLink(False)

      # name
      self.obj1638.name.setValue('')
      self.obj1638.name.setNone()

      self.obj1638.GGLabel.setValue(1)
      self.obj1638.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(80.0,80.0,self.obj1638)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1638.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1638)
      self.obj1638.postAction( self.LHS.CREATE )


      self.RHS = ASG_pns(parent)
      self.RHS.merge(ASG_omacs(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj1642=metarial(parent)
      self.obj1642.preAction( self.RHS.CREATE )
      self.obj1642.isGraphObjectVisual = True

      if(hasattr(self.obj1642, '_setHierarchicalLink')):
        self.obj1642._setHierarchicalLink(False)

      # MaxFlow
      self.obj1642.MaxFlow.setValue(999999)

      # price
      self.obj1642.price.setValue(0)

      # Name
      self.obj1642.Name.setValue('')
      self.obj1642.Name.setNone()

      # ReqFlow
      self.obj1642.ReqFlow.setValue(0)

      self.obj1642.GGLabel.setValue(2)
      self.obj1642.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(300.0,60.0,self.obj1642)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1642.graphObject_ = new_obj
      self.obj16420= AttrCalc()
      self.obj16420.Copy=ATOM3Boolean()
      self.obj16420.Copy.setValue(('Copy from LHS', 1))
      self.obj16420.Copy.config = 0
      self.obj16420.Specify=ATOM3Constraint()
      self.obj16420.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1642.GGset2Any['MaxFlow']= self.obj16420
      self.obj16421= AttrCalc()
      self.obj16421.Copy=ATOM3Boolean()
      self.obj16421.Copy.setValue(('Copy from LHS', 0))
      self.obj16421.Copy.config = 0
      self.obj16421.Specify=ATOM3Constraint()
      self.obj16421.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()\n'))
      self.obj1642.GGset2Any['Name']= self.obj16421
      self.obj16422= AttrCalc()
      self.obj16422.Copy=ATOM3Boolean()
      self.obj16422.Copy.setValue(('Copy from LHS', 1))
      self.obj16422.Copy.config = 0
      self.obj16422.Specify=ATOM3Constraint()
      self.obj16422.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1642.GGset2Any['ReqFlow']= self.obj16422

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1642)
      self.obj1642.postAction( self.RHS.CREATE )

      self.obj1643=Goal(parent)
      self.obj1643.preAction( self.RHS.CREATE )
      self.obj1643.isGraphObjectVisual = True

      if(hasattr(self.obj1643, '_setHierarchicalLink')):
        self.obj1643._setHierarchicalLink(False)

      # name
      self.obj1643.name.setValue('')
      self.obj1643.name.setNone()

      self.obj1643.GGLabel.setValue(1)
      self.obj1643.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(80.0,80.0,self.obj1643)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1643.graphObject_ = new_obj
      self.obj16430= AttrCalc()
      self.obj16430.Copy=ATOM3Boolean()
      self.obj16430.Copy.setValue(('Copy from LHS', 1))
      self.obj16430.Copy.config = 0
      self.obj16430.Specify=ATOM3Constraint()
      self.obj16430.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1643.GGset2Any['name']= self.obj16430

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1643)
      self.obj1643.postAction( self.RHS.CREATE )

      self.obj1644=GenericGraphEdge(parent)
      self.obj1644.preAction( self.RHS.CREATE )
      self.obj1644.isGraphObjectVisual = True

      if(hasattr(self.obj1644, '_setHierarchicalLink')):
        self.obj1644._setHierarchicalLink(False)

      self.obj1644.GGLabel.setValue(4)
      self.obj1644.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(209.5,91.5,self.obj1644)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1644.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1644)
      self.obj1644.postAction( self.RHS.CREATE )

      self.obj1643.out_connections_.append(self.obj1644)
      self.obj1644.in_connections_.append(self.obj1643)
      self.obj1643.graphObject_.pendingConnections.append((self.obj1643.graphObject_.tag, self.obj1644.graphObject_.tag, [113.0, 81.0, 209.5, 91.5], 0, True))
      self.obj1644.out_connections_.append(self.obj1642)
      self.obj1642.in_connections_.append(self.obj1644)
      self.obj1644.graphObject_.pendingConnections.append((self.obj1644.graphObject_.tag, self.obj1642.graphObject_.tag, [306.0, 102.0, 209.5, 91.5], 0, True))

   def condition(self, graphID, isograph, atom3i):
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      return not hasattr(node, "Goal2Mat")
      

   def action(self, graphID, isograph, atom3i):
      node = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) )
      node.Goal2Mat = True
      
      

