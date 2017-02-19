# _ RemoveRolez_GG_rule.py ____________________________________________________________________________
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
class RemoveRolez_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 28)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_omacss(parent)
      self.LHS.merge(ASG_pns2(parent))
      self.LHS.merge(ASG_GenericGraph(parent))

      self.obj439=Role(parent)
      self.obj439.preAction( self.LHS.CREATE )
      self.obj439.isGraphObjectVisual = True

      if(hasattr(self.obj439, '_setHierarchicalLink')):
        self.obj439._setHierarchicalLink(False)

      # name
      self.obj439.name.setValue('')
      self.obj439.name.setNone()

      self.obj439.GGLabel.setValue(1)
      self.obj439.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(60.0,60.0,self.obj439)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj439.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj439)
      self.obj439.postAction( self.LHS.CREATE )

      self.obj440=operatingUnit(parent)
      self.obj440.preAction( self.LHS.CREATE )
      self.obj440.isGraphObjectVisual = True

      if(hasattr(self.obj440, '_setHierarchicalLink')):
        self.obj440._setHierarchicalLink(False)

      # name
      self.obj440.name.setValue('')
      self.obj440.name.setNone()

      self.obj440.GGLabel.setValue(2)
      self.obj440.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(260.0,160.0,self.obj440)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj440.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj440)
      self.obj440.postAction( self.LHS.CREATE )

      self.obj441=metarial(parent)
      self.obj441.preAction( self.LHS.CREATE )
      self.obj441.isGraphObjectVisual = True

      if(hasattr(self.obj441, '_setHierarchicalLink')):
        self.obj441._setHierarchicalLink(False)

      # Name
      self.obj441.Name.setValue('')
      self.obj441.Name.setNone()

      self.obj441.GGLabel.setValue(5)
      self.obj441.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(260.0,60.0,self.obj441)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj441.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj441)
      self.obj441.postAction( self.LHS.CREATE )

      self.obj442=fromMaterial(parent)
      self.obj442.preAction( self.LHS.CREATE )
      self.obj442.isGraphObjectVisual = True

      if(hasattr(self.obj442, '_setHierarchicalLink')):
        self.obj442._setHierarchicalLink(False)

      # rate
      self.obj442.rate.setNone()

      self.obj442.GGLabel.setValue(3)
      self.obj442.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(288.785046729,139.210526316,self.obj442)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj442.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj442)
      self.obj442.postAction( self.LHS.CREATE )

      self.obj441.out_connections_.append(self.obj442)
      self.obj442.in_connections_.append(self.obj441)
      self.obj441.graphObject_.pendingConnections.append((self.obj441.graphObject_.tag, self.obj442.graphObject_.tag, [284.0, 110.0, 288.78504672897196, 139.21052631578948], 0, True))
      self.obj442.out_connections_.append(self.obj440)
      self.obj440.in_connections_.append(self.obj442)
      self.obj442.graphObject_.pendingConnections.append((self.obj442.graphObject_.tag, self.obj440.graphObject_.tag, [273.5700934579439, 168.42105263157896, 288.78504672897196, 139.21052631578948], 0, True))

      self.RHS = ASG_omacss(parent)
      self.RHS.merge(ASG_pns2(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj446=operatingUnit(parent)
      self.obj446.preAction( self.RHS.CREATE )
      self.obj446.isGraphObjectVisual = True

      if(hasattr(self.obj446, '_setHierarchicalLink')):
        self.obj446._setHierarchicalLink(False)

      # name
      self.obj446.name.setValue('')
      self.obj446.name.setNone()

      self.obj446.GGLabel.setValue(2)
      self.obj446.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(240.0,160.0,self.obj446)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj446.graphObject_ = new_obj
      self.obj4460= AttrCalc()
      self.obj4460.Copy=ATOM3Boolean()
      self.obj4460.Copy.setValue(('Copy from LHS', 1))
      self.obj4460.Copy.config = 0
      self.obj4460.Specify=ATOM3Constraint()
      self.obj4460.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj446.GGset2Any['name']= self.obj4460

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj446)
      self.obj446.postAction( self.RHS.CREATE )

      self.obj447=metarial(parent)
      self.obj447.preAction( self.RHS.CREATE )
      self.obj447.isGraphObjectVisual = True

      if(hasattr(self.obj447, '_setHierarchicalLink')):
        self.obj447._setHierarchicalLink(False)

      # Name
      self.obj447.Name.setValue('')
      self.obj447.Name.setNone()

      self.obj447.GGLabel.setValue(5)
      self.obj447.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(240.0,40.0,self.obj447)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj447.graphObject_ = new_obj
      self.obj4470= AttrCalc()
      self.obj4470.Copy=ATOM3Boolean()
      self.obj4470.Copy.setValue(('Copy from LHS', 1))
      self.obj4470.Copy.config = 0
      self.obj4470.Specify=ATOM3Constraint()
      self.obj4470.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj447.GGset2Any['Name']= self.obj4470

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj447)
      self.obj447.postAction( self.RHS.CREATE )

      self.obj448=fromMaterial(parent)
      self.obj448.preAction( self.RHS.CREATE )
      self.obj448.isGraphObjectVisual = True

      if(hasattr(self.obj448, '_setHierarchicalLink')):
        self.obj448._setHierarchicalLink(False)

      # rate
      self.obj448.rate.setValue(0.0)

      self.obj448.GGLabel.setValue(3)
      self.obj448.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(258.785046729,129.210526316,self.obj448)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj448.graphObject_ = new_obj
      self.obj4480= AttrCalc()
      self.obj4480.Copy=ATOM3Boolean()
      self.obj4480.Copy.setValue(('Copy from LHS', 1))
      self.obj4480.Copy.config = 0
      self.obj4480.Specify=ATOM3Constraint()
      self.obj4480.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj448.GGset2Any['rate']= self.obj4480

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj448)
      self.obj448.postAction( self.RHS.CREATE )

      self.obj447.out_connections_.append(self.obj448)
      self.obj448.in_connections_.append(self.obj447)
      self.obj447.graphObject_.pendingConnections.append((self.obj447.graphObject_.tag, self.obj448.graphObject_.tag, [264.0, 90.0, 258.78504672897196, 129.21052631578948], 0, True))
      self.obj448.out_connections_.append(self.obj446)
      self.obj446.in_connections_.append(self.obj448)
      self.obj448.graphObject_.pendingConnections.append((self.obj448.graphObject_.tag, self.obj446.graphObject_.tag, [253.57009345794393, 168.42105263157896, 258.78504672897196, 129.21052631578948], 0, True))

   def condition(self, graphID, isograph, atom3i):
      return self.graphRewritingSystem.finalStat > 20 
      
      

   def action(self, graphID, isograph, atom3i):
      pass

