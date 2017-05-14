# _ CreateLinkAR2Mat_GG_rule.py ____________________________________________________________________________
# File generated automatically by ATOM3. Graph Grammar Rule
# ___________________________________________________________________________________________
from GGrule import *
from Capabilitie import *
from rawMaterial import *
from GenericGraphEdge import *
from Goal import *
from ASG_pns import *
from operatingUnit import *
from metarial import *
from GenericGraphNode import *
from product import *
from Agent import *
from fromMaterial import *
from CapableOf import *
from intoProduct import *
from Role import *
from fromRaw import *
from intoMaterial import *
from ASG_GenericGraph import *
from ASG_omacs import *
from require import *
from achieve import *
from posses import *
class CreateLinkAR2Mat_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 21)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_pns(parent)
      self.LHS.merge(ASG_omacs(parent))
      self.LHS.merge(ASG_GenericGraph(parent))

      self.obj1747=rawMaterial(parent)
      self.obj1747.preAction( self.LHS.CREATE )
      self.obj1747.isGraphObjectVisual = True

      if(hasattr(self.obj1747, '_setHierarchicalLink')):
        self.obj1747._setHierarchicalLink(False)

      # MaxFlow
      self.obj1747.MaxFlow.setNone()

      # price
      self.obj1747.price.setValue(0)

      # Name
      self.obj1747.Name.setValue('')
      self.obj1747.Name.setNone()

      # ReqFlow
      self.obj1747.ReqFlow.setNone()

      self.obj1747.GGLabel.setValue(6)
      self.obj1747.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(240.0,0.0,self.obj1747)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1747.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1747)
      self.obj1747.postAction( self.LHS.CREATE )

      self.obj1748=metarial(parent)
      self.obj1748.preAction( self.LHS.CREATE )
      self.obj1748.isGraphObjectVisual = True

      if(hasattr(self.obj1748, '_setHierarchicalLink')):
        self.obj1748._setHierarchicalLink(False)

      # MaxFlow
      self.obj1748.MaxFlow.setNone()

      # price
      self.obj1748.price.setValue(0)

      # Name
      self.obj1748.Name.setValue('')
      self.obj1748.Name.setNone()

      # ReqFlow
      self.obj1748.ReqFlow.setNone()

      self.obj1748.GGLabel.setValue(11)
      self.obj1748.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(260.0,200.0,self.obj1748)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1748.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1748)
      self.obj1748.postAction( self.LHS.CREATE )

      self.obj1749=operatingUnit(parent)
      self.obj1749.preAction( self.LHS.CREATE )
      self.obj1749.isGraphObjectVisual = True

      if(hasattr(self.obj1749, '_setHierarchicalLink')):
        self.obj1749._setHierarchicalLink(False)

      # OperCostProp
      self.obj1749.OperCostProp.setNone()

      # name
      self.obj1749.name.setValue('')
      self.obj1749.name.setNone()

      # OperCostFix
      self.obj1749.OperCostFix.setNone()

      self.obj1749.GGLabel.setValue(7)
      self.obj1749.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(280.0,100.0,self.obj1749)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1749.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1749)
      self.obj1749.postAction( self.LHS.CREATE )

      self.obj1750=operatingUnit(parent)
      self.obj1750.preAction( self.LHS.CREATE )
      self.obj1750.isGraphObjectVisual = True

      if(hasattr(self.obj1750, '_setHierarchicalLink')):
        self.obj1750._setHierarchicalLink(False)

      # OperCostProp
      self.obj1750.OperCostProp.setNone()

      # name
      self.obj1750.name.setValue('')
      self.obj1750.name.setNone()

      # OperCostFix
      self.obj1750.OperCostFix.setNone()

      self.obj1750.GGLabel.setValue(12)
      self.obj1750.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(360.0,260.0,self.obj1750)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1750.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1750)
      self.obj1750.postAction( self.LHS.CREATE )

      self.obj1751=fromRaw(parent)
      self.obj1751.preAction( self.LHS.CREATE )
      self.obj1751.isGraphObjectVisual = True

      if(hasattr(self.obj1751, '_setHierarchicalLink')):
        self.obj1751._setHierarchicalLink(False)

      # rate
      self.obj1751.rate.setNone()

      self.obj1751.GGLabel.setValue(8)
      self.obj1751.graphClass_= graph_fromRaw
      if parent.genGraphics:
         new_obj = graph_fromRaw(311.5,63.25,self.obj1751)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1751.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1751)
      self.obj1751.postAction( self.LHS.CREATE )

      self.obj1752=fromMaterial(parent)
      self.obj1752.preAction( self.LHS.CREATE )
      self.obj1752.isGraphObjectVisual = True

      if(hasattr(self.obj1752, '_setHierarchicalLink')):
        self.obj1752._setHierarchicalLink(False)

      # rate
      self.obj1752.rate.setNone()

      self.obj1752.GGLabel.setValue(14)
      self.obj1752.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(379.5,235.25,self.obj1752)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1752.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1752)
      self.obj1752.postAction( self.LHS.CREATE )

      self.obj1753=CapableOf(parent)
      self.obj1753.preAction( self.LHS.CREATE )
      self.obj1753.isGraphObjectVisual = True

      if(hasattr(self.obj1753, '_setHierarchicalLink')):
        self.obj1753._setHierarchicalLink(False)

      # rate
      self.obj1753.rate.setNone()

      self.obj1753.GGLabel.setValue(3)
      self.obj1753.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(84.5,131.5,self.obj1753)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1753.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1753)
      self.obj1753.postAction( self.LHS.CREATE )

      self.obj1754=Agent(parent)
      self.obj1754.preAction( self.LHS.CREATE )
      self.obj1754.isGraphObjectVisual = True

      if(hasattr(self.obj1754, '_setHierarchicalLink')):
        self.obj1754._setHierarchicalLink(False)

      # price
      self.obj1754.price.setNone()

      # name
      self.obj1754.name.setValue('')
      self.obj1754.name.setNone()

      self.obj1754.GGLabel.setValue(1)
      self.obj1754.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(60.0,20.0,self.obj1754)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1754.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1754)
      self.obj1754.postAction( self.LHS.CREATE )

      self.obj1755=Role(parent)
      self.obj1755.preAction( self.LHS.CREATE )
      self.obj1755.isGraphObjectVisual = True

      if(hasattr(self.obj1755, '_setHierarchicalLink')):
        self.obj1755._setHierarchicalLink(False)

      # name
      self.obj1755.name.setValue('')
      self.obj1755.name.setNone()

      self.obj1755.GGLabel.setValue(2)
      self.obj1755.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(60.0,180.0,self.obj1755)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1755.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1755)
      self.obj1755.postAction( self.LHS.CREATE )

      self.obj1756=GenericGraphEdge(parent)
      self.obj1756.preAction( self.LHS.CREATE )
      self.obj1756.isGraphObjectVisual = True

      if(hasattr(self.obj1756, '_setHierarchicalLink')):
        self.obj1756._setHierarchicalLink(False)

      self.obj1756.GGLabel.setValue(15)
      self.obj1756.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(174.5,69.0,self.obj1756)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1756.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1756)
      self.obj1756.postAction( self.LHS.CREATE )

      self.obj1757=GenericGraphEdge(parent)
      self.obj1757.preAction( self.LHS.CREATE )
      self.obj1757.isGraphObjectVisual = True

      if(hasattr(self.obj1757, '_setHierarchicalLink')):
        self.obj1757._setHierarchicalLink(False)

      self.obj1757.GGLabel.setValue(10)
      self.obj1757.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(245.75,97.25,self.obj1757)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1757.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1757)
      self.obj1757.postAction( self.LHS.CREATE )

      self.obj1758=GenericGraphEdge(parent)
      self.obj1758.preAction( self.LHS.CREATE )
      self.obj1758.isGraphObjectVisual = True

      if(hasattr(self.obj1758, '_setHierarchicalLink')):
        self.obj1758._setHierarchicalLink(False)

      self.obj1758.GGLabel.setValue(13)
      self.obj1758.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(175.0,234.0,self.obj1758)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1758.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1758)
      self.obj1758.postAction( self.LHS.CREATE )

      self.obj1747.out_connections_.append(self.obj1751)
      self.obj1751.in_connections_.append(self.obj1747)
      self.obj1747.graphObject_.pendingConnections.append((self.obj1747.graphObject_.tag, self.obj1751.graphObject_.tag, [264.0, 56.0, 295.0, 49.5, 311.5, 63.25], 2, True))
      self.obj1748.out_connections_.append(self.obj1752)
      self.obj1752.in_connections_.append(self.obj1748)
      self.obj1748.graphObject_.pendingConnections.append((self.obj1748.graphObject_.tag, self.obj1752.graphObject_.tag, [306.0, 210.0, 353.5, 220.0, 379.5, 235.25], 2, True))
      self.obj1751.out_connections_.append(self.obj1749)
      self.obj1749.in_connections_.append(self.obj1751)
      self.obj1751.graphObject_.pendingConnections.append((self.obj1751.graphObject_.tag, self.obj1749.graphObject_.tag, [330.0, 111.0, 328.0, 77.0, 311.5, 63.25], 2, True))
      self.obj1752.out_connections_.append(self.obj1750)
      self.obj1750.in_connections_.append(self.obj1752)
      self.obj1752.graphObject_.pendingConnections.append((self.obj1752.graphObject_.tag, self.obj1750.graphObject_.tag, [410.0, 271.0, 405.5, 250.5, 379.5, 235.25], 2, True))
      self.obj1753.out_connections_.append(self.obj1755)
      self.obj1755.in_connections_.append(self.obj1753)
      self.obj1753.graphObject_.pendingConnections.append((self.obj1753.graphObject_.tag, self.obj1755.graphObject_.tag, [84.0, 181.0, 84.5, 131.5], 0, True))
      self.obj1754.out_connections_.append(self.obj1753)
      self.obj1753.in_connections_.append(self.obj1754)
      self.obj1754.graphObject_.pendingConnections.append((self.obj1754.graphObject_.tag, self.obj1753.graphObject_.tag, [85.0, 82.0, 84.5, 131.5], 0, True))
      self.obj1754.out_connections_.append(self.obj1756)
      self.obj1756.in_connections_.append(self.obj1754)
      self.obj1754.graphObject_.pendingConnections.append((self.obj1754.graphObject_.tag, self.obj1756.graphObject_.tag, [85.0, 82.0, 174.5, 69.0], 0, True))
      self.obj1754.out_connections_.append(self.obj1757)
      self.obj1757.in_connections_.append(self.obj1754)
      self.obj1754.graphObject_.pendingConnections.append((self.obj1754.graphObject_.tag, self.obj1757.graphObject_.tag, [85.0, 82.0, 192.0, 90.0, 245.75, 97.25], 2, True))
      self.obj1755.out_connections_.append(self.obj1758)
      self.obj1758.in_connections_.append(self.obj1755)
      self.obj1755.graphObject_.pendingConnections.append((self.obj1755.graphObject_.tag, self.obj1758.graphObject_.tag, [84.0, 226.0, 175.0, 234.0], 0, True))
      self.obj1756.out_connections_.append(self.obj1747)
      self.obj1747.in_connections_.append(self.obj1756)
      self.obj1756.graphObject_.pendingConnections.append((self.obj1756.graphObject_.tag, self.obj1747.graphObject_.tag, [264.0, 56.0, 174.5, 69.0], 0, True))
      self.obj1757.out_connections_.append(self.obj1749)
      self.obj1749.in_connections_.append(self.obj1757)
      self.obj1757.graphObject_.pendingConnections.append((self.obj1757.graphObject_.tag, self.obj1749.graphObject_.tag, [300.0, 111.0, 299.5, 104.5, 245.75, 97.25], 2, True))
      self.obj1758.out_connections_.append(self.obj1748)
      self.obj1748.in_connections_.append(self.obj1758)
      self.obj1758.graphObject_.pendingConnections.append((self.obj1758.graphObject_.tag, self.obj1748.graphObject_.tag, [266.0, 242.0, 175.0, 234.0], 0, True))

      self.RHS = ASG_pns(parent)
      self.RHS.merge(ASG_omacs(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj1762=rawMaterial(parent)
      self.obj1762.preAction( self.RHS.CREATE )
      self.obj1762.isGraphObjectVisual = True

      if(hasattr(self.obj1762, '_setHierarchicalLink')):
        self.obj1762._setHierarchicalLink(False)

      # MaxFlow
      self.obj1762.MaxFlow.setNone()

      # price
      self.obj1762.price.setValue(0)

      # Name
      self.obj1762.Name.setValue('')
      self.obj1762.Name.setNone()

      # ReqFlow
      self.obj1762.ReqFlow.setNone()

      self.obj1762.GGLabel.setValue(6)
      self.obj1762.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(240.0,0.0,self.obj1762)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1762.graphObject_ = new_obj
      self.obj17620= AttrCalc()
      self.obj17620.Copy=ATOM3Boolean()
      self.obj17620.Copy.setValue(('Copy from LHS', 1))
      self.obj17620.Copy.config = 0
      self.obj17620.Specify=ATOM3Constraint()
      self.obj17620.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1762.GGset2Any['MaxFlow']= self.obj17620
      self.obj17621= AttrCalc()
      self.obj17621.Copy=ATOM3Boolean()
      self.obj17621.Copy.setValue(('Copy from LHS', 1))
      self.obj17621.Copy.config = 0
      self.obj17621.Specify=ATOM3Constraint()
      self.obj17621.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1762.GGset2Any['Name']= self.obj17621
      self.obj17622= AttrCalc()
      self.obj17622.Copy=ATOM3Boolean()
      self.obj17622.Copy.setValue(('Copy from LHS', 1))
      self.obj17622.Copy.config = 0
      self.obj17622.Specify=ATOM3Constraint()
      self.obj17622.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1762.GGset2Any['ReqFlow']= self.obj17622

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1762)
      self.obj1762.postAction( self.RHS.CREATE )

      self.obj1763=metarial(parent)
      self.obj1763.preAction( self.RHS.CREATE )
      self.obj1763.isGraphObjectVisual = True

      if(hasattr(self.obj1763, '_setHierarchicalLink')):
        self.obj1763._setHierarchicalLink(False)

      # MaxFlow
      self.obj1763.MaxFlow.setNone()

      # price
      self.obj1763.price.setValue(0)

      # Name
      self.obj1763.Name.setValue('')
      self.obj1763.Name.setNone()

      # ReqFlow
      self.obj1763.ReqFlow.setNone()

      self.obj1763.GGLabel.setValue(11)
      self.obj1763.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(260.0,200.0,self.obj1763)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1763.graphObject_ = new_obj
      self.obj17630= AttrCalc()
      self.obj17630.Copy=ATOM3Boolean()
      self.obj17630.Copy.setValue(('Copy from LHS', 1))
      self.obj17630.Copy.config = 0
      self.obj17630.Specify=ATOM3Constraint()
      self.obj17630.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1763.GGset2Any['MaxFlow']= self.obj17630
      self.obj17631= AttrCalc()
      self.obj17631.Copy=ATOM3Boolean()
      self.obj17631.Copy.setValue(('Copy from LHS', 1))
      self.obj17631.Copy.config = 0
      self.obj17631.Specify=ATOM3Constraint()
      self.obj17631.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1763.GGset2Any['Name']= self.obj17631
      self.obj17632= AttrCalc()
      self.obj17632.Copy=ATOM3Boolean()
      self.obj17632.Copy.setValue(('Copy from LHS', 1))
      self.obj17632.Copy.config = 0
      self.obj17632.Specify=ATOM3Constraint()
      self.obj17632.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1763.GGset2Any['ReqFlow']= self.obj17632

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1763)
      self.obj1763.postAction( self.RHS.CREATE )

      self.obj1764=operatingUnit(parent)
      self.obj1764.preAction( self.RHS.CREATE )
      self.obj1764.isGraphObjectVisual = True

      if(hasattr(self.obj1764, '_setHierarchicalLink')):
        self.obj1764._setHierarchicalLink(False)

      # OperCostProp
      self.obj1764.OperCostProp.setNone()

      # name
      self.obj1764.name.setValue('')
      self.obj1764.name.setNone()

      # OperCostFix
      self.obj1764.OperCostFix.setNone()

      self.obj1764.GGLabel.setValue(7)
      self.obj1764.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(280.0,100.0,self.obj1764)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1764.graphObject_ = new_obj
      self.obj17640= AttrCalc()
      self.obj17640.Copy=ATOM3Boolean()
      self.obj17640.Copy.setValue(('Copy from LHS', 1))
      self.obj17640.Copy.config = 0
      self.obj17640.Specify=ATOM3Constraint()
      self.obj17640.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1764.GGset2Any['OperCostProp']= self.obj17640
      self.obj17641= AttrCalc()
      self.obj17641.Copy=ATOM3Boolean()
      self.obj17641.Copy.setValue(('Copy from LHS', 1))
      self.obj17641.Copy.config = 0
      self.obj17641.Specify=ATOM3Constraint()
      self.obj17641.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1764.GGset2Any['name']= self.obj17641
      self.obj17642= AttrCalc()
      self.obj17642.Copy=ATOM3Boolean()
      self.obj17642.Copy.setValue(('Copy from LHS', 1))
      self.obj17642.Copy.config = 0
      self.obj17642.Specify=ATOM3Constraint()
      self.obj17642.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1764.GGset2Any['OperCostFix']= self.obj17642

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1764)
      self.obj1764.postAction( self.RHS.CREATE )

      self.obj1765=operatingUnit(parent)
      self.obj1765.preAction( self.RHS.CREATE )
      self.obj1765.isGraphObjectVisual = True

      if(hasattr(self.obj1765, '_setHierarchicalLink')):
        self.obj1765._setHierarchicalLink(False)

      # OperCostProp
      self.obj1765.OperCostProp.setNone()

      # name
      self.obj1765.name.setValue('')
      self.obj1765.name.setNone()

      # OperCostFix
      self.obj1765.OperCostFix.setNone()

      self.obj1765.GGLabel.setValue(12)
      self.obj1765.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(360.0,260.0,self.obj1765)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1765.graphObject_ = new_obj
      self.obj17650= AttrCalc()
      self.obj17650.Copy=ATOM3Boolean()
      self.obj17650.Copy.setValue(('Copy from LHS', 1))
      self.obj17650.Copy.config = 0
      self.obj17650.Specify=ATOM3Constraint()
      self.obj17650.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1765.GGset2Any['OperCostProp']= self.obj17650
      self.obj17651= AttrCalc()
      self.obj17651.Copy=ATOM3Boolean()
      self.obj17651.Copy.setValue(('Copy from LHS', 1))
      self.obj17651.Copy.config = 0
      self.obj17651.Specify=ATOM3Constraint()
      self.obj17651.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1765.GGset2Any['name']= self.obj17651
      self.obj17652= AttrCalc()
      self.obj17652.Copy=ATOM3Boolean()
      self.obj17652.Copy.setValue(('Copy from LHS', 1))
      self.obj17652.Copy.config = 0
      self.obj17652.Specify=ATOM3Constraint()
      self.obj17652.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1765.GGset2Any['OperCostFix']= self.obj17652

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1765)
      self.obj1765.postAction( self.RHS.CREATE )

      self.obj1766=fromRaw(parent)
      self.obj1766.preAction( self.RHS.CREATE )
      self.obj1766.isGraphObjectVisual = True

      if(hasattr(self.obj1766, '_setHierarchicalLink')):
        self.obj1766._setHierarchicalLink(False)

      # rate
      self.obj1766.rate.setNone()

      self.obj1766.GGLabel.setValue(8)
      self.obj1766.graphClass_= graph_fromRaw
      if parent.genGraphics:
         new_obj = graph_fromRaw(311.5,63.25,self.obj1766)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1766.graphObject_ = new_obj
      self.obj17660= AttrCalc()
      self.obj17660.Copy=ATOM3Boolean()
      self.obj17660.Copy.setValue(('Copy from LHS', 1))
      self.obj17660.Copy.config = 0
      self.obj17660.Specify=ATOM3Constraint()
      self.obj17660.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1766.GGset2Any['rate']= self.obj17660

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1766)
      self.obj1766.postAction( self.RHS.CREATE )

      self.obj1767=intoMaterial(parent)
      self.obj1767.preAction( self.RHS.CREATE )
      self.obj1767.isGraphObjectVisual = True

      if(hasattr(self.obj1767, '_setHierarchicalLink')):
        self.obj1767._setHierarchicalLink(False)

      # rate
      self.obj1767.rate.setValue(0.0)

      self.obj1767.GGLabel.setValue(17)
      self.obj1767.graphClass_= graph_intoMaterial
      if parent.genGraphics:
         new_obj = graph_intoMaterial(324.25,167.5,self.obj1767)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1767.graphObject_ = new_obj
      self.obj17670= AttrCalc()
      self.obj17670.Copy=ATOM3Boolean()
      self.obj17670.Copy.setValue(('Copy from LHS', 0))
      self.obj17670.Copy.config = 0
      self.obj17670.Specify=ATOM3Constraint()
      self.obj17670.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'a = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) ).name.getValue()\nb = self.getMatched ( graphID , self.LHS.nodeWithLabel(2) ).name.getValue()\nreturn self.graphRewritingSystem.Dictag[ a ][b]\n\n'))
      self.obj1767.GGset2Any['rate']= self.obj17670

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1767)
      self.obj1767.postAction( self.RHS.CREATE )

      self.obj1768=fromMaterial(parent)
      self.obj1768.preAction( self.RHS.CREATE )
      self.obj1768.isGraphObjectVisual = True

      if(hasattr(self.obj1768, '_setHierarchicalLink')):
        self.obj1768._setHierarchicalLink(False)

      # rate
      self.obj1768.rate.setNone()

      self.obj1768.GGLabel.setValue(14)
      self.obj1768.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(379.5,235.25,self.obj1768)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1768.graphObject_ = new_obj
      self.obj17680= AttrCalc()
      self.obj17680.Copy=ATOM3Boolean()
      self.obj17680.Copy.setValue(('Copy from LHS', 1))
      self.obj17680.Copy.config = 0
      self.obj17680.Specify=ATOM3Constraint()
      self.obj17680.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1768.GGset2Any['rate']= self.obj17680

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1768)
      self.obj1768.postAction( self.RHS.CREATE )

      self.obj1769=CapableOf(parent)
      self.obj1769.preAction( self.RHS.CREATE )
      self.obj1769.isGraphObjectVisual = True

      if(hasattr(self.obj1769, '_setHierarchicalLink')):
        self.obj1769._setHierarchicalLink(False)

      # rate
      self.obj1769.rate.setNone()

      self.obj1769.GGLabel.setValue(3)
      self.obj1769.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(84.5,131.5,self.obj1769)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1769.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1769)
      self.obj1769.postAction( self.RHS.CREATE )

      self.obj1770=Agent(parent)
      self.obj1770.preAction( self.RHS.CREATE )
      self.obj1770.isGraphObjectVisual = True

      if(hasattr(self.obj1770, '_setHierarchicalLink')):
        self.obj1770._setHierarchicalLink(False)

      # price
      self.obj1770.price.setNone()

      # name
      self.obj1770.name.setValue('')
      self.obj1770.name.setNone()

      self.obj1770.GGLabel.setValue(1)
      self.obj1770.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(60.0,20.0,self.obj1770)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1770.graphObject_ = new_obj
      self.obj17700= AttrCalc()
      self.obj17700.Copy=ATOM3Boolean()
      self.obj17700.Copy.setValue(('Copy from LHS', 1))
      self.obj17700.Copy.config = 0
      self.obj17700.Specify=ATOM3Constraint()
      self.obj17700.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1770.GGset2Any['price']= self.obj17700
      self.obj17701= AttrCalc()
      self.obj17701.Copy=ATOM3Boolean()
      self.obj17701.Copy.setValue(('Copy from LHS', 1))
      self.obj17701.Copy.config = 0
      self.obj17701.Specify=ATOM3Constraint()
      self.obj17701.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1770.GGset2Any['name']= self.obj17701

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1770)
      self.obj1770.postAction( self.RHS.CREATE )

      self.obj1771=Role(parent)
      self.obj1771.preAction( self.RHS.CREATE )
      self.obj1771.isGraphObjectVisual = True

      if(hasattr(self.obj1771, '_setHierarchicalLink')):
        self.obj1771._setHierarchicalLink(False)

      # name
      self.obj1771.name.setValue('')
      self.obj1771.name.setNone()

      self.obj1771.GGLabel.setValue(2)
      self.obj1771.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(60.0,180.0,self.obj1771)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1771.graphObject_ = new_obj
      self.obj17710= AttrCalc()
      self.obj17710.Copy=ATOM3Boolean()
      self.obj17710.Copy.setValue(('Copy from LHS', 1))
      self.obj17710.Copy.config = 0
      self.obj17710.Specify=ATOM3Constraint()
      self.obj17710.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1771.GGset2Any['name']= self.obj17710

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1771)
      self.obj1771.postAction( self.RHS.CREATE )

      self.obj1772=GenericGraphEdge(parent)
      self.obj1772.preAction( self.RHS.CREATE )
      self.obj1772.isGraphObjectVisual = True

      if(hasattr(self.obj1772, '_setHierarchicalLink')):
        self.obj1772._setHierarchicalLink(False)

      self.obj1772.GGLabel.setValue(15)
      self.obj1772.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(174.5,69.0,self.obj1772)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1772.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1772)
      self.obj1772.postAction( self.RHS.CREATE )

      self.obj1773=GenericGraphEdge(parent)
      self.obj1773.preAction( self.RHS.CREATE )
      self.obj1773.isGraphObjectVisual = True

      if(hasattr(self.obj1773, '_setHierarchicalLink')):
        self.obj1773._setHierarchicalLink(False)

      self.obj1773.GGLabel.setValue(10)
      self.obj1773.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(245.75,97.25,self.obj1773)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1773.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1773)
      self.obj1773.postAction( self.RHS.CREATE )

      self.obj1774=GenericGraphEdge(parent)
      self.obj1774.preAction( self.RHS.CREATE )
      self.obj1774.isGraphObjectVisual = True

      if(hasattr(self.obj1774, '_setHierarchicalLink')):
        self.obj1774._setHierarchicalLink(False)

      self.obj1774.GGLabel.setValue(13)
      self.obj1774.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(175.0,234.0,self.obj1774)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1774.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1774)
      self.obj1774.postAction( self.RHS.CREATE )

      self.obj1762.out_connections_.append(self.obj1766)
      self.obj1766.in_connections_.append(self.obj1762)
      self.obj1762.graphObject_.pendingConnections.append((self.obj1762.graphObject_.tag, self.obj1766.graphObject_.tag, [264.0, 50.0, 311.5, 63.25], 2, 0))
      self.obj1763.out_connections_.append(self.obj1768)
      self.obj1768.in_connections_.append(self.obj1763)
      self.obj1763.graphObject_.pendingConnections.append((self.obj1763.graphObject_.tag, self.obj1768.graphObject_.tag, [306.0, 210.0, 379.5, 235.25], 2, 0))
      self.obj1764.out_connections_.append(self.obj1767)
      self.obj1767.in_connections_.append(self.obj1764)
      self.obj1764.graphObject_.pendingConnections.append((self.obj1764.graphObject_.tag, self.obj1767.graphObject_.tag, [333.0, 108.0, 331.0, 142.0, 324.25, 167.5], 2, True))
      self.obj1766.out_connections_.append(self.obj1764)
      self.obj1764.in_connections_.append(self.obj1766)
      self.obj1766.graphObject_.pendingConnections.append((self.obj1766.graphObject_.tag, self.obj1764.graphObject_.tag, [330.0, 101.0, 311.5, 63.25], 2, 0))
      self.obj1767.out_connections_.append(self.obj1763)
      self.obj1763.in_connections_.append(self.obj1767)
      self.obj1767.graphObject_.pendingConnections.append((self.obj1767.graphObject_.tag, self.obj1763.graphObject_.tag, [306.0, 210.0, 317.5, 193.0, 324.25, 167.5], 2, True))
      self.obj1768.out_connections_.append(self.obj1765)
      self.obj1765.in_connections_.append(self.obj1768)
      self.obj1768.graphObject_.pendingConnections.append((self.obj1768.graphObject_.tag, self.obj1765.graphObject_.tag, [413.0, 268.0, 379.5, 235.25], 2, 0))
      self.obj1769.out_connections_.append(self.obj1771)
      self.obj1771.in_connections_.append(self.obj1769)
      self.obj1769.graphObject_.pendingConnections.append((self.obj1769.graphObject_.tag, self.obj1771.graphObject_.tag, [91.0, 180.0, 84.5, 131.5], 2, 0))
      self.obj1770.out_connections_.append(self.obj1769)
      self.obj1769.in_connections_.append(self.obj1770)
      self.obj1770.graphObject_.pendingConnections.append((self.obj1770.graphObject_.tag, self.obj1769.graphObject_.tag, [97.0, 82.0, 84.5, 131.5], 2, 0))
      self.obj1770.out_connections_.append(self.obj1772)
      self.obj1772.in_connections_.append(self.obj1770)
      self.obj1770.graphObject_.pendingConnections.append((self.obj1770.graphObject_.tag, self.obj1772.graphObject_.tag, [97.0, 82.0, 174.5, 69.0], 2, 0))
      self.obj1770.out_connections_.append(self.obj1773)
      self.obj1773.in_connections_.append(self.obj1770)
      self.obj1770.graphObject_.pendingConnections.append((self.obj1770.graphObject_.tag, self.obj1773.graphObject_.tag, [97.0, 82.0, 245.75, 97.25], 2, 0))
      self.obj1771.out_connections_.append(self.obj1774)
      self.obj1774.in_connections_.append(self.obj1771)
      self.obj1771.graphObject_.pendingConnections.append((self.obj1771.graphObject_.tag, self.obj1774.graphObject_.tag, [91.0, 225.0, 175.0, 234.0], 2, 0))
      self.obj1772.out_connections_.append(self.obj1762)
      self.obj1762.in_connections_.append(self.obj1772)
      self.obj1772.graphObject_.pendingConnections.append((self.obj1772.graphObject_.tag, self.obj1762.graphObject_.tag, [264.0, 50.0, 174.5, 69.0], 2, 0))
      self.obj1773.out_connections_.append(self.obj1764)
      self.obj1764.in_connections_.append(self.obj1773)
      self.obj1773.graphObject_.pendingConnections.append((self.obj1773.graphObject_.tag, self.obj1764.graphObject_.tag, [300.0, 101.0, 245.75, 97.25], 2, 0))
      self.obj1774.out_connections_.append(self.obj1763)
      self.obj1763.in_connections_.append(self.obj1774)
      self.obj1774.graphObject_.pendingConnections.append((self.obj1774.graphObject_.tag, self.obj1763.graphObject_.tag, [266.0, 242.0, 175.0, 234.0], 2, 0))

   def condition(self, graphID, isograph, atom3i):
      print 'Rule 21 '
      node7 = self.getMatched(graphID, self.LHS.nodeWithLabel(7))
      
      node11 = self.getMatched(graphID, self.LHS.nodeWithLabel(11))
      node1 = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      
      print node7.name.getValue()+' in '+ node11.Name.getValue() 
      print node7.name.getValue() in  node11.Name.getValue()
      
      
      test = not ( hasattr(node11, "linkAux2") and hasattr(node7, "linkAux2") )
      print test
      if test : 
       return (node7.name.getValue() in node11.Name.getValue() )
      else : 
       return False
      
      

   def action(self, graphID, isograph, atom3i):
      # code action of rule
      node = self.getMatched ( graphID , self.LHS.nodeWithLabel(7) )
      node.linkAux2 = True 
      node = self.getMatched ( graphID , self.LHS.nodeWithLabel(11) )
      node.linkAux2 = True 
      self.graphRewritingSystem.finalStat = 21
      
      

