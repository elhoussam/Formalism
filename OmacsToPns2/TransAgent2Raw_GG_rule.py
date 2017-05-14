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
      GGrule.__init__(self, 9)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_omacs(parent)

      self.obj1607=Agent(parent)
      self.obj1607.preAction( self.LHS.CREATE )
      self.obj1607.isGraphObjectVisual = True

      if(hasattr(self.obj1607, '_setHierarchicalLink')):
        self.obj1607._setHierarchicalLink(False)

      # price
      self.obj1607.price.setNone()

      # name
      self.obj1607.name.setValue('')
      self.obj1607.name.setNone()

      self.obj1607.GGLabel.setValue(1)
      self.obj1607.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(100.0,20.0,self.obj1607)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1607.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1607)
      self.obj1607.postAction( self.LHS.CREATE )

      self.obj1608=Role(parent)
      self.obj1608.preAction( self.LHS.CREATE )
      self.obj1608.isGraphObjectVisual = True

      if(hasattr(self.obj1608, '_setHierarchicalLink')):
        self.obj1608._setHierarchicalLink(False)

      # name
      self.obj1608.name.setValue('')
      self.obj1608.name.setNone()

      self.obj1608.GGLabel.setValue(2)
      self.obj1608.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(360.0,160.0,self.obj1608)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1608.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1608)
      self.obj1608.postAction( self.LHS.CREATE )

      self.obj1609=CapableOf(parent)
      self.obj1609.preAction( self.LHS.CREATE )
      self.obj1609.isGraphObjectVisual = True

      if(hasattr(self.obj1609, '_setHierarchicalLink')):
        self.obj1609._setHierarchicalLink(False)

      # rate
      self.obj1609.rate.setNone()

      self.obj1609.GGLabel.setValue(3)
      self.obj1609.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(281.5,134.0,self.obj1609)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1609.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1609)
      self.obj1609.postAction( self.LHS.CREATE )

      self.obj1607.out_connections_.append(self.obj1609)
      self.obj1609.in_connections_.append(self.obj1607)
      self.obj1607.graphObject_.pendingConnections.append((self.obj1607.graphObject_.tag, self.obj1609.graphObject_.tag, [125.0, 82.0, 161.0, 153.0, 281.5, 134.0], 2, True))
      self.obj1609.out_connections_.append(self.obj1608)
      self.obj1608.in_connections_.append(self.obj1609)
      self.obj1609.graphObject_.pendingConnections.append((self.obj1609.graphObject_.tag, self.obj1608.graphObject_.tag, [384.0, 161.0, 402.0, 115.0, 281.5, 134.0], 2, True))

      self.RHS = ASG_omacs(parent)
      self.RHS.merge(ASG_pns(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj1613=Agent(parent)
      self.obj1613.preAction( self.RHS.CREATE )
      self.obj1613.isGraphObjectVisual = True

      if(hasattr(self.obj1613, '_setHierarchicalLink')):
        self.obj1613._setHierarchicalLink(False)

      # price
      self.obj1613.price.setNone()

      # name
      self.obj1613.name.setValue('')
      self.obj1613.name.setNone()

      self.obj1613.GGLabel.setValue(1)
      self.obj1613.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(100.0,20.0,self.obj1613)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1613.graphObject_ = new_obj
      self.obj16130= AttrCalc()
      self.obj16130.Copy=ATOM3Boolean()
      self.obj16130.Copy.setValue(('Copy from LHS', 1))
      self.obj16130.Copy.config = 0
      self.obj16130.Specify=ATOM3Constraint()
      self.obj16130.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1613.GGset2Any['price']= self.obj16130
      self.obj16131= AttrCalc()
      self.obj16131.Copy=ATOM3Boolean()
      self.obj16131.Copy.setValue(('Copy from LHS', 1))
      self.obj16131.Copy.config = 0
      self.obj16131.Specify=ATOM3Constraint()
      self.obj16131.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1613.GGset2Any['name']= self.obj16131

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1613)
      self.obj1613.postAction( self.RHS.CREATE )

      self.obj1614=Role(parent)
      self.obj1614.preAction( self.RHS.CREATE )
      self.obj1614.isGraphObjectVisual = True

      if(hasattr(self.obj1614, '_setHierarchicalLink')):
        self.obj1614._setHierarchicalLink(False)

      # name
      self.obj1614.name.setValue('')
      self.obj1614.name.setNone()

      self.obj1614.GGLabel.setValue(2)
      self.obj1614.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(360.0,160.0,self.obj1614)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1614.graphObject_ = new_obj
      self.obj16140= AttrCalc()
      self.obj16140.Copy=ATOM3Boolean()
      self.obj16140.Copy.setValue(('Copy from LHS', 1))
      self.obj16140.Copy.config = 0
      self.obj16140.Specify=ATOM3Constraint()
      self.obj16140.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1614.GGset2Any['name']= self.obj16140

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1614)
      self.obj1614.postAction( self.RHS.CREATE )

      self.obj1615=CapableOf(parent)
      self.obj1615.preAction( self.RHS.CREATE )
      self.obj1615.isGraphObjectVisual = True

      if(hasattr(self.obj1615, '_setHierarchicalLink')):
        self.obj1615._setHierarchicalLink(False)

      # rate
      self.obj1615.rate.setValue(0.0)

      self.obj1615.GGLabel.setValue(3)
      self.obj1615.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(281.5,134.0,self.obj1615)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1615.graphObject_ = new_obj
      self.obj16150= AttrCalc()
      self.obj16150.Copy=ATOM3Boolean()
      self.obj16150.Copy.setValue(('Copy from LHS', 1))
      self.obj16150.Copy.config = 0
      self.obj16150.Specify=ATOM3Constraint()
      self.obj16150.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1615.GGset2Any['rate']= self.obj16150

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1615)
      self.obj1615.postAction( self.RHS.CREATE )

      self.obj1616=rawMaterial(parent)
      self.obj1616.preAction( self.RHS.CREATE )
      self.obj1616.isGraphObjectVisual = True

      if(hasattr(self.obj1616, '_setHierarchicalLink')):
        self.obj1616._setHierarchicalLink(False)

      # MaxFlow
      self.obj1616.MaxFlow.setValue(999999)

      # price
      self.obj1616.price.setValue(0)

      # Name
      self.obj1616.Name.setValue('')
      self.obj1616.Name.setNone()

      # ReqFlow
      self.obj1616.ReqFlow.setValue(0)

      self.obj1616.GGLabel.setValue(6)
      self.obj1616.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(280.0,20.0,self.obj1616)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1616.graphObject_ = new_obj
      self.obj16160= AttrCalc()
      self.obj16160.Copy=ATOM3Boolean()
      self.obj16160.Copy.setValue(('Copy from LHS', 1))
      self.obj16160.Copy.config = 0
      self.obj16160.Specify=ATOM3Constraint()
      self.obj16160.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1616.GGset2Any['MaxFlow']= self.obj16160
      self.obj16161= AttrCalc()
      self.obj16161.Copy=ATOM3Boolean()
      self.obj16161.Copy.setValue(('Copy from LHS', 1))
      self.obj16161.Copy.config = 0
      self.obj16161.Specify=ATOM3Constraint()
      self.obj16161.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1616.GGset2Any['price']= self.obj16161
      self.obj16162= AttrCalc()
      self.obj16162.Copy=ATOM3Boolean()
      self.obj16162.Copy.setValue(('Copy from LHS', 0))
      self.obj16162.Copy.config = 0
      self.obj16162.Specify=ATOM3Constraint()
      self.obj16162.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()\n\n\n\n'))
      self.obj1616.GGset2Any['Name']= self.obj16162
      self.obj16163= AttrCalc()
      self.obj16163.Copy=ATOM3Boolean()
      self.obj16163.Copy.setValue(('Copy from LHS', 1))
      self.obj16163.Copy.config = 0
      self.obj16163.Specify=ATOM3Constraint()
      self.obj16163.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1616.GGset2Any['ReqFlow']= self.obj16163

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1616)
      self.obj1616.postAction( self.RHS.CREATE )

      self.obj1617=GenericGraphEdge(parent)
      self.obj1617.preAction( self.RHS.CREATE )
      self.obj1617.isGraphObjectVisual = True

      if(hasattr(self.obj1617, '_setHierarchicalLink')):
        self.obj1617._setHierarchicalLink(False)

      self.obj1617.GGLabel.setValue(7)
      self.obj1617.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(220.5,79.0,self.obj1617)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1617.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1617)
      self.obj1617.postAction( self.RHS.CREATE )

      self.obj1613.out_connections_.append(self.obj1615)
      self.obj1615.in_connections_.append(self.obj1613)
      self.obj1613.graphObject_.pendingConnections.append((self.obj1613.graphObject_.tag, self.obj1615.graphObject_.tag, [137.0, 82.0, 281.5, 134.0], 2, 0))
      self.obj1613.out_connections_.append(self.obj1617)
      self.obj1617.in_connections_.append(self.obj1613)
      self.obj1613.graphObject_.pendingConnections.append((self.obj1613.graphObject_.tag, self.obj1617.graphObject_.tag, [137.0, 82.0, 220.5, 79.0], 0, True))
      self.obj1615.out_connections_.append(self.obj1614)
      self.obj1614.in_connections_.append(self.obj1615)
      self.obj1615.graphObject_.pendingConnections.append((self.obj1615.graphObject_.tag, self.obj1614.graphObject_.tag, [391.0, 160.0, 281.5, 134.0], 2, 0))
      self.obj1617.out_connections_.append(self.obj1616)
      self.obj1616.in_connections_.append(self.obj1617)
      self.obj1617.graphObject_.pendingConnections.append((self.obj1617.graphObject_.tag, self.obj1616.graphObject_.tag, [304.0, 76.0, 220.5, 79.0], 0, True))

   def condition(self, graphID, isograph, atom3i):
      
      
      print "Dic ro "+str( self.graphRewritingSystem.Dictro )
      print "Dic ag"+str( self.graphRewritingSystem.Dictag )
      
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      
      
      return not hasattr(node, "Agent2Raw")
      
      

   def action(self, graphID, isograph, atom3i):
      node = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) )
      node.Agent2Raw = True 
      
      

