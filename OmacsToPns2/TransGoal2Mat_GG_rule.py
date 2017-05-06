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

      self.obj637=Goal(parent)
      self.obj637.preAction( self.LHS.CREATE )
      self.obj637.isGraphObjectVisual = True

      if(hasattr(self.obj637, '_setHierarchicalLink')):
        self.obj637._setHierarchicalLink(False)

      # name
      self.obj637.name.setValue('')
      self.obj637.name.setNone()

      self.obj637.GGLabel.setValue(1)
      self.obj637.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(80.0,80.0,self.obj637)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj637.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj637)
      self.obj637.postAction( self.LHS.CREATE )


      self.RHS = ASG_pns(parent)
      self.RHS.merge(ASG_omacs(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj641=metarial(parent)
      self.obj641.preAction( self.RHS.CREATE )
      self.obj641.isGraphObjectVisual = True

      if(hasattr(self.obj641, '_setHierarchicalLink')):
        self.obj641._setHierarchicalLink(False)

      # MaxFlow
      self.obj641.MaxFlow.setValue(999999)

      # price
      self.obj641.price.setValue(0)

      # Name
      self.obj641.Name.setValue('')
      self.obj641.Name.setNone()

      # ReqFlow
      self.obj641.ReqFlow.setValue(0)

      self.obj641.GGLabel.setValue(2)
      self.obj641.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(300.0,60.0,self.obj641)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj641.graphObject_ = new_obj
      self.obj6410= AttrCalc()
      self.obj6410.Copy=ATOM3Boolean()
      self.obj6410.Copy.setValue(('Copy from LHS', 1))
      self.obj6410.Copy.config = 0
      self.obj6410.Specify=ATOM3Constraint()
      self.obj6410.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj641.GGset2Any['MaxFlow']= self.obj6410
      self.obj6411= AttrCalc()
      self.obj6411.Copy=ATOM3Boolean()
      self.obj6411.Copy.setValue(('Copy from LHS', 0))
      self.obj6411.Copy.config = 0
      self.obj6411.Specify=ATOM3Constraint()
      self.obj6411.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()\n'))
      self.obj641.GGset2Any['Name']= self.obj6411
      self.obj6412= AttrCalc()
      self.obj6412.Copy=ATOM3Boolean()
      self.obj6412.Copy.setValue(('Copy from LHS', 1))
      self.obj6412.Copy.config = 0
      self.obj6412.Specify=ATOM3Constraint()
      self.obj6412.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj641.GGset2Any['ReqFlow']= self.obj6412

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj641)
      self.obj641.postAction( self.RHS.CREATE )

      self.obj642=Goal(parent)
      self.obj642.preAction( self.RHS.CREATE )
      self.obj642.isGraphObjectVisual = True

      if(hasattr(self.obj642, '_setHierarchicalLink')):
        self.obj642._setHierarchicalLink(False)

      # name
      self.obj642.name.setValue('')
      self.obj642.name.setNone()

      self.obj642.GGLabel.setValue(1)
      self.obj642.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(80.0,80.0,self.obj642)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj642.graphObject_ = new_obj
      self.obj6420= AttrCalc()
      self.obj6420.Copy=ATOM3Boolean()
      self.obj6420.Copy.setValue(('Copy from LHS', 1))
      self.obj6420.Copy.config = 0
      self.obj6420.Specify=ATOM3Constraint()
      self.obj6420.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj642.GGset2Any['name']= self.obj6420

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj642)
      self.obj642.postAction( self.RHS.CREATE )

      self.obj643=GenericGraphEdge(parent)
      self.obj643.preAction( self.RHS.CREATE )
      self.obj643.isGraphObjectVisual = True

      if(hasattr(self.obj643, '_setHierarchicalLink')):
        self.obj643._setHierarchicalLink(False)

      self.obj643.GGLabel.setValue(4)
      self.obj643.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(209.5,91.5,self.obj643)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj643.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj643)
      self.obj643.postAction( self.RHS.CREATE )

      self.obj642.out_connections_.append(self.obj643)
      self.obj643.in_connections_.append(self.obj642)
      self.obj642.graphObject_.pendingConnections.append((self.obj642.graphObject_.tag, self.obj643.graphObject_.tag, [113.0, 81.0, 209.5, 91.5], 0, True))
      self.obj643.out_connections_.append(self.obj641)
      self.obj641.in_connections_.append(self.obj643)
      self.obj643.graphObject_.pendingConnections.append((self.obj643.graphObject_.tag, self.obj641.graphObject_.tag, [306.0, 102.0, 209.5, 91.5], 0, True))

   def condition(self, graphID, isograph, atom3i):
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      return not hasattr(node, "Goal2Mat")
      

   def action(self, graphID, isograph, atom3i):
      node = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) )
      node.Goal2Mat = True
      
      

