# _ TransLinkAR2OpUnit_GG_rule.py ____________________________________________________________________________
# File generated automatically by ATOM3. Graph Grammar Rule
# ___________________________________________________________________________________________
from GGrule import *
from CapableOf import *
from Goal import *
from require import *
from Agent import *
from Capabilitie import *
from Role import *
from ASG_omacs import *
from achieve import *
from posses import *
from GenericGraphEdge import *
from ASG_pns import *
from metarial import *
from GenericGraphNode import *
from rawMaterial import *
from fromMaterial import *
from intoProduct import *
from fromRaw import *
from ASG_GenericGraph import *
from intoMaterial import *
from product import *
from operatingUnit import *
class TransLinkAR2OpUnit_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 10)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_omacs(parent)

      self.obj1622=Agent(parent)
      self.obj1622.preAction( self.LHS.CREATE )
      self.obj1622.isGraphObjectVisual = True

      if(hasattr(self.obj1622, '_setHierarchicalLink')):
        self.obj1622._setHierarchicalLink(False)

      # price
      self.obj1622.price.setNone()

      # name
      self.obj1622.name.setValue('')
      self.obj1622.name.setNone()

      self.obj1622.GGLabel.setValue(1)
      self.obj1622.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(60.0,40.0,self.obj1622)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1622.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1622)
      self.obj1622.postAction( self.LHS.CREATE )

      self.obj1623=Role(parent)
      self.obj1623.preAction( self.LHS.CREATE )
      self.obj1623.isGraphObjectVisual = True

      if(hasattr(self.obj1623, '_setHierarchicalLink')):
        self.obj1623._setHierarchicalLink(False)

      # name
      self.obj1623.name.setValue('')
      self.obj1623.name.setNone()

      self.obj1623.GGLabel.setValue(2)
      self.obj1623.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(320.0,220.0,self.obj1623)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1623.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1623)
      self.obj1623.postAction( self.LHS.CREATE )

      self.obj1624=CapableOf(parent)
      self.obj1624.preAction( self.LHS.CREATE )
      self.obj1624.isGraphObjectVisual = True

      if(hasattr(self.obj1624, '_setHierarchicalLink')):
        self.obj1624._setHierarchicalLink(False)

      # rate
      self.obj1624.rate.setNone()

      self.obj1624.GGLabel.setValue(3)
      self.obj1624.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(230.0,173.0,self.obj1624)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1624.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1624)
      self.obj1624.postAction( self.LHS.CREATE )

      self.obj1622.out_connections_.append(self.obj1624)
      self.obj1624.in_connections_.append(self.obj1622)
      self.obj1622.graphObject_.pendingConnections.append((self.obj1622.graphObject_.tag, self.obj1624.graphObject_.tag, [85.0, 102.0, 117.0, 188.0, 230.0, 173.0], 2, True))
      self.obj1624.out_connections_.append(self.obj1623)
      self.obj1623.in_connections_.append(self.obj1624)
      self.obj1624.graphObject_.pendingConnections.append((self.obj1624.graphObject_.tag, self.obj1623.graphObject_.tag, [344.0, 221.0, 343.0, 158.0, 230.0, 173.0], 2, True))

      self.RHS = ASG_omacs(parent)
      self.RHS.merge(ASG_pns(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj1628=Agent(parent)
      self.obj1628.preAction( self.RHS.CREATE )
      self.obj1628.isGraphObjectVisual = True

      if(hasattr(self.obj1628, '_setHierarchicalLink')):
        self.obj1628._setHierarchicalLink(False)

      # price
      self.obj1628.price.setNone()

      # name
      self.obj1628.name.setValue('')
      self.obj1628.name.setNone()

      self.obj1628.GGLabel.setValue(1)
      self.obj1628.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(60.0,40.0,self.obj1628)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1628.graphObject_ = new_obj
      self.obj16280= AttrCalc()
      self.obj16280.Copy=ATOM3Boolean()
      self.obj16280.Copy.setValue(('Copy from LHS', 1))
      self.obj16280.Copy.config = 0
      self.obj16280.Specify=ATOM3Constraint()
      self.obj16280.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1628.GGset2Any['price']= self.obj16280
      self.obj16281= AttrCalc()
      self.obj16281.Copy=ATOM3Boolean()
      self.obj16281.Copy.setValue(('Copy from LHS', 1))
      self.obj16281.Copy.config = 0
      self.obj16281.Specify=ATOM3Constraint()
      self.obj16281.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1628.GGset2Any['name']= self.obj16281

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1628)
      self.obj1628.postAction( self.RHS.CREATE )

      self.obj1629=Role(parent)
      self.obj1629.preAction( self.RHS.CREATE )
      self.obj1629.isGraphObjectVisual = True

      if(hasattr(self.obj1629, '_setHierarchicalLink')):
        self.obj1629._setHierarchicalLink(False)

      # name
      self.obj1629.name.setValue('')
      self.obj1629.name.setNone()

      self.obj1629.GGLabel.setValue(2)
      self.obj1629.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(320.0,220.0,self.obj1629)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1629.graphObject_ = new_obj
      self.obj16290= AttrCalc()
      self.obj16290.Copy=ATOM3Boolean()
      self.obj16290.Copy.setValue(('Copy from LHS', 1))
      self.obj16290.Copy.config = 0
      self.obj16290.Specify=ATOM3Constraint()
      self.obj16290.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1629.GGset2Any['name']= self.obj16290

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1629)
      self.obj1629.postAction( self.RHS.CREATE )

      self.obj1630=CapableOf(parent)
      self.obj1630.preAction( self.RHS.CREATE )
      self.obj1630.isGraphObjectVisual = True

      if(hasattr(self.obj1630, '_setHierarchicalLink')):
        self.obj1630._setHierarchicalLink(False)

      # rate
      self.obj1630.rate.setNone()

      self.obj1630.GGLabel.setValue(3)
      self.obj1630.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(230.0,173.0,self.obj1630)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1630.graphObject_ = new_obj
      self.obj16300= AttrCalc()
      self.obj16300.Copy=ATOM3Boolean()
      self.obj16300.Copy.setValue(('Copy from LHS', 1))
      self.obj16300.Copy.config = 0
      self.obj16300.Specify=ATOM3Constraint()
      self.obj16300.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1630.GGset2Any['rate']= self.obj16300

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1630)
      self.obj1630.postAction( self.RHS.CREATE )

      self.obj1631=operatingUnit(parent)
      self.obj1631.preAction( self.RHS.CREATE )
      self.obj1631.isGraphObjectVisual = True

      if(hasattr(self.obj1631, '_setHierarchicalLink')):
        self.obj1631._setHierarchicalLink(False)

      # OperCostProp
      self.obj1631.OperCostProp.setValue(0.0)

      # name
      self.obj1631.name.setValue('')
      self.obj1631.name.setNone()

      # OperCostFix
      self.obj1631.OperCostFix.setValue(0.0)

      self.obj1631.GGLabel.setValue(5)
      self.obj1631.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(60.0,220.0,self.obj1631)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1631.graphObject_ = new_obj
      self.obj16310= AttrCalc()
      self.obj16310.Copy=ATOM3Boolean()
      self.obj16310.Copy.setValue(('Copy from LHS', 1))
      self.obj16310.Copy.config = 0
      self.obj16310.Specify=ATOM3Constraint()
      self.obj16310.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1631.GGset2Any['OperCostProp']= self.obj16310
      self.obj16311= AttrCalc()
      self.obj16311.Copy=ATOM3Boolean()
      self.obj16311.Copy.setValue(('Copy from LHS', 0))
      self.obj16311.Copy.config = 0
      self.obj16311.Specify=ATOM3Constraint()
      self.obj16311.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()+\' \'+self.getMatched(graphID, self.LHS.nodeWithLabel(2)).name.getValue()\n\n\n\n'))
      self.obj1631.GGset2Any['name']= self.obj16311
      self.obj16312= AttrCalc()
      self.obj16312.Copy=ATOM3Boolean()
      self.obj16312.Copy.setValue(('Copy from LHS', 1))
      self.obj16312.Copy.config = 0
      self.obj16312.Specify=ATOM3Constraint()
      self.obj16312.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1631.GGset2Any['OperCostFix']= self.obj16312

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1631)
      self.obj1631.postAction( self.RHS.CREATE )

      self.obj1632=GenericGraphEdge(parent)
      self.obj1632.preAction( self.RHS.CREATE )
      self.obj1632.isGraphObjectVisual = True

      if(hasattr(self.obj1632, '_setHierarchicalLink')):
        self.obj1632._setHierarchicalLink(False)

      self.obj1632.GGLabel.setValue(6)
      self.obj1632.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(103.5,161.5,self.obj1632)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1632.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1632)
      self.obj1632.postAction( self.RHS.CREATE )

      self.obj1628.out_connections_.append(self.obj1630)
      self.obj1630.in_connections_.append(self.obj1628)
      self.obj1628.graphObject_.pendingConnections.append((self.obj1628.graphObject_.tag, self.obj1630.graphObject_.tag, [97.0, 102.0, 230.0, 173.0], 2, 0))
      self.obj1628.out_connections_.append(self.obj1632)
      self.obj1632.in_connections_.append(self.obj1628)
      self.obj1628.graphObject_.pendingConnections.append((self.obj1628.graphObject_.tag, self.obj1632.graphObject_.tag, [97.0, 102.0, 103.5, 161.5], 0, True))
      self.obj1630.out_connections_.append(self.obj1629)
      self.obj1629.in_connections_.append(self.obj1630)
      self.obj1630.graphObject_.pendingConnections.append((self.obj1630.graphObject_.tag, self.obj1629.graphObject_.tag, [351.0, 220.0, 230.0, 173.0], 2, 0))
      self.obj1632.out_connections_.append(self.obj1631)
      self.obj1631.in_connections_.append(self.obj1632)
      self.obj1632.graphObject_.pendingConnections.append((self.obj1632.graphObject_.tag, self.obj1631.graphObject_.tag, [110.0, 221.0, 103.5, 161.5], 0, True))

   def condition(self, graphID, isograph, atom3i):
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      node2 = self.getMatched(graphID, self.LHS.nodeWithLabel(2))
      print node.name.getValue()+' '+node2.name.getValue()
      # remplaceed by  "LinkAR2OpUnit"
      return not(  hasattr(node,node2.name.getValue()+'7') and hasattr(node2, node.name.getValue()+'7') )
      
      

   def action(self, graphID, isograph, atom3i):
      node = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) )
      
      node2 = self.getMatched ( graphID , self.LHS.nodeWithLabel(2) )
      setattr( node ,node2.name.getValue()+'7' ,True )
      setattr( node2 ,node.name.getValue()+'7' ,True )
      
      
      

