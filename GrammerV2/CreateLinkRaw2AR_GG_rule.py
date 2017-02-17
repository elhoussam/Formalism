# _ CreateLinkRaw2AR_GG_rule.py ____________________________________________________________________________
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
class CreateLinkRaw2AR_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 11)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_omacss(parent)
      self.LHS.merge(ASG_pns2(parent))
      self.LHS.merge(ASG_GenericGraph(parent))

      self.obj835=Agent(parent)
      self.obj835.preAction( self.LHS.CREATE )
      self.obj835.isGraphObjectVisual = True

      if(hasattr(self.obj835, '_setHierarchicalLink')):
        self.obj835._setHierarchicalLink(False)

      # price
      self.obj835.price.setValue(0)

      # name
      self.obj835.name.setValue('')
      self.obj835.name.setNone()

      self.obj835.GGLabel.setValue(1)
      self.obj835.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(80.0,60.0,self.obj835)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj835.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj835)
      self.obj835.postAction( self.LHS.CREATE )

      self.obj845=rawMaterial(parent)
      self.obj845.preAction( self.LHS.CREATE )
      self.obj845.isGraphObjectVisual = True

      if(hasattr(self.obj845, '_setHierarchicalLink')):
        self.obj845._setHierarchicalLink(False)

      # Name
      self.obj845.Name.setValue('')
      self.obj845.Name.setNone()

      self.obj845.GGLabel.setValue(3)
      self.obj845.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(240.0,20.0,self.obj845)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj845.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj845)
      self.obj845.postAction( self.LHS.CREATE )

      self.obj844=operatingUnit(parent)
      self.obj844.preAction( self.LHS.CREATE )
      self.obj844.isGraphObjectVisual = True

      if(hasattr(self.obj844, '_setHierarchicalLink')):
        self.obj844._setHierarchicalLink(False)

      # name
      self.obj844.name.setValue('')
      self.obj844.name.setNone()

      self.obj844.GGLabel.setValue(2)
      self.obj844.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(240.0,140.0,self.obj844)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj844.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj844)
      self.obj844.postAction( self.LHS.CREATE )

      self.obj850=GenericGraphEdge(parent)
      self.obj850.preAction( self.LHS.CREATE )
      self.obj850.isGraphObjectVisual = True

      if(hasattr(self.obj850, '_setHierarchicalLink')):
        self.obj850._setHierarchicalLink(False)

      self.obj850.GGLabel.setValue(4)
      self.obj850.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(184.5,97.5,self.obj850)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj850.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj850)
      self.obj850.postAction( self.LHS.CREATE )

      self.obj851=GenericGraphEdge(parent)
      self.obj851.preAction( self.LHS.CREATE )
      self.obj851.isGraphObjectVisual = True

      if(hasattr(self.obj851, '_setHierarchicalLink')):
        self.obj851._setHierarchicalLink(False)

      self.obj851.GGLabel.setValue(5)
      self.obj851.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(179.285046729,135.210526316,self.obj851)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj851.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj851)
      self.obj851.postAction( self.LHS.CREATE )

      self.obj835.out_connections_.append(self.obj850)
      self.obj850.in_connections_.append(self.obj835)
      self.obj835.graphObject_.pendingConnections.append((self.obj835.graphObject_.tag, self.obj850.graphObject_.tag, [105.0, 122.0, 184.5, 97.5], 0, True))
      self.obj835.out_connections_.append(self.obj851)
      self.obj851.in_connections_.append(self.obj835)
      self.obj835.graphObject_.pendingConnections.append((self.obj835.graphObject_.tag, self.obj851.graphObject_.tag, [105.0, 122.0, 179.28504672897196, 135.21052631578948], 0, True))
      self.obj850.out_connections_.append(self.obj845)
      self.obj845.in_connections_.append(self.obj850)
      self.obj850.graphObject_.pendingConnections.append((self.obj850.graphObject_.tag, self.obj845.graphObject_.tag, [264.0, 73.0, 184.5, 97.5], 0, True))
      self.obj851.out_connections_.append(self.obj844)
      self.obj844.in_connections_.append(self.obj851)
      self.obj851.graphObject_.pendingConnections.append((self.obj851.graphObject_.tag, self.obj844.graphObject_.tag, [253.57009345794393, 148.42105263157896, 179.28504672897196, 135.21052631578948], 0, True))

      self.RHS = ASG_omacss(parent)
      self.RHS.merge(ASG_pns2(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj861=Agent(parent)
      self.obj861.preAction( self.RHS.CREATE )
      self.obj861.isGraphObjectVisual = True

      if(hasattr(self.obj861, '_setHierarchicalLink')):
        self.obj861._setHierarchicalLink(False)

      # price
      self.obj861.price.setValue(0)

      # name
      self.obj861.name.setValue('')
      self.obj861.name.setNone()

      self.obj861.GGLabel.setValue(1)
      self.obj861.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(60.0,100.0,self.obj861)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj861.graphObject_ = new_obj
      self.obj8610= AttrCalc()
      self.obj8610.Copy=ATOM3Boolean()
      self.obj8610.Copy.setValue(('Copy from LHS', 1))
      self.obj8610.Copy.config = 0
      self.obj8610.Specify=ATOM3Constraint()
      self.obj8610.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj861.GGset2Any['price']= self.obj8610
      self.obj8611= AttrCalc()
      self.obj8611.Copy=ATOM3Boolean()
      self.obj8611.Copy.setValue(('Copy from LHS', 1))
      self.obj8611.Copy.config = 0
      self.obj8611.Specify=ATOM3Constraint()
      self.obj8611.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj861.GGset2Any['name']= self.obj8611

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj861)
      self.obj861.postAction( self.RHS.CREATE )

      self.obj863=rawMaterial(parent)
      self.obj863.preAction( self.RHS.CREATE )
      self.obj863.isGraphObjectVisual = True

      if(hasattr(self.obj863, '_setHierarchicalLink')):
        self.obj863._setHierarchicalLink(False)

      # Name
      self.obj863.Name.setValue('')
      self.obj863.Name.setNone()

      self.obj863.GGLabel.setValue(3)
      self.obj863.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(240.0,60.0,self.obj863)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj863.graphObject_ = new_obj
      self.obj8630= AttrCalc()
      self.obj8630.Copy=ATOM3Boolean()
      self.obj8630.Copy.setValue(('Copy from LHS', 1))
      self.obj8630.Copy.config = 0
      self.obj8630.Specify=ATOM3Constraint()
      self.obj8630.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj863.GGset2Any['Name']= self.obj8630

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj863)
      self.obj863.postAction( self.RHS.CREATE )

      self.obj862=operatingUnit(parent)
      self.obj862.preAction( self.RHS.CREATE )
      self.obj862.isGraphObjectVisual = True

      if(hasattr(self.obj862, '_setHierarchicalLink')):
        self.obj862._setHierarchicalLink(False)

      # name
      self.obj862.name.setValue('')
      self.obj862.name.setNone()

      self.obj862.GGLabel.setValue(2)
      self.obj862.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(240.0,180.0,self.obj862)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj862.graphObject_ = new_obj
      self.obj8620= AttrCalc()
      self.obj8620.Copy=ATOM3Boolean()
      self.obj8620.Copy.setValue(('Copy from LHS', 1))
      self.obj8620.Copy.config = 0
      self.obj8620.Specify=ATOM3Constraint()
      self.obj8620.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj862.GGset2Any['name']= self.obj8620

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj862)
      self.obj862.postAction( self.RHS.CREATE )

      self.obj870=fromRaw(parent)
      self.obj870.preAction( self.RHS.CREATE )
      self.obj870.isGraphObjectVisual = True

      if(hasattr(self.obj870, '_setHierarchicalLink')):
        self.obj870._setHierarchicalLink(False)

      # rate
      self.obj870.rate.setValue(0.0)

      self.obj870.GGLabel.setValue(6)
      self.obj870.graphClass_= graph_fromRaw
      if parent.genGraphics:
         new_obj = graph_fromRaw(258.785046729,150.710526316,self.obj870)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj870.graphObject_ = new_obj
      self.obj8700= AttrCalc()
      self.obj8700.Copy=ATOM3Boolean()
      self.obj8700.Copy.setValue(('Copy from LHS', 0))
      self.obj8700.Copy.config = 0
      self.obj8700.Specify=ATOM3Constraint()
      self.obj8700.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj870.GGset2Any['rate']= self.obj8700

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj870)
      self.obj870.postAction( self.RHS.CREATE )

      self.obj868=GenericGraphEdge(parent)
      self.obj868.preAction( self.RHS.CREATE )
      self.obj868.isGraphObjectVisual = True

      if(hasattr(self.obj868, '_setHierarchicalLink')):
        self.obj868._setHierarchicalLink(False)

      self.obj868.GGLabel.setValue(4)
      self.obj868.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(174.5,137.5,self.obj868)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj868.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj868)
      self.obj868.postAction( self.RHS.CREATE )

      self.obj869=GenericGraphEdge(parent)
      self.obj869.preAction( self.RHS.CREATE )
      self.obj869.isGraphObjectVisual = True

      if(hasattr(self.obj869, '_setHierarchicalLink')):
        self.obj869._setHierarchicalLink(False)

      self.obj869.GGLabel.setValue(5)
      self.obj869.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(169.285046729,175.210526316,self.obj869)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj869.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj869)
      self.obj869.postAction( self.RHS.CREATE )

      self.obj861.out_connections_.append(self.obj868)
      self.obj868.in_connections_.append(self.obj861)
      self.obj861.graphObject_.pendingConnections.append((self.obj861.graphObject_.tag, self.obj868.graphObject_.tag, [85.0, 162.0, 174.5, 137.5], 0, True))
      self.obj861.out_connections_.append(self.obj869)
      self.obj869.in_connections_.append(self.obj861)
      self.obj861.graphObject_.pendingConnections.append((self.obj861.graphObject_.tag, self.obj869.graphObject_.tag, [85.0, 162.0, 169.28504672897196, 175.21052631578948], 0, True))
      self.obj863.out_connections_.append(self.obj870)
      self.obj870.in_connections_.append(self.obj863)
      self.obj863.graphObject_.pendingConnections.append((self.obj863.graphObject_.tag, self.obj870.graphObject_.tag, [264.0, 113.0, 258.78504672897196, 150.71052631578948], 0, True))
      self.obj870.out_connections_.append(self.obj862)
      self.obj862.in_connections_.append(self.obj870)
      self.obj870.graphObject_.pendingConnections.append((self.obj870.graphObject_.tag, self.obj862.graphObject_.tag, [253.57009345794393, 188.42105263157896, 258.78504672897196, 150.71052631578948], 0, True))
      self.obj868.out_connections_.append(self.obj863)
      self.obj863.in_connections_.append(self.obj868)
      self.obj868.graphObject_.pendingConnections.append((self.obj868.graphObject_.tag, self.obj863.graphObject_.tag, [264.0, 113.0, 174.5, 137.5], 0, True))
      self.obj869.out_connections_.append(self.obj862)
      self.obj862.in_connections_.append(self.obj869)
      self.obj869.graphObject_.pendingConnections.append((self.obj869.graphObject_.tag, self.obj862.graphObject_.tag, [253.57009345794393, 188.42105263157896, 169.28504672897196, 175.21052631578948], 0, True))

   def condition(self, graphID, isograph, atom3i):
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(3))
      return not hasattr(node, "Goal2Mat")
      
      
      

   def action(self, graphID, isograph, atom3i):
      node = self.getMatched ( graphID , self.LHS.nodeWithLabel(3) )
      node.Goal2Mat = True
      

