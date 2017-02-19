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

      self.obj213=Agent(parent)
      self.obj213.preAction( self.LHS.CREATE )
      self.obj213.isGraphObjectVisual = True

      if(hasattr(self.obj213, '_setHierarchicalLink')):
        self.obj213._setHierarchicalLink(False)

      # price
      self.obj213.price.setNone()

      # name
      self.obj213.name.setValue('')
      self.obj213.name.setNone()

      self.obj213.GGLabel.setValue(1)
      self.obj213.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(60.0,60.0,self.obj213)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj213.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj213)
      self.obj213.postAction( self.LHS.CREATE )

      self.obj214=Role(parent)
      self.obj214.preAction( self.LHS.CREATE )
      self.obj214.isGraphObjectVisual = True

      if(hasattr(self.obj214, '_setHierarchicalLink')):
        self.obj214._setHierarchicalLink(False)

      # name
      self.obj214.name.setValue('')
      self.obj214.name.setNone()

      self.obj214.GGLabel.setValue(2)
      self.obj214.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(320.0,140.0,self.obj214)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj214.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj214)
      self.obj214.postAction( self.LHS.CREATE )

      self.obj215=CapableOf(parent)
      self.obj215.preAction( self.LHS.CREATE )
      self.obj215.isGraphObjectVisual = True

      if(hasattr(self.obj215, '_setHierarchicalLink')):
        self.obj215._setHierarchicalLink(False)

      self.obj215.GGLabel.setValue(3)
      self.obj215.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(207.0,130.0,self.obj215)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj215.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj215)
      self.obj215.postAction( self.LHS.CREATE )

      self.obj213.out_connections_.append(self.obj215)
      self.obj215.in_connections_.append(self.obj213)
      self.obj213.graphObject_.pendingConnections.append((self.obj213.graphObject_.tag, self.obj215.graphObject_.tag, [85.0, 122.0, 117.0, 172.0, 207.0, 130.0], 2, True))
      self.obj215.out_connections_.append(self.obj214)
      self.obj214.in_connections_.append(self.obj215)
      self.obj215.graphObject_.pendingConnections.append((self.obj215.graphObject_.tag, self.obj214.graphObject_.tag, [344.0, 141.0, 297.0, 88.0, 207.0, 130.0], 2, True))

      self.RHS = ASG_omacss(parent)
      self.RHS.merge(ASG_pns2(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj219=Agent(parent)
      self.obj219.preAction( self.RHS.CREATE )
      self.obj219.isGraphObjectVisual = True

      if(hasattr(self.obj219, '_setHierarchicalLink')):
        self.obj219._setHierarchicalLink(False)

      # price
      self.obj219.price.setNone()

      # name
      self.obj219.name.setValue('')
      self.obj219.name.setNone()

      self.obj219.GGLabel.setValue(1)
      self.obj219.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(60.0,60.0,self.obj219)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj219.graphObject_ = new_obj
      self.obj2190= AttrCalc()
      self.obj2190.Copy=ATOM3Boolean()
      self.obj2190.Copy.setValue(('Copy from LHS', 1))
      self.obj2190.Copy.config = 0
      self.obj2190.Specify=ATOM3Constraint()
      self.obj2190.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj219.GGset2Any['price']= self.obj2190
      self.obj2191= AttrCalc()
      self.obj2191.Copy=ATOM3Boolean()
      self.obj2191.Copy.setValue(('Copy from LHS', 1))
      self.obj2191.Copy.config = 0
      self.obj2191.Specify=ATOM3Constraint()
      self.obj2191.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj219.GGset2Any['name']= self.obj2191

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj219)
      self.obj219.postAction( self.RHS.CREATE )

      self.obj220=Role(parent)
      self.obj220.preAction( self.RHS.CREATE )
      self.obj220.isGraphObjectVisual = True

      if(hasattr(self.obj220, '_setHierarchicalLink')):
        self.obj220._setHierarchicalLink(False)

      # name
      self.obj220.name.setValue('')
      self.obj220.name.setNone()

      self.obj220.GGLabel.setValue(2)
      self.obj220.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(320.0,140.0,self.obj220)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj220.graphObject_ = new_obj
      self.obj2200= AttrCalc()
      self.obj2200.Copy=ATOM3Boolean()
      self.obj2200.Copy.setValue(('Copy from LHS', 1))
      self.obj2200.Copy.config = 0
      self.obj2200.Specify=ATOM3Constraint()
      self.obj2200.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj220.GGset2Any['name']= self.obj2200

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj220)
      self.obj220.postAction( self.RHS.CREATE )

      self.obj221=CapableOf(parent)
      self.obj221.preAction( self.RHS.CREATE )
      self.obj221.isGraphObjectVisual = True

      if(hasattr(self.obj221, '_setHierarchicalLink')):
        self.obj221._setHierarchicalLink(False)

      self.obj221.GGLabel.setValue(3)
      self.obj221.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(207.0,130.0,self.obj221)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj221.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj221)
      self.obj221.postAction( self.RHS.CREATE )

      self.obj222=operatingUnit(parent)
      self.obj222.preAction( self.RHS.CREATE )
      self.obj222.isGraphObjectVisual = True

      if(hasattr(self.obj222, '_setHierarchicalLink')):
        self.obj222._setHierarchicalLink(False)

      # name
      self.obj222.name.setValue('')
      self.obj222.name.setNone()

      self.obj222.GGLabel.setValue(6)
      self.obj222.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(220.0,80.0,self.obj222)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj222.graphObject_ = new_obj
      self.obj2220= AttrCalc()
      self.obj2220.Copy=ATOM3Boolean()
      self.obj2220.Copy.setValue(('Copy from LHS', 0))
      self.obj2220.Copy.config = 0
      self.obj2220.Specify=ATOM3Constraint()
      self.obj2220.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()+\' \'+self.getMatched(graphID, self.LHS.nodeWithLabel(2)).name.getValue()\n\n\n\n\n\n\n'))
      self.obj222.GGset2Any['name']= self.obj2220

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj222)
      self.obj222.postAction( self.RHS.CREATE )

      self.obj223=GenericGraphEdge(parent)
      self.obj223.preAction( self.RHS.CREATE )
      self.obj223.isGraphObjectVisual = True

      if(hasattr(self.obj223, '_setHierarchicalLink')):
        self.obj223._setHierarchicalLink(False)

      self.obj223.GGLabel.setValue(7)
      self.obj223.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(196.5,66.5,self.obj223)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj223.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj223)
      self.obj223.postAction( self.RHS.CREATE )

      self.obj219.out_connections_.append(self.obj221)
      self.obj221.in_connections_.append(self.obj219)
      self.obj219.graphObject_.pendingConnections.append((self.obj219.graphObject_.tag, self.obj221.graphObject_.tag, [97.0, 122.0, 207.0, 130.0], 2, 0))
      self.obj219.out_connections_.append(self.obj223)
      self.obj223.in_connections_.append(self.obj219)
      self.obj219.graphObject_.pendingConnections.append((self.obj219.graphObject_.tag, self.obj223.graphObject_.tag, [97.0, 122.0, 173.0, 79.0, 167.0, 103.0, 196.5, 66.5], 4, True))
      self.obj221.out_connections_.append(self.obj220)
      self.obj220.in_connections_.append(self.obj221)
      self.obj221.graphObject_.pendingConnections.append((self.obj221.graphObject_.tag, self.obj220.graphObject_.tag, [351.0, 140.0, 207.0, 130.0], 2, 0))
      self.obj223.out_connections_.append(self.obj222)
      self.obj222.in_connections_.append(self.obj223)
      self.obj223.graphObject_.pendingConnections.append((self.obj223.graphObject_.tag, self.obj222.graphObject_.tag, [261.32710280373834, 87.47368421052629, 220.0, 54.0, 261.0, 53.0, 196.5, 66.5], 4, True))

   def condition(self, graphID, isograph, atom3i):
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      node2 = self.getMatched(graphID, self.LHS.nodeWithLabel(2))
      return not(  hasattr(node, "LinkAR2OpUnit") and hasattr(node2, "LinkAR2OpUnit") )
      
      

   def action(self, graphID, isograph, atom3i):
      node = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) )
      node.LinkAR2OpUnit = True 
      node = self.getMatched ( graphID , self.LHS.nodeWithLabel(2) )
      node.LinkAR2OpUnit = True 
      
      

