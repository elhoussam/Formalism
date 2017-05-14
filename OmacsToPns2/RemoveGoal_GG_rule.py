# _ RemoveGoal_GG_rule.py ____________________________________________________________________________
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
class RemoveGoal_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 25)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_pns(parent)
      self.LHS.merge(ASG_omacs(parent))
      self.LHS.merge(ASG_GenericGraph(parent))

      self.obj1815=metarial(parent)
      self.obj1815.preAction( self.LHS.CREATE )
      self.obj1815.isGraphObjectVisual = True

      if(hasattr(self.obj1815, '_setHierarchicalLink')):
        self.obj1815._setHierarchicalLink(False)

      # MaxFlow
      self.obj1815.MaxFlow.setNone()

      # price
      self.obj1815.price.setValue(0)

      # Name
      self.obj1815.Name.setValue('')
      self.obj1815.Name.setNone()

      # ReqFlow
      self.obj1815.ReqFlow.setNone()

      self.obj1815.GGLabel.setValue(1)
      self.obj1815.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(280.0,60.0,self.obj1815)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1815.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1815)
      self.obj1815.postAction( self.LHS.CREATE )

      self.obj1816=Goal(parent)
      self.obj1816.preAction( self.LHS.CREATE )
      self.obj1816.isGraphObjectVisual = True

      if(hasattr(self.obj1816, '_setHierarchicalLink')):
        self.obj1816._setHierarchicalLink(False)

      # name
      self.obj1816.name.setValue('')
      self.obj1816.name.setNone()

      self.obj1816.GGLabel.setValue(3)
      self.obj1816.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(100.0,60.0,self.obj1816)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1816.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1816)
      self.obj1816.postAction( self.LHS.CREATE )

      self.obj1817=GenericGraphEdge(parent)
      self.obj1817.preAction( self.LHS.CREATE )
      self.obj1817.isGraphObjectVisual = True

      if(hasattr(self.obj1817, '_setHierarchicalLink')):
        self.obj1817._setHierarchicalLink(False)

      self.obj1817.GGLabel.setValue(4)
      self.obj1817.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(205.0,106.0,self.obj1817)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1817.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1817)
      self.obj1817.postAction( self.LHS.CREATE )

      self.obj1816.out_connections_.append(self.obj1817)
      self.obj1817.in_connections_.append(self.obj1816)
      self.obj1816.graphObject_.pendingConnections.append((self.obj1816.graphObject_.tag, self.obj1817.graphObject_.tag, [124.0, 110.0, 205.0, 106.0], 0, True))
      self.obj1817.out_connections_.append(self.obj1815)
      self.obj1815.in_connections_.append(self.obj1817)
      self.obj1817.graphObject_.pendingConnections.append((self.obj1817.graphObject_.tag, self.obj1815.graphObject_.tag, [286.0, 102.0, 205.0, 106.0], 0, True))

      self.RHS = ASG_pns(parent)

      self.obj1819=metarial(parent)
      self.obj1819.preAction( self.RHS.CREATE )
      self.obj1819.isGraphObjectVisual = True

      if(hasattr(self.obj1819, '_setHierarchicalLink')):
        self.obj1819._setHierarchicalLink(False)

      # MaxFlow
      self.obj1819.MaxFlow.setNone()

      # price
      self.obj1819.price.setValue(0)

      # Name
      self.obj1819.Name.setValue('')
      self.obj1819.Name.setNone()

      # ReqFlow
      self.obj1819.ReqFlow.setNone()

      self.obj1819.GGLabel.setValue(1)
      self.obj1819.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(180.0,40.0,self.obj1819)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1819.graphObject_ = new_obj
      self.obj18190= AttrCalc()
      self.obj18190.Copy=ATOM3Boolean()
      self.obj18190.Copy.setValue(('Copy from LHS', 1))
      self.obj18190.Copy.config = 0
      self.obj18190.Specify=ATOM3Constraint()
      self.obj18190.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1819.GGset2Any['MaxFlow']= self.obj18190
      self.obj18191= AttrCalc()
      self.obj18191.Copy=ATOM3Boolean()
      self.obj18191.Copy.setValue(('Copy from LHS', 1))
      self.obj18191.Copy.config = 0
      self.obj18191.Specify=ATOM3Constraint()
      self.obj18191.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1819.GGset2Any['Name']= self.obj18191
      self.obj18192= AttrCalc()
      self.obj18192.Copy=ATOM3Boolean()
      self.obj18192.Copy.setValue(('Copy from LHS', 1))
      self.obj18192.Copy.config = 0
      self.obj18192.Specify=ATOM3Constraint()
      self.obj18192.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1819.GGset2Any['ReqFlow']= self.obj18192

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1819)
      self.obj1819.postAction( self.RHS.CREATE )


   def condition(self, graphID, isograph, atom3i):
      return self.graphRewritingSystem.finalStat > 20 
      

   def action(self, graphID, isograph, atom3i):
      # If you want to apply this rule at most once on asingle host graph node, 
      # then uncomment the next two lines. Change the default GG label (1) if needed.
      
      # Make sure to enable the CONDITION code as well
      # And to use the same label & unique name in the ACTION
      # WARNING: _uniqueName503 is not guaranteed to be unique (so change it, be safe!)
      
      #node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      #node._uniqueName503 = True
      pass
      

