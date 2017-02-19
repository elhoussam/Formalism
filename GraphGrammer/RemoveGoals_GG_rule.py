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
      GGrule.__init__(self, 25)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_omacss(parent)
      self.LHS.merge(ASG_pns2(parent))
      self.LHS.merge(ASG_GenericGraph(parent))

      self.obj404=Goal(parent)
      self.obj404.preAction( self.LHS.CREATE )
      self.obj404.isGraphObjectVisual = True

      if(hasattr(self.obj404, '_setHierarchicalLink')):
        self.obj404._setHierarchicalLink(False)

      # name
      self.obj404.name.setValue('')
      self.obj404.name.setNone()

      self.obj404.GGLabel.setValue(1)
      self.obj404.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(200.0,60.0,self.obj404)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj404.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj404)
      self.obj404.postAction( self.LHS.CREATE )

      self.obj405=metarial(parent)
      self.obj405.preAction( self.LHS.CREATE )
      self.obj405.isGraphObjectVisual = True

      if(hasattr(self.obj405, '_setHierarchicalLink')):
        self.obj405._setHierarchicalLink(False)

      # Name
      self.obj405.Name.setValue('')
      self.obj405.Name.setNone()

      self.obj405.GGLabel.setValue(2)
      self.obj405.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(340.0,60.0,self.obj405)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj405.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj405)
      self.obj405.postAction( self.LHS.CREATE )

      self.obj406=GenericGraphEdge(parent)
      self.obj406.preAction( self.LHS.CREATE )
      self.obj406.isGraphObjectVisual = True

      if(hasattr(self.obj406, '_setHierarchicalLink')):
        self.obj406._setHierarchicalLink(False)

      self.obj406.GGLabel.setValue(3)
      self.obj406.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(292.0,107.0,self.obj406)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj406.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj406)
      self.obj406.postAction( self.LHS.CREATE )

      self.obj404.out_connections_.append(self.obj406)
      self.obj406.in_connections_.append(self.obj404)
      self.obj404.graphObject_.pendingConnections.append((self.obj404.graphObject_.tag, self.obj406.graphObject_.tag, [234.0, 110.0, 292.0, 107.0], 0, True))
      self.obj406.out_connections_.append(self.obj405)
      self.obj405.in_connections_.append(self.obj406)
      self.obj406.graphObject_.pendingConnections.append((self.obj406.graphObject_.tag, self.obj405.graphObject_.tag, [350.0, 104.0, 292.0, 107.0], 0, True))

      self.RHS = ASG_omacss(parent)
      self.RHS.merge(ASG_pns2(parent))

      self.obj409=metarial(parent)
      self.obj409.preAction( self.RHS.CREATE )
      self.obj409.isGraphObjectVisual = True

      if(hasattr(self.obj409, '_setHierarchicalLink')):
        self.obj409._setHierarchicalLink(False)

      # Name
      self.obj409.Name.setValue('')
      self.obj409.Name.setNone()

      self.obj409.GGLabel.setValue(2)
      self.obj409.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(280.0,60.0,self.obj409)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj409.graphObject_ = new_obj
      self.obj4090= AttrCalc()
      self.obj4090.Copy=ATOM3Boolean()
      self.obj4090.Copy.setValue(('Copy from LHS', 1))
      self.obj4090.Copy.config = 0
      self.obj4090.Specify=ATOM3Constraint()
      self.obj4090.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj409.GGset2Any['Name']= self.obj4090

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj409)
      self.obj409.postAction( self.RHS.CREATE )


   def condition(self, graphID, isograph, atom3i):
      return self.graphRewritingSystem.finalStat > 20 
      

   def action(self, graphID, isograph, atom3i):
      pass

