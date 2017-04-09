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
      GGrule.__init__(self, 9)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_pns(parent)
      self.LHS.merge(ASG_omacs(parent))

      self.obj165=Goal(parent)
      self.obj165.preAction( self.LHS.CREATE )
      self.obj165.isGraphObjectVisual = True

      if(hasattr(self.obj165, '_setHierarchicalLink')):
        self.obj165._setHierarchicalLink(False)

      # name
      self.obj165.name.setValue('')
      self.obj165.name.setNone()

      self.obj165.GGLabel.setValue(1)
      self.obj165.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(80.0,80.0,self.obj165)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj165.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj165)
      self.obj165.postAction( self.LHS.CREATE )


      self.RHS = ASG_pns(parent)
      self.RHS.merge(ASG_omacs(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj169=metarial(parent)
      self.obj169.preAction( self.RHS.CREATE )
      self.obj169.isGraphObjectVisual = True

      if(hasattr(self.obj169, '_setHierarchicalLink')):
        self.obj169._setHierarchicalLink(False)

      # MaxFlow
      self.obj169.MaxFlow.setValue(999999)

      # price
      self.obj169.price.setValue(0)

      # Name
      self.obj169.Name.setValue('')
      self.obj169.Name.setNone()

      # ReqFlow
      self.obj169.ReqFlow.setValue(0)

      self.obj169.GGLabel.setValue(2)
      self.obj169.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(300.0,60.0,self.obj169)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj169.graphObject_ = new_obj
      self.obj1690= AttrCalc()
      self.obj1690.Copy=ATOM3Boolean()
      self.obj1690.Copy.setValue(('Copy from LHS', 1))
      self.obj1690.Copy.config = 0
      self.obj1690.Specify=ATOM3Constraint()
      self.obj1690.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj169.GGset2Any['MaxFlow']= self.obj1690
      self.obj1691= AttrCalc()
      self.obj1691.Copy=ATOM3Boolean()
      self.obj1691.Copy.setValue(('Copy from LHS', 0))
      self.obj1691.Copy.config = 0
      self.obj1691.Specify=ATOM3Constraint()
      self.obj1691.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()\n'))
      self.obj169.GGset2Any['Name']= self.obj1691
      self.obj1692= AttrCalc()
      self.obj1692.Copy=ATOM3Boolean()
      self.obj1692.Copy.setValue(('Copy from LHS', 1))
      self.obj1692.Copy.config = 0
      self.obj1692.Specify=ATOM3Constraint()
      self.obj1692.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj169.GGset2Any['ReqFlow']= self.obj1692

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj169)
      self.obj169.postAction( self.RHS.CREATE )

      self.obj170=Goal(parent)
      self.obj170.preAction( self.RHS.CREATE )
      self.obj170.isGraphObjectVisual = True

      if(hasattr(self.obj170, '_setHierarchicalLink')):
        self.obj170._setHierarchicalLink(False)

      # name
      self.obj170.name.setValue('')
      self.obj170.name.setNone()

      self.obj170.GGLabel.setValue(1)
      self.obj170.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(80.0,80.0,self.obj170)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj170.graphObject_ = new_obj
      self.obj1700= AttrCalc()
      self.obj1700.Copy=ATOM3Boolean()
      self.obj1700.Copy.setValue(('Copy from LHS', 1))
      self.obj1700.Copy.config = 0
      self.obj1700.Specify=ATOM3Constraint()
      self.obj1700.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj170.GGset2Any['name']= self.obj1700

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj170)
      self.obj170.postAction( self.RHS.CREATE )

      self.obj171=GenericGraphEdge(parent)
      self.obj171.preAction( self.RHS.CREATE )
      self.obj171.isGraphObjectVisual = True

      if(hasattr(self.obj171, '_setHierarchicalLink')):
        self.obj171._setHierarchicalLink(False)

      self.obj171.GGLabel.setValue(4)
      self.obj171.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(209.5,91.5,self.obj171)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj171.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj171)
      self.obj171.postAction( self.RHS.CREATE )

      self.obj170.out_connections_.append(self.obj171)
      self.obj171.in_connections_.append(self.obj170)
      self.obj170.graphObject_.pendingConnections.append((self.obj170.graphObject_.tag, self.obj171.graphObject_.tag, [113.0, 81.0, 209.5, 91.5], 0, True))
      self.obj171.out_connections_.append(self.obj169)
      self.obj169.in_connections_.append(self.obj171)
      self.obj171.graphObject_.pendingConnections.append((self.obj171.graphObject_.tag, self.obj169.graphObject_.tag, [306.0, 102.0, 209.5, 91.5], 0, True))

   def condition(self, graphID, isograph, atom3i):
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      return not hasattr(node, "Goal2Mat")
      

   def action(self, graphID, isograph, atom3i):
      node = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) )
      node.Goal2Mat = True
      
      

