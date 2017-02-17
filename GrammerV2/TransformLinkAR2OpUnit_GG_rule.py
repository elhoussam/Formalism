# _ TransformLinkAR2OpUnit_GG_rule.py ____________________________________________________________________________
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
class TransformLinkAR2OpUnit_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 7)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_omacss(parent)

      self.obj1010=Agent(parent)
      self.obj1010.preAction( self.LHS.CREATE )
      self.obj1010.isGraphObjectVisual = True

      if(hasattr(self.obj1010, '_setHierarchicalLink')):
        self.obj1010._setHierarchicalLink(False)

      # price
      self.obj1010.price.setNone()

      # name
      self.obj1010.name.setValue('')
      self.obj1010.name.setNone()

      self.obj1010.GGLabel.setValue(1)
      self.obj1010.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(60.0,60.0,self.obj1010)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1010.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1010)
      self.obj1010.postAction( self.LHS.CREATE )

      self.obj1011=Role(parent)
      self.obj1011.preAction( self.LHS.CREATE )
      self.obj1011.isGraphObjectVisual = True

      if(hasattr(self.obj1011, '_setHierarchicalLink')):
        self.obj1011._setHierarchicalLink(False)

      # name
      self.obj1011.name.setValue('')
      self.obj1011.name.setNone()

      self.obj1011.GGLabel.setValue(2)
      self.obj1011.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(320.0,140.0,self.obj1011)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1011.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1011)
      self.obj1011.postAction( self.LHS.CREATE )

      self.obj1012=CapableOf(parent)
      self.obj1012.preAction( self.LHS.CREATE )
      self.obj1012.isGraphObjectVisual = True

      if(hasattr(self.obj1012, '_setHierarchicalLink')):
        self.obj1012._setHierarchicalLink(False)

      self.obj1012.GGLabel.setValue(3)
      self.obj1012.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(207.0,130.0,self.obj1012)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1012.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1012)
      self.obj1012.postAction( self.LHS.CREATE )

      self.obj1010.out_connections_.append(self.obj1012)
      self.obj1012.in_connections_.append(self.obj1010)
      self.obj1010.graphObject_.pendingConnections.append((self.obj1010.graphObject_.tag, self.obj1012.graphObject_.tag, [85.0, 122.0, 117.0, 172.0, 207.0, 130.0], 2, True))
      self.obj1012.out_connections_.append(self.obj1011)
      self.obj1011.in_connections_.append(self.obj1012)
      self.obj1012.graphObject_.pendingConnections.append((self.obj1012.graphObject_.tag, self.obj1011.graphObject_.tag, [344.0, 141.0, 297.0, 88.0, 207.0, 130.0], 2, True))

      self.RHS = ASG_omacss(parent)
      self.RHS.merge(ASG_pns2(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj1016=Agent(parent)
      self.obj1016.preAction( self.RHS.CREATE )
      self.obj1016.isGraphObjectVisual = True

      if(hasattr(self.obj1016, '_setHierarchicalLink')):
        self.obj1016._setHierarchicalLink(False)

      # price
      self.obj1016.price.setNone()

      # name
      self.obj1016.name.setValue('')
      self.obj1016.name.setNone()

      self.obj1016.GGLabel.setValue(1)
      self.obj1016.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(60.0,60.0,self.obj1016)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1016.graphObject_ = new_obj
      self.obj10160= AttrCalc()
      self.obj10160.Copy=ATOM3Boolean()
      self.obj10160.Copy.setValue(('Copy from LHS', 1))
      self.obj10160.Copy.config = 0
      self.obj10160.Specify=ATOM3Constraint()
      self.obj10160.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1016.GGset2Any['price']= self.obj10160
      self.obj10161= AttrCalc()
      self.obj10161.Copy=ATOM3Boolean()
      self.obj10161.Copy.setValue(('Copy from LHS', 1))
      self.obj10161.Copy.config = 0
      self.obj10161.Specify=ATOM3Constraint()
      self.obj10161.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1016.GGset2Any['name']= self.obj10161

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1016)
      self.obj1016.postAction( self.RHS.CREATE )

      self.obj1017=Role(parent)
      self.obj1017.preAction( self.RHS.CREATE )
      self.obj1017.isGraphObjectVisual = True

      if(hasattr(self.obj1017, '_setHierarchicalLink')):
        self.obj1017._setHierarchicalLink(False)

      # name
      self.obj1017.name.setValue('')
      self.obj1017.name.setNone()

      self.obj1017.GGLabel.setValue(2)
      self.obj1017.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(320.0,140.0,self.obj1017)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1017.graphObject_ = new_obj
      self.obj10170= AttrCalc()
      self.obj10170.Copy=ATOM3Boolean()
      self.obj10170.Copy.setValue(('Copy from LHS', 1))
      self.obj10170.Copy.config = 0
      self.obj10170.Specify=ATOM3Constraint()
      self.obj10170.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1017.GGset2Any['name']= self.obj10170

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1017)
      self.obj1017.postAction( self.RHS.CREATE )

      self.obj1018=CapableOf(parent)
      self.obj1018.preAction( self.RHS.CREATE )
      self.obj1018.isGraphObjectVisual = True

      if(hasattr(self.obj1018, '_setHierarchicalLink')):
        self.obj1018._setHierarchicalLink(False)

      self.obj1018.GGLabel.setValue(3)
      self.obj1018.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(207.0,130.0,self.obj1018)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1018.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1018)
      self.obj1018.postAction( self.RHS.CREATE )

      self.obj1019=operatingUnit(parent)
      self.obj1019.preAction( self.RHS.CREATE )
      self.obj1019.isGraphObjectVisual = True

      if(hasattr(self.obj1019, '_setHierarchicalLink')):
        self.obj1019._setHierarchicalLink(False)

      # name
      self.obj1019.name.setValue('')
      self.obj1019.name.setNone()

      self.obj1019.GGLabel.setValue(6)
      self.obj1019.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(220.0,80.0,self.obj1019)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1019.graphObject_ = new_obj
      self.obj10190= AttrCalc()
      self.obj10190.Copy=ATOM3Boolean()
      self.obj10190.Copy.setValue(('Copy from LHS', 0))
      self.obj10190.Copy.config = 0
      self.obj10190.Specify=ATOM3Constraint()
      self.obj10190.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()+\' \'+self.getMatched(graphID, self.LHS.nodeWithLabel(2)).name.getValue()\n\n\n\n'))
      self.obj1019.GGset2Any['name']= self.obj10190

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1019)
      self.obj1019.postAction( self.RHS.CREATE )

      self.obj1020=GenericGraphEdge(parent)
      self.obj1020.preAction( self.RHS.CREATE )
      self.obj1020.isGraphObjectVisual = True

      if(hasattr(self.obj1020, '_setHierarchicalLink')):
        self.obj1020._setHierarchicalLink(False)

      self.obj1020.GGLabel.setValue(7)
      self.obj1020.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(196.5,66.5,self.obj1020)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1020.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1020)
      self.obj1020.postAction( self.RHS.CREATE )

      self.obj1016.out_connections_.append(self.obj1018)
      self.obj1018.in_connections_.append(self.obj1016)
      self.obj1016.graphObject_.pendingConnections.append((self.obj1016.graphObject_.tag, self.obj1018.graphObject_.tag, [97.0, 122.0, 207.0, 130.0], 2, 0))
      self.obj1016.out_connections_.append(self.obj1020)
      self.obj1020.in_connections_.append(self.obj1016)
      self.obj1016.graphObject_.pendingConnections.append((self.obj1016.graphObject_.tag, self.obj1020.graphObject_.tag, [97.0, 122.0, 173.0, 79.0, 167.0, 103.0, 196.5, 66.5], 4, True))
      self.obj1018.out_connections_.append(self.obj1017)
      self.obj1017.in_connections_.append(self.obj1018)
      self.obj1018.graphObject_.pendingConnections.append((self.obj1018.graphObject_.tag, self.obj1017.graphObject_.tag, [351.0, 140.0, 207.0, 130.0], 2, 0))
      self.obj1020.out_connections_.append(self.obj1019)
      self.obj1019.in_connections_.append(self.obj1020)
      self.obj1020.graphObject_.pendingConnections.append((self.obj1020.graphObject_.tag, self.obj1019.graphObject_.tag, [261.32710280373834, 87.47368421052629, 220.0, 54.0, 261.0, 53.0, 196.5, 66.5], 4, True))

   def condition(self, graphID, isograph, atom3i):
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      node2 = self.getMatched(graphID, self.LHS.nodeWithLabel(2))
      return not(  hasattr(node, "LinkAR2OpUnit") and hasattr(node2, "LinkAR2OpUnit") )
      
      

   def action(self, graphID, isograph, atom3i):
      node = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) )
      node.LinkAR2OpUnit = True 
      node = self.getMatched ( graphID , self.LHS.nodeWithLabel(2) )
      node.LinkAR2OpUnit = True 
      
      

