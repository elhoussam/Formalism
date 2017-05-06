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

      self.obj606=Agent(parent)
      self.obj606.preAction( self.LHS.CREATE )
      self.obj606.isGraphObjectVisual = True

      if(hasattr(self.obj606, '_setHierarchicalLink')):
        self.obj606._setHierarchicalLink(False)

      # price
      self.obj606.price.setNone()

      # name
      self.obj606.name.setValue('')
      self.obj606.name.setNone()

      self.obj606.GGLabel.setValue(1)
      self.obj606.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(100.0,20.0,self.obj606)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj606.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj606)
      self.obj606.postAction( self.LHS.CREATE )

      self.obj607=Role(parent)
      self.obj607.preAction( self.LHS.CREATE )
      self.obj607.isGraphObjectVisual = True

      if(hasattr(self.obj607, '_setHierarchicalLink')):
        self.obj607._setHierarchicalLink(False)

      # name
      self.obj607.name.setValue('')
      self.obj607.name.setNone()

      self.obj607.GGLabel.setValue(2)
      self.obj607.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(360.0,160.0,self.obj607)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj607.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj607)
      self.obj607.postAction( self.LHS.CREATE )

      self.obj608=CapableOf(parent)
      self.obj608.preAction( self.LHS.CREATE )
      self.obj608.isGraphObjectVisual = True

      if(hasattr(self.obj608, '_setHierarchicalLink')):
        self.obj608._setHierarchicalLink(False)

      # rate
      self.obj608.rate.setNone()

      self.obj608.GGLabel.setValue(3)
      self.obj608.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(281.5,134.0,self.obj608)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj608.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj608)
      self.obj608.postAction( self.LHS.CREATE )

      self.obj606.out_connections_.append(self.obj608)
      self.obj608.in_connections_.append(self.obj606)
      self.obj606.graphObject_.pendingConnections.append((self.obj606.graphObject_.tag, self.obj608.graphObject_.tag, [125.0, 82.0, 161.0, 153.0, 281.5, 134.0], 2, True))
      self.obj608.out_connections_.append(self.obj607)
      self.obj607.in_connections_.append(self.obj608)
      self.obj608.graphObject_.pendingConnections.append((self.obj608.graphObject_.tag, self.obj607.graphObject_.tag, [384.0, 161.0, 402.0, 115.0, 281.5, 134.0], 2, True))

      self.RHS = ASG_omacs(parent)
      self.RHS.merge(ASG_pns(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj612=Agent(parent)
      self.obj612.preAction( self.RHS.CREATE )
      self.obj612.isGraphObjectVisual = True

      if(hasattr(self.obj612, '_setHierarchicalLink')):
        self.obj612._setHierarchicalLink(False)

      # price
      self.obj612.price.setNone()

      # name
      self.obj612.name.setValue('')
      self.obj612.name.setNone()

      self.obj612.GGLabel.setValue(1)
      self.obj612.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(100.0,20.0,self.obj612)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj612.graphObject_ = new_obj
      self.obj6120= AttrCalc()
      self.obj6120.Copy=ATOM3Boolean()
      self.obj6120.Copy.setValue(('Copy from LHS', 1))
      self.obj6120.Copy.config = 0
      self.obj6120.Specify=ATOM3Constraint()
      self.obj6120.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj612.GGset2Any['price']= self.obj6120
      self.obj6121= AttrCalc()
      self.obj6121.Copy=ATOM3Boolean()
      self.obj6121.Copy.setValue(('Copy from LHS', 1))
      self.obj6121.Copy.config = 0
      self.obj6121.Specify=ATOM3Constraint()
      self.obj6121.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj612.GGset2Any['name']= self.obj6121

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj612)
      self.obj612.postAction( self.RHS.CREATE )

      self.obj613=Role(parent)
      self.obj613.preAction( self.RHS.CREATE )
      self.obj613.isGraphObjectVisual = True

      if(hasattr(self.obj613, '_setHierarchicalLink')):
        self.obj613._setHierarchicalLink(False)

      # name
      self.obj613.name.setValue('')
      self.obj613.name.setNone()

      self.obj613.GGLabel.setValue(2)
      self.obj613.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(360.0,160.0,self.obj613)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj613.graphObject_ = new_obj
      self.obj6130= AttrCalc()
      self.obj6130.Copy=ATOM3Boolean()
      self.obj6130.Copy.setValue(('Copy from LHS', 1))
      self.obj6130.Copy.config = 0
      self.obj6130.Specify=ATOM3Constraint()
      self.obj6130.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj613.GGset2Any['name']= self.obj6130

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj613)
      self.obj613.postAction( self.RHS.CREATE )

      self.obj614=CapableOf(parent)
      self.obj614.preAction( self.RHS.CREATE )
      self.obj614.isGraphObjectVisual = True

      if(hasattr(self.obj614, '_setHierarchicalLink')):
        self.obj614._setHierarchicalLink(False)

      # rate
      self.obj614.rate.setValue(0.0)

      self.obj614.GGLabel.setValue(3)
      self.obj614.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(281.5,134.0,self.obj614)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj614.graphObject_ = new_obj
      self.obj6140= AttrCalc()
      self.obj6140.Copy=ATOM3Boolean()
      self.obj6140.Copy.setValue(('Copy from LHS', 1))
      self.obj6140.Copy.config = 0
      self.obj6140.Specify=ATOM3Constraint()
      self.obj6140.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj614.GGset2Any['rate']= self.obj6140

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj614)
      self.obj614.postAction( self.RHS.CREATE )

      self.obj615=rawMaterial(parent)
      self.obj615.preAction( self.RHS.CREATE )
      self.obj615.isGraphObjectVisual = True

      if(hasattr(self.obj615, '_setHierarchicalLink')):
        self.obj615._setHierarchicalLink(False)

      # MaxFlow
      self.obj615.MaxFlow.setValue(999999)

      # price
      self.obj615.price.setValue(0)

      # Name
      self.obj615.Name.setValue('')
      self.obj615.Name.setNone()

      # ReqFlow
      self.obj615.ReqFlow.setValue(0)

      self.obj615.GGLabel.setValue(6)
      self.obj615.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(280.0,20.0,self.obj615)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj615.graphObject_ = new_obj
      self.obj6150= AttrCalc()
      self.obj6150.Copy=ATOM3Boolean()
      self.obj6150.Copy.setValue(('Copy from LHS', 1))
      self.obj6150.Copy.config = 0
      self.obj6150.Specify=ATOM3Constraint()
      self.obj6150.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj615.GGset2Any['MaxFlow']= self.obj6150
      self.obj6151= AttrCalc()
      self.obj6151.Copy=ATOM3Boolean()
      self.obj6151.Copy.setValue(('Copy from LHS', 1))
      self.obj6151.Copy.config = 0
      self.obj6151.Specify=ATOM3Constraint()
      self.obj6151.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj615.GGset2Any['price']= self.obj6151
      self.obj6152= AttrCalc()
      self.obj6152.Copy=ATOM3Boolean()
      self.obj6152.Copy.setValue(('Copy from LHS', 0))
      self.obj6152.Copy.config = 0
      self.obj6152.Specify=ATOM3Constraint()
      self.obj6152.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()\n\n\n\n'))
      self.obj615.GGset2Any['Name']= self.obj6152
      self.obj6153= AttrCalc()
      self.obj6153.Copy=ATOM3Boolean()
      self.obj6153.Copy.setValue(('Copy from LHS', 1))
      self.obj6153.Copy.config = 0
      self.obj6153.Specify=ATOM3Constraint()
      self.obj6153.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj615.GGset2Any['ReqFlow']= self.obj6153

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj615)
      self.obj615.postAction( self.RHS.CREATE )

      self.obj616=GenericGraphEdge(parent)
      self.obj616.preAction( self.RHS.CREATE )
      self.obj616.isGraphObjectVisual = True

      if(hasattr(self.obj616, '_setHierarchicalLink')):
        self.obj616._setHierarchicalLink(False)

      self.obj616.GGLabel.setValue(7)
      self.obj616.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(220.5,79.0,self.obj616)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj616.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj616)
      self.obj616.postAction( self.RHS.CREATE )

      self.obj612.out_connections_.append(self.obj614)
      self.obj614.in_connections_.append(self.obj612)
      self.obj612.graphObject_.pendingConnections.append((self.obj612.graphObject_.tag, self.obj614.graphObject_.tag, [137.0, 82.0, 281.5, 134.0], 2, 0))
      self.obj612.out_connections_.append(self.obj616)
      self.obj616.in_connections_.append(self.obj612)
      self.obj612.graphObject_.pendingConnections.append((self.obj612.graphObject_.tag, self.obj616.graphObject_.tag, [137.0, 82.0, 220.5, 79.0], 0, True))
      self.obj614.out_connections_.append(self.obj613)
      self.obj613.in_connections_.append(self.obj614)
      self.obj614.graphObject_.pendingConnections.append((self.obj614.graphObject_.tag, self.obj613.graphObject_.tag, [391.0, 160.0, 281.5, 134.0], 2, 0))
      self.obj616.out_connections_.append(self.obj615)
      self.obj615.in_connections_.append(self.obj616)
      self.obj616.graphObject_.pendingConnections.append((self.obj616.graphObject_.tag, self.obj615.graphObject_.tag, [304.0, 76.0, 220.5, 79.0], 0, True))

   def condition(self, graphID, isograph, atom3i):
      
      
      print "Dic ro "+str( self.graphRewritingSystem.Dictro )
      print "Dic ag"+str( self.graphRewritingSystem.Dictag )
      
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      
      
      return not hasattr(node, "Agent2Raw")
      
      

   def action(self, graphID, isograph, atom3i):
      node = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) )
      node.Agent2Raw = True 
      
      

