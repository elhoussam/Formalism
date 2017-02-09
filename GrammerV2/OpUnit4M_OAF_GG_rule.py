# _ OpUnit4M_OAF_GG_rule.py ____________________________________________________________________________
# File generated automatically by ATOM3. Graph Grammar Rule
# ___________________________________________________________________________________________
from GGrule import *
from Capabilitie import *
from rawMaterial import *
from GenericGraphEdge import *
from Goal import *
from intoProduct import *
from operatingUnit import *
from metarial import *
from GenericGraphNode import *
from product import *
from Agent import *
from fromMaterial import *
from CapableOf import *
from Role import *
from fromRaw import *
from ASG_pns2 import *
from intoMaterial import *
from ASG_GenericGraph import *
from ASG_omacs import *
from require import *
from achieve import *
from posses import *
class OpUnit4M_OAF_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 51)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_pns2(parent)
      self.LHS.merge(ASG_omacs(parent))
      self.LHS.merge(ASG_GenericGraph(parent))

      self.obj167=product(parent)
      self.obj167.preAction( self.LHS.CREATE )
      self.obj167.isGraphObjectVisual = True

      if(hasattr(self.obj167, '_setHierarchicalLink')):
        self.obj167._setHierarchicalLink(False)

      # Name
      self.obj167.Name.setValue('')
      self.obj167.Name.setNone()

      self.obj167.GGLabel.setValue(4)
      self.obj167.graphClass_= graph_product
      if parent.genGraphics:
         new_obj = graph_product(360.0,40.0,self.obj167)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj167.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj167)
      self.obj167.postAction( self.LHS.CREATE )

      self.obj168=metarial(parent)
      self.obj168.preAction( self.LHS.CREATE )
      self.obj168.isGraphObjectVisual = True

      if(hasattr(self.obj168, '_setHierarchicalLink')):
        self.obj168._setHierarchicalLink(False)

      # Name
      self.obj168.Name.setValue('')
      self.obj168.Name.setNone()

      self.obj168.GGLabel.setValue(2)
      self.obj168.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(180.0,40.0,self.obj168)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj168.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj168)
      self.obj168.postAction( self.LHS.CREATE )

      self.obj169=Goal(parent)
      self.obj169.preAction( self.LHS.CREATE )
      self.obj169.isGraphObjectVisual = True

      if(hasattr(self.obj169, '_setHierarchicalLink')):
        self.obj169._setHierarchicalLink(False)

      # name
      self.obj169.name.setValue('')
      self.obj169.name.setNone()

      self.obj169.GGLabel.setValue(1)
      self.obj169.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(20.0,20.0,self.obj169)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj169.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj169)
      self.obj169.postAction( self.LHS.CREATE )

      self.obj170=GenericGraphEdge(parent)
      self.obj170.preAction( self.LHS.CREATE )
      self.obj170.isGraphObjectVisual = True

      if(hasattr(self.obj170, '_setHierarchicalLink')):
        self.obj170._setHierarchicalLink(False)

      self.obj170.GGLabel.setValue(3)
      self.obj170.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(136.0,126.5,self.obj170)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj170.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj170)
      self.obj170.postAction( self.LHS.CREATE )

      self.obj169.out_connections_.append(self.obj170)
      self.obj170.in_connections_.append(self.obj169)
      self.obj169.graphObject_.pendingConnections.append((self.obj169.graphObject_.tag, self.obj170.graphObject_.tag, [53.0, 90.0, 59.0, 129.0, 136.0, 126.5], 2, True))
      self.obj170.out_connections_.append(self.obj168)
      self.obj168.in_connections_.append(self.obj170)
      self.obj170.graphObject_.pendingConnections.append((self.obj170.graphObject_.tag, self.obj168.graphObject_.tag, [204.0, 90.0, 213.0, 124.0, 136.0, 126.5], 2, True))

      self.RHS = ASG_pns2(parent)
      self.RHS.merge(ASG_omacs(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj174=product(parent)
      self.obj174.preAction( self.RHS.CREATE )
      self.obj174.isGraphObjectVisual = True

      if(hasattr(self.obj174, '_setHierarchicalLink')):
        self.obj174._setHierarchicalLink(False)

      # Name
      self.obj174.Name.setValue('')
      self.obj174.Name.setNone()

      self.obj174.GGLabel.setValue(4)
      self.obj174.graphClass_= graph_product
      if parent.genGraphics:
         new_obj = graph_product(360.0,40.0,self.obj174)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj174.graphObject_ = new_obj
      self.obj1740= AttrCalc()
      self.obj1740.Copy=ATOM3Boolean()
      self.obj1740.Copy.setValue(('Copy from LHS', 1))
      self.obj1740.Copy.config = 0
      self.obj1740.Specify=ATOM3Constraint()
      self.obj1740.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj174.GGset2Any['Name']= self.obj1740

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj174)
      self.obj174.postAction( self.RHS.CREATE )

      self.obj175=metarial(parent)
      self.obj175.preAction( self.RHS.CREATE )
      self.obj175.isGraphObjectVisual = True

      if(hasattr(self.obj175, '_setHierarchicalLink')):
        self.obj175._setHierarchicalLink(False)

      # Name
      self.obj175.Name.setValue('')
      self.obj175.Name.setNone()

      self.obj175.GGLabel.setValue(2)
      self.obj175.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(240.0,40.0,self.obj175)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj175.graphObject_ = new_obj
      self.obj1750= AttrCalc()
      self.obj1750.Copy=ATOM3Boolean()
      self.obj1750.Copy.setValue(('Copy from LHS', 1))
      self.obj1750.Copy.config = 0
      self.obj1750.Specify=ATOM3Constraint()
      self.obj1750.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj175.GGset2Any['Name']= self.obj1750

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj175)
      self.obj175.postAction( self.RHS.CREATE )

      self.obj176=operatingUnit(parent)
      self.obj176.preAction( self.RHS.CREATE )
      self.obj176.isGraphObjectVisual = True

      if(hasattr(self.obj176, '_setHierarchicalLink')):
        self.obj176._setHierarchicalLink(False)

      self.obj176.GGLabel.setValue(5)
      self.obj176.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(300.0,120.0,self.obj176)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj176.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj176)
      self.obj176.postAction( self.RHS.CREATE )

      self.obj177=intoProduct(parent)
      self.obj177.preAction( self.RHS.CREATE )
      self.obj177.isGraphObjectVisual = True

      if(hasattr(self.obj177, '_setHierarchicalLink')):
        self.obj177._setHierarchicalLink(False)

      # rate
      self.obj177.rate.setValue(0.0)

      self.obj177.GGLabel.setValue(7)
      self.obj177.graphClass_= graph_intoProduct
      if parent.genGraphics:
         new_obj = graph_intoProduct(328.0,48.5,self.obj177)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj177.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj177)
      self.obj177.postAction( self.RHS.CREATE )

      self.obj178=fromMaterial(parent)
      self.obj178.preAction( self.RHS.CREATE )
      self.obj178.isGraphObjectVisual = True

      if(hasattr(self.obj178, '_setHierarchicalLink')):
        self.obj178._setHierarchicalLink(False)

      # rate
      self.obj178.rate.setValue(0.0)

      self.obj178.GGLabel.setValue(6)
      self.obj178.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(306.0,171.0,self.obj178)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj178.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj178)
      self.obj178.postAction( self.RHS.CREATE )

      self.obj179=Goal(parent)
      self.obj179.preAction( self.RHS.CREATE )
      self.obj179.isGraphObjectVisual = True

      if(hasattr(self.obj179, '_setHierarchicalLink')):
        self.obj179._setHierarchicalLink(False)

      # name
      self.obj179.name.setValue('')
      self.obj179.name.setNone()

      self.obj179.GGLabel.setValue(1)
      self.obj179.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(60.0,40.0,self.obj179)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj179.graphObject_ = new_obj
      self.obj1790= AttrCalc()
      self.obj1790.Copy=ATOM3Boolean()
      self.obj1790.Copy.setValue(('Copy from LHS', 1))
      self.obj1790.Copy.config = 0
      self.obj1790.Specify=ATOM3Constraint()
      self.obj1790.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj179.GGset2Any['name']= self.obj1790

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj179)
      self.obj179.postAction( self.RHS.CREATE )

      self.obj180=GenericGraphEdge(parent)
      self.obj180.preAction( self.RHS.CREATE )
      self.obj180.isGraphObjectVisual = True

      if(hasattr(self.obj180, '_setHierarchicalLink')):
        self.obj180._setHierarchicalLink(False)

      self.obj180.GGLabel.setValue(3)
      self.obj180.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(199.0,133.0,self.obj180)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj180.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj180)
      self.obj180.postAction( self.RHS.CREATE )

      self.obj175.out_connections_.append(self.obj178)
      self.obj178.in_connections_.append(self.obj175)
      self.obj175.graphObject_.pendingConnections.append((self.obj175.graphObject_.tag, self.obj178.graphObject_.tag, [264.0, 90.0, 274.0, 173.0, 306.0, 171.0], 2, True))
      self.obj176.out_connections_.append(self.obj177)
      self.obj177.in_connections_.append(self.obj176)
      self.obj176.graphObject_.pendingConnections.append((self.obj176.graphObject_.tag, self.obj177.graphObject_.tag, [322.0, 123.0, 330.0, 71.0, 328.0, 48.5], 2, True))
      self.obj177.out_connections_.append(self.obj174)
      self.obj174.in_connections_.append(self.obj177)
      self.obj177.graphObject_.pendingConnections.append((self.obj177.graphObject_.tag, self.obj174.graphObject_.tag, [387.0, 39.0, 326.0, 26.0, 328.0, 48.5], 2, True))
      self.obj178.out_connections_.append(self.obj176)
      self.obj176.in_connections_.append(self.obj178)
      self.obj178.graphObject_.pendingConnections.append((self.obj178.graphObject_.tag, self.obj176.graphObject_.tag, [323.0, 138.0, 338.0, 169.0, 306.0, 171.0], 2, True))
      self.obj179.out_connections_.append(self.obj180)
      self.obj180.in_connections_.append(self.obj179)
      self.obj179.graphObject_.pendingConnections.append((self.obj179.graphObject_.tag, self.obj180.graphObject_.tag, [93.0, 110.0, 126.0, 142.0, 199.0, 133.0], 2, True))
      self.obj180.out_connections_.append(self.obj175)
      self.obj175.in_connections_.append(self.obj180)
      self.obj180.graphObject_.pendingConnections.append((self.obj180.graphObject_.tag, self.obj175.graphObject_.tag, [264.0, 90.0, 272.0, 124.0, 199.0, 133.0], 2, True))

   def condition(self, graphID, isograph, atom3i):
      # If you want to apply this rule at most once on asingle host graph node, 
      # then uncomment the next two lines. Change the default GG label (1) if needed.
      
      # Make sure to enable the ACTION code as well
      # And to use the same label & unique name in the ACTION
      # WARNING: _uniqueName23 is not guaranteed to be unique (so change it, be safe!)
      
      #node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      #return not hasattr(node, "_uniqueName23")
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      return not hasattr(node, "OpUnitM_OAF")
      
      

   def action(self, graphID, isograph, atom3i):
      # If you want to apply this rule at most once on asingle host graph node, 
      # then uncomment the next two lines. Change the default GG label (1) if needed.
      
      # Make sure to enable the CONDITION code as well
      # And to use the same label & unique name in the ACTION
      # WARNING: _uniqueName23 is not guaranteed to be unique (so change it, be safe!)
      
      #node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      #node._uniqueName23 = True
      
      node = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) )
      node.OpUnitM_OAF  = True  
      

