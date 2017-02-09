# _ Goal2Matr_GG_rule.py ____________________________________________________________________________
# File generated automatically by ATOM3. Graph Grammar Rule
# ___________________________________________________________________________________________
from GGrule import *
from Capabilitie import *
from rawMaterial import *
from Goal import *
from intoProduct import *
from operatingUnit import *
from metarial import *
from product import *
from Agent import *
from fromMaterial import *
from CapableOf import *
from Role import *
from fromRaw import *
from ASG_pns2 import *
from intoMaterial import *
from ASG_omacs import *
from require import *
from achieve import *
from posses import *
from GenericGraphEdge import *
from GenericGraphNode import *
from ASG_GenericGraph import *
class Goal2Matr_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 7)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_pns2(parent)
      self.LHS.merge(ASG_omacs(parent))

      self.obj98=Goal(parent)
      self.obj98.preAction( self.LHS.CREATE )
      self.obj98.isGraphObjectVisual = True

      if(hasattr(self.obj98, '_setHierarchicalLink')):
        self.obj98._setHierarchicalLink(False)

      # name
      self.obj98.name.setValue('')
      self.obj98.name.setNone()

      self.obj98.GGLabel.setValue(1)
      self.obj98.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(120.0,40.0,self.obj98)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj98.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj98)
      self.obj98.postAction( self.LHS.CREATE )


      self.RHS = ASG_pns2(parent)
      self.RHS.merge(ASG_omacs(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj102=metarial(parent)
      self.obj102.preAction( self.RHS.CREATE )
      self.obj102.isGraphObjectVisual = True

      if(hasattr(self.obj102, '_setHierarchicalLink')):
        self.obj102._setHierarchicalLink(False)

      # Name
      self.obj102.Name.setValue('')
      self.obj102.Name.setNone()

      self.obj102.GGLabel.setValue(3)
      self.obj102.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(260.0,40.0,self.obj102)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj102.graphObject_ = new_obj
      self.obj1020= AttrCalc()
      self.obj1020.Copy=ATOM3Boolean()
      self.obj1020.Copy.setValue(('Copy from LHS', 0))
      self.obj1020.Copy.config = 0
      self.obj1020.Specify=ATOM3Constraint()
      self.obj1020.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# Template for typical GG specify code (specified field is a string)\n# See atom3\\Kernel\\ATOM3Types directory for info on specific types\n\n# return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).Name.getValue()\n\n# "self.LHS.nodeWithLabel(1)" gets the node with GG label 1 in the LHS of the GG\n# "self.getMatched(graphID, self.LHS.nodeWithLabel(1))" gets node in host graph\n# ".Name" will access that node\'s Name attribute, an ATOM3 string object\n# ".getValue()" will return the ATOM3 string as a regular Python string\n# Finally, a Python string is returned, and becomes the value of the specified\n# field\n\n# A more complicated template (specified field is an integer)\n\n# # Source loses one car\n# sourceNode = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\n# currentNumCars = sourceNode.num_vehicles.getValue()\n# # If source has an infinite supply (infinite_supply = ATOM3 boolean value)\n# if(source.infinite_supply.getValueBoolean()): \n#     return currentNumCars\n# return currentNumCars - 1\nreturn self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()\n\n'))
      self.obj102.GGset2Any['Name']= self.obj1020

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj102)
      self.obj102.postAction( self.RHS.CREATE )

      self.obj103=Goal(parent)
      self.obj103.preAction( self.RHS.CREATE )
      self.obj103.isGraphObjectVisual = True

      if(hasattr(self.obj103, '_setHierarchicalLink')):
        self.obj103._setHierarchicalLink(False)

      # name
      self.obj103.name.setValue('')
      self.obj103.name.setNone()

      self.obj103.GGLabel.setValue(1)
      self.obj103.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(60.0,60.0,self.obj103)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj103.graphObject_ = new_obj
      self.obj1030= AttrCalc()
      self.obj1030.Copy=ATOM3Boolean()
      self.obj1030.Copy.setValue(('Copy from LHS', 1))
      self.obj1030.Copy.config = 0
      self.obj1030.Specify=ATOM3Constraint()
      self.obj1030.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj103.GGset2Any['name']= self.obj1030

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj103)
      self.obj103.postAction( self.RHS.CREATE )

      self.obj104=GenericGraphEdge(parent)
      self.obj104.preAction( self.RHS.CREATE )
      self.obj104.isGraphObjectVisual = True

      if(hasattr(self.obj104, '_setHierarchicalLink')):
        self.obj104._setHierarchicalLink(False)

      self.obj104.GGLabel.setValue(4)
      self.obj104.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(189.0,162.5,self.obj104)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj104.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj104)
      self.obj104.postAction( self.RHS.CREATE )

      self.obj103.out_connections_.append(self.obj104)
      self.obj104.in_connections_.append(self.obj103)
      self.obj103.graphObject_.pendingConnections.append((self.obj103.graphObject_.tag, self.obj104.graphObject_.tag, [94.0, 130.0, 94.0, 163.0, 189.0, 162.5], 2, True))
      self.obj104.out_connections_.append(self.obj102)
      self.obj102.in_connections_.append(self.obj104)
      self.obj104.graphObject_.pendingConnections.append((self.obj104.graphObject_.tag, self.obj102.graphObject_.tag, [284.0, 90.0, 284.0, 162.0, 189.0, 162.5], 2, True))

   def condition(self, graphID, isograph, atom3i):
      # If you want to apply this rule at most once on asingle host graph node, 
      # then uncomment the next two lines. Change the default GG label (1) if needed.
      
      # Make sure to enable the ACTION code as well
      # And to use the same label & unique name in the ACTION
      # WARNING: _uniqueName43 is not guaranteed to be unique (so change it, be safe!)
      
      #node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      #return not hasattr(node, "_uniqueName43")
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      return not hasattr(node, "Goal2Mat")
      

   def action(self, graphID, isograph, atom3i):
      # If you want to apply this rule at most once on asingle host graph node, 
      # then uncomment the next two lines. Change the default GG label (1) if needed.
      
      # Make sure to enable the CONDITION code as well
      # And to use the same label & unique name in the ACTION
      # WARNING: _uniqueName43 is not guaranteed to be unique (so change it, be safe!)
      
      #node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      #node._uniqueName43 = True
      node = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) )
      node.Goal2Mat = True 
      

