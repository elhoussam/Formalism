# _ TransformGoal2Matr_GG_rule.py ____________________________________________________________________________
# File generated automatically by ATOM3. Graph Grammar Rule
# ___________________________________________________________________________________________
from GGrule import *
from CapableOf import *
from Goal import *
from ASG_omacss import *
from Agent import *
from Capabilitie import *
from Role import *
from requir import *
from achieve import *
from posses import *
from GenericGraphEdge import *
from intoProduct import *
from operatingUnit import *
from metarial import *
from rawMaterial import *
from fromMaterial import *
from fromRaw import *
from ASG_pns2 import *
from intoMaterial import *
from ASG_GenericGraph import *
from product import *
from GenericGraphNode import *
class TransformGoal2Matr_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 9)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_omacss(parent)

      self.obj287=Goal(parent)
      self.obj287.preAction( self.LHS.CREATE )
      self.obj287.isGraphObjectVisual = True

      if(hasattr(self.obj287, '_setHierarchicalLink')):
        self.obj287._setHierarchicalLink(False)

      # name
      self.obj287.name.setValue('')
      self.obj287.name.setNone()

      self.obj287.GGLabel.setValue(1)
      self.obj287.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(80.0,60.0,self.obj287)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj287.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj287)
      self.obj287.postAction( self.LHS.CREATE )


      self.RHS = ASG_omacss(parent)
      self.RHS.merge(ASG_pns2(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj287=Goal(parent)
      self.obj287.preAction( self.RHS.CREATE )
      self.obj287.isGraphObjectVisual = True

      if(hasattr(self.obj287, '_setHierarchicalLink')):
        self.obj287._setHierarchicalLink(False)

      # name
      self.obj287.name.setValue('')
      self.obj287.name.setNone()

      self.obj287.GGLabel.setValue(1)
      self.obj287.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(80.0,60.0,self.obj287)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj287.graphObject_ = new_obj
      self.obj2870= AttrCalc()
      self.obj2870.Copy=ATOM3Boolean()
      self.obj2870.Copy.setValue(('Copy from LHS', 1))
      self.obj2870.Copy.config = 0
      self.obj2870.Specify=ATOM3Constraint()
      self.obj2870.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj287.GGset2Any['name']= self.obj2870

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj287)
      self.obj287.postAction( self.RHS.CREATE )

      self.obj301=metarial(parent)
      self.obj301.preAction( self.RHS.CREATE )
      self.obj301.isGraphObjectVisual = True

      if(hasattr(self.obj301, '_setHierarchicalLink')):
        self.obj301._setHierarchicalLink(False)

      # Name
      self.obj301.Name.setValue('')
      self.obj301.Name.setNone()

      self.obj301.GGLabel.setValue(3)
      self.obj301.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(240.0,80.0,self.obj301)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj301.graphObject_ = new_obj
      self.obj3010= AttrCalc()
      self.obj3010.Copy=ATOM3Boolean()
      self.obj3010.Copy.setValue(('Copy from LHS', 0))
      self.obj3010.Copy.config = 0
      self.obj3010.Specify=ATOM3Constraint()
      self.obj3010.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\nreturn self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()\n'))
      self.obj301.GGset2Any['Name']= self.obj3010

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj301)
      self.obj301.postAction( self.RHS.CREATE )

      self.obj306=GenericGraphEdge(parent)
      self.obj306.preAction( self.RHS.CREATE )
      self.obj306.isGraphObjectVisual = True

      if(hasattr(self.obj306, '_setHierarchicalLink')):
        self.obj306._setHierarchicalLink(False)

      self.obj306.GGLabel.setValue(4)
      self.obj306.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(182.0,117.0,self.obj306)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj306.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj306)
      self.obj306.postAction( self.RHS.CREATE )

      self.obj287.out_connections_.append(self.obj306)
      self.obj306.in_connections_.append(self.obj287)
      self.obj287.graphObject_.pendingConnections.append((self.obj287.graphObject_.tag, self.obj306.graphObject_.tag, [114.0, 110.0, 182.0, 117.0], 0, True))
      self.obj306.out_connections_.append(self.obj301)
      self.obj301.in_connections_.append(self.obj306)
      self.obj306.graphObject_.pendingConnections.append((self.obj306.graphObject_.tag, self.obj301.graphObject_.tag, [250.0, 124.0, 182.0, 117.0], 0, True))

   def condition(self, graphID, isograph, atom3i):
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      return not hasattr(node, "Goal2Mat")
      
      

   def action(self, graphID, isograph, atom3i):
      node = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) )
      node.Goal2Mat = True
      
      

