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

      self.obj308=rawMaterial(parent)
      self.obj308.preAction( self.LHS.CREATE )
      self.obj308.isGraphObjectVisual = True

      if(hasattr(self.obj308, '_setHierarchicalLink')):
        self.obj308._setHierarchicalLink(False)

      # MaxFlow
      self.obj308.MaxFlow.setNone()

      # price
      self.obj308.price.setNone()

      # Name
      self.obj308.Name.setValue('')
      self.obj308.Name.setNone()

      # ReqFlow
      self.obj308.ReqFlow.setNone()

      self.obj308.GGLabel.setValue(1)
      self.obj308.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(280.0,60.0,self.obj308)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['Text Scale'] = 0.5
         new_obj.layConstraints['scale'] = [0.5, 0.5]
      else: new_obj = None
      self.obj308.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj308)
      self.obj308.postAction( self.LHS.CREATE )

      self.obj309=Agent(parent)
      self.obj309.preAction( self.LHS.CREATE )
      self.obj309.isGraphObjectVisual = True

      if(hasattr(self.obj309, '_setHierarchicalLink')):
        self.obj309._setHierarchicalLink(False)

      # price
      self.obj309.price.setNone()

      # name
      self.obj309.name.setValue('')
      self.obj309.name.setNone()

      self.obj309.GGLabel.setValue(2)
      self.obj309.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(120.0,60.0,self.obj309)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['Text Scale'] = 0.5
         new_obj.layConstraints['scale'] = [0.5, 0.5]
      else: new_obj = None
      self.obj309.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj309)
      self.obj309.postAction( self.LHS.CREATE )

      self.obj310=GenericGraphEdge(parent)
      self.obj310.preAction( self.LHS.CREATE )
      self.obj310.isGraphObjectVisual = True

      if(hasattr(self.obj310, '_setHierarchicalLink')):
        self.obj310._setHierarchicalLink(False)

      self.obj310.GGLabel.setValue(3)
      self.obj310.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(198.5,126.5,self.obj310)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj310.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj310)
      self.obj310.postAction( self.LHS.CREATE )

      self.obj309.out_connections_.append(self.obj310)
      self.obj310.in_connections_.append(self.obj309)
      self.obj309.graphObject_.pendingConnections.append((self.obj309.graphObject_.tag, self.obj310.graphObject_.tag, [105.0, 89.5, 130.0, 127.0, 198.5, 126.5], 2, True))
      self.obj310.out_connections_.append(self.obj308)
      self.obj308.in_connections_.append(self.obj310)
      self.obj310.graphObject_.pendingConnections.append((self.obj310.graphObject_.tag, self.obj308.graphObject_.tag, [290.5, 89.5, 267.0, 126.0, 198.5, 126.5], 2, True))

      self.RHS = ASG_pns(parent)
      self.RHS.merge(ASG_omacs(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj314=rawMaterial(parent)
      self.obj314.preAction( self.RHS.CREATE )
      self.obj314.isGraphObjectVisual = True

      if(hasattr(self.obj314, '_setHierarchicalLink')):
        self.obj314._setHierarchicalLink(False)

      # MaxFlow
      self.obj314.MaxFlow.setNone()

      # price
      self.obj314.price.setNone()

      # Name
      self.obj314.Name.setValue('')
      self.obj314.Name.setNone()

      # ReqFlow
      self.obj314.ReqFlow.setNone()

      self.obj314.GGLabel.setValue(1)
      self.obj314.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(280.0,60.0,self.obj314)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj314.graphObject_ = new_obj
      self.obj3140= AttrCalc()
      self.obj3140.Copy=ATOM3Boolean()
      self.obj3140.Copy.setValue(('Copy from LHS', 1))
      self.obj3140.Copy.config = 0
      self.obj3140.Specify=ATOM3Constraint()
      self.obj3140.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj314.GGset2Any['MaxFlow']= self.obj3140
      self.obj3141= AttrCalc()
      self.obj3141.Copy=ATOM3Boolean()
      self.obj3141.Copy.setValue(('Copy from LHS', 0))
      self.obj3141.Copy.config = 0
      self.obj3141.Specify=ATOM3Constraint()
      self.obj3141.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(2)).price.getValue()\n\n\n\n\n\n\n'))
      self.obj314.GGset2Any['price']= self.obj3141
      self.obj3142= AttrCalc()
      self.obj3142.Copy=ATOM3Boolean()
      self.obj3142.Copy.setValue(('Copy from LHS', 1))
      self.obj3142.Copy.config = 0
      self.obj3142.Specify=ATOM3Constraint()
      self.obj3142.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj314.GGset2Any['Name']= self.obj3142
      self.obj3143= AttrCalc()
      self.obj3143.Copy=ATOM3Boolean()
      self.obj3143.Copy.setValue(('Copy from LHS', 1))
      self.obj3143.Copy.config = 0
      self.obj3143.Specify=ATOM3Constraint()
      self.obj3143.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj314.GGset2Any['ReqFlow']= self.obj3143

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj314)
      self.obj314.postAction( self.RHS.CREATE )

      self.obj315=Agent(parent)
      self.obj315.preAction( self.RHS.CREATE )
      self.obj315.isGraphObjectVisual = True

      if(hasattr(self.obj315, '_setHierarchicalLink')):
        self.obj315._setHierarchicalLink(False)

      # price
      self.obj315.price.setNone()

      # name
      self.obj315.name.setValue('')
      self.obj315.name.setNone()

      self.obj315.GGLabel.setValue(2)
      self.obj315.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(120.0,60.0,self.obj315)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj315.graphObject_ = new_obj
      self.obj3150= AttrCalc()
      self.obj3150.Copy=ATOM3Boolean()
      self.obj3150.Copy.setValue(('Copy from LHS', 1))
      self.obj3150.Copy.config = 0
      self.obj3150.Specify=ATOM3Constraint()
      self.obj3150.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj315.GGset2Any['price']= self.obj3150
      self.obj3151= AttrCalc()
      self.obj3151.Copy=ATOM3Boolean()
      self.obj3151.Copy.setValue(('Copy from LHS', 1))
      self.obj3151.Copy.config = 0
      self.obj3151.Specify=ATOM3Constraint()
      self.obj3151.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj315.GGset2Any['name']= self.obj3151

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj315)
      self.obj315.postAction( self.RHS.CREATE )

      self.obj316=GenericGraphEdge(parent)
      self.obj316.preAction( self.RHS.CREATE )
      self.obj316.isGraphObjectVisual = True

      if(hasattr(self.obj316, '_setHierarchicalLink')):
        self.obj316._setHierarchicalLink(False)

      self.obj316.GGLabel.setValue(3)
      self.obj316.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(198.5,126.5,self.obj316)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj316.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj316)
      self.obj316.postAction( self.RHS.CREATE )

      self.obj315.out_connections_.append(self.obj316)
      self.obj316.in_connections_.append(self.obj315)
      self.obj315.graphObject_.pendingConnections.append((self.obj315.graphObject_.tag, self.obj316.graphObject_.tag, [157.0, 122.0, 198.5, 126.5], 2, 0))
      self.obj316.out_connections_.append(self.obj314)
      self.obj314.in_connections_.append(self.obj316)
      self.obj316.graphObject_.pendingConnections.append((self.obj316.graphObject_.tag, self.obj314.graphObject_.tag, [304.0, 110.0, 198.5, 126.5], 2, 0))

   def condition(self, graphID, isograph, atom3i):
      
      raw = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      return not ( hasattr(raw, "AssignPrice" ) )
      
      

   def action(self, graphID, isograph, atom3i):
      raw = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      raw.AssignPrice=True
      print '######################## Assign Price for '+raw.Name.getValue()
      
      

