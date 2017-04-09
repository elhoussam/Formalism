# _ AssignCost4AR_GG_rule.py ____________________________________________________________________________
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
class AssignCost4AR_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 23)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_pns(parent)
      self.LHS.merge(ASG_omacs(parent))
      self.LHS.merge(ASG_GenericGraph(parent))

      self.obj323=operatingUnit(parent)
      self.obj323.preAction( self.LHS.CREATE )
      self.obj323.isGraphObjectVisual = True

      if(hasattr(self.obj323, '_setHierarchicalLink')):
        self.obj323._setHierarchicalLink(False)

      # OperCostProp
      self.obj323.OperCostProp.setNone()

      # name
      self.obj323.name.setValue('')
      self.obj323.name.setNone()

      # OperCostFix
      self.obj323.OperCostFix.setNone()

      self.obj323.GGLabel.setValue(4)
      self.obj323.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(280.0,120.0,self.obj323)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj323.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj323)
      self.obj323.postAction( self.LHS.CREATE )

      self.obj324=CapableOf(parent)
      self.obj324.preAction( self.LHS.CREATE )
      self.obj324.isGraphObjectVisual = True

      if(hasattr(self.obj324, '_setHierarchicalLink')):
        self.obj324._setHierarchicalLink(False)

      # rate
      self.obj324.rate.setNone()

      self.obj324.GGLabel.setValue(5)
      self.obj324.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(160.5,121.5,self.obj324)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj324.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj324)
      self.obj324.postAction( self.LHS.CREATE )

      self.obj325=Agent(parent)
      self.obj325.preAction( self.LHS.CREATE )
      self.obj325.isGraphObjectVisual = True

      if(hasattr(self.obj325, '_setHierarchicalLink')):
        self.obj325._setHierarchicalLink(False)

      # price
      self.obj325.price.setNone()

      # name
      self.obj325.name.setValue('')
      self.obj325.name.setNone()

      self.obj325.GGLabel.setValue(1)
      self.obj325.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(120.0,40.0,self.obj325)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj325.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj325)
      self.obj325.postAction( self.LHS.CREATE )

      self.obj326=Role(parent)
      self.obj326.preAction( self.LHS.CREATE )
      self.obj326.isGraphObjectVisual = True

      if(hasattr(self.obj326, '_setHierarchicalLink')):
        self.obj326._setHierarchicalLink(False)

      # name
      self.obj326.name.setValue('')
      self.obj326.name.setNone()

      self.obj326.GGLabel.setValue(2)
      self.obj326.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(140.0,140.0,self.obj326)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj326.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj326)
      self.obj326.postAction( self.LHS.CREATE )

      self.obj327=GenericGraphEdge(parent)
      self.obj327.preAction( self.LHS.CREATE )
      self.obj327.isGraphObjectVisual = True

      if(hasattr(self.obj327, '_setHierarchicalLink')):
        self.obj327._setHierarchicalLink(False)

      self.obj327.GGLabel.setValue(3)
      self.obj327.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(264.75,85.25,self.obj327)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj327.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj327)
      self.obj327.postAction( self.LHS.CREATE )

      self.obj324.out_connections_.append(self.obj326)
      self.obj326.in_connections_.append(self.obj324)
      self.obj324.graphObject_.pendingConnections.append((self.obj324.graphObject_.tag, self.obj326.graphObject_.tag, [164.0, 141.0, 160.5, 121.5], 0, True))
      self.obj325.out_connections_.append(self.obj327)
      self.obj327.in_connections_.append(self.obj325)
      self.obj325.graphObject_.pendingConnections.append((self.obj325.graphObject_.tag, self.obj327.graphObject_.tag, [145.0, 102.0, 226.0, 83.0, 264.75, 85.25], 2, True))
      self.obj325.out_connections_.append(self.obj324)
      self.obj324.in_connections_.append(self.obj325)
      self.obj325.graphObject_.pendingConnections.append((self.obj325.graphObject_.tag, self.obj324.graphObject_.tag, [157.0, 102.0, 160.5, 121.5], 0, True))
      self.obj327.out_connections_.append(self.obj323)
      self.obj323.in_connections_.append(self.obj327)
      self.obj327.graphObject_.pendingConnections.append((self.obj327.graphObject_.tag, self.obj323.graphObject_.tag, [300.0, 121.0, 264.75, 85.25], 2, 0))

      self.RHS = ASG_pns(parent)
      self.RHS.merge(ASG_omacs(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj331=operatingUnit(parent)
      self.obj331.preAction( self.RHS.CREATE )
      self.obj331.isGraphObjectVisual = True

      if(hasattr(self.obj331, '_setHierarchicalLink')):
        self.obj331._setHierarchicalLink(False)

      # OperCostProp
      self.obj331.OperCostProp.setNone()

      # name
      self.obj331.name.setValue('')
      self.obj331.name.setNone()

      # OperCostFix
      self.obj331.OperCostFix.setNone()

      self.obj331.GGLabel.setValue(4)
      self.obj331.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(280.0,120.0,self.obj331)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj331.graphObject_ = new_obj
      self.obj3310= AttrCalc()
      self.obj3310.Copy=ATOM3Boolean()
      self.obj3310.Copy.setValue(('Copy from LHS', 0))
      self.obj3310.Copy.config = 0
      self.obj3310.Specify=ATOM3Constraint()
      self.obj3310.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'a = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) ).name.getValue()\nb = self.getMatched ( graphID , self.LHS.nodeWithLabel(2) ).name.getValue()\nreturn self.graphRewritingSystem.Dictag[ a ][b]\n\n'))
      self.obj331.GGset2Any['OperCostProp']= self.obj3310
      self.obj3311= AttrCalc()
      self.obj3311.Copy=ATOM3Boolean()
      self.obj3311.Copy.setValue(('Copy from LHS', 1))
      self.obj3311.Copy.config = 0
      self.obj3311.Specify=ATOM3Constraint()
      self.obj3311.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj331.GGset2Any['name']= self.obj3311
      self.obj3312= AttrCalc()
      self.obj3312.Copy=ATOM3Boolean()
      self.obj3312.Copy.setValue(('Copy from LHS', 0))
      self.obj3312.Copy.config = 0
      self.obj3312.Specify=ATOM3Constraint()
      self.obj3312.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj331.GGset2Any['OperCostFix']= self.obj3312

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj331)
      self.obj331.postAction( self.RHS.CREATE )

      self.obj332=CapableOf(parent)
      self.obj332.preAction( self.RHS.CREATE )
      self.obj332.isGraphObjectVisual = True

      if(hasattr(self.obj332, '_setHierarchicalLink')):
        self.obj332._setHierarchicalLink(False)

      # rate
      self.obj332.rate.setNone()

      self.obj332.GGLabel.setValue(5)
      self.obj332.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(160.5,121.5,self.obj332)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj332.graphObject_ = new_obj
      self.obj3320= AttrCalc()
      self.obj3320.Copy=ATOM3Boolean()
      self.obj3320.Copy.setValue(('Copy from LHS', 1))
      self.obj3320.Copy.config = 0
      self.obj3320.Specify=ATOM3Constraint()
      self.obj3320.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj332.GGset2Any['rate']= self.obj3320

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj332)
      self.obj332.postAction( self.RHS.CREATE )

      self.obj333=Agent(parent)
      self.obj333.preAction( self.RHS.CREATE )
      self.obj333.isGraphObjectVisual = True

      if(hasattr(self.obj333, '_setHierarchicalLink')):
        self.obj333._setHierarchicalLink(False)

      # price
      self.obj333.price.setNone()

      # name
      self.obj333.name.setValue('')
      self.obj333.name.setNone()

      self.obj333.GGLabel.setValue(1)
      self.obj333.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(120.0,40.0,self.obj333)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj333.graphObject_ = new_obj
      self.obj3330= AttrCalc()
      self.obj3330.Copy=ATOM3Boolean()
      self.obj3330.Copy.setValue(('Copy from LHS', 1))
      self.obj3330.Copy.config = 0
      self.obj3330.Specify=ATOM3Constraint()
      self.obj3330.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj333.GGset2Any['price']= self.obj3330
      self.obj3331= AttrCalc()
      self.obj3331.Copy=ATOM3Boolean()
      self.obj3331.Copy.setValue(('Copy from LHS', 1))
      self.obj3331.Copy.config = 0
      self.obj3331.Specify=ATOM3Constraint()
      self.obj3331.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj333.GGset2Any['name']= self.obj3331

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj333)
      self.obj333.postAction( self.RHS.CREATE )

      self.obj334=Role(parent)
      self.obj334.preAction( self.RHS.CREATE )
      self.obj334.isGraphObjectVisual = True

      if(hasattr(self.obj334, '_setHierarchicalLink')):
        self.obj334._setHierarchicalLink(False)

      # name
      self.obj334.name.setValue('')
      self.obj334.name.setNone()

      self.obj334.GGLabel.setValue(2)
      self.obj334.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(140.0,140.0,self.obj334)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj334.graphObject_ = new_obj
      self.obj3340= AttrCalc()
      self.obj3340.Copy=ATOM3Boolean()
      self.obj3340.Copy.setValue(('Copy from LHS', 1))
      self.obj3340.Copy.config = 0
      self.obj3340.Specify=ATOM3Constraint()
      self.obj3340.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj334.GGset2Any['name']= self.obj3340

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj334)
      self.obj334.postAction( self.RHS.CREATE )

      self.obj335=GenericGraphEdge(parent)
      self.obj335.preAction( self.RHS.CREATE )
      self.obj335.isGraphObjectVisual = True

      if(hasattr(self.obj335, '_setHierarchicalLink')):
        self.obj335._setHierarchicalLink(False)

      self.obj335.GGLabel.setValue(3)
      self.obj335.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(264.75,85.25,self.obj335)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj335.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj335)
      self.obj335.postAction( self.RHS.CREATE )

      self.obj332.out_connections_.append(self.obj334)
      self.obj334.in_connections_.append(self.obj332)
      self.obj332.graphObject_.pendingConnections.append((self.obj332.graphObject_.tag, self.obj334.graphObject_.tag, [171.0, 140.0, 160.5, 121.5], 2, 0))
      self.obj333.out_connections_.append(self.obj335)
      self.obj335.in_connections_.append(self.obj333)
      self.obj333.graphObject_.pendingConnections.append((self.obj333.graphObject_.tag, self.obj335.graphObject_.tag, [157.0, 102.0, 264.75, 85.25], 2, 0))
      self.obj333.out_connections_.append(self.obj332)
      self.obj332.in_connections_.append(self.obj333)
      self.obj333.graphObject_.pendingConnections.append((self.obj333.graphObject_.tag, self.obj332.graphObject_.tag, [157.0, 102.0, 160.5, 121.5], 2, 0))
      self.obj335.out_connections_.append(self.obj331)
      self.obj331.in_connections_.append(self.obj335)
      self.obj335.graphObject_.pendingConnections.append((self.obj335.graphObject_.tag, self.obj331.graphObject_.tag, [300.0, 121.0, 264.75, 85.25], 2, 0))

   def condition(self, graphID, isograph, atom3i):
      AR = self.getMatched(graphID, self.LHS.nodeWithLabel(4))
      return not ( hasattr(AR, "AssignCost" ) )
      
      

   def action(self, graphID, isograph, atom3i):
      AR = self.getMatched(graphID, self.LHS.nodeWithLabel(4))
      AR.AssignCost=True
      print '######################## Assign Cost for '+AR.name.getValue()
      
      

