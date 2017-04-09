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
      GGrule.__init__(self, 7)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_omacs(parent)

      self.obj149=Agent(parent)
      self.obj149.preAction( self.LHS.CREATE )
      self.obj149.isGraphObjectVisual = True

      if(hasattr(self.obj149, '_setHierarchicalLink')):
        self.obj149._setHierarchicalLink(False)

      # price
      self.obj149.price.setNone()

      # name
      self.obj149.name.setValue('')
      self.obj149.name.setNone()

      self.obj149.GGLabel.setValue(1)
      self.obj149.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(60.0,40.0,self.obj149)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj149.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj149)
      self.obj149.postAction( self.LHS.CREATE )

      self.obj150=Role(parent)
      self.obj150.preAction( self.LHS.CREATE )
      self.obj150.isGraphObjectVisual = True

      if(hasattr(self.obj150, '_setHierarchicalLink')):
        self.obj150._setHierarchicalLink(False)

      # name
      self.obj150.name.setValue('')
      self.obj150.name.setNone()

      self.obj150.GGLabel.setValue(2)
      self.obj150.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(320.0,220.0,self.obj150)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj150.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj150)
      self.obj150.postAction( self.LHS.CREATE )

      self.obj151=CapableOf(parent)
      self.obj151.preAction( self.LHS.CREATE )
      self.obj151.isGraphObjectVisual = True

      if(hasattr(self.obj151, '_setHierarchicalLink')):
        self.obj151._setHierarchicalLink(False)

      # rate
      self.obj151.rate.setNone()

      self.obj151.GGLabel.setValue(3)
      self.obj151.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(230.0,173.0,self.obj151)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj151.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj151)
      self.obj151.postAction( self.LHS.CREATE )

      self.obj149.out_connections_.append(self.obj151)
      self.obj151.in_connections_.append(self.obj149)
      self.obj149.graphObject_.pendingConnections.append((self.obj149.graphObject_.tag, self.obj151.graphObject_.tag, [85.0, 102.0, 117.0, 188.0, 230.0, 173.0], 2, True))
      self.obj151.out_connections_.append(self.obj150)
      self.obj150.in_connections_.append(self.obj151)
      self.obj151.graphObject_.pendingConnections.append((self.obj151.graphObject_.tag, self.obj150.graphObject_.tag, [344.0, 221.0, 343.0, 158.0, 230.0, 173.0], 2, True))

      self.RHS = ASG_omacs(parent)
      self.RHS.merge(ASG_pns(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj155=Agent(parent)
      self.obj155.preAction( self.RHS.CREATE )
      self.obj155.isGraphObjectVisual = True

      if(hasattr(self.obj155, '_setHierarchicalLink')):
        self.obj155._setHierarchicalLink(False)

      # price
      self.obj155.price.setNone()

      # name
      self.obj155.name.setValue('')
      self.obj155.name.setNone()

      self.obj155.GGLabel.setValue(1)
      self.obj155.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(60.0,40.0,self.obj155)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj155.graphObject_ = new_obj
      self.obj1550= AttrCalc()
      self.obj1550.Copy=ATOM3Boolean()
      self.obj1550.Copy.setValue(('Copy from LHS', 1))
      self.obj1550.Copy.config = 0
      self.obj1550.Specify=ATOM3Constraint()
      self.obj1550.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj155.GGset2Any['price']= self.obj1550
      self.obj1551= AttrCalc()
      self.obj1551.Copy=ATOM3Boolean()
      self.obj1551.Copy.setValue(('Copy from LHS', 1))
      self.obj1551.Copy.config = 0
      self.obj1551.Specify=ATOM3Constraint()
      self.obj1551.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj155.GGset2Any['name']= self.obj1551

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj155)
      self.obj155.postAction( self.RHS.CREATE )

      self.obj156=Role(parent)
      self.obj156.preAction( self.RHS.CREATE )
      self.obj156.isGraphObjectVisual = True

      if(hasattr(self.obj156, '_setHierarchicalLink')):
        self.obj156._setHierarchicalLink(False)

      # name
      self.obj156.name.setValue('')
      self.obj156.name.setNone()

      self.obj156.GGLabel.setValue(2)
      self.obj156.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(320.0,220.0,self.obj156)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj156.graphObject_ = new_obj
      self.obj1560= AttrCalc()
      self.obj1560.Copy=ATOM3Boolean()
      self.obj1560.Copy.setValue(('Copy from LHS', 1))
      self.obj1560.Copy.config = 0
      self.obj1560.Specify=ATOM3Constraint()
      self.obj1560.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj156.GGset2Any['name']= self.obj1560

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj156)
      self.obj156.postAction( self.RHS.CREATE )

      self.obj157=CapableOf(parent)
      self.obj157.preAction( self.RHS.CREATE )
      self.obj157.isGraphObjectVisual = True

      if(hasattr(self.obj157, '_setHierarchicalLink')):
        self.obj157._setHierarchicalLink(False)

      # rate
      self.obj157.rate.setNone()

      self.obj157.GGLabel.setValue(3)
      self.obj157.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(230.0,173.0,self.obj157)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj157.graphObject_ = new_obj
      self.obj1570= AttrCalc()
      self.obj1570.Copy=ATOM3Boolean()
      self.obj1570.Copy.setValue(('Copy from LHS', 1))
      self.obj1570.Copy.config = 0
      self.obj1570.Specify=ATOM3Constraint()
      self.obj1570.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj157.GGset2Any['rate']= self.obj1570

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj157)
      self.obj157.postAction( self.RHS.CREATE )

      self.obj158=operatingUnit(parent)
      self.obj158.preAction( self.RHS.CREATE )
      self.obj158.isGraphObjectVisual = True

      if(hasattr(self.obj158, '_setHierarchicalLink')):
        self.obj158._setHierarchicalLink(False)

      # OperCostProp
      self.obj158.OperCostProp.setValue(0.0)

      # name
      self.obj158.name.setValue('')
      self.obj158.name.setNone()

      # OperCostFix
      self.obj158.OperCostFix.setValue(0.0)

      self.obj158.GGLabel.setValue(5)
      self.obj158.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(60.0,220.0,self.obj158)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj158.graphObject_ = new_obj
      self.obj1580= AttrCalc()
      self.obj1580.Copy=ATOM3Boolean()
      self.obj1580.Copy.setValue(('Copy from LHS', 1))
      self.obj1580.Copy.config = 0
      self.obj1580.Specify=ATOM3Constraint()
      self.obj1580.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj158.GGset2Any['OperCostProp']= self.obj1580
      self.obj1581= AttrCalc()
      self.obj1581.Copy=ATOM3Boolean()
      self.obj1581.Copy.setValue(('Copy from LHS', 0))
      self.obj1581.Copy.config = 0
      self.obj1581.Specify=ATOM3Constraint()
      self.obj1581.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()+\' \'+self.getMatched(graphID, self.LHS.nodeWithLabel(2)).name.getValue()\n\n\n\n'))
      self.obj158.GGset2Any['name']= self.obj1581
      self.obj1582= AttrCalc()
      self.obj1582.Copy=ATOM3Boolean()
      self.obj1582.Copy.setValue(('Copy from LHS', 1))
      self.obj1582.Copy.config = 0
      self.obj1582.Specify=ATOM3Constraint()
      self.obj1582.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj158.GGset2Any['OperCostFix']= self.obj1582

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj158)
      self.obj158.postAction( self.RHS.CREATE )

      self.obj159=GenericGraphEdge(parent)
      self.obj159.preAction( self.RHS.CREATE )
      self.obj159.isGraphObjectVisual = True

      if(hasattr(self.obj159, '_setHierarchicalLink')):
        self.obj159._setHierarchicalLink(False)

      self.obj159.GGLabel.setValue(6)
      self.obj159.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(103.5,161.5,self.obj159)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj159.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj159)
      self.obj159.postAction( self.RHS.CREATE )

      self.obj155.out_connections_.append(self.obj157)
      self.obj157.in_connections_.append(self.obj155)
      self.obj155.graphObject_.pendingConnections.append((self.obj155.graphObject_.tag, self.obj157.graphObject_.tag, [97.0, 102.0, 230.0, 173.0], 2, 0))
      self.obj155.out_connections_.append(self.obj159)
      self.obj159.in_connections_.append(self.obj155)
      self.obj155.graphObject_.pendingConnections.append((self.obj155.graphObject_.tag, self.obj159.graphObject_.tag, [97.0, 102.0, 103.5, 161.5], 0, True))
      self.obj157.out_connections_.append(self.obj156)
      self.obj156.in_connections_.append(self.obj157)
      self.obj157.graphObject_.pendingConnections.append((self.obj157.graphObject_.tag, self.obj156.graphObject_.tag, [351.0, 220.0, 230.0, 173.0], 2, 0))
      self.obj159.out_connections_.append(self.obj158)
      self.obj158.in_connections_.append(self.obj159)
      self.obj159.graphObject_.pendingConnections.append((self.obj159.graphObject_.tag, self.obj158.graphObject_.tag, [110.0, 221.0, 103.5, 161.5], 0, True))

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
      
      
      

