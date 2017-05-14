# _ RemoveRole_GG_rule.py ____________________________________________________________________________
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
class RemoveRole_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 28)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_pns(parent)
      self.LHS.merge(ASG_omacs(parent))
      self.LHS.merge(ASG_GenericGraph(parent))

      self.obj1849=metarial(parent)
      self.obj1849.preAction( self.LHS.CREATE )
      self.obj1849.isGraphObjectVisual = True

      if(hasattr(self.obj1849, '_setHierarchicalLink')):
        self.obj1849._setHierarchicalLink(False)

      # MaxFlow
      self.obj1849.MaxFlow.setNone()

      # price
      self.obj1849.price.setValue(0)

      # Name
      self.obj1849.Name.setValue('')
      self.obj1849.Name.setNone()

      # ReqFlow
      self.obj1849.ReqFlow.setNone()

      self.obj1849.GGLabel.setValue(2)
      self.obj1849.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(280.0,40.0,self.obj1849)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1849.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1849)
      self.obj1849.postAction( self.LHS.CREATE )

      self.obj1850=operatingUnit(parent)
      self.obj1850.preAction( self.LHS.CREATE )
      self.obj1850.isGraphObjectVisual = True

      if(hasattr(self.obj1850, '_setHierarchicalLink')):
        self.obj1850._setHierarchicalLink(False)

      # OperCostProp
      self.obj1850.OperCostProp.setNone()

      # name
      self.obj1850.name.setValue('')
      self.obj1850.name.setNone()

      # OperCostFix
      self.obj1850.OperCostFix.setNone()

      self.obj1850.GGLabel.setValue(3)
      self.obj1850.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(300.0,140.0,self.obj1850)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1850.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1850)
      self.obj1850.postAction( self.LHS.CREATE )

      self.obj1851=fromMaterial(parent)
      self.obj1851.preAction( self.LHS.CREATE )
      self.obj1851.isGraphObjectVisual = True

      if(hasattr(self.obj1851, '_setHierarchicalLink')):
        self.obj1851._setHierarchicalLink(False)

      # rate
      self.obj1851.rate.setNone()

      self.obj1851.GGLabel.setValue(4)
      self.obj1851.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(342.75,113.75,self.obj1851)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1851.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1851)
      self.obj1851.postAction( self.LHS.CREATE )

      self.obj1852=Role(parent)
      self.obj1852.preAction( self.LHS.CREATE )
      self.obj1852.isGraphObjectVisual = True

      if(hasattr(self.obj1852, '_setHierarchicalLink')):
        self.obj1852._setHierarchicalLink(False)

      # name
      self.obj1852.name.setValue('')
      self.obj1852.name.setNone()

      self.obj1852.GGLabel.setValue(1)
      self.obj1852.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(80.0,60.0,self.obj1852)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1852.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1852)
      self.obj1852.postAction( self.LHS.CREATE )

      self.obj1853=GenericGraphEdge(parent)
      self.obj1853.preAction( self.LHS.CREATE )
      self.obj1853.isGraphObjectVisual = True

      if(hasattr(self.obj1853, '_setHierarchicalLink')):
        self.obj1853._setHierarchicalLink(False)

      self.obj1853.GGLabel.setValue(5)
      self.obj1853.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(195.0,71.5,self.obj1853)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1853.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1853)
      self.obj1853.postAction( self.LHS.CREATE )

      self.obj1849.out_connections_.append(self.obj1851)
      self.obj1851.in_connections_.append(self.obj1849)
      self.obj1849.graphObject_.pendingConnections.append((self.obj1849.graphObject_.tag, self.obj1851.graphObject_.tag, [321.0, 82.0, 335.5, 96.5, 342.75, 113.75], 2, True))
      self.obj1851.out_connections_.append(self.obj1850)
      self.obj1850.in_connections_.append(self.obj1851)
      self.obj1851.graphObject_.pendingConnections.append((self.obj1851.graphObject_.tag, self.obj1850.graphObject_.tag, [350.0, 151.0, 350.0, 131.0, 342.75, 113.75], 2, True))
      self.obj1852.out_connections_.append(self.obj1853)
      self.obj1853.in_connections_.append(self.obj1852)
      self.obj1852.graphObject_.pendingConnections.append((self.obj1852.graphObject_.tag, self.obj1853.graphObject_.tag, [104.0, 61.0, 195.0, 71.5], 0, True))
      self.obj1853.out_connections_.append(self.obj1849)
      self.obj1849.in_connections_.append(self.obj1853)
      self.obj1853.graphObject_.pendingConnections.append((self.obj1853.graphObject_.tag, self.obj1849.graphObject_.tag, [286.0, 82.0, 195.0, 71.5], 0, True))

      self.RHS = ASG_pns(parent)

      self.obj1855=metarial(parent)
      self.obj1855.preAction( self.RHS.CREATE )
      self.obj1855.isGraphObjectVisual = True

      if(hasattr(self.obj1855, '_setHierarchicalLink')):
        self.obj1855._setHierarchicalLink(False)

      # MaxFlow
      self.obj1855.MaxFlow.setValue(999999)

      # price
      self.obj1855.price.setValue(0)

      # Name
      self.obj1855.Name.setValue('')
      self.obj1855.Name.setNone()

      # ReqFlow
      self.obj1855.ReqFlow.setValue(0)

      self.obj1855.GGLabel.setValue(2)
      self.obj1855.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(160.0,40.0,self.obj1855)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1855.graphObject_ = new_obj
      self.obj18550= AttrCalc()
      self.obj18550.Copy=ATOM3Boolean()
      self.obj18550.Copy.setValue(('Copy from LHS', 1))
      self.obj18550.Copy.config = 0
      self.obj18550.Specify=ATOM3Constraint()
      self.obj18550.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1855.GGset2Any['MaxFlow']= self.obj18550
      self.obj18551= AttrCalc()
      self.obj18551.Copy=ATOM3Boolean()
      self.obj18551.Copy.setValue(('Copy from LHS', 1))
      self.obj18551.Copy.config = 0
      self.obj18551.Specify=ATOM3Constraint()
      self.obj18551.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1855.GGset2Any['Name']= self.obj18551
      self.obj18552= AttrCalc()
      self.obj18552.Copy=ATOM3Boolean()
      self.obj18552.Copy.setValue(('Copy from LHS', 1))
      self.obj18552.Copy.config = 0
      self.obj18552.Specify=ATOM3Constraint()
      self.obj18552.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1855.GGset2Any['ReqFlow']= self.obj18552

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1855)
      self.obj1855.postAction( self.RHS.CREATE )

      self.obj1856=operatingUnit(parent)
      self.obj1856.preAction( self.RHS.CREATE )
      self.obj1856.isGraphObjectVisual = True

      if(hasattr(self.obj1856, '_setHierarchicalLink')):
        self.obj1856._setHierarchicalLink(False)

      # OperCostProp
      self.obj1856.OperCostProp.setValue(0.0)

      # name
      self.obj1856.name.setValue('')
      self.obj1856.name.setNone()

      # OperCostFix
      self.obj1856.OperCostFix.setValue(0.0)

      self.obj1856.GGLabel.setValue(3)
      self.obj1856.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(200.0,140.0,self.obj1856)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1856.graphObject_ = new_obj
      self.obj18560= AttrCalc()
      self.obj18560.Copy=ATOM3Boolean()
      self.obj18560.Copy.setValue(('Copy from LHS', 1))
      self.obj18560.Copy.config = 0
      self.obj18560.Specify=ATOM3Constraint()
      self.obj18560.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1856.GGset2Any['OperCostProp']= self.obj18560
      self.obj18561= AttrCalc()
      self.obj18561.Copy=ATOM3Boolean()
      self.obj18561.Copy.setValue(('Copy from LHS', 1))
      self.obj18561.Copy.config = 0
      self.obj18561.Specify=ATOM3Constraint()
      self.obj18561.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1856.GGset2Any['name']= self.obj18561
      self.obj18562= AttrCalc()
      self.obj18562.Copy=ATOM3Boolean()
      self.obj18562.Copy.setValue(('Copy from LHS', 1))
      self.obj18562.Copy.config = 0
      self.obj18562.Specify=ATOM3Constraint()
      self.obj18562.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1856.GGset2Any['OperCostFix']= self.obj18562

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1856)
      self.obj1856.postAction( self.RHS.CREATE )

      self.obj1857=fromMaterial(parent)
      self.obj1857.preAction( self.RHS.CREATE )
      self.obj1857.isGraphObjectVisual = True

      if(hasattr(self.obj1857, '_setHierarchicalLink')):
        self.obj1857._setHierarchicalLink(False)

      # rate
      self.obj1857.rate.setValue(0.0)

      self.obj1857.GGLabel.setValue(4)
      self.obj1857.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(238.75,106.25,self.obj1857)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1857.graphObject_ = new_obj
      self.obj18570= AttrCalc()
      self.obj18570.Copy=ATOM3Boolean()
      self.obj18570.Copy.setValue(('Copy from LHS', 1))
      self.obj18570.Copy.config = 0
      self.obj18570.Specify=ATOM3Constraint()
      self.obj18570.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1857.GGset2Any['rate']= self.obj18570

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1857)
      self.obj1857.postAction( self.RHS.CREATE )

      self.obj1855.out_connections_.append(self.obj1857)
      self.obj1857.in_connections_.append(self.obj1855)
      self.obj1855.graphObject_.pendingConnections.append((self.obj1855.graphObject_.tag, self.obj1857.graphObject_.tag, [201.0, 82.0, 226.5, 89.0, 238.75, 106.25], 2, True))
      self.obj1857.out_connections_.append(self.obj1856)
      self.obj1856.in_connections_.append(self.obj1857)
      self.obj1857.graphObject_.pendingConnections.append((self.obj1857.graphObject_.tag, self.obj1856.graphObject_.tag, [250.0, 151.0, 251.0, 123.5, 238.75, 106.25], 2, True))

   def condition(self, graphID, isograph, atom3i):
      return self.graphRewritingSystem.finalStat > 20 
      

   def action(self, graphID, isograph, atom3i):
      pass

