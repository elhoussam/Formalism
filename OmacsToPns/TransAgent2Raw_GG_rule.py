# _ TransAgent2Raw_GG_rule.py ____________________________________________________________________________
# File generated automatically by ATOM3. Graph Grammar Rule
# ___________________________________________________________________________________________
from GGrule import *
from CapableOf import *
from Goal import *
from require import *
from Agent import *
from Capabilitie import *
from Role import *
from ASG_omacs import *
from achieve import *
from posses import *
from GenericGraphEdge import *
from ASG_pns import *
from metarial import *
from GenericGraphNode import *
from rawMaterial import *
from fromMaterial import *
from intoProduct import *
from fromRaw import *
from ASG_GenericGraph import *
from intoMaterial import *
from product import *
from operatingUnit import *
class TransAgent2Raw_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 5)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_omacs(parent)

      self.obj134=Agent(parent)
      self.obj134.preAction( self.LHS.CREATE )
      self.obj134.isGraphObjectVisual = True

      if(hasattr(self.obj134, '_setHierarchicalLink')):
        self.obj134._setHierarchicalLink(False)

      # price
      self.obj134.price.setNone()

      # name
      self.obj134.name.setValue('')
      self.obj134.name.setNone()

      self.obj134.GGLabel.setValue(1)
      self.obj134.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(100.0,20.0,self.obj134)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj134.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj134)
      self.obj134.postAction( self.LHS.CREATE )

      self.obj135=Role(parent)
      self.obj135.preAction( self.LHS.CREATE )
      self.obj135.isGraphObjectVisual = True

      if(hasattr(self.obj135, '_setHierarchicalLink')):
        self.obj135._setHierarchicalLink(False)

      # name
      self.obj135.name.setValue('')
      self.obj135.name.setNone()

      self.obj135.GGLabel.setValue(2)
      self.obj135.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(360.0,160.0,self.obj135)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj135.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj135)
      self.obj135.postAction( self.LHS.CREATE )

      self.obj136=CapableOf(parent)
      self.obj136.preAction( self.LHS.CREATE )
      self.obj136.isGraphObjectVisual = True

      if(hasattr(self.obj136, '_setHierarchicalLink')):
        self.obj136._setHierarchicalLink(False)

      # rate
      self.obj136.rate.setNone()

      self.obj136.GGLabel.setValue(3)
      self.obj136.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(281.5,134.0,self.obj136)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj136.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj136)
      self.obj136.postAction( self.LHS.CREATE )

      self.obj134.out_connections_.append(self.obj136)
      self.obj136.in_connections_.append(self.obj134)
      self.obj134.graphObject_.pendingConnections.append((self.obj134.graphObject_.tag, self.obj136.graphObject_.tag, [125.0, 82.0, 161.0, 153.0, 281.5, 134.0], 2, True))
      self.obj136.out_connections_.append(self.obj135)
      self.obj135.in_connections_.append(self.obj136)
      self.obj136.graphObject_.pendingConnections.append((self.obj136.graphObject_.tag, self.obj135.graphObject_.tag, [384.0, 161.0, 402.0, 115.0, 281.5, 134.0], 2, True))

      self.RHS = ASG_omacs(parent)
      self.RHS.merge(ASG_pns(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj140=Agent(parent)
      self.obj140.preAction( self.RHS.CREATE )
      self.obj140.isGraphObjectVisual = True

      if(hasattr(self.obj140, '_setHierarchicalLink')):
        self.obj140._setHierarchicalLink(False)

      # price
      self.obj140.price.setNone()

      # name
      self.obj140.name.setValue('')
      self.obj140.name.setNone()

      self.obj140.GGLabel.setValue(1)
      self.obj140.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(100.0,20.0,self.obj140)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj140.graphObject_ = new_obj
      self.obj1400= AttrCalc()
      self.obj1400.Copy=ATOM3Boolean()
      self.obj1400.Copy.setValue(('Copy from LHS', 1))
      self.obj1400.Copy.config = 0
      self.obj1400.Specify=ATOM3Constraint()
      self.obj1400.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj140.GGset2Any['price']= self.obj1400
      self.obj1401= AttrCalc()
      self.obj1401.Copy=ATOM3Boolean()
      self.obj1401.Copy.setValue(('Copy from LHS', 1))
      self.obj1401.Copy.config = 0
      self.obj1401.Specify=ATOM3Constraint()
      self.obj1401.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj140.GGset2Any['name']= self.obj1401

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj140)
      self.obj140.postAction( self.RHS.CREATE )

      self.obj141=Role(parent)
      self.obj141.preAction( self.RHS.CREATE )
      self.obj141.isGraphObjectVisual = True

      if(hasattr(self.obj141, '_setHierarchicalLink')):
        self.obj141._setHierarchicalLink(False)

      # name
      self.obj141.name.setValue('')
      self.obj141.name.setNone()

      self.obj141.GGLabel.setValue(2)
      self.obj141.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(360.0,160.0,self.obj141)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj141.graphObject_ = new_obj
      self.obj1410= AttrCalc()
      self.obj1410.Copy=ATOM3Boolean()
      self.obj1410.Copy.setValue(('Copy from LHS', 1))
      self.obj1410.Copy.config = 0
      self.obj1410.Specify=ATOM3Constraint()
      self.obj1410.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj141.GGset2Any['name']= self.obj1410

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj141)
      self.obj141.postAction( self.RHS.CREATE )

      self.obj142=CapableOf(parent)
      self.obj142.preAction( self.RHS.CREATE )
      self.obj142.isGraphObjectVisual = True

      if(hasattr(self.obj142, '_setHierarchicalLink')):
        self.obj142._setHierarchicalLink(False)

      # rate
      self.obj142.rate.setValue(0.0)

      self.obj142.GGLabel.setValue(3)
      self.obj142.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(281.5,134.0,self.obj142)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj142.graphObject_ = new_obj
      self.obj1420= AttrCalc()
      self.obj1420.Copy=ATOM3Boolean()
      self.obj1420.Copy.setValue(('Copy from LHS', 1))
      self.obj1420.Copy.config = 0
      self.obj1420.Specify=ATOM3Constraint()
      self.obj1420.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj142.GGset2Any['rate']= self.obj1420

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj142)
      self.obj142.postAction( self.RHS.CREATE )

      self.obj143=rawMaterial(parent)
      self.obj143.preAction( self.RHS.CREATE )
      self.obj143.isGraphObjectVisual = True

      if(hasattr(self.obj143, '_setHierarchicalLink')):
        self.obj143._setHierarchicalLink(False)

      # MaxFlow
      self.obj143.MaxFlow.setValue(999999)

      # price
      self.obj143.price.setValue(0)

      # Name
      self.obj143.Name.setValue('')
      self.obj143.Name.setNone()

      # ReqFlow
      self.obj143.ReqFlow.setValue(0)

      self.obj143.GGLabel.setValue(6)
      self.obj143.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(280.0,20.0,self.obj143)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj143.graphObject_ = new_obj
      self.obj1430= AttrCalc()
      self.obj1430.Copy=ATOM3Boolean()
      self.obj1430.Copy.setValue(('Copy from LHS', 1))
      self.obj1430.Copy.config = 0
      self.obj1430.Specify=ATOM3Constraint()
      self.obj1430.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj143.GGset2Any['MaxFlow']= self.obj1430
      self.obj1431= AttrCalc()
      self.obj1431.Copy=ATOM3Boolean()
      self.obj1431.Copy.setValue(('Copy from LHS', 1))
      self.obj1431.Copy.config = 0
      self.obj1431.Specify=ATOM3Constraint()
      self.obj1431.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj143.GGset2Any['price']= self.obj1431
      self.obj1432= AttrCalc()
      self.obj1432.Copy=ATOM3Boolean()
      self.obj1432.Copy.setValue(('Copy from LHS', 0))
      self.obj1432.Copy.config = 0
      self.obj1432.Specify=ATOM3Constraint()
      self.obj1432.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()\n\n\n\n'))
      self.obj143.GGset2Any['Name']= self.obj1432
      self.obj1433= AttrCalc()
      self.obj1433.Copy=ATOM3Boolean()
      self.obj1433.Copy.setValue(('Copy from LHS', 1))
      self.obj1433.Copy.config = 0
      self.obj1433.Specify=ATOM3Constraint()
      self.obj1433.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj143.GGset2Any['ReqFlow']= self.obj1433

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj143)
      self.obj143.postAction( self.RHS.CREATE )

      self.obj144=GenericGraphEdge(parent)
      self.obj144.preAction( self.RHS.CREATE )
      self.obj144.isGraphObjectVisual = True

      if(hasattr(self.obj144, '_setHierarchicalLink')):
        self.obj144._setHierarchicalLink(False)

      self.obj144.GGLabel.setValue(7)
      self.obj144.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(220.5,79.0,self.obj144)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj144.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj144)
      self.obj144.postAction( self.RHS.CREATE )

      self.obj140.out_connections_.append(self.obj142)
      self.obj142.in_connections_.append(self.obj140)
      self.obj140.graphObject_.pendingConnections.append((self.obj140.graphObject_.tag, self.obj142.graphObject_.tag, [137.0, 82.0, 281.5, 134.0], 2, 0))
      self.obj140.out_connections_.append(self.obj144)
      self.obj144.in_connections_.append(self.obj140)
      self.obj140.graphObject_.pendingConnections.append((self.obj140.graphObject_.tag, self.obj144.graphObject_.tag, [137.0, 82.0, 220.5, 79.0], 0, True))
      self.obj142.out_connections_.append(self.obj141)
      self.obj141.in_connections_.append(self.obj142)
      self.obj142.graphObject_.pendingConnections.append((self.obj142.graphObject_.tag, self.obj141.graphObject_.tag, [391.0, 160.0, 281.5, 134.0], 2, 0))
      self.obj144.out_connections_.append(self.obj143)
      self.obj143.in_connections_.append(self.obj144)
      self.obj144.graphObject_.pendingConnections.append((self.obj144.graphObject_.tag, self.obj143.graphObject_.tag, [304.0, 76.0, 220.5, 79.0], 0, True))

   def condition(self, graphID, isograph, atom3i):
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      return not hasattr(node, "Agent2Raw")
      
      

   def action(self, graphID, isograph, atom3i):
      node = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) )
      node.Agent2Raw = True 
      
      

