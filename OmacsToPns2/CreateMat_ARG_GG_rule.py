# _ CreateMat_ARG_GG_rule.py ____________________________________________________________________________
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
class CreateMat_ARG_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 17)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_pns(parent)
      self.LHS.merge(ASG_omacs(parent))

      self.obj1696=CapableOf(parent)
      self.obj1696.preAction( self.LHS.CREATE )
      self.obj1696.isGraphObjectVisual = True

      if(hasattr(self.obj1696, '_setHierarchicalLink')):
        self.obj1696._setHierarchicalLink(False)

      # rate
      self.obj1696.rate.setNone()

      self.obj1696.GGLabel.setValue(4)
      self.obj1696.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(250.75,110.75,self.obj1696)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1696.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1696)
      self.obj1696.postAction( self.LHS.CREATE )

      self.obj1697=Goal(parent)
      self.obj1697.preAction( self.LHS.CREATE )
      self.obj1697.isGraphObjectVisual = True

      if(hasattr(self.obj1697, '_setHierarchicalLink')):
        self.obj1697._setHierarchicalLink(False)

      # name
      self.obj1697.name.setValue('')
      self.obj1697.name.setNone()

      self.obj1697.GGLabel.setValue(3)
      self.obj1697.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(100.0,240.0,self.obj1697)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1697.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1697)
      self.obj1697.postAction( self.LHS.CREATE )

      self.obj1698=Agent(parent)
      self.obj1698.preAction( self.LHS.CREATE )
      self.obj1698.isGraphObjectVisual = True

      if(hasattr(self.obj1698, '_setHierarchicalLink')):
        self.obj1698._setHierarchicalLink(False)

      # price
      self.obj1698.price.setNone()

      # name
      self.obj1698.name.setValue('')
      self.obj1698.name.setNone()

      self.obj1698.GGLabel.setValue(1)
      self.obj1698.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(80.0,40.0,self.obj1698)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1698.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1698)
      self.obj1698.postAction( self.LHS.CREATE )

      self.obj1699=Role(parent)
      self.obj1699.preAction( self.LHS.CREATE )
      self.obj1699.isGraphObjectVisual = True

      if(hasattr(self.obj1699, '_setHierarchicalLink')):
        self.obj1699._setHierarchicalLink(False)

      # name
      self.obj1699.name.setValue('')
      self.obj1699.name.setNone()

      self.obj1699.GGLabel.setValue(2)
      self.obj1699.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(280.0,140.0,self.obj1699)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1699.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1699)
      self.obj1699.postAction( self.LHS.CREATE )

      self.obj1700=achieve(parent)
      self.obj1700.preAction( self.LHS.CREATE )
      self.obj1700.isGraphObjectVisual = True

      if(hasattr(self.obj1700, '_setHierarchicalLink')):
        self.obj1700._setHierarchicalLink(False)

      # rate
      self.obj1700.rate.setNone()

      self.obj1700.GGLabel.setValue(5)
      self.obj1700.graphClass_= graph_achieve
      if parent.genGraphics:
         new_obj = graph_achieve(258.5,259.0,self.obj1700)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1700.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1700)
      self.obj1700.postAction( self.LHS.CREATE )

      self.obj1696.out_connections_.append(self.obj1699)
      self.obj1699.in_connections_.append(self.obj1696)
      self.obj1696.graphObject_.pendingConnections.append((self.obj1696.graphObject_.tag, self.obj1699.graphObject_.tag, [304.0, 141.0, 300.5, 120.5, 250.75, 110.75], 2, True))
      self.obj1698.out_connections_.append(self.obj1696)
      self.obj1696.in_connections_.append(self.obj1698)
      self.obj1698.graphObject_.pendingConnections.append((self.obj1698.graphObject_.tag, self.obj1696.graphObject_.tag, [105.0, 102.0, 201.0, 101.0, 250.75, 110.75], 2, True))
      self.obj1699.out_connections_.append(self.obj1700)
      self.obj1700.in_connections_.append(self.obj1699)
      self.obj1699.graphObject_.pendingConnections.append((self.obj1699.graphObject_.tag, self.obj1700.graphObject_.tag, [304.0, 186.0, 303.5, 233.0, 258.5, 259.0], 2, True))
      self.obj1700.out_connections_.append(self.obj1697)
      self.obj1697.in_connections_.append(self.obj1700)
      self.obj1700.graphObject_.pendingConnections.append((self.obj1700.graphObject_.tag, self.obj1697.graphObject_.tag, [124.0, 290.0, 213.5, 285.0, 258.5, 259.0], 2, True))

      self.RHS = ASG_pns(parent)
      self.RHS.merge(ASG_omacs(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj1704=metarial(parent)
      self.obj1704.preAction( self.RHS.CREATE )
      self.obj1704.isGraphObjectVisual = True

      if(hasattr(self.obj1704, '_setHierarchicalLink')):
        self.obj1704._setHierarchicalLink(False)

      # MaxFlow
      self.obj1704.MaxFlow.setValue(999999)

      # price
      self.obj1704.price.setValue(0)

      # Name
      self.obj1704.Name.setValue('')
      self.obj1704.Name.setNone()

      # ReqFlow
      self.obj1704.ReqFlow.setValue(0)

      self.obj1704.GGLabel.setValue(8)
      self.obj1704.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(400.0,80.0,self.obj1704)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1704.graphObject_ = new_obj
      self.obj17040= AttrCalc()
      self.obj17040.Copy=ATOM3Boolean()
      self.obj17040.Copy.setValue(('Copy from LHS', 1))
      self.obj17040.Copy.config = 0
      self.obj17040.Specify=ATOM3Constraint()
      self.obj17040.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1704.GGset2Any['MaxFlow']= self.obj17040
      self.obj17041= AttrCalc()
      self.obj17041.Copy=ATOM3Boolean()
      self.obj17041.Copy.setValue(('Copy from LHS', 0))
      self.obj17041.Copy.config = 0
      self.obj17041.Specify=ATOM3Constraint()
      self.obj17041.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()+\' \'+ self.getMatched(graphID, self.LHS.nodeWithLabel(2)).name.getValue()+\' \'+ self.getMatched(graphID, self.LHS.nodeWithLabel(3)).name.getValue()\n\n'))
      self.obj1704.GGset2Any['Name']= self.obj17041
      self.obj17042= AttrCalc()
      self.obj17042.Copy=ATOM3Boolean()
      self.obj17042.Copy.setValue(('Copy from LHS', 1))
      self.obj17042.Copy.config = 0
      self.obj17042.Specify=ATOM3Constraint()
      self.obj17042.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1704.GGset2Any['ReqFlow']= self.obj17042

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1704)
      self.obj1704.postAction( self.RHS.CREATE )

      self.obj1705=operatingUnit(parent)
      self.obj1705.preAction( self.RHS.CREATE )
      self.obj1705.isGraphObjectVisual = True

      if(hasattr(self.obj1705, '_setHierarchicalLink')):
        self.obj1705._setHierarchicalLink(False)

      # OperCostProp
      self.obj1705.OperCostProp.setValue(0.0)

      # name
      self.obj1705.name.setValue('')
      self.obj1705.name.setNone()

      # OperCostFix
      self.obj1705.OperCostFix.setValue(0.0)

      self.obj1705.GGLabel.setValue(7)
      self.obj1705.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(400.0,240.0,self.obj1705)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1705.graphObject_ = new_obj
      self.obj17050= AttrCalc()
      self.obj17050.Copy=ATOM3Boolean()
      self.obj17050.Copy.setValue(('Copy from LHS', 0))
      self.obj17050.Copy.config = 0
      self.obj17050.Specify=ATOM3Constraint()
      self.obj17050.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(5)).rate.getValue()\n'))
      self.obj1705.GGset2Any['OperCostProp']= self.obj17050
      self.obj17051= AttrCalc()
      self.obj17051.Copy=ATOM3Boolean()
      self.obj17051.Copy.setValue(('Copy from LHS', 0))
      self.obj17051.Copy.config = 0
      self.obj17051.Specify=ATOM3Constraint()
      self.obj17051.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()+\' \'+ self.getMatched(graphID, self.LHS.nodeWithLabel(2)).name.getValue()+\' \'+ self.getMatched(graphID, self.LHS.nodeWithLabel(3)).name.getValue()\n\n\n\n\n\n\n'))
      self.obj1705.GGset2Any['name']= self.obj17051
      self.obj17052= AttrCalc()
      self.obj17052.Copy=ATOM3Boolean()
      self.obj17052.Copy.setValue(('Copy from LHS', 0))
      self.obj17052.Copy.config = 0
      self.obj17052.Specify=ATOM3Constraint()
      self.obj17052.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return 2.0\n'))
      self.obj1705.GGset2Any['OperCostFix']= self.obj17052

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1705)
      self.obj1705.postAction( self.RHS.CREATE )

      self.obj1706=fromMaterial(parent)
      self.obj1706.preAction( self.RHS.CREATE )
      self.obj1706.isGraphObjectVisual = True

      if(hasattr(self.obj1706, '_setHierarchicalLink')):
        self.obj1706._setHierarchicalLink(False)

      # rate
      self.obj1706.rate.setValue(1.0)

      self.obj1706.GGLabel.setValue(9)
      self.obj1706.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(422.0,190.0,self.obj1706)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1706.graphObject_ = new_obj
      self.obj17060= AttrCalc()
      self.obj17060.Copy=ATOM3Boolean()
      self.obj17060.Copy.setValue(('Copy from LHS', 0))
      self.obj17060.Copy.config = 0
      self.obj17060.Specify=ATOM3Constraint()
      self.obj17060.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1706.GGset2Any['rate']= self.obj17060

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1706)
      self.obj1706.postAction( self.RHS.CREATE )

      self.obj1707=CapableOf(parent)
      self.obj1707.preAction( self.RHS.CREATE )
      self.obj1707.isGraphObjectVisual = True

      if(hasattr(self.obj1707, '_setHierarchicalLink')):
        self.obj1707._setHierarchicalLink(False)

      # rate
      self.obj1707.rate.setNone()

      self.obj1707.GGLabel.setValue(4)
      self.obj1707.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(250.75,110.75,self.obj1707)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1707.graphObject_ = new_obj
      self.obj17070= AttrCalc()
      self.obj17070.Copy=ATOM3Boolean()
      self.obj17070.Copy.setValue(('Copy from LHS', 1))
      self.obj17070.Copy.config = 0
      self.obj17070.Specify=ATOM3Constraint()
      self.obj17070.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1707.GGset2Any['rate']= self.obj17070

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1707)
      self.obj1707.postAction( self.RHS.CREATE )

      self.obj1708=Goal(parent)
      self.obj1708.preAction( self.RHS.CREATE )
      self.obj1708.isGraphObjectVisual = True

      if(hasattr(self.obj1708, '_setHierarchicalLink')):
        self.obj1708._setHierarchicalLink(False)

      # name
      self.obj1708.name.setValue('')
      self.obj1708.name.setNone()

      self.obj1708.GGLabel.setValue(3)
      self.obj1708.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(100.0,240.0,self.obj1708)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1708.graphObject_ = new_obj
      self.obj17080= AttrCalc()
      self.obj17080.Copy=ATOM3Boolean()
      self.obj17080.Copy.setValue(('Copy from LHS', 1))
      self.obj17080.Copy.config = 0
      self.obj17080.Specify=ATOM3Constraint()
      self.obj17080.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1708.GGset2Any['name']= self.obj17080

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1708)
      self.obj1708.postAction( self.RHS.CREATE )

      self.obj1709=Agent(parent)
      self.obj1709.preAction( self.RHS.CREATE )
      self.obj1709.isGraphObjectVisual = True

      if(hasattr(self.obj1709, '_setHierarchicalLink')):
        self.obj1709._setHierarchicalLink(False)

      # price
      self.obj1709.price.setNone()

      # name
      self.obj1709.name.setValue('')
      self.obj1709.name.setNone()

      self.obj1709.GGLabel.setValue(1)
      self.obj1709.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(80.0,40.0,self.obj1709)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1709.graphObject_ = new_obj
      self.obj17090= AttrCalc()
      self.obj17090.Copy=ATOM3Boolean()
      self.obj17090.Copy.setValue(('Copy from LHS', 1))
      self.obj17090.Copy.config = 0
      self.obj17090.Specify=ATOM3Constraint()
      self.obj17090.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1709.GGset2Any['price']= self.obj17090
      self.obj17091= AttrCalc()
      self.obj17091.Copy=ATOM3Boolean()
      self.obj17091.Copy.setValue(('Copy from LHS', 1))
      self.obj17091.Copy.config = 0
      self.obj17091.Specify=ATOM3Constraint()
      self.obj17091.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1709.GGset2Any['name']= self.obj17091

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1709)
      self.obj1709.postAction( self.RHS.CREATE )

      self.obj1710=Role(parent)
      self.obj1710.preAction( self.RHS.CREATE )
      self.obj1710.isGraphObjectVisual = True

      if(hasattr(self.obj1710, '_setHierarchicalLink')):
        self.obj1710._setHierarchicalLink(False)

      # name
      self.obj1710.name.setValue('')
      self.obj1710.name.setNone()

      self.obj1710.GGLabel.setValue(2)
      self.obj1710.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(280.0,140.0,self.obj1710)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1710.graphObject_ = new_obj
      self.obj17100= AttrCalc()
      self.obj17100.Copy=ATOM3Boolean()
      self.obj17100.Copy.setValue(('Copy from LHS', 1))
      self.obj17100.Copy.config = 0
      self.obj17100.Specify=ATOM3Constraint()
      self.obj17100.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1710.GGset2Any['name']= self.obj17100

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1710)
      self.obj1710.postAction( self.RHS.CREATE )

      self.obj1711=achieve(parent)
      self.obj1711.preAction( self.RHS.CREATE )
      self.obj1711.isGraphObjectVisual = True

      if(hasattr(self.obj1711, '_setHierarchicalLink')):
        self.obj1711._setHierarchicalLink(False)

      # rate
      self.obj1711.rate.setNone()

      self.obj1711.GGLabel.setValue(5)
      self.obj1711.graphClass_= graph_achieve
      if parent.genGraphics:
         new_obj = graph_achieve(258.5,259.0,self.obj1711)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1711.graphObject_ = new_obj
      self.obj17110= AttrCalc()
      self.obj17110.Copy=ATOM3Boolean()
      self.obj17110.Copy.setValue(('Copy from LHS', 1))
      self.obj17110.Copy.config = 0
      self.obj17110.Specify=ATOM3Constraint()
      self.obj17110.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1711.GGset2Any['rate']= self.obj17110

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1711)
      self.obj1711.postAction( self.RHS.CREATE )

      self.obj1712=GenericGraphEdge(parent)
      self.obj1712.preAction( self.RHS.CREATE )
      self.obj1712.isGraphObjectVisual = True

      if(hasattr(self.obj1712, '_setHierarchicalLink')):
        self.obj1712._setHierarchicalLink(False)

      self.obj1712.GGLabel.setValue(10)
      self.obj1712.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(358.5,131.0,self.obj1712)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1712.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1712)
      self.obj1712.postAction( self.RHS.CREATE )

      self.obj1704.out_connections_.append(self.obj1706)
      self.obj1706.in_connections_.append(self.obj1704)
      self.obj1704.graphObject_.pendingConnections.append((self.obj1704.graphObject_.tag, self.obj1706.graphObject_.tag, [424.0, 129.0, 422.0, 190.0], 0, True))
      self.obj1706.out_connections_.append(self.obj1705)
      self.obj1705.in_connections_.append(self.obj1706)
      self.obj1706.graphObject_.pendingConnections.append((self.obj1706.graphObject_.tag, self.obj1705.graphObject_.tag, [420.0, 251.0, 422.0, 190.0], 0, True))
      self.obj1707.out_connections_.append(self.obj1710)
      self.obj1710.in_connections_.append(self.obj1707)
      self.obj1707.graphObject_.pendingConnections.append((self.obj1707.graphObject_.tag, self.obj1710.graphObject_.tag, [311.0, 140.0, 250.75, 110.75], 2, 0))
      self.obj1709.out_connections_.append(self.obj1707)
      self.obj1707.in_connections_.append(self.obj1709)
      self.obj1709.graphObject_.pendingConnections.append((self.obj1709.graphObject_.tag, self.obj1707.graphObject_.tag, [117.0, 102.0, 250.75, 110.75], 2, 0))
      self.obj1710.out_connections_.append(self.obj1711)
      self.obj1711.in_connections_.append(self.obj1710)
      self.obj1710.graphObject_.pendingConnections.append((self.obj1710.graphObject_.tag, self.obj1711.graphObject_.tag, [311.0, 185.0, 258.5, 259.0], 2, 0))
      self.obj1710.out_connections_.append(self.obj1712)
      self.obj1712.in_connections_.append(self.obj1710)
      self.obj1710.graphObject_.pendingConnections.append((self.obj1710.graphObject_.tag, self.obj1712.graphObject_.tag, [311.0, 140.0, 358.5, 131.0], 0, True))
      self.obj1711.out_connections_.append(self.obj1708)
      self.obj1708.in_connections_.append(self.obj1711)
      self.obj1711.graphObject_.pendingConnections.append((self.obj1711.graphObject_.tag, self.obj1708.graphObject_.tag, [134.0, 290.0, 258.5, 259.0], 2, 0))
      self.obj1712.out_connections_.append(self.obj1704)
      self.obj1704.in_connections_.append(self.obj1712)
      self.obj1712.graphObject_.pendingConnections.append((self.obj1712.graphObject_.tag, self.obj1704.graphObject_.tag, [406.0, 122.0, 358.5, 131.0], 0, True))

   def condition(self, graphID, isograph, atom3i):
      print '======> GenAux1 Condition'
      a = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      aN = a.name.getValue()
      #print a.name.getValue()+' has att AUX : '+str( hasattr(a, "AUX") )
      r = self.getMatched(graphID, self.LHS.nodeWithLabel(2))
      Rn = r.name.getValue()
      g = self.getMatched(graphID, self.LHS.nodeWithLabel(3))
      Gn = g.name.getValue()
      # add list to the Agent Node
      if not hasattr(a,'markedNode') : 
      	a.markedNode = []
      	print 'add List to '+aN
      
      print 'CHeck if '+aN+'Have'
      for ele in a.markedNode : 
          if ele == (Rn,Gn) : return False
      return True
      #        print 'Check if '+aN+'Have '
      #        for ele in a.markedNode : 
      #            if ele == (Rn,Gn) : return False 
      #        return True
      
      

   def action(self, graphID, isograph, atom3i):
      print '======> GenAux1 ACtion'
      a = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      aN = a.name.getValue()
      #print a.name.getValue()+' has att AUX : '+str( hasattr(a, "AUX") )
      r = self.getMatched(graphID, self.LHS.nodeWithLabel(2))
      Rn = r.name.getValue()
      g = self.getMatched(graphID, self.LHS.nodeWithLabel(3))
      Gn = g.name.getValue()
      # add ele list to the Agent Node
      print 'Add Ele into list of '+aN
      a.markedNode.append( (Rn,Gn) )
      print 'List of MarkedNode'
      for ele in a.markedNode : 
      	print ele
      

