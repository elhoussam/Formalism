# _ GenAux1_GG_rule.py ____________________________________________________________________________
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
class GenAux1_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 9)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_pns2(parent)
      self.LHS.merge(ASG_omacs(parent))

      self.obj110=CapableOf(parent)
      self.obj110.preAction( self.LHS.CREATE )
      self.obj110.isGraphObjectVisual = True

      if(hasattr(self.obj110, '_setHierarchicalLink')):
        self.obj110._setHierarchicalLink(False)

      self.obj110.GGLabel.setValue(4)
      self.obj110.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(124.5,62.0,self.obj110)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj110.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj110)
      self.obj110.postAction( self.LHS.CREATE )

      self.obj111=Goal(parent)
      self.obj111.preAction( self.LHS.CREATE )
      self.obj111.isGraphObjectVisual = True

      if(hasattr(self.obj111, '_setHierarchicalLink')):
        self.obj111._setHierarchicalLink(False)

      # name
      self.obj111.name.setValue('')
      self.obj111.name.setNone()

      self.obj111.GGLabel.setValue(3)
      self.obj111.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(40.0,160.0,self.obj111)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj111.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj111)
      self.obj111.postAction( self.LHS.CREATE )

      self.obj112=Agent(parent)
      self.obj112.preAction( self.LHS.CREATE )
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
      if parent.genGraphics:
         new_obj = graph_Agent(0.0,-20.0,self.obj112)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj112.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj112)
      self.obj112.postAction( self.LHS.CREATE )

      self.obj113=Role(parent)
      self.obj113.preAction( self.LHS.CREATE )
      self.obj113.isGraphObjectVisual = True

      if(hasattr(self.obj113, '_setHierarchicalLink')):
        self.obj113._setHierarchicalLink(False)

      # name
      self.obj113.name.setValue('')
      self.obj113.name.setNone()

      self.obj113.GGLabel.setValue(2)
      self.obj113.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(160.0,80.0,self.obj113)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj113.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj113)
      self.obj113.postAction( self.LHS.CREATE )

      self.obj114=achieve(parent)
      self.obj114.preAction( self.LHS.CREATE )
      self.obj114.isGraphObjectVisual = True

      if(hasattr(self.obj114, '_setHierarchicalLink')):
        self.obj114._setHierarchicalLink(False)

      self.obj114.GGLabel.setValue(5)
      self.obj114.graphClass_= graph_achieve
      if parent.genGraphics:
         new_obj = graph_achieve(131.0,152.0,self.obj114)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj114.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj114)
      self.obj114.postAction( self.LHS.CREATE )

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

      self.RHS = ASG_pns2(parent)
      self.RHS.merge(ASG_omacs(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj118=metarial(parent)
      self.obj118.preAction( self.RHS.CREATE )
      self.obj118.isGraphObjectVisual = True

      if(hasattr(self.obj118, '_setHierarchicalLink')):
        self.obj118._setHierarchicalLink(False)

      # Name
      self.obj118.Name.setValue('')
      self.obj118.Name.setNone()

      self.obj118.GGLabel.setValue(7)
      self.obj118.graphClass_= graph_metarial
      if parent.genGraphics:
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

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj118)
      self.obj118.postAction( self.RHS.CREATE )

      self.obj119=operatingUnit(parent)
      self.obj119.preAction( self.RHS.CREATE )
      self.obj119.isGraphObjectVisual = True

      if(hasattr(self.obj119, '_setHierarchicalLink')):
        self.obj119._setHierarchicalLink(False)

      self.obj119.GGLabel.setValue(8)
      self.obj119.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(320.0,140.0,self.obj119)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj119.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj119)
      self.obj119.postAction( self.RHS.CREATE )

      self.obj120=fromMaterial(parent)
      self.obj120.preAction( self.RHS.CREATE )
      self.obj120.isGraphObjectVisual = True

      if(hasattr(self.obj120, '_setHierarchicalLink')):
        self.obj120._setHierarchicalLink(False)

      # rate
      self.obj120.rate.setValue(0.0)

      self.obj120.GGLabel.setValue(10)
      self.obj120.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(343.0,116.5,self.obj120)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj120.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj120)
      self.obj120.postAction( self.RHS.CREATE )

      self.obj121=CapableOf(parent)
      self.obj121.preAction( self.RHS.CREATE )
      self.obj121.isGraphObjectVisual = True

      if(hasattr(self.obj121, '_setHierarchicalLink')):
        self.obj121._setHierarchicalLink(False)

      self.obj121.GGLabel.setValue(4)
      self.obj121.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(124.5,62.0,self.obj121)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj121.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj121)
      self.obj121.postAction( self.RHS.CREATE )

      self.obj122=Goal(parent)
      self.obj122.preAction( self.RHS.CREATE )
      self.obj122.isGraphObjectVisual = True

      if(hasattr(self.obj122, '_setHierarchicalLink')):
        self.obj122._setHierarchicalLink(False)

      # name
      self.obj122.name.setValue('')
      self.obj122.name.setNone()

      self.obj122.GGLabel.setValue(3)
      self.obj122.graphClass_= graph_Goal
      if parent.genGraphics:
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

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj122)
      self.obj122.postAction( self.RHS.CREATE )

      self.obj123=Agent(parent)
      self.obj123.preAction( self.RHS.CREATE )
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
      if parent.genGraphics:
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

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj123)
      self.obj123.postAction( self.RHS.CREATE )

      self.obj124=Role(parent)
      self.obj124.preAction( self.RHS.CREATE )
      self.obj124.isGraphObjectVisual = True

      if(hasattr(self.obj124, '_setHierarchicalLink')):
        self.obj124._setHierarchicalLink(False)

      # name
      self.obj124.name.setValue('')
      self.obj124.name.setNone()

      self.obj124.GGLabel.setValue(2)
      self.obj124.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(160.0,80.0,self.obj124)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj124.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj124)
      self.obj124.postAction( self.RHS.CREATE )

      self.obj125=achieve(parent)
      self.obj125.preAction( self.RHS.CREATE )
      self.obj125.isGraphObjectVisual = True

      if(hasattr(self.obj125, '_setHierarchicalLink')):
        self.obj125._setHierarchicalLink(False)

      self.obj125.GGLabel.setValue(5)
      self.obj125.graphClass_= graph_achieve
      if parent.genGraphics:
         new_obj = graph_achieve(131.0,152.0,self.obj125)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj125.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj125)
      self.obj125.postAction( self.RHS.CREATE )

      self.obj126=GenericGraphEdge(parent)
      self.obj126.preAction( self.RHS.CREATE )
      self.obj126.isGraphObjectVisual = True

      if(hasattr(self.obj126, '_setHierarchicalLink')):
        self.obj126._setHierarchicalLink(False)

      self.obj126.GGLabel.setValue(9)
      self.obj126.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(258.75,50.75,self.obj126)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj126.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj126)
      self.obj126.postAction( self.RHS.CREATE )

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

   def condition(self, graphID, isograph, atom3i):
      		print '======> GenAux1 Condition'
      		a = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      		aN = a.name.getValue()
      		#print a.name.getValue()+' has att AUX : '+str( hasattr(a, "AUX") )
      		r = self.getMatched(graphID, self.LHS.nodeWithLabel(2))
      		Rn = r.name.getValue()
      		g = self.getMatched(graphID, self.LHS.nodeWithLabel(3))
      		Gn = g.name.getValue()
      		# add list to the Agent Node
      		if not hasattr(a,'markedNode') : 
      			a.markedNode = []
      			print 'add List to '+aN
      		else : 
      			print 'Check if '+aN+'Have '
      			for ele in a.markedNode : 
      				if ele == (Rn,Gn) : return False
      			return True
      
      

   def action(self, graphID, isograph, atom3i):
      
      		print '======> GenAux1 ACtion'
      		a = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      		aN = a.name.getValue()
      		#print a.name.getValue()+' has att AUX : '+str( hasattr(a, "AUX") )
      		r = self.getMatched(graphID, self.LHS.nodeWithLabel(2))
      		Rn = r.name.getValue()
      		g = self.getMatched(graphID, self.LHS.nodeWithLabel(3))
      		Gn = g.name.getValue()
      		# add ele list to the Agent Node
      		print 'Add Ele into list of '+aN
      		a.markedNode.append( (Rn,Gn) )
      		print 'List of MarkedNode'
      		for ele in a.markedNode : 
      			print ele
      
      

