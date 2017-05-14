# _ CreatLinkRaw2AR_GG_rule.py ____________________________________________________________________________
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
class CreatLinkRaw2AR_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 12)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_pns(parent)
      self.LHS.merge(ASG_omacs(parent))
      self.LHS.merge(ASG_GenericGraph(parent))

      self.obj1651=rawMaterial(parent)
      self.obj1651.preAction( self.LHS.CREATE )
      self.obj1651.isGraphObjectVisual = True

      if(hasattr(self.obj1651, '_setHierarchicalLink')):
        self.obj1651._setHierarchicalLink(False)

      # MaxFlow
      self.obj1651.MaxFlow.setValue(999999)

      # price
      self.obj1651.price.setValue(0)

      # Name
      self.obj1651.Name.setValue('')
      self.obj1651.Name.setNone()

      # ReqFlow
      self.obj1651.ReqFlow.setValue(0)

      self.obj1651.GGLabel.setValue(3)
      self.obj1651.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(220.0,20.0,self.obj1651)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1651.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1651)
      self.obj1651.postAction( self.LHS.CREATE )

      self.obj1652=operatingUnit(parent)
      self.obj1652.preAction( self.LHS.CREATE )
      self.obj1652.isGraphObjectVisual = True

      if(hasattr(self.obj1652, '_setHierarchicalLink')):
        self.obj1652._setHierarchicalLink(False)

      # OperCostProp
      self.obj1652.OperCostProp.setValue(0.0)

      # name
      self.obj1652.name.setValue('')
      self.obj1652.name.setNone()

      # OperCostFix
      self.obj1652.OperCostFix.setValue(0.0)

      self.obj1652.GGLabel.setValue(2)
      self.obj1652.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(260.0,160.0,self.obj1652)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1652.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1652)
      self.obj1652.postAction( self.LHS.CREATE )

      self.obj1653=Agent(parent)
      self.obj1653.preAction( self.LHS.CREATE )
      self.obj1653.isGraphObjectVisual = True

      if(hasattr(self.obj1653, '_setHierarchicalLink')):
        self.obj1653._setHierarchicalLink(False)

      # price
      self.obj1653.price.setNone()

      # name
      self.obj1653.name.setValue('')
      self.obj1653.name.setNone()

      self.obj1653.GGLabel.setValue(1)
      self.obj1653.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(80.0,120.0,self.obj1653)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1653.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1653)
      self.obj1653.postAction( self.LHS.CREATE )

      self.obj1654=GenericGraphEdge(parent)
      self.obj1654.preAction( self.LHS.CREATE )
      self.obj1654.isGraphObjectVisual = True

      if(hasattr(self.obj1654, '_setHierarchicalLink')):
        self.obj1654._setHierarchicalLink(False)

      self.obj1654.GGLabel.setValue(4)
      self.obj1654.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(181.75,114.0,self.obj1654)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1654.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1654)
      self.obj1654.postAction( self.LHS.CREATE )

      self.obj1655=GenericGraphEdge(parent)
      self.obj1655.preAction( self.LHS.CREATE )
      self.obj1655.isGraphObjectVisual = True

      if(hasattr(self.obj1655, '_setHierarchicalLink')):
        self.obj1655._setHierarchicalLink(False)

      self.obj1655.GGLabel.setValue(5)
      self.obj1655.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(229.25,150.25,self.obj1655)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1655.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1655)
      self.obj1655.postAction( self.LHS.CREATE )

      self.obj1653.out_connections_.append(self.obj1654)
      self.obj1654.in_connections_.append(self.obj1653)
      self.obj1653.graphObject_.pendingConnections.append((self.obj1653.graphObject_.tag, self.obj1654.graphObject_.tag, [105.0, 182.0, 147.0, 140.5, 181.75, 114.0], 2, True))
      self.obj1653.out_connections_.append(self.obj1655)
      self.obj1655.in_connections_.append(self.obj1653)
      self.obj1653.graphObject_.pendingConnections.append((self.obj1653.graphObject_.tag, self.obj1655.graphObject_.tag, [105.0, 182.0, 185.5, 153.0, 229.25, 150.25], 2, True))
      self.obj1654.out_connections_.append(self.obj1651)
      self.obj1651.in_connections_.append(self.obj1654)
      self.obj1654.graphObject_.pendingConnections.append((self.obj1654.graphObject_.tag, self.obj1651.graphObject_.tag, [244.0, 76.0, 216.5, 87.5, 181.75, 114.0], 2, True))
      self.obj1655.out_connections_.append(self.obj1652)
      self.obj1652.in_connections_.append(self.obj1655)
      self.obj1655.graphObject_.pendingConnections.append((self.obj1655.graphObject_.tag, self.obj1652.graphObject_.tag, [280.0, 171.0, 273.0, 147.5, 229.25, 150.25], 2, True))

      self.RHS = ASG_pns(parent)
      self.RHS.merge(ASG_omacs(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj1659=rawMaterial(parent)
      self.obj1659.preAction( self.RHS.CREATE )
      self.obj1659.isGraphObjectVisual = True

      if(hasattr(self.obj1659, '_setHierarchicalLink')):
        self.obj1659._setHierarchicalLink(False)

      # MaxFlow
      self.obj1659.MaxFlow.setValue(999999)

      # price
      self.obj1659.price.setValue(0)

      # Name
      self.obj1659.Name.setValue('')
      self.obj1659.Name.setNone()

      # ReqFlow
      self.obj1659.ReqFlow.setValue(0)

      self.obj1659.GGLabel.setValue(3)
      self.obj1659.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(220.0,20.0,self.obj1659)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1659.graphObject_ = new_obj
      self.obj16590= AttrCalc()
      self.obj16590.Copy=ATOM3Boolean()
      self.obj16590.Copy.setValue(('Copy from LHS', 1))
      self.obj16590.Copy.config = 0
      self.obj16590.Specify=ATOM3Constraint()
      self.obj16590.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1659.GGset2Any['MaxFlow']= self.obj16590
      self.obj16591= AttrCalc()
      self.obj16591.Copy=ATOM3Boolean()
      self.obj16591.Copy.setValue(('Copy from LHS', 1))
      self.obj16591.Copy.config = 0
      self.obj16591.Specify=ATOM3Constraint()
      self.obj16591.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1659.GGset2Any['Name']= self.obj16591
      self.obj16592= AttrCalc()
      self.obj16592.Copy=ATOM3Boolean()
      self.obj16592.Copy.setValue(('Copy from LHS', 1))
      self.obj16592.Copy.config = 0
      self.obj16592.Specify=ATOM3Constraint()
      self.obj16592.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1659.GGset2Any['ReqFlow']= self.obj16592

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1659)
      self.obj1659.postAction( self.RHS.CREATE )

      self.obj1660=operatingUnit(parent)
      self.obj1660.preAction( self.RHS.CREATE )
      self.obj1660.isGraphObjectVisual = True

      if(hasattr(self.obj1660, '_setHierarchicalLink')):
        self.obj1660._setHierarchicalLink(False)

      # OperCostProp
      self.obj1660.OperCostProp.setValue(0.0)

      # name
      self.obj1660.name.setValue('')
      self.obj1660.name.setNone()

      # OperCostFix
      self.obj1660.OperCostFix.setValue(0.0)

      self.obj1660.GGLabel.setValue(2)
      self.obj1660.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(260.0,160.0,self.obj1660)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1660.graphObject_ = new_obj
      self.obj16600= AttrCalc()
      self.obj16600.Copy=ATOM3Boolean()
      self.obj16600.Copy.setValue(('Copy from LHS', 1))
      self.obj16600.Copy.config = 0
      self.obj16600.Specify=ATOM3Constraint()
      self.obj16600.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1660.GGset2Any['OperCostProp']= self.obj16600
      self.obj16601= AttrCalc()
      self.obj16601.Copy=ATOM3Boolean()
      self.obj16601.Copy.setValue(('Copy from LHS', 1))
      self.obj16601.Copy.config = 0
      self.obj16601.Specify=ATOM3Constraint()
      self.obj16601.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1660.GGset2Any['name']= self.obj16601
      self.obj16602= AttrCalc()
      self.obj16602.Copy=ATOM3Boolean()
      self.obj16602.Copy.setValue(('Copy from LHS', 1))
      self.obj16602.Copy.config = 0
      self.obj16602.Specify=ATOM3Constraint()
      self.obj16602.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1660.GGset2Any['OperCostFix']= self.obj16602

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1660)
      self.obj1660.postAction( self.RHS.CREATE )

      self.obj1661=fromRaw(parent)
      self.obj1661.preAction( self.RHS.CREATE )
      self.obj1661.isGraphObjectVisual = True

      if(hasattr(self.obj1661, '_setHierarchicalLink')):
        self.obj1661._setHierarchicalLink(False)

      # rate
      self.obj1661.rate.setValue(1.0)

      self.obj1661.GGLabel.setValue(7)
      self.obj1661.graphClass_= graph_fromRaw
      if parent.genGraphics:
         new_obj = graph_fromRaw(262.0,115.5,self.obj1661)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1661.graphObject_ = new_obj
      self.obj16610= AttrCalc()
      self.obj16610.Copy=ATOM3Boolean()
      self.obj16610.Copy.setValue(('Copy from LHS', 0))
      self.obj16610.Copy.config = 0
      self.obj16610.Specify=ATOM3Constraint()
      self.obj16610.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1661.GGset2Any['rate']= self.obj16610

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1661)
      self.obj1661.postAction( self.RHS.CREATE )

      self.obj1662=Agent(parent)
      self.obj1662.preAction( self.RHS.CREATE )
      self.obj1662.isGraphObjectVisual = True

      if(hasattr(self.obj1662, '_setHierarchicalLink')):
        self.obj1662._setHierarchicalLink(False)

      # price
      self.obj1662.price.setNone()

      # name
      self.obj1662.name.setValue('')
      self.obj1662.name.setNone()

      self.obj1662.GGLabel.setValue(1)
      self.obj1662.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(80.0,120.0,self.obj1662)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1662.graphObject_ = new_obj
      self.obj16620= AttrCalc()
      self.obj16620.Copy=ATOM3Boolean()
      self.obj16620.Copy.setValue(('Copy from LHS', 1))
      self.obj16620.Copy.config = 0
      self.obj16620.Specify=ATOM3Constraint()
      self.obj16620.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1662.GGset2Any['price']= self.obj16620
      self.obj16621= AttrCalc()
      self.obj16621.Copy=ATOM3Boolean()
      self.obj16621.Copy.setValue(('Copy from LHS', 1))
      self.obj16621.Copy.config = 0
      self.obj16621.Specify=ATOM3Constraint()
      self.obj16621.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1662.GGset2Any['name']= self.obj16621

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1662)
      self.obj1662.postAction( self.RHS.CREATE )

      self.obj1663=GenericGraphEdge(parent)
      self.obj1663.preAction( self.RHS.CREATE )
      self.obj1663.isGraphObjectVisual = True

      if(hasattr(self.obj1663, '_setHierarchicalLink')):
        self.obj1663._setHierarchicalLink(False)

      self.obj1663.GGLabel.setValue(4)
      self.obj1663.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(181.75,114.0,self.obj1663)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1663.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1663)
      self.obj1663.postAction( self.RHS.CREATE )

      self.obj1664=GenericGraphEdge(parent)
      self.obj1664.preAction( self.RHS.CREATE )
      self.obj1664.isGraphObjectVisual = True

      if(hasattr(self.obj1664, '_setHierarchicalLink')):
        self.obj1664._setHierarchicalLink(False)

      self.obj1664.GGLabel.setValue(5)
      self.obj1664.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(229.25,150.25,self.obj1664)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1664.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1664)
      self.obj1664.postAction( self.RHS.CREATE )

      self.obj1659.out_connections_.append(self.obj1661)
      self.obj1661.in_connections_.append(self.obj1659)
      self.obj1659.graphObject_.pendingConnections.append((self.obj1659.graphObject_.tag, self.obj1661.graphObject_.tag, [244.0, 70.0, 262.0, 115.5], 0, True))
      self.obj1661.out_connections_.append(self.obj1660)
      self.obj1660.in_connections_.append(self.obj1661)
      self.obj1661.graphObject_.pendingConnections.append((self.obj1661.graphObject_.tag, self.obj1660.graphObject_.tag, [280.0, 161.0, 262.0, 115.5], 0, True))
      self.obj1662.out_connections_.append(self.obj1663)
      self.obj1663.in_connections_.append(self.obj1662)
      self.obj1662.graphObject_.pendingConnections.append((self.obj1662.graphObject_.tag, self.obj1663.graphObject_.tag, [117.0, 182.0, 181.75, 114.0], 2, 0))
      self.obj1662.out_connections_.append(self.obj1664)
      self.obj1664.in_connections_.append(self.obj1662)
      self.obj1662.graphObject_.pendingConnections.append((self.obj1662.graphObject_.tag, self.obj1664.graphObject_.tag, [117.0, 182.0, 229.25, 150.25], 2, 0))
      self.obj1663.out_connections_.append(self.obj1659)
      self.obj1659.in_connections_.append(self.obj1663)
      self.obj1663.graphObject_.pendingConnections.append((self.obj1663.graphObject_.tag, self.obj1659.graphObject_.tag, [244.0, 70.0, 181.75, 114.0], 2, 0))
      self.obj1664.out_connections_.append(self.obj1660)
      self.obj1660.in_connections_.append(self.obj1664)
      self.obj1664.graphObject_.pendingConnections.append((self.obj1664.graphObject_.tag, self.obj1660.graphObject_.tag, [280.0, 161.0, 229.25, 150.25], 2, 0))

   def condition(self, graphID, isograph, atom3i):
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(2))
      return not hasattr(node, "LinkRaw2AR")
      

   def action(self, graphID, isograph, atom3i):
      node = self.getMatched ( graphID , self.LHS.nodeWithLabel(2) )
      node.LinkRaw2AR = True
      
      

