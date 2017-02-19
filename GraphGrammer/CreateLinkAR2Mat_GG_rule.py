# _ CreateLinkAR2Mat_GG_rule.py ____________________________________________________________________________
# File generated automatically by ATOM3. Graph Grammar Rule
# ___________________________________________________________________________________________
from GGrule import *
from CapableOf import *
from GenericGraphEdge import *
from Goal import *
from ASG_omacss import *
from intoProduct import *
from operatingUnit import *
from metarial import *
from rawMaterial import *
from Agent import *
from fromMaterial import *
from Capabilitie import *
from Role import *
from requir import *
from fromRaw import *
from ASG_pns2 import *
from intoMaterial import *
from ASG_GenericGraph import *
from product import *
from GenericGraphNode import *
from achieve import *
from posses import *
class CreateLinkAR2Mat_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 20)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_omacss(parent)
      self.LHS.merge(ASG_pns2(parent))
      self.LHS.merge(ASG_GenericGraph(parent))

      self.obj337=Agent(parent)
      self.obj337.preAction( self.LHS.CREATE )
      self.obj337.isGraphObjectVisual = True

      if(hasattr(self.obj337, '_setHierarchicalLink')):
        self.obj337._setHierarchicalLink(False)

      # price
      self.obj337.price.setNone()

      # name
      self.obj337.name.setValue('')
      self.obj337.name.setNone()

      self.obj337.GGLabel.setValue(1)
      self.obj337.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(40.0,20.0,self.obj337)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj337.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj337)
      self.obj337.postAction( self.LHS.CREATE )

      self.obj338=Role(parent)
      self.obj338.preAction( self.LHS.CREATE )
      self.obj338.isGraphObjectVisual = True

      if(hasattr(self.obj338, '_setHierarchicalLink')):
        self.obj338._setHierarchicalLink(False)

      # name
      self.obj338.name.setValue('')
      self.obj338.name.setNone()

      self.obj338.GGLabel.setValue(2)
      self.obj338.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(60.0,140.0,self.obj338)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj338.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj338)
      self.obj338.postAction( self.LHS.CREATE )

      self.obj339=CapableOf(parent)
      self.obj339.preAction( self.LHS.CREATE )
      self.obj339.isGraphObjectVisual = True

      if(hasattr(self.obj339, '_setHierarchicalLink')):
        self.obj339._setHierarchicalLink(False)

      self.obj339.GGLabel.setValue(3)
      self.obj339.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(74.5,111.5,self.obj339)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj339.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj339)
      self.obj339.postAction( self.LHS.CREATE )

      self.obj340=rawMaterial(parent)
      self.obj340.preAction( self.LHS.CREATE )
      self.obj340.isGraphObjectVisual = True

      if(hasattr(self.obj340, '_setHierarchicalLink')):
        self.obj340._setHierarchicalLink(False)

      # Name
      self.obj340.Name.setValue('')
      self.obj340.Name.setNone()

      self.obj340.GGLabel.setValue(6)
      self.obj340.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(240.0,20.0,self.obj340)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj340.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj340)
      self.obj340.postAction( self.LHS.CREATE )

      self.obj341=operatingUnit(parent)
      self.obj341.preAction( self.LHS.CREATE )
      self.obj341.isGraphObjectVisual = True

      if(hasattr(self.obj341, '_setHierarchicalLink')):
        self.obj341._setHierarchicalLink(False)

      # name
      self.obj341.name.setValue('')
      self.obj341.name.setNone()

      self.obj341.GGLabel.setValue(12)
      self.obj341.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(320.0,240.0,self.obj341)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj341.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj341)
      self.obj341.postAction( self.LHS.CREATE )

      self.obj342=operatingUnit(parent)
      self.obj342.preAction( self.LHS.CREATE )
      self.obj342.isGraphObjectVisual = True

      if(hasattr(self.obj342, '_setHierarchicalLink')):
        self.obj342._setHierarchicalLink(False)

      # name
      self.obj342.name.setValue('')
      self.obj342.name.setNone()

      self.obj342.GGLabel.setValue(7)
      self.obj342.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(320.0,100.0,self.obj342)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj342.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj342)
      self.obj342.postAction( self.LHS.CREATE )

      self.obj343=metarial(parent)
      self.obj343.preAction( self.LHS.CREATE )
      self.obj343.isGraphObjectVisual = True

      if(hasattr(self.obj343, '_setHierarchicalLink')):
        self.obj343._setHierarchicalLink(False)

      # Name
      self.obj343.Name.setValue('')
      self.obj343.Name.setNone()

      self.obj343.GGLabel.setValue(11)
      self.obj343.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(240.0,160.0,self.obj343)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj343.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj343)
      self.obj343.postAction( self.LHS.CREATE )

      self.obj344=fromMaterial(parent)
      self.obj344.preAction( self.LHS.CREATE )
      self.obj344.isGraphObjectVisual = True

      if(hasattr(self.obj344, '_setHierarchicalLink')):
        self.obj344._setHierarchicalLink(False)

      # rate
      self.obj344.rate.setNone()

      self.obj344.GGLabel.setValue(14)
      self.obj344.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(340.0,197.0,self.obj344)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj344.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj344)
      self.obj344.postAction( self.LHS.CREATE )

      self.obj345=fromRaw(parent)
      self.obj345.preAction( self.LHS.CREATE )
      self.obj345.isGraphObjectVisual = True

      if(hasattr(self.obj345, '_setHierarchicalLink')):
        self.obj345._setHierarchicalLink(False)

      # rate
      self.obj345.rate.setNone()

      self.obj345.GGLabel.setValue(9)
      self.obj345.graphClass_= graph_fromRaw
      if parent.genGraphics:
         new_obj = graph_fromRaw(329.081775701,37.1184210526,self.obj345)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj345.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj345)
      self.obj345.postAction( self.LHS.CREATE )

      self.obj346=GenericGraphEdge(parent)
      self.obj346.preAction( self.LHS.CREATE )
      self.obj346.isGraphObjectVisual = True

      if(hasattr(self.obj346, '_setHierarchicalLink')):
        self.obj346._setHierarchicalLink(False)

      self.obj346.GGLabel.setValue(13)
      self.obj346.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(167.0,195.0,self.obj346)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj346.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj346)
      self.obj346.postAction( self.LHS.CREATE )

      self.obj347=GenericGraphEdge(parent)
      self.obj347.preAction( self.LHS.CREATE )
      self.obj347.isGraphObjectVisual = True

      if(hasattr(self.obj347, '_setHierarchicalLink')):
        self.obj347._setHierarchicalLink(False)

      self.obj347.GGLabel.setValue(10)
      self.obj347.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(288.198598131,95.0,self.obj347)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj347.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj347)
      self.obj347.postAction( self.LHS.CREATE )

      self.obj348=GenericGraphEdge(parent)
      self.obj348.preAction( self.LHS.CREATE )
      self.obj348.isGraphObjectVisual = True

      if(hasattr(self.obj348, '_setHierarchicalLink')):
        self.obj348._setHierarchicalLink(False)

      self.obj348.GGLabel.setValue(15)
      self.obj348.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(170.5,76.0,self.obj348)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj348.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj348)
      self.obj348.postAction( self.LHS.CREATE )

      self.obj337.out_connections_.append(self.obj339)
      self.obj339.in_connections_.append(self.obj337)
      self.obj337.graphObject_.pendingConnections.append((self.obj337.graphObject_.tag, self.obj339.graphObject_.tag, [65.0, 82.0, 74.5, 111.5], 0, True))
      self.obj337.out_connections_.append(self.obj347)
      self.obj347.in_connections_.append(self.obj337)
      self.obj337.graphObject_.pendingConnections.append((self.obj337.graphObject_.tag, self.obj347.graphObject_.tag, [77.0, 82.0, 216.5, 96.5, 288.1985981308411, 95.0], 2, True))
      self.obj337.out_connections_.append(self.obj348)
      self.obj348.in_connections_.append(self.obj337)
      self.obj337.graphObject_.pendingConnections.append((self.obj337.graphObject_.tag, self.obj348.graphObject_.tag, [77.0, 82.0, 170.5, 76.0], 0, True))
      self.obj338.out_connections_.append(self.obj346)
      self.obj346.in_connections_.append(self.obj338)
      self.obj338.graphObject_.pendingConnections.append((self.obj338.graphObject_.tag, self.obj346.graphObject_.tag, [84.0, 186.0, 167.0, 195.0], 0, True))
      self.obj339.out_connections_.append(self.obj338)
      self.obj338.in_connections_.append(self.obj339)
      self.obj339.graphObject_.pendingConnections.append((self.obj339.graphObject_.tag, self.obj338.graphObject_.tag, [91.0, 140.0, 74.5, 111.5], 2, 0))
      self.obj340.out_connections_.append(self.obj345)
      self.obj345.in_connections_.append(self.obj340)
      self.obj340.graphObject_.pendingConnections.append((self.obj340.graphObject_.tag, self.obj345.graphObject_.tag, [264.0, 73.0, 299.5, 33.5, 329.0817757009346, 37.118421052631575], 2, True))
      self.obj343.out_connections_.append(self.obj344)
      self.obj344.in_connections_.append(self.obj343)
      self.obj343.graphObject_.pendingConnections.append((self.obj343.graphObject_.tag, self.obj344.graphObject_.tag, [281.0, 167.0, 372.0, 226.0, 328.0, 153.0], 2, True))
      self.obj344.out_connections_.append(self.obj341)
      self.obj341.in_connections_.append(self.obj344)
      self.obj344.graphObject_.pendingConnections.append((self.obj344.graphObject_.tag, self.obj341.graphObject_.tag, [333.5700934579439, 248.42105263157896, 296.0, 124.0, 328.0, 153.0], 2, True))
      self.obj345.out_connections_.append(self.obj342)
      self.obj342.in_connections_.append(self.obj345)
      self.obj345.graphObject_.pendingConnections.append((self.obj345.graphObject_.tag, self.obj342.graphObject_.tag, [362.32710280373834, 107.47368421052629, 358.6635514018692, 40.73684210526314, 329.0817757009346, 37.118421052631575], 2, True))
      self.obj346.out_connections_.append(self.obj343)
      self.obj343.in_connections_.append(self.obj346)
      self.obj346.graphObject_.pendingConnections.append((self.obj346.graphObject_.tag, self.obj343.graphObject_.tag, [250.0, 204.0, 167.0, 195.0], 2, 0))
      self.obj347.out_connections_.append(self.obj342)
      self.obj342.in_connections_.append(self.obj347)
      self.obj347.graphObject_.pendingConnections.append((self.obj347.graphObject_.tag, self.obj342.graphObject_.tag, [335.1869158878505, 115.5263157894737, 288.198598131, 95.0], 2, 0))
      self.obj348.out_connections_.append(self.obj340)
      self.obj340.in_connections_.append(self.obj348)
      self.obj348.graphObject_.pendingConnections.append((self.obj348.graphObject_.tag, self.obj340.graphObject_.tag, [264.0, 70.0, 170.5, 76.0], 2, 0))

      self.RHS = ASG_omacss(parent)
      self.RHS.merge(ASG_pns2(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj352=Agent(parent)
      self.obj352.preAction( self.RHS.CREATE )
      self.obj352.isGraphObjectVisual = True

      if(hasattr(self.obj352, '_setHierarchicalLink')):
        self.obj352._setHierarchicalLink(False)

      # price
      self.obj352.price.setValue(0)

      # name
      self.obj352.name.setValue('')
      self.obj352.name.setNone()

      self.obj352.GGLabel.setValue(1)
      self.obj352.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(60.0,20.0,self.obj352)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj352.graphObject_ = new_obj
      self.obj3520= AttrCalc()
      self.obj3520.Copy=ATOM3Boolean()
      self.obj3520.Copy.setValue(('Copy from LHS', 1))
      self.obj3520.Copy.config = 0
      self.obj3520.Specify=ATOM3Constraint()
      self.obj3520.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj352.GGset2Any['price']= self.obj3520
      self.obj3521= AttrCalc()
      self.obj3521.Copy=ATOM3Boolean()
      self.obj3521.Copy.setValue(('Copy from LHS', 1))
      self.obj3521.Copy.config = 0
      self.obj3521.Specify=ATOM3Constraint()
      self.obj3521.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj352.GGset2Any['name']= self.obj3521

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj352)
      self.obj352.postAction( self.RHS.CREATE )

      self.obj353=Role(parent)
      self.obj353.preAction( self.RHS.CREATE )
      self.obj353.isGraphObjectVisual = True

      if(hasattr(self.obj353, '_setHierarchicalLink')):
        self.obj353._setHierarchicalLink(False)

      # name
      self.obj353.name.setValue('')
      self.obj353.name.setNone()

      self.obj353.GGLabel.setValue(2)
      self.obj353.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(80.0,160.0,self.obj353)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj353.graphObject_ = new_obj
      self.obj3530= AttrCalc()
      self.obj3530.Copy=ATOM3Boolean()
      self.obj3530.Copy.setValue(('Copy from LHS', 1))
      self.obj3530.Copy.config = 0
      self.obj3530.Specify=ATOM3Constraint()
      self.obj3530.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj353.GGset2Any['name']= self.obj3530

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj353)
      self.obj353.postAction( self.RHS.CREATE )

      self.obj354=CapableOf(parent)
      self.obj354.preAction( self.RHS.CREATE )
      self.obj354.isGraphObjectVisual = True

      if(hasattr(self.obj354, '_setHierarchicalLink')):
        self.obj354._setHierarchicalLink(False)

      self.obj354.GGLabel.setValue(3)
      self.obj354.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(104.5,111.5,self.obj354)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj354.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj354)
      self.obj354.postAction( self.RHS.CREATE )

      self.obj355=rawMaterial(parent)
      self.obj355.preAction( self.RHS.CREATE )
      self.obj355.isGraphObjectVisual = True

      if(hasattr(self.obj355, '_setHierarchicalLink')):
        self.obj355._setHierarchicalLink(False)

      # Name
      self.obj355.Name.setValue('')
      self.obj355.Name.setNone()

      self.obj355.GGLabel.setValue(6)
      self.obj355.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(300.0,20.0,self.obj355)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj355.graphObject_ = new_obj
      self.obj3550= AttrCalc()
      self.obj3550.Copy=ATOM3Boolean()
      self.obj3550.Copy.setValue(('Copy from LHS', 1))
      self.obj3550.Copy.config = 0
      self.obj3550.Specify=ATOM3Constraint()
      self.obj3550.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj355.GGset2Any['Name']= self.obj3550

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj355)
      self.obj355.postAction( self.RHS.CREATE )

      self.obj356=operatingUnit(parent)
      self.obj356.preAction( self.RHS.CREATE )
      self.obj356.isGraphObjectVisual = True

      if(hasattr(self.obj356, '_setHierarchicalLink')):
        self.obj356._setHierarchicalLink(False)

      # name
      self.obj356.name.setValue('')
      self.obj356.name.setNone()

      self.obj356.GGLabel.setValue(7)
      self.obj356.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(300.0,100.0,self.obj356)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj356.graphObject_ = new_obj
      self.obj3560= AttrCalc()
      self.obj3560.Copy=ATOM3Boolean()
      self.obj3560.Copy.setValue(('Copy from LHS', 1))
      self.obj3560.Copy.config = 0
      self.obj3560.Specify=ATOM3Constraint()
      self.obj3560.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj356.GGset2Any['name']= self.obj3560

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj356)
      self.obj356.postAction( self.RHS.CREATE )

      self.obj357=operatingUnit(parent)
      self.obj357.preAction( self.RHS.CREATE )
      self.obj357.isGraphObjectVisual = True

      if(hasattr(self.obj357, '_setHierarchicalLink')):
        self.obj357._setHierarchicalLink(False)

      # name
      self.obj357.name.setValue('')
      self.obj357.name.setNone()

      self.obj357.GGLabel.setValue(12)
      self.obj357.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(240.0,260.0,self.obj357)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj357.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj357)
      self.obj357.postAction( self.RHS.CREATE )

      self.obj358=metarial(parent)
      self.obj358.preAction( self.RHS.CREATE )
      self.obj358.isGraphObjectVisual = True

      if(hasattr(self.obj358, '_setHierarchicalLink')):
        self.obj358._setHierarchicalLink(False)

      # Name
      self.obj358.Name.setValue('')
      self.obj358.Name.setNone()

      self.obj358.GGLabel.setValue(11)
      self.obj358.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(320.0,160.0,self.obj358)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj358.graphObject_ = new_obj
      self.obj3580= AttrCalc()
      self.obj3580.Copy=ATOM3Boolean()
      self.obj3580.Copy.setValue(('Copy from LHS', 1))
      self.obj3580.Copy.config = 0
      self.obj3580.Specify=ATOM3Constraint()
      self.obj3580.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj358.GGset2Any['Name']= self.obj3580

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj358)
      self.obj358.postAction( self.RHS.CREATE )

      self.obj359=fromMaterial(parent)
      self.obj359.preAction( self.RHS.CREATE )
      self.obj359.isGraphObjectVisual = True

      if(hasattr(self.obj359, '_setHierarchicalLink')):
        self.obj359._setHierarchicalLink(False)

      # rate
      self.obj359.rate.setValue(0.0)

      self.obj359.GGLabel.setValue(14)
      self.obj359.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(317.285046729,218.710526316,self.obj359)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj359.graphObject_ = new_obj
      self.obj3590= AttrCalc()
      self.obj3590.Copy=ATOM3Boolean()
      self.obj3590.Copy.setValue(('Copy from LHS', 1))
      self.obj3590.Copy.config = 0
      self.obj3590.Specify=ATOM3Constraint()
      self.obj3590.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj359.GGset2Any['rate']= self.obj3590

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj359)
      self.obj359.postAction( self.RHS.CREATE )

      self.obj360=fromRaw(parent)
      self.obj360.preAction( self.RHS.CREATE )
      self.obj360.isGraphObjectVisual = True

      if(hasattr(self.obj360, '_setHierarchicalLink')):
        self.obj360._setHierarchicalLink(False)

      # rate
      self.obj360.rate.setValue(0.0)

      self.obj360.GGLabel.setValue(9)
      self.obj360.graphClass_= graph_fromRaw
      if parent.genGraphics:
         new_obj = graph_fromRaw(318.285046729,90.7105263158,self.obj360)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj360.graphObject_ = new_obj
      self.obj3600= AttrCalc()
      self.obj3600.Copy=ATOM3Boolean()
      self.obj3600.Copy.setValue(('Copy from LHS', 1))
      self.obj3600.Copy.config = 0
      self.obj3600.Specify=ATOM3Constraint()
      self.obj3600.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj360.GGset2Any['rate']= self.obj3600

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj360)
      self.obj360.postAction( self.RHS.CREATE )

      self.obj361=intoMaterial(parent)
      self.obj361.preAction( self.RHS.CREATE )
      self.obj361.isGraphObjectVisual = True

      if(hasattr(self.obj361, '_setHierarchicalLink')):
        self.obj361._setHierarchicalLink(False)

      # rate
      self.obj361.rate.setValue(16.16)

      self.obj361.GGLabel.setValue(16)
      self.obj361.graphClass_= graph_intoMaterial
      if parent.genGraphics:
         new_obj = graph_intoMaterial(322.093457944,135.263157895,self.obj361)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj361.graphObject_ = new_obj
      self.obj3610= AttrCalc()
      self.obj3610.Copy=ATOM3Boolean()
      self.obj3610.Copy.setValue(('Copy from LHS', 0))
      self.obj3610.Copy.config = 0
      self.obj3610.Specify=ATOM3Constraint()
      self.obj3610.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return 16.16\n\n\n\n\n\n\n\n\n\n\n\n\n'))
      self.obj361.GGset2Any['rate']= self.obj3610

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj361)
      self.obj361.postAction( self.RHS.CREATE )

      self.obj362=GenericGraphEdge(parent)
      self.obj362.preAction( self.RHS.CREATE )
      self.obj362.isGraphObjectVisual = True

      if(hasattr(self.obj362, '_setHierarchicalLink')):
        self.obj362._setHierarchicalLink(False)

      self.obj362.GGLabel.setValue(10)
      self.obj362.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(199.285046729,85.2105263158,self.obj362)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj362.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj362)
      self.obj362.postAction( self.RHS.CREATE )

      self.obj363=GenericGraphEdge(parent)
      self.obj363.preAction( self.RHS.CREATE )
      self.obj363.isGraphObjectVisual = True

      if(hasattr(self.obj363, '_setHierarchicalLink')):
        self.obj363._setHierarchicalLink(False)

      self.obj363.GGLabel.setValue(13)
      self.obj363.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(208.0,174.0,self.obj363)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj363.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj363)
      self.obj363.postAction( self.RHS.CREATE )

      self.obj364=GenericGraphEdge(parent)
      self.obj364.preAction( self.RHS.CREATE )
      self.obj364.isGraphObjectVisual = True

      if(hasattr(self.obj364, '_setHierarchicalLink')):
        self.obj364._setHierarchicalLink(False)

      self.obj364.GGLabel.setValue(15)
      self.obj364.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(229.5,47.0,self.obj364)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj364.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj364)
      self.obj364.postAction( self.RHS.CREATE )

      self.obj352.out_connections_.append(self.obj354)
      self.obj354.in_connections_.append(self.obj352)
      self.obj352.graphObject_.pendingConnections.append((self.obj352.graphObject_.tag, self.obj354.graphObject_.tag, [85.0, 82.0, 104.5, 111.5], 0, True))
      self.obj352.out_connections_.append(self.obj362)
      self.obj362.in_connections_.append(self.obj352)
      self.obj352.graphObject_.pendingConnections.append((self.obj352.graphObject_.tag, self.obj362.graphObject_.tag, [85.0, 82.0, 199.28504672897196, 85.21052631578948], 0, True))
      self.obj352.out_connections_.append(self.obj364)
      self.obj364.in_connections_.append(self.obj352)
      self.obj352.graphObject_.pendingConnections.append((self.obj352.graphObject_.tag, self.obj364.graphObject_.tag, [97.0, 82.0, 229.5, 47.0], 0, True))
      self.obj353.out_connections_.append(self.obj363)
      self.obj363.in_connections_.append(self.obj353)
      self.obj353.graphObject_.pendingConnections.append((self.obj353.graphObject_.tag, self.obj363.graphObject_.tag, [104.0, 161.0, 208.0, 174.0], 0, True))
      self.obj354.out_connections_.append(self.obj353)
      self.obj353.in_connections_.append(self.obj354)
      self.obj354.graphObject_.pendingConnections.append((self.obj354.graphObject_.tag, self.obj353.graphObject_.tag, [111.0, 160.0, 104.5, 111.5], 2, 0))
      self.obj355.out_connections_.append(self.obj360)
      self.obj360.in_connections_.append(self.obj355)
      self.obj355.graphObject_.pendingConnections.append((self.obj355.graphObject_.tag, self.obj360.graphObject_.tag, [324.0, 73.0, 318.28504672897196, 90.71052631578948], 0, True))
      self.obj356.out_connections_.append(self.obj361)
      self.obj361.in_connections_.append(self.obj356)
      self.obj356.graphObject_.pendingConnections.append((self.obj356.graphObject_.tag, self.obj361.graphObject_.tag, [315.1869158878505, 115.5263157894737, 322.0934579439253, 135.26315789473685], 0, True))
      self.obj358.out_connections_.append(self.obj359)
      self.obj359.in_connections_.append(self.obj358)
      self.obj358.graphObject_.pendingConnections.append((self.obj358.graphObject_.tag, self.obj359.graphObject_.tag, [357.0, 205.0, 317.28504672897196, 218.71052631578948], 0, True))
      self.obj359.out_connections_.append(self.obj357)
      self.obj357.in_connections_.append(self.obj359)
      self.obj359.graphObject_.pendingConnections.append((self.obj359.graphObject_.tag, self.obj357.graphObject_.tag, [253.57009345794393, 248.42105263157896, 315.28504672897196, 206.71052631578948], 0, True))
      self.obj360.out_connections_.append(self.obj356)
      self.obj356.in_connections_.append(self.obj360)
      self.obj360.graphObject_.pendingConnections.append((self.obj360.graphObject_.tag, self.obj356.graphObject_.tag, [314.5700934579439, 108.42105263157895, 319.28504672897196, 90.71052631578948], 0, True))
      self.obj361.out_connections_.append(self.obj358)
      self.obj358.in_connections_.append(self.obj361)
      self.obj361.graphObject_.pendingConnections.append((self.obj361.graphObject_.tag, self.obj358.graphObject_.tag, [347.0, 161.0, 311.0934579439253, 128.26315789473685], 0, True))
      self.obj362.out_connections_.append(self.obj356)
      self.obj356.in_connections_.append(self.obj362)
      self.obj362.graphObject_.pendingConnections.append((self.obj362.graphObject_.tag, self.obj356.graphObject_.tag, [314.5700934579439, 108.42105263157895, 199.285046729, 85.2105263158], 2, 0))
      self.obj363.out_connections_.append(self.obj358)
      self.obj358.in_connections_.append(self.obj363)
      self.obj363.graphObject_.pendingConnections.append((self.obj363.graphObject_.tag, self.obj358.graphObject_.tag, [332.0, 165.0, 208.0, 143.0], 2, 0))
      self.obj364.out_connections_.append(self.obj355)
      self.obj355.in_connections_.append(self.obj364)
      self.obj364.graphObject_.pendingConnections.append((self.obj364.graphObject_.tag, self.obj355.graphObject_.tag, [324.0, 70.0, 210.5, 76.0], 0, True))

   def condition(self, graphID, isograph, atom3i):
      
      node7 = self.getMatched(graphID, self.LHS.nodeWithLabel(7))
      
      node11 = self.getMatched(graphID, self.LHS.nodeWithLabel(11))
      node1 = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      
      print node7.name.getValue()+' in '+ node11.Name.getValue() 
      print node7.name.getValue() in  node11.Name.getValue()
      print 'Rule 20 '
      
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
      
      

