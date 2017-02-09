# _ LinkAux1_GG_rule.py ____________________________________________________________________________
# File generated automatically by ATOM3. Graph Grammar Rule
# ___________________________________________________________________________________________
from GGrule import *
from Capabilitie import *
from rawMaterial import *
from GenericGraphEdge import *
from Goal import *
from intoProduct import *
from operatingUnit import *
from metarial import *
from GenericGraphNode import *
from product import *
from Agent import *
from fromMaterial import *
from CapableOf import *
from Role import *
from fromRaw import *
from ASG_pns2 import *
from intoMaterial import *
from ASG_GenericGraph import *
from ASG_omacs import *
from require import *
from achieve import *
from posses import *
class LinkAux1_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 10)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_pns2(parent)
      self.LHS.merge(ASG_omacs(parent))
      self.LHS.merge(ASG_GenericGraph(parent))

      self.obj133=metarial(parent)
      self.obj133.preAction( self.LHS.CREATE )
      self.obj133.isGraphObjectVisual = True

      if(hasattr(self.obj133, '_setHierarchicalLink')):
        self.obj133._setHierarchicalLink(False)

      # Name
      self.obj133.Name.setValue('')
      self.obj133.Name.setNone()

      self.obj133.GGLabel.setValue(4)
      self.obj133.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(260.0,40.0,self.obj133)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj133.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj133)
      self.obj133.postAction( self.LHS.CREATE )

      self.obj134=metarial(parent)
      self.obj134.preAction( self.LHS.CREATE )
      self.obj134.isGraphObjectVisual = True

      if(hasattr(self.obj134, '_setHierarchicalLink')):
        self.obj134._setHierarchicalLink(False)

      # Name
      self.obj134.Name.setValue('')
      self.obj134.Name.setNone()

      self.obj134.GGLabel.setValue(8)
      self.obj134.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(240.0,220.0,self.obj134)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj134.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj134)
      self.obj134.postAction( self.LHS.CREATE )

      self.obj135=operatingUnit(parent)
      self.obj135.preAction( self.LHS.CREATE )
      self.obj135.isGraphObjectVisual = True

      if(hasattr(self.obj135, '_setHierarchicalLink')):
        self.obj135._setHierarchicalLink(False)

      self.obj135.GGLabel.setValue(5)
      self.obj135.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(260.0,120.0,self.obj135)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj135.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj135)
      self.obj135.postAction( self.LHS.CREATE )

      self.obj136=fromMaterial(parent)
      self.obj136.preAction( self.LHS.CREATE )
      self.obj136.isGraphObjectVisual = True

      if(hasattr(self.obj136, '_setHierarchicalLink')):
        self.obj136._setHierarchicalLink(False)

      # rate
      self.obj136.rate.setValue(0.0)

      self.obj136.GGLabel.setValue(6)
      self.obj136.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(283.0,106.5,self.obj136)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj136.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj136)
      self.obj136.postAction( self.LHS.CREATE )

      self.obj137=Goal(parent)
      self.obj137.preAction( self.LHS.CREATE )
      self.obj137.isGraphObjectVisual = True

      if(hasattr(self.obj137, '_setHierarchicalLink')):
        self.obj137._setHierarchicalLink(False)

      # name
      self.obj137.name.setValue('')
      self.obj137.name.setNone()

      self.obj137.GGLabel.setValue(2)
      self.obj137.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(80.0,200.0,self.obj137)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj137.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj137)
      self.obj137.postAction( self.LHS.CREATE )

      self.obj138=Role(parent)
      self.obj138.preAction( self.LHS.CREATE )
      self.obj138.isGraphObjectVisual = True

      if(hasattr(self.obj138, '_setHierarchicalLink')):
        self.obj138._setHierarchicalLink(False)

      # name
      self.obj138.name.setValue('')
      self.obj138.name.setNone()

      self.obj138.GGLabel.setValue(1)
      self.obj138.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(80.0,40.0,self.obj138)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj138.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj138)
      self.obj138.postAction( self.LHS.CREATE )

      self.obj139=achieve(parent)
      self.obj139.preAction( self.LHS.CREATE )
      self.obj139.isGraphObjectVisual = True

      if(hasattr(self.obj139, '_setHierarchicalLink')):
        self.obj139._setHierarchicalLink(False)

      self.obj139.GGLabel.setValue(3)
      self.obj139.graphClass_= graph_achieve
      if parent.genGraphics:
         new_obj = graph_achieve(112.0,155.5,self.obj139)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj139.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj139)
      self.obj139.postAction( self.LHS.CREATE )

      self.obj140=GenericGraphEdge(parent)
      self.obj140.preAction( self.LHS.CREATE )
      self.obj140.isGraphObjectVisual = True

      if(hasattr(self.obj140, '_setHierarchicalLink')):
        self.obj140._setHierarchicalLink(False)

      self.obj140.GGLabel.setValue(7)
      self.obj140.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(201.0,126.75,self.obj140)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj140.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj140)
      self.obj140.postAction( self.LHS.CREATE )

      self.obj141=GenericGraphEdge(parent)
      self.obj141.preAction( self.LHS.CREATE )
      self.obj141.isGraphObjectVisual = True

      if(hasattr(self.obj141, '_setHierarchicalLink')):
        self.obj141._setHierarchicalLink(False)

      self.obj141.GGLabel.setValue(9)
      self.obj141.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(181.5,267.0,self.obj141)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj141.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj141)
      self.obj141.postAction( self.LHS.CREATE )

      self.obj133.out_connections_.append(self.obj136)
      self.obj136.in_connections_.append(self.obj133)
      self.obj133.graphObject_.pendingConnections.append((self.obj133.graphObject_.tag, self.obj136.graphObject_.tag, [284.0, 90.0, 283.0, 106.5], 0, True))
      self.obj136.out_connections_.append(self.obj135)
      self.obj135.in_connections_.append(self.obj136)
      self.obj136.graphObject_.pendingConnections.append((self.obj136.graphObject_.tag, self.obj135.graphObject_.tag, [282.0, 123.0, 283.0, 106.5], 0, True))
      self.obj137.out_connections_.append(self.obj141)
      self.obj141.in_connections_.append(self.obj137)
      self.obj137.graphObject_.pendingConnections.append((self.obj137.graphObject_.tag, self.obj141.graphObject_.tag, [113.0, 270.0, 181.5, 267.0], 0, True))
      self.obj138.out_connections_.append(self.obj139)
      self.obj139.in_connections_.append(self.obj138)
      self.obj138.graphObject_.pendingConnections.append((self.obj138.graphObject_.tag, self.obj139.graphObject_.tag, [112.0, 110.0, 112.0, 155.5], 0, True))
      self.obj138.out_connections_.append(self.obj140)
      self.obj140.in_connections_.append(self.obj138)
      self.obj138.graphObject_.pendingConnections.append((self.obj138.graphObject_.tag, self.obj140.graphObject_.tag, [112.0, 110.0, 188.5, 154.5, 158.0, 152.0, 201.0, 126.75], 4, True))
      self.obj139.out_connections_.append(self.obj137)
      self.obj137.in_connections_.append(self.obj139)
      self.obj139.graphObject_.pendingConnections.append((self.obj139.graphObject_.tag, self.obj137.graphObject_.tag, [112.0, 201.0, 112.0, 155.5], 0, True))
      self.obj140.out_connections_.append(self.obj133)
      self.obj133.in_connections_.append(self.obj140)
      self.obj140.graphObject_.pendingConnections.append((self.obj140.graphObject_.tag, self.obj133.graphObject_.tag, [272.0, 45.0, 213.5, 99.0, 208.0, 41.0, 201.0, 126.75], 4, True))
      self.obj141.out_connections_.append(self.obj134)
      self.obj134.in_connections_.append(self.obj141)
      self.obj141.graphObject_.pendingConnections.append((self.obj141.graphObject_.tag, self.obj134.graphObject_.tag, [250.0, 264.0, 181.5, 267.0], 0, True))

      self.RHS = ASG_pns2(parent)
      self.RHS.merge(ASG_omacs(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj145=metarial(parent)
      self.obj145.preAction( self.RHS.CREATE )
      self.obj145.isGraphObjectVisual = True

      if(hasattr(self.obj145, '_setHierarchicalLink')):
        self.obj145._setHierarchicalLink(False)

      # Name
      self.obj145.Name.setValue('')
      self.obj145.Name.setNone()

      self.obj145.GGLabel.setValue(4)
      self.obj145.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(280.0,40.0,self.obj145)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj145.graphObject_ = new_obj
      self.obj1450= AttrCalc()
      self.obj1450.Copy=ATOM3Boolean()
      self.obj1450.Copy.setValue(('Copy from LHS', 1))
      self.obj1450.Copy.config = 0
      self.obj1450.Specify=ATOM3Constraint()
      self.obj1450.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj145.GGset2Any['Name']= self.obj1450

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj145)
      self.obj145.postAction( self.RHS.CREATE )

      self.obj146=metarial(parent)
      self.obj146.preAction( self.RHS.CREATE )
      self.obj146.isGraphObjectVisual = True

      if(hasattr(self.obj146, '_setHierarchicalLink')):
        self.obj146._setHierarchicalLink(False)

      # Name
      self.obj146.Name.setValue('')
      self.obj146.Name.setNone()

      self.obj146.GGLabel.setValue(8)
      self.obj146.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(260.0,240.0,self.obj146)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj146.graphObject_ = new_obj
      self.obj1460= AttrCalc()
      self.obj1460.Copy=ATOM3Boolean()
      self.obj1460.Copy.setValue(('Copy from LHS', 1))
      self.obj1460.Copy.config = 0
      self.obj1460.Specify=ATOM3Constraint()
      self.obj1460.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj146.GGset2Any['Name']= self.obj1460

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj146)
      self.obj146.postAction( self.RHS.CREATE )

      self.obj147=operatingUnit(parent)
      self.obj147.preAction( self.RHS.CREATE )
      self.obj147.isGraphObjectVisual = True

      if(hasattr(self.obj147, '_setHierarchicalLink')):
        self.obj147._setHierarchicalLink(False)

      self.obj147.GGLabel.setValue(5)
      self.obj147.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(260.0,140.0,self.obj147)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj147.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj147)
      self.obj147.postAction( self.RHS.CREATE )

      self.obj148=intoMaterial(parent)
      self.obj148.preAction( self.RHS.CREATE )
      self.obj148.isGraphObjectVisual = True

      if(hasattr(self.obj148, '_setHierarchicalLink')):
        self.obj148._setHierarchicalLink(False)

      # rate
      self.obj148.rate.setValue(0.0)

      self.obj148.GGLabel.setValue(10)
      self.obj148.graphClass_= graph_intoMaterial
      if parent.genGraphics:
         new_obj = graph_intoMaterial(285.0,199.5,self.obj148)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj148.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj148)
      self.obj148.postAction( self.RHS.CREATE )

      self.obj149=fromMaterial(parent)
      self.obj149.preAction( self.RHS.CREATE )
      self.obj149.isGraphObjectVisual = True

      if(hasattr(self.obj149, '_setHierarchicalLink')):
        self.obj149._setHierarchicalLink(False)

      # rate
      self.obj149.rate.setValue(0.0)

      self.obj149.GGLabel.setValue(6)
      self.obj149.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(315.5,115.5,self.obj149)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj149.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj149)
      self.obj149.postAction( self.RHS.CREATE )

      self.obj150=Goal(parent)
      self.obj150.preAction( self.RHS.CREATE )
      self.obj150.isGraphObjectVisual = True

      if(hasattr(self.obj150, '_setHierarchicalLink')):
        self.obj150._setHierarchicalLink(False)

      # name
      self.obj150.name.setValue('')
      self.obj150.name.setNone()

      self.obj150.GGLabel.setValue(2)
      self.obj150.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(60.0,220.0,self.obj150)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj150.graphObject_ = new_obj
      self.obj1500= AttrCalc()
      self.obj1500.Copy=ATOM3Boolean()
      self.obj1500.Copy.setValue(('Copy from LHS', 1))
      self.obj1500.Copy.config = 0
      self.obj1500.Specify=ATOM3Constraint()
      self.obj1500.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj150.GGset2Any['name']= self.obj1500

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj150)
      self.obj150.postAction( self.RHS.CREATE )

      self.obj151=Role(parent)
      self.obj151.preAction( self.RHS.CREATE )
      self.obj151.isGraphObjectVisual = True

      if(hasattr(self.obj151, '_setHierarchicalLink')):
        self.obj151._setHierarchicalLink(False)

      # name
      self.obj151.name.setValue('')
      self.obj151.name.setNone()

      self.obj151.GGLabel.setValue(1)
      self.obj151.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(60.0,40.0,self.obj151)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj151.graphObject_ = new_obj
      self.obj1510= AttrCalc()
      self.obj1510.Copy=ATOM3Boolean()
      self.obj1510.Copy.setValue(('Copy from LHS', 1))
      self.obj1510.Copy.config = 0
      self.obj1510.Specify=ATOM3Constraint()
      self.obj1510.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj151.GGset2Any['name']= self.obj1510

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj151)
      self.obj151.postAction( self.RHS.CREATE )

      self.obj152=achieve(parent)
      self.obj152.preAction( self.RHS.CREATE )
      self.obj152.isGraphObjectVisual = True

      if(hasattr(self.obj152, '_setHierarchicalLink')):
        self.obj152._setHierarchicalLink(False)

      self.obj152.GGLabel.setValue(3)
      self.obj152.graphClass_= graph_achieve
      if parent.genGraphics:
         new_obj = graph_achieve(92.0,165.5,self.obj152)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj152.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj152)
      self.obj152.postAction( self.RHS.CREATE )

      self.obj153=GenericGraphEdge(parent)
      self.obj153.preAction( self.RHS.CREATE )
      self.obj153.isGraphObjectVisual = True

      if(hasattr(self.obj153, '_setHierarchicalLink')):
        self.obj153._setHierarchicalLink(False)

      self.obj153.GGLabel.setValue(7)
      self.obj153.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(179.5,82.0,self.obj153)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj153.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj153)
      self.obj153.postAction( self.RHS.CREATE )

      self.obj154=GenericGraphEdge(parent)
      self.obj154.preAction( self.RHS.CREATE )
      self.obj154.isGraphObjectVisual = True

      if(hasattr(self.obj154, '_setHierarchicalLink')):
        self.obj154._setHierarchicalLink(False)

      self.obj154.GGLabel.setValue(9)
      self.obj154.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(181.5,287.0,self.obj154)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj154.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj154)
      self.obj154.postAction( self.RHS.CREATE )

      self.obj145.out_connections_.append(self.obj149)
      self.obj149.in_connections_.append(self.obj145)
      self.obj145.graphObject_.pendingConnections.append((self.obj145.graphObject_.tag, self.obj149.graphObject_.tag, [304.0, 90.0, 315.5, 115.5], 0, True))
      self.obj147.out_connections_.append(self.obj148)
      self.obj148.in_connections_.append(self.obj147)
      self.obj147.graphObject_.pendingConnections.append((self.obj147.graphObject_.tag, self.obj148.graphObject_.tag, [283.0, 158.0, 285.0, 199.5], 0, True))
      self.obj148.out_connections_.append(self.obj146)
      self.obj146.in_connections_.append(self.obj148)
      self.obj148.graphObject_.pendingConnections.append((self.obj148.graphObject_.tag, self.obj146.graphObject_.tag, [287.0, 241.0, 285.0, 199.5], 0, True))
      self.obj149.out_connections_.append(self.obj147)
      self.obj147.in_connections_.append(self.obj149)
      self.obj149.graphObject_.pendingConnections.append((self.obj149.graphObject_.tag, self.obj147.graphObject_.tag, [327.0, 141.0, 315.5, 115.5], 0, True))
      self.obj150.out_connections_.append(self.obj154)
      self.obj154.in_connections_.append(self.obj150)
      self.obj150.graphObject_.pendingConnections.append((self.obj150.graphObject_.tag, self.obj154.graphObject_.tag, [93.0, 290.0, 181.5, 287.0], 0, True))
      self.obj151.out_connections_.append(self.obj152)
      self.obj152.in_connections_.append(self.obj151)
      self.obj151.graphObject_.pendingConnections.append((self.obj151.graphObject_.tag, self.obj152.graphObject_.tag, [92.0, 110.0, 92.0, 165.5], 0, True))
      self.obj151.out_connections_.append(self.obj153)
      self.obj153.in_connections_.append(self.obj151)
      self.obj151.graphObject_.pendingConnections.append((self.obj151.graphObject_.tag, self.obj153.graphObject_.tag, [92.0, 110.0, 137.0, 139.0, 179.5, 82.0], 2, True))
      self.obj152.out_connections_.append(self.obj150)
      self.obj150.in_connections_.append(self.obj152)
      self.obj152.graphObject_.pendingConnections.append((self.obj152.graphObject_.tag, self.obj150.graphObject_.tag, [92.0, 221.0, 92.0, 165.5], 0, True))
      self.obj153.out_connections_.append(self.obj145)
      self.obj145.in_connections_.append(self.obj153)
      self.obj153.graphObject_.pendingConnections.append((self.obj153.graphObject_.tag, self.obj145.graphObject_.tag, [292.0, 45.0, 222.0, 25.0, 179.5, 82.0], 2, True))
      self.obj154.out_connections_.append(self.obj146)
      self.obj146.in_connections_.append(self.obj154)
      self.obj154.graphObject_.pendingConnections.append((self.obj154.graphObject_.tag, self.obj146.graphObject_.tag, [270.0, 284.0, 181.5, 287.0], 0, True))

   def condition(self, graphID, isograph, atom3i):
      print '======> Link Aux Condition'
      aRg = self.getMatched ( graphID , self.LHS.nodeWithLabel(4) )
      nameARG = aRg.Name.getValue()
      g = self.getMatched ( graphID , self.LHS.nodeWithLabel(8) )
      # test if nameARG  end with name of Goal 
      if nameARG.endswith( g.Name.getValue() ) and not hasattr(aRg,'LinkAux'): 
      	return True
      else : 
      	return False
      
      

   def action(self, graphID, isograph, atom3i):
      print '======> Link Aux Action'
      aRg = self.getMatched ( graphID , self.LHS.nodeWithLabel(4) )
      aRg.LinkAux = True 
      
      

