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

      self.obj650=rawMaterial(parent)
      self.obj650.preAction( self.LHS.CREATE )
      self.obj650.isGraphObjectVisual = True

      if(hasattr(self.obj650, '_setHierarchicalLink')):
        self.obj650._setHierarchicalLink(False)

      # MaxFlow
      self.obj650.MaxFlow.setValue(999999)

      # price
      self.obj650.price.setValue(0)

      # Name
      self.obj650.Name.setValue('')
      self.obj650.Name.setNone()

      # ReqFlow
      self.obj650.ReqFlow.setValue(0)

      self.obj650.GGLabel.setValue(3)
      self.obj650.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(220.0,20.0,self.obj650)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj650.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj650)
      self.obj650.postAction( self.LHS.CREATE )

      self.obj651=operatingUnit(parent)
      self.obj651.preAction( self.LHS.CREATE )
      self.obj651.isGraphObjectVisual = True

      if(hasattr(self.obj651, '_setHierarchicalLink')):
        self.obj651._setHierarchicalLink(False)

      # OperCostProp
      self.obj651.OperCostProp.setValue(0.0)

      # name
      self.obj651.name.setValue('')
      self.obj651.name.setNone()

      # OperCostFix
      self.obj651.OperCostFix.setValue(0.0)

      self.obj651.GGLabel.setValue(2)
      self.obj651.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(260.0,160.0,self.obj651)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj651.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj651)
      self.obj651.postAction( self.LHS.CREATE )

      self.obj652=Agent(parent)
      self.obj652.preAction( self.LHS.CREATE )
      self.obj652.isGraphObjectVisual = True

      if(hasattr(self.obj652, '_setHierarchicalLink')):
        self.obj652._setHierarchicalLink(False)

      # price
      self.obj652.price.setNone()

      # name
      self.obj652.name.setValue('')
      self.obj652.name.setNone()

      self.obj652.GGLabel.setValue(1)
      self.obj652.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(80.0,120.0,self.obj652)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj652.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj652)
      self.obj652.postAction( self.LHS.CREATE )

      self.obj653=GenericGraphEdge(parent)
      self.obj653.preAction( self.LHS.CREATE )
      self.obj653.isGraphObjectVisual = True

      if(hasattr(self.obj653, '_setHierarchicalLink')):
        self.obj653._setHierarchicalLink(False)

      self.obj653.GGLabel.setValue(4)
      self.obj653.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(181.75,114.0,self.obj653)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj653.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj653)
      self.obj653.postAction( self.LHS.CREATE )

      self.obj654=GenericGraphEdge(parent)
      self.obj654.preAction( self.LHS.CREATE )
      self.obj654.isGraphObjectVisual = True

      if(hasattr(self.obj654, '_setHierarchicalLink')):
        self.obj654._setHierarchicalLink(False)

      self.obj654.GGLabel.setValue(5)
      self.obj654.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(229.25,150.25,self.obj654)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj654.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj654)
      self.obj654.postAction( self.LHS.CREATE )

      self.obj652.out_connections_.append(self.obj653)
      self.obj653.in_connections_.append(self.obj652)
      self.obj652.graphObject_.pendingConnections.append((self.obj652.graphObject_.tag, self.obj653.graphObject_.tag, [105.0, 182.0, 147.0, 140.5, 181.75, 114.0], 2, True))
      self.obj652.out_connections_.append(self.obj654)
      self.obj654.in_connections_.append(self.obj652)
      self.obj652.graphObject_.pendingConnections.append((self.obj652.graphObject_.tag, self.obj654.graphObject_.tag, [105.0, 182.0, 185.5, 153.0, 229.25, 150.25], 2, True))
      self.obj653.out_connections_.append(self.obj650)
      self.obj650.in_connections_.append(self.obj653)
      self.obj653.graphObject_.pendingConnections.append((self.obj653.graphObject_.tag, self.obj650.graphObject_.tag, [244.0, 76.0, 216.5, 87.5, 181.75, 114.0], 2, True))
      self.obj654.out_connections_.append(self.obj651)
      self.obj651.in_connections_.append(self.obj654)
      self.obj654.graphObject_.pendingConnections.append((self.obj654.graphObject_.tag, self.obj651.graphObject_.tag, [280.0, 171.0, 273.0, 147.5, 229.25, 150.25], 2, True))

      self.RHS = ASG_pns(parent)
      self.RHS.merge(ASG_omacs(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj658=rawMaterial(parent)
      self.obj658.preAction( self.RHS.CREATE )
      self.obj658.isGraphObjectVisual = True

      if(hasattr(self.obj658, '_setHierarchicalLink')):
        self.obj658._setHierarchicalLink(False)

      # MaxFlow
      self.obj658.MaxFlow.setValue(999999)

      # price
      self.obj658.price.setValue(0)

      # Name
      self.obj658.Name.setValue('')
      self.obj658.Name.setNone()

      # ReqFlow
      self.obj658.ReqFlow.setValue(0)

      self.obj658.GGLabel.setValue(3)
      self.obj658.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(220.0,20.0,self.obj658)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj658.graphObject_ = new_obj
      self.obj6580= AttrCalc()
      self.obj6580.Copy=ATOM3Boolean()
      self.obj6580.Copy.setValue(('Copy from LHS', 1))
      self.obj6580.Copy.config = 0
      self.obj6580.Specify=ATOM3Constraint()
      self.obj6580.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj658.GGset2Any['MaxFlow']= self.obj6580
      self.obj6581= AttrCalc()
      self.obj6581.Copy=ATOM3Boolean()
      self.obj6581.Copy.setValue(('Copy from LHS', 1))
      self.obj6581.Copy.config = 0
      self.obj6581.Specify=ATOM3Constraint()
      self.obj6581.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj658.GGset2Any['Name']= self.obj6581
      self.obj6582= AttrCalc()
      self.obj6582.Copy=ATOM3Boolean()
      self.obj6582.Copy.setValue(('Copy from LHS', 1))
      self.obj6582.Copy.config = 0
      self.obj6582.Specify=ATOM3Constraint()
      self.obj6582.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj658.GGset2Any['ReqFlow']= self.obj6582

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj658)
      self.obj658.postAction( self.RHS.CREATE )

      self.obj659=operatingUnit(parent)
      self.obj659.preAction( self.RHS.CREATE )
      self.obj659.isGraphObjectVisual = True

      if(hasattr(self.obj659, '_setHierarchicalLink')):
        self.obj659._setHierarchicalLink(False)

      # OperCostProp
      self.obj659.OperCostProp.setValue(0.0)

      # name
      self.obj659.name.setValue('')
      self.obj659.name.setNone()

      # OperCostFix
      self.obj659.OperCostFix.setValue(0.0)

      self.obj659.GGLabel.setValue(2)
      self.obj659.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(260.0,160.0,self.obj659)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj659.graphObject_ = new_obj
      self.obj6590= AttrCalc()
      self.obj6590.Copy=ATOM3Boolean()
      self.obj6590.Copy.setValue(('Copy from LHS', 1))
      self.obj6590.Copy.config = 0
      self.obj6590.Specify=ATOM3Constraint()
      self.obj6590.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj659.GGset2Any['OperCostProp']= self.obj6590
      self.obj6591= AttrCalc()
      self.obj6591.Copy=ATOM3Boolean()
      self.obj6591.Copy.setValue(('Copy from LHS', 1))
      self.obj6591.Copy.config = 0
      self.obj6591.Specify=ATOM3Constraint()
      self.obj6591.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj659.GGset2Any['name']= self.obj6591
      self.obj6592= AttrCalc()
      self.obj6592.Copy=ATOM3Boolean()
      self.obj6592.Copy.setValue(('Copy from LHS', 1))
      self.obj6592.Copy.config = 0
      self.obj6592.Specify=ATOM3Constraint()
      self.obj6592.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj659.GGset2Any['OperCostFix']= self.obj6592

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj659)
      self.obj659.postAction( self.RHS.CREATE )

      self.obj660=fromRaw(parent)
      self.obj660.preAction( self.RHS.CREATE )
      self.obj660.isGraphObjectVisual = True

      if(hasattr(self.obj660, '_setHierarchicalLink')):
        self.obj660._setHierarchicalLink(False)

      # rate
      self.obj660.rate.setValue(1.0)

      self.obj660.GGLabel.setValue(7)
      self.obj660.graphClass_= graph_fromRaw
      if parent.genGraphics:
         new_obj = graph_fromRaw(262.0,115.5,self.obj660)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj660.graphObject_ = new_obj
      self.obj6600= AttrCalc()
      self.obj6600.Copy=ATOM3Boolean()
      self.obj6600.Copy.setValue(('Copy from LHS', 0))
      self.obj6600.Copy.config = 0
      self.obj6600.Specify=ATOM3Constraint()
      self.obj6600.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj660.GGset2Any['rate']= self.obj6600

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj660)
      self.obj660.postAction( self.RHS.CREATE )

      self.obj661=Agent(parent)
      self.obj661.preAction( self.RHS.CREATE )
      self.obj661.isGraphObjectVisual = True

      if(hasattr(self.obj661, '_setHierarchicalLink')):
        self.obj661._setHierarchicalLink(False)

      # price
      self.obj661.price.setNone()

      # name
      self.obj661.name.setValue('')
      self.obj661.name.setNone()

      self.obj661.GGLabel.setValue(1)
      self.obj661.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(80.0,120.0,self.obj661)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj661.graphObject_ = new_obj
      self.obj6610= AttrCalc()
      self.obj6610.Copy=ATOM3Boolean()
      self.obj6610.Copy.setValue(('Copy from LHS', 1))
      self.obj6610.Copy.config = 0
      self.obj6610.Specify=ATOM3Constraint()
      self.obj6610.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj661.GGset2Any['price']= self.obj6610
      self.obj6611= AttrCalc()
      self.obj6611.Copy=ATOM3Boolean()
      self.obj6611.Copy.setValue(('Copy from LHS', 1))
      self.obj6611.Copy.config = 0
      self.obj6611.Specify=ATOM3Constraint()
      self.obj6611.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj661.GGset2Any['name']= self.obj6611

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj661)
      self.obj661.postAction( self.RHS.CREATE )

      self.obj662=GenericGraphEdge(parent)
      self.obj662.preAction( self.RHS.CREATE )
      self.obj662.isGraphObjectVisual = True

      if(hasattr(self.obj662, '_setHierarchicalLink')):
        self.obj662._setHierarchicalLink(False)

      self.obj662.GGLabel.setValue(4)
      self.obj662.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(181.75,114.0,self.obj662)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj662.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj662)
      self.obj662.postAction( self.RHS.CREATE )

      self.obj663=GenericGraphEdge(parent)
      self.obj663.preAction( self.RHS.CREATE )
      self.obj663.isGraphObjectVisual = True

      if(hasattr(self.obj663, '_setHierarchicalLink')):
        self.obj663._setHierarchicalLink(False)

      self.obj663.GGLabel.setValue(5)
      self.obj663.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(229.25,150.25,self.obj663)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj663.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj663)
      self.obj663.postAction( self.RHS.CREATE )

      self.obj658.out_connections_.append(self.obj660)
      self.obj660.in_connections_.append(self.obj658)
      self.obj658.graphObject_.pendingConnections.append((self.obj658.graphObject_.tag, self.obj660.graphObject_.tag, [244.0, 70.0, 262.0, 115.5], 0, True))
      self.obj660.out_connections_.append(self.obj659)
      self.obj659.in_connections_.append(self.obj660)
      self.obj660.graphObject_.pendingConnections.append((self.obj660.graphObject_.tag, self.obj659.graphObject_.tag, [280.0, 161.0, 262.0, 115.5], 0, True))
      self.obj661.out_connections_.append(self.obj662)
      self.obj662.in_connections_.append(self.obj661)
      self.obj661.graphObject_.pendingConnections.append((self.obj661.graphObject_.tag, self.obj662.graphObject_.tag, [117.0, 182.0, 181.75, 114.0], 2, 0))
      self.obj661.out_connections_.append(self.obj663)
      self.obj663.in_connections_.append(self.obj661)
      self.obj661.graphObject_.pendingConnections.append((self.obj661.graphObject_.tag, self.obj663.graphObject_.tag, [117.0, 182.0, 229.25, 150.25], 2, 0))
      self.obj662.out_connections_.append(self.obj658)
      self.obj658.in_connections_.append(self.obj662)
      self.obj662.graphObject_.pendingConnections.append((self.obj662.graphObject_.tag, self.obj658.graphObject_.tag, [244.0, 70.0, 181.75, 114.0], 2, 0))
      self.obj663.out_connections_.append(self.obj659)
      self.obj659.in_connections_.append(self.obj663)
      self.obj663.graphObject_.pendingConnections.append((self.obj663.graphObject_.tag, self.obj659.graphObject_.tag, [280.0, 161.0, 229.25, 150.25], 2, 0))

   def condition(self, graphID, isograph, atom3i):
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(2))
      return not hasattr(node, "LinkRaw2AR")
      

   def action(self, graphID, isograph, atom3i):
      node = self.getMatched ( graphID , self.LHS.nodeWithLabel(2) )
      node.LinkRaw2AR = True
      
      

