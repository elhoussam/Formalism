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
      GGrule.__init__(self, 11)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_pns(parent)
      self.LHS.merge(ASG_omacs(parent))
      self.LHS.merge(ASG_GenericGraph(parent))

      self.obj178=rawMaterial(parent)
      self.obj178.preAction( self.LHS.CREATE )
      self.obj178.isGraphObjectVisual = True

      if(hasattr(self.obj178, '_setHierarchicalLink')):
        self.obj178._setHierarchicalLink(False)

      # MaxFlow
      self.obj178.MaxFlow.setValue(999999)

      # price
      self.obj178.price.setValue(0)

      # Name
      self.obj178.Name.setValue('')
      self.obj178.Name.setNone()

      # ReqFlow
      self.obj178.ReqFlow.setValue(0)

      self.obj178.GGLabel.setValue(3)
      self.obj178.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(220.0,20.0,self.obj178)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj178.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj178)
      self.obj178.postAction( self.LHS.CREATE )

      self.obj179=operatingUnit(parent)
      self.obj179.preAction( self.LHS.CREATE )
      self.obj179.isGraphObjectVisual = True

      if(hasattr(self.obj179, '_setHierarchicalLink')):
        self.obj179._setHierarchicalLink(False)

      # OperCostProp
      self.obj179.OperCostProp.setValue(0.0)

      # name
      self.obj179.name.setValue('')
      self.obj179.name.setNone()

      # OperCostFix
      self.obj179.OperCostFix.setValue(0.0)

      self.obj179.GGLabel.setValue(2)
      self.obj179.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(260.0,160.0,self.obj179)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj179.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj179)
      self.obj179.postAction( self.LHS.CREATE )

      self.obj180=Agent(parent)
      self.obj180.preAction( self.LHS.CREATE )
      self.obj180.isGraphObjectVisual = True

      if(hasattr(self.obj180, '_setHierarchicalLink')):
        self.obj180._setHierarchicalLink(False)

      # price
      self.obj180.price.setNone()

      # name
      self.obj180.name.setValue('')
      self.obj180.name.setNone()

      self.obj180.GGLabel.setValue(1)
      self.obj180.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(80.0,120.0,self.obj180)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj180.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj180)
      self.obj180.postAction( self.LHS.CREATE )

      self.obj181=GenericGraphEdge(parent)
      self.obj181.preAction( self.LHS.CREATE )
      self.obj181.isGraphObjectVisual = True

      if(hasattr(self.obj181, '_setHierarchicalLink')):
        self.obj181._setHierarchicalLink(False)

      self.obj181.GGLabel.setValue(4)
      self.obj181.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(181.75,114.0,self.obj181)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj181.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj181)
      self.obj181.postAction( self.LHS.CREATE )

      self.obj182=GenericGraphEdge(parent)
      self.obj182.preAction( self.LHS.CREATE )
      self.obj182.isGraphObjectVisual = True

      if(hasattr(self.obj182, '_setHierarchicalLink')):
        self.obj182._setHierarchicalLink(False)

      self.obj182.GGLabel.setValue(5)
      self.obj182.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(229.25,150.25,self.obj182)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj182.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj182)
      self.obj182.postAction( self.LHS.CREATE )

      self.obj180.out_connections_.append(self.obj181)
      self.obj181.in_connections_.append(self.obj180)
      self.obj180.graphObject_.pendingConnections.append((self.obj180.graphObject_.tag, self.obj181.graphObject_.tag, [105.0, 182.0, 147.0, 140.5, 181.75, 114.0], 2, True))
      self.obj180.out_connections_.append(self.obj182)
      self.obj182.in_connections_.append(self.obj180)
      self.obj180.graphObject_.pendingConnections.append((self.obj180.graphObject_.tag, self.obj182.graphObject_.tag, [105.0, 182.0, 185.5, 153.0, 229.25, 150.25], 2, True))
      self.obj181.out_connections_.append(self.obj178)
      self.obj178.in_connections_.append(self.obj181)
      self.obj181.graphObject_.pendingConnections.append((self.obj181.graphObject_.tag, self.obj178.graphObject_.tag, [244.0, 76.0, 216.5, 87.5, 181.75, 114.0], 2, True))
      self.obj182.out_connections_.append(self.obj179)
      self.obj179.in_connections_.append(self.obj182)
      self.obj182.graphObject_.pendingConnections.append((self.obj182.graphObject_.tag, self.obj179.graphObject_.tag, [280.0, 171.0, 273.0, 147.5, 229.25, 150.25], 2, True))

      self.RHS = ASG_pns(parent)
      self.RHS.merge(ASG_omacs(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj186=rawMaterial(parent)
      self.obj186.preAction( self.RHS.CREATE )
      self.obj186.isGraphObjectVisual = True

      if(hasattr(self.obj186, '_setHierarchicalLink')):
        self.obj186._setHierarchicalLink(False)

      # MaxFlow
      self.obj186.MaxFlow.setValue(999999)

      # price
      self.obj186.price.setValue(0)

      # Name
      self.obj186.Name.setValue('')
      self.obj186.Name.setNone()

      # ReqFlow
      self.obj186.ReqFlow.setValue(0)

      self.obj186.GGLabel.setValue(3)
      self.obj186.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(220.0,20.0,self.obj186)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj186.graphObject_ = new_obj
      self.obj1860= AttrCalc()
      self.obj1860.Copy=ATOM3Boolean()
      self.obj1860.Copy.setValue(('Copy from LHS', 1))
      self.obj1860.Copy.config = 0
      self.obj1860.Specify=ATOM3Constraint()
      self.obj1860.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj186.GGset2Any['MaxFlow']= self.obj1860
      self.obj1861= AttrCalc()
      self.obj1861.Copy=ATOM3Boolean()
      self.obj1861.Copy.setValue(('Copy from LHS', 1))
      self.obj1861.Copy.config = 0
      self.obj1861.Specify=ATOM3Constraint()
      self.obj1861.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj186.GGset2Any['Name']= self.obj1861
      self.obj1862= AttrCalc()
      self.obj1862.Copy=ATOM3Boolean()
      self.obj1862.Copy.setValue(('Copy from LHS', 1))
      self.obj1862.Copy.config = 0
      self.obj1862.Specify=ATOM3Constraint()
      self.obj1862.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj186.GGset2Any['ReqFlow']= self.obj1862

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj186)
      self.obj186.postAction( self.RHS.CREATE )

      self.obj187=operatingUnit(parent)
      self.obj187.preAction( self.RHS.CREATE )
      self.obj187.isGraphObjectVisual = True

      if(hasattr(self.obj187, '_setHierarchicalLink')):
        self.obj187._setHierarchicalLink(False)

      # OperCostProp
      self.obj187.OperCostProp.setValue(0.0)

      # name
      self.obj187.name.setValue('')
      self.obj187.name.setNone()

      # OperCostFix
      self.obj187.OperCostFix.setValue(0.0)

      self.obj187.GGLabel.setValue(2)
      self.obj187.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(260.0,160.0,self.obj187)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj187.graphObject_ = new_obj
      self.obj1870= AttrCalc()
      self.obj1870.Copy=ATOM3Boolean()
      self.obj1870.Copy.setValue(('Copy from LHS', 1))
      self.obj1870.Copy.config = 0
      self.obj1870.Specify=ATOM3Constraint()
      self.obj1870.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj187.GGset2Any['OperCostProp']= self.obj1870
      self.obj1871= AttrCalc()
      self.obj1871.Copy=ATOM3Boolean()
      self.obj1871.Copy.setValue(('Copy from LHS', 1))
      self.obj1871.Copy.config = 0
      self.obj1871.Specify=ATOM3Constraint()
      self.obj1871.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj187.GGset2Any['name']= self.obj1871
      self.obj1872= AttrCalc()
      self.obj1872.Copy=ATOM3Boolean()
      self.obj1872.Copy.setValue(('Copy from LHS', 1))
      self.obj1872.Copy.config = 0
      self.obj1872.Specify=ATOM3Constraint()
      self.obj1872.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj187.GGset2Any['OperCostFix']= self.obj1872

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj187)
      self.obj187.postAction( self.RHS.CREATE )

      self.obj188=fromRaw(parent)
      self.obj188.preAction( self.RHS.CREATE )
      self.obj188.isGraphObjectVisual = True

      if(hasattr(self.obj188, '_setHierarchicalLink')):
        self.obj188._setHierarchicalLink(False)

      # rate
      self.obj188.rate.setValue(1.0)

      self.obj188.GGLabel.setValue(7)
      self.obj188.graphClass_= graph_fromRaw
      if parent.genGraphics:
         new_obj = graph_fromRaw(262.0,115.5,self.obj188)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj188.graphObject_ = new_obj
      self.obj1880= AttrCalc()
      self.obj1880.Copy=ATOM3Boolean()
      self.obj1880.Copy.setValue(('Copy from LHS', 0))
      self.obj1880.Copy.config = 0
      self.obj1880.Specify=ATOM3Constraint()
      self.obj1880.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj188.GGset2Any['rate']= self.obj1880

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj188)
      self.obj188.postAction( self.RHS.CREATE )

      self.obj189=Agent(parent)
      self.obj189.preAction( self.RHS.CREATE )
      self.obj189.isGraphObjectVisual = True

      if(hasattr(self.obj189, '_setHierarchicalLink')):
        self.obj189._setHierarchicalLink(False)

      # price
      self.obj189.price.setNone()

      # name
      self.obj189.name.setValue('')
      self.obj189.name.setNone()

      self.obj189.GGLabel.setValue(1)
      self.obj189.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(80.0,120.0,self.obj189)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj189.graphObject_ = new_obj
      self.obj1890= AttrCalc()
      self.obj1890.Copy=ATOM3Boolean()
      self.obj1890.Copy.setValue(('Copy from LHS', 1))
      self.obj1890.Copy.config = 0
      self.obj1890.Specify=ATOM3Constraint()
      self.obj1890.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj189.GGset2Any['price']= self.obj1890
      self.obj1891= AttrCalc()
      self.obj1891.Copy=ATOM3Boolean()
      self.obj1891.Copy.setValue(('Copy from LHS', 1))
      self.obj1891.Copy.config = 0
      self.obj1891.Specify=ATOM3Constraint()
      self.obj1891.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj189.GGset2Any['name']= self.obj1891

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj189)
      self.obj189.postAction( self.RHS.CREATE )

      self.obj190=GenericGraphEdge(parent)
      self.obj190.preAction( self.RHS.CREATE )
      self.obj190.isGraphObjectVisual = True

      if(hasattr(self.obj190, '_setHierarchicalLink')):
        self.obj190._setHierarchicalLink(False)

      self.obj190.GGLabel.setValue(4)
      self.obj190.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(181.75,114.0,self.obj190)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj190.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj190)
      self.obj190.postAction( self.RHS.CREATE )

      self.obj191=GenericGraphEdge(parent)
      self.obj191.preAction( self.RHS.CREATE )
      self.obj191.isGraphObjectVisual = True

      if(hasattr(self.obj191, '_setHierarchicalLink')):
        self.obj191._setHierarchicalLink(False)

      self.obj191.GGLabel.setValue(5)
      self.obj191.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(229.25,150.25,self.obj191)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj191.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj191)
      self.obj191.postAction( self.RHS.CREATE )

      self.obj186.out_connections_.append(self.obj188)
      self.obj188.in_connections_.append(self.obj186)
      self.obj186.graphObject_.pendingConnections.append((self.obj186.graphObject_.tag, self.obj188.graphObject_.tag, [244.0, 70.0, 262.0, 115.5], 0, True))
      self.obj188.out_connections_.append(self.obj187)
      self.obj187.in_connections_.append(self.obj188)
      self.obj188.graphObject_.pendingConnections.append((self.obj188.graphObject_.tag, self.obj187.graphObject_.tag, [280.0, 161.0, 262.0, 115.5], 0, True))
      self.obj189.out_connections_.append(self.obj190)
      self.obj190.in_connections_.append(self.obj189)
      self.obj189.graphObject_.pendingConnections.append((self.obj189.graphObject_.tag, self.obj190.graphObject_.tag, [117.0, 182.0, 181.75, 114.0], 2, 0))
      self.obj189.out_connections_.append(self.obj191)
      self.obj191.in_connections_.append(self.obj189)
      self.obj189.graphObject_.pendingConnections.append((self.obj189.graphObject_.tag, self.obj191.graphObject_.tag, [117.0, 182.0, 229.25, 150.25], 2, 0))
      self.obj190.out_connections_.append(self.obj186)
      self.obj186.in_connections_.append(self.obj190)
      self.obj190.graphObject_.pendingConnections.append((self.obj190.graphObject_.tag, self.obj186.graphObject_.tag, [244.0, 70.0, 181.75, 114.0], 2, 0))
      self.obj191.out_connections_.append(self.obj187)
      self.obj187.in_connections_.append(self.obj191)
      self.obj191.graphObject_.pendingConnections.append((self.obj191.graphObject_.tag, self.obj187.graphObject_.tag, [280.0, 161.0, 229.25, 150.25], 2, 0))

   def condition(self, graphID, isograph, atom3i):
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(2))
      return not hasattr(node, "LinkRaw2AR")
      

   def action(self, graphID, isograph, atom3i):
      node = self.getMatched ( graphID , self.LHS.nodeWithLabel(2) )
      node.LinkRaw2AR = True
      
      

