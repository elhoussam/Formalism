# _ AssignPrice4Raw_GG_rule.py ____________________________________________________________________________
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
class AssignPrice4Raw_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 22)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_pns(parent)
      self.LHS.merge(ASG_omacs(parent))
      self.LHS.merge(ASG_GenericGraph(parent))

      self.obj1781=rawMaterial(parent)
      self.obj1781.preAction( self.LHS.CREATE )
      self.obj1781.isGraphObjectVisual = True

      if(hasattr(self.obj1781, '_setHierarchicalLink')):
        self.obj1781._setHierarchicalLink(False)

      # MaxFlow
      self.obj1781.MaxFlow.setNone()

      # price
      self.obj1781.price.setNone()

      # Name
      self.obj1781.Name.setValue('')
      self.obj1781.Name.setNone()

      # ReqFlow
      self.obj1781.ReqFlow.setNone()

      self.obj1781.GGLabel.setValue(1)
      self.obj1781.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(280.0,60.0,self.obj1781)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['Text Scale'] = 0.5
         new_obj.layConstraints['scale'] = [0.5, 0.5]
      else: new_obj = None
      self.obj1781.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1781)
      self.obj1781.postAction( self.LHS.CREATE )

      self.obj1782=Agent(parent)
      self.obj1782.preAction( self.LHS.CREATE )
      self.obj1782.isGraphObjectVisual = True

      if(hasattr(self.obj1782, '_setHierarchicalLink')):
        self.obj1782._setHierarchicalLink(False)

      # price
      self.obj1782.price.setNone()

      # name
      self.obj1782.name.setValue('')
      self.obj1782.name.setNone()

      self.obj1782.GGLabel.setValue(2)
      self.obj1782.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(120.0,60.0,self.obj1782)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['Text Scale'] = 0.5
         new_obj.layConstraints['scale'] = [0.5, 0.5]
      else: new_obj = None
      self.obj1782.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1782)
      self.obj1782.postAction( self.LHS.CREATE )

      self.obj1783=GenericGraphEdge(parent)
      self.obj1783.preAction( self.LHS.CREATE )
      self.obj1783.isGraphObjectVisual = True

      if(hasattr(self.obj1783, '_setHierarchicalLink')):
        self.obj1783._setHierarchicalLink(False)

      self.obj1783.GGLabel.setValue(3)
      self.obj1783.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(198.5,126.5,self.obj1783)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1783.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1783)
      self.obj1783.postAction( self.LHS.CREATE )

      self.obj1782.out_connections_.append(self.obj1783)
      self.obj1783.in_connections_.append(self.obj1782)
      self.obj1782.graphObject_.pendingConnections.append((self.obj1782.graphObject_.tag, self.obj1783.graphObject_.tag, [105.0, 89.5, 130.0, 127.0, 198.5, 126.5], 2, True))
      self.obj1783.out_connections_.append(self.obj1781)
      self.obj1781.in_connections_.append(self.obj1783)
      self.obj1783.graphObject_.pendingConnections.append((self.obj1783.graphObject_.tag, self.obj1781.graphObject_.tag, [290.5, 89.5, 267.0, 126.0, 198.5, 126.5], 2, True))

      self.RHS = ASG_pns(parent)
      self.RHS.merge(ASG_omacs(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj1787=rawMaterial(parent)
      self.obj1787.preAction( self.RHS.CREATE )
      self.obj1787.isGraphObjectVisual = True

      if(hasattr(self.obj1787, '_setHierarchicalLink')):
        self.obj1787._setHierarchicalLink(False)

      # MaxFlow
      self.obj1787.MaxFlow.setNone()

      # price
      self.obj1787.price.setNone()

      # Name
      self.obj1787.Name.setValue('')
      self.obj1787.Name.setNone()

      # ReqFlow
      self.obj1787.ReqFlow.setNone()

      self.obj1787.GGLabel.setValue(1)
      self.obj1787.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(280.0,60.0,self.obj1787)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1787.graphObject_ = new_obj
      self.obj17870= AttrCalc()
      self.obj17870.Copy=ATOM3Boolean()
      self.obj17870.Copy.setValue(('Copy from LHS', 1))
      self.obj17870.Copy.config = 0
      self.obj17870.Specify=ATOM3Constraint()
      self.obj17870.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1787.GGset2Any['MaxFlow']= self.obj17870
      self.obj17871= AttrCalc()
      self.obj17871.Copy=ATOM3Boolean()
      self.obj17871.Copy.setValue(('Copy from LHS', 0))
      self.obj17871.Copy.config = 0
      self.obj17871.Specify=ATOM3Constraint()
      self.obj17871.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(2)).price.getValue()\n\n\n\n\n\n\n'))
      self.obj1787.GGset2Any['price']= self.obj17871
      self.obj17872= AttrCalc()
      self.obj17872.Copy=ATOM3Boolean()
      self.obj17872.Copy.setValue(('Copy from LHS', 1))
      self.obj17872.Copy.config = 0
      self.obj17872.Specify=ATOM3Constraint()
      self.obj17872.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1787.GGset2Any['Name']= self.obj17872
      self.obj17873= AttrCalc()
      self.obj17873.Copy=ATOM3Boolean()
      self.obj17873.Copy.setValue(('Copy from LHS', 1))
      self.obj17873.Copy.config = 0
      self.obj17873.Specify=ATOM3Constraint()
      self.obj17873.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1787.GGset2Any['ReqFlow']= self.obj17873

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1787)
      self.obj1787.postAction( self.RHS.CREATE )

      self.obj1788=Agent(parent)
      self.obj1788.preAction( self.RHS.CREATE )
      self.obj1788.isGraphObjectVisual = True

      if(hasattr(self.obj1788, '_setHierarchicalLink')):
        self.obj1788._setHierarchicalLink(False)

      # price
      self.obj1788.price.setNone()

      # name
      self.obj1788.name.setValue('')
      self.obj1788.name.setNone()

      self.obj1788.GGLabel.setValue(2)
      self.obj1788.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(120.0,60.0,self.obj1788)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1788.graphObject_ = new_obj
      self.obj17880= AttrCalc()
      self.obj17880.Copy=ATOM3Boolean()
      self.obj17880.Copy.setValue(('Copy from LHS', 1))
      self.obj17880.Copy.config = 0
      self.obj17880.Specify=ATOM3Constraint()
      self.obj17880.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1788.GGset2Any['price']= self.obj17880
      self.obj17881= AttrCalc()
      self.obj17881.Copy=ATOM3Boolean()
      self.obj17881.Copy.setValue(('Copy from LHS', 1))
      self.obj17881.Copy.config = 0
      self.obj17881.Specify=ATOM3Constraint()
      self.obj17881.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1788.GGset2Any['name']= self.obj17881

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1788)
      self.obj1788.postAction( self.RHS.CREATE )

      self.obj1789=GenericGraphEdge(parent)
      self.obj1789.preAction( self.RHS.CREATE )
      self.obj1789.isGraphObjectVisual = True

      if(hasattr(self.obj1789, '_setHierarchicalLink')):
        self.obj1789._setHierarchicalLink(False)

      self.obj1789.GGLabel.setValue(3)
      self.obj1789.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(198.5,126.5,self.obj1789)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1789.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1789)
      self.obj1789.postAction( self.RHS.CREATE )

      self.obj1788.out_connections_.append(self.obj1789)
      self.obj1789.in_connections_.append(self.obj1788)
      self.obj1788.graphObject_.pendingConnections.append((self.obj1788.graphObject_.tag, self.obj1789.graphObject_.tag, [157.0, 122.0, 198.5, 126.5], 2, 0))
      self.obj1789.out_connections_.append(self.obj1787)
      self.obj1787.in_connections_.append(self.obj1789)
      self.obj1789.graphObject_.pendingConnections.append((self.obj1789.graphObject_.tag, self.obj1787.graphObject_.tag, [304.0, 110.0, 198.5, 126.5], 2, 0))

   def condition(self, graphID, isograph, atom3i):
      
      raw = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      return not ( hasattr(raw, "AssignPrice" ) )
      
      

   def action(self, graphID, isograph, atom3i):
      raw = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      raw.AssignPrice=True
      print '######################## Assign Price for '+raw.Name.getValue()
      
      

