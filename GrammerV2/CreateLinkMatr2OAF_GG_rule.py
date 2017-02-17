# _ CreateLinkMatr2OAF_GG_rule.py ____________________________________________________________________________
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
class CreateLinkMatr2OAF_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 15)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_omacss(parent)
      self.LHS.merge(ASG_pns2(parent))
      self.LHS.merge(ASG_GenericGraph(parent))

      self.obj1065=Goal(parent)
      self.obj1065.preAction( self.LHS.CREATE )
      self.obj1065.isGraphObjectVisual = True

      if(hasattr(self.obj1065, '_setHierarchicalLink')):
        self.obj1065._setHierarchicalLink(False)

      # name
      self.obj1065.name.setValue('')
      self.obj1065.name.setNone()

      self.obj1065.GGLabel.setValue(2)
      self.obj1065.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(80.0,40.0,self.obj1065)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1065.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1065)
      self.obj1065.postAction( self.LHS.CREATE )

      self.obj1066=metarial(parent)
      self.obj1066.preAction( self.LHS.CREATE )
      self.obj1066.isGraphObjectVisual = True

      if(hasattr(self.obj1066, '_setHierarchicalLink')):
        self.obj1066._setHierarchicalLink(False)

      # Name
      self.obj1066.Name.setValue('')
      self.obj1066.Name.setNone()

      self.obj1066.GGLabel.setValue(3)
      self.obj1066.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(220.0,40.0,self.obj1066)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1066.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1066)
      self.obj1066.postAction( self.LHS.CREATE )

      self.obj1067=product(parent)
      self.obj1067.preAction( self.LHS.CREATE )
      self.obj1067.isGraphObjectVisual = True

      if(hasattr(self.obj1067, '_setHierarchicalLink')):
        self.obj1067._setHierarchicalLink(False)

      # Name
      self.obj1067.Name.setValue('')
      self.obj1067.Name.setNone()

      self.obj1067.GGLabel.setValue(5)
      self.obj1067.graphClass_= graph_product
      if parent.genGraphics:
         new_obj = graph_product(160.0,180.0,self.obj1067)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1067.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1067)
      self.obj1067.postAction( self.LHS.CREATE )

      self.obj1068=GenericGraphEdge(parent)
      self.obj1068.preAction( self.LHS.CREATE )
      self.obj1068.isGraphObjectVisual = True

      if(hasattr(self.obj1068, '_setHierarchicalLink')):
        self.obj1068._setHierarchicalLink(False)

      self.obj1068.GGLabel.setValue(4)
      self.obj1068.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(167.0,87.0,self.obj1068)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1068.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1068)
      self.obj1068.postAction( self.LHS.CREATE )

      self.obj1065.out_connections_.append(self.obj1068)
      self.obj1068.in_connections_.append(self.obj1065)
      self.obj1065.graphObject_.pendingConnections.append((self.obj1065.graphObject_.tag, self.obj1068.graphObject_.tag, [104.0, 90.0, 167.0, 87.0], 0, True))
      self.obj1068.out_connections_.append(self.obj1066)
      self.obj1066.in_connections_.append(self.obj1068)
      self.obj1068.graphObject_.pendingConnections.append((self.obj1068.graphObject_.tag, self.obj1066.graphObject_.tag, [230.0, 84.0, 167.0, 87.0], 0, True))

      self.RHS = ASG_omacss(parent)
      self.RHS.merge(ASG_pns2(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj1072=Goal(parent)
      self.obj1072.preAction( self.RHS.CREATE )
      self.obj1072.isGraphObjectVisual = True

      if(hasattr(self.obj1072, '_setHierarchicalLink')):
        self.obj1072._setHierarchicalLink(False)

      # name
      self.obj1072.name.setValue('')
      self.obj1072.name.setNone()

      self.obj1072.GGLabel.setValue(2)
      self.obj1072.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(60.0,40.0,self.obj1072)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1072.graphObject_ = new_obj
      self.obj10720= AttrCalc()
      self.obj10720.Copy=ATOM3Boolean()
      self.obj10720.Copy.setValue(('Copy from LHS', 1))
      self.obj10720.Copy.config = 0
      self.obj10720.Specify=ATOM3Constraint()
      self.obj10720.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1072.GGset2Any['name']= self.obj10720

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1072)
      self.obj1072.postAction( self.RHS.CREATE )

      self.obj1073=intoProduct(parent)
      self.obj1073.preAction( self.RHS.CREATE )
      self.obj1073.isGraphObjectVisual = True

      if(hasattr(self.obj1073, '_setHierarchicalLink')):
        self.obj1073._setHierarchicalLink(False)

      # rate
      self.obj1073.rate.setValue(1.0)

      self.obj1073.GGLabel.setValue(6)
      self.obj1073.graphClass_= graph_intoProduct
      if parent.genGraphics:
         new_obj = graph_intoProduct(267.198598131,175.25,self.obj1073)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1073.graphObject_ = new_obj
      self.obj10730= AttrCalc()
      self.obj10730.Copy=ATOM3Boolean()
      self.obj10730.Copy.setValue(('Copy from LHS', 0))
      self.obj10730.Copy.config = 0
      self.obj10730.Specify=ATOM3Constraint()
      self.obj10730.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1073.GGset2Any['rate']= self.obj10730

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1073)
      self.obj1073.postAction( self.RHS.CREATE )

      self.obj1074=operatingUnit(parent)
      self.obj1074.preAction( self.RHS.CREATE )
      self.obj1074.isGraphObjectVisual = True

      if(hasattr(self.obj1074, '_setHierarchicalLink')):
        self.obj1074._setHierarchicalLink(False)

      # name
      self.obj1074.name.setValue('')
      self.obj1074.name.setNone()

      self.obj1074.GGLabel.setValue(1)
      self.obj1074.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(260.0,120.0,self.obj1074)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1074.graphObject_ = new_obj
      self.obj10740= AttrCalc()
      self.obj10740.Copy=ATOM3Boolean()
      self.obj10740.Copy.setValue(('Copy from LHS', 0))
      self.obj10740.Copy.config = 0
      self.obj10740.Specify=ATOM3Constraint()
      self.obj10740.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(2)).name.getValue()+\' OAF\'\n\n\n\n\n\n\n\n\n\n'))
      self.obj1074.GGset2Any['name']= self.obj10740

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1074)
      self.obj1074.postAction( self.RHS.CREATE )

      self.obj1075=metarial(parent)
      self.obj1075.preAction( self.RHS.CREATE )
      self.obj1075.isGraphObjectVisual = True

      if(hasattr(self.obj1075, '_setHierarchicalLink')):
        self.obj1075._setHierarchicalLink(False)

      # Name
      self.obj1075.Name.setValue('')
      self.obj1075.Name.setNone()

      self.obj1075.GGLabel.setValue(3)
      self.obj1075.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(180.0,40.0,self.obj1075)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1075.graphObject_ = new_obj
      self.obj10750= AttrCalc()
      self.obj10750.Copy=ATOM3Boolean()
      self.obj10750.Copy.setValue(('Copy from LHS', 1))
      self.obj10750.Copy.config = 0
      self.obj10750.Specify=ATOM3Constraint()
      self.obj10750.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1075.GGset2Any['Name']= self.obj10750

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1075)
      self.obj1075.postAction( self.RHS.CREATE )

      self.obj1076=product(parent)
      self.obj1076.preAction( self.RHS.CREATE )
      self.obj1076.isGraphObjectVisual = True

      if(hasattr(self.obj1076, '_setHierarchicalLink')):
        self.obj1076._setHierarchicalLink(False)

      # Name
      self.obj1076.Name.setValue('')
      self.obj1076.Name.setNone()

      self.obj1076.GGLabel.setValue(5)
      self.obj1076.graphClass_= graph_product
      if parent.genGraphics:
         new_obj = graph_product(160.0,180.0,self.obj1076)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1076.graphObject_ = new_obj
      self.obj10760= AttrCalc()
      self.obj10760.Copy=ATOM3Boolean()
      self.obj10760.Copy.setValue(('Copy from LHS', 1))
      self.obj10760.Copy.config = 0
      self.obj10760.Specify=ATOM3Constraint()
      self.obj10760.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1076.GGset2Any['Name']= self.obj10760

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1076)
      self.obj1076.postAction( self.RHS.CREATE )

      self.obj1077=fromMaterial(parent)
      self.obj1077.preAction( self.RHS.CREATE )
      self.obj1077.isGraphObjectVisual = True

      if(hasattr(self.obj1077, '_setHierarchicalLink')):
        self.obj1077._setHierarchicalLink(False)

      # rate
      self.obj1077.rate.setValue(1.0)

      self.obj1077.GGLabel.setValue(7)
      self.obj1077.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(273.081775701,95.6184210526,self.obj1077)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1077.graphObject_ = new_obj
      self.obj10770= AttrCalc()
      self.obj10770.Copy=ATOM3Boolean()
      self.obj10770.Copy.setValue(('Copy from LHS', 0))
      self.obj10770.Copy.config = 0
      self.obj10770.Specify=ATOM3Constraint()
      self.obj10770.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1077.GGset2Any['rate']= self.obj10770

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1077)
      self.obj1077.postAction( self.RHS.CREATE )

      self.obj1078=GenericGraphEdge(parent)
      self.obj1078.preAction( self.RHS.CREATE )
      self.obj1078.isGraphObjectVisual = True

      if(hasattr(self.obj1078, '_setHierarchicalLink')):
        self.obj1078._setHierarchicalLink(False)

      self.obj1078.GGLabel.setValue(4)
      self.obj1078.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(137.5,43.0,self.obj1078)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1078.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1078)
      self.obj1078.postAction( self.RHS.CREATE )

      self.obj1072.out_connections_.append(self.obj1078)
      self.obj1078.in_connections_.append(self.obj1072)
      self.obj1072.graphObject_.pendingConnections.append((self.obj1072.graphObject_.tag, self.obj1078.graphObject_.tag, [83.0, 41.0, 137.5, 43.0], 0, True))
      self.obj1073.out_connections_.append(self.obj1076)
      self.obj1076.in_connections_.append(self.obj1073)
      self.obj1073.graphObject_.pendingConnections.append((self.obj1073.graphObject_.tag, self.obj1076.graphObject_.tag, [187.0, 179.0, 238.0, 186.0, 267.1985981308411, 175.25], 2, True))
      self.obj1074.out_connections_.append(self.obj1073)
      self.obj1073.in_connections_.append(self.obj1074)
      self.obj1074.graphObject_.pendingConnections.append((self.obj1074.graphObject_.tag, self.obj1073.graphObject_.tag, [303.79439252336454, 136.0, 296.39719626168227, 164.5, 267.1985981308411, 175.25], 2, True))
      self.obj1075.out_connections_.append(self.obj1077)
      self.obj1077.in_connections_.append(self.obj1075)
      self.obj1075.graphObject_.pendingConnections.append((self.obj1075.graphObject_.tag, self.obj1077.graphObject_.tag, [217.0, 85.0, 252.0, 85.0, 273.0817757009346, 95.61842105263158], 2, True))
      self.obj1077.out_connections_.append(self.obj1074)
      self.obj1074.in_connections_.append(self.obj1077)
      self.obj1077.graphObject_.pendingConnections.append((self.obj1077.graphObject_.tag, self.obj1074.graphObject_.tag, [301.32710280373834, 127.4736842105263, 294.1635514018692, 106.23684210526315, 273.0817757009346, 95.61842105263158], 2, True))
      self.obj1078.out_connections_.append(self.obj1075)
      self.obj1075.in_connections_.append(self.obj1078)
      self.obj1078.graphObject_.pendingConnections.append((self.obj1078.graphObject_.tag, self.obj1075.graphObject_.tag, [192.0, 45.0, 137.5, 43.0], 0, True))

   def condition(self, graphID, isograph, atom3i):
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(3))
      return not hasattr(node, "link2oaf")
      
      

   def action(self, graphID, isograph, atom3i):
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(3))
      node.link2oaf = True
      
      

