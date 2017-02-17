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

      self.obj1038=Agent(parent)
      self.obj1038.preAction( self.LHS.CREATE )
      self.obj1038.isGraphObjectVisual = True

      if(hasattr(self.obj1038, '_setHierarchicalLink')):
        self.obj1038._setHierarchicalLink(False)

      # price
      self.obj1038.price.setValue(0)

      # name
      self.obj1038.name.setValue('')
      self.obj1038.name.setNone()

      self.obj1038.GGLabel.setValue(1)
      self.obj1038.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(100.0,40.0,self.obj1038)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1038.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1038)
      self.obj1038.postAction( self.LHS.CREATE )

      self.obj1039=rawMaterial(parent)
      self.obj1039.preAction( self.LHS.CREATE )
      self.obj1039.isGraphObjectVisual = True

      if(hasattr(self.obj1039, '_setHierarchicalLink')):
        self.obj1039._setHierarchicalLink(False)

      # Name
      self.obj1039.Name.setValue('')
      self.obj1039.Name.setNone()

      self.obj1039.GGLabel.setValue(3)
      self.obj1039.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(280.0,20.0,self.obj1039)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1039.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1039)
      self.obj1039.postAction( self.LHS.CREATE )

      self.obj1040=operatingUnit(parent)
      self.obj1040.preAction( self.LHS.CREATE )
      self.obj1040.isGraphObjectVisual = True

      if(hasattr(self.obj1040, '_setHierarchicalLink')):
        self.obj1040._setHierarchicalLink(False)

      # name
      self.obj1040.name.setValue('')
      self.obj1040.name.setNone()

      self.obj1040.GGLabel.setValue(2)
      self.obj1040.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(260.0,160.0,self.obj1040)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1040.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1040)
      self.obj1040.postAction( self.LHS.CREATE )

      self.obj1041=GenericGraphEdge(parent)
      self.obj1041.preAction( self.LHS.CREATE )
      self.obj1041.isGraphObjectVisual = True

      if(hasattr(self.obj1041, '_setHierarchicalLink')):
        self.obj1041._setHierarchicalLink(False)

      self.obj1041.GGLabel.setValue(4)
      self.obj1041.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(214.75,92.75,self.obj1041)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1041.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1041)
      self.obj1041.postAction( self.LHS.CREATE )

      self.obj1042=GenericGraphEdge(parent)
      self.obj1042.preAction( self.LHS.CREATE )
      self.obj1042.isGraphObjectVisual = True

      if(hasattr(self.obj1042, '_setHierarchicalLink')):
        self.obj1042._setHierarchicalLink(False)

      self.obj1042.GGLabel.setValue(5)
      self.obj1042.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(241.642523364,131.105263158,self.obj1042)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1042.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1042)
      self.obj1042.postAction( self.LHS.CREATE )

      self.obj1038.out_connections_.append(self.obj1041)
      self.obj1041.in_connections_.append(self.obj1038)
      self.obj1038.graphObject_.pendingConnections.append((self.obj1038.graphObject_.tag, self.obj1041.graphObject_.tag, [125.0, 102.0, 170.0, 100.0, 214.75, 92.75], 2, True))
      self.obj1038.out_connections_.append(self.obj1042)
      self.obj1042.in_connections_.append(self.obj1038)
      self.obj1038.graphObject_.pendingConnections.append((self.obj1038.graphObject_.tag, self.obj1042.graphObject_.tag, [125.0, 102.0, 204.5, 114.5, 241.64252336448598, 131.10526315789474], 2, True))
      self.obj1041.out_connections_.append(self.obj1039)
      self.obj1039.in_connections_.append(self.obj1041)
      self.obj1041.graphObject_.pendingConnections.append((self.obj1041.graphObject_.tag, self.obj1039.graphObject_.tag, [304.0, 73.0, 259.5, 85.5, 214.75, 92.75], 2, True))
      self.obj1042.out_connections_.append(self.obj1040)
      self.obj1040.in_connections_.append(self.obj1042)
      self.obj1042.graphObject_.pendingConnections.append((self.obj1042.graphObject_.tag, self.obj1040.graphObject_.tag, [273.5700934579439, 168.42105263157896, 278.78504672897196, 147.71052631578948, 241.64252336448598, 131.10526315789474], 2, True))

      self.RHS = ASG_omacss(parent)
      self.RHS.merge(ASG_pns2(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj1046=Agent(parent)
      self.obj1046.preAction( self.RHS.CREATE )
      self.obj1046.isGraphObjectVisual = True

      if(hasattr(self.obj1046, '_setHierarchicalLink')):
        self.obj1046._setHierarchicalLink(False)

      # price
      self.obj1046.price.setValue(0)

      # name
      self.obj1046.name.setValue('')
      self.obj1046.name.setNone()

      self.obj1046.GGLabel.setValue(1)
      self.obj1046.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(60.0,60.0,self.obj1046)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1046.graphObject_ = new_obj
      self.obj10460= AttrCalc()
      self.obj10460.Copy=ATOM3Boolean()
      self.obj10460.Copy.setValue(('Copy from LHS', 1))
      self.obj10460.Copy.config = 0
      self.obj10460.Specify=ATOM3Constraint()
      self.obj10460.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1046.GGset2Any['price']= self.obj10460
      self.obj10461= AttrCalc()
      self.obj10461.Copy=ATOM3Boolean()
      self.obj10461.Copy.setValue(('Copy from LHS', 1))
      self.obj10461.Copy.config = 0
      self.obj10461.Specify=ATOM3Constraint()
      self.obj10461.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1046.GGset2Any['name']= self.obj10461

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1046)
      self.obj1046.postAction( self.RHS.CREATE )

      self.obj1047=rawMaterial(parent)
      self.obj1047.preAction( self.RHS.CREATE )
      self.obj1047.isGraphObjectVisual = True

      if(hasattr(self.obj1047, '_setHierarchicalLink')):
        self.obj1047._setHierarchicalLink(False)

      # Name
      self.obj1047.Name.setValue('')
      self.obj1047.Name.setNone()

      self.obj1047.GGLabel.setValue(3)
      self.obj1047.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(240.0,20.0,self.obj1047)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1047.graphObject_ = new_obj
      self.obj10470= AttrCalc()
      self.obj10470.Copy=ATOM3Boolean()
      self.obj10470.Copy.setValue(('Copy from LHS', 1))
      self.obj10470.Copy.config = 0
      self.obj10470.Specify=ATOM3Constraint()
      self.obj10470.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1047.GGset2Any['Name']= self.obj10470

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1047)
      self.obj1047.postAction( self.RHS.CREATE )

      self.obj1048=operatingUnit(parent)
      self.obj1048.preAction( self.RHS.CREATE )
      self.obj1048.isGraphObjectVisual = True

      if(hasattr(self.obj1048, '_setHierarchicalLink')):
        self.obj1048._setHierarchicalLink(False)

      # name
      self.obj1048.name.setValue('')
      self.obj1048.name.setNone()

      self.obj1048.GGLabel.setValue(2)
      self.obj1048.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(260.0,160.0,self.obj1048)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1048.graphObject_ = new_obj
      self.obj10480= AttrCalc()
      self.obj10480.Copy=ATOM3Boolean()
      self.obj10480.Copy.setValue(('Copy from LHS', 1))
      self.obj10480.Copy.config = 0
      self.obj10480.Specify=ATOM3Constraint()
      self.obj10480.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1048.GGset2Any['name']= self.obj10480

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1048)
      self.obj1048.postAction( self.RHS.CREATE )

      self.obj1049=fromRaw(parent)
      self.obj1049.preAction( self.RHS.CREATE )
      self.obj1049.isGraphObjectVisual = True

      if(hasattr(self.obj1049, '_setHierarchicalLink')):
        self.obj1049._setHierarchicalLink(False)

      # rate
      self.obj1049.rate.setValue(1.0)

      self.obj1049.GGLabel.setValue(6)
      self.obj1049.graphClass_= graph_fromRaw
      if parent.genGraphics:
         new_obj = graph_fromRaw(268.785046729,120.710526316,self.obj1049)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1049.graphObject_ = new_obj
      self.obj10490= AttrCalc()
      self.obj10490.Copy=ATOM3Boolean()
      self.obj10490.Copy.setValue(('Copy from LHS', 0))
      self.obj10490.Copy.config = 0
      self.obj10490.Specify=ATOM3Constraint()
      self.obj10490.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1049.GGset2Any['rate']= self.obj10490

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1049)
      self.obj1049.postAction( self.RHS.CREATE )

      self.obj1050=GenericGraphEdge(parent)
      self.obj1050.preAction( self.RHS.CREATE )
      self.obj1050.isGraphObjectVisual = True

      if(hasattr(self.obj1050, '_setHierarchicalLink')):
        self.obj1050._setHierarchicalLink(False)

      self.obj1050.GGLabel.setValue(4)
      self.obj1050.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(174.5,97.5,self.obj1050)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1050.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1050)
      self.obj1050.postAction( self.RHS.CREATE )

      self.obj1051=GenericGraphEdge(parent)
      self.obj1051.preAction( self.RHS.CREATE )
      self.obj1051.isGraphObjectVisual = True

      if(hasattr(self.obj1051, '_setHierarchicalLink')):
        self.obj1051._setHierarchicalLink(False)

      self.obj1051.GGLabel.setValue(5)
      self.obj1051.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(179.285046729,145.210526316,self.obj1051)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1051.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1051)
      self.obj1051.postAction( self.RHS.CREATE )

      self.obj1046.out_connections_.append(self.obj1050)
      self.obj1050.in_connections_.append(self.obj1046)
      self.obj1046.graphObject_.pendingConnections.append((self.obj1046.graphObject_.tag, self.obj1050.graphObject_.tag, [85.0, 122.0, 174.5, 97.5], 0, True))
      self.obj1046.out_connections_.append(self.obj1051)
      self.obj1051.in_connections_.append(self.obj1046)
      self.obj1046.graphObject_.pendingConnections.append((self.obj1046.graphObject_.tag, self.obj1051.graphObject_.tag, [85.0, 122.0, 179.28504672897196, 145.21052631578948], 0, True))
      self.obj1047.out_connections_.append(self.obj1049)
      self.obj1049.in_connections_.append(self.obj1047)
      self.obj1047.graphObject_.pendingConnections.append((self.obj1047.graphObject_.tag, self.obj1049.graphObject_.tag, [264.0, 73.0, 268.78504672897196, 120.71052631578948], 0, True))
      self.obj1049.out_connections_.append(self.obj1048)
      self.obj1048.in_connections_.append(self.obj1049)
      self.obj1049.graphObject_.pendingConnections.append((self.obj1049.graphObject_.tag, self.obj1048.graphObject_.tag, [273.5700934579439, 168.42105263157896, 268.78504672897196, 120.71052631578948], 0, True))
      self.obj1050.out_connections_.append(self.obj1047)
      self.obj1047.in_connections_.append(self.obj1050)
      self.obj1050.graphObject_.pendingConnections.append((self.obj1050.graphObject_.tag, self.obj1047.graphObject_.tag, [264.0, 73.0, 174.5, 97.5], 0, True))
      self.obj1051.out_connections_.append(self.obj1048)
      self.obj1048.in_connections_.append(self.obj1051)
      self.obj1051.graphObject_.pendingConnections.append((self.obj1051.graphObject_.tag, self.obj1048.graphObject_.tag, [273.5700934579439, 168.42105263157896, 179.28504672897196, 145.21052631578948], 0, True))

   def condition(self, graphID, isograph, atom3i):
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(2))
      return not hasattr(node, "LinkRaw2AR")
      
      

   def action(self, graphID, isograph, atom3i):
      node = self.getMatched ( graphID , self.LHS.nodeWithLabel(2) )
      node.LinkRaw2AR = True
      
      

