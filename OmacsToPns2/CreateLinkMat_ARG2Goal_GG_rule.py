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

      self.obj718=metarial(parent)
      self.obj718.preAction( self.LHS.CREATE )
      self.obj718.isGraphObjectVisual = True

      if(hasattr(self.obj718, '_setHierarchicalLink')):
        self.obj718._setHierarchicalLink(False)

      # MaxFlow
      self.obj718.MaxFlow.setNone()

      # price
      self.obj718.price.setValue(0)

      # Name
      self.obj718.Name.setValue('')
      self.obj718.Name.setNone()

      # ReqFlow
      self.obj718.ReqFlow.setNone()

      self.obj718.GGLabel.setValue(4)
      self.obj718.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(240.0,20.0,self.obj718)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj718.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj718)
      self.obj718.postAction( self.LHS.CREATE )

      self.obj719=metarial(parent)
      self.obj719.preAction( self.LHS.CREATE )
      self.obj719.isGraphObjectVisual = True

      if(hasattr(self.obj719, '_setHierarchicalLink')):
        self.obj719._setHierarchicalLink(False)

      # MaxFlow
      self.obj719.MaxFlow.setNone()

      # price
      self.obj719.price.setValue(0)

      # Name
      self.obj719.Name.setValue('')
      self.obj719.Name.setNone()

      # ReqFlow
      self.obj719.ReqFlow.setNone()

      self.obj719.GGLabel.setValue(6)
      self.obj719.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(240.0,240.0,self.obj719)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj719.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj719)
      self.obj719.postAction( self.LHS.CREATE )

      self.obj720=operatingUnit(parent)
      self.obj720.preAction( self.LHS.CREATE )
      self.obj720.isGraphObjectVisual = True

      if(hasattr(self.obj720, '_setHierarchicalLink')):
        self.obj720._setHierarchicalLink(False)

      # OperCostProp
      self.obj720.OperCostProp.setNone()

      # name
      self.obj720.name.setValue('')
      self.obj720.name.setNone()

      # OperCostFix
      self.obj720.OperCostFix.setNone()

      self.obj720.GGLabel.setValue(5)
      self.obj720.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(240.0,140.0,self.obj720)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj720.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj720)
      self.obj720.postAction( self.LHS.CREATE )

      self.obj721=fromMaterial(parent)
      self.obj721.preAction( self.LHS.CREATE )
      self.obj721.isGraphObjectVisual = True

      if(hasattr(self.obj721, '_setHierarchicalLink')):
        self.obj721._setHierarchicalLink(False)

      # rate
      self.obj721.rate.setNone()

      self.obj721.GGLabel.setValue(8)
      self.obj721.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(265.0,100.0,self.obj721)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj721.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj721)
      self.obj721.postAction( self.LHS.CREATE )

      self.obj722=Goal(parent)
      self.obj722.preAction( self.LHS.CREATE )
      self.obj722.isGraphObjectVisual = True

      if(hasattr(self.obj722, '_setHierarchicalLink')):
        self.obj722._setHierarchicalLink(False)

      # name
      self.obj722.name.setValue('')
      self.obj722.name.setNone()

      self.obj722.GGLabel.setValue(2)
      self.obj722.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(60.0,220.0,self.obj722)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj722.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj722)
      self.obj722.postAction( self.LHS.CREATE )

      self.obj723=Role(parent)
      self.obj723.preAction( self.LHS.CREATE )
      self.obj723.isGraphObjectVisual = True

      if(hasattr(self.obj723, '_setHierarchicalLink')):
        self.obj723._setHierarchicalLink(False)

      # name
      self.obj723.name.setValue('')
      self.obj723.name.setNone()

      self.obj723.GGLabel.setValue(1)
      self.obj723.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(60.0,40.0,self.obj723)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj723.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj723)
      self.obj723.postAction( self.LHS.CREATE )

      self.obj724=achieve(parent)
      self.obj724.preAction( self.LHS.CREATE )
      self.obj724.isGraphObjectVisual = True

      if(hasattr(self.obj724, '_setHierarchicalLink')):
        self.obj724._setHierarchicalLink(False)

      # rate
      self.obj724.rate.setNone()

      self.obj724.GGLabel.setValue(3)
      self.obj724.graphClass_= graph_achieve
      if parent.genGraphics:
         new_obj = graph_achieve(97.5,137.5,self.obj724)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj724.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj724)
      self.obj724.postAction( self.LHS.CREATE )

      self.obj725=GenericGraphEdge(parent)
      self.obj725.preAction( self.LHS.CREATE )
      self.obj725.isGraphObjectVisual = True

      if(hasattr(self.obj725, '_setHierarchicalLink')):
        self.obj725._setHierarchicalLink(False)

      self.obj725.GGLabel.setValue(7)
      self.obj725.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(215.0,41.5,self.obj725)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj725.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj725)
      self.obj725.postAction( self.LHS.CREATE )

      self.obj726=GenericGraphEdge(parent)
      self.obj726.preAction( self.LHS.CREATE )
      self.obj726.isGraphObjectVisual = True

      if(hasattr(self.obj726, '_setHierarchicalLink')):
        self.obj726._setHierarchicalLink(False)

      self.obj726.GGLabel.setValue(9)
      self.obj726.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(185.0,276.0,self.obj726)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj726.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj726)
      self.obj726.postAction( self.LHS.CREATE )

      self.obj718.out_connections_.append(self.obj721)
      self.obj721.in_connections_.append(self.obj718)
      self.obj718.graphObject_.pendingConnections.append((self.obj718.graphObject_.tag, self.obj721.graphObject_.tag, [264.0, 69.0, 265.0, 100.0], 0, True))
      self.obj721.out_connections_.append(self.obj720)
      self.obj720.in_connections_.append(self.obj721)
      self.obj721.graphObject_.pendingConnections.append((self.obj721.graphObject_.tag, self.obj720.graphObject_.tag, [260.0, 151.0, 352.0, 90.0], 0, True))
      self.obj722.out_connections_.append(self.obj726)
      self.obj726.in_connections_.append(self.obj722)
      self.obj722.graphObject_.pendingConnections.append((self.obj722.graphObject_.tag, self.obj726.graphObject_.tag, [84.0, 270.0, 185.0, 276.0], 0, True))
      self.obj723.out_connections_.append(self.obj724)
      self.obj724.in_connections_.append(self.obj723)
      self.obj723.graphObject_.pendingConnections.append((self.obj723.graphObject_.tag, self.obj724.graphObject_.tag, [84.0, 86.0, 97.5, 137.5], 0, True))
      self.obj723.out_connections_.append(self.obj725)
      self.obj725.in_connections_.append(self.obj723)
      self.obj723.graphObject_.pendingConnections.append((self.obj723.graphObject_.tag, self.obj725.graphObject_.tag, [84.0, 41.0, 215.0, 41.5], 0, True))
      self.obj724.out_connections_.append(self.obj722)
      self.obj722.in_connections_.append(self.obj724)
      self.obj724.graphObject_.pendingConnections.append((self.obj724.graphObject_.tag, self.obj722.graphObject_.tag, [83.0, 221.0, 93.5, 143.5], 0, True))
      self.obj725.out_connections_.append(self.obj718)
      self.obj718.in_connections_.append(self.obj725)
      self.obj725.graphObject_.pendingConnections.append((self.obj725.graphObject_.tag, self.obj718.graphObject_.tag, [246.0, 62.0, 215.0, 41.5], 0, True))
      self.obj726.out_connections_.append(self.obj719)
      self.obj719.in_connections_.append(self.obj726)
      self.obj726.graphObject_.pendingConnections.append((self.obj726.graphObject_.tag, self.obj719.graphObject_.tag, [246.0, 282.0, 185.0, 276.0], 0, True))

      self.RHS = ASG_pns(parent)
      self.RHS.merge(ASG_omacs(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj730=metarial(parent)
      self.obj730.preAction( self.RHS.CREATE )
      self.obj730.isGraphObjectVisual = True

      if(hasattr(self.obj730, '_setHierarchicalLink')):
        self.obj730._setHierarchicalLink(False)

      # MaxFlow
      self.obj730.MaxFlow.setNone()

      # price
      self.obj730.price.setValue(0)

      # Name
      self.obj730.Name.setValue('')
      self.obj730.Name.setNone()

      # ReqFlow
      self.obj730.ReqFlow.setNone()

      self.obj730.GGLabel.setValue(4)
      self.obj730.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(280.0,20.0,self.obj730)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj730.graphObject_ = new_obj
      self.obj7300= AttrCalc()
      self.obj7300.Copy=ATOM3Boolean()
      self.obj7300.Copy.setValue(('Copy from LHS', 1))
      self.obj7300.Copy.config = 0
      self.obj7300.Specify=ATOM3Constraint()
      self.obj7300.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj730.GGset2Any['MaxFlow']= self.obj7300
      self.obj7301= AttrCalc()
      self.obj7301.Copy=ATOM3Boolean()
      self.obj7301.Copy.setValue(('Copy from LHS', 1))
      self.obj7301.Copy.config = 0
      self.obj7301.Specify=ATOM3Constraint()
      self.obj7301.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj730.GGset2Any['Name']= self.obj7301
      self.obj7302= AttrCalc()
      self.obj7302.Copy=ATOM3Boolean()
      self.obj7302.Copy.setValue(('Copy from LHS', 1))
      self.obj7302.Copy.config = 0
      self.obj7302.Specify=ATOM3Constraint()
      self.obj7302.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj730.GGset2Any['ReqFlow']= self.obj7302

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj730)
      self.obj730.postAction( self.RHS.CREATE )

      self.obj731=metarial(parent)
      self.obj731.preAction( self.RHS.CREATE )
      self.obj731.isGraphObjectVisual = True

      if(hasattr(self.obj731, '_setHierarchicalLink')):
        self.obj731._setHierarchicalLink(False)

      # MaxFlow
      self.obj731.MaxFlow.setNone()

      # price
      self.obj731.price.setValue(0)

      # Name
      self.obj731.Name.setValue('')
      self.obj731.Name.setNone()

      # ReqFlow
      self.obj731.ReqFlow.setNone()

      self.obj731.GGLabel.setValue(6)
      self.obj731.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(280.0,240.0,self.obj731)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj731.graphObject_ = new_obj
      self.obj7310= AttrCalc()
      self.obj7310.Copy=ATOM3Boolean()
      self.obj7310.Copy.setValue(('Copy from LHS', 1))
      self.obj7310.Copy.config = 0
      self.obj7310.Specify=ATOM3Constraint()
      self.obj7310.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj731.GGset2Any['MaxFlow']= self.obj7310
      self.obj7311= AttrCalc()
      self.obj7311.Copy=ATOM3Boolean()
      self.obj7311.Copy.setValue(('Copy from LHS', 1))
      self.obj7311.Copy.config = 0
      self.obj7311.Specify=ATOM3Constraint()
      self.obj7311.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj731.GGset2Any['Name']= self.obj7311
      self.obj7312= AttrCalc()
      self.obj7312.Copy=ATOM3Boolean()
      self.obj7312.Copy.setValue(('Copy from LHS', 1))
      self.obj7312.Copy.config = 0
      self.obj7312.Specify=ATOM3Constraint()
      self.obj7312.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj731.GGset2Any['ReqFlow']= self.obj7312

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj731)
      self.obj731.postAction( self.RHS.CREATE )

      self.obj732=operatingUnit(parent)
      self.obj732.preAction( self.RHS.CREATE )
      self.obj732.isGraphObjectVisual = True

      if(hasattr(self.obj732, '_setHierarchicalLink')):
        self.obj732._setHierarchicalLink(False)

      # OperCostProp
      self.obj732.OperCostProp.setNone()

      # name
      self.obj732.name.setValue('')
      self.obj732.name.setNone()

      # OperCostFix
      self.obj732.OperCostFix.setNone()

      self.obj732.GGLabel.setValue(5)
      self.obj732.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(280.0,140.0,self.obj732)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj732.graphObject_ = new_obj
      self.obj7320= AttrCalc()
      self.obj7320.Copy=ATOM3Boolean()
      self.obj7320.Copy.setValue(('Copy from LHS', 1))
      self.obj7320.Copy.config = 0
      self.obj7320.Specify=ATOM3Constraint()
      self.obj7320.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj732.GGset2Any['OperCostProp']= self.obj7320
      self.obj7321= AttrCalc()
      self.obj7321.Copy=ATOM3Boolean()
      self.obj7321.Copy.setValue(('Copy from LHS', 1))
      self.obj7321.Copy.config = 0
      self.obj7321.Specify=ATOM3Constraint()
      self.obj7321.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj732.GGset2Any['name']= self.obj7321
      self.obj7322= AttrCalc()
      self.obj7322.Copy=ATOM3Boolean()
      self.obj7322.Copy.setValue(('Copy from LHS', 1))
      self.obj7322.Copy.config = 0
      self.obj7322.Specify=ATOM3Constraint()
      self.obj7322.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj732.GGset2Any['OperCostFix']= self.obj7322

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj732)
      self.obj732.postAction( self.RHS.CREATE )

      self.obj733=intoMaterial(parent)
      self.obj733.preAction( self.RHS.CREATE )
      self.obj733.isGraphObjectVisual = True

      if(hasattr(self.obj733, '_setHierarchicalLink')):
        self.obj733._setHierarchicalLink(False)

      # rate
      self.obj733.rate.setValue(0.0)

      self.obj733.GGLabel.setValue(10)
      self.obj733.graphClass_= graph_intoMaterial
      if parent.genGraphics:
         new_obj = graph_intoMaterial(315.25,202.5,self.obj733)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj733.graphObject_ = new_obj
      self.obj7330= AttrCalc()
      self.obj7330.Copy=ATOM3Boolean()
      self.obj7330.Copy.setValue(('Copy from LHS', 0))
      self.obj7330.Copy.config = 0
      self.obj7330.Specify=ATOM3Constraint()
      self.obj7330.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(3)).rate.getValue()\n\n\n\n\n\n\n\n\n\n'))
      self.obj733.GGset2Any['rate']= self.obj7330

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj733)
      self.obj733.postAction( self.RHS.CREATE )

      self.obj734=fromMaterial(parent)
      self.obj734.preAction( self.RHS.CREATE )
      self.obj734.isGraphObjectVisual = True

      if(hasattr(self.obj734, '_setHierarchicalLink')):
        self.obj734._setHierarchicalLink(False)

      # rate
      self.obj734.rate.setNone()

      self.obj734.GGLabel.setValue(8)
      self.obj734.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(323.0,83.0,self.obj734)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj734.graphObject_ = new_obj
      self.obj7340= AttrCalc()
      self.obj7340.Copy=ATOM3Boolean()
      self.obj7340.Copy.setValue(('Copy from LHS', 1))
      self.obj7340.Copy.config = 0
      self.obj7340.Specify=ATOM3Constraint()
      self.obj7340.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj734.GGset2Any['rate']= self.obj7340

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj734)
      self.obj734.postAction( self.RHS.CREATE )

      self.obj735=Goal(parent)
      self.obj735.preAction( self.RHS.CREATE )
      self.obj735.isGraphObjectVisual = True

      if(hasattr(self.obj735, '_setHierarchicalLink')):
        self.obj735._setHierarchicalLink(False)

      # name
      self.obj735.name.setValue('')
      self.obj735.name.setNone()

      self.obj735.GGLabel.setValue(2)
      self.obj735.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(60.0,220.0,self.obj735)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj735.graphObject_ = new_obj
      self.obj7350= AttrCalc()
      self.obj7350.Copy=ATOM3Boolean()
      self.obj7350.Copy.setValue(('Copy from LHS', 1))
      self.obj7350.Copy.config = 0
      self.obj7350.Specify=ATOM3Constraint()
      self.obj7350.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj735.GGset2Any['name']= self.obj7350

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj735)
      self.obj735.postAction( self.RHS.CREATE )

      self.obj736=Role(parent)
      self.obj736.preAction( self.RHS.CREATE )
      self.obj736.isGraphObjectVisual = True

      if(hasattr(self.obj736, '_setHierarchicalLink')):
        self.obj736._setHierarchicalLink(False)

      # name
      self.obj736.name.setValue('')
      self.obj736.name.setNone()

      self.obj736.GGLabel.setValue(1)
      self.obj736.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(60.0,40.0,self.obj736)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj736.graphObject_ = new_obj
      self.obj7360= AttrCalc()
      self.obj7360.Copy=ATOM3Boolean()
      self.obj7360.Copy.setValue(('Copy from LHS', 1))
      self.obj7360.Copy.config = 0
      self.obj7360.Specify=ATOM3Constraint()
      self.obj7360.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj736.GGset2Any['name']= self.obj7360

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj736)
      self.obj736.postAction( self.RHS.CREATE )

      self.obj737=achieve(parent)
      self.obj737.preAction( self.RHS.CREATE )
      self.obj737.isGraphObjectVisual = True

      if(hasattr(self.obj737, '_setHierarchicalLink')):
        self.obj737._setHierarchicalLink(False)

      # rate
      self.obj737.rate.setNone()

      self.obj737.GGLabel.setValue(3)
      self.obj737.graphClass_= graph_achieve
      if parent.genGraphics:
         new_obj = graph_achieve(93.5,143.5,self.obj737)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj737.graphObject_ = new_obj
      self.obj7370= AttrCalc()
      self.obj7370.Copy=ATOM3Boolean()
      self.obj7370.Copy.setValue(('Copy from LHS', 1))
      self.obj7370.Copy.config = 0
      self.obj7370.Specify=ATOM3Constraint()
      self.obj7370.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj737.GGset2Any['rate']= self.obj7370

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj737)
      self.obj737.postAction( self.RHS.CREATE )

      self.obj738=GenericGraphEdge(parent)
      self.obj738.preAction( self.RHS.CREATE )
      self.obj738.isGraphObjectVisual = True

      if(hasattr(self.obj738, '_setHierarchicalLink')):
        self.obj738._setHierarchicalLink(False)

      self.obj738.GGLabel.setValue(7)
      self.obj738.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(215.0,41.5,self.obj738)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj738.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj738)
      self.obj738.postAction( self.RHS.CREATE )

      self.obj739=GenericGraphEdge(parent)
      self.obj739.preAction( self.RHS.CREATE )
      self.obj739.isGraphObjectVisual = True

      if(hasattr(self.obj739, '_setHierarchicalLink')):
        self.obj739._setHierarchicalLink(False)

      self.obj739.GGLabel.setValue(9)
      self.obj739.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(185.0,276.0,self.obj739)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj739.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj739)
      self.obj739.postAction( self.RHS.CREATE )

      self.obj730.out_connections_.append(self.obj734)
      self.obj734.in_connections_.append(self.obj730)
      self.obj730.graphObject_.pendingConnections.append((self.obj730.graphObject_.tag, self.obj734.graphObject_.tag, [284.0, 69.0, 323.0, 83.0], 2, 0))
      self.obj732.out_connections_.append(self.obj733)
      self.obj733.in_connections_.append(self.obj732)
      self.obj732.graphObject_.pendingConnections.append((self.obj732.graphObject_.tag, self.obj733.graphObject_.tag, [333.0, 148.0, 332.0, 167.0, 371.25, 179.5], 2, True))
      self.obj733.out_connections_.append(self.obj731)
      self.obj731.in_connections_.append(self.obj733)
      self.obj733.graphObject_.pendingConnections.append((self.obj733.graphObject_.tag, self.obj731.graphObject_.tag, [326.0, 250.0, 354.5, 215.0, 371.25, 179.5], 2, True))
      self.obj734.out_connections_.append(self.obj732)
      self.obj732.in_connections_.append(self.obj734)
      self.obj734.graphObject_.pendingConnections.append((self.obj734.graphObject_.tag, self.obj732.graphObject_.tag, [333.0, 148.0, 352.0, 90.0], 2, 0))
      self.obj735.out_connections_.append(self.obj739)
      self.obj739.in_connections_.append(self.obj735)
      self.obj735.graphObject_.pendingConnections.append((self.obj735.graphObject_.tag, self.obj739.graphObject_.tag, [94.0, 270.0, 185.0, 276.0], 2, 0))
      self.obj736.out_connections_.append(self.obj737)
      self.obj737.in_connections_.append(self.obj736)
      self.obj736.graphObject_.pendingConnections.append((self.obj736.graphObject_.tag, self.obj737.graphObject_.tag, [91.0, 85.0, 93.5, 143.5], 2, 0))
      self.obj736.out_connections_.append(self.obj738)
      self.obj738.in_connections_.append(self.obj736)
      self.obj736.graphObject_.pendingConnections.append((self.obj736.graphObject_.tag, self.obj738.graphObject_.tag, [91.0, 40.0, 215.0, 41.5], 2, 0))
      self.obj737.out_connections_.append(self.obj735)
      self.obj735.in_connections_.append(self.obj737)
      self.obj737.graphObject_.pendingConnections.append((self.obj737.graphObject_.tag, self.obj735.graphObject_.tag, [93.0, 221.0, 93.5, 143.5], 2, 0))
      self.obj738.out_connections_.append(self.obj730)
      self.obj730.in_connections_.append(self.obj738)
      self.obj738.graphObject_.pendingConnections.append((self.obj738.graphObject_.tag, self.obj730.graphObject_.tag, [266.0, 62.0, 215.0, 41.5], 2, 0))
      self.obj739.out_connections_.append(self.obj731)
      self.obj731.in_connections_.append(self.obj739)
      self.obj739.graphObject_.pendingConnections.append((self.obj739.graphObject_.tag, self.obj731.graphObject_.tag, [286.0, 282.0, 185.0, 276.0], 2, 0))

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
      
      

