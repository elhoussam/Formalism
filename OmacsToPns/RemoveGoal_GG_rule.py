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

      self.obj342=metarial(parent)
      self.obj342.preAction( self.LHS.CREATE )
      self.obj342.isGraphObjectVisual = True

      if(hasattr(self.obj342, '_setHierarchicalLink')):
        self.obj342._setHierarchicalLink(False)

      # MaxFlow
      self.obj342.MaxFlow.setNone()

      # price
      self.obj342.price.setValue(0)

      # Name
      self.obj342.Name.setValue('')
      self.obj342.Name.setNone()

      # ReqFlow
      self.obj342.ReqFlow.setNone()

      self.obj342.GGLabel.setValue(1)
      self.obj342.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(280.0,60.0,self.obj342)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj342.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj342)
      self.obj342.postAction( self.LHS.CREATE )

      self.obj343=Goal(parent)
      self.obj343.preAction( self.LHS.CREATE )
      self.obj343.isGraphObjectVisual = True

      if(hasattr(self.obj343, '_setHierarchicalLink')):
        self.obj343._setHierarchicalLink(False)

      # name
      self.obj343.name.setValue('')
      self.obj343.name.setNone()

      self.obj343.GGLabel.setValue(3)
      self.obj343.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(100.0,60.0,self.obj343)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj343.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj343)
      self.obj343.postAction( self.LHS.CREATE )

      self.obj344=GenericGraphEdge(parent)
      self.obj344.preAction( self.LHS.CREATE )
      self.obj344.isGraphObjectVisual = True

      if(hasattr(self.obj344, '_setHierarchicalLink')):
        self.obj344._setHierarchicalLink(False)

      self.obj344.GGLabel.setValue(4)
      self.obj344.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(205.0,106.0,self.obj344)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj344.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj344)
      self.obj344.postAction( self.LHS.CREATE )

      self.obj343.out_connections_.append(self.obj344)
      self.obj344.in_connections_.append(self.obj343)
      self.obj343.graphObject_.pendingConnections.append((self.obj343.graphObject_.tag, self.obj344.graphObject_.tag, [124.0, 110.0, 205.0, 106.0], 0, True))
      self.obj344.out_connections_.append(self.obj342)
      self.obj342.in_connections_.append(self.obj344)
      self.obj344.graphObject_.pendingConnections.append((self.obj344.graphObject_.tag, self.obj342.graphObject_.tag, [286.0, 102.0, 205.0, 106.0], 0, True))

      self.RHS = ASG_pns(parent)

      self.obj346=metarial(parent)
      self.obj346.preAction( self.RHS.CREATE )
      self.obj346.isGraphObjectVisual = True

      if(hasattr(self.obj346, '_setHierarchicalLink')):
        self.obj346._setHierarchicalLink(False)

      # MaxFlow
      self.obj346.MaxFlow.setNone()

      # price
      self.obj346.price.setValue(0)

      # Name
      self.obj346.Name.setValue('')
      self.obj346.Name.setNone()

      # ReqFlow
      self.obj346.ReqFlow.setNone()

      self.obj346.GGLabel.setValue(1)
      self.obj346.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(180.0,40.0,self.obj346)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj346.graphObject_ = new_obj
      self.obj3460= AttrCalc()
      self.obj3460.Copy=ATOM3Boolean()
      self.obj3460.Copy.setValue(('Copy from LHS', 1))
      self.obj3460.Copy.config = 0
      self.obj3460.Specify=ATOM3Constraint()
      self.obj3460.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj346.GGset2Any['MaxFlow']= self.obj3460
      self.obj3461= AttrCalc()
      self.obj3461.Copy=ATOM3Boolean()
      self.obj3461.Copy.setValue(('Copy from LHS', 1))
      self.obj3461.Copy.config = 0
      self.obj3461.Specify=ATOM3Constraint()
      self.obj3461.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj346.GGset2Any['Name']= self.obj3461
      self.obj3462= AttrCalc()
      self.obj3462.Copy=ATOM3Boolean()
      self.obj3462.Copy.setValue(('Copy from LHS', 1))
      self.obj3462.Copy.config = 0
      self.obj3462.Specify=ATOM3Constraint()
      self.obj3462.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj346.GGset2Any['ReqFlow']= self.obj3462

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj346)
      self.obj346.postAction( self.RHS.CREATE )


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
      

