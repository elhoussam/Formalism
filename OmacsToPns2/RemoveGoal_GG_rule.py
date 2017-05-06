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

      self.obj814=metarial(parent)
      self.obj814.preAction( self.LHS.CREATE )
      self.obj814.isGraphObjectVisual = True

      if(hasattr(self.obj814, '_setHierarchicalLink')):
        self.obj814._setHierarchicalLink(False)

      # MaxFlow
      self.obj814.MaxFlow.setNone()

      # price
      self.obj814.price.setValue(0)

      # Name
      self.obj814.Name.setValue('')
      self.obj814.Name.setNone()

      # ReqFlow
      self.obj814.ReqFlow.setNone()

      self.obj814.GGLabel.setValue(1)
      self.obj814.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(280.0,60.0,self.obj814)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj814.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj814)
      self.obj814.postAction( self.LHS.CREATE )

      self.obj815=Goal(parent)
      self.obj815.preAction( self.LHS.CREATE )
      self.obj815.isGraphObjectVisual = True

      if(hasattr(self.obj815, '_setHierarchicalLink')):
        self.obj815._setHierarchicalLink(False)

      # name
      self.obj815.name.setValue('')
      self.obj815.name.setNone()

      self.obj815.GGLabel.setValue(3)
      self.obj815.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(100.0,60.0,self.obj815)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj815.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj815)
      self.obj815.postAction( self.LHS.CREATE )

      self.obj816=GenericGraphEdge(parent)
      self.obj816.preAction( self.LHS.CREATE )
      self.obj816.isGraphObjectVisual = True

      if(hasattr(self.obj816, '_setHierarchicalLink')):
        self.obj816._setHierarchicalLink(False)

      self.obj816.GGLabel.setValue(4)
      self.obj816.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(205.0,106.0,self.obj816)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj816.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj816)
      self.obj816.postAction( self.LHS.CREATE )

      self.obj815.out_connections_.append(self.obj816)
      self.obj816.in_connections_.append(self.obj815)
      self.obj815.graphObject_.pendingConnections.append((self.obj815.graphObject_.tag, self.obj816.graphObject_.tag, [124.0, 110.0, 205.0, 106.0], 0, True))
      self.obj816.out_connections_.append(self.obj814)
      self.obj814.in_connections_.append(self.obj816)
      self.obj816.graphObject_.pendingConnections.append((self.obj816.graphObject_.tag, self.obj814.graphObject_.tag, [286.0, 102.0, 205.0, 106.0], 0, True))

      self.RHS = ASG_pns(parent)

      self.obj818=metarial(parent)
      self.obj818.preAction( self.RHS.CREATE )
      self.obj818.isGraphObjectVisual = True

      if(hasattr(self.obj818, '_setHierarchicalLink')):
        self.obj818._setHierarchicalLink(False)

      # MaxFlow
      self.obj818.MaxFlow.setNone()

      # price
      self.obj818.price.setValue(0)

      # Name
      self.obj818.Name.setValue('')
      self.obj818.Name.setNone()

      # ReqFlow
      self.obj818.ReqFlow.setNone()

      self.obj818.GGLabel.setValue(1)
      self.obj818.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(180.0,40.0,self.obj818)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj818.graphObject_ = new_obj
      self.obj8180= AttrCalc()
      self.obj8180.Copy=ATOM3Boolean()
      self.obj8180.Copy.setValue(('Copy from LHS', 1))
      self.obj8180.Copy.config = 0
      self.obj8180.Specify=ATOM3Constraint()
      self.obj8180.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj818.GGset2Any['MaxFlow']= self.obj8180
      self.obj8181= AttrCalc()
      self.obj8181.Copy=ATOM3Boolean()
      self.obj8181.Copy.setValue(('Copy from LHS', 1))
      self.obj8181.Copy.config = 0
      self.obj8181.Specify=ATOM3Constraint()
      self.obj8181.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj818.GGset2Any['Name']= self.obj8181
      self.obj8182= AttrCalc()
      self.obj8182.Copy=ATOM3Boolean()
      self.obj8182.Copy.setValue(('Copy from LHS', 1))
      self.obj8182.Copy.config = 0
      self.obj8182.Specify=ATOM3Constraint()
      self.obj8182.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj818.GGset2Any['ReqFlow']= self.obj8182

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj818)
      self.obj818.postAction( self.RHS.CREATE )


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
      

