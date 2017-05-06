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

      self.obj780=rawMaterial(parent)
      self.obj780.preAction( self.LHS.CREATE )
      self.obj780.isGraphObjectVisual = True

      if(hasattr(self.obj780, '_setHierarchicalLink')):
        self.obj780._setHierarchicalLink(False)

      # MaxFlow
      self.obj780.MaxFlow.setNone()

      # price
      self.obj780.price.setNone()

      # Name
      self.obj780.Name.setValue('')
      self.obj780.Name.setNone()

      # ReqFlow
      self.obj780.ReqFlow.setNone()

      self.obj780.GGLabel.setValue(1)
      self.obj780.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(280.0,60.0,self.obj780)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['Text Scale'] = 0.5
         new_obj.layConstraints['scale'] = [0.5, 0.5]
      else: new_obj = None
      self.obj780.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj780)
      self.obj780.postAction( self.LHS.CREATE )

      self.obj781=Agent(parent)
      self.obj781.preAction( self.LHS.CREATE )
      self.obj781.isGraphObjectVisual = True

      if(hasattr(self.obj781, '_setHierarchicalLink')):
        self.obj781._setHierarchicalLink(False)

      # price
      self.obj781.price.setNone()

      # name
      self.obj781.name.setValue('')
      self.obj781.name.setNone()

      self.obj781.GGLabel.setValue(2)
      self.obj781.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(120.0,60.0,self.obj781)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['Text Scale'] = 0.5
         new_obj.layConstraints['scale'] = [0.5, 0.5]
      else: new_obj = None
      self.obj781.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj781)
      self.obj781.postAction( self.LHS.CREATE )

      self.obj782=GenericGraphEdge(parent)
      self.obj782.preAction( self.LHS.CREATE )
      self.obj782.isGraphObjectVisual = True

      if(hasattr(self.obj782, '_setHierarchicalLink')):
        self.obj782._setHierarchicalLink(False)

      self.obj782.GGLabel.setValue(3)
      self.obj782.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(198.5,126.5,self.obj782)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj782.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj782)
      self.obj782.postAction( self.LHS.CREATE )

      self.obj781.out_connections_.append(self.obj782)
      self.obj782.in_connections_.append(self.obj781)
      self.obj781.graphObject_.pendingConnections.append((self.obj781.graphObject_.tag, self.obj782.graphObject_.tag, [105.0, 89.5, 130.0, 127.0, 198.5, 126.5], 2, True))
      self.obj782.out_connections_.append(self.obj780)
      self.obj780.in_connections_.append(self.obj782)
      self.obj782.graphObject_.pendingConnections.append((self.obj782.graphObject_.tag, self.obj780.graphObject_.tag, [290.5, 89.5, 267.0, 126.0, 198.5, 126.5], 2, True))

      self.RHS = ASG_pns(parent)
      self.RHS.merge(ASG_omacs(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj786=rawMaterial(parent)
      self.obj786.preAction( self.RHS.CREATE )
      self.obj786.isGraphObjectVisual = True

      if(hasattr(self.obj786, '_setHierarchicalLink')):
        self.obj786._setHierarchicalLink(False)

      # MaxFlow
      self.obj786.MaxFlow.setNone()

      # price
      self.obj786.price.setNone()

      # Name
      self.obj786.Name.setValue('')
      self.obj786.Name.setNone()

      # ReqFlow
      self.obj786.ReqFlow.setNone()

      self.obj786.GGLabel.setValue(1)
      self.obj786.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(280.0,60.0,self.obj786)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj786.graphObject_ = new_obj
      self.obj7860= AttrCalc()
      self.obj7860.Copy=ATOM3Boolean()
      self.obj7860.Copy.setValue(('Copy from LHS', 1))
      self.obj7860.Copy.config = 0
      self.obj7860.Specify=ATOM3Constraint()
      self.obj7860.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj786.GGset2Any['MaxFlow']= self.obj7860
      self.obj7861= AttrCalc()
      self.obj7861.Copy=ATOM3Boolean()
      self.obj7861.Copy.setValue(('Copy from LHS', 0))
      self.obj7861.Copy.config = 0
      self.obj7861.Specify=ATOM3Constraint()
      self.obj7861.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(2)).price.getValue()\n\n\n\n\n\n\n'))
      self.obj786.GGset2Any['price']= self.obj7861
      self.obj7862= AttrCalc()
      self.obj7862.Copy=ATOM3Boolean()
      self.obj7862.Copy.setValue(('Copy from LHS', 1))
      self.obj7862.Copy.config = 0
      self.obj7862.Specify=ATOM3Constraint()
      self.obj7862.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj786.GGset2Any['Name']= self.obj7862
      self.obj7863= AttrCalc()
      self.obj7863.Copy=ATOM3Boolean()
      self.obj7863.Copy.setValue(('Copy from LHS', 1))
      self.obj7863.Copy.config = 0
      self.obj7863.Specify=ATOM3Constraint()
      self.obj7863.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj786.GGset2Any['ReqFlow']= self.obj7863

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj786)
      self.obj786.postAction( self.RHS.CREATE )

      self.obj787=Agent(parent)
      self.obj787.preAction( self.RHS.CREATE )
      self.obj787.isGraphObjectVisual = True

      if(hasattr(self.obj787, '_setHierarchicalLink')):
        self.obj787._setHierarchicalLink(False)

      # price
      self.obj787.price.setNone()

      # name
      self.obj787.name.setValue('')
      self.obj787.name.setNone()

      self.obj787.GGLabel.setValue(2)
      self.obj787.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(120.0,60.0,self.obj787)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj787.graphObject_ = new_obj
      self.obj7870= AttrCalc()
      self.obj7870.Copy=ATOM3Boolean()
      self.obj7870.Copy.setValue(('Copy from LHS', 1))
      self.obj7870.Copy.config = 0
      self.obj7870.Specify=ATOM3Constraint()
      self.obj7870.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj787.GGset2Any['price']= self.obj7870
      self.obj7871= AttrCalc()
      self.obj7871.Copy=ATOM3Boolean()
      self.obj7871.Copy.setValue(('Copy from LHS', 1))
      self.obj7871.Copy.config = 0
      self.obj7871.Specify=ATOM3Constraint()
      self.obj7871.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj787.GGset2Any['name']= self.obj7871

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj787)
      self.obj787.postAction( self.RHS.CREATE )

      self.obj788=GenericGraphEdge(parent)
      self.obj788.preAction( self.RHS.CREATE )
      self.obj788.isGraphObjectVisual = True

      if(hasattr(self.obj788, '_setHierarchicalLink')):
        self.obj788._setHierarchicalLink(False)

      self.obj788.GGLabel.setValue(3)
      self.obj788.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(198.5,126.5,self.obj788)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj788.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj788)
      self.obj788.postAction( self.RHS.CREATE )

      self.obj787.out_connections_.append(self.obj788)
      self.obj788.in_connections_.append(self.obj787)
      self.obj787.graphObject_.pendingConnections.append((self.obj787.graphObject_.tag, self.obj788.graphObject_.tag, [157.0, 122.0, 198.5, 126.5], 2, 0))
      self.obj788.out_connections_.append(self.obj786)
      self.obj786.in_connections_.append(self.obj788)
      self.obj788.graphObject_.pendingConnections.append((self.obj788.graphObject_.tag, self.obj786.graphObject_.tag, [304.0, 110.0, 198.5, 126.5], 2, 0))

   def condition(self, graphID, isograph, atom3i):
      
      raw = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      return not ( hasattr(raw, "AssignPrice" ) )
      
      

   def action(self, graphID, isograph, atom3i):
      raw = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      raw.AssignPrice=True
      print '######################## Assign Price for '+raw.Name.getValue()
      
      

