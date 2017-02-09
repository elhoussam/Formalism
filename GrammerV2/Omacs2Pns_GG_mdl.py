from GraphGrammarEdit import *
from GGruleEdit import *

def savedTrans(self):
   self.EditingGraphGrammar= GraphGrammarEdit(None, self)
   self.EditingGraphGrammar.Name=ATOM3String('Omacs2Pns', 20)
   self.EditingGraphGrammar.Rules=ATOM3List([ 1, 1, 1, 0],GGruleEdit,None, self)
   lcobj0=[]
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('OpUnit4AR', 20)
   cobj0.Order=ATOM3Integer(5)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

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

   cobj0.LHS = ASG_pns2(self)
   cobj0.LHS.merge(ASG_omacs(self))

   self.obj70=CapableOf(self)
   self.obj70.preAction( cobj0.LHS.CREATE )
   self.obj70.isGraphObjectVisual = True

   if(hasattr(self.obj70, '_setHierarchicalLink')):
     self.obj70._setHierarchicalLink(False)

   self.obj70.GGLabel.setValue(3)
   self.obj70.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(204.0,100.5,self.obj70)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj70.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj70)
   self.obj70.postAction( cobj0.LHS.CREATE )

   self.obj71=Agent(self)
   self.obj71.preAction( cobj0.LHS.CREATE )
   self.obj71.isGraphObjectVisual = True

   if(hasattr(self.obj71, '_setHierarchicalLink')):
     self.obj71._setHierarchicalLink(False)

   # price
   self.obj71.price.setValue(0)

   # name
   self.obj71.name.setValue('')
   self.obj71.name.setNone()

   self.obj71.GGLabel.setValue(1)
   self.obj71.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(40.0,0.0,self.obj71)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj71.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj71)
   self.obj71.postAction( cobj0.LHS.CREATE )

   self.obj72=Role(self)
   self.obj72.preAction( cobj0.LHS.CREATE )
   self.obj72.isGraphObjectVisual = True

   if(hasattr(self.obj72, '_setHierarchicalLink')):
     self.obj72._setHierarchicalLink(False)

   # name
   self.obj72.name.setValue('')
   self.obj72.name.setNone()

   self.obj72.GGLabel.setValue(2)
   self.obj72.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(300.0,120.0,self.obj72)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj72.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj72)
   self.obj72.postAction( cobj0.LHS.CREATE )

   self.obj70.out_connections_.append(self.obj72)
   self.obj72.in_connections_.append(self.obj70)
   self.obj70.graphObject_.pendingConnections.append((self.obj70.graphObject_.tag, self.obj72.graphObject_.tag, [330.0, 120.0, 247.0, 55.0, 204.0, 100.5], 2, True))
   self.obj71.out_connections_.append(self.obj70)
   self.obj70.in_connections_.append(self.obj71)
   self.obj71.graphObject_.pendingConnections.append((self.obj71.graphObject_.tag, self.obj70.graphObject_.tag, [72.0, 86.0, 161.0, 146.0, 204.0, 100.5], 2, True))

   cobj0.RHS = ASG_pns2(self)
   cobj0.RHS.merge(ASG_omacs(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj76=operatingUnit(self)
   self.obj76.preAction( cobj0.RHS.CREATE )
   self.obj76.isGraphObjectVisual = True

   if(hasattr(self.obj76, '_setHierarchicalLink')):
     self.obj76._setHierarchicalLink(False)

   self.obj76.GGLabel.setValue(5)
   self.obj76.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(280.0,40.0,self.obj76)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj76.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj76)
   self.obj76.postAction( cobj0.RHS.CREATE )

   self.obj77=CapableOf(self)
   self.obj77.preAction( cobj0.RHS.CREATE )
   self.obj77.isGraphObjectVisual = True

   if(hasattr(self.obj77, '_setHierarchicalLink')):
     self.obj77._setHierarchicalLink(False)

   self.obj77.GGLabel.setValue(3)
   self.obj77.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(204.0,100.5,self.obj77)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj77.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj77)
   self.obj77.postAction( cobj0.RHS.CREATE )

   self.obj78=Agent(self)
   self.obj78.preAction( cobj0.RHS.CREATE )
   self.obj78.isGraphObjectVisual = True

   if(hasattr(self.obj78, '_setHierarchicalLink')):
     self.obj78._setHierarchicalLink(False)

   # price
   self.obj78.price.setValue(0)

   # name
   self.obj78.name.setValue('')
   self.obj78.name.setNone()

   self.obj78.GGLabel.setValue(1)
   self.obj78.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(40.0,0.0,self.obj78)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj78.graphObject_ = new_obj
   self.obj780= AttrCalc()
   self.obj780.Copy=ATOM3Boolean()
   self.obj780.Copy.setValue(('Copy from LHS', 1))
   self.obj780.Copy.config = 0
   self.obj780.Specify=ATOM3Constraint()
   self.obj780.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj78.GGset2Any['price']= self.obj780
   self.obj781= AttrCalc()
   self.obj781.Copy=ATOM3Boolean()
   self.obj781.Copy.setValue(('Copy from LHS', 1))
   self.obj781.Copy.config = 0
   self.obj781.Specify=ATOM3Constraint()
   self.obj781.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj78.GGset2Any['name']= self.obj781

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj78)
   self.obj78.postAction( cobj0.RHS.CREATE )

   self.obj79=Role(self)
   self.obj79.preAction( cobj0.RHS.CREATE )
   self.obj79.isGraphObjectVisual = True

   if(hasattr(self.obj79, '_setHierarchicalLink')):
     self.obj79._setHierarchicalLink(False)

   # name
   self.obj79.name.setValue('')
   self.obj79.name.setNone()

   self.obj79.GGLabel.setValue(2)
   self.obj79.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(300.0,120.0,self.obj79)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj79.graphObject_ = new_obj
   self.obj790= AttrCalc()
   self.obj790.Copy=ATOM3Boolean()
   self.obj790.Copy.setValue(('Copy from LHS', 1))
   self.obj790.Copy.config = 0
   self.obj790.Specify=ATOM3Constraint()
   self.obj790.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj79.GGset2Any['name']= self.obj790

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj79)
   self.obj79.postAction( cobj0.RHS.CREATE )

   self.obj80=GenericGraphEdge(self)
   self.obj80.preAction( cobj0.RHS.CREATE )
   self.obj80.isGraphObjectVisual = True

   if(hasattr(self.obj80, '_setHierarchicalLink')):
     self.obj80._setHierarchicalLink(False)

   self.obj80.GGLabel.setValue(6)
   self.obj80.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(240.75,24.25,self.obj80)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj80.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj80)
   self.obj80.postAction( cobj0.RHS.CREATE )

   self.obj77.out_connections_.append(self.obj79)
   self.obj79.in_connections_.append(self.obj77)
   self.obj77.graphObject_.pendingConnections.append((self.obj77.graphObject_.tag, self.obj79.graphObject_.tag, [331.0, 120.0, 204.0, 100.5], 2, 0))
   self.obj78.out_connections_.append(self.obj77)
   self.obj77.in_connections_.append(self.obj78)
   self.obj78.graphObject_.pendingConnections.append((self.obj78.graphObject_.tag, self.obj77.graphObject_.tag, [74.0, 86.0, 204.0, 100.5], 2, 0))
   self.obj78.out_connections_.append(self.obj80)
   self.obj80.in_connections_.append(self.obj78)
   self.obj78.graphObject_.pendingConnections.append((self.obj78.graphObject_.tag, self.obj80.graphObject_.tag, [74.0, 86.0, 200.5, 40.0, 173.0, 72.0, 240.75, 24.25], 4, True))
   self.obj80.out_connections_.append(self.obj76)
   self.obj76.in_connections_.append(self.obj80)
   self.obj80.graphObject_.pendingConnections.append((self.obj80.graphObject_.tag, self.obj76.graphObject_.tag, [347.0, 41.0, 281.0, 8.5, 334.0, 9.0, 240.75, 24.25], 4, True))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# If you want to apply this rule at most once on asingle host graph node, \n# then uncomment the next two lines. Change the default GG label (1) if needed.\n\n# Make sure to enable the ACTION code as well\n# And to use the same label & unique name in the ACTION\n# WARNING: _uniqueName2 is not guaranteed to be unique (so change it, be safe!)\n\n#node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\n#return not hasattr(node, "_uniqueName2")\nnode = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nnode2 = self.getMatched(graphID, self.LHS.nodeWithLabel(2))\nreturn not(  hasattr(node, "_rule_1_executed_already") and hasattr(node2, "_rule_1_executed_already") )\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# If you want to apply this rule at most once on asingle host graph node, \n# then uncomment the next two lines. Change the default GG label (1) if needed.\n\n# Make sure to enable the CONDITION code as well\n# And to use the same label & unique name in the ACTION\n# WARNING: _uniqueName2 is not guaranteed to be unique (so change it, be safe!)\n\n#node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\n#node._uniqueName2 = True\nnode = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) )\nnode._rule_1_executed_already = True \nnode = self.getMatched ( graphID , self.LHS.nodeWithLabel(2) )\nnode._rule_1_executed_already = True \n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('Agent2Raw', 20)
   cobj0.Order=ATOM3Integer(6)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

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

   cobj0.LHS = ASG_pns2(self)
   cobj0.LHS.merge(ASG_omacs(self))

   self.obj86=Agent(self)
   self.obj86.preAction( cobj0.LHS.CREATE )
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
   if self.genGraphics:
      new_obj = graph_Agent(60.0,40.0,self.obj86)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj86.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj86)
   self.obj86.postAction( cobj0.LHS.CREATE )


   cobj0.RHS = ASG_pns2(self)
   cobj0.RHS.merge(ASG_omacs(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj90=rawMaterial(self)
   self.obj90.preAction( cobj0.RHS.CREATE )
   self.obj90.isGraphObjectVisual = True

   if(hasattr(self.obj90, '_setHierarchicalLink')):
     self.obj90._setHierarchicalLink(False)

   # Name
   self.obj90.Name.setValue('')
   self.obj90.Name.setNone()

   self.obj90.GGLabel.setValue(3)
   self.obj90.graphClass_= graph_rawMaterial
   if self.genGraphics:
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

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj90)
   self.obj90.postAction( cobj0.RHS.CREATE )

   self.obj91=Agent(self)
   self.obj91.preAction( cobj0.RHS.CREATE )
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
   if self.genGraphics:
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

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj91)
   self.obj91.postAction( cobj0.RHS.CREATE )

   self.obj92=GenericGraphEdge(self)
   self.obj92.preAction( cobj0.RHS.CREATE )
   self.obj92.isGraphObjectVisual = True

   if(hasattr(self.obj92, '_setHierarchicalLink')):
     self.obj92._setHierarchicalLink(False)

   self.obj92.GGLabel.setValue(4)
   self.obj92.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(225.0,158.0,self.obj92)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj92.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj92)
   self.obj92.postAction( cobj0.RHS.CREATE )

   self.obj91.out_connections_.append(self.obj92)
   self.obj92.in_connections_.append(self.obj91)
   self.obj91.graphObject_.pendingConnections.append((self.obj91.graphObject_.tag, self.obj92.graphObject_.tag, [94.0, 126.0, 159.0, 168.0, 225.0, 158.0], 2, True))
   self.obj92.out_connections_.append(self.obj90)
   self.obj90.in_connections_.append(self.obj92)
   self.obj92.graphObject_.pendingConnections.append((self.obj92.graphObject_.tag, self.obj90.graphObject_.tag, [284.0, 93.0, 291.0, 148.0, 225.0, 158.0], 2, True))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# If you want to apply this rule at most once on asingle host graph node, \n# then uncomment the next two lines. Change the default GG label (1) if needed.\n\n# Make sure to enable the ACTION code as well\n# And to use the same label & unique name in the ACTION\n# WARNING: _uniqueName56 is not guaranteed to be unique (so change it, be safe!)\n\n#node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\n#return not hasattr(node, "_uniqueName56")\nnode = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nreturn not hasattr(node, "Agent2Raw")\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# If you want to apply this rule at most once on asingle host graph node, \n# then uncomment the next two lines. Change the default GG label (1) if needed.\n\n# Make sure to enable the CONDITION code as well\n# And to use the same label & unique name in the ACTION\n# WARNING: _uniqueName56 is not guaranteed to be unique (so change it, be safe!)\n\n#node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\n#node._uniqueName56 = True\nnode = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) )\nnode.Agent2Raw = True \n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('Goal2Matr', 20)
   cobj0.Order=ATOM3Integer(7)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

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

   cobj0.LHS = ASG_pns2(self)
   cobj0.LHS.merge(ASG_omacs(self))

   self.obj98=Goal(self)
   self.obj98.preAction( cobj0.LHS.CREATE )
   self.obj98.isGraphObjectVisual = True

   if(hasattr(self.obj98, '_setHierarchicalLink')):
     self.obj98._setHierarchicalLink(False)

   # name
   self.obj98.name.setValue('')
   self.obj98.name.setNone()

   self.obj98.GGLabel.setValue(1)
   self.obj98.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(120.0,40.0,self.obj98)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj98.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj98)
   self.obj98.postAction( cobj0.LHS.CREATE )


   cobj0.RHS = ASG_pns2(self)
   cobj0.RHS.merge(ASG_omacs(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj102=metarial(self)
   self.obj102.preAction( cobj0.RHS.CREATE )
   self.obj102.isGraphObjectVisual = True

   if(hasattr(self.obj102, '_setHierarchicalLink')):
     self.obj102._setHierarchicalLink(False)

   # Name
   self.obj102.Name.setValue('')
   self.obj102.Name.setNone()

   self.obj102.GGLabel.setValue(3)
   self.obj102.graphClass_= graph_metarial
   if self.genGraphics:
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

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj102)
   self.obj102.postAction( cobj0.RHS.CREATE )

   self.obj103=Goal(self)
   self.obj103.preAction( cobj0.RHS.CREATE )
   self.obj103.isGraphObjectVisual = True

   if(hasattr(self.obj103, '_setHierarchicalLink')):
     self.obj103._setHierarchicalLink(False)

   # name
   self.obj103.name.setValue('')
   self.obj103.name.setNone()

   self.obj103.GGLabel.setValue(1)
   self.obj103.graphClass_= graph_Goal
   if self.genGraphics:
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

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj103)
   self.obj103.postAction( cobj0.RHS.CREATE )

   self.obj104=GenericGraphEdge(self)
   self.obj104.preAction( cobj0.RHS.CREATE )
   self.obj104.isGraphObjectVisual = True

   if(hasattr(self.obj104, '_setHierarchicalLink')):
     self.obj104._setHierarchicalLink(False)

   self.obj104.GGLabel.setValue(4)
   self.obj104.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(189.0,162.5,self.obj104)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj104.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj104)
   self.obj104.postAction( cobj0.RHS.CREATE )

   self.obj103.out_connections_.append(self.obj104)
   self.obj104.in_connections_.append(self.obj103)
   self.obj103.graphObject_.pendingConnections.append((self.obj103.graphObject_.tag, self.obj104.graphObject_.tag, [94.0, 130.0, 94.0, 163.0, 189.0, 162.5], 2, True))
   self.obj104.out_connections_.append(self.obj102)
   self.obj102.in_connections_.append(self.obj104)
   self.obj104.graphObject_.pendingConnections.append((self.obj104.graphObject_.tag, self.obj102.graphObject_.tag, [284.0, 90.0, 284.0, 162.0, 189.0, 162.5], 2, True))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# If you want to apply this rule at most once on asingle host graph node, \n# then uncomment the next two lines. Change the default GG label (1) if needed.\n\n# Make sure to enable the ACTION code as well\n# And to use the same label & unique name in the ACTION\n# WARNING: _uniqueName43 is not guaranteed to be unique (so change it, be safe!)\n\n#node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\n#return not hasattr(node, "_uniqueName43")\nnode = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nreturn not hasattr(node, "Goal2Mat")\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# If you want to apply this rule at most once on asingle host graph node, \n# then uncomment the next two lines. Change the default GG label (1) if needed.\n\n# Make sure to enable the CONDITION code as well\n# And to use the same label & unique name in the ACTION\n# WARNING: _uniqueName43 is not guaranteed to be unique (so change it, be safe!)\n\n#node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\n#node._uniqueName43 = True\nnode = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) )\nnode.Goal2Mat = True \n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('LinkRaw2AR', 20)
   cobj0.Order=ATOM3Integer(8)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

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

   cobj0.LHS = ASG_pns2(self)
   cobj0.LHS.merge(ASG_omacs(self))
   cobj0.LHS.merge(ASG_GenericGraph(self))

   self.obj289=rawMaterial(self)
   self.obj289.preAction( cobj0.LHS.CREATE )
   self.obj289.isGraphObjectVisual = True

   if(hasattr(self.obj289, '_setHierarchicalLink')):
     self.obj289._setHierarchicalLink(False)

   # Name
   self.obj289.Name.setValue('')
   self.obj289.Name.setNone()

   self.obj289.GGLabel.setValue(1)
   self.obj289.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(280.0,60.0,self.obj289)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj289.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj289)
   self.obj289.postAction( cobj0.LHS.CREATE )

   self.obj291=operatingUnit(self)
   self.obj291.preAction( cobj0.LHS.CREATE )
   self.obj291.isGraphObjectVisual = True

   if(hasattr(self.obj291, '_setHierarchicalLink')):
     self.obj291._setHierarchicalLink(False)

   self.obj291.GGLabel.setValue(3)
   self.obj291.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(280.0,240.0,self.obj291)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj291.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj291)
   self.obj291.postAction( cobj0.LHS.CREATE )

   self.obj304=Agent(self)
   self.obj304.preAction( cobj0.LHS.CREATE )
   self.obj304.isGraphObjectVisual = True

   if(hasattr(self.obj304, '_setHierarchicalLink')):
     self.obj304._setHierarchicalLink(False)

   # price
   self.obj304.price.setValue(0)

   # name
   self.obj304.name.setValue('')
   self.obj304.name.setNone()

   self.obj304.GGLabel.setValue(5)
   self.obj304.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(20.0,120.0,self.obj304)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj304.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj304)
   self.obj304.postAction( cobj0.LHS.CREATE )

   self.obj309=GenericGraphEdge(self)
   self.obj309.preAction( cobj0.LHS.CREATE )
   self.obj309.isGraphObjectVisual = True

   if(hasattr(self.obj309, '_setHierarchicalLink')):
     self.obj309._setHierarchicalLink(False)

   self.obj309.GGLabel.setValue(6)
   self.obj309.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(264.0,158.75,self.obj309)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj309.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj309)
   self.obj309.postAction( cobj0.LHS.CREATE )

   self.obj310=GenericGraphEdge(self)
   self.obj310.preAction( cobj0.LHS.CREATE )
   self.obj310.isGraphObjectVisual = True

   if(hasattr(self.obj310, '_setHierarchicalLink')):
     self.obj310._setHierarchicalLink(False)

   self.obj310.GGLabel.setValue(7)
   self.obj310.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(262.75,206.25,self.obj310)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj310.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj310)
   self.obj310.postAction( cobj0.LHS.CREATE )

   self.obj304.out_connections_.append(self.obj309)
   self.obj309.in_connections_.append(self.obj304)
   self.obj304.graphObject_.pendingConnections.append((self.obj304.graphObject_.tag, self.obj309.graphObject_.tag, [52.0, 206.0, 201.0, 182.0, 264.0, 158.75], 2, True))
   self.obj304.out_connections_.append(self.obj310)
   self.obj310.in_connections_.append(self.obj304)
   self.obj304.graphObject_.pendingConnections.append((self.obj304.graphObject_.tag, self.obj310.graphObject_.tag, [52.0, 206.0, 189.0, 197.5, 262.75, 206.25], 2, True))
   self.obj309.out_connections_.append(self.obj289)
   self.obj289.in_connections_.append(self.obj309)
   self.obj309.graphObject_.pendingConnections.append((self.obj309.graphObject_.tag, self.obj289.graphObject_.tag, [304.0, 113.0, 327.0, 135.5, 264.0, 158.75], 2, True))
   self.obj310.out_connections_.append(self.obj291)
   self.obj291.in_connections_.append(self.obj310)
   self.obj310.graphObject_.pendingConnections.append((self.obj310.graphObject_.tag, self.obj291.graphObject_.tag, [347.0, 241.0, 336.5, 215.0, 262.75, 206.25], 2, True))

   cobj0.RHS = ASG_pns2(self)
   cobj0.RHS.merge(ASG_omacs(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj292=rawMaterial(self)
   self.obj292.preAction( cobj0.RHS.CREATE )
   self.obj292.isGraphObjectVisual = True

   if(hasattr(self.obj292, '_setHierarchicalLink')):
     self.obj292._setHierarchicalLink(False)

   # Name
   self.obj292.Name.setValue('')
   self.obj292.Name.setNone()

   self.obj292.GGLabel.setValue(1)
   self.obj292.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(260.0,60.0,self.obj292)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj292.graphObject_ = new_obj
   self.obj2920= AttrCalc()
   self.obj2920.Copy=ATOM3Boolean()
   self.obj2920.Copy.setValue(('Copy from LHS', 1))
   self.obj2920.Copy.config = 0
   self.obj2920.Specify=ATOM3Constraint()
   self.obj2920.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj292.GGset2Any['Name']= self.obj2920

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj292)
   self.obj292.postAction( cobj0.RHS.CREATE )

   self.obj294=operatingUnit(self)
   self.obj294.preAction( cobj0.RHS.CREATE )
   self.obj294.isGraphObjectVisual = True

   if(hasattr(self.obj294, '_setHierarchicalLink')):
     self.obj294._setHierarchicalLink(False)

   self.obj294.GGLabel.setValue(3)
   self.obj294.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(280.0,240.0,self.obj294)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj294.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj294)
   self.obj294.postAction( cobj0.RHS.CREATE )

   self.obj295=fromRaw(self)
   self.obj295.preAction( cobj0.RHS.CREATE )
   self.obj295.isGraphObjectVisual = True

   if(hasattr(self.obj295, '_setHierarchicalLink')):
     self.obj295._setHierarchicalLink(False)

   # rate
   self.obj295.rate.setValue(0.0)

   self.obj295.GGLabel.setValue(4)
   self.obj295.graphClass_= graph_fromRaw
   if self.genGraphics:
      new_obj = graph_fromRaw(293.0,178.0,self.obj295)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj295.graphObject_ = new_obj
   self.obj2950= AttrCalc()
   self.obj2950.Copy=ATOM3Boolean()
   self.obj2950.Copy.setValue(('Copy from LHS', 1))
   self.obj2950.Copy.config = 0
   self.obj2950.Specify=ATOM3Constraint()
   self.obj2950.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj295.GGset2Any['rate']= self.obj2950

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj295)
   self.obj295.postAction( cobj0.RHS.CREATE )

   self.obj319=Agent(self)
   self.obj319.preAction( cobj0.RHS.CREATE )
   self.obj319.isGraphObjectVisual = True

   if(hasattr(self.obj319, '_setHierarchicalLink')):
     self.obj319._setHierarchicalLink(False)

   # price
   self.obj319.price.setValue(0)

   # name
   self.obj319.name.setValue('')
   self.obj319.name.setNone()

   self.obj319.GGLabel.setValue(5)
   self.obj319.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(20.0,120.0,self.obj319)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj319.graphObject_ = new_obj
   self.obj3190= AttrCalc()
   self.obj3190.Copy=ATOM3Boolean()
   self.obj3190.Copy.setValue(('Copy from LHS', 1))
   self.obj3190.Copy.config = 0
   self.obj3190.Specify=ATOM3Constraint()
   self.obj3190.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj319.GGset2Any['price']= self.obj3190
   self.obj3191= AttrCalc()
   self.obj3191.Copy=ATOM3Boolean()
   self.obj3191.Copy.setValue(('Copy from LHS', 1))
   self.obj3191.Copy.config = 0
   self.obj3191.Specify=ATOM3Constraint()
   self.obj3191.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj319.GGset2Any['name']= self.obj3191

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj319)
   self.obj319.postAction( cobj0.RHS.CREATE )

   self.obj324=GenericGraphEdge(self)
   self.obj324.preAction( cobj0.RHS.CREATE )
   self.obj324.isGraphObjectVisual = True

   if(hasattr(self.obj324, '_setHierarchicalLink')):
     self.obj324._setHierarchicalLink(False)

   self.obj324.GGLabel.setValue(6)
   self.obj324.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(205.5,156.75,self.obj324)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj324.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj324)
   self.obj324.postAction( cobj0.RHS.CREATE )

   self.obj325=GenericGraphEdge(self)
   self.obj325.preAction( cobj0.RHS.CREATE )
   self.obj325.isGraphObjectVisual = True

   if(hasattr(self.obj325, '_setHierarchicalLink')):
     self.obj325._setHierarchicalLink(False)

   self.obj325.GGLabel.setValue(7)
   self.obj325.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(215.0,206.75,self.obj325)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj325.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj325)
   self.obj325.postAction( cobj0.RHS.CREATE )

   self.obj292.out_connections_.append(self.obj295)
   self.obj295.in_connections_.append(self.obj292)
   self.obj292.graphObject_.pendingConnections.append((self.obj292.graphObject_.tag, self.obj295.graphObject_.tag, [284.0, 113.0, 293.0, 178.0], 0, True))
   self.obj295.out_connections_.append(self.obj294)
   self.obj294.in_connections_.append(self.obj295)
   self.obj295.graphObject_.pendingConnections.append((self.obj295.graphObject_.tag, self.obj294.graphObject_.tag, [302.0, 243.0, 293.0, 178.0], 0, True))
   self.obj319.out_connections_.append(self.obj324)
   self.obj324.in_connections_.append(self.obj319)
   self.obj319.graphObject_.pendingConnections.append((self.obj319.graphObject_.tag, self.obj324.graphObject_.tag, [52.0, 206.0, 147.5, 180.0, 205.5, 156.75], 2, True))
   self.obj319.out_connections_.append(self.obj325)
   self.obj325.in_connections_.append(self.obj319)
   self.obj319.graphObject_.pendingConnections.append((self.obj319.graphObject_.tag, self.obj325.graphObject_.tag, [52.0, 206.0, 152.5, 197.5, 215.0, 206.75], 2, True))
   self.obj324.out_connections_.append(self.obj292)
   self.obj292.in_connections_.append(self.obj324)
   self.obj324.graphObject_.pendingConnections.append((self.obj324.graphObject_.tag, self.obj292.graphObject_.tag, [284.0, 113.0, 263.5, 133.5, 205.5, 156.75], 2, True))
   self.obj325.out_connections_.append(self.obj294)
   self.obj294.in_connections_.append(self.obj325)
   self.obj325.graphObject_.pendingConnections.append((self.obj325.graphObject_.tag, self.obj294.graphObject_.tag, [302.0, 243.0, 277.5, 216.0, 215.0, 206.75], 2, True))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# code condition of rule\nnode = self.getMatched(graphID, self.LHS.nodeWithLabel(3))\nreturn not hasattr(node, "LinkRaw2AR")\n\n\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# code action of rule\nnode = self.getMatched ( graphID , self.LHS.nodeWithLabel(3) )\nnode.LinkRaw2AR = True\n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('GenAux1', 20)
   cobj0.Order=ATOM3Integer(9)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

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

   cobj0.LHS = ASG_pns2(self)
   cobj0.LHS.merge(ASG_omacs(self))

   self.obj110=CapableOf(self)
   self.obj110.preAction( cobj0.LHS.CREATE )
   self.obj110.isGraphObjectVisual = True

   if(hasattr(self.obj110, '_setHierarchicalLink')):
     self.obj110._setHierarchicalLink(False)

   self.obj110.GGLabel.setValue(4)
   self.obj110.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(124.5,62.0,self.obj110)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj110.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj110)
   self.obj110.postAction( cobj0.LHS.CREATE )

   self.obj111=Goal(self)
   self.obj111.preAction( cobj0.LHS.CREATE )
   self.obj111.isGraphObjectVisual = True

   if(hasattr(self.obj111, '_setHierarchicalLink')):
     self.obj111._setHierarchicalLink(False)

   # name
   self.obj111.name.setValue('')
   self.obj111.name.setNone()

   self.obj111.GGLabel.setValue(3)
   self.obj111.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(40.0,160.0,self.obj111)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj111.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj111)
   self.obj111.postAction( cobj0.LHS.CREATE )

   self.obj112=Agent(self)
   self.obj112.preAction( cobj0.LHS.CREATE )
   self.obj112.isGraphObjectVisual = True

   if(hasattr(self.obj112, '_setHierarchicalLink')):
     self.obj112._setHierarchicalLink(False)

   # price
   self.obj112.price.setValue(0)

   # name
   self.obj112.name.setValue('')
   self.obj112.name.setNone()

   self.obj112.GGLabel.setValue(1)
   self.obj112.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(0.0,-20.0,self.obj112)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj112.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj112)
   self.obj112.postAction( cobj0.LHS.CREATE )

   self.obj113=Role(self)
   self.obj113.preAction( cobj0.LHS.CREATE )
   self.obj113.isGraphObjectVisual = True

   if(hasattr(self.obj113, '_setHierarchicalLink')):
     self.obj113._setHierarchicalLink(False)

   # name
   self.obj113.name.setValue('')
   self.obj113.name.setNone()

   self.obj113.GGLabel.setValue(2)
   self.obj113.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(160.0,80.0,self.obj113)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj113.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj113)
   self.obj113.postAction( cobj0.LHS.CREATE )

   self.obj114=achieve(self)
   self.obj114.preAction( cobj0.LHS.CREATE )
   self.obj114.isGraphObjectVisual = True

   if(hasattr(self.obj114, '_setHierarchicalLink')):
     self.obj114._setHierarchicalLink(False)

   self.obj114.GGLabel.setValue(5)
   self.obj114.graphClass_= graph_achieve
   if self.genGraphics:
      new_obj = graph_achieve(131.0,152.0,self.obj114)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj114.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj114)
   self.obj114.postAction( cobj0.LHS.CREATE )

   self.obj110.out_connections_.append(self.obj113)
   self.obj113.in_connections_.append(self.obj110)
   self.obj110.graphObject_.pendingConnections.append((self.obj110.graphObject_.tag, self.obj113.graphObject_.tag, [190.0, 80.0, 158.0, 52.0, 191.0, 54.0, 124.5, 62.0], 4, True))
   self.obj112.out_connections_.append(self.obj110)
   self.obj110.in_connections_.append(self.obj112)
   self.obj112.graphObject_.pendingConnections.append((self.obj112.graphObject_.tag, self.obj110.graphObject_.tag, [32.0, 66.0, 91.0, 72.0, 57.0, 94.0, 124.5, 62.0], 4, True))
   self.obj113.out_connections_.append(self.obj114)
   self.obj114.in_connections_.append(self.obj113)
   self.obj113.graphObject_.pendingConnections.append((self.obj113.graphObject_.tag, self.obj114.graphObject_.tag, [192.0, 150.0, 170.0, 172.0, 131.0, 152.0], 2, True))
   self.obj114.out_connections_.append(self.obj111)
   self.obj111.in_connections_.append(self.obj114)
   self.obj114.graphObject_.pendingConnections.append((self.obj114.graphObject_.tag, self.obj111.graphObject_.tag, [72.0, 161.0, 92.0, 132.0, 131.0, 152.0], 2, True))

   cobj0.RHS = ASG_pns2(self)
   cobj0.RHS.merge(ASG_omacs(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj118=metarial(self)
   self.obj118.preAction( cobj0.RHS.CREATE )
   self.obj118.isGraphObjectVisual = True

   if(hasattr(self.obj118, '_setHierarchicalLink')):
     self.obj118._setHierarchicalLink(False)

   # Name
   self.obj118.Name.setValue('')
   self.obj118.Name.setNone()

   self.obj118.GGLabel.setValue(7)
   self.obj118.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(320.0,40.0,self.obj118)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj118.graphObject_ = new_obj
   self.obj1180= AttrCalc()
   self.obj1180.Copy=ATOM3Boolean()
   self.obj1180.Copy.setValue(('Copy from LHS', 0))
   self.obj1180.Copy.config = 0
   self.obj1180.Specify=ATOM3Constraint()
   self.obj1180.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# Template for typical GG specify code (specified field is a string)\n# See atom3\\Kernel\\ATOM3Types directory for info on specific types\n\n# return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).Name.getValue()\n\n# "self.LHS.nodeWithLabel(1)" gets the node with GG label 1 in the LHS of the GG\n# "self.getMatched(graphID, self.LHS.nodeWithLabel(1))" gets node in host graph\n# ".Name" will access that node\'s Name attribute, an ATOM3 string object\n# ".getValue()" will return the ATOM3 string as a regular Python string\n# Finally, a Python string is returned, and becomes the value of the specified\n# field\n\n# A more complicated template (specified field is an integer)\n\n# # Source loses one car\n# sourceNode = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\n# currentNumCars = sourceNode.num_vehicles.getValue()\n# # If source has an infinite supply (infinite_supply = ATOM3 boolean value)\n# if(source.infinite_supply.getValueBoolean()): \n#     return currentNumCars\n# return currentNumCars - 1\nagent = self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()\nrole = self.getMatched(graphID, self.LHS.nodeWithLabel(2)).name.getValue()\ngoal = self.getMatched(graphID, self.LHS.nodeWithLabel(3)).name.getValue()\n\nreturn agent +\' \'+ role +\' \'+ goal\n\n'))
   self.obj118.GGset2Any['Name']= self.obj1180

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj118)
   self.obj118.postAction( cobj0.RHS.CREATE )

   self.obj119=operatingUnit(self)
   self.obj119.preAction( cobj0.RHS.CREATE )
   self.obj119.isGraphObjectVisual = True

   if(hasattr(self.obj119, '_setHierarchicalLink')):
     self.obj119._setHierarchicalLink(False)

   self.obj119.GGLabel.setValue(8)
   self.obj119.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(320.0,140.0,self.obj119)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj119.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj119)
   self.obj119.postAction( cobj0.RHS.CREATE )

   self.obj120=fromMaterial(self)
   self.obj120.preAction( cobj0.RHS.CREATE )
   self.obj120.isGraphObjectVisual = True

   if(hasattr(self.obj120, '_setHierarchicalLink')):
     self.obj120._setHierarchicalLink(False)

   # rate
   self.obj120.rate.setValue(0.0)

   self.obj120.GGLabel.setValue(10)
   self.obj120.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(343.0,116.5,self.obj120)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj120.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj120)
   self.obj120.postAction( cobj0.RHS.CREATE )

   self.obj121=CapableOf(self)
   self.obj121.preAction( cobj0.RHS.CREATE )
   self.obj121.isGraphObjectVisual = True

   if(hasattr(self.obj121, '_setHierarchicalLink')):
     self.obj121._setHierarchicalLink(False)

   self.obj121.GGLabel.setValue(4)
   self.obj121.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(124.5,62.0,self.obj121)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj121.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj121)
   self.obj121.postAction( cobj0.RHS.CREATE )

   self.obj122=Goal(self)
   self.obj122.preAction( cobj0.RHS.CREATE )
   self.obj122.isGraphObjectVisual = True

   if(hasattr(self.obj122, '_setHierarchicalLink')):
     self.obj122._setHierarchicalLink(False)

   # name
   self.obj122.name.setValue('')
   self.obj122.name.setNone()

   self.obj122.GGLabel.setValue(3)
   self.obj122.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(40.0,160.0,self.obj122)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj122.graphObject_ = new_obj
   self.obj1220= AttrCalc()
   self.obj1220.Copy=ATOM3Boolean()
   self.obj1220.Copy.setValue(('Copy from LHS', 1))
   self.obj1220.Copy.config = 0
   self.obj1220.Specify=ATOM3Constraint()
   self.obj1220.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj122.GGset2Any['name']= self.obj1220

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj122)
   self.obj122.postAction( cobj0.RHS.CREATE )

   self.obj123=Agent(self)
   self.obj123.preAction( cobj0.RHS.CREATE )
   self.obj123.isGraphObjectVisual = True

   if(hasattr(self.obj123, '_setHierarchicalLink')):
     self.obj123._setHierarchicalLink(False)

   # price
   self.obj123.price.setValue(0)

   # name
   self.obj123.name.setValue('')
   self.obj123.name.setNone()

   self.obj123.GGLabel.setValue(1)
   self.obj123.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(0.0,-20.0,self.obj123)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj123.graphObject_ = new_obj
   self.obj1230= AttrCalc()
   self.obj1230.Copy=ATOM3Boolean()
   self.obj1230.Copy.setValue(('Copy from LHS', 1))
   self.obj1230.Copy.config = 0
   self.obj1230.Specify=ATOM3Constraint()
   self.obj1230.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj123.GGset2Any['price']= self.obj1230
   self.obj1231= AttrCalc()
   self.obj1231.Copy=ATOM3Boolean()
   self.obj1231.Copy.setValue(('Copy from LHS', 1))
   self.obj1231.Copy.config = 0
   self.obj1231.Specify=ATOM3Constraint()
   self.obj1231.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj123.GGset2Any['name']= self.obj1231

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj123)
   self.obj123.postAction( cobj0.RHS.CREATE )

   self.obj124=Role(self)
   self.obj124.preAction( cobj0.RHS.CREATE )
   self.obj124.isGraphObjectVisual = True

   if(hasattr(self.obj124, '_setHierarchicalLink')):
     self.obj124._setHierarchicalLink(False)

   # name
   self.obj124.name.setValue('')
   self.obj124.name.setNone()

   self.obj124.GGLabel.setValue(2)
   self.obj124.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(160.0,80.0,self.obj124)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj124.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj124)
   self.obj124.postAction( cobj0.RHS.CREATE )

   self.obj125=achieve(self)
   self.obj125.preAction( cobj0.RHS.CREATE )
   self.obj125.isGraphObjectVisual = True

   if(hasattr(self.obj125, '_setHierarchicalLink')):
     self.obj125._setHierarchicalLink(False)

   self.obj125.GGLabel.setValue(5)
   self.obj125.graphClass_= graph_achieve
   if self.genGraphics:
      new_obj = graph_achieve(131.0,152.0,self.obj125)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj125.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj125)
   self.obj125.postAction( cobj0.RHS.CREATE )

   self.obj126=GenericGraphEdge(self)
   self.obj126.preAction( cobj0.RHS.CREATE )
   self.obj126.isGraphObjectVisual = True

   if(hasattr(self.obj126, '_setHierarchicalLink')):
     self.obj126._setHierarchicalLink(False)

   self.obj126.GGLabel.setValue(9)
   self.obj126.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(258.75,50.75,self.obj126)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj126.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj126)
   self.obj126.postAction( cobj0.RHS.CREATE )

   self.obj118.out_connections_.append(self.obj120)
   self.obj120.in_connections_.append(self.obj118)
   self.obj118.graphObject_.pendingConnections.append((self.obj118.graphObject_.tag, self.obj120.graphObject_.tag, [344.0, 90.0, 343.0, 116.5], 0, True))
   self.obj120.out_connections_.append(self.obj119)
   self.obj119.in_connections_.append(self.obj120)
   self.obj120.graphObject_.pendingConnections.append((self.obj120.graphObject_.tag, self.obj119.graphObject_.tag, [342.0, 143.0, 343.0, 116.5], 0, True))
   self.obj121.out_connections_.append(self.obj124)
   self.obj124.in_connections_.append(self.obj121)
   self.obj121.graphObject_.pendingConnections.append((self.obj121.graphObject_.tag, self.obj124.graphObject_.tag, [191.0, 80.0, 124.5, 62.0], 2, 0))
   self.obj123.out_connections_.append(self.obj121)
   self.obj121.in_connections_.append(self.obj123)
   self.obj123.graphObject_.pendingConnections.append((self.obj123.graphObject_.tag, self.obj121.graphObject_.tag, [34.0, 66.0, 124.5, 62.0], 2, 0))
   self.obj124.out_connections_.append(self.obj125)
   self.obj125.in_connections_.append(self.obj124)
   self.obj124.graphObject_.pendingConnections.append((self.obj124.graphObject_.tag, self.obj125.graphObject_.tag, [193.0, 150.0, 131.0, 152.0], 2, 0))
   self.obj124.out_connections_.append(self.obj126)
   self.obj126.in_connections_.append(self.obj124)
   self.obj124.graphObject_.pendingConnections.append((self.obj124.graphObject_.tag, self.obj126.graphObject_.tag, [191.0, 80.0, 223.5, 59.5, 258.75, 50.75], 2, True))
   self.obj125.out_connections_.append(self.obj122)
   self.obj122.in_connections_.append(self.obj125)
   self.obj125.graphObject_.pendingConnections.append((self.obj125.graphObject_.tag, self.obj122.graphObject_.tag, [73.0, 161.0, 131.0, 152.0], 2, 0))
   self.obj126.out_connections_.append(self.obj118)
   self.obj118.in_connections_.append(self.obj126)
   self.obj126.graphObject_.pendingConnections.append((self.obj126.graphObject_.tag, self.obj118.graphObject_.tag, [332.0, 45.0, 294.0, 42.0, 258.75, 50.75], 2, True))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '		print \'======> GenAux1 Condition\'\n		a = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\n		aN = a.name.getValue()\n		#print a.name.getValue()+\' has att AUX : \'+str( hasattr(a, "AUX") )\n		r = self.getMatched(graphID, self.LHS.nodeWithLabel(2))\n		Rn = r.name.getValue()\n		g = self.getMatched(graphID, self.LHS.nodeWithLabel(3))\n		Gn = g.name.getValue()\n		# add list to the Agent Node\n		if not hasattr(a,\'markedNode\') : \n			a.markedNode = []\n			print \'add List to \'+aN\n		else : \n			print \'Check if \'+aN+\'Have \'\n			for ele in a.markedNode : \n				if ele == (Rn,Gn) : return False\n			return True\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n		print \'======> GenAux1 ACtion\'\n		a = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\n		aN = a.name.getValue()\n		#print a.name.getValue()+\' has att AUX : \'+str( hasattr(a, "AUX") )\n		r = self.getMatched(graphID, self.LHS.nodeWithLabel(2))\n		Rn = r.name.getValue()\n		g = self.getMatched(graphID, self.LHS.nodeWithLabel(3))\n		Gn = g.name.getValue()\n		# add ele list to the Agent Node\n		print \'Add Ele into list of \'+aN\n		a.markedNode.append( (Rn,Gn) )\n		print \'List of MarkedNode\'\n		for ele in a.markedNode : \n			print ele\n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('LinkAux1', 20)
   cobj0.Order=ATOM3Integer(10)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

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

   cobj0.LHS = ASG_pns2(self)
   cobj0.LHS.merge(ASG_omacs(self))
   cobj0.LHS.merge(ASG_GenericGraph(self))

   self.obj133=metarial(self)
   self.obj133.preAction( cobj0.LHS.CREATE )
   self.obj133.isGraphObjectVisual = True

   if(hasattr(self.obj133, '_setHierarchicalLink')):
     self.obj133._setHierarchicalLink(False)

   # Name
   self.obj133.Name.setValue('')
   self.obj133.Name.setNone()

   self.obj133.GGLabel.setValue(4)
   self.obj133.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(260.0,40.0,self.obj133)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj133.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj133)
   self.obj133.postAction( cobj0.LHS.CREATE )

   self.obj134=metarial(self)
   self.obj134.preAction( cobj0.LHS.CREATE )
   self.obj134.isGraphObjectVisual = True

   if(hasattr(self.obj134, '_setHierarchicalLink')):
     self.obj134._setHierarchicalLink(False)

   # Name
   self.obj134.Name.setValue('')
   self.obj134.Name.setNone()

   self.obj134.GGLabel.setValue(8)
   self.obj134.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(240.0,220.0,self.obj134)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj134.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj134)
   self.obj134.postAction( cobj0.LHS.CREATE )

   self.obj135=operatingUnit(self)
   self.obj135.preAction( cobj0.LHS.CREATE )
   self.obj135.isGraphObjectVisual = True

   if(hasattr(self.obj135, '_setHierarchicalLink')):
     self.obj135._setHierarchicalLink(False)

   self.obj135.GGLabel.setValue(5)
   self.obj135.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(260.0,120.0,self.obj135)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj135.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj135)
   self.obj135.postAction( cobj0.LHS.CREATE )

   self.obj136=fromMaterial(self)
   self.obj136.preAction( cobj0.LHS.CREATE )
   self.obj136.isGraphObjectVisual = True

   if(hasattr(self.obj136, '_setHierarchicalLink')):
     self.obj136._setHierarchicalLink(False)

   # rate
   self.obj136.rate.setValue(0.0)

   self.obj136.GGLabel.setValue(6)
   self.obj136.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(283.0,106.5,self.obj136)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj136.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj136)
   self.obj136.postAction( cobj0.LHS.CREATE )

   self.obj137=Goal(self)
   self.obj137.preAction( cobj0.LHS.CREATE )
   self.obj137.isGraphObjectVisual = True

   if(hasattr(self.obj137, '_setHierarchicalLink')):
     self.obj137._setHierarchicalLink(False)

   # name
   self.obj137.name.setValue('')
   self.obj137.name.setNone()

   self.obj137.GGLabel.setValue(2)
   self.obj137.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(80.0,200.0,self.obj137)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj137.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj137)
   self.obj137.postAction( cobj0.LHS.CREATE )

   self.obj138=Role(self)
   self.obj138.preAction( cobj0.LHS.CREATE )
   self.obj138.isGraphObjectVisual = True

   if(hasattr(self.obj138, '_setHierarchicalLink')):
     self.obj138._setHierarchicalLink(False)

   # name
   self.obj138.name.setValue('')
   self.obj138.name.setNone()

   self.obj138.GGLabel.setValue(1)
   self.obj138.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(80.0,40.0,self.obj138)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj138.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj138)
   self.obj138.postAction( cobj0.LHS.CREATE )

   self.obj139=achieve(self)
   self.obj139.preAction( cobj0.LHS.CREATE )
   self.obj139.isGraphObjectVisual = True

   if(hasattr(self.obj139, '_setHierarchicalLink')):
     self.obj139._setHierarchicalLink(False)

   self.obj139.GGLabel.setValue(3)
   self.obj139.graphClass_= graph_achieve
   if self.genGraphics:
      new_obj = graph_achieve(112.0,155.5,self.obj139)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj139.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj139)
   self.obj139.postAction( cobj0.LHS.CREATE )

   self.obj140=GenericGraphEdge(self)
   self.obj140.preAction( cobj0.LHS.CREATE )
   self.obj140.isGraphObjectVisual = True

   if(hasattr(self.obj140, '_setHierarchicalLink')):
     self.obj140._setHierarchicalLink(False)

   self.obj140.GGLabel.setValue(7)
   self.obj140.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(201.0,126.75,self.obj140)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj140.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj140)
   self.obj140.postAction( cobj0.LHS.CREATE )

   self.obj141=GenericGraphEdge(self)
   self.obj141.preAction( cobj0.LHS.CREATE )
   self.obj141.isGraphObjectVisual = True

   if(hasattr(self.obj141, '_setHierarchicalLink')):
     self.obj141._setHierarchicalLink(False)

   self.obj141.GGLabel.setValue(9)
   self.obj141.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(181.5,267.0,self.obj141)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj141.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj141)
   self.obj141.postAction( cobj0.LHS.CREATE )

   self.obj133.out_connections_.append(self.obj136)
   self.obj136.in_connections_.append(self.obj133)
   self.obj133.graphObject_.pendingConnections.append((self.obj133.graphObject_.tag, self.obj136.graphObject_.tag, [284.0, 90.0, 283.0, 106.5], 0, True))
   self.obj136.out_connections_.append(self.obj135)
   self.obj135.in_connections_.append(self.obj136)
   self.obj136.graphObject_.pendingConnections.append((self.obj136.graphObject_.tag, self.obj135.graphObject_.tag, [282.0, 123.0, 283.0, 106.5], 0, True))
   self.obj137.out_connections_.append(self.obj141)
   self.obj141.in_connections_.append(self.obj137)
   self.obj137.graphObject_.pendingConnections.append((self.obj137.graphObject_.tag, self.obj141.graphObject_.tag, [113.0, 270.0, 181.5, 267.0], 0, True))
   self.obj138.out_connections_.append(self.obj139)
   self.obj139.in_connections_.append(self.obj138)
   self.obj138.graphObject_.pendingConnections.append((self.obj138.graphObject_.tag, self.obj139.graphObject_.tag, [112.0, 110.0, 112.0, 155.5], 0, True))
   self.obj138.out_connections_.append(self.obj140)
   self.obj140.in_connections_.append(self.obj138)
   self.obj138.graphObject_.pendingConnections.append((self.obj138.graphObject_.tag, self.obj140.graphObject_.tag, [112.0, 110.0, 188.5, 154.5, 158.0, 152.0, 201.0, 126.75], 4, True))
   self.obj139.out_connections_.append(self.obj137)
   self.obj137.in_connections_.append(self.obj139)
   self.obj139.graphObject_.pendingConnections.append((self.obj139.graphObject_.tag, self.obj137.graphObject_.tag, [112.0, 201.0, 112.0, 155.5], 0, True))
   self.obj140.out_connections_.append(self.obj133)
   self.obj133.in_connections_.append(self.obj140)
   self.obj140.graphObject_.pendingConnections.append((self.obj140.graphObject_.tag, self.obj133.graphObject_.tag, [272.0, 45.0, 213.5, 99.0, 208.0, 41.0, 201.0, 126.75], 4, True))
   self.obj141.out_connections_.append(self.obj134)
   self.obj134.in_connections_.append(self.obj141)
   self.obj141.graphObject_.pendingConnections.append((self.obj141.graphObject_.tag, self.obj134.graphObject_.tag, [250.0, 264.0, 181.5, 267.0], 0, True))

   cobj0.RHS = ASG_pns2(self)
   cobj0.RHS.merge(ASG_omacs(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj145=metarial(self)
   self.obj145.preAction( cobj0.RHS.CREATE )
   self.obj145.isGraphObjectVisual = True

   if(hasattr(self.obj145, '_setHierarchicalLink')):
     self.obj145._setHierarchicalLink(False)

   # Name
   self.obj145.Name.setValue('')
   self.obj145.Name.setNone()

   self.obj145.GGLabel.setValue(4)
   self.obj145.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(280.0,40.0,self.obj145)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj145.graphObject_ = new_obj
   self.obj1450= AttrCalc()
   self.obj1450.Copy=ATOM3Boolean()
   self.obj1450.Copy.setValue(('Copy from LHS', 1))
   self.obj1450.Copy.config = 0
   self.obj1450.Specify=ATOM3Constraint()
   self.obj1450.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj145.GGset2Any['Name']= self.obj1450

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj145)
   self.obj145.postAction( cobj0.RHS.CREATE )

   self.obj146=metarial(self)
   self.obj146.preAction( cobj0.RHS.CREATE )
   self.obj146.isGraphObjectVisual = True

   if(hasattr(self.obj146, '_setHierarchicalLink')):
     self.obj146._setHierarchicalLink(False)

   # Name
   self.obj146.Name.setValue('')
   self.obj146.Name.setNone()

   self.obj146.GGLabel.setValue(8)
   self.obj146.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(260.0,240.0,self.obj146)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj146.graphObject_ = new_obj
   self.obj1460= AttrCalc()
   self.obj1460.Copy=ATOM3Boolean()
   self.obj1460.Copy.setValue(('Copy from LHS', 1))
   self.obj1460.Copy.config = 0
   self.obj1460.Specify=ATOM3Constraint()
   self.obj1460.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj146.GGset2Any['Name']= self.obj1460

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj146)
   self.obj146.postAction( cobj0.RHS.CREATE )

   self.obj147=operatingUnit(self)
   self.obj147.preAction( cobj0.RHS.CREATE )
   self.obj147.isGraphObjectVisual = True

   if(hasattr(self.obj147, '_setHierarchicalLink')):
     self.obj147._setHierarchicalLink(False)

   self.obj147.GGLabel.setValue(5)
   self.obj147.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(260.0,140.0,self.obj147)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj147.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj147)
   self.obj147.postAction( cobj0.RHS.CREATE )

   self.obj148=intoMaterial(self)
   self.obj148.preAction( cobj0.RHS.CREATE )
   self.obj148.isGraphObjectVisual = True

   if(hasattr(self.obj148, '_setHierarchicalLink')):
     self.obj148._setHierarchicalLink(False)

   # rate
   self.obj148.rate.setValue(0.0)

   self.obj148.GGLabel.setValue(10)
   self.obj148.graphClass_= graph_intoMaterial
   if self.genGraphics:
      new_obj = graph_intoMaterial(285.0,199.5,self.obj148)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj148.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj148)
   self.obj148.postAction( cobj0.RHS.CREATE )

   self.obj149=fromMaterial(self)
   self.obj149.preAction( cobj0.RHS.CREATE )
   self.obj149.isGraphObjectVisual = True

   if(hasattr(self.obj149, '_setHierarchicalLink')):
     self.obj149._setHierarchicalLink(False)

   # rate
   self.obj149.rate.setValue(0.0)

   self.obj149.GGLabel.setValue(6)
   self.obj149.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(315.5,115.5,self.obj149)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj149.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj149)
   self.obj149.postAction( cobj0.RHS.CREATE )

   self.obj150=Goal(self)
   self.obj150.preAction( cobj0.RHS.CREATE )
   self.obj150.isGraphObjectVisual = True

   if(hasattr(self.obj150, '_setHierarchicalLink')):
     self.obj150._setHierarchicalLink(False)

   # name
   self.obj150.name.setValue('')
   self.obj150.name.setNone()

   self.obj150.GGLabel.setValue(2)
   self.obj150.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(60.0,220.0,self.obj150)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj150.graphObject_ = new_obj
   self.obj1500= AttrCalc()
   self.obj1500.Copy=ATOM3Boolean()
   self.obj1500.Copy.setValue(('Copy from LHS', 1))
   self.obj1500.Copy.config = 0
   self.obj1500.Specify=ATOM3Constraint()
   self.obj1500.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj150.GGset2Any['name']= self.obj1500

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj150)
   self.obj150.postAction( cobj0.RHS.CREATE )

   self.obj151=Role(self)
   self.obj151.preAction( cobj0.RHS.CREATE )
   self.obj151.isGraphObjectVisual = True

   if(hasattr(self.obj151, '_setHierarchicalLink')):
     self.obj151._setHierarchicalLink(False)

   # name
   self.obj151.name.setValue('')
   self.obj151.name.setNone()

   self.obj151.GGLabel.setValue(1)
   self.obj151.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(60.0,40.0,self.obj151)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj151.graphObject_ = new_obj
   self.obj1510= AttrCalc()
   self.obj1510.Copy=ATOM3Boolean()
   self.obj1510.Copy.setValue(('Copy from LHS', 1))
   self.obj1510.Copy.config = 0
   self.obj1510.Specify=ATOM3Constraint()
   self.obj1510.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj151.GGset2Any['name']= self.obj1510

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj151)
   self.obj151.postAction( cobj0.RHS.CREATE )

   self.obj152=achieve(self)
   self.obj152.preAction( cobj0.RHS.CREATE )
   self.obj152.isGraphObjectVisual = True

   if(hasattr(self.obj152, '_setHierarchicalLink')):
     self.obj152._setHierarchicalLink(False)

   self.obj152.GGLabel.setValue(3)
   self.obj152.graphClass_= graph_achieve
   if self.genGraphics:
      new_obj = graph_achieve(92.0,165.5,self.obj152)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj152.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj152)
   self.obj152.postAction( cobj0.RHS.CREATE )

   self.obj153=GenericGraphEdge(self)
   self.obj153.preAction( cobj0.RHS.CREATE )
   self.obj153.isGraphObjectVisual = True

   if(hasattr(self.obj153, '_setHierarchicalLink')):
     self.obj153._setHierarchicalLink(False)

   self.obj153.GGLabel.setValue(7)
   self.obj153.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(179.5,82.0,self.obj153)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj153.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj153)
   self.obj153.postAction( cobj0.RHS.CREATE )

   self.obj154=GenericGraphEdge(self)
   self.obj154.preAction( cobj0.RHS.CREATE )
   self.obj154.isGraphObjectVisual = True

   if(hasattr(self.obj154, '_setHierarchicalLink')):
     self.obj154._setHierarchicalLink(False)

   self.obj154.GGLabel.setValue(9)
   self.obj154.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(181.5,287.0,self.obj154)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj154.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj154)
   self.obj154.postAction( cobj0.RHS.CREATE )

   self.obj145.out_connections_.append(self.obj149)
   self.obj149.in_connections_.append(self.obj145)
   self.obj145.graphObject_.pendingConnections.append((self.obj145.graphObject_.tag, self.obj149.graphObject_.tag, [304.0, 90.0, 315.5, 115.5], 0, True))
   self.obj147.out_connections_.append(self.obj148)
   self.obj148.in_connections_.append(self.obj147)
   self.obj147.graphObject_.pendingConnections.append((self.obj147.graphObject_.tag, self.obj148.graphObject_.tag, [283.0, 158.0, 285.0, 199.5], 0, True))
   self.obj148.out_connections_.append(self.obj146)
   self.obj146.in_connections_.append(self.obj148)
   self.obj148.graphObject_.pendingConnections.append((self.obj148.graphObject_.tag, self.obj146.graphObject_.tag, [287.0, 241.0, 285.0, 199.5], 0, True))
   self.obj149.out_connections_.append(self.obj147)
   self.obj147.in_connections_.append(self.obj149)
   self.obj149.graphObject_.pendingConnections.append((self.obj149.graphObject_.tag, self.obj147.graphObject_.tag, [327.0, 141.0, 315.5, 115.5], 0, True))
   self.obj150.out_connections_.append(self.obj154)
   self.obj154.in_connections_.append(self.obj150)
   self.obj150.graphObject_.pendingConnections.append((self.obj150.graphObject_.tag, self.obj154.graphObject_.tag, [93.0, 290.0, 181.5, 287.0], 0, True))
   self.obj151.out_connections_.append(self.obj152)
   self.obj152.in_connections_.append(self.obj151)
   self.obj151.graphObject_.pendingConnections.append((self.obj151.graphObject_.tag, self.obj152.graphObject_.tag, [92.0, 110.0, 92.0, 165.5], 0, True))
   self.obj151.out_connections_.append(self.obj153)
   self.obj153.in_connections_.append(self.obj151)
   self.obj151.graphObject_.pendingConnections.append((self.obj151.graphObject_.tag, self.obj153.graphObject_.tag, [92.0, 110.0, 137.0, 139.0, 179.5, 82.0], 2, True))
   self.obj152.out_connections_.append(self.obj150)
   self.obj150.in_connections_.append(self.obj152)
   self.obj152.graphObject_.pendingConnections.append((self.obj152.graphObject_.tag, self.obj150.graphObject_.tag, [92.0, 221.0, 92.0, 165.5], 0, True))
   self.obj153.out_connections_.append(self.obj145)
   self.obj145.in_connections_.append(self.obj153)
   self.obj153.graphObject_.pendingConnections.append((self.obj153.graphObject_.tag, self.obj145.graphObject_.tag, [292.0, 45.0, 222.0, 25.0, 179.5, 82.0], 2, True))
   self.obj154.out_connections_.append(self.obj146)
   self.obj146.in_connections_.append(self.obj154)
   self.obj154.graphObject_.pendingConnections.append((self.obj154.graphObject_.tag, self.obj146.graphObject_.tag, [270.0, 284.0, 181.5, 287.0], 0, True))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'print \'======> Link Aux Condition\'\naRg = self.getMatched ( graphID , self.LHS.nodeWithLabel(4) )\nnameARG = aRg.Name.getValue()\ng = self.getMatched ( graphID , self.LHS.nodeWithLabel(8) )\n# test if nameARG  end with name of Goal \nif nameARG.endswith( g.Name.getValue() ) and not hasattr(aRg,\'LinkAux\'): \n	return True\nelse : \n	return False\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'print \'======> Link Aux Action\'\naRg = self.getMatched ( graphID , self.LHS.nodeWithLabel(4) )\naRg.LinkAux = True \n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('GenOaf', 20)
   cobj0.Order=ATOM3Integer(50)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

   from rawMaterial import *
   from intoProduct import *
   from operatingUnit import *
   from metarial import *
   from product import *
   from fromMaterial import *
   from fromRaw import *
   from ASG_pns2 import *
   from intoMaterial import *

   cobj0.LHS = ASG_pns2(self)


   cobj0.RHS = ASG_pns2(self)

   self.obj160=product(self)
   self.obj160.preAction( cobj0.RHS.CREATE )
   self.obj160.isGraphObjectVisual = True

   if(hasattr(self.obj160, '_setHierarchicalLink')):
     self.obj160._setHierarchicalLink(False)

   # Name
   self.obj160.Name.setValue('')
   self.obj160.Name.setNone()

   self.obj160.GGLabel.setValue(1)
   self.obj160.graphClass_= graph_product
   if self.genGraphics:
      new_obj = graph_product(200.0,100.0,self.obj160)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj160.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj160)
   self.obj160.postAction( cobj0.RHS.CREATE )


   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# If you want to apply this rule at most once on asingle host graph node, \n# then uncomment the next two lines. Change the default GG label (1) if needed.\n\n# Make sure to enable the ACTION code as well\n# And to use the same label & unique name in the ACTION\n# WARNING: _uniqueName22 is not guaranteed to be unique (so change it, be safe!)\n\n#node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\n#return not hasattr(node, "_uniqueName22")\nreturn self.graphRewritingSystem.Start == 0\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# If you want to apply this rule at most once on asingle host graph node, \n# then uncomment the next two lines. Change the default GG label (1) if needed.\n\n# Make sure to enable the CONDITION code as well\n# And to use the same label & unique name in the ACTION\n# WARNING: _uniqueName22 is not guaranteed to be unique (so change it, be safe!)\n\n#node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\n#node._uniqueName22 = True\n self.graphRewritingSystem.Start = 1\n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('OpUnit4M_OAF', 20)
   cobj0.Order=ATOM3Integer(51)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

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

   cobj0.LHS = ASG_pns2(self)
   cobj0.LHS.merge(ASG_omacs(self))
   cobj0.LHS.merge(ASG_GenericGraph(self))

   self.obj167=product(self)
   self.obj167.preAction( cobj0.LHS.CREATE )
   self.obj167.isGraphObjectVisual = True

   if(hasattr(self.obj167, '_setHierarchicalLink')):
     self.obj167._setHierarchicalLink(False)

   # Name
   self.obj167.Name.setValue('')
   self.obj167.Name.setNone()

   self.obj167.GGLabel.setValue(4)
   self.obj167.graphClass_= graph_product
   if self.genGraphics:
      new_obj = graph_product(360.0,40.0,self.obj167)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj167.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj167)
   self.obj167.postAction( cobj0.LHS.CREATE )

   self.obj168=metarial(self)
   self.obj168.preAction( cobj0.LHS.CREATE )
   self.obj168.isGraphObjectVisual = True

   if(hasattr(self.obj168, '_setHierarchicalLink')):
     self.obj168._setHierarchicalLink(False)

   # Name
   self.obj168.Name.setValue('')
   self.obj168.Name.setNone()

   self.obj168.GGLabel.setValue(2)
   self.obj168.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(180.0,40.0,self.obj168)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj168.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj168)
   self.obj168.postAction( cobj0.LHS.CREATE )

   self.obj169=Goal(self)
   self.obj169.preAction( cobj0.LHS.CREATE )
   self.obj169.isGraphObjectVisual = True

   if(hasattr(self.obj169, '_setHierarchicalLink')):
     self.obj169._setHierarchicalLink(False)

   # name
   self.obj169.name.setValue('')
   self.obj169.name.setNone()

   self.obj169.GGLabel.setValue(1)
   self.obj169.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(20.0,20.0,self.obj169)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj169.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj169)
   self.obj169.postAction( cobj0.LHS.CREATE )

   self.obj170=GenericGraphEdge(self)
   self.obj170.preAction( cobj0.LHS.CREATE )
   self.obj170.isGraphObjectVisual = True

   if(hasattr(self.obj170, '_setHierarchicalLink')):
     self.obj170._setHierarchicalLink(False)

   self.obj170.GGLabel.setValue(3)
   self.obj170.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(136.0,126.5,self.obj170)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj170.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj170)
   self.obj170.postAction( cobj0.LHS.CREATE )

   self.obj169.out_connections_.append(self.obj170)
   self.obj170.in_connections_.append(self.obj169)
   self.obj169.graphObject_.pendingConnections.append((self.obj169.graphObject_.tag, self.obj170.graphObject_.tag, [53.0, 90.0, 59.0, 129.0, 136.0, 126.5], 2, True))
   self.obj170.out_connections_.append(self.obj168)
   self.obj168.in_connections_.append(self.obj170)
   self.obj170.graphObject_.pendingConnections.append((self.obj170.graphObject_.tag, self.obj168.graphObject_.tag, [204.0, 90.0, 213.0, 124.0, 136.0, 126.5], 2, True))

   cobj0.RHS = ASG_pns2(self)
   cobj0.RHS.merge(ASG_omacs(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj174=product(self)
   self.obj174.preAction( cobj0.RHS.CREATE )
   self.obj174.isGraphObjectVisual = True

   if(hasattr(self.obj174, '_setHierarchicalLink')):
     self.obj174._setHierarchicalLink(False)

   # Name
   self.obj174.Name.setValue('')
   self.obj174.Name.setNone()

   self.obj174.GGLabel.setValue(4)
   self.obj174.graphClass_= graph_product
   if self.genGraphics:
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

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj174)
   self.obj174.postAction( cobj0.RHS.CREATE )

   self.obj175=metarial(self)
   self.obj175.preAction( cobj0.RHS.CREATE )
   self.obj175.isGraphObjectVisual = True

   if(hasattr(self.obj175, '_setHierarchicalLink')):
     self.obj175._setHierarchicalLink(False)

   # Name
   self.obj175.Name.setValue('')
   self.obj175.Name.setNone()

   self.obj175.GGLabel.setValue(2)
   self.obj175.graphClass_= graph_metarial
   if self.genGraphics:
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

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj175)
   self.obj175.postAction( cobj0.RHS.CREATE )

   self.obj176=operatingUnit(self)
   self.obj176.preAction( cobj0.RHS.CREATE )
   self.obj176.isGraphObjectVisual = True

   if(hasattr(self.obj176, '_setHierarchicalLink')):
     self.obj176._setHierarchicalLink(False)

   self.obj176.GGLabel.setValue(5)
   self.obj176.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(300.0,120.0,self.obj176)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj176.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj176)
   self.obj176.postAction( cobj0.RHS.CREATE )

   self.obj177=intoProduct(self)
   self.obj177.preAction( cobj0.RHS.CREATE )
   self.obj177.isGraphObjectVisual = True

   if(hasattr(self.obj177, '_setHierarchicalLink')):
     self.obj177._setHierarchicalLink(False)

   # rate
   self.obj177.rate.setValue(0.0)

   self.obj177.GGLabel.setValue(7)
   self.obj177.graphClass_= graph_intoProduct
   if self.genGraphics:
      new_obj = graph_intoProduct(328.0,48.5,self.obj177)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj177.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj177)
   self.obj177.postAction( cobj0.RHS.CREATE )

   self.obj178=fromMaterial(self)
   self.obj178.preAction( cobj0.RHS.CREATE )
   self.obj178.isGraphObjectVisual = True

   if(hasattr(self.obj178, '_setHierarchicalLink')):
     self.obj178._setHierarchicalLink(False)

   # rate
   self.obj178.rate.setValue(0.0)

   self.obj178.GGLabel.setValue(6)
   self.obj178.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(306.0,171.0,self.obj178)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj178.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj178)
   self.obj178.postAction( cobj0.RHS.CREATE )

   self.obj179=Goal(self)
   self.obj179.preAction( cobj0.RHS.CREATE )
   self.obj179.isGraphObjectVisual = True

   if(hasattr(self.obj179, '_setHierarchicalLink')):
     self.obj179._setHierarchicalLink(False)

   # name
   self.obj179.name.setValue('')
   self.obj179.name.setNone()

   self.obj179.GGLabel.setValue(1)
   self.obj179.graphClass_= graph_Goal
   if self.genGraphics:
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

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj179)
   self.obj179.postAction( cobj0.RHS.CREATE )

   self.obj180=GenericGraphEdge(self)
   self.obj180.preAction( cobj0.RHS.CREATE )
   self.obj180.isGraphObjectVisual = True

   if(hasattr(self.obj180, '_setHierarchicalLink')):
     self.obj180._setHierarchicalLink(False)

   self.obj180.GGLabel.setValue(3)
   self.obj180.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(199.0,133.0,self.obj180)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj180.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj180)
   self.obj180.postAction( cobj0.RHS.CREATE )

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

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# If you want to apply this rule at most once on asingle host graph node, \n# then uncomment the next two lines. Change the default GG label (1) if needed.\n\n# Make sure to enable the ACTION code as well\n# And to use the same label & unique name in the ACTION\n# WARNING: _uniqueName23 is not guaranteed to be unique (so change it, be safe!)\n\n#node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\n#return not hasattr(node, "_uniqueName23")\nnode = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nreturn not hasattr(node, "OpUnitM_OAF")\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# If you want to apply this rule at most once on asingle host graph node, \n# then uncomment the next two lines. Change the default GG label (1) if needed.\n\n# Make sure to enable the CONDITION code as well\n# And to use the same label & unique name in the ACTION\n# WARNING: _uniqueName23 is not guaranteed to be unique (so change it, be safe!)\n\n#node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\n#node._uniqueName23 = True\n\nnode = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) )\nnode.OpUnitM_OAF  = True  \n'))
   lcobj0.append(cobj0)
   self.EditingGraphGrammar.Rules.setValue(lcobj0)
   self.EditingGraphGrammar.InitialAction=ATOM3Constraint()
   self.EditingGraphGrammar.InitialAction.setValue(('constraint', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# Template code for an initial action (a full host graph traversal)\n\n#idInt = 0\n#for nodeType in graph.listNodes.keys():\n#    for node in graph.listNodes[nodeType]:\n#      # Prints the class name of all nodes in graph\n#      print node.__class__.__name__ \n#\n#      # This part assumes that *ALL* nodes in graph have ATOM3 Integer \n#      # attribute called "id" and that this attribute is in the visual icon\n#      # NOTE: setGenValue() sets the semantic value, updates visually, and\n#      # catches attribute name errors and displays correct alternatives\n#      node.setGenValue(\'id\', idInt)\n#      idInt += 1\nself.rewritingSystem.Start = 0 \n\n'))
   self.EditingGraphGrammar.FinalAction=ATOM3Constraint()
   self.EditingGraphGrammar.FinalAction.setValue(('const', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))


