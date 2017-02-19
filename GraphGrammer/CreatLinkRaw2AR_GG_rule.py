# _ CreatLinkRaw2AR_GG_rule.py ____________________________________________________________________________
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
class CreatLinkRaw2AR_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 11)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_omacss(parent)
      self.LHS.merge(ASG_pns2(parent))
      self.LHS.merge(ASG_GenericGraph(parent))

      self.obj241=Agent(parent)
      self.obj241.preAction( self.LHS.CREATE )
      self.obj241.isGraphObjectVisual = True

      if(hasattr(self.obj241, '_setHierarchicalLink')):
        self.obj241._setHierarchicalLink(False)

      # price
      self.obj241.price.setValue(0)

      # name
      self.obj241.name.setValue('')
      self.obj241.name.setNone()

      self.obj241.GGLabel.setValue(1)
      self.obj241.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(100.0,40.0,self.obj241)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj241.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj241)
      self.obj241.postAction( self.LHS.CREATE )

      self.obj242=rawMaterial(parent)
      self.obj242.preAction( self.LHS.CREATE )
      self.obj242.isGraphObjectVisual = True

      if(hasattr(self.obj242, '_setHierarchicalLink')):
        self.obj242._setHierarchicalLink(False)

      # Name
      self.obj242.Name.setValue('')
      self.obj242.Name.setNone()

      self.obj242.GGLabel.setValue(3)
      self.obj242.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(280.0,20.0,self.obj242)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj242.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj242)
      self.obj242.postAction( self.LHS.CREATE )

      self.obj243=operatingUnit(parent)
      self.obj243.preAction( self.LHS.CREATE )
      self.obj243.isGraphObjectVisual = True

      if(hasattr(self.obj243, '_setHierarchicalLink')):
        self.obj243._setHierarchicalLink(False)

      # name
      self.obj243.name.setValue('')
      self.obj243.name.setNone()

      self.obj243.GGLabel.setValue(2)
      self.obj243.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(260.0,160.0,self.obj243)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj243.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj243)
      self.obj243.postAction( self.LHS.CREATE )

      self.obj244=GenericGraphEdge(parent)
      self.obj244.preAction( self.LHS.CREATE )
      self.obj244.isGraphObjectVisual = True

      if(hasattr(self.obj244, '_setHierarchicalLink')):
        self.obj244._setHierarchicalLink(False)

      self.obj244.GGLabel.setValue(4)
      self.obj244.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(214.75,92.75,self.obj244)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj244.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj244)
      self.obj244.postAction( self.LHS.CREATE )

      self.obj245=GenericGraphEdge(parent)
      self.obj245.preAction( self.LHS.CREATE )
      self.obj245.isGraphObjectVisual = True

      if(hasattr(self.obj245, '_setHierarchicalLink')):
        self.obj245._setHierarchicalLink(False)

      self.obj245.GGLabel.setValue(5)
      self.obj245.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(241.642523364,131.105263158,self.obj245)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj245.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj245)
      self.obj245.postAction( self.LHS.CREATE )

      self.obj241.out_connections_.append(self.obj244)
      self.obj244.in_connections_.append(self.obj241)
      self.obj241.graphObject_.pendingConnections.append((self.obj241.graphObject_.tag, self.obj244.graphObject_.tag, [125.0, 102.0, 170.0, 100.0, 214.75, 92.75], 2, True))
      self.obj241.out_connections_.append(self.obj245)
      self.obj245.in_connections_.append(self.obj241)
      self.obj241.graphObject_.pendingConnections.append((self.obj241.graphObject_.tag, self.obj245.graphObject_.tag, [125.0, 102.0, 204.5, 114.5, 241.64252336448598, 131.10526315789474], 2, True))
      self.obj244.out_connections_.append(self.obj242)
      self.obj242.in_connections_.append(self.obj244)
      self.obj244.graphObject_.pendingConnections.append((self.obj244.graphObject_.tag, self.obj242.graphObject_.tag, [304.0, 73.0, 259.5, 85.5, 214.75, 92.75], 2, True))
      self.obj245.out_connections_.append(self.obj243)
      self.obj243.in_connections_.append(self.obj245)
      self.obj245.graphObject_.pendingConnections.append((self.obj245.graphObject_.tag, self.obj243.graphObject_.tag, [273.5700934579439, 168.42105263157896, 278.78504672897196, 147.71052631578948, 241.64252336448598, 131.10526315789474], 2, True))

      self.RHS = ASG_omacss(parent)
      self.RHS.merge(ASG_pns2(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj249=Agent(parent)
      self.obj249.preAction( self.RHS.CREATE )
      self.obj249.isGraphObjectVisual = True

      if(hasattr(self.obj249, '_setHierarchicalLink')):
        self.obj249._setHierarchicalLink(False)

      # price
      self.obj249.price.setValue(0)

      # name
      self.obj249.name.setValue('')
      self.obj249.name.setNone()

      self.obj249.GGLabel.setValue(1)
      self.obj249.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(60.0,60.0,self.obj249)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj249.graphObject_ = new_obj
      self.obj2490= AttrCalc()
      self.obj2490.Copy=ATOM3Boolean()
      self.obj2490.Copy.setValue(('Copy from LHS', 1))
      self.obj2490.Copy.config = 0
      self.obj2490.Specify=ATOM3Constraint()
      self.obj2490.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj249.GGset2Any['price']= self.obj2490
      self.obj2491= AttrCalc()
      self.obj2491.Copy=ATOM3Boolean()
      self.obj2491.Copy.setValue(('Copy from LHS', 1))
      self.obj2491.Copy.config = 0
      self.obj2491.Specify=ATOM3Constraint()
      self.obj2491.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj249.GGset2Any['name']= self.obj2491

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj249)
      self.obj249.postAction( self.RHS.CREATE )

      self.obj250=rawMaterial(parent)
      self.obj250.preAction( self.RHS.CREATE )
      self.obj250.isGraphObjectVisual = True

      if(hasattr(self.obj250, '_setHierarchicalLink')):
        self.obj250._setHierarchicalLink(False)

      # Name
      self.obj250.Name.setValue('')
      self.obj250.Name.setNone()

      self.obj250.GGLabel.setValue(3)
      self.obj250.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(240.0,20.0,self.obj250)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj250.graphObject_ = new_obj
      self.obj2500= AttrCalc()
      self.obj2500.Copy=ATOM3Boolean()
      self.obj2500.Copy.setValue(('Copy from LHS', 1))
      self.obj2500.Copy.config = 0
      self.obj2500.Specify=ATOM3Constraint()
      self.obj2500.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj250.GGset2Any['Name']= self.obj2500

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj250)
      self.obj250.postAction( self.RHS.CREATE )

      self.obj251=operatingUnit(parent)
      self.obj251.preAction( self.RHS.CREATE )
      self.obj251.isGraphObjectVisual = True

      if(hasattr(self.obj251, '_setHierarchicalLink')):
        self.obj251._setHierarchicalLink(False)

      # name
      self.obj251.name.setValue('')
      self.obj251.name.setNone()

      self.obj251.GGLabel.setValue(2)
      self.obj251.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(260.0,160.0,self.obj251)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj251.graphObject_ = new_obj
      self.obj2510= AttrCalc()
      self.obj2510.Copy=ATOM3Boolean()
      self.obj2510.Copy.setValue(('Copy from LHS', 1))
      self.obj2510.Copy.config = 0
      self.obj2510.Specify=ATOM3Constraint()
      self.obj2510.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj251.GGset2Any['name']= self.obj2510

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj251)
      self.obj251.postAction( self.RHS.CREATE )

      self.obj252=fromRaw(parent)
      self.obj252.preAction( self.RHS.CREATE )
      self.obj252.isGraphObjectVisual = True

      if(hasattr(self.obj252, '_setHierarchicalLink')):
        self.obj252._setHierarchicalLink(False)

      # rate
      self.obj252.rate.setValue(1.0)

      self.obj252.GGLabel.setValue(6)
      self.obj252.graphClass_= graph_fromRaw
      if parent.genGraphics:
         new_obj = graph_fromRaw(268.785046729,120.710526316,self.obj252)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj252.graphObject_ = new_obj
      self.obj2520= AttrCalc()
      self.obj2520.Copy=ATOM3Boolean()
      self.obj2520.Copy.setValue(('Copy from LHS', 0))
      self.obj2520.Copy.config = 0
      self.obj2520.Specify=ATOM3Constraint()
      self.obj2520.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj252.GGset2Any['rate']= self.obj2520

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj252)
      self.obj252.postAction( self.RHS.CREATE )

      self.obj253=GenericGraphEdge(parent)
      self.obj253.preAction( self.RHS.CREATE )
      self.obj253.isGraphObjectVisual = True

      if(hasattr(self.obj253, '_setHierarchicalLink')):
        self.obj253._setHierarchicalLink(False)

      self.obj253.GGLabel.setValue(4)
      self.obj253.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(174.5,97.5,self.obj253)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj253.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj253)
      self.obj253.postAction( self.RHS.CREATE )

      self.obj254=GenericGraphEdge(parent)
      self.obj254.preAction( self.RHS.CREATE )
      self.obj254.isGraphObjectVisual = True

      if(hasattr(self.obj254, '_setHierarchicalLink')):
        self.obj254._setHierarchicalLink(False)

      self.obj254.GGLabel.setValue(5)
      self.obj254.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(179.285046729,145.210526316,self.obj254)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj254.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj254)
      self.obj254.postAction( self.RHS.CREATE )

      self.obj249.out_connections_.append(self.obj253)
      self.obj253.in_connections_.append(self.obj249)
      self.obj249.graphObject_.pendingConnections.append((self.obj249.graphObject_.tag, self.obj253.graphObject_.tag, [85.0, 122.0, 174.5, 97.5], 0, True))
      self.obj249.out_connections_.append(self.obj254)
      self.obj254.in_connections_.append(self.obj249)
      self.obj249.graphObject_.pendingConnections.append((self.obj249.graphObject_.tag, self.obj254.graphObject_.tag, [85.0, 122.0, 179.28504672897196, 145.21052631578948], 0, True))
      self.obj250.out_connections_.append(self.obj252)
      self.obj252.in_connections_.append(self.obj250)
      self.obj250.graphObject_.pendingConnections.append((self.obj250.graphObject_.tag, self.obj252.graphObject_.tag, [264.0, 73.0, 268.78504672897196, 120.71052631578948], 0, True))
      self.obj252.out_connections_.append(self.obj251)
      self.obj251.in_connections_.append(self.obj252)
      self.obj252.graphObject_.pendingConnections.append((self.obj252.graphObject_.tag, self.obj251.graphObject_.tag, [273.5700934579439, 168.42105263157896, 268.78504672897196, 120.71052631578948], 0, True))
      self.obj253.out_connections_.append(self.obj250)
      self.obj250.in_connections_.append(self.obj253)
      self.obj253.graphObject_.pendingConnections.append((self.obj253.graphObject_.tag, self.obj250.graphObject_.tag, [264.0, 73.0, 174.5, 97.5], 0, True))
      self.obj254.out_connections_.append(self.obj251)
      self.obj251.in_connections_.append(self.obj254)
      self.obj254.graphObject_.pendingConnections.append((self.obj254.graphObject_.tag, self.obj251.graphObject_.tag, [273.5700934579439, 168.42105263157896, 179.28504672897196, 145.21052631578948], 0, True))

   def condition(self, graphID, isograph, atom3i):
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(2))
      return not hasattr(node, "LinkRaw2AR")
      
      

   def action(self, graphID, isograph, atom3i):
      node = self.getMatched ( graphID , self.LHS.nodeWithLabel(2) )
      node.LinkRaw2AR = True
      
      

