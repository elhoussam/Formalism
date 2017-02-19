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

      self.obj268=Goal(parent)
      self.obj268.preAction( self.LHS.CREATE )
      self.obj268.isGraphObjectVisual = True

      if(hasattr(self.obj268, '_setHierarchicalLink')):
        self.obj268._setHierarchicalLink(False)

      # name
      self.obj268.name.setValue('')
      self.obj268.name.setNone()

      self.obj268.GGLabel.setValue(2)
      self.obj268.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(80.0,40.0,self.obj268)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj268.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj268)
      self.obj268.postAction( self.LHS.CREATE )

      self.obj269=metarial(parent)
      self.obj269.preAction( self.LHS.CREATE )
      self.obj269.isGraphObjectVisual = True

      if(hasattr(self.obj269, '_setHierarchicalLink')):
        self.obj269._setHierarchicalLink(False)

      # Name
      self.obj269.Name.setValue('')
      self.obj269.Name.setNone()

      self.obj269.GGLabel.setValue(3)
      self.obj269.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(220.0,40.0,self.obj269)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj269.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj269)
      self.obj269.postAction( self.LHS.CREATE )

      self.obj270=product(parent)
      self.obj270.preAction( self.LHS.CREATE )
      self.obj270.isGraphObjectVisual = True

      if(hasattr(self.obj270, '_setHierarchicalLink')):
        self.obj270._setHierarchicalLink(False)

      # Name
      self.obj270.Name.setValue('')
      self.obj270.Name.setNone()

      self.obj270.GGLabel.setValue(5)
      self.obj270.graphClass_= graph_product
      if parent.genGraphics:
         new_obj = graph_product(160.0,180.0,self.obj270)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj270.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj270)
      self.obj270.postAction( self.LHS.CREATE )

      self.obj271=GenericGraphEdge(parent)
      self.obj271.preAction( self.LHS.CREATE )
      self.obj271.isGraphObjectVisual = True

      if(hasattr(self.obj271, '_setHierarchicalLink')):
        self.obj271._setHierarchicalLink(False)

      self.obj271.GGLabel.setValue(4)
      self.obj271.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(167.0,87.0,self.obj271)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj271.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj271)
      self.obj271.postAction( self.LHS.CREATE )

      self.obj268.out_connections_.append(self.obj271)
      self.obj271.in_connections_.append(self.obj268)
      self.obj268.graphObject_.pendingConnections.append((self.obj268.graphObject_.tag, self.obj271.graphObject_.tag, [104.0, 90.0, 167.0, 87.0], 0, True))
      self.obj271.out_connections_.append(self.obj269)
      self.obj269.in_connections_.append(self.obj271)
      self.obj271.graphObject_.pendingConnections.append((self.obj271.graphObject_.tag, self.obj269.graphObject_.tag, [230.0, 84.0, 167.0, 87.0], 0, True))

      self.RHS = ASG_omacss(parent)
      self.RHS.merge(ASG_pns2(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj275=Goal(parent)
      self.obj275.preAction( self.RHS.CREATE )
      self.obj275.isGraphObjectVisual = True

      if(hasattr(self.obj275, '_setHierarchicalLink')):
        self.obj275._setHierarchicalLink(False)

      # name
      self.obj275.name.setValue('')
      self.obj275.name.setNone()

      self.obj275.GGLabel.setValue(2)
      self.obj275.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(60.0,40.0,self.obj275)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj275.graphObject_ = new_obj
      self.obj2750= AttrCalc()
      self.obj2750.Copy=ATOM3Boolean()
      self.obj2750.Copy.setValue(('Copy from LHS', 1))
      self.obj2750.Copy.config = 0
      self.obj2750.Specify=ATOM3Constraint()
      self.obj2750.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj275.GGset2Any['name']= self.obj2750

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj275)
      self.obj275.postAction( self.RHS.CREATE )

      self.obj276=intoProduct(parent)
      self.obj276.preAction( self.RHS.CREATE )
      self.obj276.isGraphObjectVisual = True

      if(hasattr(self.obj276, '_setHierarchicalLink')):
        self.obj276._setHierarchicalLink(False)

      # rate
      self.obj276.rate.setValue(1.0)

      self.obj276.GGLabel.setValue(6)
      self.obj276.graphClass_= graph_intoProduct
      if parent.genGraphics:
         new_obj = graph_intoProduct(267.198598131,175.25,self.obj276)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj276.graphObject_ = new_obj
      self.obj2760= AttrCalc()
      self.obj2760.Copy=ATOM3Boolean()
      self.obj2760.Copy.setValue(('Copy from LHS', 0))
      self.obj2760.Copy.config = 0
      self.obj2760.Specify=ATOM3Constraint()
      self.obj2760.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj276.GGset2Any['rate']= self.obj2760

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj276)
      self.obj276.postAction( self.RHS.CREATE )

      self.obj277=operatingUnit(parent)
      self.obj277.preAction( self.RHS.CREATE )
      self.obj277.isGraphObjectVisual = True

      if(hasattr(self.obj277, '_setHierarchicalLink')):
        self.obj277._setHierarchicalLink(False)

      # name
      self.obj277.name.setValue('')
      self.obj277.name.setNone()

      self.obj277.GGLabel.setValue(1)
      self.obj277.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(260.0,120.0,self.obj277)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj277.graphObject_ = new_obj
      self.obj2770= AttrCalc()
      self.obj2770.Copy=ATOM3Boolean()
      self.obj2770.Copy.setValue(('Copy from LHS', 0))
      self.obj2770.Copy.config = 0
      self.obj2770.Specify=ATOM3Constraint()
      self.obj2770.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(2)).name.getValue()+\' OAF\'\n\n\n\n\n\n\n\n\n\n'))
      self.obj277.GGset2Any['name']= self.obj2770

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj277)
      self.obj277.postAction( self.RHS.CREATE )

      self.obj278=metarial(parent)
      self.obj278.preAction( self.RHS.CREATE )
      self.obj278.isGraphObjectVisual = True

      if(hasattr(self.obj278, '_setHierarchicalLink')):
        self.obj278._setHierarchicalLink(False)

      # Name
      self.obj278.Name.setValue('')
      self.obj278.Name.setNone()

      self.obj278.GGLabel.setValue(3)
      self.obj278.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(180.0,40.0,self.obj278)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj278.graphObject_ = new_obj
      self.obj2780= AttrCalc()
      self.obj2780.Copy=ATOM3Boolean()
      self.obj2780.Copy.setValue(('Copy from LHS', 1))
      self.obj2780.Copy.config = 0
      self.obj2780.Specify=ATOM3Constraint()
      self.obj2780.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj278.GGset2Any['Name']= self.obj2780

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj278)
      self.obj278.postAction( self.RHS.CREATE )

      self.obj279=product(parent)
      self.obj279.preAction( self.RHS.CREATE )
      self.obj279.isGraphObjectVisual = True

      if(hasattr(self.obj279, '_setHierarchicalLink')):
        self.obj279._setHierarchicalLink(False)

      # Name
      self.obj279.Name.setValue('')
      self.obj279.Name.setNone()

      self.obj279.GGLabel.setValue(5)
      self.obj279.graphClass_= graph_product
      if parent.genGraphics:
         new_obj = graph_product(160.0,180.0,self.obj279)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj279.graphObject_ = new_obj
      self.obj2790= AttrCalc()
      self.obj2790.Copy=ATOM3Boolean()
      self.obj2790.Copy.setValue(('Copy from LHS', 1))
      self.obj2790.Copy.config = 0
      self.obj2790.Specify=ATOM3Constraint()
      self.obj2790.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj279.GGset2Any['Name']= self.obj2790

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj279)
      self.obj279.postAction( self.RHS.CREATE )

      self.obj280=fromMaterial(parent)
      self.obj280.preAction( self.RHS.CREATE )
      self.obj280.isGraphObjectVisual = True

      if(hasattr(self.obj280, '_setHierarchicalLink')):
        self.obj280._setHierarchicalLink(False)

      # rate
      self.obj280.rate.setValue(1.0)

      self.obj280.GGLabel.setValue(7)
      self.obj280.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(273.081775701,95.6184210526,self.obj280)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj280.graphObject_ = new_obj
      self.obj2800= AttrCalc()
      self.obj2800.Copy=ATOM3Boolean()
      self.obj2800.Copy.setValue(('Copy from LHS', 0))
      self.obj2800.Copy.config = 0
      self.obj2800.Specify=ATOM3Constraint()
      self.obj2800.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj280.GGset2Any['rate']= self.obj2800

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj280)
      self.obj280.postAction( self.RHS.CREATE )

      self.obj281=GenericGraphEdge(parent)
      self.obj281.preAction( self.RHS.CREATE )
      self.obj281.isGraphObjectVisual = True

      if(hasattr(self.obj281, '_setHierarchicalLink')):
        self.obj281._setHierarchicalLink(False)

      self.obj281.GGLabel.setValue(4)
      self.obj281.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(137.5,43.0,self.obj281)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj281.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj281)
      self.obj281.postAction( self.RHS.CREATE )

      self.obj275.out_connections_.append(self.obj281)
      self.obj281.in_connections_.append(self.obj275)
      self.obj275.graphObject_.pendingConnections.append((self.obj275.graphObject_.tag, self.obj281.graphObject_.tag, [83.0, 41.0, 137.5, 43.0], 0, True))
      self.obj276.out_connections_.append(self.obj279)
      self.obj279.in_connections_.append(self.obj276)
      self.obj276.graphObject_.pendingConnections.append((self.obj276.graphObject_.tag, self.obj279.graphObject_.tag, [187.0, 179.0, 238.0, 186.0, 267.1985981308411, 175.25], 2, True))
      self.obj277.out_connections_.append(self.obj276)
      self.obj276.in_connections_.append(self.obj277)
      self.obj277.graphObject_.pendingConnections.append((self.obj277.graphObject_.tag, self.obj276.graphObject_.tag, [303.79439252336454, 136.0, 296.39719626168227, 164.5, 267.1985981308411, 175.25], 2, True))
      self.obj278.out_connections_.append(self.obj280)
      self.obj280.in_connections_.append(self.obj278)
      self.obj278.graphObject_.pendingConnections.append((self.obj278.graphObject_.tag, self.obj280.graphObject_.tag, [217.0, 85.0, 252.0, 85.0, 273.0817757009346, 95.61842105263158], 2, True))
      self.obj280.out_connections_.append(self.obj277)
      self.obj277.in_connections_.append(self.obj280)
      self.obj280.graphObject_.pendingConnections.append((self.obj280.graphObject_.tag, self.obj277.graphObject_.tag, [301.32710280373834, 127.4736842105263, 294.1635514018692, 106.23684210526315, 273.0817757009346, 95.61842105263158], 2, True))
      self.obj281.out_connections_.append(self.obj278)
      self.obj278.in_connections_.append(self.obj281)
      self.obj281.graphObject_.pendingConnections.append((self.obj281.graphObject_.tag, self.obj278.graphObject_.tag, [192.0, 45.0, 137.5, 43.0], 0, True))

   def condition(self, graphID, isograph, atom3i):
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(3))
      return not hasattr(node, "link2oaf")
      
      

   def action(self, graphID, isograph, atom3i):
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(3))
      node.link2oaf = True
      
      

