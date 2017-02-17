# _ RemoveGoals_GG_rule.py ____________________________________________________________________________
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
class RemoveGoals_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 21)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_omacss(parent)
      self.LHS.merge(ASG_pns2(parent))
      self.LHS.merge(ASG_GenericGraph(parent))

      self.obj1168=Goal(parent)
      self.obj1168.preAction( self.LHS.CREATE )
      self.obj1168.isGraphObjectVisual = True

      if(hasattr(self.obj1168, '_setHierarchicalLink')):
        self.obj1168._setHierarchicalLink(False)

      # name
      self.obj1168.name.setValue('')
      self.obj1168.name.setNone()

      self.obj1168.GGLabel.setValue(1)
      self.obj1168.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(200.0,60.0,self.obj1168)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1168.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1168)
      self.obj1168.postAction( self.LHS.CREATE )

      self.obj1169=metarial(parent)
      self.obj1169.preAction( self.LHS.CREATE )
      self.obj1169.isGraphObjectVisual = True

      if(hasattr(self.obj1169, '_setHierarchicalLink')):
        self.obj1169._setHierarchicalLink(False)

      # Name
      self.obj1169.Name.setValue('')
      self.obj1169.Name.setNone()

      self.obj1169.GGLabel.setValue(2)
      self.obj1169.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(340.0,60.0,self.obj1169)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1169.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1169)
      self.obj1169.postAction( self.LHS.CREATE )

      self.obj1170=GenericGraphEdge(parent)
      self.obj1170.preAction( self.LHS.CREATE )
      self.obj1170.isGraphObjectVisual = True

      if(hasattr(self.obj1170, '_setHierarchicalLink')):
        self.obj1170._setHierarchicalLink(False)

      self.obj1170.GGLabel.setValue(3)
      self.obj1170.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(292.0,107.0,self.obj1170)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1170.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1170)
      self.obj1170.postAction( self.LHS.CREATE )

      self.obj1168.out_connections_.append(self.obj1170)
      self.obj1170.in_connections_.append(self.obj1168)
      self.obj1168.graphObject_.pendingConnections.append((self.obj1168.graphObject_.tag, self.obj1170.graphObject_.tag, [234.0, 110.0, 292.0, 107.0], 0, True))
      self.obj1170.out_connections_.append(self.obj1169)
      self.obj1169.in_connections_.append(self.obj1170)
      self.obj1170.graphObject_.pendingConnections.append((self.obj1170.graphObject_.tag, self.obj1169.graphObject_.tag, [350.0, 104.0, 292.0, 107.0], 0, True))

      self.RHS = ASG_omacss(parent)
      self.RHS.merge(ASG_pns2(parent))

      self.obj1173=metarial(parent)
      self.obj1173.preAction( self.RHS.CREATE )
      self.obj1173.isGraphObjectVisual = True

      if(hasattr(self.obj1173, '_setHierarchicalLink')):
        self.obj1173._setHierarchicalLink(False)

      # Name
      self.obj1173.Name.setValue('')
      self.obj1173.Name.setNone()

      self.obj1173.GGLabel.setValue(2)
      self.obj1173.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(280.0,60.0,self.obj1173)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1173.graphObject_ = new_obj
      self.obj11730= AttrCalc()
      self.obj11730.Copy=ATOM3Boolean()
      self.obj11730.Copy.setValue(('Copy from LHS', 1))
      self.obj11730.Copy.config = 0
      self.obj11730.Specify=ATOM3Constraint()
      self.obj11730.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1173.GGset2Any['Name']= self.obj11730

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1173)
      self.obj1173.postAction( self.RHS.CREATE )


   def condition(self, graphID, isograph, atom3i):
      return self.graphRewritingSystem.finalStat > 20 
      

   def action(self, graphID, isograph, atom3i):
      pass

