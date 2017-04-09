# _ CreateLinkMatr2OAF_GG_rule.py ____________________________________________________________________________
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
class CreateLinkMatr2OAF_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 15)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_pns(parent)
      self.LHS.merge(ASG_omacs(parent))
      self.LHS.merge(ASG_GenericGraph(parent))

      self.obj204=product(parent)
      self.obj204.preAction( self.LHS.CREATE )
      self.obj204.isGraphObjectVisual = True

      if(hasattr(self.obj204, '_setHierarchicalLink')):
        self.obj204._setHierarchicalLink(False)

      # MaxFlow
      self.obj204.MaxFlow.setNone()

      # price
      self.obj204.price.setValue(0)

      # Name
      self.obj204.Name.setValue('')
      self.obj204.Name.setNone()

      # ReqFlow
      self.obj204.ReqFlow.setNone()

      self.obj204.GGLabel.setValue(5)
      self.obj204.graphClass_= graph_product
      if parent.genGraphics:
         new_obj = graph_product(280.0,220.0,self.obj204)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj204.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj204)
      self.obj204.postAction( self.LHS.CREATE )

      self.obj205=metarial(parent)
      self.obj205.preAction( self.LHS.CREATE )
      self.obj205.isGraphObjectVisual = True

      if(hasattr(self.obj205, '_setHierarchicalLink')):
        self.obj205._setHierarchicalLink(False)

      # MaxFlow
      self.obj205.MaxFlow.setNone()

      # price
      self.obj205.price.setValue(0)

      # Name
      self.obj205.Name.setValue('')
      self.obj205.Name.setNone()

      # ReqFlow
      self.obj205.ReqFlow.setNone()

      self.obj205.GGLabel.setValue(3)
      self.obj205.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(320.0,40.0,self.obj205)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj205.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj205)
      self.obj205.postAction( self.LHS.CREATE )

      self.obj206=Goal(parent)
      self.obj206.preAction( self.LHS.CREATE )
      self.obj206.isGraphObjectVisual = True

      if(hasattr(self.obj206, '_setHierarchicalLink')):
        self.obj206._setHierarchicalLink(False)

      # name
      self.obj206.name.setValue('')
      self.obj206.name.setNone()

      self.obj206.GGLabel.setValue(2)
      self.obj206.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(180.0,60.0,self.obj206)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj206.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj206)
      self.obj206.postAction( self.LHS.CREATE )

      self.obj207=GenericGraphEdge(parent)
      self.obj207.preAction( self.LHS.CREATE )
      self.obj207.isGraphObjectVisual = True

      if(hasattr(self.obj207, '_setHierarchicalLink')):
        self.obj207._setHierarchicalLink(False)

      self.obj207.GGLabel.setValue(4)
      self.obj207.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(264.5,71.5,self.obj207)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj207.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj207)
      self.obj207.postAction( self.LHS.CREATE )

      self.obj206.out_connections_.append(self.obj207)
      self.obj207.in_connections_.append(self.obj206)
      self.obj206.graphObject_.pendingConnections.append((self.obj206.graphObject_.tag, self.obj207.graphObject_.tag, [203.0, 61.0, 264.5, 71.5], 0, True))
      self.obj207.out_connections_.append(self.obj205)
      self.obj205.in_connections_.append(self.obj207)
      self.obj207.graphObject_.pendingConnections.append((self.obj207.graphObject_.tag, self.obj205.graphObject_.tag, [326.0, 82.0, 264.5, 71.5], 0, True))

      self.RHS = ASG_pns(parent)
      self.RHS.merge(ASG_omacs(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj211=product(parent)
      self.obj211.preAction( self.RHS.CREATE )
      self.obj211.isGraphObjectVisual = True

      if(hasattr(self.obj211, '_setHierarchicalLink')):
        self.obj211._setHierarchicalLink(False)

      # MaxFlow
      self.obj211.MaxFlow.setNone()

      # price
      self.obj211.price.setValue(0)

      # Name
      self.obj211.Name.setValue('')
      self.obj211.Name.setNone()

      # ReqFlow
      self.obj211.ReqFlow.setNone()

      self.obj211.GGLabel.setValue(5)
      self.obj211.graphClass_= graph_product
      if parent.genGraphics:
         new_obj = graph_product(280.0,220.0,self.obj211)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj211.graphObject_ = new_obj
      self.obj2110= AttrCalc()
      self.obj2110.Copy=ATOM3Boolean()
      self.obj2110.Copy.setValue(('Copy from LHS', 1))
      self.obj2110.Copy.config = 0
      self.obj2110.Specify=ATOM3Constraint()
      self.obj2110.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj211.GGset2Any['MaxFlow']= self.obj2110
      self.obj2111= AttrCalc()
      self.obj2111.Copy=ATOM3Boolean()
      self.obj2111.Copy.setValue(('Copy from LHS', 1))
      self.obj2111.Copy.config = 0
      self.obj2111.Specify=ATOM3Constraint()
      self.obj2111.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj211.GGset2Any['Name']= self.obj2111
      self.obj2112= AttrCalc()
      self.obj2112.Copy=ATOM3Boolean()
      self.obj2112.Copy.setValue(('Copy from LHS', 1))
      self.obj2112.Copy.config = 0
      self.obj2112.Specify=ATOM3Constraint()
      self.obj2112.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj211.GGset2Any['ReqFlow']= self.obj2112

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj211)
      self.obj211.postAction( self.RHS.CREATE )

      self.obj212=metarial(parent)
      self.obj212.preAction( self.RHS.CREATE )
      self.obj212.isGraphObjectVisual = True

      if(hasattr(self.obj212, '_setHierarchicalLink')):
        self.obj212._setHierarchicalLink(False)

      # MaxFlow
      self.obj212.MaxFlow.setNone()

      # price
      self.obj212.price.setValue(0)

      # Name
      self.obj212.Name.setValue('')
      self.obj212.Name.setNone()

      # ReqFlow
      self.obj212.ReqFlow.setNone()

      self.obj212.GGLabel.setValue(3)
      self.obj212.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(320.0,40.0,self.obj212)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj212.graphObject_ = new_obj
      self.obj2120= AttrCalc()
      self.obj2120.Copy=ATOM3Boolean()
      self.obj2120.Copy.setValue(('Copy from LHS', 1))
      self.obj2120.Copy.config = 0
      self.obj2120.Specify=ATOM3Constraint()
      self.obj2120.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj212.GGset2Any['MaxFlow']= self.obj2120
      self.obj2121= AttrCalc()
      self.obj2121.Copy=ATOM3Boolean()
      self.obj2121.Copy.setValue(('Copy from LHS', 1))
      self.obj2121.Copy.config = 0
      self.obj2121.Specify=ATOM3Constraint()
      self.obj2121.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj212.GGset2Any['Name']= self.obj2121
      self.obj2122= AttrCalc()
      self.obj2122.Copy=ATOM3Boolean()
      self.obj2122.Copy.setValue(('Copy from LHS', 1))
      self.obj2122.Copy.config = 0
      self.obj2122.Specify=ATOM3Constraint()
      self.obj2122.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj212.GGset2Any['ReqFlow']= self.obj2122

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj212)
      self.obj212.postAction( self.RHS.CREATE )

      self.obj213=operatingUnit(parent)
      self.obj213.preAction( self.RHS.CREATE )
      self.obj213.isGraphObjectVisual = True

      if(hasattr(self.obj213, '_setHierarchicalLink')):
        self.obj213._setHierarchicalLink(False)

      # OperCostProp
      self.obj213.OperCostProp.setValue(1.0)

      # name
      self.obj213.name.setValue('')
      self.obj213.name.setNone()

      # OperCostFix
      self.obj213.OperCostFix.setValue(2.0)

      self.obj213.GGLabel.setValue(7)
      self.obj213.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(320.0,140.0,self.obj213)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj213.graphObject_ = new_obj
      self.obj2130= AttrCalc()
      self.obj2130.Copy=ATOM3Boolean()
      self.obj2130.Copy.setValue(('Copy from LHS', 0))
      self.obj2130.Copy.config = 0
      self.obj2130.Specify=ATOM3Constraint()
      self.obj2130.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj213.GGset2Any['OperCostProp']= self.obj2130
      self.obj2131= AttrCalc()
      self.obj2131.Copy=ATOM3Boolean()
      self.obj2131.Copy.setValue(('Copy from LHS', 0))
      self.obj2131.Copy.config = 0
      self.obj2131.Specify=ATOM3Constraint()
      self.obj2131.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(2)).name.getValue()+\' OAF\'\n'))
      self.obj213.GGset2Any['name']= self.obj2131
      self.obj2132= AttrCalc()
      self.obj2132.Copy=ATOM3Boolean()
      self.obj2132.Copy.setValue(('Copy from LHS', 0))
      self.obj2132.Copy.config = 0
      self.obj2132.Specify=ATOM3Constraint()
      self.obj2132.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj213.GGset2Any['OperCostFix']= self.obj2132

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj213)
      self.obj213.postAction( self.RHS.CREATE )

      self.obj214=intoProduct(parent)
      self.obj214.preAction( self.RHS.CREATE )
      self.obj214.isGraphObjectVisual = True

      if(hasattr(self.obj214, '_setHierarchicalLink')):
        self.obj214._setHierarchicalLink(False)

      # rate
      self.obj214.rate.setValue(1.0)

      self.obj214.GGLabel.setValue(9)
      self.obj214.graphClass_= graph_intoProduct
      if parent.genGraphics:
         new_obj = graph_intoProduct(322.0,179.0,self.obj214)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj214.graphObject_ = new_obj
      self.obj2140= AttrCalc()
      self.obj2140.Copy=ATOM3Boolean()
      self.obj2140.Copy.setValue(('Copy from LHS', 0))
      self.obj2140.Copy.config = 0
      self.obj2140.Specify=ATOM3Constraint()
      self.obj2140.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj214.GGset2Any['rate']= self.obj2140

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj214)
      self.obj214.postAction( self.RHS.CREATE )

      self.obj215=fromMaterial(parent)
      self.obj215.preAction( self.RHS.CREATE )
      self.obj215.isGraphObjectVisual = True

      if(hasattr(self.obj215, '_setHierarchicalLink')):
        self.obj215._setHierarchicalLink(False)

      # rate
      self.obj215.rate.setValue(1.0)

      self.obj215.GGLabel.setValue(8)
      self.obj215.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(342.0,110.0,self.obj215)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj215.graphObject_ = new_obj
      self.obj2150= AttrCalc()
      self.obj2150.Copy=ATOM3Boolean()
      self.obj2150.Copy.setValue(('Copy from LHS', 0))
      self.obj2150.Copy.config = 0
      self.obj2150.Specify=ATOM3Constraint()
      self.obj2150.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj215.GGset2Any['rate']= self.obj2150

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj215)
      self.obj215.postAction( self.RHS.CREATE )

      self.obj216=Goal(parent)
      self.obj216.preAction( self.RHS.CREATE )
      self.obj216.isGraphObjectVisual = True

      if(hasattr(self.obj216, '_setHierarchicalLink')):
        self.obj216._setHierarchicalLink(False)

      # name
      self.obj216.name.setValue('')
      self.obj216.name.setNone()

      self.obj216.GGLabel.setValue(2)
      self.obj216.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(180.0,60.0,self.obj216)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj216.graphObject_ = new_obj
      self.obj2160= AttrCalc()
      self.obj2160.Copy=ATOM3Boolean()
      self.obj2160.Copy.setValue(('Copy from LHS', 1))
      self.obj2160.Copy.config = 0
      self.obj2160.Specify=ATOM3Constraint()
      self.obj2160.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj216.GGset2Any['name']= self.obj2160

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj216)
      self.obj216.postAction( self.RHS.CREATE )

      self.obj217=GenericGraphEdge(parent)
      self.obj217.preAction( self.RHS.CREATE )
      self.obj217.isGraphObjectVisual = True

      if(hasattr(self.obj217, '_setHierarchicalLink')):
        self.obj217._setHierarchicalLink(False)

      self.obj217.GGLabel.setValue(4)
      self.obj217.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(264.5,71.5,self.obj217)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj217.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj217)
      self.obj217.postAction( self.RHS.CREATE )

      self.obj212.out_connections_.append(self.obj215)
      self.obj215.in_connections_.append(self.obj212)
      self.obj212.graphObject_.pendingConnections.append((self.obj212.graphObject_.tag, self.obj215.graphObject_.tag, [244.0, 89.0, 342.0, 110.0], 0, True))
      self.obj213.out_connections_.append(self.obj214)
      self.obj214.in_connections_.append(self.obj213)
      self.obj213.graphObject_.pendingConnections.append((self.obj213.graphObject_.tag, self.obj214.graphObject_.tag, [339.0, 158.0, 322.0, 179.0], 0, True))
      self.obj214.out_connections_.append(self.obj211)
      self.obj211.in_connections_.append(self.obj214)
      self.obj214.graphObject_.pendingConnections.append((self.obj214.graphObject_.tag, self.obj211.graphObject_.tag, [305.0, 220.0, 322.0, 179.0], 0, True))
      self.obj215.out_connections_.append(self.obj213)
      self.obj213.in_connections_.append(self.obj215)
      self.obj215.graphObject_.pendingConnections.append((self.obj215.graphObject_.tag, self.obj213.graphObject_.tag, [340.0, 151.0, 342.0, 110.0], 0, True))
      self.obj216.out_connections_.append(self.obj217)
      self.obj217.in_connections_.append(self.obj216)
      self.obj216.graphObject_.pendingConnections.append((self.obj216.graphObject_.tag, self.obj217.graphObject_.tag, [93.0, 61.0, 264.5, 71.5], 2, 0))
      self.obj217.out_connections_.append(self.obj212)
      self.obj212.in_connections_.append(self.obj217)
      self.obj217.graphObject_.pendingConnections.append((self.obj217.graphObject_.tag, self.obj212.graphObject_.tag, [226.0, 82.0, 264.5, 71.5], 2, 0))

   def condition(self, graphID, isograph, atom3i):
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(3))
      return not hasattr(node, "link2oaf")
      

   def action(self, graphID, isograph, atom3i):
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(3))
      node.link2oaf = True
      
      

