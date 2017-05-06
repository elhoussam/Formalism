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

      self.obj746=rawMaterial(parent)
      self.obj746.preAction( self.LHS.CREATE )
      self.obj746.isGraphObjectVisual = True

      if(hasattr(self.obj746, '_setHierarchicalLink')):
        self.obj746._setHierarchicalLink(False)

      # MaxFlow
      self.obj746.MaxFlow.setNone()

      # price
      self.obj746.price.setValue(0)

      # Name
      self.obj746.Name.setValue('')
      self.obj746.Name.setNone()

      # ReqFlow
      self.obj746.ReqFlow.setNone()

      self.obj746.GGLabel.setValue(6)
      self.obj746.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(240.0,0.0,self.obj746)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj746.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj746)
      self.obj746.postAction( self.LHS.CREATE )

      self.obj747=metarial(parent)
      self.obj747.preAction( self.LHS.CREATE )
      self.obj747.isGraphObjectVisual = True

      if(hasattr(self.obj747, '_setHierarchicalLink')):
        self.obj747._setHierarchicalLink(False)

      # MaxFlow
      self.obj747.MaxFlow.setNone()

      # price
      self.obj747.price.setValue(0)

      # Name
      self.obj747.Name.setValue('')
      self.obj747.Name.setNone()

      # ReqFlow
      self.obj747.ReqFlow.setNone()

      self.obj747.GGLabel.setValue(11)
      self.obj747.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(260.0,200.0,self.obj747)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj747.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj747)
      self.obj747.postAction( self.LHS.CREATE )

      self.obj748=operatingUnit(parent)
      self.obj748.preAction( self.LHS.CREATE )
      self.obj748.isGraphObjectVisual = True

      if(hasattr(self.obj748, '_setHierarchicalLink')):
        self.obj748._setHierarchicalLink(False)

      # OperCostProp
      self.obj748.OperCostProp.setNone()

      # name
      self.obj748.name.setValue('')
      self.obj748.name.setNone()

      # OperCostFix
      self.obj748.OperCostFix.setNone()

      self.obj748.GGLabel.setValue(7)
      self.obj748.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(280.0,100.0,self.obj748)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj748.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj748)
      self.obj748.postAction( self.LHS.CREATE )

      self.obj749=operatingUnit(parent)
      self.obj749.preAction( self.LHS.CREATE )
      self.obj749.isGraphObjectVisual = True

      if(hasattr(self.obj749, '_setHierarchicalLink')):
        self.obj749._setHierarchicalLink(False)

      # OperCostProp
      self.obj749.OperCostProp.setNone()

      # name
      self.obj749.name.setValue('')
      self.obj749.name.setNone()

      # OperCostFix
      self.obj749.OperCostFix.setNone()

      self.obj749.GGLabel.setValue(12)
      self.obj749.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(360.0,260.0,self.obj749)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj749.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj749)
      self.obj749.postAction( self.LHS.CREATE )

      self.obj750=fromRaw(parent)
      self.obj750.preAction( self.LHS.CREATE )
      self.obj750.isGraphObjectVisual = True

      if(hasattr(self.obj750, '_setHierarchicalLink')):
        self.obj750._setHierarchicalLink(False)

      # rate
      self.obj750.rate.setNone()

      self.obj750.GGLabel.setValue(8)
      self.obj750.graphClass_= graph_fromRaw
      if parent.genGraphics:
         new_obj = graph_fromRaw(311.5,63.25,self.obj750)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj750.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj750)
      self.obj750.postAction( self.LHS.CREATE )

      self.obj751=fromMaterial(parent)
      self.obj751.preAction( self.LHS.CREATE )
      self.obj751.isGraphObjectVisual = True

      if(hasattr(self.obj751, '_setHierarchicalLink')):
        self.obj751._setHierarchicalLink(False)

      # rate
      self.obj751.rate.setNone()

      self.obj751.GGLabel.setValue(14)
      self.obj751.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(379.5,235.25,self.obj751)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj751.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj751)
      self.obj751.postAction( self.LHS.CREATE )

      self.obj752=CapableOf(parent)
      self.obj752.preAction( self.LHS.CREATE )
      self.obj752.isGraphObjectVisual = True

      if(hasattr(self.obj752, '_setHierarchicalLink')):
        self.obj752._setHierarchicalLink(False)

      # rate
      self.obj752.rate.setNone()

      self.obj752.GGLabel.setValue(3)
      self.obj752.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(84.5,131.5,self.obj752)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj752.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj752)
      self.obj752.postAction( self.LHS.CREATE )

      self.obj753=Agent(parent)
      self.obj753.preAction( self.LHS.CREATE )
      self.obj753.isGraphObjectVisual = True

      if(hasattr(self.obj753, '_setHierarchicalLink')):
        self.obj753._setHierarchicalLink(False)

      # price
      self.obj753.price.setNone()

      # name
      self.obj753.name.setValue('')
      self.obj753.name.setNone()

      self.obj753.GGLabel.setValue(1)
      self.obj753.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(60.0,20.0,self.obj753)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj753.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj753)
      self.obj753.postAction( self.LHS.CREATE )

      self.obj754=Role(parent)
      self.obj754.preAction( self.LHS.CREATE )
      self.obj754.isGraphObjectVisual = True

      if(hasattr(self.obj754, '_setHierarchicalLink')):
        self.obj754._setHierarchicalLink(False)

      # name
      self.obj754.name.setValue('')
      self.obj754.name.setNone()

      self.obj754.GGLabel.setValue(2)
      self.obj754.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(60.0,180.0,self.obj754)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj754.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj754)
      self.obj754.postAction( self.LHS.CREATE )

      self.obj755=GenericGraphEdge(parent)
      self.obj755.preAction( self.LHS.CREATE )
      self.obj755.isGraphObjectVisual = True

      if(hasattr(self.obj755, '_setHierarchicalLink')):
        self.obj755._setHierarchicalLink(False)

      self.obj755.GGLabel.setValue(15)
      self.obj755.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(174.5,69.0,self.obj755)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj755.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj755)
      self.obj755.postAction( self.LHS.CREATE )

      self.obj756=GenericGraphEdge(parent)
      self.obj756.preAction( self.LHS.CREATE )
      self.obj756.isGraphObjectVisual = True

      if(hasattr(self.obj756, '_setHierarchicalLink')):
        self.obj756._setHierarchicalLink(False)

      self.obj756.GGLabel.setValue(10)
      self.obj756.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(245.75,97.25,self.obj756)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj756.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj756)
      self.obj756.postAction( self.LHS.CREATE )

      self.obj757=GenericGraphEdge(parent)
      self.obj757.preAction( self.LHS.CREATE )
      self.obj757.isGraphObjectVisual = True

      if(hasattr(self.obj757, '_setHierarchicalLink')):
        self.obj757._setHierarchicalLink(False)

      self.obj757.GGLabel.setValue(13)
      self.obj757.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(175.0,234.0,self.obj757)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj757.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj757)
      self.obj757.postAction( self.LHS.CREATE )

      self.obj746.out_connections_.append(self.obj750)
      self.obj750.in_connections_.append(self.obj746)
      self.obj746.graphObject_.pendingConnections.append((self.obj746.graphObject_.tag, self.obj750.graphObject_.tag, [264.0, 56.0, 295.0, 49.5, 311.5, 63.25], 2, True))
      self.obj747.out_connections_.append(self.obj751)
      self.obj751.in_connections_.append(self.obj747)
      self.obj747.graphObject_.pendingConnections.append((self.obj747.graphObject_.tag, self.obj751.graphObject_.tag, [306.0, 210.0, 353.5, 220.0, 379.5, 235.25], 2, True))
      self.obj750.out_connections_.append(self.obj748)
      self.obj748.in_connections_.append(self.obj750)
      self.obj750.graphObject_.pendingConnections.append((self.obj750.graphObject_.tag, self.obj748.graphObject_.tag, [330.0, 111.0, 328.0, 77.0, 311.5, 63.25], 2, True))
      self.obj751.out_connections_.append(self.obj749)
      self.obj749.in_connections_.append(self.obj751)
      self.obj751.graphObject_.pendingConnections.append((self.obj751.graphObject_.tag, self.obj749.graphObject_.tag, [410.0, 271.0, 405.5, 250.5, 379.5, 235.25], 2, True))
      self.obj752.out_connections_.append(self.obj754)
      self.obj754.in_connections_.append(self.obj752)
      self.obj752.graphObject_.pendingConnections.append((self.obj752.graphObject_.tag, self.obj754.graphObject_.tag, [84.0, 181.0, 84.5, 131.5], 0, True))
      self.obj753.out_connections_.append(self.obj752)
      self.obj752.in_connections_.append(self.obj753)
      self.obj753.graphObject_.pendingConnections.append((self.obj753.graphObject_.tag, self.obj752.graphObject_.tag, [85.0, 82.0, 84.5, 131.5], 0, True))
      self.obj753.out_connections_.append(self.obj755)
      self.obj755.in_connections_.append(self.obj753)
      self.obj753.graphObject_.pendingConnections.append((self.obj753.graphObject_.tag, self.obj755.graphObject_.tag, [85.0, 82.0, 174.5, 69.0], 0, True))
      self.obj753.out_connections_.append(self.obj756)
      self.obj756.in_connections_.append(self.obj753)
      self.obj753.graphObject_.pendingConnections.append((self.obj753.graphObject_.tag, self.obj756.graphObject_.tag, [85.0, 82.0, 192.0, 90.0, 245.75, 97.25], 2, True))
      self.obj754.out_connections_.append(self.obj757)
      self.obj757.in_connections_.append(self.obj754)
      self.obj754.graphObject_.pendingConnections.append((self.obj754.graphObject_.tag, self.obj757.graphObject_.tag, [84.0, 226.0, 175.0, 234.0], 0, True))
      self.obj755.out_connections_.append(self.obj746)
      self.obj746.in_connections_.append(self.obj755)
      self.obj755.graphObject_.pendingConnections.append((self.obj755.graphObject_.tag, self.obj746.graphObject_.tag, [264.0, 56.0, 174.5, 69.0], 0, True))
      self.obj756.out_connections_.append(self.obj748)
      self.obj748.in_connections_.append(self.obj756)
      self.obj756.graphObject_.pendingConnections.append((self.obj756.graphObject_.tag, self.obj748.graphObject_.tag, [300.0, 111.0, 299.5, 104.5, 245.75, 97.25], 2, True))
      self.obj757.out_connections_.append(self.obj747)
      self.obj747.in_connections_.append(self.obj757)
      self.obj757.graphObject_.pendingConnections.append((self.obj757.graphObject_.tag, self.obj747.graphObject_.tag, [266.0, 242.0, 175.0, 234.0], 0, True))

      self.RHS = ASG_pns(parent)
      self.RHS.merge(ASG_omacs(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj761=rawMaterial(parent)
      self.obj761.preAction( self.RHS.CREATE )
      self.obj761.isGraphObjectVisual = True

      if(hasattr(self.obj761, '_setHierarchicalLink')):
        self.obj761._setHierarchicalLink(False)

      # MaxFlow
      self.obj761.MaxFlow.setNone()

      # price
      self.obj761.price.setValue(0)

      # Name
      self.obj761.Name.setValue('')
      self.obj761.Name.setNone()

      # ReqFlow
      self.obj761.ReqFlow.setNone()

      self.obj761.GGLabel.setValue(6)
      self.obj761.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(240.0,0.0,self.obj761)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj761.graphObject_ = new_obj
      self.obj7610= AttrCalc()
      self.obj7610.Copy=ATOM3Boolean()
      self.obj7610.Copy.setValue(('Copy from LHS', 1))
      self.obj7610.Copy.config = 0
      self.obj7610.Specify=ATOM3Constraint()
      self.obj7610.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj761.GGset2Any['MaxFlow']= self.obj7610
      self.obj7611= AttrCalc()
      self.obj7611.Copy=ATOM3Boolean()
      self.obj7611.Copy.setValue(('Copy from LHS', 1))
      self.obj7611.Copy.config = 0
      self.obj7611.Specify=ATOM3Constraint()
      self.obj7611.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj761.GGset2Any['Name']= self.obj7611
      self.obj7612= AttrCalc()
      self.obj7612.Copy=ATOM3Boolean()
      self.obj7612.Copy.setValue(('Copy from LHS', 1))
      self.obj7612.Copy.config = 0
      self.obj7612.Specify=ATOM3Constraint()
      self.obj7612.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj761.GGset2Any['ReqFlow']= self.obj7612

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj761)
      self.obj761.postAction( self.RHS.CREATE )

      self.obj762=metarial(parent)
      self.obj762.preAction( self.RHS.CREATE )
      self.obj762.isGraphObjectVisual = True

      if(hasattr(self.obj762, '_setHierarchicalLink')):
        self.obj762._setHierarchicalLink(False)

      # MaxFlow
      self.obj762.MaxFlow.setNone()

      # price
      self.obj762.price.setValue(0)

      # Name
      self.obj762.Name.setValue('')
      self.obj762.Name.setNone()

      # ReqFlow
      self.obj762.ReqFlow.setNone()

      self.obj762.GGLabel.setValue(11)
      self.obj762.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(260.0,200.0,self.obj762)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj762.graphObject_ = new_obj
      self.obj7620= AttrCalc()
      self.obj7620.Copy=ATOM3Boolean()
      self.obj7620.Copy.setValue(('Copy from LHS', 1))
      self.obj7620.Copy.config = 0
      self.obj7620.Specify=ATOM3Constraint()
      self.obj7620.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj762.GGset2Any['MaxFlow']= self.obj7620
      self.obj7621= AttrCalc()
      self.obj7621.Copy=ATOM3Boolean()
      self.obj7621.Copy.setValue(('Copy from LHS', 1))
      self.obj7621.Copy.config = 0
      self.obj7621.Specify=ATOM3Constraint()
      self.obj7621.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj762.GGset2Any['Name']= self.obj7621
      self.obj7622= AttrCalc()
      self.obj7622.Copy=ATOM3Boolean()
      self.obj7622.Copy.setValue(('Copy from LHS', 1))
      self.obj7622.Copy.config = 0
      self.obj7622.Specify=ATOM3Constraint()
      self.obj7622.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj762.GGset2Any['ReqFlow']= self.obj7622

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj762)
      self.obj762.postAction( self.RHS.CREATE )

      self.obj763=operatingUnit(parent)
      self.obj763.preAction( self.RHS.CREATE )
      self.obj763.isGraphObjectVisual = True

      if(hasattr(self.obj763, '_setHierarchicalLink')):
        self.obj763._setHierarchicalLink(False)

      # OperCostProp
      self.obj763.OperCostProp.setNone()

      # name
      self.obj763.name.setValue('')
      self.obj763.name.setNone()

      # OperCostFix
      self.obj763.OperCostFix.setNone()

      self.obj763.GGLabel.setValue(7)
      self.obj763.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(280.0,100.0,self.obj763)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj763.graphObject_ = new_obj
      self.obj7630= AttrCalc()
      self.obj7630.Copy=ATOM3Boolean()
      self.obj7630.Copy.setValue(('Copy from LHS', 1))
      self.obj7630.Copy.config = 0
      self.obj7630.Specify=ATOM3Constraint()
      self.obj7630.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj763.GGset2Any['OperCostProp']= self.obj7630
      self.obj7631= AttrCalc()
      self.obj7631.Copy=ATOM3Boolean()
      self.obj7631.Copy.setValue(('Copy from LHS', 1))
      self.obj7631.Copy.config = 0
      self.obj7631.Specify=ATOM3Constraint()
      self.obj7631.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj763.GGset2Any['name']= self.obj7631
      self.obj7632= AttrCalc()
      self.obj7632.Copy=ATOM3Boolean()
      self.obj7632.Copy.setValue(('Copy from LHS', 1))
      self.obj7632.Copy.config = 0
      self.obj7632.Specify=ATOM3Constraint()
      self.obj7632.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj763.GGset2Any['OperCostFix']= self.obj7632

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj763)
      self.obj763.postAction( self.RHS.CREATE )

      self.obj764=operatingUnit(parent)
      self.obj764.preAction( self.RHS.CREATE )
      self.obj764.isGraphObjectVisual = True

      if(hasattr(self.obj764, '_setHierarchicalLink')):
        self.obj764._setHierarchicalLink(False)

      # OperCostProp
      self.obj764.OperCostProp.setNone()

      # name
      self.obj764.name.setValue('')
      self.obj764.name.setNone()

      # OperCostFix
      self.obj764.OperCostFix.setNone()

      self.obj764.GGLabel.setValue(12)
      self.obj764.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(360.0,260.0,self.obj764)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj764.graphObject_ = new_obj
      self.obj7640= AttrCalc()
      self.obj7640.Copy=ATOM3Boolean()
      self.obj7640.Copy.setValue(('Copy from LHS', 1))
      self.obj7640.Copy.config = 0
      self.obj7640.Specify=ATOM3Constraint()
      self.obj7640.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj764.GGset2Any['OperCostProp']= self.obj7640
      self.obj7641= AttrCalc()
      self.obj7641.Copy=ATOM3Boolean()
      self.obj7641.Copy.setValue(('Copy from LHS', 1))
      self.obj7641.Copy.config = 0
      self.obj7641.Specify=ATOM3Constraint()
      self.obj7641.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj764.GGset2Any['name']= self.obj7641
      self.obj7642= AttrCalc()
      self.obj7642.Copy=ATOM3Boolean()
      self.obj7642.Copy.setValue(('Copy from LHS', 1))
      self.obj7642.Copy.config = 0
      self.obj7642.Specify=ATOM3Constraint()
      self.obj7642.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj764.GGset2Any['OperCostFix']= self.obj7642

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj764)
      self.obj764.postAction( self.RHS.CREATE )

      self.obj765=fromRaw(parent)
      self.obj765.preAction( self.RHS.CREATE )
      self.obj765.isGraphObjectVisual = True

      if(hasattr(self.obj765, '_setHierarchicalLink')):
        self.obj765._setHierarchicalLink(False)

      # rate
      self.obj765.rate.setNone()

      self.obj765.GGLabel.setValue(8)
      self.obj765.graphClass_= graph_fromRaw
      if parent.genGraphics:
         new_obj = graph_fromRaw(311.5,63.25,self.obj765)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj765.graphObject_ = new_obj
      self.obj7650= AttrCalc()
      self.obj7650.Copy=ATOM3Boolean()
      self.obj7650.Copy.setValue(('Copy from LHS', 1))
      self.obj7650.Copy.config = 0
      self.obj7650.Specify=ATOM3Constraint()
      self.obj7650.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj765.GGset2Any['rate']= self.obj7650

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj765)
      self.obj765.postAction( self.RHS.CREATE )

      self.obj766=intoMaterial(parent)
      self.obj766.preAction( self.RHS.CREATE )
      self.obj766.isGraphObjectVisual = True

      if(hasattr(self.obj766, '_setHierarchicalLink')):
        self.obj766._setHierarchicalLink(False)

      # rate
      self.obj766.rate.setValue(0.0)

      self.obj766.GGLabel.setValue(17)
      self.obj766.graphClass_= graph_intoMaterial
      if parent.genGraphics:
         new_obj = graph_intoMaterial(324.25,167.5,self.obj766)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj766.graphObject_ = new_obj
      self.obj7660= AttrCalc()
      self.obj7660.Copy=ATOM3Boolean()
      self.obj7660.Copy.setValue(('Copy from LHS', 0))
      self.obj7660.Copy.config = 0
      self.obj7660.Specify=ATOM3Constraint()
      self.obj7660.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'a = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) ).name.getValue()\nb = self.getMatched ( graphID , self.LHS.nodeWithLabel(2) ).name.getValue()\nreturn self.graphRewritingSystem.Dictag[ a ][b]\n\n'))
      self.obj766.GGset2Any['rate']= self.obj7660

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj766)
      self.obj766.postAction( self.RHS.CREATE )

      self.obj767=fromMaterial(parent)
      self.obj767.preAction( self.RHS.CREATE )
      self.obj767.isGraphObjectVisual = True

      if(hasattr(self.obj767, '_setHierarchicalLink')):
        self.obj767._setHierarchicalLink(False)

      # rate
      self.obj767.rate.setNone()

      self.obj767.GGLabel.setValue(14)
      self.obj767.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(379.5,235.25,self.obj767)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj767.graphObject_ = new_obj
      self.obj7670= AttrCalc()
      self.obj7670.Copy=ATOM3Boolean()
      self.obj7670.Copy.setValue(('Copy from LHS', 1))
      self.obj7670.Copy.config = 0
      self.obj7670.Specify=ATOM3Constraint()
      self.obj7670.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj767.GGset2Any['rate']= self.obj7670

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj767)
      self.obj767.postAction( self.RHS.CREATE )

      self.obj768=CapableOf(parent)
      self.obj768.preAction( self.RHS.CREATE )
      self.obj768.isGraphObjectVisual = True

      if(hasattr(self.obj768, '_setHierarchicalLink')):
        self.obj768._setHierarchicalLink(False)

      # rate
      self.obj768.rate.setNone()

      self.obj768.GGLabel.setValue(3)
      self.obj768.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(84.5,131.5,self.obj768)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj768.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj768)
      self.obj768.postAction( self.RHS.CREATE )

      self.obj769=Agent(parent)
      self.obj769.preAction( self.RHS.CREATE )
      self.obj769.isGraphObjectVisual = True

      if(hasattr(self.obj769, '_setHierarchicalLink')):
        self.obj769._setHierarchicalLink(False)

      # price
      self.obj769.price.setNone()

      # name
      self.obj769.name.setValue('')
      self.obj769.name.setNone()

      self.obj769.GGLabel.setValue(1)
      self.obj769.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(60.0,20.0,self.obj769)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj769.graphObject_ = new_obj
      self.obj7690= AttrCalc()
      self.obj7690.Copy=ATOM3Boolean()
      self.obj7690.Copy.setValue(('Copy from LHS', 1))
      self.obj7690.Copy.config = 0
      self.obj7690.Specify=ATOM3Constraint()
      self.obj7690.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj769.GGset2Any['price']= self.obj7690
      self.obj7691= AttrCalc()
      self.obj7691.Copy=ATOM3Boolean()
      self.obj7691.Copy.setValue(('Copy from LHS', 1))
      self.obj7691.Copy.config = 0
      self.obj7691.Specify=ATOM3Constraint()
      self.obj7691.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj769.GGset2Any['name']= self.obj7691

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj769)
      self.obj769.postAction( self.RHS.CREATE )

      self.obj770=Role(parent)
      self.obj770.preAction( self.RHS.CREATE )
      self.obj770.isGraphObjectVisual = True

      if(hasattr(self.obj770, '_setHierarchicalLink')):
        self.obj770._setHierarchicalLink(False)

      # name
      self.obj770.name.setValue('')
      self.obj770.name.setNone()

      self.obj770.GGLabel.setValue(2)
      self.obj770.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(60.0,180.0,self.obj770)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj770.graphObject_ = new_obj
      self.obj7700= AttrCalc()
      self.obj7700.Copy=ATOM3Boolean()
      self.obj7700.Copy.setValue(('Copy from LHS', 1))
      self.obj7700.Copy.config = 0
      self.obj7700.Specify=ATOM3Constraint()
      self.obj7700.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj770.GGset2Any['name']= self.obj7700

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj770)
      self.obj770.postAction( self.RHS.CREATE )

      self.obj771=GenericGraphEdge(parent)
      self.obj771.preAction( self.RHS.CREATE )
      self.obj771.isGraphObjectVisual = True

      if(hasattr(self.obj771, '_setHierarchicalLink')):
        self.obj771._setHierarchicalLink(False)

      self.obj771.GGLabel.setValue(15)
      self.obj771.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(174.5,69.0,self.obj771)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj771.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj771)
      self.obj771.postAction( self.RHS.CREATE )

      self.obj772=GenericGraphEdge(parent)
      self.obj772.preAction( self.RHS.CREATE )
      self.obj772.isGraphObjectVisual = True

      if(hasattr(self.obj772, '_setHierarchicalLink')):
        self.obj772._setHierarchicalLink(False)

      self.obj772.GGLabel.setValue(10)
      self.obj772.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(245.75,97.25,self.obj772)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj772.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj772)
      self.obj772.postAction( self.RHS.CREATE )

      self.obj773=GenericGraphEdge(parent)
      self.obj773.preAction( self.RHS.CREATE )
      self.obj773.isGraphObjectVisual = True

      if(hasattr(self.obj773, '_setHierarchicalLink')):
        self.obj773._setHierarchicalLink(False)

      self.obj773.GGLabel.setValue(13)
      self.obj773.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(175.0,234.0,self.obj773)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj773.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj773)
      self.obj773.postAction( self.RHS.CREATE )

      self.obj761.out_connections_.append(self.obj765)
      self.obj765.in_connections_.append(self.obj761)
      self.obj761.graphObject_.pendingConnections.append((self.obj761.graphObject_.tag, self.obj765.graphObject_.tag, [264.0, 50.0, 311.5, 63.25], 2, 0))
      self.obj762.out_connections_.append(self.obj767)
      self.obj767.in_connections_.append(self.obj762)
      self.obj762.graphObject_.pendingConnections.append((self.obj762.graphObject_.tag, self.obj767.graphObject_.tag, [306.0, 210.0, 379.5, 235.25], 2, 0))
      self.obj763.out_connections_.append(self.obj766)
      self.obj766.in_connections_.append(self.obj763)
      self.obj763.graphObject_.pendingConnections.append((self.obj763.graphObject_.tag, self.obj766.graphObject_.tag, [333.0, 108.0, 331.0, 142.0, 324.25, 167.5], 2, True))
      self.obj765.out_connections_.append(self.obj763)
      self.obj763.in_connections_.append(self.obj765)
      self.obj765.graphObject_.pendingConnections.append((self.obj765.graphObject_.tag, self.obj763.graphObject_.tag, [330.0, 101.0, 311.5, 63.25], 2, 0))
      self.obj766.out_connections_.append(self.obj762)
      self.obj762.in_connections_.append(self.obj766)
      self.obj766.graphObject_.pendingConnections.append((self.obj766.graphObject_.tag, self.obj762.graphObject_.tag, [306.0, 210.0, 317.5, 193.0, 324.25, 167.5], 2, True))
      self.obj767.out_connections_.append(self.obj764)
      self.obj764.in_connections_.append(self.obj767)
      self.obj767.graphObject_.pendingConnections.append((self.obj767.graphObject_.tag, self.obj764.graphObject_.tag, [413.0, 268.0, 379.5, 235.25], 2, 0))
      self.obj768.out_connections_.append(self.obj770)
      self.obj770.in_connections_.append(self.obj768)
      self.obj768.graphObject_.pendingConnections.append((self.obj768.graphObject_.tag, self.obj770.graphObject_.tag, [91.0, 180.0, 84.5, 131.5], 2, 0))
      self.obj769.out_connections_.append(self.obj768)
      self.obj768.in_connections_.append(self.obj769)
      self.obj769.graphObject_.pendingConnections.append((self.obj769.graphObject_.tag, self.obj768.graphObject_.tag, [97.0, 82.0, 84.5, 131.5], 2, 0))
      self.obj769.out_connections_.append(self.obj771)
      self.obj771.in_connections_.append(self.obj769)
      self.obj769.graphObject_.pendingConnections.append((self.obj769.graphObject_.tag, self.obj771.graphObject_.tag, [97.0, 82.0, 174.5, 69.0], 2, 0))
      self.obj769.out_connections_.append(self.obj772)
      self.obj772.in_connections_.append(self.obj769)
      self.obj769.graphObject_.pendingConnections.append((self.obj769.graphObject_.tag, self.obj772.graphObject_.tag, [97.0, 82.0, 245.75, 97.25], 2, 0))
      self.obj770.out_connections_.append(self.obj773)
      self.obj773.in_connections_.append(self.obj770)
      self.obj770.graphObject_.pendingConnections.append((self.obj770.graphObject_.tag, self.obj773.graphObject_.tag, [91.0, 225.0, 175.0, 234.0], 2, 0))
      self.obj771.out_connections_.append(self.obj761)
      self.obj761.in_connections_.append(self.obj771)
      self.obj771.graphObject_.pendingConnections.append((self.obj771.graphObject_.tag, self.obj761.graphObject_.tag, [264.0, 50.0, 174.5, 69.0], 2, 0))
      self.obj772.out_connections_.append(self.obj763)
      self.obj763.in_connections_.append(self.obj772)
      self.obj772.graphObject_.pendingConnections.append((self.obj772.graphObject_.tag, self.obj763.graphObject_.tag, [300.0, 101.0, 245.75, 97.25], 2, 0))
      self.obj773.out_connections_.append(self.obj762)
      self.obj762.in_connections_.append(self.obj773)
      self.obj773.graphObject_.pendingConnections.append((self.obj773.graphObject_.tag, self.obj762.graphObject_.tag, [266.0, 242.0, 175.0, 234.0], 2, 0))

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
      
      

