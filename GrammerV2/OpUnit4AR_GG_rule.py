# _ OpUnit4AR_GG_rule.py ____________________________________________________________________________
# File generated automatically by ATOM3. Graph Grammar Rule
# ___________________________________________________________________________________________
from GGrule import *
from Capabilitie import *
from rawMaterial import *
from Goal import *
from intoProduct import *
from operatingUnit import *
from metarial import *
from product import *
from Agent import *
from fromMaterial import *
from CapableOf import *
from Role import *
from fromRaw import *
from ASG_pns2 import *
from intoMaterial import *
from ASG_omacs import *
from require import *
from achieve import *
from posses import *
from GenericGraphEdge import *
from GenericGraphNode import *
from ASG_GenericGraph import *
class OpUnit4AR_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 5)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_pns2(parent)
      self.LHS.merge(ASG_omacs(parent))

      self.obj70=CapableOf(parent)
      self.obj70.preAction( self.LHS.CREATE )
      self.obj70.isGraphObjectVisual = True

      if(hasattr(self.obj70, '_setHierarchicalLink')):
        self.obj70._setHierarchicalLink(False)

      self.obj70.GGLabel.setValue(3)
      self.obj70.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(204.0,100.5,self.obj70)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj70.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj70)
      self.obj70.postAction( self.LHS.CREATE )

      self.obj71=Agent(parent)
      self.obj71.preAction( self.LHS.CREATE )
      self.obj71.isGraphObjectVisual = True

      if(hasattr(self.obj71, '_setHierarchicalLink')):
        self.obj71._setHierarchicalLink(False)

      # price
      self.obj71.price.setValue(0)

      # name
      self.obj71.name.setValue('')
      self.obj71.name.setNone()

      self.obj71.GGLabel.setValue(1)
      self.obj71.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(40.0,0.0,self.obj71)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj71.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj71)
      self.obj71.postAction( self.LHS.CREATE )

      self.obj72=Role(parent)
      self.obj72.preAction( self.LHS.CREATE )
      self.obj72.isGraphObjectVisual = True

      if(hasattr(self.obj72, '_setHierarchicalLink')):
        self.obj72._setHierarchicalLink(False)

      # name
      self.obj72.name.setValue('')
      self.obj72.name.setNone()

      self.obj72.GGLabel.setValue(2)
      self.obj72.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(300.0,120.0,self.obj72)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj72.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj72)
      self.obj72.postAction( self.LHS.CREATE )

      self.obj70.out_connections_.append(self.obj72)
      self.obj72.in_connections_.append(self.obj70)
      self.obj70.graphObject_.pendingConnections.append((self.obj70.graphObject_.tag, self.obj72.graphObject_.tag, [330.0, 120.0, 247.0, 55.0, 204.0, 100.5], 2, True))
      self.obj71.out_connections_.append(self.obj70)
      self.obj70.in_connections_.append(self.obj71)
      self.obj71.graphObject_.pendingConnections.append((self.obj71.graphObject_.tag, self.obj70.graphObject_.tag, [72.0, 86.0, 161.0, 146.0, 204.0, 100.5], 2, True))

      self.RHS = ASG_pns2(parent)
      self.RHS.merge(ASG_omacs(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj76=operatingUnit(parent)
      self.obj76.preAction( self.RHS.CREATE )
      self.obj76.isGraphObjectVisual = True

      if(hasattr(self.obj76, '_setHierarchicalLink')):
        self.obj76._setHierarchicalLink(False)

      self.obj76.GGLabel.setValue(5)
      self.obj76.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(280.0,40.0,self.obj76)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj76.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj76)
      self.obj76.postAction( self.RHS.CREATE )

      self.obj77=CapableOf(parent)
      self.obj77.preAction( self.RHS.CREATE )
      self.obj77.isGraphObjectVisual = True

      if(hasattr(self.obj77, '_setHierarchicalLink')):
        self.obj77._setHierarchicalLink(False)

      self.obj77.GGLabel.setValue(3)
      self.obj77.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(204.0,100.5,self.obj77)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj77.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj77)
      self.obj77.postAction( self.RHS.CREATE )

      self.obj78=Agent(parent)
      self.obj78.preAction( self.RHS.CREATE )
      self.obj78.isGraphObjectVisual = True

      if(hasattr(self.obj78, '_setHierarchicalLink')):
        self.obj78._setHierarchicalLink(False)

      # price
      self.obj78.price.setValue(0)

      # name
      self.obj78.name.setValue('')
      self.obj78.name.setNone()

      self.obj78.GGLabel.setValue(1)
      self.obj78.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(40.0,0.0,self.obj78)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj78.graphObject_ = new_obj
      self.obj780= AttrCalc()
      self.obj780.Copy=ATOM3Boolean()
      self.obj780.Copy.setValue(('Copy from LHS', 1))
      self.obj780.Copy.config = 0
      self.obj780.Specify=ATOM3Constraint()
      self.obj780.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj78.GGset2Any['price']= self.obj780
      self.obj781= AttrCalc()
      self.obj781.Copy=ATOM3Boolean()
      self.obj781.Copy.setValue(('Copy from LHS', 1))
      self.obj781.Copy.config = 0
      self.obj781.Specify=ATOM3Constraint()
      self.obj781.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj78.GGset2Any['name']= self.obj781

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj78)
      self.obj78.postAction( self.RHS.CREATE )

      self.obj79=Role(parent)
      self.obj79.preAction( self.RHS.CREATE )
      self.obj79.isGraphObjectVisual = True

      if(hasattr(self.obj79, '_setHierarchicalLink')):
        self.obj79._setHierarchicalLink(False)

      # name
      self.obj79.name.setValue('')
      self.obj79.name.setNone()

      self.obj79.GGLabel.setValue(2)
      self.obj79.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(300.0,120.0,self.obj79)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj79.graphObject_ = new_obj
      self.obj790= AttrCalc()
      self.obj790.Copy=ATOM3Boolean()
      self.obj790.Copy.setValue(('Copy from LHS', 1))
      self.obj790.Copy.config = 0
      self.obj790.Specify=ATOM3Constraint()
      self.obj790.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj79.GGset2Any['name']= self.obj790

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj79)
      self.obj79.postAction( self.RHS.CREATE )

      self.obj80=GenericGraphEdge(parent)
      self.obj80.preAction( self.RHS.CREATE )
      self.obj80.isGraphObjectVisual = True

      if(hasattr(self.obj80, '_setHierarchicalLink')):
        self.obj80._setHierarchicalLink(False)

      self.obj80.GGLabel.setValue(6)
      self.obj80.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(240.75,24.25,self.obj80)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj80.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj80)
      self.obj80.postAction( self.RHS.CREATE )

      self.obj77.out_connections_.append(self.obj79)
      self.obj79.in_connections_.append(self.obj77)
      self.obj77.graphObject_.pendingConnections.append((self.obj77.graphObject_.tag, self.obj79.graphObject_.tag, [331.0, 120.0, 204.0, 100.5], 2, 0))
      self.obj78.out_connections_.append(self.obj77)
      self.obj77.in_connections_.append(self.obj78)
      self.obj78.graphObject_.pendingConnections.append((self.obj78.graphObject_.tag, self.obj77.graphObject_.tag, [74.0, 86.0, 204.0, 100.5], 2, 0))
      self.obj78.out_connections_.append(self.obj80)
      self.obj80.in_connections_.append(self.obj78)
      self.obj78.graphObject_.pendingConnections.append((self.obj78.graphObject_.tag, self.obj80.graphObject_.tag, [74.0, 86.0, 200.5, 40.0, 173.0, 72.0, 240.75, 24.25], 4, True))
      self.obj80.out_connections_.append(self.obj76)
      self.obj76.in_connections_.append(self.obj80)
      self.obj80.graphObject_.pendingConnections.append((self.obj80.graphObject_.tag, self.obj76.graphObject_.tag, [347.0, 41.0, 281.0, 8.5, 334.0, 9.0, 240.75, 24.25], 4, True))

   def condition(self, graphID, isograph, atom3i):
      # If you want to apply this rule at most once on asingle host graph node, 
      # then uncomment the next two lines. Change the default GG label (1) if needed.
      
      # Make sure to enable the ACTION code as well
      # And to use the same label & unique name in the ACTION
      # WARNING: _uniqueName2 is not guaranteed to be unique (so change it, be safe!)
      
      #node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      #return not hasattr(node, "_uniqueName2")
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      node2 = self.getMatched(graphID, self.LHS.nodeWithLabel(2))
      return not(  hasattr(node, "_rule_1_executed_already") and hasattr(node2, "_rule_1_executed_already") )
      
      

   def action(self, graphID, isograph, atom3i):
      # If you want to apply this rule at most once on asingle host graph node, 
      # then uncomment the next two lines. Change the default GG label (1) if needed.
      
      # Make sure to enable the CONDITION code as well
      # And to use the same label & unique name in the ACTION
      # WARNING: _uniqueName2 is not guaranteed to be unique (so change it, be safe!)
      
      #node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      #node._uniqueName2 = True
      node = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) )
      node._rule_1_executed_already = True 
      node = self.getMatched ( graphID , self.LHS.nodeWithLabel(2) )
      node._rule_1_executed_already = True 
      
      

