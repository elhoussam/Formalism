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

      self.obj695=CapableOf(parent)
      self.obj695.preAction( self.LHS.CREATE )
      self.obj695.isGraphObjectVisual = True

      if(hasattr(self.obj695, '_setHierarchicalLink')):
        self.obj695._setHierarchicalLink(False)

      # rate
      self.obj695.rate.setNone()

      self.obj695.GGLabel.setValue(4)
      self.obj695.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(250.75,110.75,self.obj695)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj695.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj695)
      self.obj695.postAction( self.LHS.CREATE )

      self.obj696=Goal(parent)
      self.obj696.preAction( self.LHS.CREATE )
      self.obj696.isGraphObjectVisual = True

      if(hasattr(self.obj696, '_setHierarchicalLink')):
        self.obj696._setHierarchicalLink(False)

      # name
      self.obj696.name.setValue('')
      self.obj696.name.setNone()

      self.obj696.GGLabel.setValue(3)
      self.obj696.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(100.0,240.0,self.obj696)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj696.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj696)
      self.obj696.postAction( self.LHS.CREATE )

      self.obj697=Agent(parent)
      self.obj697.preAction( self.LHS.CREATE )
      self.obj697.isGraphObjectVisual = True

      if(hasattr(self.obj697, '_setHierarchicalLink')):
        self.obj697._setHierarchicalLink(False)

      # price
      self.obj697.price.setNone()

      # name
      self.obj697.name.setValue('')
      self.obj697.name.setNone()

      self.obj697.GGLabel.setValue(1)
      self.obj697.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(80.0,40.0,self.obj697)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj697.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj697)
      self.obj697.postAction( self.LHS.CREATE )

      self.obj698=Role(parent)
      self.obj698.preAction( self.LHS.CREATE )
      self.obj698.isGraphObjectVisual = True

      if(hasattr(self.obj698, '_setHierarchicalLink')):
        self.obj698._setHierarchicalLink(False)

      # name
      self.obj698.name.setValue('')
      self.obj698.name.setNone()

      self.obj698.GGLabel.setValue(2)
      self.obj698.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(280.0,140.0,self.obj698)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj698.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj698)
      self.obj698.postAction( self.LHS.CREATE )

      self.obj699=achieve(parent)
      self.obj699.preAction( self.LHS.CREATE )
      self.obj699.isGraphObjectVisual = True

      if(hasattr(self.obj699, '_setHierarchicalLink')):
        self.obj699._setHierarchicalLink(False)

      # rate
      self.obj699.rate.setNone()

      self.obj699.GGLabel.setValue(5)
      self.obj699.graphClass_= graph_achieve
      if parent.genGraphics:
         new_obj = graph_achieve(258.5,259.0,self.obj699)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj699.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj699)
      self.obj699.postAction( self.LHS.CREATE )

      self.obj695.out_connections_.append(self.obj698)
      self.obj698.in_connections_.append(self.obj695)
      self.obj695.graphObject_.pendingConnections.append((self.obj695.graphObject_.tag, self.obj698.graphObject_.tag, [304.0, 141.0, 300.5, 120.5, 250.75, 110.75], 2, True))
      self.obj697.out_connections_.append(self.obj695)
      self.obj695.in_connections_.append(self.obj697)
      self.obj697.graphObject_.pendingConnections.append((self.obj697.graphObject_.tag, self.obj695.graphObject_.tag, [105.0, 102.0, 201.0, 101.0, 250.75, 110.75], 2, True))
      self.obj698.out_connections_.append(self.obj699)
      self.obj699.in_connections_.append(self.obj698)
      self.obj698.graphObject_.pendingConnections.append((self.obj698.graphObject_.tag, self.obj699.graphObject_.tag, [304.0, 186.0, 303.5, 233.0, 258.5, 259.0], 2, True))
      self.obj699.out_connections_.append(self.obj696)
      self.obj696.in_connections_.append(self.obj699)
      self.obj699.graphObject_.pendingConnections.append((self.obj699.graphObject_.tag, self.obj696.graphObject_.tag, [124.0, 290.0, 213.5, 285.0, 258.5, 259.0], 2, True))

      self.RHS = ASG_pns(parent)
      self.RHS.merge(ASG_omacs(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj703=metarial(parent)
      self.obj703.preAction( self.RHS.CREATE )
      self.obj703.isGraphObjectVisual = True

      if(hasattr(self.obj703, '_setHierarchicalLink')):
        self.obj703._setHierarchicalLink(False)

      # MaxFlow
      self.obj703.MaxFlow.setValue(999999)

      # price
      self.obj703.price.setValue(0)

      # Name
      self.obj703.Name.setValue('')
      self.obj703.Name.setNone()

      # ReqFlow
      self.obj703.ReqFlow.setValue(0)

      self.obj703.GGLabel.setValue(8)
      self.obj703.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(400.0,80.0,self.obj703)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj703.graphObject_ = new_obj
      self.obj7030= AttrCalc()
      self.obj7030.Copy=ATOM3Boolean()
      self.obj7030.Copy.setValue(('Copy from LHS', 1))
      self.obj7030.Copy.config = 0
      self.obj7030.Specify=ATOM3Constraint()
      self.obj7030.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj703.GGset2Any['MaxFlow']= self.obj7030
      self.obj7031= AttrCalc()
      self.obj7031.Copy=ATOM3Boolean()
      self.obj7031.Copy.setValue(('Copy from LHS', 0))
      self.obj7031.Copy.config = 0
      self.obj7031.Specify=ATOM3Constraint()
      self.obj7031.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()+\' \'+ self.getMatched(graphID, self.LHS.nodeWithLabel(2)).name.getValue()+\' \'+ self.getMatched(graphID, self.LHS.nodeWithLabel(3)).name.getValue()\n\n'))
      self.obj703.GGset2Any['Name']= self.obj7031
      self.obj7032= AttrCalc()
      self.obj7032.Copy=ATOM3Boolean()
      self.obj7032.Copy.setValue(('Copy from LHS', 1))
      self.obj7032.Copy.config = 0
      self.obj7032.Specify=ATOM3Constraint()
      self.obj7032.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj703.GGset2Any['ReqFlow']= self.obj7032

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj703)
      self.obj703.postAction( self.RHS.CREATE )

      self.obj704=operatingUnit(parent)
      self.obj704.preAction( self.RHS.CREATE )
      self.obj704.isGraphObjectVisual = True

      if(hasattr(self.obj704, '_setHierarchicalLink')):
        self.obj704._setHierarchicalLink(False)

      # OperCostProp
      self.obj704.OperCostProp.setValue(0.0)

      # name
      self.obj704.name.setValue('')
      self.obj704.name.setNone()

      # OperCostFix
      self.obj704.OperCostFix.setValue(0.0)

      self.obj704.GGLabel.setValue(7)
      self.obj704.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(400.0,240.0,self.obj704)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj704.graphObject_ = new_obj
      self.obj7040= AttrCalc()
      self.obj7040.Copy=ATOM3Boolean()
      self.obj7040.Copy.setValue(('Copy from LHS', 0))
      self.obj7040.Copy.config = 0
      self.obj7040.Specify=ATOM3Constraint()
      self.obj7040.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(5)).rate.getValue()\n'))
      self.obj704.GGset2Any['OperCostProp']= self.obj7040
      self.obj7041= AttrCalc()
      self.obj7041.Copy=ATOM3Boolean()
      self.obj7041.Copy.setValue(('Copy from LHS', 0))
      self.obj7041.Copy.config = 0
      self.obj7041.Specify=ATOM3Constraint()
      self.obj7041.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()+\' \'+ self.getMatched(graphID, self.LHS.nodeWithLabel(2)).name.getValue()+\' \'+ self.getMatched(graphID, self.LHS.nodeWithLabel(3)).name.getValue()\n\n\n\n\n\n\n'))
      self.obj704.GGset2Any['name']= self.obj7041
      self.obj7042= AttrCalc()
      self.obj7042.Copy=ATOM3Boolean()
      self.obj7042.Copy.setValue(('Copy from LHS', 0))
      self.obj7042.Copy.config = 0
      self.obj7042.Specify=ATOM3Constraint()
      self.obj7042.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return 2.0\n'))
      self.obj704.GGset2Any['OperCostFix']= self.obj7042

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj704)
      self.obj704.postAction( self.RHS.CREATE )

      self.obj705=fromMaterial(parent)
      self.obj705.preAction( self.RHS.CREATE )
      self.obj705.isGraphObjectVisual = True

      if(hasattr(self.obj705, '_setHierarchicalLink')):
        self.obj705._setHierarchicalLink(False)

      # rate
      self.obj705.rate.setValue(1.0)

      self.obj705.GGLabel.setValue(9)
      self.obj705.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(422.0,190.0,self.obj705)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj705.graphObject_ = new_obj
      self.obj7050= AttrCalc()
      self.obj7050.Copy=ATOM3Boolean()
      self.obj7050.Copy.setValue(('Copy from LHS', 0))
      self.obj7050.Copy.config = 0
      self.obj7050.Specify=ATOM3Constraint()
      self.obj7050.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj705.GGset2Any['rate']= self.obj7050

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj705)
      self.obj705.postAction( self.RHS.CREATE )

      self.obj706=CapableOf(parent)
      self.obj706.preAction( self.RHS.CREATE )
      self.obj706.isGraphObjectVisual = True

      if(hasattr(self.obj706, '_setHierarchicalLink')):
        self.obj706._setHierarchicalLink(False)

      # rate
      self.obj706.rate.setNone()

      self.obj706.GGLabel.setValue(4)
      self.obj706.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(250.75,110.75,self.obj706)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj706.graphObject_ = new_obj
      self.obj7060= AttrCalc()
      self.obj7060.Copy=ATOM3Boolean()
      self.obj7060.Copy.setValue(('Copy from LHS', 1))
      self.obj7060.Copy.config = 0
      self.obj7060.Specify=ATOM3Constraint()
      self.obj7060.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj706.GGset2Any['rate']= self.obj7060

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj706)
      self.obj706.postAction( self.RHS.CREATE )

      self.obj707=Goal(parent)
      self.obj707.preAction( self.RHS.CREATE )
      self.obj707.isGraphObjectVisual = True

      if(hasattr(self.obj707, '_setHierarchicalLink')):
        self.obj707._setHierarchicalLink(False)

      # name
      self.obj707.name.setValue('')
      self.obj707.name.setNone()

      self.obj707.GGLabel.setValue(3)
      self.obj707.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(100.0,240.0,self.obj707)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj707.graphObject_ = new_obj
      self.obj7070= AttrCalc()
      self.obj7070.Copy=ATOM3Boolean()
      self.obj7070.Copy.setValue(('Copy from LHS', 1))
      self.obj7070.Copy.config = 0
      self.obj7070.Specify=ATOM3Constraint()
      self.obj7070.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj707.GGset2Any['name']= self.obj7070

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj707)
      self.obj707.postAction( self.RHS.CREATE )

      self.obj708=Agent(parent)
      self.obj708.preAction( self.RHS.CREATE )
      self.obj708.isGraphObjectVisual = True

      if(hasattr(self.obj708, '_setHierarchicalLink')):
        self.obj708._setHierarchicalLink(False)

      # price
      self.obj708.price.setNone()

      # name
      self.obj708.name.setValue('')
      self.obj708.name.setNone()

      self.obj708.GGLabel.setValue(1)
      self.obj708.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(80.0,40.0,self.obj708)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj708.graphObject_ = new_obj
      self.obj7080= AttrCalc()
      self.obj7080.Copy=ATOM3Boolean()
      self.obj7080.Copy.setValue(('Copy from LHS', 1))
      self.obj7080.Copy.config = 0
      self.obj7080.Specify=ATOM3Constraint()
      self.obj7080.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj708.GGset2Any['price']= self.obj7080
      self.obj7081= AttrCalc()
      self.obj7081.Copy=ATOM3Boolean()
      self.obj7081.Copy.setValue(('Copy from LHS', 1))
      self.obj7081.Copy.config = 0
      self.obj7081.Specify=ATOM3Constraint()
      self.obj7081.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj708.GGset2Any['name']= self.obj7081

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj708)
      self.obj708.postAction( self.RHS.CREATE )

      self.obj709=Role(parent)
      self.obj709.preAction( self.RHS.CREATE )
      self.obj709.isGraphObjectVisual = True

      if(hasattr(self.obj709, '_setHierarchicalLink')):
        self.obj709._setHierarchicalLink(False)

      # name
      self.obj709.name.setValue('')
      self.obj709.name.setNone()

      self.obj709.GGLabel.setValue(2)
      self.obj709.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(280.0,140.0,self.obj709)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj709.graphObject_ = new_obj
      self.obj7090= AttrCalc()
      self.obj7090.Copy=ATOM3Boolean()
      self.obj7090.Copy.setValue(('Copy from LHS', 1))
      self.obj7090.Copy.config = 0
      self.obj7090.Specify=ATOM3Constraint()
      self.obj7090.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj709.GGset2Any['name']= self.obj7090

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj709)
      self.obj709.postAction( self.RHS.CREATE )

      self.obj710=achieve(parent)
      self.obj710.preAction( self.RHS.CREATE )
      self.obj710.isGraphObjectVisual = True

      if(hasattr(self.obj710, '_setHierarchicalLink')):
        self.obj710._setHierarchicalLink(False)

      # rate
      self.obj710.rate.setNone()

      self.obj710.GGLabel.setValue(5)
      self.obj710.graphClass_= graph_achieve
      if parent.genGraphics:
         new_obj = graph_achieve(258.5,259.0,self.obj710)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj710.graphObject_ = new_obj
      self.obj7100= AttrCalc()
      self.obj7100.Copy=ATOM3Boolean()
      self.obj7100.Copy.setValue(('Copy from LHS', 1))
      self.obj7100.Copy.config = 0
      self.obj7100.Specify=ATOM3Constraint()
      self.obj7100.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj710.GGset2Any['rate']= self.obj7100

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj710)
      self.obj710.postAction( self.RHS.CREATE )

      self.obj711=GenericGraphEdge(parent)
      self.obj711.preAction( self.RHS.CREATE )
      self.obj711.isGraphObjectVisual = True

      if(hasattr(self.obj711, '_setHierarchicalLink')):
        self.obj711._setHierarchicalLink(False)

      self.obj711.GGLabel.setValue(10)
      self.obj711.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(358.5,131.0,self.obj711)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj711.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj711)
      self.obj711.postAction( self.RHS.CREATE )

      self.obj703.out_connections_.append(self.obj705)
      self.obj705.in_connections_.append(self.obj703)
      self.obj703.graphObject_.pendingConnections.append((self.obj703.graphObject_.tag, self.obj705.graphObject_.tag, [424.0, 129.0, 422.0, 190.0], 0, True))
      self.obj705.out_connections_.append(self.obj704)
      self.obj704.in_connections_.append(self.obj705)
      self.obj705.graphObject_.pendingConnections.append((self.obj705.graphObject_.tag, self.obj704.graphObject_.tag, [420.0, 251.0, 422.0, 190.0], 0, True))
      self.obj706.out_connections_.append(self.obj709)
      self.obj709.in_connections_.append(self.obj706)
      self.obj706.graphObject_.pendingConnections.append((self.obj706.graphObject_.tag, self.obj709.graphObject_.tag, [311.0, 140.0, 250.75, 110.75], 2, 0))
      self.obj708.out_connections_.append(self.obj706)
      self.obj706.in_connections_.append(self.obj708)
      self.obj708.graphObject_.pendingConnections.append((self.obj708.graphObject_.tag, self.obj706.graphObject_.tag, [117.0, 102.0, 250.75, 110.75], 2, 0))
      self.obj709.out_connections_.append(self.obj710)
      self.obj710.in_connections_.append(self.obj709)
      self.obj709.graphObject_.pendingConnections.append((self.obj709.graphObject_.tag, self.obj710.graphObject_.tag, [311.0, 185.0, 258.5, 259.0], 2, 0))
      self.obj709.out_connections_.append(self.obj711)
      self.obj711.in_connections_.append(self.obj709)
      self.obj709.graphObject_.pendingConnections.append((self.obj709.graphObject_.tag, self.obj711.graphObject_.tag, [311.0, 140.0, 358.5, 131.0], 0, True))
      self.obj710.out_connections_.append(self.obj707)
      self.obj707.in_connections_.append(self.obj710)
      self.obj710.graphObject_.pendingConnections.append((self.obj710.graphObject_.tag, self.obj707.graphObject_.tag, [134.0, 290.0, 258.5, 259.0], 2, 0))
      self.obj711.out_connections_.append(self.obj703)
      self.obj703.in_connections_.append(self.obj711)
      self.obj711.graphObject_.pendingConnections.append((self.obj711.graphObject_.tag, self.obj703.graphObject_.tag, [406.0, 122.0, 358.5, 131.0], 0, True))

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
      

