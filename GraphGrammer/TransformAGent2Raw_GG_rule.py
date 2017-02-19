# _ TransformAGent2Raw_GG_rule.py ____________________________________________________________________________
# File generated automatically by ATOM3. Graph Grammar Rule
# ___________________________________________________________________________________________
from GGrule import *
from CapableOf import *
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
from product import *
from achieve import *
from posses import *
from GenericGraphEdge import *
from ASG_GenericGraph import *
from GenericGraphNode import *
class TransformAGent2Raw_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 5)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_omacss(parent)
      self.LHS.merge(ASG_pns2(parent))

      self.obj198=Agent(parent)
      self.obj198.preAction( self.LHS.CREATE )
      self.obj198.isGraphObjectVisual = True

      if(hasattr(self.obj198, '_setHierarchicalLink')):
        self.obj198._setHierarchicalLink(False)

      # price
      self.obj198.price.setValue(0)

      # name
      self.obj198.name.setValue('')
      self.obj198.name.setNone()

      self.obj198.GGLabel.setValue(1)
      self.obj198.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(60.0,20.0,self.obj198)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj198.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj198)
      self.obj198.postAction( self.LHS.CREATE )

      self.obj199=Role(parent)
      self.obj199.preAction( self.LHS.CREATE )
      self.obj199.isGraphObjectVisual = True

      if(hasattr(self.obj199, '_setHierarchicalLink')):
        self.obj199._setHierarchicalLink(False)

      # name
      self.obj199.name.setValue('')
      self.obj199.name.setNone()

      self.obj199.GGLabel.setValue(2)
      self.obj199.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(240.0,100.0,self.obj199)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj199.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj199)
      self.obj199.postAction( self.LHS.CREATE )

      self.obj200=CapableOf(parent)
      self.obj200.preAction( self.LHS.CREATE )
      self.obj200.isGraphObjectVisual = True

      if(hasattr(self.obj200, '_setHierarchicalLink')):
        self.obj200._setHierarchicalLink(False)

      self.obj200.GGLabel.setValue(3)
      self.obj200.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(170.0,88.5,self.obj200)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj200.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj200)
      self.obj200.postAction( self.LHS.CREATE )

      self.obj198.out_connections_.append(self.obj200)
      self.obj200.in_connections_.append(self.obj198)
      self.obj198.graphObject_.pendingConnections.append((self.obj198.graphObject_.tag, self.obj200.graphObject_.tag, [85.0, 82.0, 109.0, 127.0, 170.0, 88.5], 2, True))
      self.obj200.out_connections_.append(self.obj199)
      self.obj199.in_connections_.append(self.obj200)
      self.obj200.graphObject_.pendingConnections.append((self.obj200.graphObject_.tag, self.obj199.graphObject_.tag, [264.0, 101.0, 231.0, 50.0, 170.0, 88.5], 2, True))

      self.RHS = ASG_omacss(parent)
      self.RHS.merge(ASG_pns2(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj204=Agent(parent)
      self.obj204.preAction( self.RHS.CREATE )
      self.obj204.isGraphObjectVisual = True

      if(hasattr(self.obj204, '_setHierarchicalLink')):
        self.obj204._setHierarchicalLink(False)

      # price
      self.obj204.price.setValue(0)

      # name
      self.obj204.name.setValue('')
      self.obj204.name.setNone()

      self.obj204.GGLabel.setValue(1)
      self.obj204.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(60.0,20.0,self.obj204)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj204.graphObject_ = new_obj
      self.obj2040= AttrCalc()
      self.obj2040.Copy=ATOM3Boolean()
      self.obj2040.Copy.setValue(('Copy from LHS', 1))
      self.obj2040.Copy.config = 0
      self.obj2040.Specify=ATOM3Constraint()
      self.obj2040.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj204.GGset2Any['price']= self.obj2040
      self.obj2041= AttrCalc()
      self.obj2041.Copy=ATOM3Boolean()
      self.obj2041.Copy.setValue(('Copy from LHS', 1))
      self.obj2041.Copy.config = 0
      self.obj2041.Specify=ATOM3Constraint()
      self.obj2041.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj204.GGset2Any['name']= self.obj2041

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj204)
      self.obj204.postAction( self.RHS.CREATE )

      self.obj205=Role(parent)
      self.obj205.preAction( self.RHS.CREATE )
      self.obj205.isGraphObjectVisual = True

      if(hasattr(self.obj205, '_setHierarchicalLink')):
        self.obj205._setHierarchicalLink(False)

      # name
      self.obj205.name.setValue('')
      self.obj205.name.setNone()

      self.obj205.GGLabel.setValue(2)
      self.obj205.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(240.0,100.0,self.obj205)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj205.graphObject_ = new_obj
      self.obj2050= AttrCalc()
      self.obj2050.Copy=ATOM3Boolean()
      self.obj2050.Copy.setValue(('Copy from LHS', 1))
      self.obj2050.Copy.config = 0
      self.obj2050.Specify=ATOM3Constraint()
      self.obj2050.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj205.GGset2Any['name']= self.obj2050

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj205)
      self.obj205.postAction( self.RHS.CREATE )

      self.obj206=CapableOf(parent)
      self.obj206.preAction( self.RHS.CREATE )
      self.obj206.isGraphObjectVisual = True

      if(hasattr(self.obj206, '_setHierarchicalLink')):
        self.obj206._setHierarchicalLink(False)

      self.obj206.GGLabel.setValue(3)
      self.obj206.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(170.0,88.5,self.obj206)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj206.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj206)
      self.obj206.postAction( self.RHS.CREATE )

      self.obj207=rawMaterial(parent)
      self.obj207.preAction( self.RHS.CREATE )
      self.obj207.isGraphObjectVisual = True

      if(hasattr(self.obj207, '_setHierarchicalLink')):
        self.obj207._setHierarchicalLink(False)

      # Name
      self.obj207.Name.setValue('')
      self.obj207.Name.setNone()

      self.obj207.GGLabel.setValue(5)
      self.obj207.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(20.0,140.0,self.obj207)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj207.graphObject_ = new_obj
      self.obj2070= AttrCalc()
      self.obj2070.Copy=ATOM3Boolean()
      self.obj2070.Copy.setValue(('Copy from LHS', 0))
      self.obj2070.Copy.config = 0
      self.obj2070.Specify=ATOM3Constraint()
      self.obj2070.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()\n'))
      self.obj207.GGset2Any['Name']= self.obj2070

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj207)
      self.obj207.postAction( self.RHS.CREATE )

      self.obj208=GenericGraphEdge(parent)
      self.obj208.preAction( self.RHS.CREATE )
      self.obj208.isGraphObjectVisual = True

      if(hasattr(self.obj208, '_setHierarchicalLink')):
        self.obj208._setHierarchicalLink(False)

      self.obj208.GGLabel.setValue(6)
      self.obj208.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(93.5,165.0,self.obj208)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj208.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj208)
      self.obj208.postAction( self.RHS.CREATE )

      self.obj204.out_connections_.append(self.obj206)
      self.obj206.in_connections_.append(self.obj204)
      self.obj204.graphObject_.pendingConnections.append((self.obj204.graphObject_.tag, self.obj206.graphObject_.tag, [97.0, 82.0, 170.0, 88.5], 2, 0))
      self.obj204.out_connections_.append(self.obj208)
      self.obj208.in_connections_.append(self.obj204)
      self.obj204.graphObject_.pendingConnections.append((self.obj204.graphObject_.tag, self.obj208.graphObject_.tag, [97.0, 82.0, 67.0, 166.0, 93.5, 165.0], 2, True))
      self.obj206.out_connections_.append(self.obj205)
      self.obj205.in_connections_.append(self.obj206)
      self.obj206.graphObject_.pendingConnections.append((self.obj206.graphObject_.tag, self.obj205.graphObject_.tag, [271.0, 100.0, 170.0, 88.5], 2, 0))
      self.obj208.out_connections_.append(self.obj207)
      self.obj207.in_connections_.append(self.obj208)
      self.obj208.graphObject_.pendingConnections.append((self.obj208.graphObject_.tag, self.obj207.graphObject_.tag, [44.0, 193.0, 120.0, 164.0, 93.5, 165.0], 2, True))

   def condition(self, graphID, isograph, atom3i):
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      return not hasattr(node, "Agent2Raw")
      

   def action(self, graphID, isograph, atom3i):
      node = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) )
      node.Agent2Raw = True 
      

