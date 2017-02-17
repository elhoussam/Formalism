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

      self.obj995=Agent(parent)
      self.obj995.preAction( self.LHS.CREATE )
      self.obj995.isGraphObjectVisual = True

      if(hasattr(self.obj995, '_setHierarchicalLink')):
        self.obj995._setHierarchicalLink(False)

      # price
      self.obj995.price.setValue(0)

      # name
      self.obj995.name.setValue('')
      self.obj995.name.setNone()

      self.obj995.GGLabel.setValue(1)
      self.obj995.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(60.0,20.0,self.obj995)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj995.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj995)
      self.obj995.postAction( self.LHS.CREATE )

      self.obj996=Role(parent)
      self.obj996.preAction( self.LHS.CREATE )
      self.obj996.isGraphObjectVisual = True

      if(hasattr(self.obj996, '_setHierarchicalLink')):
        self.obj996._setHierarchicalLink(False)

      # name
      self.obj996.name.setValue('')
      self.obj996.name.setNone()

      self.obj996.GGLabel.setValue(2)
      self.obj996.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(240.0,100.0,self.obj996)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj996.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj996)
      self.obj996.postAction( self.LHS.CREATE )

      self.obj997=CapableOf(parent)
      self.obj997.preAction( self.LHS.CREATE )
      self.obj997.isGraphObjectVisual = True

      if(hasattr(self.obj997, '_setHierarchicalLink')):
        self.obj997._setHierarchicalLink(False)

      self.obj997.GGLabel.setValue(3)
      self.obj997.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(170.0,88.5,self.obj997)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj997.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj997)
      self.obj997.postAction( self.LHS.CREATE )

      self.obj995.out_connections_.append(self.obj997)
      self.obj997.in_connections_.append(self.obj995)
      self.obj995.graphObject_.pendingConnections.append((self.obj995.graphObject_.tag, self.obj997.graphObject_.tag, [85.0, 82.0, 109.0, 127.0, 170.0, 88.5], 2, True))
      self.obj997.out_connections_.append(self.obj996)
      self.obj996.in_connections_.append(self.obj997)
      self.obj997.graphObject_.pendingConnections.append((self.obj997.graphObject_.tag, self.obj996.graphObject_.tag, [264.0, 101.0, 231.0, 50.0, 170.0, 88.5], 2, True))

      self.RHS = ASG_omacss(parent)
      self.RHS.merge(ASG_pns2(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj1001=Agent(parent)
      self.obj1001.preAction( self.RHS.CREATE )
      self.obj1001.isGraphObjectVisual = True

      if(hasattr(self.obj1001, '_setHierarchicalLink')):
        self.obj1001._setHierarchicalLink(False)

      # price
      self.obj1001.price.setValue(0)

      # name
      self.obj1001.name.setValue('')
      self.obj1001.name.setNone()

      self.obj1001.GGLabel.setValue(1)
      self.obj1001.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(60.0,20.0,self.obj1001)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1001.graphObject_ = new_obj
      self.obj10010= AttrCalc()
      self.obj10010.Copy=ATOM3Boolean()
      self.obj10010.Copy.setValue(('Copy from LHS', 1))
      self.obj10010.Copy.config = 0
      self.obj10010.Specify=ATOM3Constraint()
      self.obj10010.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1001.GGset2Any['price']= self.obj10010
      self.obj10011= AttrCalc()
      self.obj10011.Copy=ATOM3Boolean()
      self.obj10011.Copy.setValue(('Copy from LHS', 1))
      self.obj10011.Copy.config = 0
      self.obj10011.Specify=ATOM3Constraint()
      self.obj10011.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1001.GGset2Any['name']= self.obj10011

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1001)
      self.obj1001.postAction( self.RHS.CREATE )

      self.obj1002=Role(parent)
      self.obj1002.preAction( self.RHS.CREATE )
      self.obj1002.isGraphObjectVisual = True

      if(hasattr(self.obj1002, '_setHierarchicalLink')):
        self.obj1002._setHierarchicalLink(False)

      # name
      self.obj1002.name.setValue('')
      self.obj1002.name.setNone()

      self.obj1002.GGLabel.setValue(2)
      self.obj1002.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(240.0,100.0,self.obj1002)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1002.graphObject_ = new_obj
      self.obj10020= AttrCalc()
      self.obj10020.Copy=ATOM3Boolean()
      self.obj10020.Copy.setValue(('Copy from LHS', 1))
      self.obj10020.Copy.config = 0
      self.obj10020.Specify=ATOM3Constraint()
      self.obj10020.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1002.GGset2Any['name']= self.obj10020

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1002)
      self.obj1002.postAction( self.RHS.CREATE )

      self.obj1003=CapableOf(parent)
      self.obj1003.preAction( self.RHS.CREATE )
      self.obj1003.isGraphObjectVisual = True

      if(hasattr(self.obj1003, '_setHierarchicalLink')):
        self.obj1003._setHierarchicalLink(False)

      self.obj1003.GGLabel.setValue(3)
      self.obj1003.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(170.0,88.5,self.obj1003)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1003.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1003)
      self.obj1003.postAction( self.RHS.CREATE )

      self.obj1004=rawMaterial(parent)
      self.obj1004.preAction( self.RHS.CREATE )
      self.obj1004.isGraphObjectVisual = True

      if(hasattr(self.obj1004, '_setHierarchicalLink')):
        self.obj1004._setHierarchicalLink(False)

      # Name
      self.obj1004.Name.setValue('')
      self.obj1004.Name.setNone()

      self.obj1004.GGLabel.setValue(5)
      self.obj1004.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(20.0,140.0,self.obj1004)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1004.graphObject_ = new_obj
      self.obj10040= AttrCalc()
      self.obj10040.Copy=ATOM3Boolean()
      self.obj10040.Copy.setValue(('Copy from LHS', 0))
      self.obj10040.Copy.config = 0
      self.obj10040.Specify=ATOM3Constraint()
      self.obj10040.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()\n'))
      self.obj1004.GGset2Any['Name']= self.obj10040

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1004)
      self.obj1004.postAction( self.RHS.CREATE )

      self.obj1005=GenericGraphEdge(parent)
      self.obj1005.preAction( self.RHS.CREATE )
      self.obj1005.isGraphObjectVisual = True

      if(hasattr(self.obj1005, '_setHierarchicalLink')):
        self.obj1005._setHierarchicalLink(False)

      self.obj1005.GGLabel.setValue(6)
      self.obj1005.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(93.5,165.0,self.obj1005)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1005.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1005)
      self.obj1005.postAction( self.RHS.CREATE )

      self.obj1001.out_connections_.append(self.obj1003)
      self.obj1003.in_connections_.append(self.obj1001)
      self.obj1001.graphObject_.pendingConnections.append((self.obj1001.graphObject_.tag, self.obj1003.graphObject_.tag, [97.0, 82.0, 170.0, 88.5], 2, 0))
      self.obj1001.out_connections_.append(self.obj1005)
      self.obj1005.in_connections_.append(self.obj1001)
      self.obj1001.graphObject_.pendingConnections.append((self.obj1001.graphObject_.tag, self.obj1005.graphObject_.tag, [97.0, 82.0, 67.0, 166.0, 93.5, 165.0], 2, True))
      self.obj1003.out_connections_.append(self.obj1002)
      self.obj1002.in_connections_.append(self.obj1003)
      self.obj1003.graphObject_.pendingConnections.append((self.obj1003.graphObject_.tag, self.obj1002.graphObject_.tag, [271.0, 100.0, 170.0, 88.5], 2, 0))
      self.obj1005.out_connections_.append(self.obj1004)
      self.obj1004.in_connections_.append(self.obj1005)
      self.obj1005.graphObject_.pendingConnections.append((self.obj1005.graphObject_.tag, self.obj1004.graphObject_.tag, [44.0, 193.0, 120.0, 164.0, 93.5, 165.0], 2, True))

   def condition(self, graphID, isograph, atom3i):
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      return not hasattr(node, "Agent2Raw")
      

   def action(self, graphID, isograph, atom3i):
      node = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) )
      node.Agent2Raw = True 
      

