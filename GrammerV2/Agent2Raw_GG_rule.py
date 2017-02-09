# _ Agent2Raw_GG_rule.py ____________________________________________________________________________
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
class Agent2Raw_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 6)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_pns2(parent)
      self.LHS.merge(ASG_omacs(parent))

      self.obj86=Agent(parent)
      self.obj86.preAction( self.LHS.CREATE )
      self.obj86.isGraphObjectVisual = True

      if(hasattr(self.obj86, '_setHierarchicalLink')):
        self.obj86._setHierarchicalLink(False)

      # price
      self.obj86.price.setValue(0)

      # name
      self.obj86.name.setValue('')
      self.obj86.name.setNone()

      self.obj86.GGLabel.setValue(1)
      self.obj86.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(60.0,40.0,self.obj86)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj86.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj86)
      self.obj86.postAction( self.LHS.CREATE )


      self.RHS = ASG_pns2(parent)
      self.RHS.merge(ASG_omacs(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj90=rawMaterial(parent)
      self.obj90.preAction( self.RHS.CREATE )
      self.obj90.isGraphObjectVisual = True

      if(hasattr(self.obj90, '_setHierarchicalLink')):
        self.obj90._setHierarchicalLink(False)

      # Name
      self.obj90.Name.setValue('')
      self.obj90.Name.setNone()

      self.obj90.GGLabel.setValue(3)
      self.obj90.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(260.0,40.0,self.obj90)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj90.graphObject_ = new_obj
      self.obj900= AttrCalc()
      self.obj900.Copy=ATOM3Boolean()
      self.obj900.Copy.setValue(('Copy from LHS', 0))
      self.obj900.Copy.config = 0
      self.obj900.Specify=ATOM3Constraint()
      self.obj900.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# Template for typical GG specify code (specified field is a string)\n# See atom3\\Kernel\\ATOM3Types directory for info on specific types\n\n# return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).Name.getValue()\n\n# "self.LHS.nodeWithLabel(1)" gets the node with GG label 1 in the LHS of the GG\n# "self.getMatched(graphID, self.LHS.nodeWithLabel(1))" gets node in host graph\n# ".Name" will access that node\'s Name attribute, an ATOM3 string object\n# ".getValue()" will return the ATOM3 string as a regular Python string\n# Finally, a Python string is returned, and becomes the value of the specified\n# field\n\n# A more complicated template (specified field is an integer)\n\n# # Source loses one car\n# sourceNode = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\n# currentNumCars = sourceNode.num_vehicles.getValue()\n# # If source has an infinite supply (infinite_supply = ATOM3 boolean value)\n# if(source.infinite_supply.getValueBoolean()): \n#     return currentNumCars\n# return currentNumCars - 1\nreturn self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()\n'))
      self.obj90.GGset2Any['Name']= self.obj900

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj90)
      self.obj90.postAction( self.RHS.CREATE )

      self.obj91=Agent(parent)
      self.obj91.preAction( self.RHS.CREATE )
      self.obj91.isGraphObjectVisual = True

      if(hasattr(self.obj91, '_setHierarchicalLink')):
        self.obj91._setHierarchicalLink(False)

      # price
      self.obj91.price.setValue(0)

      # name
      self.obj91.name.setValue('')
      self.obj91.name.setNone()

      self.obj91.GGLabel.setValue(1)
      self.obj91.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(60.0,40.0,self.obj91)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj91.graphObject_ = new_obj
      self.obj910= AttrCalc()
      self.obj910.Copy=ATOM3Boolean()
      self.obj910.Copy.setValue(('Copy from LHS', 1))
      self.obj910.Copy.config = 0
      self.obj910.Specify=ATOM3Constraint()
      self.obj910.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj91.GGset2Any['price']= self.obj910
      self.obj911= AttrCalc()
      self.obj911.Copy=ATOM3Boolean()
      self.obj911.Copy.setValue(('Copy from LHS', 1))
      self.obj911.Copy.config = 0
      self.obj911.Specify=ATOM3Constraint()
      self.obj911.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj91.GGset2Any['name']= self.obj911

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj91)
      self.obj91.postAction( self.RHS.CREATE )

      self.obj92=GenericGraphEdge(parent)
      self.obj92.preAction( self.RHS.CREATE )
      self.obj92.isGraphObjectVisual = True

      if(hasattr(self.obj92, '_setHierarchicalLink')):
        self.obj92._setHierarchicalLink(False)

      self.obj92.GGLabel.setValue(4)
      self.obj92.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(225.0,158.0,self.obj92)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj92.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj92)
      self.obj92.postAction( self.RHS.CREATE )

      self.obj91.out_connections_.append(self.obj92)
      self.obj92.in_connections_.append(self.obj91)
      self.obj91.graphObject_.pendingConnections.append((self.obj91.graphObject_.tag, self.obj92.graphObject_.tag, [94.0, 126.0, 159.0, 168.0, 225.0, 158.0], 2, True))
      self.obj92.out_connections_.append(self.obj90)
      self.obj90.in_connections_.append(self.obj92)
      self.obj92.graphObject_.pendingConnections.append((self.obj92.graphObject_.tag, self.obj90.graphObject_.tag, [284.0, 93.0, 291.0, 148.0, 225.0, 158.0], 2, True))

   def condition(self, graphID, isograph, atom3i):
      # If you want to apply this rule at most once on asingle host graph node, 
      # then uncomment the next two lines. Change the default GG label (1) if needed.
      
      # Make sure to enable the ACTION code as well
      # And to use the same label & unique name in the ACTION
      # WARNING: _uniqueName56 is not guaranteed to be unique (so change it, be safe!)
      
      #node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      #return not hasattr(node, "_uniqueName56")
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      return not hasattr(node, "Agent2Raw")
      
      

   def action(self, graphID, isograph, atom3i):
      # If you want to apply this rule at most once on asingle host graph node, 
      # then uncomment the next two lines. Change the default GG label (1) if needed.
      
      # Make sure to enable the CONDITION code as well
      # And to use the same label & unique name in the ACTION
      # WARNING: _uniqueName56 is not guaranteed to be unique (so change it, be safe!)
      
      #node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      #node._uniqueName56 = True
      node = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) )
      node.Agent2Raw = True 
      

