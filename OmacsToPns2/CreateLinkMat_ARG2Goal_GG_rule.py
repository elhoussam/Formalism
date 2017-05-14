# _ CreateLinkMat_ARG2Goal_GG_rule.py ____________________________________________________________________________
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
class CreateLinkMat_ARG2Goal_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 19)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_pns(parent)
      self.LHS.merge(ASG_omacs(parent))
      self.LHS.merge(ASG_GenericGraph(parent))

      self.obj1719=metarial(parent)
      self.obj1719.preAction( self.LHS.CREATE )
      self.obj1719.isGraphObjectVisual = True

      if(hasattr(self.obj1719, '_setHierarchicalLink')):
        self.obj1719._setHierarchicalLink(False)

      # MaxFlow
      self.obj1719.MaxFlow.setNone()

      # price
      self.obj1719.price.setValue(0)

      # Name
      self.obj1719.Name.setValue('')
      self.obj1719.Name.setNone()

      # ReqFlow
      self.obj1719.ReqFlow.setNone()

      self.obj1719.GGLabel.setValue(4)
      self.obj1719.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(240.0,20.0,self.obj1719)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1719.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1719)
      self.obj1719.postAction( self.LHS.CREATE )

      self.obj1720=metarial(parent)
      self.obj1720.preAction( self.LHS.CREATE )
      self.obj1720.isGraphObjectVisual = True

      if(hasattr(self.obj1720, '_setHierarchicalLink')):
        self.obj1720._setHierarchicalLink(False)

      # MaxFlow
      self.obj1720.MaxFlow.setNone()

      # price
      self.obj1720.price.setValue(0)

      # Name
      self.obj1720.Name.setValue('')
      self.obj1720.Name.setNone()

      # ReqFlow
      self.obj1720.ReqFlow.setNone()

      self.obj1720.GGLabel.setValue(6)
      self.obj1720.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(240.0,240.0,self.obj1720)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1720.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1720)
      self.obj1720.postAction( self.LHS.CREATE )

      self.obj1721=operatingUnit(parent)
      self.obj1721.preAction( self.LHS.CREATE )
      self.obj1721.isGraphObjectVisual = True

      if(hasattr(self.obj1721, '_setHierarchicalLink')):
        self.obj1721._setHierarchicalLink(False)

      # OperCostProp
      self.obj1721.OperCostProp.setNone()

      # name
      self.obj1721.name.setValue('')
      self.obj1721.name.setNone()

      # OperCostFix
      self.obj1721.OperCostFix.setNone()

      self.obj1721.GGLabel.setValue(5)
      self.obj1721.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(240.0,140.0,self.obj1721)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1721.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1721)
      self.obj1721.postAction( self.LHS.CREATE )

      self.obj1722=fromMaterial(parent)
      self.obj1722.preAction( self.LHS.CREATE )
      self.obj1722.isGraphObjectVisual = True

      if(hasattr(self.obj1722, '_setHierarchicalLink')):
        self.obj1722._setHierarchicalLink(False)

      # rate
      self.obj1722.rate.setNone()

      self.obj1722.GGLabel.setValue(8)
      self.obj1722.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(265.0,100.0,self.obj1722)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1722.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1722)
      self.obj1722.postAction( self.LHS.CREATE )

      self.obj1723=Goal(parent)
      self.obj1723.preAction( self.LHS.CREATE )
      self.obj1723.isGraphObjectVisual = True

      if(hasattr(self.obj1723, '_setHierarchicalLink')):
        self.obj1723._setHierarchicalLink(False)

      # name
      self.obj1723.name.setValue('')
      self.obj1723.name.setNone()

      self.obj1723.GGLabel.setValue(2)
      self.obj1723.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(60.0,220.0,self.obj1723)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1723.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1723)
      self.obj1723.postAction( self.LHS.CREATE )

      self.obj1724=Role(parent)
      self.obj1724.preAction( self.LHS.CREATE )
      self.obj1724.isGraphObjectVisual = True

      if(hasattr(self.obj1724, '_setHierarchicalLink')):
        self.obj1724._setHierarchicalLink(False)

      # name
      self.obj1724.name.setValue('')
      self.obj1724.name.setNone()

      self.obj1724.GGLabel.setValue(1)
      self.obj1724.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(60.0,40.0,self.obj1724)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1724.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1724)
      self.obj1724.postAction( self.LHS.CREATE )

      self.obj1725=achieve(parent)
      self.obj1725.preAction( self.LHS.CREATE )
      self.obj1725.isGraphObjectVisual = True

      if(hasattr(self.obj1725, '_setHierarchicalLink')):
        self.obj1725._setHierarchicalLink(False)

      # rate
      self.obj1725.rate.setNone()

      self.obj1725.GGLabel.setValue(3)
      self.obj1725.graphClass_= graph_achieve
      if parent.genGraphics:
         new_obj = graph_achieve(97.5,137.5,self.obj1725)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1725.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1725)
      self.obj1725.postAction( self.LHS.CREATE )

      self.obj1726=GenericGraphEdge(parent)
      self.obj1726.preAction( self.LHS.CREATE )
      self.obj1726.isGraphObjectVisual = True

      if(hasattr(self.obj1726, '_setHierarchicalLink')):
        self.obj1726._setHierarchicalLink(False)

      self.obj1726.GGLabel.setValue(7)
      self.obj1726.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(215.0,41.5,self.obj1726)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1726.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1726)
      self.obj1726.postAction( self.LHS.CREATE )

      self.obj1727=GenericGraphEdge(parent)
      self.obj1727.preAction( self.LHS.CREATE )
      self.obj1727.isGraphObjectVisual = True

      if(hasattr(self.obj1727, '_setHierarchicalLink')):
        self.obj1727._setHierarchicalLink(False)

      self.obj1727.GGLabel.setValue(9)
      self.obj1727.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(185.0,276.0,self.obj1727)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1727.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1727)
      self.obj1727.postAction( self.LHS.CREATE )

      self.obj1719.out_connections_.append(self.obj1722)
      self.obj1722.in_connections_.append(self.obj1719)
      self.obj1719.graphObject_.pendingConnections.append((self.obj1719.graphObject_.tag, self.obj1722.graphObject_.tag, [264.0, 69.0, 265.0, 100.0], 0, True))
      self.obj1722.out_connections_.append(self.obj1721)
      self.obj1721.in_connections_.append(self.obj1722)
      self.obj1722.graphObject_.pendingConnections.append((self.obj1722.graphObject_.tag, self.obj1721.graphObject_.tag, [260.0, 151.0, 352.0, 90.0], 0, True))
      self.obj1723.out_connections_.append(self.obj1727)
      self.obj1727.in_connections_.append(self.obj1723)
      self.obj1723.graphObject_.pendingConnections.append((self.obj1723.graphObject_.tag, self.obj1727.graphObject_.tag, [84.0, 270.0, 185.0, 276.0], 0, True))
      self.obj1724.out_connections_.append(self.obj1725)
      self.obj1725.in_connections_.append(self.obj1724)
      self.obj1724.graphObject_.pendingConnections.append((self.obj1724.graphObject_.tag, self.obj1725.graphObject_.tag, [84.0, 86.0, 97.5, 137.5], 0, True))
      self.obj1724.out_connections_.append(self.obj1726)
      self.obj1726.in_connections_.append(self.obj1724)
      self.obj1724.graphObject_.pendingConnections.append((self.obj1724.graphObject_.tag, self.obj1726.graphObject_.tag, [84.0, 41.0, 215.0, 41.5], 0, True))
      self.obj1725.out_connections_.append(self.obj1723)
      self.obj1723.in_connections_.append(self.obj1725)
      self.obj1725.graphObject_.pendingConnections.append((self.obj1725.graphObject_.tag, self.obj1723.graphObject_.tag, [83.0, 221.0, 93.5, 143.5], 0, True))
      self.obj1726.out_connections_.append(self.obj1719)
      self.obj1719.in_connections_.append(self.obj1726)
      self.obj1726.graphObject_.pendingConnections.append((self.obj1726.graphObject_.tag, self.obj1719.graphObject_.tag, [246.0, 62.0, 215.0, 41.5], 0, True))
      self.obj1727.out_connections_.append(self.obj1720)
      self.obj1720.in_connections_.append(self.obj1727)
      self.obj1727.graphObject_.pendingConnections.append((self.obj1727.graphObject_.tag, self.obj1720.graphObject_.tag, [246.0, 282.0, 185.0, 276.0], 0, True))

      self.RHS = ASG_pns(parent)
      self.RHS.merge(ASG_omacs(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj1731=metarial(parent)
      self.obj1731.preAction( self.RHS.CREATE )
      self.obj1731.isGraphObjectVisual = True

      if(hasattr(self.obj1731, '_setHierarchicalLink')):
        self.obj1731._setHierarchicalLink(False)

      # MaxFlow
      self.obj1731.MaxFlow.setNone()

      # price
      self.obj1731.price.setValue(0)

      # Name
      self.obj1731.Name.setValue('')
      self.obj1731.Name.setNone()

      # ReqFlow
      self.obj1731.ReqFlow.setNone()

      self.obj1731.GGLabel.setValue(4)
      self.obj1731.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(280.0,20.0,self.obj1731)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1731.graphObject_ = new_obj
      self.obj17310= AttrCalc()
      self.obj17310.Copy=ATOM3Boolean()
      self.obj17310.Copy.setValue(('Copy from LHS', 1))
      self.obj17310.Copy.config = 0
      self.obj17310.Specify=ATOM3Constraint()
      self.obj17310.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1731.GGset2Any['MaxFlow']= self.obj17310
      self.obj17311= AttrCalc()
      self.obj17311.Copy=ATOM3Boolean()
      self.obj17311.Copy.setValue(('Copy from LHS', 1))
      self.obj17311.Copy.config = 0
      self.obj17311.Specify=ATOM3Constraint()
      self.obj17311.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1731.GGset2Any['Name']= self.obj17311
      self.obj17312= AttrCalc()
      self.obj17312.Copy=ATOM3Boolean()
      self.obj17312.Copy.setValue(('Copy from LHS', 1))
      self.obj17312.Copy.config = 0
      self.obj17312.Specify=ATOM3Constraint()
      self.obj17312.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1731.GGset2Any['ReqFlow']= self.obj17312

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1731)
      self.obj1731.postAction( self.RHS.CREATE )

      self.obj1732=metarial(parent)
      self.obj1732.preAction( self.RHS.CREATE )
      self.obj1732.isGraphObjectVisual = True

      if(hasattr(self.obj1732, '_setHierarchicalLink')):
        self.obj1732._setHierarchicalLink(False)

      # MaxFlow
      self.obj1732.MaxFlow.setNone()

      # price
      self.obj1732.price.setValue(0)

      # Name
      self.obj1732.Name.setValue('')
      self.obj1732.Name.setNone()

      # ReqFlow
      self.obj1732.ReqFlow.setNone()

      self.obj1732.GGLabel.setValue(6)
      self.obj1732.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(280.0,240.0,self.obj1732)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1732.graphObject_ = new_obj
      self.obj17320= AttrCalc()
      self.obj17320.Copy=ATOM3Boolean()
      self.obj17320.Copy.setValue(('Copy from LHS', 1))
      self.obj17320.Copy.config = 0
      self.obj17320.Specify=ATOM3Constraint()
      self.obj17320.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1732.GGset2Any['MaxFlow']= self.obj17320
      self.obj17321= AttrCalc()
      self.obj17321.Copy=ATOM3Boolean()
      self.obj17321.Copy.setValue(('Copy from LHS', 1))
      self.obj17321.Copy.config = 0
      self.obj17321.Specify=ATOM3Constraint()
      self.obj17321.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1732.GGset2Any['Name']= self.obj17321
      self.obj17322= AttrCalc()
      self.obj17322.Copy=ATOM3Boolean()
      self.obj17322.Copy.setValue(('Copy from LHS', 1))
      self.obj17322.Copy.config = 0
      self.obj17322.Specify=ATOM3Constraint()
      self.obj17322.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1732.GGset2Any['ReqFlow']= self.obj17322

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1732)
      self.obj1732.postAction( self.RHS.CREATE )

      self.obj1733=operatingUnit(parent)
      self.obj1733.preAction( self.RHS.CREATE )
      self.obj1733.isGraphObjectVisual = True

      if(hasattr(self.obj1733, '_setHierarchicalLink')):
        self.obj1733._setHierarchicalLink(False)

      # OperCostProp
      self.obj1733.OperCostProp.setNone()

      # name
      self.obj1733.name.setValue('')
      self.obj1733.name.setNone()

      # OperCostFix
      self.obj1733.OperCostFix.setNone()

      self.obj1733.GGLabel.setValue(5)
      self.obj1733.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(280.0,140.0,self.obj1733)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1733.graphObject_ = new_obj
      self.obj17330= AttrCalc()
      self.obj17330.Copy=ATOM3Boolean()
      self.obj17330.Copy.setValue(('Copy from LHS', 1))
      self.obj17330.Copy.config = 0
      self.obj17330.Specify=ATOM3Constraint()
      self.obj17330.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1733.GGset2Any['OperCostProp']= self.obj17330
      self.obj17331= AttrCalc()
      self.obj17331.Copy=ATOM3Boolean()
      self.obj17331.Copy.setValue(('Copy from LHS', 1))
      self.obj17331.Copy.config = 0
      self.obj17331.Specify=ATOM3Constraint()
      self.obj17331.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1733.GGset2Any['name']= self.obj17331
      self.obj17332= AttrCalc()
      self.obj17332.Copy=ATOM3Boolean()
      self.obj17332.Copy.setValue(('Copy from LHS', 1))
      self.obj17332.Copy.config = 0
      self.obj17332.Specify=ATOM3Constraint()
      self.obj17332.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1733.GGset2Any['OperCostFix']= self.obj17332

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1733)
      self.obj1733.postAction( self.RHS.CREATE )

      self.obj1734=intoMaterial(parent)
      self.obj1734.preAction( self.RHS.CREATE )
      self.obj1734.isGraphObjectVisual = True

      if(hasattr(self.obj1734, '_setHierarchicalLink')):
        self.obj1734._setHierarchicalLink(False)

      # rate
      self.obj1734.rate.setValue(0.0)

      self.obj1734.GGLabel.setValue(10)
      self.obj1734.graphClass_= graph_intoMaterial
      if parent.genGraphics:
         new_obj = graph_intoMaterial(315.25,202.5,self.obj1734)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1734.graphObject_ = new_obj
      self.obj17340= AttrCalc()
      self.obj17340.Copy=ATOM3Boolean()
      self.obj17340.Copy.setValue(('Copy from LHS', 0))
      self.obj17340.Copy.config = 0
      self.obj17340.Specify=ATOM3Constraint()
      self.obj17340.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(3)).rate.getValue()\n\n\n\n\n\n\n\n\n\n'))
      self.obj1734.GGset2Any['rate']= self.obj17340

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1734)
      self.obj1734.postAction( self.RHS.CREATE )

      self.obj1735=fromMaterial(parent)
      self.obj1735.preAction( self.RHS.CREATE )
      self.obj1735.isGraphObjectVisual = True

      if(hasattr(self.obj1735, '_setHierarchicalLink')):
        self.obj1735._setHierarchicalLink(False)

      # rate
      self.obj1735.rate.setNone()

      self.obj1735.GGLabel.setValue(8)
      self.obj1735.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(323.0,83.0,self.obj1735)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1735.graphObject_ = new_obj
      self.obj17350= AttrCalc()
      self.obj17350.Copy=ATOM3Boolean()
      self.obj17350.Copy.setValue(('Copy from LHS', 1))
      self.obj17350.Copy.config = 0
      self.obj17350.Specify=ATOM3Constraint()
      self.obj17350.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1735.GGset2Any['rate']= self.obj17350

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1735)
      self.obj1735.postAction( self.RHS.CREATE )

      self.obj1736=Goal(parent)
      self.obj1736.preAction( self.RHS.CREATE )
      self.obj1736.isGraphObjectVisual = True

      if(hasattr(self.obj1736, '_setHierarchicalLink')):
        self.obj1736._setHierarchicalLink(False)

      # name
      self.obj1736.name.setValue('')
      self.obj1736.name.setNone()

      self.obj1736.GGLabel.setValue(2)
      self.obj1736.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(60.0,220.0,self.obj1736)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1736.graphObject_ = new_obj
      self.obj17360= AttrCalc()
      self.obj17360.Copy=ATOM3Boolean()
      self.obj17360.Copy.setValue(('Copy from LHS', 1))
      self.obj17360.Copy.config = 0
      self.obj17360.Specify=ATOM3Constraint()
      self.obj17360.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1736.GGset2Any['name']= self.obj17360

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1736)
      self.obj1736.postAction( self.RHS.CREATE )

      self.obj1737=Role(parent)
      self.obj1737.preAction( self.RHS.CREATE )
      self.obj1737.isGraphObjectVisual = True

      if(hasattr(self.obj1737, '_setHierarchicalLink')):
        self.obj1737._setHierarchicalLink(False)

      # name
      self.obj1737.name.setValue('')
      self.obj1737.name.setNone()

      self.obj1737.GGLabel.setValue(1)
      self.obj1737.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(60.0,40.0,self.obj1737)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1737.graphObject_ = new_obj
      self.obj17370= AttrCalc()
      self.obj17370.Copy=ATOM3Boolean()
      self.obj17370.Copy.setValue(('Copy from LHS', 1))
      self.obj17370.Copy.config = 0
      self.obj17370.Specify=ATOM3Constraint()
      self.obj17370.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1737.GGset2Any['name']= self.obj17370

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1737)
      self.obj1737.postAction( self.RHS.CREATE )

      self.obj1738=achieve(parent)
      self.obj1738.preAction( self.RHS.CREATE )
      self.obj1738.isGraphObjectVisual = True

      if(hasattr(self.obj1738, '_setHierarchicalLink')):
        self.obj1738._setHierarchicalLink(False)

      # rate
      self.obj1738.rate.setNone()

      self.obj1738.GGLabel.setValue(3)
      self.obj1738.graphClass_= graph_achieve
      if parent.genGraphics:
         new_obj = graph_achieve(93.5,143.5,self.obj1738)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1738.graphObject_ = new_obj
      self.obj17380= AttrCalc()
      self.obj17380.Copy=ATOM3Boolean()
      self.obj17380.Copy.setValue(('Copy from LHS', 1))
      self.obj17380.Copy.config = 0
      self.obj17380.Specify=ATOM3Constraint()
      self.obj17380.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1738.GGset2Any['rate']= self.obj17380

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1738)
      self.obj1738.postAction( self.RHS.CREATE )

      self.obj1739=GenericGraphEdge(parent)
      self.obj1739.preAction( self.RHS.CREATE )
      self.obj1739.isGraphObjectVisual = True

      if(hasattr(self.obj1739, '_setHierarchicalLink')):
        self.obj1739._setHierarchicalLink(False)

      self.obj1739.GGLabel.setValue(7)
      self.obj1739.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(215.0,41.5,self.obj1739)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1739.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1739)
      self.obj1739.postAction( self.RHS.CREATE )

      self.obj1740=GenericGraphEdge(parent)
      self.obj1740.preAction( self.RHS.CREATE )
      self.obj1740.isGraphObjectVisual = True

      if(hasattr(self.obj1740, '_setHierarchicalLink')):
        self.obj1740._setHierarchicalLink(False)

      self.obj1740.GGLabel.setValue(9)
      self.obj1740.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(185.0,276.0,self.obj1740)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1740.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1740)
      self.obj1740.postAction( self.RHS.CREATE )

      self.obj1731.out_connections_.append(self.obj1735)
      self.obj1735.in_connections_.append(self.obj1731)
      self.obj1731.graphObject_.pendingConnections.append((self.obj1731.graphObject_.tag, self.obj1735.graphObject_.tag, [284.0, 69.0, 323.0, 83.0], 2, 0))
      self.obj1733.out_connections_.append(self.obj1734)
      self.obj1734.in_connections_.append(self.obj1733)
      self.obj1733.graphObject_.pendingConnections.append((self.obj1733.graphObject_.tag, self.obj1734.graphObject_.tag, [333.0, 148.0, 332.0, 167.0, 371.25, 179.5], 2, True))
      self.obj1734.out_connections_.append(self.obj1732)
      self.obj1732.in_connections_.append(self.obj1734)
      self.obj1734.graphObject_.pendingConnections.append((self.obj1734.graphObject_.tag, self.obj1732.graphObject_.tag, [326.0, 250.0, 354.5, 215.0, 371.25, 179.5], 2, True))
      self.obj1735.out_connections_.append(self.obj1733)
      self.obj1733.in_connections_.append(self.obj1735)
      self.obj1735.graphObject_.pendingConnections.append((self.obj1735.graphObject_.tag, self.obj1733.graphObject_.tag, [333.0, 148.0, 352.0, 90.0], 2, 0))
      self.obj1736.out_connections_.append(self.obj1740)
      self.obj1740.in_connections_.append(self.obj1736)
      self.obj1736.graphObject_.pendingConnections.append((self.obj1736.graphObject_.tag, self.obj1740.graphObject_.tag, [94.0, 270.0, 185.0, 276.0], 2, 0))
      self.obj1737.out_connections_.append(self.obj1738)
      self.obj1738.in_connections_.append(self.obj1737)
      self.obj1737.graphObject_.pendingConnections.append((self.obj1737.graphObject_.tag, self.obj1738.graphObject_.tag, [91.0, 85.0, 93.5, 143.5], 2, 0))
      self.obj1737.out_connections_.append(self.obj1739)
      self.obj1739.in_connections_.append(self.obj1737)
      self.obj1737.graphObject_.pendingConnections.append((self.obj1737.graphObject_.tag, self.obj1739.graphObject_.tag, [91.0, 40.0, 215.0, 41.5], 2, 0))
      self.obj1738.out_connections_.append(self.obj1736)
      self.obj1736.in_connections_.append(self.obj1738)
      self.obj1738.graphObject_.pendingConnections.append((self.obj1738.graphObject_.tag, self.obj1736.graphObject_.tag, [93.0, 221.0, 93.5, 143.5], 2, 0))
      self.obj1739.out_connections_.append(self.obj1731)
      self.obj1731.in_connections_.append(self.obj1739)
      self.obj1739.graphObject_.pendingConnections.append((self.obj1739.graphObject_.tag, self.obj1731.graphObject_.tag, [266.0, 62.0, 215.0, 41.5], 2, 0))
      self.obj1740.out_connections_.append(self.obj1732)
      self.obj1732.in_connections_.append(self.obj1740)
      self.obj1740.graphObject_.pendingConnections.append((self.obj1740.graphObject_.tag, self.obj1732.graphObject_.tag, [286.0, 282.0, 185.0, 276.0], 2, 0))

   def condition(self, graphID, isograph, atom3i):
      print '======> Link Aux Condition'# _ Agent2Raw_GG_rule.py _
      aRg = self.getMatched ( graphID , self.LHS.nodeWithLabel(4) )
      nameARG = aRg.Name.getValue()
      g = self.getMatched ( graphID , self.LHS.nodeWithLabel(6) )
      # test if nameARG  end with name of Goal 
      print  nameARG +' END WITH '+g.Name.getValue()
      print nameARG.endswith( g.Name.getValue() )
      if nameARG.endswith( g.Name.getValue() ) and not hasattr(aRg,'LinkAux'): 
       print 'Real True'
       return True
      else : 
       print 'Real False'
       return False
      
      

   def action(self, graphID, isograph, atom3i):
      print '======> Link Aux Action'
      aRg = self.getMatched ( graphID , self.LHS.nodeWithLabel(4) )
      aRg.LinkAux = True 
      
      

