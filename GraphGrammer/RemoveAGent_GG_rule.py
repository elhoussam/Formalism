# _ RemoveAGent_GG_rule.py ____________________________________________________________________________
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
class RemoveAGent_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 26)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_omacss(parent)
      self.LHS.merge(ASG_pns2(parent))
      self.LHS.merge(ASG_GenericGraph(parent))

      self.obj416=Agent(parent)
      self.obj416.preAction( self.LHS.CREATE )
      self.obj416.isGraphObjectVisual = True

      if(hasattr(self.obj416, '_setHierarchicalLink')):
        self.obj416._setHierarchicalLink(False)

      # price
      self.obj416.price.setNone()

      # name
      self.obj416.name.setValue('')
      self.obj416.name.setNone()

      self.obj416.GGLabel.setValue(1)
      self.obj416.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(100.0,60.0,self.obj416)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj416.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj416)
      self.obj416.postAction( self.LHS.CREATE )

      self.obj417=rawMaterial(parent)
      self.obj417.preAction( self.LHS.CREATE )
      self.obj417.isGraphObjectVisual = True

      if(hasattr(self.obj417, '_setHierarchicalLink')):
        self.obj417._setHierarchicalLink(False)

      # Name
      self.obj417.Name.setValue('')
      self.obj417.Name.setNone()

      self.obj417.GGLabel.setValue(2)
      self.obj417.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(280.0,20.0,self.obj417)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj417.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj417)
      self.obj417.postAction( self.LHS.CREATE )

      self.obj418=operatingUnit(parent)
      self.obj418.preAction( self.LHS.CREATE )
      self.obj418.isGraphObjectVisual = True

      if(hasattr(self.obj418, '_setHierarchicalLink')):
        self.obj418._setHierarchicalLink(False)

      # name
      self.obj418.name.setValue('')
      self.obj418.name.setNone()

      self.obj418.GGLabel.setValue(3)
      self.obj418.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(280.0,140.0,self.obj418)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj418.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj418)
      self.obj418.postAction( self.LHS.CREATE )

      self.obj419=fromRaw(parent)
      self.obj419.preAction( self.LHS.CREATE )
      self.obj419.isGraphObjectVisual = True

      if(hasattr(self.obj419, '_setHierarchicalLink')):
        self.obj419._setHierarchicalLink(False)

      # rate
      self.obj419.rate.setNone()

      self.obj419.GGLabel.setValue(6)
      self.obj419.graphClass_= graph_fromRaw
      if parent.genGraphics:
         new_obj = graph_fromRaw(298.785046729,110.710526316,self.obj419)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj419.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj419)
      self.obj419.postAction( self.LHS.CREATE )

      self.obj420=GenericGraphEdge(parent)
      self.obj420.preAction( self.LHS.CREATE )
      self.obj420.isGraphObjectVisual = True

      if(hasattr(self.obj420, '_setHierarchicalLink')):
        self.obj420._setHierarchicalLink(False)

      self.obj420.GGLabel.setValue(4)
      self.obj420.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(220.5,97.5,self.obj420)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj420.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj420)
      self.obj420.postAction( self.LHS.CREATE )

      self.obj421=GenericGraphEdge(parent)
      self.obj421.preAction( self.LHS.CREATE )
      self.obj421.isGraphObjectVisual = True

      if(hasattr(self.obj421, '_setHierarchicalLink')):
        self.obj421._setHierarchicalLink(False)

      self.obj421.GGLabel.setValue(5)
      self.obj421.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(215.285046729,135.210526316,self.obj421)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj421.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj421)
      self.obj421.postAction( self.LHS.CREATE )

      self.obj416.out_connections_.append(self.obj420)
      self.obj420.in_connections_.append(self.obj416)
      self.obj416.graphObject_.pendingConnections.append((self.obj416.graphObject_.tag, self.obj420.graphObject_.tag, [137.0, 122.0, 220.5, 97.5], 0, True))
      self.obj416.out_connections_.append(self.obj421)
      self.obj421.in_connections_.append(self.obj416)
      self.obj416.graphObject_.pendingConnections.append((self.obj416.graphObject_.tag, self.obj421.graphObject_.tag, [137.0, 122.0, 215.285046729, 135.210526316], 2, 0))
      self.obj417.out_connections_.append(self.obj419)
      self.obj419.in_connections_.append(self.obj417)
      self.obj417.graphObject_.pendingConnections.append((self.obj417.graphObject_.tag, self.obj419.graphObject_.tag, [304.0, 73.0, 298.78504672897196, 110.71052631578948], 0, True))
      self.obj419.out_connections_.append(self.obj418)
      self.obj418.in_connections_.append(self.obj419)
      self.obj419.graphObject_.pendingConnections.append((self.obj419.graphObject_.tag, self.obj418.graphObject_.tag, [293.5700934579439, 148.42105263157896, 298.78504672897196, 110.71052631578948], 0, True))
      self.obj420.out_connections_.append(self.obj417)
      self.obj417.in_connections_.append(self.obj420)
      self.obj420.graphObject_.pendingConnections.append((self.obj420.graphObject_.tag, self.obj417.graphObject_.tag, [304.0, 73.0, 220.5, 97.5], 0, True))
      self.obj421.out_connections_.append(self.obj418)
      self.obj418.in_connections_.append(self.obj421)
      self.obj421.graphObject_.pendingConnections.append((self.obj421.graphObject_.tag, self.obj418.graphObject_.tag, [294.5700934579439, 148.42105263157896, 215.285046729, 135.210526316], 2, 0))

      self.RHS = ASG_omacss(parent)
      self.RHS.merge(ASG_pns2(parent))

      self.obj424=rawMaterial(parent)
      self.obj424.preAction( self.RHS.CREATE )
      self.obj424.isGraphObjectVisual = True

      if(hasattr(self.obj424, '_setHierarchicalLink')):
        self.obj424._setHierarchicalLink(False)

      # Name
      self.obj424.Name.setValue('')
      self.obj424.Name.setNone()

      self.obj424.GGLabel.setValue(2)
      self.obj424.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(200.0,20.0,self.obj424)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj424.graphObject_ = new_obj
      self.obj4240= AttrCalc()
      self.obj4240.Copy=ATOM3Boolean()
      self.obj4240.Copy.setValue(('Copy from LHS', 1))
      self.obj4240.Copy.config = 0
      self.obj4240.Specify=ATOM3Constraint()
      self.obj4240.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj424.GGset2Any['Name']= self.obj4240

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj424)
      self.obj424.postAction( self.RHS.CREATE )

      self.obj425=operatingUnit(parent)
      self.obj425.preAction( self.RHS.CREATE )
      self.obj425.isGraphObjectVisual = True

      if(hasattr(self.obj425, '_setHierarchicalLink')):
        self.obj425._setHierarchicalLink(False)

      # name
      self.obj425.name.setValue('')
      self.obj425.name.setNone()

      self.obj425.GGLabel.setValue(3)
      self.obj425.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(200.0,160.0,self.obj425)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj425.graphObject_ = new_obj
      self.obj4250= AttrCalc()
      self.obj4250.Copy=ATOM3Boolean()
      self.obj4250.Copy.setValue(('Copy from LHS', 1))
      self.obj4250.Copy.config = 0
      self.obj4250.Specify=ATOM3Constraint()
      self.obj4250.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj425.GGset2Any['name']= self.obj4250

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj425)
      self.obj425.postAction( self.RHS.CREATE )

      self.obj426=fromRaw(parent)
      self.obj426.preAction( self.RHS.CREATE )
      self.obj426.isGraphObjectVisual = True

      if(hasattr(self.obj426, '_setHierarchicalLink')):
        self.obj426._setHierarchicalLink(False)

      # rate
      self.obj426.rate.setValue(0.0)

      self.obj426.GGLabel.setValue(6)
      self.obj426.graphClass_= graph_fromRaw
      if parent.genGraphics:
         new_obj = graph_fromRaw(228.785046729,120.710526316,self.obj426)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj426.graphObject_ = new_obj
      self.obj4260= AttrCalc()
      self.obj4260.Copy=ATOM3Boolean()
      self.obj4260.Copy.setValue(('Copy from LHS', 1))
      self.obj4260.Copy.config = 0
      self.obj4260.Specify=ATOM3Constraint()
      self.obj4260.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj426.GGset2Any['rate']= self.obj4260

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj426)
      self.obj426.postAction( self.RHS.CREATE )

      self.obj424.out_connections_.append(self.obj426)
      self.obj426.in_connections_.append(self.obj424)
      self.obj424.graphObject_.pendingConnections.append((self.obj424.graphObject_.tag, self.obj426.graphObject_.tag, [224.0, 73.0, 228.78504672897196, 120.71052631578948], 0, True))
      self.obj426.out_connections_.append(self.obj425)
      self.obj425.in_connections_.append(self.obj426)
      self.obj426.graphObject_.pendingConnections.append((self.obj426.graphObject_.tag, self.obj425.graphObject_.tag, [213.57009345794393, 168.42105263157896, 228.78504672897196, 120.71052631578948], 0, True))

   def condition(self, graphID, isograph, atom3i):
      return self.graphRewritingSystem.finalStat > 20 
      

   def action(self, graphID, isograph, atom3i):
      pass

