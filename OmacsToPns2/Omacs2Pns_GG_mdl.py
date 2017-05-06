from GraphGrammarEdit import *
from GGruleEdit import *

def savedTrans(self):
   self.EditingGraphGrammar= GraphGrammarEdit(None, self)
   self.EditingGraphGrammar.Name=ATOM3String('Omacs2Pns', 20)
   self.EditingGraphGrammar.Rules=ATOM3List([ 1, 1, 1, 0],GGruleEdit,None, self)
   lcobj0=[]
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('Agent2RoleLink1', 20)
   cobj0.Order=ATOM3Integer(1)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

   from CapableOf import *
   from Goal import *
   from require import *
   from Agent import *
   from Capabilitie import *
   from Role import *
   from ASG_omacs import *
   from achieve import *
   from posses import *

   cobj0.LHS = ASG_omacs(self)

   self.obj508=Agent(self)
   self.obj508.preAction( cobj0.LHS.CREATE )
   self.obj508.isGraphObjectVisual = True

   if(hasattr(self.obj508, '_setHierarchicalLink')):
     self.obj508._setHierarchicalLink(False)

   # price
   self.obj508.price.setNone()

   # name
   self.obj508.name.setValue('')
   self.obj508.name.setNone()

   self.obj508.GGLabel.setValue(1)
   self.obj508.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(80.0,20.0,self.obj508)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj508.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj508)
   self.obj508.postAction( cobj0.LHS.CREATE )

   self.obj509=Capabilitie(self)
   self.obj509.preAction( cobj0.LHS.CREATE )
   self.obj509.isGraphObjectVisual = True

   if(hasattr(self.obj509, '_setHierarchicalLink')):
     self.obj509._setHierarchicalLink(False)

   # name
   self.obj509.name.setValue('')
   self.obj509.name.setNone()

   self.obj509.GGLabel.setValue(2)
   self.obj509.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(160.0,180.0,self.obj509)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj509.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj509)
   self.obj509.postAction( cobj0.LHS.CREATE )

   self.obj510=Role(self)
   self.obj510.preAction( cobj0.LHS.CREATE )
   self.obj510.isGraphObjectVisual = True

   if(hasattr(self.obj510, '_setHierarchicalLink')):
     self.obj510._setHierarchicalLink(False)

   # name
   self.obj510.name.setValue('')
   self.obj510.name.setNone()

   self.obj510.GGLabel.setValue(3)
   self.obj510.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(280.0,40.0,self.obj510)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj510.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj510)
   self.obj510.postAction( cobj0.LHS.CREATE )

   self.obj511=posses(self)
   self.obj511.preAction( cobj0.LHS.CREATE )
   self.obj511.isGraphObjectVisual = True

   if(hasattr(self.obj511, '_setHierarchicalLink')):
     self.obj511._setHierarchicalLink(False)

   # rate
   self.obj511.rate.setNone()

   self.obj511.GGLabel.setValue(4)
   self.obj511.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(143.0,130.5,self.obj511)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj511.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj511)
   self.obj511.postAction( cobj0.LHS.CREATE )

   self.obj512=require(self)
   self.obj512.preAction( cobj0.LHS.CREATE )
   self.obj512.isGraphObjectVisual = True

   if(hasattr(self.obj512, '_setHierarchicalLink')):
     self.obj512._setHierarchicalLink(False)

   self.obj512.GGLabel.setValue(5)
   self.obj512.graphClass_= graph_require
   if self.genGraphics:
      new_obj = graph_require(242.5,132.5,self.obj512)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj512.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj512)
   self.obj512.postAction( cobj0.LHS.CREATE )

   self.obj508.out_connections_.append(self.obj511)
   self.obj511.in_connections_.append(self.obj508)
   self.obj508.graphObject_.pendingConnections.append((self.obj508.graphObject_.tag, self.obj511.graphObject_.tag, [105.0, 82.0, 143.0, 130.5], 0, True))
   self.obj510.out_connections_.append(self.obj512)
   self.obj512.in_connections_.append(self.obj510)
   self.obj510.graphObject_.pendingConnections.append((self.obj510.graphObject_.tag, self.obj512.graphObject_.tag, [304.0, 86.0, 242.5, 132.5], 0, True))
   self.obj511.out_connections_.append(self.obj509)
   self.obj509.in_connections_.append(self.obj511)
   self.obj511.graphObject_.pendingConnections.append((self.obj511.graphObject_.tag, self.obj509.graphObject_.tag, [181.0, 179.0, 143.0, 130.5], 0, True))
   self.obj512.out_connections_.append(self.obj509)
   self.obj509.in_connections_.append(self.obj512)
   self.obj512.graphObject_.pendingConnections.append((self.obj512.graphObject_.tag, self.obj509.graphObject_.tag, [181.0, 179.0, 242.5, 132.5], 0, True))

   cobj0.RHS = ASG_omacs(self)

   self.obj514=Agent(self)
   self.obj514.preAction( cobj0.RHS.CREATE )
   self.obj514.isGraphObjectVisual = True

   if(hasattr(self.obj514, '_setHierarchicalLink')):
     self.obj514._setHierarchicalLink(False)

   # price
   self.obj514.price.setNone()

   # name
   self.obj514.name.setValue('')
   self.obj514.name.setNone()

   self.obj514.GGLabel.setValue(1)
   self.obj514.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(80.0,20.0,self.obj514)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj514.graphObject_ = new_obj
   self.obj5140= AttrCalc()
   self.obj5140.Copy=ATOM3Boolean()
   self.obj5140.Copy.setValue(('Copy from LHS', 1))
   self.obj5140.Copy.config = 0
   self.obj5140.Specify=ATOM3Constraint()
   self.obj5140.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj514.GGset2Any['price']= self.obj5140
   self.obj5141= AttrCalc()
   self.obj5141.Copy=ATOM3Boolean()
   self.obj5141.Copy.setValue(('Copy from LHS', 1))
   self.obj5141.Copy.config = 0
   self.obj5141.Specify=ATOM3Constraint()
   self.obj5141.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj514.GGset2Any['name']= self.obj5141

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj514)
   self.obj514.postAction( cobj0.RHS.CREATE )

   self.obj515=Capabilitie(self)
   self.obj515.preAction( cobj0.RHS.CREATE )
   self.obj515.isGraphObjectVisual = True

   if(hasattr(self.obj515, '_setHierarchicalLink')):
     self.obj515._setHierarchicalLink(False)

   # name
   self.obj515.name.setValue('')
   self.obj515.name.setNone()

   self.obj515.GGLabel.setValue(2)
   self.obj515.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(160.0,180.0,self.obj515)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj515.graphObject_ = new_obj
   self.obj5150= AttrCalc()
   self.obj5150.Copy=ATOM3Boolean()
   self.obj5150.Copy.setValue(('Copy from LHS', 1))
   self.obj5150.Copy.config = 0
   self.obj5150.Specify=ATOM3Constraint()
   self.obj5150.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj515.GGset2Any['name']= self.obj5150

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj515)
   self.obj515.postAction( cobj0.RHS.CREATE )

   self.obj516=Role(self)
   self.obj516.preAction( cobj0.RHS.CREATE )
   self.obj516.isGraphObjectVisual = True

   if(hasattr(self.obj516, '_setHierarchicalLink')):
     self.obj516._setHierarchicalLink(False)

   # name
   self.obj516.name.setValue('')
   self.obj516.name.setNone()

   self.obj516.GGLabel.setValue(3)
   self.obj516.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(280.0,40.0,self.obj516)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj516.graphObject_ = new_obj
   self.obj5160= AttrCalc()
   self.obj5160.Copy=ATOM3Boolean()
   self.obj5160.Copy.setValue(('Copy from LHS', 1))
   self.obj5160.Copy.config = 0
   self.obj5160.Specify=ATOM3Constraint()
   self.obj5160.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj516.GGset2Any['name']= self.obj5160

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj516)
   self.obj516.postAction( cobj0.RHS.CREATE )

   self.obj517=posses(self)
   self.obj517.preAction( cobj0.RHS.CREATE )
   self.obj517.isGraphObjectVisual = True

   if(hasattr(self.obj517, '_setHierarchicalLink')):
     self.obj517._setHierarchicalLink(False)

   # rate
   self.obj517.rate.setNone()

   self.obj517.GGLabel.setValue(4)
   self.obj517.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(143.0,130.5,self.obj517)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj517.graphObject_ = new_obj
   self.obj5170= AttrCalc()
   self.obj5170.Copy=ATOM3Boolean()
   self.obj5170.Copy.setValue(('Copy from LHS', 1))
   self.obj5170.Copy.config = 0
   self.obj5170.Specify=ATOM3Constraint()
   self.obj5170.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj517.GGset2Any['rate']= self.obj5170

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj517)
   self.obj517.postAction( cobj0.RHS.CREATE )

   self.obj518=CapableOf(self)
   self.obj518.preAction( cobj0.RHS.CREATE )
   self.obj518.isGraphObjectVisual = True

   if(hasattr(self.obj518, '_setHierarchicalLink')):
     self.obj518._setHierarchicalLink(False)

   # rate
   self.obj518.rate.setValue(0.0)

   self.obj518.GGLabel.setValue(7)
   self.obj518.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(214.0,83.5,self.obj518)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj518.graphObject_ = new_obj
   self.obj5180= AttrCalc()
   self.obj5180.Copy=ATOM3Boolean()
   self.obj5180.Copy.setValue(('Copy from LHS', 1))
   self.obj5180.Copy.config = 0
   self.obj5180.Specify=ATOM3Constraint()
   self.obj5180.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj518.GGset2Any['rate']= self.obj5180

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj518)
   self.obj518.postAction( cobj0.RHS.CREATE )

   self.obj519=require(self)
   self.obj519.preAction( cobj0.RHS.CREATE )
   self.obj519.isGraphObjectVisual = True

   if(hasattr(self.obj519, '_setHierarchicalLink')):
     self.obj519._setHierarchicalLink(False)

   self.obj519.GGLabel.setValue(5)
   self.obj519.graphClass_= graph_require
   if self.genGraphics:
      new_obj = graph_require(242.5,132.5,self.obj519)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj519.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj519)
   self.obj519.postAction( cobj0.RHS.CREATE )

   self.obj514.out_connections_.append(self.obj517)
   self.obj517.in_connections_.append(self.obj514)
   self.obj514.graphObject_.pendingConnections.append((self.obj514.graphObject_.tag, self.obj517.graphObject_.tag, [117.0, 82.0, 143.0, 130.5], 2, 0))
   self.obj514.out_connections_.append(self.obj518)
   self.obj518.in_connections_.append(self.obj514)
   self.obj514.graphObject_.pendingConnections.append((self.obj514.graphObject_.tag, self.obj518.graphObject_.tag, [117.0, 82.0, 214.0, 83.5], 0, True))
   self.obj516.out_connections_.append(self.obj519)
   self.obj519.in_connections_.append(self.obj516)
   self.obj516.graphObject_.pendingConnections.append((self.obj516.graphObject_.tag, self.obj519.graphObject_.tag, [311.0, 85.0, 242.5, 132.5], 2, 0))
   self.obj517.out_connections_.append(self.obj515)
   self.obj515.in_connections_.append(self.obj517)
   self.obj517.graphObject_.pendingConnections.append((self.obj517.graphObject_.tag, self.obj515.graphObject_.tag, [191.0, 183.0, 143.0, 130.5], 2, 0))
   self.obj518.out_connections_.append(self.obj516)
   self.obj516.in_connections_.append(self.obj518)
   self.obj518.graphObject_.pendingConnections.append((self.obj518.graphObject_.tag, self.obj516.graphObject_.tag, [311.0, 85.0, 214.0, 83.5], 0, True))
   self.obj519.out_connections_.append(self.obj515)
   self.obj515.in_connections_.append(self.obj519)
   self.obj519.graphObject_.pendingConnections.append((self.obj519.graphObject_.tag, self.obj515.graphObject_.tag, [191.0, 183.0, 242.5, 132.5], 2, 0))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'agent = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\n\nrole = self.getMatched(graphID, self.LHS.nodeWithLabel(3))\nreturn not ( hasattr(agent, role.name.getValue()) and hasattr(role, agent.name.getValue() ) )\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'ag = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) )\nc1 = self.getMatched ( graphID , self.LHS.nodeWithLabel(2) )\nrole = self.getMatched ( graphID , self.LHS.nodeWithLabel(3) )\nsetattr(ag ,role.name.getValue(),True )\nsetattr(role ,ag.name.getValue(),True )\n\nsetattr( c1 ,  ag.name.getValue() , True )\nsetattr( c1 ,  role.name.getValue() , True )\n\nprint \'connCt (\'+ag.name.getValue()+\',\'+role.name.getValue()+\')\'\nif not (ag.name.getValue() in self.graphRewritingSystem.Dictag.keys() ) :\n self.graphRewritingSystem.Dictag[ag.name.getValue()] = {}\nif not (c1.name.getValue() in self.graphRewritingSystem.Dictag[ag.name.getValue()].keys() ) :\n self.graphRewritingSystem.Dictag[ag.name.getValue()][c1.name.getValue()]=0\nif not (role.name.getValue() in self.graphRewritingSystem.Dictag[ag.name.getValue()].keys() ) :\n self.graphRewritingSystem.Dictag[ag.name.getValue()][role.name.getValue()]=0   \n\nself.graphRewritingSystem.Dictag[ag.name.getValue()][\'nb\']=0\n\nprint str( self.graphRewritingSystem.Dictag )\n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('Agent2RoleLink2', 20)
   cobj0.Order=ATOM3Integer(2)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

   from CapableOf import *
   from Goal import *
   from require import *
   from Agent import *
   from Capabilitie import *
   from Role import *
   from ASG_omacs import *
   from achieve import *
   from posses import *

   cobj0.LHS = ASG_omacs(self)

   self.obj524=Agent(self)
   self.obj524.preAction( cobj0.LHS.CREATE )
   self.obj524.isGraphObjectVisual = True

   if(hasattr(self.obj524, '_setHierarchicalLink')):
     self.obj524._setHierarchicalLink(False)

   # price
   self.obj524.price.setNone()

   # name
   self.obj524.name.setValue('')
   self.obj524.name.setNone()

   self.obj524.GGLabel.setValue(1)
   self.obj524.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(60.0,20.0,self.obj524)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj524.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj524)
   self.obj524.postAction( cobj0.LHS.CREATE )

   self.obj525=Capabilitie(self)
   self.obj525.preAction( cobj0.LHS.CREATE )
   self.obj525.isGraphObjectVisual = True

   if(hasattr(self.obj525, '_setHierarchicalLink')):
     self.obj525._setHierarchicalLink(False)

   # name
   self.obj525.name.setValue('')
   self.obj525.name.setNone()

   self.obj525.GGLabel.setValue(2)
   self.obj525.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(80.0,180.0,self.obj525)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj525.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj525)
   self.obj525.postAction( cobj0.LHS.CREATE )

   self.obj526=Capabilitie(self)
   self.obj526.preAction( cobj0.LHS.CREATE )
   self.obj526.isGraphObjectVisual = True

   if(hasattr(self.obj526, '_setHierarchicalLink')):
     self.obj526._setHierarchicalLink(False)

   # name
   self.obj526.name.setValue('')
   self.obj526.name.setNone()

   self.obj526.GGLabel.setValue(3)
   self.obj526.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(300.0,20.0,self.obj526)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj526.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj526)
   self.obj526.postAction( cobj0.LHS.CREATE )

   self.obj527=Role(self)
   self.obj527.preAction( cobj0.LHS.CREATE )
   self.obj527.isGraphObjectVisual = True

   if(hasattr(self.obj527, '_setHierarchicalLink')):
     self.obj527._setHierarchicalLink(False)

   # name
   self.obj527.name.setValue('')
   self.obj527.name.setNone()

   self.obj527.GGLabel.setValue(4)
   self.obj527.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(320.0,180.0,self.obj527)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj527.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj527)
   self.obj527.postAction( cobj0.LHS.CREATE )

   self.obj528=posses(self)
   self.obj528.preAction( cobj0.LHS.CREATE )
   self.obj528.isGraphObjectVisual = True

   if(hasattr(self.obj528, '_setHierarchicalLink')):
     self.obj528._setHierarchicalLink(False)

   # rate
   self.obj528.rate.setNone()

   self.obj528.GGLabel.setValue(5)
   self.obj528.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(203.0,70.5,self.obj528)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj528.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj528)
   self.obj528.postAction( cobj0.LHS.CREATE )

   self.obj529=posses(self)
   self.obj529.preAction( cobj0.LHS.CREATE )
   self.obj529.isGraphObjectVisual = True

   if(hasattr(self.obj529, '_setHierarchicalLink')):
     self.obj529._setHierarchicalLink(False)

   # rate
   self.obj529.rate.setNone()

   self.obj529.GGLabel.setValue(6)
   self.obj529.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(93.0,130.5,self.obj529)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj529.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj529)
   self.obj529.postAction( cobj0.LHS.CREATE )

   self.obj530=CapableOf(self)
   self.obj530.preAction( cobj0.LHS.CREATE )
   self.obj530.isGraphObjectVisual = True

   if(hasattr(self.obj530, '_setHierarchicalLink')):
     self.obj530._setHierarchicalLink(False)

   # rate
   self.obj530.rate.setNone()

   self.obj530.GGLabel.setValue(9)
   self.obj530.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(209.5,129.5,self.obj530)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj530.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj530)
   self.obj530.postAction( cobj0.LHS.CREATE )

   self.obj531=require(self)
   self.obj531.preAction( cobj0.LHS.CREATE )
   self.obj531.isGraphObjectVisual = True

   if(hasattr(self.obj531, '_setHierarchicalLink')):
     self.obj531._setHierarchicalLink(False)

   self.obj531.GGLabel.setValue(7)
   self.obj531.graphClass_= graph_require
   if self.genGraphics:
      new_obj = graph_require(222.5,180.0,self.obj531)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj531.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj531)
   self.obj531.postAction( cobj0.LHS.CREATE )

   self.obj532=require(self)
   self.obj532.preAction( cobj0.LHS.CREATE )
   self.obj532.isGraphObjectVisual = True

   if(hasattr(self.obj532, '_setHierarchicalLink')):
     self.obj532._setHierarchicalLink(False)

   self.obj532.GGLabel.setValue(8)
   self.obj532.graphClass_= graph_require
   if self.genGraphics:
      new_obj = graph_require(332.5,120.0,self.obj532)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj532.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj532)
   self.obj532.postAction( cobj0.LHS.CREATE )

   self.obj524.out_connections_.append(self.obj528)
   self.obj528.in_connections_.append(self.obj524)
   self.obj524.out_connections_.append(self.obj529)
   self.obj529.in_connections_.append(self.obj524)
   self.obj524.graphObject_.pendingConnections.append((self.obj524.graphObject_.tag, self.obj529.graphObject_.tag, [85.0, 82.0, 93.0, 130.5], 0, True))
   self.obj524.out_connections_.append(self.obj530)
   self.obj530.in_connections_.append(self.obj524)
   self.obj524.graphObject_.pendingConnections.append((self.obj524.graphObject_.tag, self.obj530.graphObject_.tag, [85.0, 82.0, 163.0, 138.0, 209.5, 129.5], 2, True))
   self.obj527.out_connections_.append(self.obj531)
   self.obj531.in_connections_.append(self.obj527)
   self.obj527.graphObject_.pendingConnections.append((self.obj527.graphObject_.tag, self.obj531.graphObject_.tag, [344.0, 181.0, 222.5, 180.0], 0, True))
   self.obj527.out_connections_.append(self.obj532)
   self.obj532.in_connections_.append(self.obj527)
   self.obj527.graphObject_.pendingConnections.append((self.obj527.graphObject_.tag, self.obj532.graphObject_.tag, [344.0, 181.0, 332.5, 120.0], 0, True))
   self.obj528.out_connections_.append(self.obj526)
   self.obj526.in_connections_.append(self.obj528)
   self.obj528.graphObject_.pendingConnections.append((self.obj528.graphObject_.tag, self.obj526.graphObject_.tag, [321.0, 59.0, 203.0, 70.5], 0, True))
   self.obj529.out_connections_.append(self.obj525)
   self.obj525.in_connections_.append(self.obj529)
   self.obj529.graphObject_.pendingConnections.append((self.obj529.graphObject_.tag, self.obj525.graphObject_.tag, [101.0, 179.0, 93.0, 130.5], 0, True))
   self.obj530.out_connections_.append(self.obj527)
   self.obj527.in_connections_.append(self.obj530)
   self.obj530.graphObject_.pendingConnections.append((self.obj530.graphObject_.tag, self.obj527.graphObject_.tag, [344.0, 181.0, 256.0, 121.0, 209.5, 129.5], 2, True))
   self.obj531.out_connections_.append(self.obj525)
   self.obj525.in_connections_.append(self.obj531)
   self.obj531.graphObject_.pendingConnections.append((self.obj531.graphObject_.tag, self.obj525.graphObject_.tag, [101.0, 179.0, 222.5, 180.0], 0, True))
   self.obj532.out_connections_.append(self.obj526)
   self.obj526.in_connections_.append(self.obj532)

   cobj0.RHS = ASG_omacs(self)

   self.obj534=Agent(self)
   self.obj534.preAction( cobj0.RHS.CREATE )
   self.obj534.isGraphObjectVisual = True

   if(hasattr(self.obj534, '_setHierarchicalLink')):
     self.obj534._setHierarchicalLink(False)

   # price
   self.obj534.price.setNone()

   # name
   self.obj534.name.setValue('')
   self.obj534.name.setNone()

   self.obj534.GGLabel.setValue(1)
   self.obj534.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(60.0,20.0,self.obj534)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj534.graphObject_ = new_obj
   self.obj5340= AttrCalc()
   self.obj5340.Copy=ATOM3Boolean()
   self.obj5340.Copy.setValue(('Copy from LHS', 1))
   self.obj5340.Copy.config = 0
   self.obj5340.Specify=ATOM3Constraint()
   self.obj5340.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj534.GGset2Any['price']= self.obj5340
   self.obj5341= AttrCalc()
   self.obj5341.Copy=ATOM3Boolean()
   self.obj5341.Copy.setValue(('Copy from LHS', 1))
   self.obj5341.Copy.config = 0
   self.obj5341.Specify=ATOM3Constraint()
   self.obj5341.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj534.GGset2Any['name']= self.obj5341

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj534)
   self.obj534.postAction( cobj0.RHS.CREATE )

   self.obj535=Capabilitie(self)
   self.obj535.preAction( cobj0.RHS.CREATE )
   self.obj535.isGraphObjectVisual = True

   if(hasattr(self.obj535, '_setHierarchicalLink')):
     self.obj535._setHierarchicalLink(False)

   # name
   self.obj535.name.setValue('')
   self.obj535.name.setNone()

   self.obj535.GGLabel.setValue(2)
   self.obj535.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(80.0,180.0,self.obj535)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj535.graphObject_ = new_obj
   self.obj5350= AttrCalc()
   self.obj5350.Copy=ATOM3Boolean()
   self.obj5350.Copy.setValue(('Copy from LHS', 1))
   self.obj5350.Copy.config = 0
   self.obj5350.Specify=ATOM3Constraint()
   self.obj5350.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj535.GGset2Any['name']= self.obj5350

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj535)
   self.obj535.postAction( cobj0.RHS.CREATE )

   self.obj536=Capabilitie(self)
   self.obj536.preAction( cobj0.RHS.CREATE )
   self.obj536.isGraphObjectVisual = True

   if(hasattr(self.obj536, '_setHierarchicalLink')):
     self.obj536._setHierarchicalLink(False)

   # name
   self.obj536.name.setValue('')
   self.obj536.name.setNone()

   self.obj536.GGLabel.setValue(3)
   self.obj536.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(300.0,20.0,self.obj536)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj536.graphObject_ = new_obj
   self.obj5360= AttrCalc()
   self.obj5360.Copy=ATOM3Boolean()
   self.obj5360.Copy.setValue(('Copy from LHS', 1))
   self.obj5360.Copy.config = 0
   self.obj5360.Specify=ATOM3Constraint()
   self.obj5360.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj536.GGset2Any['name']= self.obj5360

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj536)
   self.obj536.postAction( cobj0.RHS.CREATE )

   self.obj537=Role(self)
   self.obj537.preAction( cobj0.RHS.CREATE )
   self.obj537.isGraphObjectVisual = True

   if(hasattr(self.obj537, '_setHierarchicalLink')):
     self.obj537._setHierarchicalLink(False)

   # name
   self.obj537.name.setValue('')
   self.obj537.name.setNone()

   self.obj537.GGLabel.setValue(4)
   self.obj537.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(320.0,180.0,self.obj537)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj537.graphObject_ = new_obj
   self.obj5370= AttrCalc()
   self.obj5370.Copy=ATOM3Boolean()
   self.obj5370.Copy.setValue(('Copy from LHS', 1))
   self.obj5370.Copy.config = 0
   self.obj5370.Specify=ATOM3Constraint()
   self.obj5370.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj537.GGset2Any['name']= self.obj5370

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj537)
   self.obj537.postAction( cobj0.RHS.CREATE )

   self.obj538=posses(self)
   self.obj538.preAction( cobj0.RHS.CREATE )
   self.obj538.isGraphObjectVisual = True

   if(hasattr(self.obj538, '_setHierarchicalLink')):
     self.obj538._setHierarchicalLink(False)

   # rate
   self.obj538.rate.setNone()

   self.obj538.GGLabel.setValue(5)
   self.obj538.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(203.0,70.5,self.obj538)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj538.graphObject_ = new_obj
   self.obj5380= AttrCalc()
   self.obj5380.Copy=ATOM3Boolean()
   self.obj5380.Copy.setValue(('Copy from LHS', 1))
   self.obj5380.Copy.config = 0
   self.obj5380.Specify=ATOM3Constraint()
   self.obj5380.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj538.GGset2Any['rate']= self.obj5380

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj538)
   self.obj538.postAction( cobj0.RHS.CREATE )

   self.obj539=posses(self)
   self.obj539.preAction( cobj0.RHS.CREATE )
   self.obj539.isGraphObjectVisual = True

   if(hasattr(self.obj539, '_setHierarchicalLink')):
     self.obj539._setHierarchicalLink(False)

   # rate
   self.obj539.rate.setNone()

   self.obj539.GGLabel.setValue(6)
   self.obj539.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(93.0,130.5,self.obj539)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj539.graphObject_ = new_obj
   self.obj5390= AttrCalc()
   self.obj5390.Copy=ATOM3Boolean()
   self.obj5390.Copy.setValue(('Copy from LHS', 1))
   self.obj5390.Copy.config = 0
   self.obj5390.Specify=ATOM3Constraint()
   self.obj5390.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj539.GGset2Any['rate']= self.obj5390

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj539)
   self.obj539.postAction( cobj0.RHS.CREATE )

   self.obj540=CapableOf(self)
   self.obj540.preAction( cobj0.RHS.CREATE )
   self.obj540.isGraphObjectVisual = True

   if(hasattr(self.obj540, '_setHierarchicalLink')):
     self.obj540._setHierarchicalLink(False)

   # rate
   self.obj540.rate.setValue(0.0)

   self.obj540.GGLabel.setValue(9)
   self.obj540.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(209.5,129.5,self.obj540)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj540.graphObject_ = new_obj
   self.obj5400= AttrCalc()
   self.obj5400.Copy=ATOM3Boolean()
   self.obj5400.Copy.setValue(('Copy from LHS', 1))
   self.obj5400.Copy.config = 0
   self.obj5400.Specify=ATOM3Constraint()
   self.obj5400.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj540.GGset2Any['rate']= self.obj5400

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj540)
   self.obj540.postAction( cobj0.RHS.CREATE )

   self.obj541=require(self)
   self.obj541.preAction( cobj0.RHS.CREATE )
   self.obj541.isGraphObjectVisual = True

   if(hasattr(self.obj541, '_setHierarchicalLink')):
     self.obj541._setHierarchicalLink(False)

   self.obj541.GGLabel.setValue(7)
   self.obj541.graphClass_= graph_require
   if self.genGraphics:
      new_obj = graph_require(222.5,180.0,self.obj541)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj541.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj541)
   self.obj541.postAction( cobj0.RHS.CREATE )

   self.obj542=require(self)
   self.obj542.preAction( cobj0.RHS.CREATE )
   self.obj542.isGraphObjectVisual = True

   if(hasattr(self.obj542, '_setHierarchicalLink')):
     self.obj542._setHierarchicalLink(False)

   self.obj542.GGLabel.setValue(8)
   self.obj542.graphClass_= graph_require
   if self.genGraphics:
      new_obj = graph_require(332.5,120.0,self.obj542)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj542.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj542)
   self.obj542.postAction( cobj0.RHS.CREATE )

   self.obj534.out_connections_.append(self.obj538)
   self.obj538.in_connections_.append(self.obj534)
   self.obj534.out_connections_.append(self.obj539)
   self.obj539.in_connections_.append(self.obj534)
   self.obj534.graphObject_.pendingConnections.append((self.obj534.graphObject_.tag, self.obj539.graphObject_.tag, [97.0, 82.0, 93.0, 130.5], 2, 0))
   self.obj534.out_connections_.append(self.obj540)
   self.obj540.in_connections_.append(self.obj534)
   self.obj534.graphObject_.pendingConnections.append((self.obj534.graphObject_.tag, self.obj540.graphObject_.tag, [97.0, 82.0, 209.5, 129.5], 2, 0))
   self.obj537.out_connections_.append(self.obj541)
   self.obj541.in_connections_.append(self.obj537)
   self.obj537.graphObject_.pendingConnections.append((self.obj537.graphObject_.tag, self.obj541.graphObject_.tag, [351.0, 180.0, 222.5, 180.0], 2, 0))
   self.obj537.out_connections_.append(self.obj542)
   self.obj542.in_connections_.append(self.obj537)
   self.obj537.graphObject_.pendingConnections.append((self.obj537.graphObject_.tag, self.obj542.graphObject_.tag, [351.0, 180.0, 332.5, 120.0], 2, 0))
   self.obj538.out_connections_.append(self.obj536)
   self.obj536.in_connections_.append(self.obj538)
   self.obj538.graphObject_.pendingConnections.append((self.obj538.graphObject_.tag, self.obj536.graphObject_.tag, [331.0, 63.0, 203.0, 70.5], 2, 0))
   self.obj539.out_connections_.append(self.obj535)
   self.obj535.in_connections_.append(self.obj539)
   self.obj539.graphObject_.pendingConnections.append((self.obj539.graphObject_.tag, self.obj535.graphObject_.tag, [111.0, 183.0, 93.0, 130.5], 2, 0))
   self.obj540.out_connections_.append(self.obj537)
   self.obj537.in_connections_.append(self.obj540)
   self.obj540.graphObject_.pendingConnections.append((self.obj540.graphObject_.tag, self.obj537.graphObject_.tag, [351.0, 180.0, 209.5, 129.5], 2, 0))
   self.obj541.out_connections_.append(self.obj535)
   self.obj535.in_connections_.append(self.obj541)
   self.obj541.graphObject_.pendingConnections.append((self.obj541.graphObject_.tag, self.obj535.graphObject_.tag, [111.0, 183.0, 222.5, 180.0], 2, 0))
   self.obj542.out_connections_.append(self.obj536)
   self.obj536.in_connections_.append(self.obj542)

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\nagent = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nc1 = self.getMatched(graphID, self.LHS.nodeWithLabel(2))\nc2 = self.getMatched(graphID, self.LHS.nodeWithLabel(3))\nrole = self.getMatched(graphID, self.LHS.nodeWithLabel(4))\n\nreturn not ( hasattr(c1, agent.name.getValue() ) and \nhasattr(c1, role.name.getValue() ) and\nhasattr(c2, agent.name.getValue() ) and  hasattr(c2,  role.name.getValue()  ) )\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'agent = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nc1 = self.getMatched(graphID, self.LHS.nodeWithLabel(2))\nc2 = self.getMatched(graphID, self.LHS.nodeWithLabel(3))\nrole = self.getMatched(graphID, self.LHS.nodeWithLabel(4))\n\nsetattr( c1 ,  agent.name.getValue() , True )\nsetattr( c1 ,  role.name.getValue() , True )\n\nsetattr( c2 ,  agent.name.getValue() , True )\nsetattr( c2 ,  role.name.getValue() , True )\nprint\' Mark :(\'+agent.name.getValue()+\',\'+c1.name.getValue()+\',\'+c2.name.getValue()+\',\'+role.name.getValue()+\')\'\n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('Agent2RoleLink3', 20)
   cobj0.Order=ATOM3Integer(3)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

   from CapableOf import *
   from Goal import *
   from require import *
   from Agent import *
   from Capabilitie import *
   from Role import *
   from ASG_omacs import *
   from achieve import *
   from posses import *

   cobj0.LHS = ASG_omacs(self)

   self.obj547=Agent(self)
   self.obj547.preAction( cobj0.LHS.CREATE )
   self.obj547.isGraphObjectVisual = True

   if(hasattr(self.obj547, '_setHierarchicalLink')):
     self.obj547._setHierarchicalLink(False)

   # price
   self.obj547.price.setNone()

   # name
   self.obj547.name.setValue('')
   self.obj547.name.setNone()

   self.obj547.GGLabel.setValue(1)
   self.obj547.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(100.0,20.0,self.obj547)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj547.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj547)
   self.obj547.postAction( cobj0.LHS.CREATE )

   self.obj548=Capabilitie(self)
   self.obj548.preAction( cobj0.LHS.CREATE )
   self.obj548.isGraphObjectVisual = True

   if(hasattr(self.obj548, '_setHierarchicalLink')):
     self.obj548._setHierarchicalLink(False)

   # name
   self.obj548.name.setValue('')
   self.obj548.name.setNone()

   self.obj548.GGLabel.setValue(3)
   self.obj548.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(340.0,40.0,self.obj548)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj548.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj548)
   self.obj548.postAction( cobj0.LHS.CREATE )

   self.obj549=Capabilitie(self)
   self.obj549.preAction( cobj0.LHS.CREATE )
   self.obj549.isGraphObjectVisual = True

   if(hasattr(self.obj549, '_setHierarchicalLink')):
     self.obj549._setHierarchicalLink(False)

   # name
   self.obj549.name.setValue('')
   self.obj549.name.setNone()

   self.obj549.GGLabel.setValue(4)
   self.obj549.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(140.0,160.0,self.obj549)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj549.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj549)
   self.obj549.postAction( cobj0.LHS.CREATE )

   self.obj550=Role(self)
   self.obj550.preAction( cobj0.LHS.CREATE )
   self.obj550.isGraphObjectVisual = True

   if(hasattr(self.obj550, '_setHierarchicalLink')):
     self.obj550._setHierarchicalLink(False)

   # name
   self.obj550.name.setValue('')
   self.obj550.name.setNone()

   self.obj550.GGLabel.setValue(2)
   self.obj550.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(300.0,140.0,self.obj550)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj550.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj550)
   self.obj550.postAction( cobj0.LHS.CREATE )

   self.obj551=posses(self)
   self.obj551.preAction( cobj0.LHS.CREATE )
   self.obj551.isGraphObjectVisual = True

   if(hasattr(self.obj551, '_setHierarchicalLink')):
     self.obj551._setHierarchicalLink(False)

   # rate
   self.obj551.rate.setNone()

   self.obj551.GGLabel.setValue(5)
   self.obj551.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(143.0,120.5,self.obj551)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj551.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj551)
   self.obj551.postAction( cobj0.LHS.CREATE )

   self.obj552=CapableOf(self)
   self.obj552.preAction( cobj0.LHS.CREATE )
   self.obj552.isGraphObjectVisual = True

   if(hasattr(self.obj552, '_setHierarchicalLink')):
     self.obj552._setHierarchicalLink(False)

   # rate
   self.obj552.rate.setNone()

   self.obj552.GGLabel.setValue(8)
   self.obj552.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(224.5,111.5,self.obj552)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj552.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj552)
   self.obj552.postAction( cobj0.LHS.CREATE )

   self.obj553=require(self)
   self.obj553.preAction( cobj0.LHS.CREATE )
   self.obj553.isGraphObjectVisual = True

   if(hasattr(self.obj553, '_setHierarchicalLink')):
     self.obj553._setHierarchicalLink(False)

   self.obj553.GGLabel.setValue(7)
   self.obj553.graphClass_= graph_require
   if self.genGraphics:
      new_obj = graph_require(242.5,192.5,self.obj553)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj553.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj553)
   self.obj553.postAction( cobj0.LHS.CREATE )

   self.obj554=require(self)
   self.obj554.preAction( cobj0.LHS.CREATE )
   self.obj554.isGraphObjectVisual = True

   if(hasattr(self.obj554, '_setHierarchicalLink')):
     self.obj554._setHierarchicalLink(False)

   self.obj554.GGLabel.setValue(9)
   self.obj554.graphClass_= graph_require
   if self.genGraphics:
      new_obj = graph_require(351.0,111.5,self.obj554)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj554.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj554)
   self.obj554.postAction( cobj0.LHS.CREATE )

   self.obj547.out_connections_.append(self.obj551)
   self.obj551.in_connections_.append(self.obj547)
   self.obj547.graphObject_.pendingConnections.append((self.obj547.graphObject_.tag, self.obj551.graphObject_.tag, [137.0, 82.0, 143.0, 120.5], 2, 0))
   self.obj547.out_connections_.append(self.obj552)
   self.obj552.in_connections_.append(self.obj547)
   self.obj547.graphObject_.pendingConnections.append((self.obj547.graphObject_.tag, self.obj552.graphObject_.tag, [125.0, 82.0, 224.5, 111.5], 0, True))
   self.obj550.out_connections_.append(self.obj553)
   self.obj553.in_connections_.append(self.obj550)
   self.obj550.graphObject_.pendingConnections.append((self.obj550.graphObject_.tag, self.obj553.graphObject_.tag, [324.0, 186.0, 242.5, 192.5], 0, True))
   self.obj550.out_connections_.append(self.obj554)
   self.obj554.in_connections_.append(self.obj550)
   self.obj550.graphObject_.pendingConnections.append((self.obj550.graphObject_.tag, self.obj554.graphObject_.tag, [331.0, 140.0, 351.0, 111.5], 0, True))
   self.obj551.out_connections_.append(self.obj549)
   self.obj549.in_connections_.append(self.obj551)
   self.obj551.graphObject_.pendingConnections.append((self.obj551.graphObject_.tag, self.obj549.graphObject_.tag, [161.0, 159.0, 143.0, 120.5], 0, True))
   self.obj552.out_connections_.append(self.obj550)
   self.obj550.in_connections_.append(self.obj552)
   self.obj552.graphObject_.pendingConnections.append((self.obj552.graphObject_.tag, self.obj550.graphObject_.tag, [324.0, 141.0, 224.5, 111.5], 0, True))
   self.obj553.out_connections_.append(self.obj549)
   self.obj549.in_connections_.append(self.obj553)
   self.obj553.graphObject_.pendingConnections.append((self.obj553.graphObject_.tag, self.obj549.graphObject_.tag, [161.0, 199.0, 242.5, 192.5], 0, True))
   self.obj554.out_connections_.append(self.obj548)
   self.obj548.in_connections_.append(self.obj554)
   self.obj554.graphObject_.pendingConnections.append((self.obj554.graphObject_.tag, self.obj548.graphObject_.tag, [371.0, 83.0, 351.0, 111.5], 0, True))

   cobj0.RHS = ASG_omacs(self)

   self.obj556=Agent(self)
   self.obj556.preAction( cobj0.RHS.CREATE )
   self.obj556.isGraphObjectVisual = True

   if(hasattr(self.obj556, '_setHierarchicalLink')):
     self.obj556._setHierarchicalLink(False)

   # price
   self.obj556.price.setNone()

   # name
   self.obj556.name.setValue('')
   self.obj556.name.setNone()

   self.obj556.GGLabel.setValue(1)
   self.obj556.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(100.0,20.0,self.obj556)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj556.graphObject_ = new_obj
   self.obj5560= AttrCalc()
   self.obj5560.Copy=ATOM3Boolean()
   self.obj5560.Copy.setValue(('Copy from LHS', 1))
   self.obj5560.Copy.config = 0
   self.obj5560.Specify=ATOM3Constraint()
   self.obj5560.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj556.GGset2Any['price']= self.obj5560
   self.obj5561= AttrCalc()
   self.obj5561.Copy=ATOM3Boolean()
   self.obj5561.Copy.setValue(('Copy from LHS', 1))
   self.obj5561.Copy.config = 0
   self.obj5561.Specify=ATOM3Constraint()
   self.obj5561.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj556.GGset2Any['name']= self.obj5561

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj556)
   self.obj556.postAction( cobj0.RHS.CREATE )

   self.obj557=Capabilitie(self)
   self.obj557.preAction( cobj0.RHS.CREATE )
   self.obj557.isGraphObjectVisual = True

   if(hasattr(self.obj557, '_setHierarchicalLink')):
     self.obj557._setHierarchicalLink(False)

   # name
   self.obj557.name.setValue('')
   self.obj557.name.setNone()

   self.obj557.GGLabel.setValue(3)
   self.obj557.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(340.0,40.0,self.obj557)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj557.graphObject_ = new_obj
   self.obj5570= AttrCalc()
   self.obj5570.Copy=ATOM3Boolean()
   self.obj5570.Copy.setValue(('Copy from LHS', 1))
   self.obj5570.Copy.config = 0
   self.obj5570.Specify=ATOM3Constraint()
   self.obj5570.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj557.GGset2Any['name']= self.obj5570

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj557)
   self.obj557.postAction( cobj0.RHS.CREATE )

   self.obj558=Capabilitie(self)
   self.obj558.preAction( cobj0.RHS.CREATE )
   self.obj558.isGraphObjectVisual = True

   if(hasattr(self.obj558, '_setHierarchicalLink')):
     self.obj558._setHierarchicalLink(False)

   # name
   self.obj558.name.setValue('')
   self.obj558.name.setNone()

   self.obj558.GGLabel.setValue(4)
   self.obj558.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(140.0,160.0,self.obj558)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj558.graphObject_ = new_obj
   self.obj5580= AttrCalc()
   self.obj5580.Copy=ATOM3Boolean()
   self.obj5580.Copy.setValue(('Copy from LHS', 1))
   self.obj5580.Copy.config = 0
   self.obj5580.Specify=ATOM3Constraint()
   self.obj5580.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj558.GGset2Any['name']= self.obj5580

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj558)
   self.obj558.postAction( cobj0.RHS.CREATE )

   self.obj559=Role(self)
   self.obj559.preAction( cobj0.RHS.CREATE )
   self.obj559.isGraphObjectVisual = True

   if(hasattr(self.obj559, '_setHierarchicalLink')):
     self.obj559._setHierarchicalLink(False)

   # name
   self.obj559.name.setValue('')
   self.obj559.name.setNone()

   self.obj559.GGLabel.setValue(2)
   self.obj559.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(300.0,140.0,self.obj559)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj559.graphObject_ = new_obj
   self.obj5590= AttrCalc()
   self.obj5590.Copy=ATOM3Boolean()
   self.obj5590.Copy.setValue(('Copy from LHS', 1))
   self.obj5590.Copy.config = 0
   self.obj5590.Specify=ATOM3Constraint()
   self.obj5590.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj559.GGset2Any['name']= self.obj5590

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj559)
   self.obj559.postAction( cobj0.RHS.CREATE )

   self.obj560=posses(self)
   self.obj560.preAction( cobj0.RHS.CREATE )
   self.obj560.isGraphObjectVisual = True

   if(hasattr(self.obj560, '_setHierarchicalLink')):
     self.obj560._setHierarchicalLink(False)

   # rate
   self.obj560.rate.setNone()

   self.obj560.GGLabel.setValue(5)
   self.obj560.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(143.0,120.5,self.obj560)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj560.graphObject_ = new_obj
   self.obj5600= AttrCalc()
   self.obj5600.Copy=ATOM3Boolean()
   self.obj5600.Copy.setValue(('Copy from LHS', 1))
   self.obj5600.Copy.config = 0
   self.obj5600.Specify=ATOM3Constraint()
   self.obj5600.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj560.GGset2Any['rate']= self.obj5600

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj560)
   self.obj560.postAction( cobj0.RHS.CREATE )

   self.obj561=require(self)
   self.obj561.preAction( cobj0.RHS.CREATE )
   self.obj561.isGraphObjectVisual = True

   if(hasattr(self.obj561, '_setHierarchicalLink')):
     self.obj561._setHierarchicalLink(False)

   self.obj561.GGLabel.setValue(7)
   self.obj561.graphClass_= graph_require
   if self.genGraphics:
      new_obj = graph_require(242.5,192.5,self.obj561)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj561.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj561)
   self.obj561.postAction( cobj0.RHS.CREATE )

   self.obj562=require(self)
   self.obj562.preAction( cobj0.RHS.CREATE )
   self.obj562.isGraphObjectVisual = True

   if(hasattr(self.obj562, '_setHierarchicalLink')):
     self.obj562._setHierarchicalLink(False)

   self.obj562.GGLabel.setValue(9)
   self.obj562.graphClass_= graph_require
   if self.genGraphics:
      new_obj = graph_require(351.0,111.5,self.obj562)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj562.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj562)
   self.obj562.postAction( cobj0.RHS.CREATE )

   self.obj556.out_connections_.append(self.obj560)
   self.obj560.in_connections_.append(self.obj556)
   self.obj556.graphObject_.pendingConnections.append((self.obj556.graphObject_.tag, self.obj560.graphObject_.tag, [137.0, 82.0, 143.0, 120.5], 2, 0))
   self.obj559.out_connections_.append(self.obj561)
   self.obj561.in_connections_.append(self.obj559)
   self.obj559.graphObject_.pendingConnections.append((self.obj559.graphObject_.tag, self.obj561.graphObject_.tag, [331.0, 185.0, 242.5, 192.5], 2, 0))
   self.obj559.out_connections_.append(self.obj562)
   self.obj562.in_connections_.append(self.obj559)
   self.obj559.graphObject_.pendingConnections.append((self.obj559.graphObject_.tag, self.obj562.graphObject_.tag, [331.0, 140.0, 351.0, 111.5], 0, True))
   self.obj560.out_connections_.append(self.obj558)
   self.obj558.in_connections_.append(self.obj560)
   self.obj560.graphObject_.pendingConnections.append((self.obj560.graphObject_.tag, self.obj558.graphObject_.tag, [171.0, 163.0, 143.0, 120.5], 2, 0))
   self.obj561.out_connections_.append(self.obj558)
   self.obj558.in_connections_.append(self.obj561)
   self.obj561.graphObject_.pendingConnections.append((self.obj561.graphObject_.tag, self.obj558.graphObject_.tag, [171.0, 203.0, 242.5, 192.5], 2, 0))
   self.obj562.out_connections_.append(self.obj557)
   self.obj557.in_connections_.append(self.obj562)
   self.obj562.graphObject_.pendingConnections.append((self.obj562.graphObject_.tag, self.obj557.graphObject_.tag, [371.0, 83.0, 351.0, 111.5], 0, True))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'agent = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nrole  = self.getMatched(graphID, self.LHS.nodeWithLabel(2))\nc1 = self.getMatched(graphID, self.LHS.nodeWithLabel(3))\nc2 = self.getMatched(graphID, self.LHS.nodeWithLabel(4))\n\nreturn not ( hasattr(c1,  agent.name.getValue() ) and \nhasattr(c1,  role.name.getValue() ) and\nhasattr(c2,  agent.name.getValue() ) and  hasattr(c2, role.name.getValue() ) )\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'agent = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nc1 = self.getMatched(graphID, self.LHS.nodeWithLabel(4))\nc2 = self.getMatched(graphID, self.LHS.nodeWithLabel(3))\nrole = self.getMatched(graphID, self.LHS.nodeWithLabel(2))\n\nsetattr( c1 ,  agent.name.getValue() , True )\nsetattr( c1 ,  role.name.getValue() , True )\n\nsetattr( c2 ,  agent.name.getValue() , True )\nsetattr( c2 ,  role.name.getValue() , True )\nprint\' Eli : (\'+agent.name.getValue()+\',\'+c1.name.getValue()+\',\'+c2.name.getValue()+\',\'+role.name.getValue()+\')\'\n\n\n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('CollectInf1', 20)
   cobj0.Order=ATOM3Integer(4)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

   from CapableOf import *
   from Goal import *
   from require import *
   from Agent import *
   from Capabilitie import *
   from Role import *
   from ASG_omacs import *
   from achieve import *
   from posses import *

   cobj0.LHS = ASG_omacs(self)

   self.obj567=Agent(self)
   self.obj567.preAction( cobj0.LHS.CREATE )
   self.obj567.isGraphObjectVisual = True

   if(hasattr(self.obj567, '_setHierarchicalLink')):
     self.obj567._setHierarchicalLink(False)

   # price
   self.obj567.price.setNone()

   # name
   self.obj567.name.setValue('')
   self.obj567.name.setNone()

   self.obj567.GGLabel.setValue(1)
   self.obj567.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(20.0,20.0,self.obj567)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj567.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj567)
   self.obj567.postAction( cobj0.LHS.CREATE )

   self.obj568=Capabilitie(self)
   self.obj568.preAction( cobj0.LHS.CREATE )
   self.obj568.isGraphObjectVisual = True

   if(hasattr(self.obj568, '_setHierarchicalLink')):
     self.obj568._setHierarchicalLink(False)

   # name
   self.obj568.name.setValue('')
   self.obj568.name.setNone()

   self.obj568.GGLabel.setValue(3)
   self.obj568.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(140.0,160.0,self.obj568)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj568.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj568)
   self.obj568.postAction( cobj0.LHS.CREATE )

   self.obj569=Role(self)
   self.obj569.preAction( cobj0.LHS.CREATE )
   self.obj569.isGraphObjectVisual = True

   if(hasattr(self.obj569, '_setHierarchicalLink')):
     self.obj569._setHierarchicalLink(False)

   # name
   self.obj569.name.setValue('')
   self.obj569.name.setNone()

   self.obj569.GGLabel.setValue(2)
   self.obj569.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(380.0,180.0,self.obj569)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj569.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj569)
   self.obj569.postAction( cobj0.LHS.CREATE )

   self.obj570=posses(self)
   self.obj570.preAction( cobj0.LHS.CREATE )
   self.obj570.isGraphObjectVisual = True

   if(hasattr(self.obj570, '_setHierarchicalLink')):
     self.obj570._setHierarchicalLink(False)

   # rate
   self.obj570.rate.setNone()

   self.obj570.GGLabel.setValue(4)
   self.obj570.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(78.5,145.75,self.obj570)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj570.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj570)
   self.obj570.postAction( cobj0.LHS.CREATE )

   self.obj571=CapableOf(self)
   self.obj571.preAction( cobj0.LHS.CREATE )
   self.obj571.isGraphObjectVisual = True

   if(hasattr(self.obj571, '_setHierarchicalLink')):
     self.obj571._setHierarchicalLink(False)

   # rate
   self.obj571.rate.setNone()

   self.obj571.GGLabel.setValue(6)
   self.obj571.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(295.25,111.25,self.obj571)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj571.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj571)
   self.obj571.postAction( cobj0.LHS.CREATE )

   self.obj572=require(self)
   self.obj572.preAction( cobj0.LHS.CREATE )
   self.obj572.isGraphObjectVisual = True

   if(hasattr(self.obj572, '_setHierarchicalLink')):
     self.obj572._setHierarchicalLink(False)

   self.obj572.GGLabel.setValue(5)
   self.obj572.graphClass_= graph_require
   if self.genGraphics:
      new_obj = graph_require(291.0,171.5,self.obj572)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj572.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj572)
   self.obj572.postAction( cobj0.LHS.CREATE )

   self.obj567.out_connections_.append(self.obj570)
   self.obj570.in_connections_.append(self.obj567)
   self.obj567.graphObject_.pendingConnections.append((self.obj567.graphObject_.tag, self.obj570.graphObject_.tag, [45.0, 82.0, 49.5, 126.5, 78.5, 145.75], 2, True))
   self.obj567.out_connections_.append(self.obj571)
   self.obj571.in_connections_.append(self.obj567)
   self.obj567.graphObject_.pendingConnections.append((self.obj567.graphObject_.tag, self.obj571.graphObject_.tag, [45.0, 82.0, 205.5, 86.5, 295.25, 111.25], 2, True))
   self.obj569.out_connections_.append(self.obj572)
   self.obj572.in_connections_.append(self.obj569)
   self.obj569.graphObject_.pendingConnections.append((self.obj569.graphObject_.tag, self.obj572.graphObject_.tag, [404.0, 181.0, 374.0, 146.0, 291.0, 171.5], 2, True))
   self.obj570.out_connections_.append(self.obj568)
   self.obj568.in_connections_.append(self.obj570)
   self.obj570.graphObject_.pendingConnections.append((self.obj570.graphObject_.tag, self.obj568.graphObject_.tag, [161.0, 159.0, 107.5, 165.0, 78.5, 145.75], 2, True))
   self.obj571.out_connections_.append(self.obj569)
   self.obj569.in_connections_.append(self.obj571)
   self.obj571.graphObject_.pendingConnections.append((self.obj571.graphObject_.tag, self.obj569.graphObject_.tag, [404.0, 181.0, 385.0, 136.0, 295.25, 111.25], 2, True))
   self.obj572.out_connections_.append(self.obj568)
   self.obj568.in_connections_.append(self.obj572)
   self.obj572.graphObject_.pendingConnections.append((self.obj572.graphObject_.tag, self.obj568.graphObject_.tag, [161.0, 199.0, 208.0, 197.0, 291.0, 171.5], 2, True))

   cobj0.RHS = ASG_omacs(self)

   self.obj574=Agent(self)
   self.obj574.preAction( cobj0.RHS.CREATE )
   self.obj574.isGraphObjectVisual = True

   if(hasattr(self.obj574, '_setHierarchicalLink')):
     self.obj574._setHierarchicalLink(False)

   # price
   self.obj574.price.setNone()

   # name
   self.obj574.name.setValue('')
   self.obj574.name.setNone()

   self.obj574.GGLabel.setValue(1)
   self.obj574.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(20.0,20.0,self.obj574)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj574.graphObject_ = new_obj
   self.obj5740= AttrCalc()
   self.obj5740.Copy=ATOM3Boolean()
   self.obj5740.Copy.setValue(('Copy from LHS', 1))
   self.obj5740.Copy.config = 0
   self.obj5740.Specify=ATOM3Constraint()
   self.obj5740.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj574.GGset2Any['price']= self.obj5740
   self.obj5741= AttrCalc()
   self.obj5741.Copy=ATOM3Boolean()
   self.obj5741.Copy.setValue(('Copy from LHS', 1))
   self.obj5741.Copy.config = 0
   self.obj5741.Specify=ATOM3Constraint()
   self.obj5741.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj574.GGset2Any['name']= self.obj5741

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj574)
   self.obj574.postAction( cobj0.RHS.CREATE )

   self.obj575=Capabilitie(self)
   self.obj575.preAction( cobj0.RHS.CREATE )
   self.obj575.isGraphObjectVisual = True

   if(hasattr(self.obj575, '_setHierarchicalLink')):
     self.obj575._setHierarchicalLink(False)

   # name
   self.obj575.name.setValue('')
   self.obj575.name.setNone()

   self.obj575.GGLabel.setValue(3)
   self.obj575.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(140.0,160.0,self.obj575)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj575.graphObject_ = new_obj
   self.obj5750= AttrCalc()
   self.obj5750.Copy=ATOM3Boolean()
   self.obj5750.Copy.setValue(('Copy from LHS', 1))
   self.obj5750.Copy.config = 0
   self.obj5750.Specify=ATOM3Constraint()
   self.obj5750.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj575.GGset2Any['name']= self.obj5750

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj575)
   self.obj575.postAction( cobj0.RHS.CREATE )

   self.obj576=Role(self)
   self.obj576.preAction( cobj0.RHS.CREATE )
   self.obj576.isGraphObjectVisual = True

   if(hasattr(self.obj576, '_setHierarchicalLink')):
     self.obj576._setHierarchicalLink(False)

   # name
   self.obj576.name.setValue('')
   self.obj576.name.setNone()

   self.obj576.GGLabel.setValue(2)
   self.obj576.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(380.0,180.0,self.obj576)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj576.graphObject_ = new_obj
   self.obj5760= AttrCalc()
   self.obj5760.Copy=ATOM3Boolean()
   self.obj5760.Copy.setValue(('Copy from LHS', 1))
   self.obj5760.Copy.config = 0
   self.obj5760.Specify=ATOM3Constraint()
   self.obj5760.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj576.GGset2Any['name']= self.obj5760

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj576)
   self.obj576.postAction( cobj0.RHS.CREATE )

   self.obj577=posses(self)
   self.obj577.preAction( cobj0.RHS.CREATE )
   self.obj577.isGraphObjectVisual = True

   if(hasattr(self.obj577, '_setHierarchicalLink')):
     self.obj577._setHierarchicalLink(False)

   # rate
   self.obj577.rate.setNone()

   self.obj577.GGLabel.setValue(4)
   self.obj577.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(78.5,145.75,self.obj577)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj577.graphObject_ = new_obj
   self.obj5770= AttrCalc()
   self.obj5770.Copy=ATOM3Boolean()
   self.obj5770.Copy.setValue(('Copy from LHS', 1))
   self.obj5770.Copy.config = 0
   self.obj5770.Specify=ATOM3Constraint()
   self.obj5770.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj577.GGset2Any['rate']= self.obj5770

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj577)
   self.obj577.postAction( cobj0.RHS.CREATE )

   self.obj578=CapableOf(self)
   self.obj578.preAction( cobj0.RHS.CREATE )
   self.obj578.isGraphObjectVisual = True

   if(hasattr(self.obj578, '_setHierarchicalLink')):
     self.obj578._setHierarchicalLink(False)

   # rate
   self.obj578.rate.setNone()

   self.obj578.GGLabel.setValue(6)
   self.obj578.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(295.25,111.25,self.obj578)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj578.graphObject_ = new_obj
   self.obj5780= AttrCalc()
   self.obj5780.Copy=ATOM3Boolean()
   self.obj5780.Copy.setValue(('Copy from LHS', 1))
   self.obj5780.Copy.config = 0
   self.obj5780.Specify=ATOM3Constraint()
   self.obj5780.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj578.GGset2Any['rate']= self.obj5780

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj578)
   self.obj578.postAction( cobj0.RHS.CREATE )

   self.obj579=require(self)
   self.obj579.preAction( cobj0.RHS.CREATE )
   self.obj579.isGraphObjectVisual = True

   if(hasattr(self.obj579, '_setHierarchicalLink')):
     self.obj579._setHierarchicalLink(False)

   self.obj579.GGLabel.setValue(5)
   self.obj579.graphClass_= graph_require
   if self.genGraphics:
      new_obj = graph_require(291.0,171.5,self.obj579)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj579.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj579)
   self.obj579.postAction( cobj0.RHS.CREATE )

   self.obj574.out_connections_.append(self.obj577)
   self.obj577.in_connections_.append(self.obj574)
   self.obj574.graphObject_.pendingConnections.append((self.obj574.graphObject_.tag, self.obj577.graphObject_.tag, [57.0, 82.0, 78.5, 145.75], 2, 0))
   self.obj574.out_connections_.append(self.obj578)
   self.obj578.in_connections_.append(self.obj574)
   self.obj574.graphObject_.pendingConnections.append((self.obj574.graphObject_.tag, self.obj578.graphObject_.tag, [57.0, 82.0, 295.25, 111.25], 2, 0))
   self.obj576.out_connections_.append(self.obj579)
   self.obj579.in_connections_.append(self.obj576)
   self.obj576.graphObject_.pendingConnections.append((self.obj576.graphObject_.tag, self.obj579.graphObject_.tag, [411.0, 180.0, 291.0, 171.5], 2, 0))
   self.obj577.out_connections_.append(self.obj575)
   self.obj575.in_connections_.append(self.obj577)
   self.obj577.graphObject_.pendingConnections.append((self.obj577.graphObject_.tag, self.obj575.graphObject_.tag, [171.0, 163.0, 78.5, 145.75], 2, 0))
   self.obj578.out_connections_.append(self.obj576)
   self.obj576.in_connections_.append(self.obj578)
   self.obj578.graphObject_.pendingConnections.append((self.obj578.graphObject_.tag, self.obj576.graphObject_.tag, [411.0, 180.0, 295.25, 111.25], 2, 0))
   self.obj579.out_connections_.append(self.obj575)
   self.obj575.in_connections_.append(self.obj579)
   self.obj579.graphObject_.pendingConnections.append((self.obj579.graphObject_.tag, self.obj575.graphObject_.tag, [171.0, 163.0, 291.0, 171.5], 2, 0))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'agent = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nrole  = self.getMatched(graphID, self.LHS.nodeWithLabel(2))\nlink = self.getMatched(graphID, self.LHS.nodeWithLabel(5)) \n\nreturn not ( hasattr(link,  "rule1"+agent.name.getValue()+role.name.getValue() ))\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'linkk = self.getMatched(graphID, self.LHS.nodeWithLabel(5)) \nc1 = self.getMatched(graphID, self.LHS.nodeWithLabel(3)) \na = self.getMatched(graphID, self.LHS.nodeWithLabel(1)) \nr = self.getMatched(graphID, self.LHS.nodeWithLabel(2)) \nlink = self.getMatched(graphID, self.LHS.nodeWithLabel(4))\n\nsetattr( linkk ,  "rule1"+a.name.getValue()+r.name.getValue() , True )\n\nprint "Collect 1 "+a.name.getValue()+" "+r.name.getValue()+" "+str(link.rate.getValue())+c1.name.getValue()\nif not ( "nb"+r.name.getValue() in  self.graphRewritingSystem.Dictag[a.name.getValue()].keys() ):\n self.graphRewritingSystem.Dictag[a.name.getValue()]["nb"+r.name.getValue()]=0\n\nself.graphRewritingSystem.Dictag[a.name.getValue()]["nb"+r.name.getValue()] += 1\nself.graphRewritingSystem.Dictag[a.name.getValue()][r.name.getValue()] += link.rate.getValue()\nself.graphRewritingSystem.Dictag[a.name.getValue()][c1.name.getValue()] = link.rate.getValue()\nprint "Collect inf 1 "+str( self.graphRewritingSystem.Dictag )\n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('CollectInf2', 20)
   cobj0.Order=ATOM3Integer(5)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

   from CapableOf import *
   from Goal import *
   from require import *
   from Agent import *
   from Capabilitie import *
   from Role import *
   from ASG_omacs import *
   from achieve import *
   from posses import *

   cobj0.LHS = ASG_omacs(self)

   self.obj584=Agent(self)
   self.obj584.preAction( cobj0.LHS.CREATE )
   self.obj584.isGraphObjectVisual = True

   if(hasattr(self.obj584, '_setHierarchicalLink')):
     self.obj584._setHierarchicalLink(False)

   # price
   self.obj584.price.setNone()

   # name
   self.obj584.name.setValue('')
   self.obj584.name.setNone()

   self.obj584.GGLabel.setValue(1)
   self.obj584.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(40.0,20.0,self.obj584)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj584.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj584)
   self.obj584.postAction( cobj0.LHS.CREATE )

   self.obj585=Role(self)
   self.obj585.preAction( cobj0.LHS.CREATE )
   self.obj585.isGraphObjectVisual = True

   if(hasattr(self.obj585, '_setHierarchicalLink')):
     self.obj585._setHierarchicalLink(False)

   # name
   self.obj585.name.setValue('')
   self.obj585.name.setNone()

   self.obj585.GGLabel.setValue(2)
   self.obj585.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(360.0,160.0,self.obj585)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj585.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj585)
   self.obj585.postAction( cobj0.LHS.CREATE )

   self.obj586=CapableOf(self)
   self.obj586.preAction( cobj0.LHS.CREATE )
   self.obj586.isGraphObjectVisual = True

   if(hasattr(self.obj586, '_setHierarchicalLink')):
     self.obj586._setHierarchicalLink(False)

   # rate
   self.obj586.rate.setNone()

   self.obj586.GGLabel.setValue(3)
   self.obj586.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(220.0,114.5,self.obj586)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj586.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj586)
   self.obj586.postAction( cobj0.LHS.CREATE )

   self.obj584.out_connections_.append(self.obj586)
   self.obj586.in_connections_.append(self.obj584)
   self.obj584.graphObject_.pendingConnections.append((self.obj584.graphObject_.tag, self.obj586.graphObject_.tag, [65.0, 82.0, 84.0, 138.0, 220.0, 114.5], 2, True))
   self.obj586.out_connections_.append(self.obj585)
   self.obj585.in_connections_.append(self.obj586)
   self.obj586.graphObject_.pendingConnections.append((self.obj586.graphObject_.tag, self.obj585.graphObject_.tag, [384.0, 161.0, 356.0, 91.0, 220.0, 114.5], 2, True))

   cobj0.RHS = ASG_omacs(self)

   self.obj588=Agent(self)
   self.obj588.preAction( cobj0.RHS.CREATE )
   self.obj588.isGraphObjectVisual = True

   if(hasattr(self.obj588, '_setHierarchicalLink')):
     self.obj588._setHierarchicalLink(False)

   # price
   self.obj588.price.setNone()

   # name
   self.obj588.name.setValue('')
   self.obj588.name.setNone()

   self.obj588.GGLabel.setValue(1)
   self.obj588.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(40.0,20.0,self.obj588)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj588.graphObject_ = new_obj
   self.obj5880= AttrCalc()
   self.obj5880.Copy=ATOM3Boolean()
   self.obj5880.Copy.setValue(('Copy from LHS', 1))
   self.obj5880.Copy.config = 0
   self.obj5880.Specify=ATOM3Constraint()
   self.obj5880.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj588.GGset2Any['price']= self.obj5880
   self.obj5881= AttrCalc()
   self.obj5881.Copy=ATOM3Boolean()
   self.obj5881.Copy.setValue(('Copy from LHS', 1))
   self.obj5881.Copy.config = 0
   self.obj5881.Specify=ATOM3Constraint()
   self.obj5881.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj588.GGset2Any['name']= self.obj5881

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj588)
   self.obj588.postAction( cobj0.RHS.CREATE )

   self.obj589=Role(self)
   self.obj589.preAction( cobj0.RHS.CREATE )
   self.obj589.isGraphObjectVisual = True

   if(hasattr(self.obj589, '_setHierarchicalLink')):
     self.obj589._setHierarchicalLink(False)

   # name
   self.obj589.name.setValue('')
   self.obj589.name.setNone()

   self.obj589.GGLabel.setValue(2)
   self.obj589.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(360.0,160.0,self.obj589)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj589.graphObject_ = new_obj
   self.obj5890= AttrCalc()
   self.obj5890.Copy=ATOM3Boolean()
   self.obj5890.Copy.setValue(('Copy from LHS', 1))
   self.obj5890.Copy.config = 0
   self.obj5890.Specify=ATOM3Constraint()
   self.obj5890.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj589.GGset2Any['name']= self.obj5890

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj589)
   self.obj589.postAction( cobj0.RHS.CREATE )

   self.obj590=CapableOf(self)
   self.obj590.preAction( cobj0.RHS.CREATE )
   self.obj590.isGraphObjectVisual = True

   if(hasattr(self.obj590, '_setHierarchicalLink')):
     self.obj590._setHierarchicalLink(False)

   # rate
   self.obj590.rate.setNone()

   self.obj590.GGLabel.setValue(3)
   self.obj590.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(220.0,114.5,self.obj590)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj590.graphObject_ = new_obj
   self.obj5900= AttrCalc()
   self.obj5900.Copy=ATOM3Boolean()
   self.obj5900.Copy.setValue(('Copy from LHS', 1))
   self.obj5900.Copy.config = 0
   self.obj5900.Specify=ATOM3Constraint()
   self.obj5900.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj590.GGset2Any['rate']= self.obj5900

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj590)
   self.obj590.postAction( cobj0.RHS.CREATE )

   self.obj588.out_connections_.append(self.obj590)
   self.obj590.in_connections_.append(self.obj588)
   self.obj588.graphObject_.pendingConnections.append((self.obj588.graphObject_.tag, self.obj590.graphObject_.tag, [77.0, 82.0, 220.0, 114.5], 2, 0))
   self.obj590.out_connections_.append(self.obj589)
   self.obj589.in_connections_.append(self.obj590)
   self.obj590.graphObject_.pendingConnections.append((self.obj590.graphObject_.tag, self.obj589.graphObject_.tag, [391.0, 160.0, 220.0, 114.5], 2, 0))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'link = self.getMatched(graphID, self.LHS.nodeWithLabel(3))\nreturn not ( hasattr(link,"done") )\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'a = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nr = self.getMatched(graphID, self.LHS.nodeWithLabel(2))\nlink = self.getMatched(graphID, self.LHS.nodeWithLabel(3))\n\nlink.done = True \n\n\nprint "Collect 2 "+a.name.getValue()+" "+r.name.getValue()+" "+str(link.rate.getValue())\n\nself.graphRewritingSystem.Dictag[a.name.getValue()][r.name.getValue()] /=  self.graphRewritingSystem.Dictag[a.name.getValue()]["nb"+r.name.getValue()]\nround( self.graphRewritingSystem.Dictag[a.name.getValue()][r.name.getValue()] ,3)\nprint "Collect 2  : "+str(  self.graphRewritingSystem.Dictag )\n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('CollectInf3', 20)
   cobj0.Order=ATOM3Integer(6)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

   from CapableOf import *
   from Goal import *
   from require import *
   from Agent import *
   from Capabilitie import *
   from Role import *
   from ASG_omacs import *
   from achieve import *
   from posses import *

   cobj0.LHS = ASG_omacs(self)

   self.obj595=Role(self)
   self.obj595.preAction( cobj0.LHS.CREATE )
   self.obj595.isGraphObjectVisual = True

   if(hasattr(self.obj595, '_setHierarchicalLink')):
     self.obj595._setHierarchicalLink(False)

   # name
   self.obj595.name.setValue('')
   self.obj595.name.setNone()

   self.obj595.GGLabel.setValue(2)
   self.obj595.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(40.0,40.0,self.obj595)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj595.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj595)
   self.obj595.postAction( cobj0.LHS.CREATE )

   self.obj596=Goal(self)
   self.obj596.preAction( cobj0.LHS.CREATE )
   self.obj596.isGraphObjectVisual = True

   if(hasattr(self.obj596, '_setHierarchicalLink')):
     self.obj596._setHierarchicalLink(False)

   # name
   self.obj596.name.setValue('')
   self.obj596.name.setNone()

   self.obj596.GGLabel.setValue(1)
   self.obj596.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(300.0,160.0,self.obj596)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj596.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj596)
   self.obj596.postAction( cobj0.LHS.CREATE )

   self.obj597=achieve(self)
   self.obj597.preAction( cobj0.LHS.CREATE )
   self.obj597.isGraphObjectVisual = True

   if(hasattr(self.obj597, '_setHierarchicalLink')):
     self.obj597._setHierarchicalLink(False)

   # rate
   self.obj597.rate.setNone()

   self.obj597.GGLabel.setValue(3)
   self.obj597.graphClass_= graph_achieve
   if self.genGraphics:
      new_obj = graph_achieve(171.25,141.25,self.obj597)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj597.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj597)
   self.obj597.postAction( cobj0.LHS.CREATE )

   self.obj595.out_connections_.append(self.obj597)
   self.obj597.in_connections_.append(self.obj595)
   self.obj595.graphObject_.pendingConnections.append((self.obj595.graphObject_.tag, self.obj597.graphObject_.tag, [64.0, 86.0, 106.5, 122.5, 171.25, 141.25], 2, True))
   self.obj597.out_connections_.append(self.obj596)
   self.obj596.in_connections_.append(self.obj597)
   self.obj597.graphObject_.pendingConnections.append((self.obj597.graphObject_.tag, self.obj596.graphObject_.tag, [323.0, 161.0, 236.0, 160.0, 171.25, 141.25], 2, True))

   cobj0.RHS = ASG_omacs(self)

   self.obj599=Role(self)
   self.obj599.preAction( cobj0.RHS.CREATE )
   self.obj599.isGraphObjectVisual = True

   if(hasattr(self.obj599, '_setHierarchicalLink')):
     self.obj599._setHierarchicalLink(False)

   # name
   self.obj599.name.setValue('')
   self.obj599.name.setNone()

   self.obj599.GGLabel.setValue(2)
   self.obj599.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(40.0,40.0,self.obj599)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj599.graphObject_ = new_obj
   self.obj5990= AttrCalc()
   self.obj5990.Copy=ATOM3Boolean()
   self.obj5990.Copy.setValue(('Copy from LHS', 1))
   self.obj5990.Copy.config = 0
   self.obj5990.Specify=ATOM3Constraint()
   self.obj5990.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj599.GGset2Any['name']= self.obj5990

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj599)
   self.obj599.postAction( cobj0.RHS.CREATE )

   self.obj600=Goal(self)
   self.obj600.preAction( cobj0.RHS.CREATE )
   self.obj600.isGraphObjectVisual = True

   if(hasattr(self.obj600, '_setHierarchicalLink')):
     self.obj600._setHierarchicalLink(False)

   # name
   self.obj600.name.setValue('')
   self.obj600.name.setNone()

   self.obj600.GGLabel.setValue(1)
   self.obj600.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(300.0,160.0,self.obj600)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj600.graphObject_ = new_obj
   self.obj6000= AttrCalc()
   self.obj6000.Copy=ATOM3Boolean()
   self.obj6000.Copy.setValue(('Copy from LHS', 1))
   self.obj6000.Copy.config = 0
   self.obj6000.Specify=ATOM3Constraint()
   self.obj6000.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj600.GGset2Any['name']= self.obj6000

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj600)
   self.obj600.postAction( cobj0.RHS.CREATE )

   self.obj601=achieve(self)
   self.obj601.preAction( cobj0.RHS.CREATE )
   self.obj601.isGraphObjectVisual = True

   if(hasattr(self.obj601, '_setHierarchicalLink')):
     self.obj601._setHierarchicalLink(False)

   # rate
   self.obj601.rate.setNone()

   self.obj601.GGLabel.setValue(3)
   self.obj601.graphClass_= graph_achieve
   if self.genGraphics:
      new_obj = graph_achieve(171.25,141.25,self.obj601)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj601.graphObject_ = new_obj
   self.obj6010= AttrCalc()
   self.obj6010.Copy=ATOM3Boolean()
   self.obj6010.Copy.setValue(('Copy from LHS', 1))
   self.obj6010.Copy.config = 0
   self.obj6010.Specify=ATOM3Constraint()
   self.obj6010.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj601.GGset2Any['rate']= self.obj6010

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj601)
   self.obj601.postAction( cobj0.RHS.CREATE )

   self.obj599.out_connections_.append(self.obj601)
   self.obj601.in_connections_.append(self.obj599)
   self.obj599.graphObject_.pendingConnections.append((self.obj599.graphObject_.tag, self.obj601.graphObject_.tag, [71.0, 85.0, 171.25, 141.25], 2, 0))
   self.obj601.out_connections_.append(self.obj600)
   self.obj600.in_connections_.append(self.obj601)
   self.obj601.graphObject_.pendingConnections.append((self.obj601.graphObject_.tag, self.obj600.graphObject_.tag, [333.0, 161.0, 171.25, 141.25], 2, 0))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\ng = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nr  = self.getMatched(graphID, self.LHS.nodeWithLabel(2))\nlink  = self.getMatched(graphID, self.LHS.nodeWithLabel(3))\n\nreturn not ( hasattr(link,  "rule2"+g.name.getValue()+r.name.getValue() ))\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'g = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nr  = self.getMatched(graphID, self.LHS.nodeWithLabel(2))\nlink  = self.getMatched(graphID, self.LHS.nodeWithLabel(3))\n\nsetattr( link ,  "rule2"+g.name.getValue()+r.name.getValue() , True )\n\nprint "Collect 3 "+g.name.getValue()+" "+r.name.getValue()+" "+str(link.rate.getValue() )\nif not (r.name.getValue() in self.graphRewritingSystem.Dictro.keys() ) :\n self.graphRewritingSystem.Dictro[r.name.getValue()] = {}\nself.graphRewritingSystem.Dictro[r.name.getValue()][g.name.getValue()] = link.rate.getValue()\n\nprint "Collect inf 3 DictRole "+str( self.graphRewritingSystem.Dictro )\n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('TransAgent2Raw', 20)
   cobj0.Order=ATOM3Integer(9)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

   from CapableOf import *
   from Goal import *
   from require import *
   from Agent import *
   from Capabilitie import *
   from Role import *
   from ASG_omacs import *
   from achieve import *
   from posses import *
   from GenericGraphEdge import *
   from ASG_pns import *
   from metarial import *
   from GenericGraphNode import *
   from rawMaterial import *
   from fromMaterial import *
   from intoProduct import *
   from fromRaw import *
   from ASG_GenericGraph import *
   from intoMaterial import *
   from product import *
   from operatingUnit import *

   cobj0.LHS = ASG_omacs(self)

   self.obj606=Agent(self)
   self.obj606.preAction( cobj0.LHS.CREATE )
   self.obj606.isGraphObjectVisual = True

   if(hasattr(self.obj606, '_setHierarchicalLink')):
     self.obj606._setHierarchicalLink(False)

   # price
   self.obj606.price.setNone()

   # name
   self.obj606.name.setValue('')
   self.obj606.name.setNone()

   self.obj606.GGLabel.setValue(1)
   self.obj606.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(100.0,20.0,self.obj606)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj606.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj606)
   self.obj606.postAction( cobj0.LHS.CREATE )

   self.obj607=Role(self)
   self.obj607.preAction( cobj0.LHS.CREATE )
   self.obj607.isGraphObjectVisual = True

   if(hasattr(self.obj607, '_setHierarchicalLink')):
     self.obj607._setHierarchicalLink(False)

   # name
   self.obj607.name.setValue('')
   self.obj607.name.setNone()

   self.obj607.GGLabel.setValue(2)
   self.obj607.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(360.0,160.0,self.obj607)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj607.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj607)
   self.obj607.postAction( cobj0.LHS.CREATE )

   self.obj608=CapableOf(self)
   self.obj608.preAction( cobj0.LHS.CREATE )
   self.obj608.isGraphObjectVisual = True

   if(hasattr(self.obj608, '_setHierarchicalLink')):
     self.obj608._setHierarchicalLink(False)

   # rate
   self.obj608.rate.setNone()

   self.obj608.GGLabel.setValue(3)
   self.obj608.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(281.5,134.0,self.obj608)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj608.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj608)
   self.obj608.postAction( cobj0.LHS.CREATE )

   self.obj606.out_connections_.append(self.obj608)
   self.obj608.in_connections_.append(self.obj606)
   self.obj606.graphObject_.pendingConnections.append((self.obj606.graphObject_.tag, self.obj608.graphObject_.tag, [125.0, 82.0, 161.0, 153.0, 281.5, 134.0], 2, True))
   self.obj608.out_connections_.append(self.obj607)
   self.obj607.in_connections_.append(self.obj608)
   self.obj608.graphObject_.pendingConnections.append((self.obj608.graphObject_.tag, self.obj607.graphObject_.tag, [384.0, 161.0, 402.0, 115.0, 281.5, 134.0], 2, True))

   cobj0.RHS = ASG_omacs(self)
   cobj0.RHS.merge(ASG_pns(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj612=Agent(self)
   self.obj612.preAction( cobj0.RHS.CREATE )
   self.obj612.isGraphObjectVisual = True

   if(hasattr(self.obj612, '_setHierarchicalLink')):
     self.obj612._setHierarchicalLink(False)

   # price
   self.obj612.price.setNone()

   # name
   self.obj612.name.setValue('')
   self.obj612.name.setNone()

   self.obj612.GGLabel.setValue(1)
   self.obj612.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(100.0,20.0,self.obj612)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj612.graphObject_ = new_obj
   self.obj6120= AttrCalc()
   self.obj6120.Copy=ATOM3Boolean()
   self.obj6120.Copy.setValue(('Copy from LHS', 1))
   self.obj6120.Copy.config = 0
   self.obj6120.Specify=ATOM3Constraint()
   self.obj6120.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj612.GGset2Any['price']= self.obj6120
   self.obj6121= AttrCalc()
   self.obj6121.Copy=ATOM3Boolean()
   self.obj6121.Copy.setValue(('Copy from LHS', 1))
   self.obj6121.Copy.config = 0
   self.obj6121.Specify=ATOM3Constraint()
   self.obj6121.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj612.GGset2Any['name']= self.obj6121

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj612)
   self.obj612.postAction( cobj0.RHS.CREATE )

   self.obj613=Role(self)
   self.obj613.preAction( cobj0.RHS.CREATE )
   self.obj613.isGraphObjectVisual = True

   if(hasattr(self.obj613, '_setHierarchicalLink')):
     self.obj613._setHierarchicalLink(False)

   # name
   self.obj613.name.setValue('')
   self.obj613.name.setNone()

   self.obj613.GGLabel.setValue(2)
   self.obj613.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(360.0,160.0,self.obj613)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj613.graphObject_ = new_obj
   self.obj6130= AttrCalc()
   self.obj6130.Copy=ATOM3Boolean()
   self.obj6130.Copy.setValue(('Copy from LHS', 1))
   self.obj6130.Copy.config = 0
   self.obj6130.Specify=ATOM3Constraint()
   self.obj6130.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj613.GGset2Any['name']= self.obj6130

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj613)
   self.obj613.postAction( cobj0.RHS.CREATE )

   self.obj614=CapableOf(self)
   self.obj614.preAction( cobj0.RHS.CREATE )
   self.obj614.isGraphObjectVisual = True

   if(hasattr(self.obj614, '_setHierarchicalLink')):
     self.obj614._setHierarchicalLink(False)

   # rate
   self.obj614.rate.setValue(0.0)

   self.obj614.GGLabel.setValue(3)
   self.obj614.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(281.5,134.0,self.obj614)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj614.graphObject_ = new_obj
   self.obj6140= AttrCalc()
   self.obj6140.Copy=ATOM3Boolean()
   self.obj6140.Copy.setValue(('Copy from LHS', 1))
   self.obj6140.Copy.config = 0
   self.obj6140.Specify=ATOM3Constraint()
   self.obj6140.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj614.GGset2Any['rate']= self.obj6140

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj614)
   self.obj614.postAction( cobj0.RHS.CREATE )

   self.obj615=rawMaterial(self)
   self.obj615.preAction( cobj0.RHS.CREATE )
   self.obj615.isGraphObjectVisual = True

   if(hasattr(self.obj615, '_setHierarchicalLink')):
     self.obj615._setHierarchicalLink(False)

   # MaxFlow
   self.obj615.MaxFlow.setValue(999999)

   # price
   self.obj615.price.setValue(0)

   # Name
   self.obj615.Name.setValue('')
   self.obj615.Name.setNone()

   # ReqFlow
   self.obj615.ReqFlow.setValue(0)

   self.obj615.GGLabel.setValue(6)
   self.obj615.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(280.0,20.0,self.obj615)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj615.graphObject_ = new_obj
   self.obj6150= AttrCalc()
   self.obj6150.Copy=ATOM3Boolean()
   self.obj6150.Copy.setValue(('Copy from LHS', 1))
   self.obj6150.Copy.config = 0
   self.obj6150.Specify=ATOM3Constraint()
   self.obj6150.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj615.GGset2Any['MaxFlow']= self.obj6150
   self.obj6151= AttrCalc()
   self.obj6151.Copy=ATOM3Boolean()
   self.obj6151.Copy.setValue(('Copy from LHS', 1))
   self.obj6151.Copy.config = 0
   self.obj6151.Specify=ATOM3Constraint()
   self.obj6151.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj615.GGset2Any['price']= self.obj6151
   self.obj6152= AttrCalc()
   self.obj6152.Copy=ATOM3Boolean()
   self.obj6152.Copy.setValue(('Copy from LHS', 0))
   self.obj6152.Copy.config = 0
   self.obj6152.Specify=ATOM3Constraint()
   self.obj6152.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()\n\n\n\n'))
   self.obj615.GGset2Any['Name']= self.obj6152
   self.obj6153= AttrCalc()
   self.obj6153.Copy=ATOM3Boolean()
   self.obj6153.Copy.setValue(('Copy from LHS', 1))
   self.obj6153.Copy.config = 0
   self.obj6153.Specify=ATOM3Constraint()
   self.obj6153.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj615.GGset2Any['ReqFlow']= self.obj6153

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj615)
   self.obj615.postAction( cobj0.RHS.CREATE )

   self.obj616=GenericGraphEdge(self)
   self.obj616.preAction( cobj0.RHS.CREATE )
   self.obj616.isGraphObjectVisual = True

   if(hasattr(self.obj616, '_setHierarchicalLink')):
     self.obj616._setHierarchicalLink(False)

   self.obj616.GGLabel.setValue(7)
   self.obj616.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(220.5,79.0,self.obj616)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj616.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj616)
   self.obj616.postAction( cobj0.RHS.CREATE )

   self.obj612.out_connections_.append(self.obj614)
   self.obj614.in_connections_.append(self.obj612)
   self.obj612.graphObject_.pendingConnections.append((self.obj612.graphObject_.tag, self.obj614.graphObject_.tag, [137.0, 82.0, 281.5, 134.0], 2, 0))
   self.obj612.out_connections_.append(self.obj616)
   self.obj616.in_connections_.append(self.obj612)
   self.obj612.graphObject_.pendingConnections.append((self.obj612.graphObject_.tag, self.obj616.graphObject_.tag, [137.0, 82.0, 220.5, 79.0], 0, True))
   self.obj614.out_connections_.append(self.obj613)
   self.obj613.in_connections_.append(self.obj614)
   self.obj614.graphObject_.pendingConnections.append((self.obj614.graphObject_.tag, self.obj613.graphObject_.tag, [391.0, 160.0, 281.5, 134.0], 2, 0))
   self.obj616.out_connections_.append(self.obj615)
   self.obj615.in_connections_.append(self.obj616)
   self.obj616.graphObject_.pendingConnections.append((self.obj616.graphObject_.tag, self.obj615.graphObject_.tag, [304.0, 76.0, 220.5, 79.0], 0, True))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n\nprint "Dic ro "+str( self.graphRewritingSystem.Dictro )\nprint "Dic ag"+str( self.graphRewritingSystem.Dictag )\n\nnode = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\n\n\nreturn not hasattr(node, "Agent2Raw")\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'node = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) )\nnode.Agent2Raw = True \n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('TransLinkAR2OpUnit', 20)
   cobj0.Order=ATOM3Integer(10)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

   from CapableOf import *
   from Goal import *
   from require import *
   from Agent import *
   from Capabilitie import *
   from Role import *
   from ASG_omacs import *
   from achieve import *
   from posses import *
   from GenericGraphEdge import *
   from ASG_pns import *
   from metarial import *
   from GenericGraphNode import *
   from rawMaterial import *
   from fromMaterial import *
   from intoProduct import *
   from fromRaw import *
   from ASG_GenericGraph import *
   from intoMaterial import *
   from product import *
   from operatingUnit import *

   cobj0.LHS = ASG_omacs(self)

   self.obj621=Agent(self)
   self.obj621.preAction( cobj0.LHS.CREATE )
   self.obj621.isGraphObjectVisual = True

   if(hasattr(self.obj621, '_setHierarchicalLink')):
     self.obj621._setHierarchicalLink(False)

   # price
   self.obj621.price.setNone()

   # name
   self.obj621.name.setValue('')
   self.obj621.name.setNone()

   self.obj621.GGLabel.setValue(1)
   self.obj621.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(60.0,40.0,self.obj621)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj621.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj621)
   self.obj621.postAction( cobj0.LHS.CREATE )

   self.obj622=Role(self)
   self.obj622.preAction( cobj0.LHS.CREATE )
   self.obj622.isGraphObjectVisual = True

   if(hasattr(self.obj622, '_setHierarchicalLink')):
     self.obj622._setHierarchicalLink(False)

   # name
   self.obj622.name.setValue('')
   self.obj622.name.setNone()

   self.obj622.GGLabel.setValue(2)
   self.obj622.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(320.0,220.0,self.obj622)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj622.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj622)
   self.obj622.postAction( cobj0.LHS.CREATE )

   self.obj623=CapableOf(self)
   self.obj623.preAction( cobj0.LHS.CREATE )
   self.obj623.isGraphObjectVisual = True

   if(hasattr(self.obj623, '_setHierarchicalLink')):
     self.obj623._setHierarchicalLink(False)

   # rate
   self.obj623.rate.setNone()

   self.obj623.GGLabel.setValue(3)
   self.obj623.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(230.0,173.0,self.obj623)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj623.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj623)
   self.obj623.postAction( cobj0.LHS.CREATE )

   self.obj621.out_connections_.append(self.obj623)
   self.obj623.in_connections_.append(self.obj621)
   self.obj621.graphObject_.pendingConnections.append((self.obj621.graphObject_.tag, self.obj623.graphObject_.tag, [85.0, 102.0, 117.0, 188.0, 230.0, 173.0], 2, True))
   self.obj623.out_connections_.append(self.obj622)
   self.obj622.in_connections_.append(self.obj623)
   self.obj623.graphObject_.pendingConnections.append((self.obj623.graphObject_.tag, self.obj622.graphObject_.tag, [344.0, 221.0, 343.0, 158.0, 230.0, 173.0], 2, True))

   cobj0.RHS = ASG_omacs(self)
   cobj0.RHS.merge(ASG_pns(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj627=Agent(self)
   self.obj627.preAction( cobj0.RHS.CREATE )
   self.obj627.isGraphObjectVisual = True

   if(hasattr(self.obj627, '_setHierarchicalLink')):
     self.obj627._setHierarchicalLink(False)

   # price
   self.obj627.price.setNone()

   # name
   self.obj627.name.setValue('')
   self.obj627.name.setNone()

   self.obj627.GGLabel.setValue(1)
   self.obj627.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(60.0,40.0,self.obj627)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj627.graphObject_ = new_obj
   self.obj6270= AttrCalc()
   self.obj6270.Copy=ATOM3Boolean()
   self.obj6270.Copy.setValue(('Copy from LHS', 1))
   self.obj6270.Copy.config = 0
   self.obj6270.Specify=ATOM3Constraint()
   self.obj6270.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj627.GGset2Any['price']= self.obj6270
   self.obj6271= AttrCalc()
   self.obj6271.Copy=ATOM3Boolean()
   self.obj6271.Copy.setValue(('Copy from LHS', 1))
   self.obj6271.Copy.config = 0
   self.obj6271.Specify=ATOM3Constraint()
   self.obj6271.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj627.GGset2Any['name']= self.obj6271

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj627)
   self.obj627.postAction( cobj0.RHS.CREATE )

   self.obj628=Role(self)
   self.obj628.preAction( cobj0.RHS.CREATE )
   self.obj628.isGraphObjectVisual = True

   if(hasattr(self.obj628, '_setHierarchicalLink')):
     self.obj628._setHierarchicalLink(False)

   # name
   self.obj628.name.setValue('')
   self.obj628.name.setNone()

   self.obj628.GGLabel.setValue(2)
   self.obj628.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(320.0,220.0,self.obj628)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj628.graphObject_ = new_obj
   self.obj6280= AttrCalc()
   self.obj6280.Copy=ATOM3Boolean()
   self.obj6280.Copy.setValue(('Copy from LHS', 1))
   self.obj6280.Copy.config = 0
   self.obj6280.Specify=ATOM3Constraint()
   self.obj6280.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj628.GGset2Any['name']= self.obj6280

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj628)
   self.obj628.postAction( cobj0.RHS.CREATE )

   self.obj629=CapableOf(self)
   self.obj629.preAction( cobj0.RHS.CREATE )
   self.obj629.isGraphObjectVisual = True

   if(hasattr(self.obj629, '_setHierarchicalLink')):
     self.obj629._setHierarchicalLink(False)

   # rate
   self.obj629.rate.setNone()

   self.obj629.GGLabel.setValue(3)
   self.obj629.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(230.0,173.0,self.obj629)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj629.graphObject_ = new_obj
   self.obj6290= AttrCalc()
   self.obj6290.Copy=ATOM3Boolean()
   self.obj6290.Copy.setValue(('Copy from LHS', 1))
   self.obj6290.Copy.config = 0
   self.obj6290.Specify=ATOM3Constraint()
   self.obj6290.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj629.GGset2Any['rate']= self.obj6290

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj629)
   self.obj629.postAction( cobj0.RHS.CREATE )

   self.obj630=operatingUnit(self)
   self.obj630.preAction( cobj0.RHS.CREATE )
   self.obj630.isGraphObjectVisual = True

   if(hasattr(self.obj630, '_setHierarchicalLink')):
     self.obj630._setHierarchicalLink(False)

   # OperCostProp
   self.obj630.OperCostProp.setValue(0.0)

   # name
   self.obj630.name.setValue('')
   self.obj630.name.setNone()

   # OperCostFix
   self.obj630.OperCostFix.setValue(0.0)

   self.obj630.GGLabel.setValue(5)
   self.obj630.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(60.0,220.0,self.obj630)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj630.graphObject_ = new_obj
   self.obj6300= AttrCalc()
   self.obj6300.Copy=ATOM3Boolean()
   self.obj6300.Copy.setValue(('Copy from LHS', 1))
   self.obj6300.Copy.config = 0
   self.obj6300.Specify=ATOM3Constraint()
   self.obj6300.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj630.GGset2Any['OperCostProp']= self.obj6300
   self.obj6301= AttrCalc()
   self.obj6301.Copy=ATOM3Boolean()
   self.obj6301.Copy.setValue(('Copy from LHS', 0))
   self.obj6301.Copy.config = 0
   self.obj6301.Specify=ATOM3Constraint()
   self.obj6301.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()+\' \'+self.getMatched(graphID, self.LHS.nodeWithLabel(2)).name.getValue()\n\n\n\n'))
   self.obj630.GGset2Any['name']= self.obj6301
   self.obj6302= AttrCalc()
   self.obj6302.Copy=ATOM3Boolean()
   self.obj6302.Copy.setValue(('Copy from LHS', 1))
   self.obj6302.Copy.config = 0
   self.obj6302.Specify=ATOM3Constraint()
   self.obj6302.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj630.GGset2Any['OperCostFix']= self.obj6302

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj630)
   self.obj630.postAction( cobj0.RHS.CREATE )

   self.obj631=GenericGraphEdge(self)
   self.obj631.preAction( cobj0.RHS.CREATE )
   self.obj631.isGraphObjectVisual = True

   if(hasattr(self.obj631, '_setHierarchicalLink')):
     self.obj631._setHierarchicalLink(False)

   self.obj631.GGLabel.setValue(6)
   self.obj631.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(103.5,161.5,self.obj631)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj631.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj631)
   self.obj631.postAction( cobj0.RHS.CREATE )

   self.obj627.out_connections_.append(self.obj629)
   self.obj629.in_connections_.append(self.obj627)
   self.obj627.graphObject_.pendingConnections.append((self.obj627.graphObject_.tag, self.obj629.graphObject_.tag, [97.0, 102.0, 230.0, 173.0], 2, 0))
   self.obj627.out_connections_.append(self.obj631)
   self.obj631.in_connections_.append(self.obj627)
   self.obj627.graphObject_.pendingConnections.append((self.obj627.graphObject_.tag, self.obj631.graphObject_.tag, [97.0, 102.0, 103.5, 161.5], 0, True))
   self.obj629.out_connections_.append(self.obj628)
   self.obj628.in_connections_.append(self.obj629)
   self.obj629.graphObject_.pendingConnections.append((self.obj629.graphObject_.tag, self.obj628.graphObject_.tag, [351.0, 220.0, 230.0, 173.0], 2, 0))
   self.obj631.out_connections_.append(self.obj630)
   self.obj630.in_connections_.append(self.obj631)
   self.obj631.graphObject_.pendingConnections.append((self.obj631.graphObject_.tag, self.obj630.graphObject_.tag, [110.0, 221.0, 103.5, 161.5], 0, True))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nnode2 = self.getMatched(graphID, self.LHS.nodeWithLabel(2))\nprint node.name.getValue()+\' \'+node2.name.getValue()\n# remplaceed by  "LinkAR2OpUnit"\nreturn not(  hasattr(node,node2.name.getValue()+\'7\') and hasattr(node2, node.name.getValue()+\'7\') )\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'node = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) )\n\nnode2 = self.getMatched ( graphID , self.LHS.nodeWithLabel(2) )\nsetattr( node ,node2.name.getValue()+\'7\' ,True )\nsetattr( node2 ,node.name.getValue()+\'7\' ,True )\n\n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('TransGoal2Mat', 20)
   cobj0.Order=ATOM3Integer(11)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

   from Capabilitie import *
   from rawMaterial import *
   from Goal import *
   from ASG_pns import *
   from operatingUnit import *
   from metarial import *
   from product import *
   from Agent import *
   from fromMaterial import *
   from CapableOf import *
   from intoProduct import *
   from Role import *
   from fromRaw import *
   from intoMaterial import *
   from ASG_omacs import *
   from require import *
   from achieve import *
   from posses import *
   from GenericGraphEdge import *
   from GenericGraphNode import *
   from ASG_GenericGraph import *

   cobj0.LHS = ASG_pns(self)
   cobj0.LHS.merge(ASG_omacs(self))

   self.obj637=Goal(self)
   self.obj637.preAction( cobj0.LHS.CREATE )
   self.obj637.isGraphObjectVisual = True

   if(hasattr(self.obj637, '_setHierarchicalLink')):
     self.obj637._setHierarchicalLink(False)

   # name
   self.obj637.name.setValue('')
   self.obj637.name.setNone()

   self.obj637.GGLabel.setValue(1)
   self.obj637.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(80.0,80.0,self.obj637)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj637.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj637)
   self.obj637.postAction( cobj0.LHS.CREATE )


   cobj0.RHS = ASG_pns(self)
   cobj0.RHS.merge(ASG_omacs(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj641=metarial(self)
   self.obj641.preAction( cobj0.RHS.CREATE )
   self.obj641.isGraphObjectVisual = True

   if(hasattr(self.obj641, '_setHierarchicalLink')):
     self.obj641._setHierarchicalLink(False)

   # MaxFlow
   self.obj641.MaxFlow.setValue(999999)

   # price
   self.obj641.price.setValue(0)

   # Name
   self.obj641.Name.setValue('')
   self.obj641.Name.setNone()

   # ReqFlow
   self.obj641.ReqFlow.setValue(0)

   self.obj641.GGLabel.setValue(2)
   self.obj641.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(300.0,60.0,self.obj641)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj641.graphObject_ = new_obj
   self.obj6410= AttrCalc()
   self.obj6410.Copy=ATOM3Boolean()
   self.obj6410.Copy.setValue(('Copy from LHS', 1))
   self.obj6410.Copy.config = 0
   self.obj6410.Specify=ATOM3Constraint()
   self.obj6410.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj641.GGset2Any['MaxFlow']= self.obj6410
   self.obj6411= AttrCalc()
   self.obj6411.Copy=ATOM3Boolean()
   self.obj6411.Copy.setValue(('Copy from LHS', 0))
   self.obj6411.Copy.config = 0
   self.obj6411.Specify=ATOM3Constraint()
   self.obj6411.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()\n'))
   self.obj641.GGset2Any['Name']= self.obj6411
   self.obj6412= AttrCalc()
   self.obj6412.Copy=ATOM3Boolean()
   self.obj6412.Copy.setValue(('Copy from LHS', 1))
   self.obj6412.Copy.config = 0
   self.obj6412.Specify=ATOM3Constraint()
   self.obj6412.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj641.GGset2Any['ReqFlow']= self.obj6412

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj641)
   self.obj641.postAction( cobj0.RHS.CREATE )

   self.obj642=Goal(self)
   self.obj642.preAction( cobj0.RHS.CREATE )
   self.obj642.isGraphObjectVisual = True

   if(hasattr(self.obj642, '_setHierarchicalLink')):
     self.obj642._setHierarchicalLink(False)

   # name
   self.obj642.name.setValue('')
   self.obj642.name.setNone()

   self.obj642.GGLabel.setValue(1)
   self.obj642.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(80.0,80.0,self.obj642)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj642.graphObject_ = new_obj
   self.obj6420= AttrCalc()
   self.obj6420.Copy=ATOM3Boolean()
   self.obj6420.Copy.setValue(('Copy from LHS', 1))
   self.obj6420.Copy.config = 0
   self.obj6420.Specify=ATOM3Constraint()
   self.obj6420.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj642.GGset2Any['name']= self.obj6420

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj642)
   self.obj642.postAction( cobj0.RHS.CREATE )

   self.obj643=GenericGraphEdge(self)
   self.obj643.preAction( cobj0.RHS.CREATE )
   self.obj643.isGraphObjectVisual = True

   if(hasattr(self.obj643, '_setHierarchicalLink')):
     self.obj643._setHierarchicalLink(False)

   self.obj643.GGLabel.setValue(4)
   self.obj643.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(209.5,91.5,self.obj643)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj643.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj643)
   self.obj643.postAction( cobj0.RHS.CREATE )

   self.obj642.out_connections_.append(self.obj643)
   self.obj643.in_connections_.append(self.obj642)
   self.obj642.graphObject_.pendingConnections.append((self.obj642.graphObject_.tag, self.obj643.graphObject_.tag, [113.0, 81.0, 209.5, 91.5], 0, True))
   self.obj643.out_connections_.append(self.obj641)
   self.obj641.in_connections_.append(self.obj643)
   self.obj643.graphObject_.pendingConnections.append((self.obj643.graphObject_.tag, self.obj641.graphObject_.tag, [306.0, 102.0, 209.5, 91.5], 0, True))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nreturn not hasattr(node, "Goal2Mat")\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'node = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) )\nnode.Goal2Mat = True\n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('CreatLinkRaw2AR', 20)
   cobj0.Order=ATOM3Integer(12)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

   from Capabilitie import *
   from rawMaterial import *
   from GenericGraphEdge import *
   from Goal import *
   from ASG_pns import *
   from operatingUnit import *
   from metarial import *
   from GenericGraphNode import *
   from product import *
   from Agent import *
   from fromMaterial import *
   from CapableOf import *
   from intoProduct import *
   from Role import *
   from fromRaw import *
   from intoMaterial import *
   from ASG_GenericGraph import *
   from ASG_omacs import *
   from require import *
   from achieve import *
   from posses import *

   cobj0.LHS = ASG_pns(self)
   cobj0.LHS.merge(ASG_omacs(self))
   cobj0.LHS.merge(ASG_GenericGraph(self))

   self.obj650=rawMaterial(self)
   self.obj650.preAction( cobj0.LHS.CREATE )
   self.obj650.isGraphObjectVisual = True

   if(hasattr(self.obj650, '_setHierarchicalLink')):
     self.obj650._setHierarchicalLink(False)

   # MaxFlow
   self.obj650.MaxFlow.setValue(999999)

   # price
   self.obj650.price.setValue(0)

   # Name
   self.obj650.Name.setValue('')
   self.obj650.Name.setNone()

   # ReqFlow
   self.obj650.ReqFlow.setValue(0)

   self.obj650.GGLabel.setValue(3)
   self.obj650.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(220.0,20.0,self.obj650)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj650.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj650)
   self.obj650.postAction( cobj0.LHS.CREATE )

   self.obj651=operatingUnit(self)
   self.obj651.preAction( cobj0.LHS.CREATE )
   self.obj651.isGraphObjectVisual = True

   if(hasattr(self.obj651, '_setHierarchicalLink')):
     self.obj651._setHierarchicalLink(False)

   # OperCostProp
   self.obj651.OperCostProp.setValue(0.0)

   # name
   self.obj651.name.setValue('')
   self.obj651.name.setNone()

   # OperCostFix
   self.obj651.OperCostFix.setValue(0.0)

   self.obj651.GGLabel.setValue(2)
   self.obj651.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(260.0,160.0,self.obj651)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj651.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj651)
   self.obj651.postAction( cobj0.LHS.CREATE )

   self.obj652=Agent(self)
   self.obj652.preAction( cobj0.LHS.CREATE )
   self.obj652.isGraphObjectVisual = True

   if(hasattr(self.obj652, '_setHierarchicalLink')):
     self.obj652._setHierarchicalLink(False)

   # price
   self.obj652.price.setNone()

   # name
   self.obj652.name.setValue('')
   self.obj652.name.setNone()

   self.obj652.GGLabel.setValue(1)
   self.obj652.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(80.0,120.0,self.obj652)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj652.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj652)
   self.obj652.postAction( cobj0.LHS.CREATE )

   self.obj653=GenericGraphEdge(self)
   self.obj653.preAction( cobj0.LHS.CREATE )
   self.obj653.isGraphObjectVisual = True

   if(hasattr(self.obj653, '_setHierarchicalLink')):
     self.obj653._setHierarchicalLink(False)

   self.obj653.GGLabel.setValue(4)
   self.obj653.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(181.75,114.0,self.obj653)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj653.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj653)
   self.obj653.postAction( cobj0.LHS.CREATE )

   self.obj654=GenericGraphEdge(self)
   self.obj654.preAction( cobj0.LHS.CREATE )
   self.obj654.isGraphObjectVisual = True

   if(hasattr(self.obj654, '_setHierarchicalLink')):
     self.obj654._setHierarchicalLink(False)

   self.obj654.GGLabel.setValue(5)
   self.obj654.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(229.25,150.25,self.obj654)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj654.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj654)
   self.obj654.postAction( cobj0.LHS.CREATE )

   self.obj652.out_connections_.append(self.obj653)
   self.obj653.in_connections_.append(self.obj652)
   self.obj652.graphObject_.pendingConnections.append((self.obj652.graphObject_.tag, self.obj653.graphObject_.tag, [105.0, 182.0, 147.0, 140.5, 181.75, 114.0], 2, True))
   self.obj652.out_connections_.append(self.obj654)
   self.obj654.in_connections_.append(self.obj652)
   self.obj652.graphObject_.pendingConnections.append((self.obj652.graphObject_.tag, self.obj654.graphObject_.tag, [105.0, 182.0, 185.5, 153.0, 229.25, 150.25], 2, True))
   self.obj653.out_connections_.append(self.obj650)
   self.obj650.in_connections_.append(self.obj653)
   self.obj653.graphObject_.pendingConnections.append((self.obj653.graphObject_.tag, self.obj650.graphObject_.tag, [244.0, 76.0, 216.5, 87.5, 181.75, 114.0], 2, True))
   self.obj654.out_connections_.append(self.obj651)
   self.obj651.in_connections_.append(self.obj654)
   self.obj654.graphObject_.pendingConnections.append((self.obj654.graphObject_.tag, self.obj651.graphObject_.tag, [280.0, 171.0, 273.0, 147.5, 229.25, 150.25], 2, True))

   cobj0.RHS = ASG_pns(self)
   cobj0.RHS.merge(ASG_omacs(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj658=rawMaterial(self)
   self.obj658.preAction( cobj0.RHS.CREATE )
   self.obj658.isGraphObjectVisual = True

   if(hasattr(self.obj658, '_setHierarchicalLink')):
     self.obj658._setHierarchicalLink(False)

   # MaxFlow
   self.obj658.MaxFlow.setValue(999999)

   # price
   self.obj658.price.setValue(0)

   # Name
   self.obj658.Name.setValue('')
   self.obj658.Name.setNone()

   # ReqFlow
   self.obj658.ReqFlow.setValue(0)

   self.obj658.GGLabel.setValue(3)
   self.obj658.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(220.0,20.0,self.obj658)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj658.graphObject_ = new_obj
   self.obj6580= AttrCalc()
   self.obj6580.Copy=ATOM3Boolean()
   self.obj6580.Copy.setValue(('Copy from LHS', 1))
   self.obj6580.Copy.config = 0
   self.obj6580.Specify=ATOM3Constraint()
   self.obj6580.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj658.GGset2Any['MaxFlow']= self.obj6580
   self.obj6581= AttrCalc()
   self.obj6581.Copy=ATOM3Boolean()
   self.obj6581.Copy.setValue(('Copy from LHS', 1))
   self.obj6581.Copy.config = 0
   self.obj6581.Specify=ATOM3Constraint()
   self.obj6581.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj658.GGset2Any['Name']= self.obj6581
   self.obj6582= AttrCalc()
   self.obj6582.Copy=ATOM3Boolean()
   self.obj6582.Copy.setValue(('Copy from LHS', 1))
   self.obj6582.Copy.config = 0
   self.obj6582.Specify=ATOM3Constraint()
   self.obj6582.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj658.GGset2Any['ReqFlow']= self.obj6582

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj658)
   self.obj658.postAction( cobj0.RHS.CREATE )

   self.obj659=operatingUnit(self)
   self.obj659.preAction( cobj0.RHS.CREATE )
   self.obj659.isGraphObjectVisual = True

   if(hasattr(self.obj659, '_setHierarchicalLink')):
     self.obj659._setHierarchicalLink(False)

   # OperCostProp
   self.obj659.OperCostProp.setValue(0.0)

   # name
   self.obj659.name.setValue('')
   self.obj659.name.setNone()

   # OperCostFix
   self.obj659.OperCostFix.setValue(0.0)

   self.obj659.GGLabel.setValue(2)
   self.obj659.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(260.0,160.0,self.obj659)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj659.graphObject_ = new_obj
   self.obj6590= AttrCalc()
   self.obj6590.Copy=ATOM3Boolean()
   self.obj6590.Copy.setValue(('Copy from LHS', 1))
   self.obj6590.Copy.config = 0
   self.obj6590.Specify=ATOM3Constraint()
   self.obj6590.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj659.GGset2Any['OperCostProp']= self.obj6590
   self.obj6591= AttrCalc()
   self.obj6591.Copy=ATOM3Boolean()
   self.obj6591.Copy.setValue(('Copy from LHS', 1))
   self.obj6591.Copy.config = 0
   self.obj6591.Specify=ATOM3Constraint()
   self.obj6591.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj659.GGset2Any['name']= self.obj6591
   self.obj6592= AttrCalc()
   self.obj6592.Copy=ATOM3Boolean()
   self.obj6592.Copy.setValue(('Copy from LHS', 1))
   self.obj6592.Copy.config = 0
   self.obj6592.Specify=ATOM3Constraint()
   self.obj6592.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj659.GGset2Any['OperCostFix']= self.obj6592

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj659)
   self.obj659.postAction( cobj0.RHS.CREATE )

   self.obj660=fromRaw(self)
   self.obj660.preAction( cobj0.RHS.CREATE )
   self.obj660.isGraphObjectVisual = True

   if(hasattr(self.obj660, '_setHierarchicalLink')):
     self.obj660._setHierarchicalLink(False)

   # rate
   self.obj660.rate.setValue(1.0)

   self.obj660.GGLabel.setValue(7)
   self.obj660.graphClass_= graph_fromRaw
   if self.genGraphics:
      new_obj = graph_fromRaw(262.0,115.5,self.obj660)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj660.graphObject_ = new_obj
   self.obj6600= AttrCalc()
   self.obj6600.Copy=ATOM3Boolean()
   self.obj6600.Copy.setValue(('Copy from LHS', 0))
   self.obj6600.Copy.config = 0
   self.obj6600.Specify=ATOM3Constraint()
   self.obj6600.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj660.GGset2Any['rate']= self.obj6600

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj660)
   self.obj660.postAction( cobj0.RHS.CREATE )

   self.obj661=Agent(self)
   self.obj661.preAction( cobj0.RHS.CREATE )
   self.obj661.isGraphObjectVisual = True

   if(hasattr(self.obj661, '_setHierarchicalLink')):
     self.obj661._setHierarchicalLink(False)

   # price
   self.obj661.price.setNone()

   # name
   self.obj661.name.setValue('')
   self.obj661.name.setNone()

   self.obj661.GGLabel.setValue(1)
   self.obj661.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(80.0,120.0,self.obj661)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj661.graphObject_ = new_obj
   self.obj6610= AttrCalc()
   self.obj6610.Copy=ATOM3Boolean()
   self.obj6610.Copy.setValue(('Copy from LHS', 1))
   self.obj6610.Copy.config = 0
   self.obj6610.Specify=ATOM3Constraint()
   self.obj6610.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj661.GGset2Any['price']= self.obj6610
   self.obj6611= AttrCalc()
   self.obj6611.Copy=ATOM3Boolean()
   self.obj6611.Copy.setValue(('Copy from LHS', 1))
   self.obj6611.Copy.config = 0
   self.obj6611.Specify=ATOM3Constraint()
   self.obj6611.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj661.GGset2Any['name']= self.obj6611

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj661)
   self.obj661.postAction( cobj0.RHS.CREATE )

   self.obj662=GenericGraphEdge(self)
   self.obj662.preAction( cobj0.RHS.CREATE )
   self.obj662.isGraphObjectVisual = True

   if(hasattr(self.obj662, '_setHierarchicalLink')):
     self.obj662._setHierarchicalLink(False)

   self.obj662.GGLabel.setValue(4)
   self.obj662.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(181.75,114.0,self.obj662)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj662.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj662)
   self.obj662.postAction( cobj0.RHS.CREATE )

   self.obj663=GenericGraphEdge(self)
   self.obj663.preAction( cobj0.RHS.CREATE )
   self.obj663.isGraphObjectVisual = True

   if(hasattr(self.obj663, '_setHierarchicalLink')):
     self.obj663._setHierarchicalLink(False)

   self.obj663.GGLabel.setValue(5)
   self.obj663.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(229.25,150.25,self.obj663)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj663.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj663)
   self.obj663.postAction( cobj0.RHS.CREATE )

   self.obj658.out_connections_.append(self.obj660)
   self.obj660.in_connections_.append(self.obj658)
   self.obj658.graphObject_.pendingConnections.append((self.obj658.graphObject_.tag, self.obj660.graphObject_.tag, [244.0, 70.0, 262.0, 115.5], 0, True))
   self.obj660.out_connections_.append(self.obj659)
   self.obj659.in_connections_.append(self.obj660)
   self.obj660.graphObject_.pendingConnections.append((self.obj660.graphObject_.tag, self.obj659.graphObject_.tag, [280.0, 161.0, 262.0, 115.5], 0, True))
   self.obj661.out_connections_.append(self.obj662)
   self.obj662.in_connections_.append(self.obj661)
   self.obj661.graphObject_.pendingConnections.append((self.obj661.graphObject_.tag, self.obj662.graphObject_.tag, [117.0, 182.0, 181.75, 114.0], 2, 0))
   self.obj661.out_connections_.append(self.obj663)
   self.obj663.in_connections_.append(self.obj661)
   self.obj661.graphObject_.pendingConnections.append((self.obj661.graphObject_.tag, self.obj663.graphObject_.tag, [117.0, 182.0, 229.25, 150.25], 2, 0))
   self.obj662.out_connections_.append(self.obj658)
   self.obj658.in_connections_.append(self.obj662)
   self.obj662.graphObject_.pendingConnections.append((self.obj662.graphObject_.tag, self.obj658.graphObject_.tag, [244.0, 70.0, 181.75, 114.0], 2, 0))
   self.obj663.out_connections_.append(self.obj659)
   self.obj659.in_connections_.append(self.obj663)
   self.obj663.graphObject_.pendingConnections.append((self.obj663.graphObject_.tag, self.obj659.graphObject_.tag, [280.0, 161.0, 229.25, 150.25], 2, 0))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'node = self.getMatched(graphID, self.LHS.nodeWithLabel(2))\nreturn not hasattr(node, "LinkRaw2AR")\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'node = self.getMatched ( graphID , self.LHS.nodeWithLabel(2) )\nnode.LinkRaw2AR = True\n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('CreateFinalStat', 20)
   cobj0.Order=ATOM3Integer(13)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

   from rawMaterial import *
   from ASG_pns import *
   from operatingUnit import *
   from metarial import *
   from product import *
   from fromMaterial import *
   from intoProduct import *
   from fromRaw import *
   from intoMaterial import *

   cobj0.LHS = ASG_pns(self)


   cobj0.RHS = ASG_pns(self)

   self.obj669=product(self)
   self.obj669.preAction( cobj0.RHS.CREATE )
   self.obj669.isGraphObjectVisual = True

   if(hasattr(self.obj669, '_setHierarchicalLink')):
     self.obj669._setHierarchicalLink(False)

   # MaxFlow
   self.obj669.MaxFlow.setValue(999999)

   # price
   self.obj669.price.setValue(0)

   # Name
   self.obj669.Name.setValue('OAF')

   # ReqFlow
   self.obj669.ReqFlow.setValue(0)

   self.obj669.GGLabel.setValue(1)
   self.obj669.graphClass_= graph_product
   if self.genGraphics:
      new_obj = graph_product(100.0,80.0,self.obj669)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj669.graphObject_ = new_obj
   self.obj6690= AttrCalc()
   self.obj6690.Copy=ATOM3Boolean()
   self.obj6690.Copy.setValue(('Copy from LHS', 1))
   self.obj6690.Copy.config = 0
   self.obj6690.Specify=ATOM3Constraint()
   self.obj6690.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj669.GGset2Any['MaxFlow']= self.obj6690
   self.obj6691= AttrCalc()
   self.obj6691.Copy=ATOM3Boolean()
   self.obj6691.Copy.setValue(('Copy from LHS', 0))
   self.obj6691.Copy.config = 0
   self.obj6691.Specify=ATOM3Constraint()
   self.obj6691.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj669.GGset2Any['Name']= self.obj6691
   self.obj6692= AttrCalc()
   self.obj6692.Copy=ATOM3Boolean()
   self.obj6692.Copy.setValue(('Copy from LHS', 1))
   self.obj6692.Copy.config = 0
   self.obj6692.Specify=ATOM3Constraint()
   self.obj6692.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj669.GGset2Any['ReqFlow']= self.obj6692

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj669)
   self.obj669.postAction( cobj0.RHS.CREATE )


   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.graphRewritingSystem.finalStat == 0\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'self.graphRewritingSystem.finalStat = 1 \n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('CreateLinkMatr2OAF', 20)
   cobj0.Order=ATOM3Integer(15)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

   from Capabilitie import *
   from rawMaterial import *
   from GenericGraphEdge import *
   from Goal import *
   from ASG_pns import *
   from operatingUnit import *
   from metarial import *
   from GenericGraphNode import *
   from product import *
   from Agent import *
   from fromMaterial import *
   from CapableOf import *
   from intoProduct import *
   from Role import *
   from fromRaw import *
   from intoMaterial import *
   from ASG_GenericGraph import *
   from ASG_omacs import *
   from require import *
   from achieve import *
   from posses import *

   cobj0.LHS = ASG_pns(self)
   cobj0.LHS.merge(ASG_omacs(self))
   cobj0.LHS.merge(ASG_GenericGraph(self))

   self.obj676=product(self)
   self.obj676.preAction( cobj0.LHS.CREATE )
   self.obj676.isGraphObjectVisual = True

   if(hasattr(self.obj676, '_setHierarchicalLink')):
     self.obj676._setHierarchicalLink(False)

   # MaxFlow
   self.obj676.MaxFlow.setNone()

   # price
   self.obj676.price.setValue(0)

   # Name
   self.obj676.Name.setValue('')
   self.obj676.Name.setNone()

   # ReqFlow
   self.obj676.ReqFlow.setNone()

   self.obj676.GGLabel.setValue(5)
   self.obj676.graphClass_= graph_product
   if self.genGraphics:
      new_obj = graph_product(280.0,220.0,self.obj676)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj676.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj676)
   self.obj676.postAction( cobj0.LHS.CREATE )

   self.obj677=metarial(self)
   self.obj677.preAction( cobj0.LHS.CREATE )
   self.obj677.isGraphObjectVisual = True

   if(hasattr(self.obj677, '_setHierarchicalLink')):
     self.obj677._setHierarchicalLink(False)

   # MaxFlow
   self.obj677.MaxFlow.setNone()

   # price
   self.obj677.price.setValue(0)

   # Name
   self.obj677.Name.setValue('')
   self.obj677.Name.setNone()

   # ReqFlow
   self.obj677.ReqFlow.setNone()

   self.obj677.GGLabel.setValue(3)
   self.obj677.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(320.0,40.0,self.obj677)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj677.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj677)
   self.obj677.postAction( cobj0.LHS.CREATE )

   self.obj678=Goal(self)
   self.obj678.preAction( cobj0.LHS.CREATE )
   self.obj678.isGraphObjectVisual = True

   if(hasattr(self.obj678, '_setHierarchicalLink')):
     self.obj678._setHierarchicalLink(False)

   # name
   self.obj678.name.setValue('')
   self.obj678.name.setNone()

   self.obj678.GGLabel.setValue(2)
   self.obj678.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(180.0,60.0,self.obj678)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj678.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj678)
   self.obj678.postAction( cobj0.LHS.CREATE )

   self.obj679=GenericGraphEdge(self)
   self.obj679.preAction( cobj0.LHS.CREATE )
   self.obj679.isGraphObjectVisual = True

   if(hasattr(self.obj679, '_setHierarchicalLink')):
     self.obj679._setHierarchicalLink(False)

   self.obj679.GGLabel.setValue(4)
   self.obj679.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(264.5,71.5,self.obj679)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj679.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj679)
   self.obj679.postAction( cobj0.LHS.CREATE )

   self.obj678.out_connections_.append(self.obj679)
   self.obj679.in_connections_.append(self.obj678)
   self.obj678.graphObject_.pendingConnections.append((self.obj678.graphObject_.tag, self.obj679.graphObject_.tag, [203.0, 61.0, 264.5, 71.5], 0, True))
   self.obj679.out_connections_.append(self.obj677)
   self.obj677.in_connections_.append(self.obj679)
   self.obj679.graphObject_.pendingConnections.append((self.obj679.graphObject_.tag, self.obj677.graphObject_.tag, [326.0, 82.0, 264.5, 71.5], 0, True))

   cobj0.RHS = ASG_pns(self)
   cobj0.RHS.merge(ASG_omacs(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj683=product(self)
   self.obj683.preAction( cobj0.RHS.CREATE )
   self.obj683.isGraphObjectVisual = True

   if(hasattr(self.obj683, '_setHierarchicalLink')):
     self.obj683._setHierarchicalLink(False)

   # MaxFlow
   self.obj683.MaxFlow.setNone()

   # price
   self.obj683.price.setValue(0)

   # Name
   self.obj683.Name.setValue('')
   self.obj683.Name.setNone()

   # ReqFlow
   self.obj683.ReqFlow.setNone()

   self.obj683.GGLabel.setValue(5)
   self.obj683.graphClass_= graph_product
   if self.genGraphics:
      new_obj = graph_product(280.0,220.0,self.obj683)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj683.graphObject_ = new_obj
   self.obj6830= AttrCalc()
   self.obj6830.Copy=ATOM3Boolean()
   self.obj6830.Copy.setValue(('Copy from LHS', 1))
   self.obj6830.Copy.config = 0
   self.obj6830.Specify=ATOM3Constraint()
   self.obj6830.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj683.GGset2Any['MaxFlow']= self.obj6830
   self.obj6831= AttrCalc()
   self.obj6831.Copy=ATOM3Boolean()
   self.obj6831.Copy.setValue(('Copy from LHS', 1))
   self.obj6831.Copy.config = 0
   self.obj6831.Specify=ATOM3Constraint()
   self.obj6831.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj683.GGset2Any['Name']= self.obj6831
   self.obj6832= AttrCalc()
   self.obj6832.Copy=ATOM3Boolean()
   self.obj6832.Copy.setValue(('Copy from LHS', 1))
   self.obj6832.Copy.config = 0
   self.obj6832.Specify=ATOM3Constraint()
   self.obj6832.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj683.GGset2Any['ReqFlow']= self.obj6832

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj683)
   self.obj683.postAction( cobj0.RHS.CREATE )

   self.obj684=metarial(self)
   self.obj684.preAction( cobj0.RHS.CREATE )
   self.obj684.isGraphObjectVisual = True

   if(hasattr(self.obj684, '_setHierarchicalLink')):
     self.obj684._setHierarchicalLink(False)

   # MaxFlow
   self.obj684.MaxFlow.setNone()

   # price
   self.obj684.price.setValue(0)

   # Name
   self.obj684.Name.setValue('')
   self.obj684.Name.setNone()

   # ReqFlow
   self.obj684.ReqFlow.setNone()

   self.obj684.GGLabel.setValue(3)
   self.obj684.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(320.0,40.0,self.obj684)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj684.graphObject_ = new_obj
   self.obj6840= AttrCalc()
   self.obj6840.Copy=ATOM3Boolean()
   self.obj6840.Copy.setValue(('Copy from LHS', 1))
   self.obj6840.Copy.config = 0
   self.obj6840.Specify=ATOM3Constraint()
   self.obj6840.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj684.GGset2Any['MaxFlow']= self.obj6840
   self.obj6841= AttrCalc()
   self.obj6841.Copy=ATOM3Boolean()
   self.obj6841.Copy.setValue(('Copy from LHS', 1))
   self.obj6841.Copy.config = 0
   self.obj6841.Specify=ATOM3Constraint()
   self.obj6841.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj684.GGset2Any['Name']= self.obj6841
   self.obj6842= AttrCalc()
   self.obj6842.Copy=ATOM3Boolean()
   self.obj6842.Copy.setValue(('Copy from LHS', 1))
   self.obj6842.Copy.config = 0
   self.obj6842.Specify=ATOM3Constraint()
   self.obj6842.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj684.GGset2Any['ReqFlow']= self.obj6842

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj684)
   self.obj684.postAction( cobj0.RHS.CREATE )

   self.obj685=operatingUnit(self)
   self.obj685.preAction( cobj0.RHS.CREATE )
   self.obj685.isGraphObjectVisual = True

   if(hasattr(self.obj685, '_setHierarchicalLink')):
     self.obj685._setHierarchicalLink(False)

   # OperCostProp
   self.obj685.OperCostProp.setValue(1.0)

   # name
   self.obj685.name.setValue('')
   self.obj685.name.setNone()

   # OperCostFix
   self.obj685.OperCostFix.setValue(2.0)

   self.obj685.GGLabel.setValue(7)
   self.obj685.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(320.0,140.0,self.obj685)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj685.graphObject_ = new_obj
   self.obj6850= AttrCalc()
   self.obj6850.Copy=ATOM3Boolean()
   self.obj6850.Copy.setValue(('Copy from LHS', 0))
   self.obj6850.Copy.config = 0
   self.obj6850.Specify=ATOM3Constraint()
   self.obj6850.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj685.GGset2Any['OperCostProp']= self.obj6850
   self.obj6851= AttrCalc()
   self.obj6851.Copy=ATOM3Boolean()
   self.obj6851.Copy.setValue(('Copy from LHS', 0))
   self.obj6851.Copy.config = 0
   self.obj6851.Specify=ATOM3Constraint()
   self.obj6851.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(2)).name.getValue()+\' OAF\'\n'))
   self.obj685.GGset2Any['name']= self.obj6851
   self.obj6852= AttrCalc()
   self.obj6852.Copy=ATOM3Boolean()
   self.obj6852.Copy.setValue(('Copy from LHS', 0))
   self.obj6852.Copy.config = 0
   self.obj6852.Specify=ATOM3Constraint()
   self.obj6852.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj685.GGset2Any['OperCostFix']= self.obj6852

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj685)
   self.obj685.postAction( cobj0.RHS.CREATE )

   self.obj686=intoProduct(self)
   self.obj686.preAction( cobj0.RHS.CREATE )
   self.obj686.isGraphObjectVisual = True

   if(hasattr(self.obj686, '_setHierarchicalLink')):
     self.obj686._setHierarchicalLink(False)

   # rate
   self.obj686.rate.setValue(1.0)

   self.obj686.GGLabel.setValue(9)
   self.obj686.graphClass_= graph_intoProduct
   if self.genGraphics:
      new_obj = graph_intoProduct(322.0,179.0,self.obj686)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj686.graphObject_ = new_obj
   self.obj6860= AttrCalc()
   self.obj6860.Copy=ATOM3Boolean()
   self.obj6860.Copy.setValue(('Copy from LHS', 0))
   self.obj6860.Copy.config = 0
   self.obj6860.Specify=ATOM3Constraint()
   self.obj6860.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj686.GGset2Any['rate']= self.obj6860

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj686)
   self.obj686.postAction( cobj0.RHS.CREATE )

   self.obj687=fromMaterial(self)
   self.obj687.preAction( cobj0.RHS.CREATE )
   self.obj687.isGraphObjectVisual = True

   if(hasattr(self.obj687, '_setHierarchicalLink')):
     self.obj687._setHierarchicalLink(False)

   # rate
   self.obj687.rate.setValue(1.0)

   self.obj687.GGLabel.setValue(8)
   self.obj687.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(342.0,110.0,self.obj687)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj687.graphObject_ = new_obj
   self.obj6870= AttrCalc()
   self.obj6870.Copy=ATOM3Boolean()
   self.obj6870.Copy.setValue(('Copy from LHS', 0))
   self.obj6870.Copy.config = 0
   self.obj6870.Specify=ATOM3Constraint()
   self.obj6870.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj687.GGset2Any['rate']= self.obj6870

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj687)
   self.obj687.postAction( cobj0.RHS.CREATE )

   self.obj688=Goal(self)
   self.obj688.preAction( cobj0.RHS.CREATE )
   self.obj688.isGraphObjectVisual = True

   if(hasattr(self.obj688, '_setHierarchicalLink')):
     self.obj688._setHierarchicalLink(False)

   # name
   self.obj688.name.setValue('')
   self.obj688.name.setNone()

   self.obj688.GGLabel.setValue(2)
   self.obj688.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(180.0,60.0,self.obj688)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj688.graphObject_ = new_obj
   self.obj6880= AttrCalc()
   self.obj6880.Copy=ATOM3Boolean()
   self.obj6880.Copy.setValue(('Copy from LHS', 1))
   self.obj6880.Copy.config = 0
   self.obj6880.Specify=ATOM3Constraint()
   self.obj6880.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj688.GGset2Any['name']= self.obj6880

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj688)
   self.obj688.postAction( cobj0.RHS.CREATE )

   self.obj689=GenericGraphEdge(self)
   self.obj689.preAction( cobj0.RHS.CREATE )
   self.obj689.isGraphObjectVisual = True

   if(hasattr(self.obj689, '_setHierarchicalLink')):
     self.obj689._setHierarchicalLink(False)

   self.obj689.GGLabel.setValue(4)
   self.obj689.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(264.5,71.5,self.obj689)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj689.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj689)
   self.obj689.postAction( cobj0.RHS.CREATE )

   self.obj684.out_connections_.append(self.obj687)
   self.obj687.in_connections_.append(self.obj684)
   self.obj684.graphObject_.pendingConnections.append((self.obj684.graphObject_.tag, self.obj687.graphObject_.tag, [244.0, 89.0, 342.0, 110.0], 0, True))
   self.obj685.out_connections_.append(self.obj686)
   self.obj686.in_connections_.append(self.obj685)
   self.obj685.graphObject_.pendingConnections.append((self.obj685.graphObject_.tag, self.obj686.graphObject_.tag, [339.0, 158.0, 322.0, 179.0], 0, True))
   self.obj686.out_connections_.append(self.obj683)
   self.obj683.in_connections_.append(self.obj686)
   self.obj686.graphObject_.pendingConnections.append((self.obj686.graphObject_.tag, self.obj683.graphObject_.tag, [305.0, 220.0, 322.0, 179.0], 0, True))
   self.obj687.out_connections_.append(self.obj685)
   self.obj685.in_connections_.append(self.obj687)
   self.obj687.graphObject_.pendingConnections.append((self.obj687.graphObject_.tag, self.obj685.graphObject_.tag, [340.0, 151.0, 342.0, 110.0], 0, True))
   self.obj688.out_connections_.append(self.obj689)
   self.obj689.in_connections_.append(self.obj688)
   self.obj688.graphObject_.pendingConnections.append((self.obj688.graphObject_.tag, self.obj689.graphObject_.tag, [93.0, 61.0, 264.5, 71.5], 2, 0))
   self.obj689.out_connections_.append(self.obj684)
   self.obj684.in_connections_.append(self.obj689)
   self.obj689.graphObject_.pendingConnections.append((self.obj689.graphObject_.tag, self.obj684.graphObject_.tag, [226.0, 82.0, 264.5, 71.5], 2, 0))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'node = self.getMatched(graphID, self.LHS.nodeWithLabel(3))\nreturn not hasattr(node, "link2oaf")\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'node = self.getMatched(graphID, self.LHS.nodeWithLabel(3))\nnode.link2oaf = True\n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('CreateMat_ARG', 20)
   cobj0.Order=ATOM3Integer(17)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

   from Capabilitie import *
   from rawMaterial import *
   from Goal import *
   from ASG_pns import *
   from operatingUnit import *
   from metarial import *
   from product import *
   from Agent import *
   from fromMaterial import *
   from CapableOf import *
   from intoProduct import *
   from Role import *
   from fromRaw import *
   from intoMaterial import *
   from ASG_omacs import *
   from require import *
   from achieve import *
   from posses import *
   from GenericGraphEdge import *
   from GenericGraphNode import *
   from ASG_GenericGraph import *

   cobj0.LHS = ASG_pns(self)
   cobj0.LHS.merge(ASG_omacs(self))

   self.obj695=CapableOf(self)
   self.obj695.preAction( cobj0.LHS.CREATE )
   self.obj695.isGraphObjectVisual = True

   if(hasattr(self.obj695, '_setHierarchicalLink')):
     self.obj695._setHierarchicalLink(False)

   # rate
   self.obj695.rate.setNone()

   self.obj695.GGLabel.setValue(4)
   self.obj695.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(250.75,110.75,self.obj695)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj695.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj695)
   self.obj695.postAction( cobj0.LHS.CREATE )

   self.obj696=Goal(self)
   self.obj696.preAction( cobj0.LHS.CREATE )
   self.obj696.isGraphObjectVisual = True

   if(hasattr(self.obj696, '_setHierarchicalLink')):
     self.obj696._setHierarchicalLink(False)

   # name
   self.obj696.name.setValue('')
   self.obj696.name.setNone()

   self.obj696.GGLabel.setValue(3)
   self.obj696.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(100.0,240.0,self.obj696)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj696.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj696)
   self.obj696.postAction( cobj0.LHS.CREATE )

   self.obj697=Agent(self)
   self.obj697.preAction( cobj0.LHS.CREATE )
   self.obj697.isGraphObjectVisual = True

   if(hasattr(self.obj697, '_setHierarchicalLink')):
     self.obj697._setHierarchicalLink(False)

   # price
   self.obj697.price.setNone()

   # name
   self.obj697.name.setValue('')
   self.obj697.name.setNone()

   self.obj697.GGLabel.setValue(1)
   self.obj697.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(80.0,40.0,self.obj697)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj697.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj697)
   self.obj697.postAction( cobj0.LHS.CREATE )

   self.obj698=Role(self)
   self.obj698.preAction( cobj0.LHS.CREATE )
   self.obj698.isGraphObjectVisual = True

   if(hasattr(self.obj698, '_setHierarchicalLink')):
     self.obj698._setHierarchicalLink(False)

   # name
   self.obj698.name.setValue('')
   self.obj698.name.setNone()

   self.obj698.GGLabel.setValue(2)
   self.obj698.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(280.0,140.0,self.obj698)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj698.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj698)
   self.obj698.postAction( cobj0.LHS.CREATE )

   self.obj699=achieve(self)
   self.obj699.preAction( cobj0.LHS.CREATE )
   self.obj699.isGraphObjectVisual = True

   if(hasattr(self.obj699, '_setHierarchicalLink')):
     self.obj699._setHierarchicalLink(False)

   # rate
   self.obj699.rate.setNone()

   self.obj699.GGLabel.setValue(5)
   self.obj699.graphClass_= graph_achieve
   if self.genGraphics:
      new_obj = graph_achieve(258.5,259.0,self.obj699)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj699.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj699)
   self.obj699.postAction( cobj0.LHS.CREATE )

   self.obj695.out_connections_.append(self.obj698)
   self.obj698.in_connections_.append(self.obj695)
   self.obj695.graphObject_.pendingConnections.append((self.obj695.graphObject_.tag, self.obj698.graphObject_.tag, [304.0, 141.0, 300.5, 120.5, 250.75, 110.75], 2, True))
   self.obj697.out_connections_.append(self.obj695)
   self.obj695.in_connections_.append(self.obj697)
   self.obj697.graphObject_.pendingConnections.append((self.obj697.graphObject_.tag, self.obj695.graphObject_.tag, [105.0, 102.0, 201.0, 101.0, 250.75, 110.75], 2, True))
   self.obj698.out_connections_.append(self.obj699)
   self.obj699.in_connections_.append(self.obj698)
   self.obj698.graphObject_.pendingConnections.append((self.obj698.graphObject_.tag, self.obj699.graphObject_.tag, [304.0, 186.0, 303.5, 233.0, 258.5, 259.0], 2, True))
   self.obj699.out_connections_.append(self.obj696)
   self.obj696.in_connections_.append(self.obj699)
   self.obj699.graphObject_.pendingConnections.append((self.obj699.graphObject_.tag, self.obj696.graphObject_.tag, [124.0, 290.0, 213.5, 285.0, 258.5, 259.0], 2, True))

   cobj0.RHS = ASG_pns(self)
   cobj0.RHS.merge(ASG_omacs(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj703=metarial(self)
   self.obj703.preAction( cobj0.RHS.CREATE )
   self.obj703.isGraphObjectVisual = True

   if(hasattr(self.obj703, '_setHierarchicalLink')):
     self.obj703._setHierarchicalLink(False)

   # MaxFlow
   self.obj703.MaxFlow.setValue(999999)

   # price
   self.obj703.price.setValue(0)

   # Name
   self.obj703.Name.setValue('')
   self.obj703.Name.setNone()

   # ReqFlow
   self.obj703.ReqFlow.setValue(0)

   self.obj703.GGLabel.setValue(8)
   self.obj703.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(400.0,80.0,self.obj703)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj703.graphObject_ = new_obj
   self.obj7030= AttrCalc()
   self.obj7030.Copy=ATOM3Boolean()
   self.obj7030.Copy.setValue(('Copy from LHS', 1))
   self.obj7030.Copy.config = 0
   self.obj7030.Specify=ATOM3Constraint()
   self.obj7030.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj703.GGset2Any['MaxFlow']= self.obj7030
   self.obj7031= AttrCalc()
   self.obj7031.Copy=ATOM3Boolean()
   self.obj7031.Copy.setValue(('Copy from LHS', 0))
   self.obj7031.Copy.config = 0
   self.obj7031.Specify=ATOM3Constraint()
   self.obj7031.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()+\' \'+ self.getMatched(graphID, self.LHS.nodeWithLabel(2)).name.getValue()+\' \'+ self.getMatched(graphID, self.LHS.nodeWithLabel(3)).name.getValue()\n\n'))
   self.obj703.GGset2Any['Name']= self.obj7031
   self.obj7032= AttrCalc()
   self.obj7032.Copy=ATOM3Boolean()
   self.obj7032.Copy.setValue(('Copy from LHS', 1))
   self.obj7032.Copy.config = 0
   self.obj7032.Specify=ATOM3Constraint()
   self.obj7032.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj703.GGset2Any['ReqFlow']= self.obj7032

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj703)
   self.obj703.postAction( cobj0.RHS.CREATE )

   self.obj704=operatingUnit(self)
   self.obj704.preAction( cobj0.RHS.CREATE )
   self.obj704.isGraphObjectVisual = True

   if(hasattr(self.obj704, '_setHierarchicalLink')):
     self.obj704._setHierarchicalLink(False)

   # OperCostProp
   self.obj704.OperCostProp.setValue(0.0)

   # name
   self.obj704.name.setValue('')
   self.obj704.name.setNone()

   # OperCostFix
   self.obj704.OperCostFix.setValue(0.0)

   self.obj704.GGLabel.setValue(7)
   self.obj704.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(400.0,240.0,self.obj704)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj704.graphObject_ = new_obj
   self.obj7040= AttrCalc()
   self.obj7040.Copy=ATOM3Boolean()
   self.obj7040.Copy.setValue(('Copy from LHS', 0))
   self.obj7040.Copy.config = 0
   self.obj7040.Specify=ATOM3Constraint()
   self.obj7040.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(5)).rate.getValue()\n'))
   self.obj704.GGset2Any['OperCostProp']= self.obj7040
   self.obj7041= AttrCalc()
   self.obj7041.Copy=ATOM3Boolean()
   self.obj7041.Copy.setValue(('Copy from LHS', 0))
   self.obj7041.Copy.config = 0
   self.obj7041.Specify=ATOM3Constraint()
   self.obj7041.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()+\' \'+ self.getMatched(graphID, self.LHS.nodeWithLabel(2)).name.getValue()+\' \'+ self.getMatched(graphID, self.LHS.nodeWithLabel(3)).name.getValue()\n\n\n\n\n\n\n'))
   self.obj704.GGset2Any['name']= self.obj7041
   self.obj7042= AttrCalc()
   self.obj7042.Copy=ATOM3Boolean()
   self.obj7042.Copy.setValue(('Copy from LHS', 0))
   self.obj7042.Copy.config = 0
   self.obj7042.Specify=ATOM3Constraint()
   self.obj7042.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return 2.0\n'))
   self.obj704.GGset2Any['OperCostFix']= self.obj7042

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj704)
   self.obj704.postAction( cobj0.RHS.CREATE )

   self.obj705=fromMaterial(self)
   self.obj705.preAction( cobj0.RHS.CREATE )
   self.obj705.isGraphObjectVisual = True

   if(hasattr(self.obj705, '_setHierarchicalLink')):
     self.obj705._setHierarchicalLink(False)

   # rate
   self.obj705.rate.setValue(1.0)

   self.obj705.GGLabel.setValue(9)
   self.obj705.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(422.0,190.0,self.obj705)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj705.graphObject_ = new_obj
   self.obj7050= AttrCalc()
   self.obj7050.Copy=ATOM3Boolean()
   self.obj7050.Copy.setValue(('Copy from LHS', 0))
   self.obj7050.Copy.config = 0
   self.obj7050.Specify=ATOM3Constraint()
   self.obj7050.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj705.GGset2Any['rate']= self.obj7050

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj705)
   self.obj705.postAction( cobj0.RHS.CREATE )

   self.obj706=CapableOf(self)
   self.obj706.preAction( cobj0.RHS.CREATE )
   self.obj706.isGraphObjectVisual = True

   if(hasattr(self.obj706, '_setHierarchicalLink')):
     self.obj706._setHierarchicalLink(False)

   # rate
   self.obj706.rate.setNone()

   self.obj706.GGLabel.setValue(4)
   self.obj706.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(250.75,110.75,self.obj706)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj706.graphObject_ = new_obj
   self.obj7060= AttrCalc()
   self.obj7060.Copy=ATOM3Boolean()
   self.obj7060.Copy.setValue(('Copy from LHS', 1))
   self.obj7060.Copy.config = 0
   self.obj7060.Specify=ATOM3Constraint()
   self.obj7060.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj706.GGset2Any['rate']= self.obj7060

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj706)
   self.obj706.postAction( cobj0.RHS.CREATE )

   self.obj707=Goal(self)
   self.obj707.preAction( cobj0.RHS.CREATE )
   self.obj707.isGraphObjectVisual = True

   if(hasattr(self.obj707, '_setHierarchicalLink')):
     self.obj707._setHierarchicalLink(False)

   # name
   self.obj707.name.setValue('')
   self.obj707.name.setNone()

   self.obj707.GGLabel.setValue(3)
   self.obj707.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(100.0,240.0,self.obj707)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj707.graphObject_ = new_obj
   self.obj7070= AttrCalc()
   self.obj7070.Copy=ATOM3Boolean()
   self.obj7070.Copy.setValue(('Copy from LHS', 1))
   self.obj7070.Copy.config = 0
   self.obj7070.Specify=ATOM3Constraint()
   self.obj7070.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj707.GGset2Any['name']= self.obj7070

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj707)
   self.obj707.postAction( cobj0.RHS.CREATE )

   self.obj708=Agent(self)
   self.obj708.preAction( cobj0.RHS.CREATE )
   self.obj708.isGraphObjectVisual = True

   if(hasattr(self.obj708, '_setHierarchicalLink')):
     self.obj708._setHierarchicalLink(False)

   # price
   self.obj708.price.setNone()

   # name
   self.obj708.name.setValue('')
   self.obj708.name.setNone()

   self.obj708.GGLabel.setValue(1)
   self.obj708.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(80.0,40.0,self.obj708)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj708.graphObject_ = new_obj
   self.obj7080= AttrCalc()
   self.obj7080.Copy=ATOM3Boolean()
   self.obj7080.Copy.setValue(('Copy from LHS', 1))
   self.obj7080.Copy.config = 0
   self.obj7080.Specify=ATOM3Constraint()
   self.obj7080.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj708.GGset2Any['price']= self.obj7080
   self.obj7081= AttrCalc()
   self.obj7081.Copy=ATOM3Boolean()
   self.obj7081.Copy.setValue(('Copy from LHS', 1))
   self.obj7081.Copy.config = 0
   self.obj7081.Specify=ATOM3Constraint()
   self.obj7081.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj708.GGset2Any['name']= self.obj7081

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj708)
   self.obj708.postAction( cobj0.RHS.CREATE )

   self.obj709=Role(self)
   self.obj709.preAction( cobj0.RHS.CREATE )
   self.obj709.isGraphObjectVisual = True

   if(hasattr(self.obj709, '_setHierarchicalLink')):
     self.obj709._setHierarchicalLink(False)

   # name
   self.obj709.name.setValue('')
   self.obj709.name.setNone()

   self.obj709.GGLabel.setValue(2)
   self.obj709.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(280.0,140.0,self.obj709)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj709.graphObject_ = new_obj
   self.obj7090= AttrCalc()
   self.obj7090.Copy=ATOM3Boolean()
   self.obj7090.Copy.setValue(('Copy from LHS', 1))
   self.obj7090.Copy.config = 0
   self.obj7090.Specify=ATOM3Constraint()
   self.obj7090.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj709.GGset2Any['name']= self.obj7090

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj709)
   self.obj709.postAction( cobj0.RHS.CREATE )

   self.obj710=achieve(self)
   self.obj710.preAction( cobj0.RHS.CREATE )
   self.obj710.isGraphObjectVisual = True

   if(hasattr(self.obj710, '_setHierarchicalLink')):
     self.obj710._setHierarchicalLink(False)

   # rate
   self.obj710.rate.setNone()

   self.obj710.GGLabel.setValue(5)
   self.obj710.graphClass_= graph_achieve
   if self.genGraphics:
      new_obj = graph_achieve(258.5,259.0,self.obj710)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj710.graphObject_ = new_obj
   self.obj7100= AttrCalc()
   self.obj7100.Copy=ATOM3Boolean()
   self.obj7100.Copy.setValue(('Copy from LHS', 1))
   self.obj7100.Copy.config = 0
   self.obj7100.Specify=ATOM3Constraint()
   self.obj7100.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj710.GGset2Any['rate']= self.obj7100

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj710)
   self.obj710.postAction( cobj0.RHS.CREATE )

   self.obj711=GenericGraphEdge(self)
   self.obj711.preAction( cobj0.RHS.CREATE )
   self.obj711.isGraphObjectVisual = True

   if(hasattr(self.obj711, '_setHierarchicalLink')):
     self.obj711._setHierarchicalLink(False)

   self.obj711.GGLabel.setValue(10)
   self.obj711.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(358.5,131.0,self.obj711)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj711.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj711)
   self.obj711.postAction( cobj0.RHS.CREATE )

   self.obj703.out_connections_.append(self.obj705)
   self.obj705.in_connections_.append(self.obj703)
   self.obj703.graphObject_.pendingConnections.append((self.obj703.graphObject_.tag, self.obj705.graphObject_.tag, [424.0, 129.0, 422.0, 190.0], 0, True))
   self.obj705.out_connections_.append(self.obj704)
   self.obj704.in_connections_.append(self.obj705)
   self.obj705.graphObject_.pendingConnections.append((self.obj705.graphObject_.tag, self.obj704.graphObject_.tag, [420.0, 251.0, 422.0, 190.0], 0, True))
   self.obj706.out_connections_.append(self.obj709)
   self.obj709.in_connections_.append(self.obj706)
   self.obj706.graphObject_.pendingConnections.append((self.obj706.graphObject_.tag, self.obj709.graphObject_.tag, [311.0, 140.0, 250.75, 110.75], 2, 0))
   self.obj708.out_connections_.append(self.obj706)
   self.obj706.in_connections_.append(self.obj708)
   self.obj708.graphObject_.pendingConnections.append((self.obj708.graphObject_.tag, self.obj706.graphObject_.tag, [117.0, 102.0, 250.75, 110.75], 2, 0))
   self.obj709.out_connections_.append(self.obj710)
   self.obj710.in_connections_.append(self.obj709)
   self.obj709.graphObject_.pendingConnections.append((self.obj709.graphObject_.tag, self.obj710.graphObject_.tag, [311.0, 185.0, 258.5, 259.0], 2, 0))
   self.obj709.out_connections_.append(self.obj711)
   self.obj711.in_connections_.append(self.obj709)
   self.obj709.graphObject_.pendingConnections.append((self.obj709.graphObject_.tag, self.obj711.graphObject_.tag, [311.0, 140.0, 358.5, 131.0], 0, True))
   self.obj710.out_connections_.append(self.obj707)
   self.obj707.in_connections_.append(self.obj710)
   self.obj710.graphObject_.pendingConnections.append((self.obj710.graphObject_.tag, self.obj707.graphObject_.tag, [134.0, 290.0, 258.5, 259.0], 2, 0))
   self.obj711.out_connections_.append(self.obj703)
   self.obj703.in_connections_.append(self.obj711)
   self.obj711.graphObject_.pendingConnections.append((self.obj711.graphObject_.tag, self.obj703.graphObject_.tag, [406.0, 122.0, 358.5, 131.0], 0, True))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'print \'======> GenAux1 Condition\'\na = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\naN = a.name.getValue()\n#print a.name.getValue()+\' has att AUX : \'+str( hasattr(a, "AUX") )\nr = self.getMatched(graphID, self.LHS.nodeWithLabel(2))\nRn = r.name.getValue()\ng = self.getMatched(graphID, self.LHS.nodeWithLabel(3))\nGn = g.name.getValue()\n# add list to the Agent Node\nif not hasattr(a,\'markedNode\') : \n	a.markedNode = []\n	print \'add List to \'+aN\n\nprint \'CHeck if \'+aN+\'Have\'\nfor ele in a.markedNode : \n    if ele == (Rn,Gn) : return False\nreturn True\n#        print \'Check if \'+aN+\'Have \'\n#        for ele in a.markedNode : \n#            if ele == (Rn,Gn) : return False \n#        return True\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'print \'======> GenAux1 ACtion\'\na = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\naN = a.name.getValue()\n#print a.name.getValue()+\' has att AUX : \'+str( hasattr(a, "AUX") )\nr = self.getMatched(graphID, self.LHS.nodeWithLabel(2))\nRn = r.name.getValue()\ng = self.getMatched(graphID, self.LHS.nodeWithLabel(3))\nGn = g.name.getValue()\n# add ele list to the Agent Node\nprint \'Add Ele into list of \'+aN\na.markedNode.append( (Rn,Gn) )\nprint \'List of MarkedNode\'\nfor ele in a.markedNode : \n	print ele\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('CreateLinkMat_ARG2Goal', 20)
   cobj0.Order=ATOM3Integer(19)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

   from Capabilitie import *
   from rawMaterial import *
   from GenericGraphEdge import *
   from Goal import *
   from ASG_pns import *
   from operatingUnit import *
   from metarial import *
   from GenericGraphNode import *
   from product import *
   from Agent import *
   from fromMaterial import *
   from CapableOf import *
   from intoProduct import *
   from Role import *
   from fromRaw import *
   from intoMaterial import *
   from ASG_GenericGraph import *
   from ASG_omacs import *
   from require import *
   from achieve import *
   from posses import *

   cobj0.LHS = ASG_pns(self)
   cobj0.LHS.merge(ASG_omacs(self))
   cobj0.LHS.merge(ASG_GenericGraph(self))

   self.obj718=metarial(self)
   self.obj718.preAction( cobj0.LHS.CREATE )
   self.obj718.isGraphObjectVisual = True

   if(hasattr(self.obj718, '_setHierarchicalLink')):
     self.obj718._setHierarchicalLink(False)

   # MaxFlow
   self.obj718.MaxFlow.setNone()

   # price
   self.obj718.price.setValue(0)

   # Name
   self.obj718.Name.setValue('')
   self.obj718.Name.setNone()

   # ReqFlow
   self.obj718.ReqFlow.setNone()

   self.obj718.GGLabel.setValue(4)
   self.obj718.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(240.0,20.0,self.obj718)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj718.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj718)
   self.obj718.postAction( cobj0.LHS.CREATE )

   self.obj719=metarial(self)
   self.obj719.preAction( cobj0.LHS.CREATE )
   self.obj719.isGraphObjectVisual = True

   if(hasattr(self.obj719, '_setHierarchicalLink')):
     self.obj719._setHierarchicalLink(False)

   # MaxFlow
   self.obj719.MaxFlow.setNone()

   # price
   self.obj719.price.setValue(0)

   # Name
   self.obj719.Name.setValue('')
   self.obj719.Name.setNone()

   # ReqFlow
   self.obj719.ReqFlow.setNone()

   self.obj719.GGLabel.setValue(6)
   self.obj719.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(240.0,240.0,self.obj719)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj719.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj719)
   self.obj719.postAction( cobj0.LHS.CREATE )

   self.obj720=operatingUnit(self)
   self.obj720.preAction( cobj0.LHS.CREATE )
   self.obj720.isGraphObjectVisual = True

   if(hasattr(self.obj720, '_setHierarchicalLink')):
     self.obj720._setHierarchicalLink(False)

   # OperCostProp
   self.obj720.OperCostProp.setNone()

   # name
   self.obj720.name.setValue('')
   self.obj720.name.setNone()

   # OperCostFix
   self.obj720.OperCostFix.setNone()

   self.obj720.GGLabel.setValue(5)
   self.obj720.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(240.0,140.0,self.obj720)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj720.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj720)
   self.obj720.postAction( cobj0.LHS.CREATE )

   self.obj721=fromMaterial(self)
   self.obj721.preAction( cobj0.LHS.CREATE )
   self.obj721.isGraphObjectVisual = True

   if(hasattr(self.obj721, '_setHierarchicalLink')):
     self.obj721._setHierarchicalLink(False)

   # rate
   self.obj721.rate.setNone()

   self.obj721.GGLabel.setValue(8)
   self.obj721.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(265.0,100.0,self.obj721)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj721.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj721)
   self.obj721.postAction( cobj0.LHS.CREATE )

   self.obj722=Goal(self)
   self.obj722.preAction( cobj0.LHS.CREATE )
   self.obj722.isGraphObjectVisual = True

   if(hasattr(self.obj722, '_setHierarchicalLink')):
     self.obj722._setHierarchicalLink(False)

   # name
   self.obj722.name.setValue('')
   self.obj722.name.setNone()

   self.obj722.GGLabel.setValue(2)
   self.obj722.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(60.0,220.0,self.obj722)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj722.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj722)
   self.obj722.postAction( cobj0.LHS.CREATE )

   self.obj723=Role(self)
   self.obj723.preAction( cobj0.LHS.CREATE )
   self.obj723.isGraphObjectVisual = True

   if(hasattr(self.obj723, '_setHierarchicalLink')):
     self.obj723._setHierarchicalLink(False)

   # name
   self.obj723.name.setValue('')
   self.obj723.name.setNone()

   self.obj723.GGLabel.setValue(1)
   self.obj723.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(60.0,40.0,self.obj723)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj723.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj723)
   self.obj723.postAction( cobj0.LHS.CREATE )

   self.obj724=achieve(self)
   self.obj724.preAction( cobj0.LHS.CREATE )
   self.obj724.isGraphObjectVisual = True

   if(hasattr(self.obj724, '_setHierarchicalLink')):
     self.obj724._setHierarchicalLink(False)

   # rate
   self.obj724.rate.setNone()

   self.obj724.GGLabel.setValue(3)
   self.obj724.graphClass_= graph_achieve
   if self.genGraphics:
      new_obj = graph_achieve(97.5,137.5,self.obj724)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj724.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj724)
   self.obj724.postAction( cobj0.LHS.CREATE )

   self.obj725=GenericGraphEdge(self)
   self.obj725.preAction( cobj0.LHS.CREATE )
   self.obj725.isGraphObjectVisual = True

   if(hasattr(self.obj725, '_setHierarchicalLink')):
     self.obj725._setHierarchicalLink(False)

   self.obj725.GGLabel.setValue(7)
   self.obj725.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(215.0,41.5,self.obj725)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj725.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj725)
   self.obj725.postAction( cobj0.LHS.CREATE )

   self.obj726=GenericGraphEdge(self)
   self.obj726.preAction( cobj0.LHS.CREATE )
   self.obj726.isGraphObjectVisual = True

   if(hasattr(self.obj726, '_setHierarchicalLink')):
     self.obj726._setHierarchicalLink(False)

   self.obj726.GGLabel.setValue(9)
   self.obj726.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(185.0,276.0,self.obj726)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj726.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj726)
   self.obj726.postAction( cobj0.LHS.CREATE )

   self.obj718.out_connections_.append(self.obj721)
   self.obj721.in_connections_.append(self.obj718)
   self.obj718.graphObject_.pendingConnections.append((self.obj718.graphObject_.tag, self.obj721.graphObject_.tag, [264.0, 69.0, 265.0, 100.0], 0, True))
   self.obj721.out_connections_.append(self.obj720)
   self.obj720.in_connections_.append(self.obj721)
   self.obj721.graphObject_.pendingConnections.append((self.obj721.graphObject_.tag, self.obj720.graphObject_.tag, [260.0, 151.0, 352.0, 90.0], 0, True))
   self.obj722.out_connections_.append(self.obj726)
   self.obj726.in_connections_.append(self.obj722)
   self.obj722.graphObject_.pendingConnections.append((self.obj722.graphObject_.tag, self.obj726.graphObject_.tag, [84.0, 270.0, 185.0, 276.0], 0, True))
   self.obj723.out_connections_.append(self.obj724)
   self.obj724.in_connections_.append(self.obj723)
   self.obj723.graphObject_.pendingConnections.append((self.obj723.graphObject_.tag, self.obj724.graphObject_.tag, [84.0, 86.0, 97.5, 137.5], 0, True))
   self.obj723.out_connections_.append(self.obj725)
   self.obj725.in_connections_.append(self.obj723)
   self.obj723.graphObject_.pendingConnections.append((self.obj723.graphObject_.tag, self.obj725.graphObject_.tag, [84.0, 41.0, 215.0, 41.5], 0, True))
   self.obj724.out_connections_.append(self.obj722)
   self.obj722.in_connections_.append(self.obj724)
   self.obj724.graphObject_.pendingConnections.append((self.obj724.graphObject_.tag, self.obj722.graphObject_.tag, [83.0, 221.0, 93.5, 143.5], 0, True))
   self.obj725.out_connections_.append(self.obj718)
   self.obj718.in_connections_.append(self.obj725)
   self.obj725.graphObject_.pendingConnections.append((self.obj725.graphObject_.tag, self.obj718.graphObject_.tag, [246.0, 62.0, 215.0, 41.5], 0, True))
   self.obj726.out_connections_.append(self.obj719)
   self.obj719.in_connections_.append(self.obj726)
   self.obj726.graphObject_.pendingConnections.append((self.obj726.graphObject_.tag, self.obj719.graphObject_.tag, [246.0, 282.0, 185.0, 276.0], 0, True))

   cobj0.RHS = ASG_pns(self)
   cobj0.RHS.merge(ASG_omacs(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj730=metarial(self)
   self.obj730.preAction( cobj0.RHS.CREATE )
   self.obj730.isGraphObjectVisual = True

   if(hasattr(self.obj730, '_setHierarchicalLink')):
     self.obj730._setHierarchicalLink(False)

   # MaxFlow
   self.obj730.MaxFlow.setNone()

   # price
   self.obj730.price.setValue(0)

   # Name
   self.obj730.Name.setValue('')
   self.obj730.Name.setNone()

   # ReqFlow
   self.obj730.ReqFlow.setNone()

   self.obj730.GGLabel.setValue(4)
   self.obj730.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(280.0,20.0,self.obj730)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj730.graphObject_ = new_obj
   self.obj7300= AttrCalc()
   self.obj7300.Copy=ATOM3Boolean()
   self.obj7300.Copy.setValue(('Copy from LHS', 1))
   self.obj7300.Copy.config = 0
   self.obj7300.Specify=ATOM3Constraint()
   self.obj7300.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj730.GGset2Any['MaxFlow']= self.obj7300
   self.obj7301= AttrCalc()
   self.obj7301.Copy=ATOM3Boolean()
   self.obj7301.Copy.setValue(('Copy from LHS', 1))
   self.obj7301.Copy.config = 0
   self.obj7301.Specify=ATOM3Constraint()
   self.obj7301.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj730.GGset2Any['Name']= self.obj7301
   self.obj7302= AttrCalc()
   self.obj7302.Copy=ATOM3Boolean()
   self.obj7302.Copy.setValue(('Copy from LHS', 1))
   self.obj7302.Copy.config = 0
   self.obj7302.Specify=ATOM3Constraint()
   self.obj7302.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj730.GGset2Any['ReqFlow']= self.obj7302

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj730)
   self.obj730.postAction( cobj0.RHS.CREATE )

   self.obj731=metarial(self)
   self.obj731.preAction( cobj0.RHS.CREATE )
   self.obj731.isGraphObjectVisual = True

   if(hasattr(self.obj731, '_setHierarchicalLink')):
     self.obj731._setHierarchicalLink(False)

   # MaxFlow
   self.obj731.MaxFlow.setNone()

   # price
   self.obj731.price.setValue(0)

   # Name
   self.obj731.Name.setValue('')
   self.obj731.Name.setNone()

   # ReqFlow
   self.obj731.ReqFlow.setNone()

   self.obj731.GGLabel.setValue(6)
   self.obj731.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(280.0,240.0,self.obj731)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj731.graphObject_ = new_obj
   self.obj7310= AttrCalc()
   self.obj7310.Copy=ATOM3Boolean()
   self.obj7310.Copy.setValue(('Copy from LHS', 1))
   self.obj7310.Copy.config = 0
   self.obj7310.Specify=ATOM3Constraint()
   self.obj7310.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj731.GGset2Any['MaxFlow']= self.obj7310
   self.obj7311= AttrCalc()
   self.obj7311.Copy=ATOM3Boolean()
   self.obj7311.Copy.setValue(('Copy from LHS', 1))
   self.obj7311.Copy.config = 0
   self.obj7311.Specify=ATOM3Constraint()
   self.obj7311.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj731.GGset2Any['Name']= self.obj7311
   self.obj7312= AttrCalc()
   self.obj7312.Copy=ATOM3Boolean()
   self.obj7312.Copy.setValue(('Copy from LHS', 1))
   self.obj7312.Copy.config = 0
   self.obj7312.Specify=ATOM3Constraint()
   self.obj7312.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj731.GGset2Any['ReqFlow']= self.obj7312

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj731)
   self.obj731.postAction( cobj0.RHS.CREATE )

   self.obj732=operatingUnit(self)
   self.obj732.preAction( cobj0.RHS.CREATE )
   self.obj732.isGraphObjectVisual = True

   if(hasattr(self.obj732, '_setHierarchicalLink')):
     self.obj732._setHierarchicalLink(False)

   # OperCostProp
   self.obj732.OperCostProp.setNone()

   # name
   self.obj732.name.setValue('')
   self.obj732.name.setNone()

   # OperCostFix
   self.obj732.OperCostFix.setNone()

   self.obj732.GGLabel.setValue(5)
   self.obj732.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(280.0,140.0,self.obj732)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj732.graphObject_ = new_obj
   self.obj7320= AttrCalc()
   self.obj7320.Copy=ATOM3Boolean()
   self.obj7320.Copy.setValue(('Copy from LHS', 1))
   self.obj7320.Copy.config = 0
   self.obj7320.Specify=ATOM3Constraint()
   self.obj7320.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj732.GGset2Any['OperCostProp']= self.obj7320
   self.obj7321= AttrCalc()
   self.obj7321.Copy=ATOM3Boolean()
   self.obj7321.Copy.setValue(('Copy from LHS', 1))
   self.obj7321.Copy.config = 0
   self.obj7321.Specify=ATOM3Constraint()
   self.obj7321.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj732.GGset2Any['name']= self.obj7321
   self.obj7322= AttrCalc()
   self.obj7322.Copy=ATOM3Boolean()
   self.obj7322.Copy.setValue(('Copy from LHS', 1))
   self.obj7322.Copy.config = 0
   self.obj7322.Specify=ATOM3Constraint()
   self.obj7322.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj732.GGset2Any['OperCostFix']= self.obj7322

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj732)
   self.obj732.postAction( cobj0.RHS.CREATE )

   self.obj733=intoMaterial(self)
   self.obj733.preAction( cobj0.RHS.CREATE )
   self.obj733.isGraphObjectVisual = True

   if(hasattr(self.obj733, '_setHierarchicalLink')):
     self.obj733._setHierarchicalLink(False)

   # rate
   self.obj733.rate.setValue(0.0)

   self.obj733.GGLabel.setValue(10)
   self.obj733.graphClass_= graph_intoMaterial
   if self.genGraphics:
      new_obj = graph_intoMaterial(315.25,202.5,self.obj733)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj733.graphObject_ = new_obj
   self.obj7330= AttrCalc()
   self.obj7330.Copy=ATOM3Boolean()
   self.obj7330.Copy.setValue(('Copy from LHS', 0))
   self.obj7330.Copy.config = 0
   self.obj7330.Specify=ATOM3Constraint()
   self.obj7330.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(3)).rate.getValue()\n\n\n\n\n\n\n\n\n\n'))
   self.obj733.GGset2Any['rate']= self.obj7330

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj733)
   self.obj733.postAction( cobj0.RHS.CREATE )

   self.obj734=fromMaterial(self)
   self.obj734.preAction( cobj0.RHS.CREATE )
   self.obj734.isGraphObjectVisual = True

   if(hasattr(self.obj734, '_setHierarchicalLink')):
     self.obj734._setHierarchicalLink(False)

   # rate
   self.obj734.rate.setNone()

   self.obj734.GGLabel.setValue(8)
   self.obj734.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(323.0,83.0,self.obj734)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj734.graphObject_ = new_obj
   self.obj7340= AttrCalc()
   self.obj7340.Copy=ATOM3Boolean()
   self.obj7340.Copy.setValue(('Copy from LHS', 1))
   self.obj7340.Copy.config = 0
   self.obj7340.Specify=ATOM3Constraint()
   self.obj7340.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj734.GGset2Any['rate']= self.obj7340

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj734)
   self.obj734.postAction( cobj0.RHS.CREATE )

   self.obj735=Goal(self)
   self.obj735.preAction( cobj0.RHS.CREATE )
   self.obj735.isGraphObjectVisual = True

   if(hasattr(self.obj735, '_setHierarchicalLink')):
     self.obj735._setHierarchicalLink(False)

   # name
   self.obj735.name.setValue('')
   self.obj735.name.setNone()

   self.obj735.GGLabel.setValue(2)
   self.obj735.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(60.0,220.0,self.obj735)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj735.graphObject_ = new_obj
   self.obj7350= AttrCalc()
   self.obj7350.Copy=ATOM3Boolean()
   self.obj7350.Copy.setValue(('Copy from LHS', 1))
   self.obj7350.Copy.config = 0
   self.obj7350.Specify=ATOM3Constraint()
   self.obj7350.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj735.GGset2Any['name']= self.obj7350

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj735)
   self.obj735.postAction( cobj0.RHS.CREATE )

   self.obj736=Role(self)
   self.obj736.preAction( cobj0.RHS.CREATE )
   self.obj736.isGraphObjectVisual = True

   if(hasattr(self.obj736, '_setHierarchicalLink')):
     self.obj736._setHierarchicalLink(False)

   # name
   self.obj736.name.setValue('')
   self.obj736.name.setNone()

   self.obj736.GGLabel.setValue(1)
   self.obj736.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(60.0,40.0,self.obj736)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj736.graphObject_ = new_obj
   self.obj7360= AttrCalc()
   self.obj7360.Copy=ATOM3Boolean()
   self.obj7360.Copy.setValue(('Copy from LHS', 1))
   self.obj7360.Copy.config = 0
   self.obj7360.Specify=ATOM3Constraint()
   self.obj7360.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj736.GGset2Any['name']= self.obj7360

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj736)
   self.obj736.postAction( cobj0.RHS.CREATE )

   self.obj737=achieve(self)
   self.obj737.preAction( cobj0.RHS.CREATE )
   self.obj737.isGraphObjectVisual = True

   if(hasattr(self.obj737, '_setHierarchicalLink')):
     self.obj737._setHierarchicalLink(False)

   # rate
   self.obj737.rate.setNone()

   self.obj737.GGLabel.setValue(3)
   self.obj737.graphClass_= graph_achieve
   if self.genGraphics:
      new_obj = graph_achieve(93.5,143.5,self.obj737)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj737.graphObject_ = new_obj
   self.obj7370= AttrCalc()
   self.obj7370.Copy=ATOM3Boolean()
   self.obj7370.Copy.setValue(('Copy from LHS', 1))
   self.obj7370.Copy.config = 0
   self.obj7370.Specify=ATOM3Constraint()
   self.obj7370.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj737.GGset2Any['rate']= self.obj7370

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj737)
   self.obj737.postAction( cobj0.RHS.CREATE )

   self.obj738=GenericGraphEdge(self)
   self.obj738.preAction( cobj0.RHS.CREATE )
   self.obj738.isGraphObjectVisual = True

   if(hasattr(self.obj738, '_setHierarchicalLink')):
     self.obj738._setHierarchicalLink(False)

   self.obj738.GGLabel.setValue(7)
   self.obj738.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(215.0,41.5,self.obj738)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj738.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj738)
   self.obj738.postAction( cobj0.RHS.CREATE )

   self.obj739=GenericGraphEdge(self)
   self.obj739.preAction( cobj0.RHS.CREATE )
   self.obj739.isGraphObjectVisual = True

   if(hasattr(self.obj739, '_setHierarchicalLink')):
     self.obj739._setHierarchicalLink(False)

   self.obj739.GGLabel.setValue(9)
   self.obj739.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(185.0,276.0,self.obj739)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj739.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj739)
   self.obj739.postAction( cobj0.RHS.CREATE )

   self.obj730.out_connections_.append(self.obj734)
   self.obj734.in_connections_.append(self.obj730)
   self.obj730.graphObject_.pendingConnections.append((self.obj730.graphObject_.tag, self.obj734.graphObject_.tag, [284.0, 69.0, 323.0, 83.0], 2, 0))
   self.obj732.out_connections_.append(self.obj733)
   self.obj733.in_connections_.append(self.obj732)
   self.obj732.graphObject_.pendingConnections.append((self.obj732.graphObject_.tag, self.obj733.graphObject_.tag, [333.0, 148.0, 332.0, 167.0, 371.25, 179.5], 2, True))
   self.obj733.out_connections_.append(self.obj731)
   self.obj731.in_connections_.append(self.obj733)
   self.obj733.graphObject_.pendingConnections.append((self.obj733.graphObject_.tag, self.obj731.graphObject_.tag, [326.0, 250.0, 354.5, 215.0, 371.25, 179.5], 2, True))
   self.obj734.out_connections_.append(self.obj732)
   self.obj732.in_connections_.append(self.obj734)
   self.obj734.graphObject_.pendingConnections.append((self.obj734.graphObject_.tag, self.obj732.graphObject_.tag, [333.0, 148.0, 352.0, 90.0], 2, 0))
   self.obj735.out_connections_.append(self.obj739)
   self.obj739.in_connections_.append(self.obj735)
   self.obj735.graphObject_.pendingConnections.append((self.obj735.graphObject_.tag, self.obj739.graphObject_.tag, [94.0, 270.0, 185.0, 276.0], 2, 0))
   self.obj736.out_connections_.append(self.obj737)
   self.obj737.in_connections_.append(self.obj736)
   self.obj736.graphObject_.pendingConnections.append((self.obj736.graphObject_.tag, self.obj737.graphObject_.tag, [91.0, 85.0, 93.5, 143.5], 2, 0))
   self.obj736.out_connections_.append(self.obj738)
   self.obj738.in_connections_.append(self.obj736)
   self.obj736.graphObject_.pendingConnections.append((self.obj736.graphObject_.tag, self.obj738.graphObject_.tag, [91.0, 40.0, 215.0, 41.5], 2, 0))
   self.obj737.out_connections_.append(self.obj735)
   self.obj735.in_connections_.append(self.obj737)
   self.obj737.graphObject_.pendingConnections.append((self.obj737.graphObject_.tag, self.obj735.graphObject_.tag, [93.0, 221.0, 93.5, 143.5], 2, 0))
   self.obj738.out_connections_.append(self.obj730)
   self.obj730.in_connections_.append(self.obj738)
   self.obj738.graphObject_.pendingConnections.append((self.obj738.graphObject_.tag, self.obj730.graphObject_.tag, [266.0, 62.0, 215.0, 41.5], 2, 0))
   self.obj739.out_connections_.append(self.obj731)
   self.obj731.in_connections_.append(self.obj739)
   self.obj739.graphObject_.pendingConnections.append((self.obj739.graphObject_.tag, self.obj731.graphObject_.tag, [286.0, 282.0, 185.0, 276.0], 2, 0))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'print \'======> Link Aux Condition\'# _ Agent2Raw_GG_rule.py _\naRg = self.getMatched ( graphID , self.LHS.nodeWithLabel(4) )\nnameARG = aRg.Name.getValue()\ng = self.getMatched ( graphID , self.LHS.nodeWithLabel(6) )\n# test if nameARG  end with name of Goal \nprint  nameARG +\' END WITH \'+g.Name.getValue()\nprint nameARG.endswith( g.Name.getValue() )\nif nameARG.endswith( g.Name.getValue() ) and not hasattr(aRg,\'LinkAux\'): \n print \'Real True\'\n return True\nelse : \n print \'Real False\'\n return False\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'print \'======> Link Aux Action\'\naRg = self.getMatched ( graphID , self.LHS.nodeWithLabel(4) )\naRg.LinkAux = True \n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('CreateLinkAR2Mat', 20)
   cobj0.Order=ATOM3Integer(21)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

   from Capabilitie import *
   from rawMaterial import *
   from GenericGraphEdge import *
   from Goal import *
   from ASG_pns import *
   from operatingUnit import *
   from metarial import *
   from GenericGraphNode import *
   from product import *
   from Agent import *
   from fromMaterial import *
   from CapableOf import *
   from intoProduct import *
   from Role import *
   from fromRaw import *
   from intoMaterial import *
   from ASG_GenericGraph import *
   from ASG_omacs import *
   from require import *
   from achieve import *
   from posses import *

   cobj0.LHS = ASG_pns(self)
   cobj0.LHS.merge(ASG_omacs(self))
   cobj0.LHS.merge(ASG_GenericGraph(self))

   self.obj746=rawMaterial(self)
   self.obj746.preAction( cobj0.LHS.CREATE )
   self.obj746.isGraphObjectVisual = True

   if(hasattr(self.obj746, '_setHierarchicalLink')):
     self.obj746._setHierarchicalLink(False)

   # MaxFlow
   self.obj746.MaxFlow.setNone()

   # price
   self.obj746.price.setValue(0)

   # Name
   self.obj746.Name.setValue('')
   self.obj746.Name.setNone()

   # ReqFlow
   self.obj746.ReqFlow.setNone()

   self.obj746.GGLabel.setValue(6)
   self.obj746.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(240.0,0.0,self.obj746)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj746.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj746)
   self.obj746.postAction( cobj0.LHS.CREATE )

   self.obj747=metarial(self)
   self.obj747.preAction( cobj0.LHS.CREATE )
   self.obj747.isGraphObjectVisual = True

   if(hasattr(self.obj747, '_setHierarchicalLink')):
     self.obj747._setHierarchicalLink(False)

   # MaxFlow
   self.obj747.MaxFlow.setNone()

   # price
   self.obj747.price.setValue(0)

   # Name
   self.obj747.Name.setValue('')
   self.obj747.Name.setNone()

   # ReqFlow
   self.obj747.ReqFlow.setNone()

   self.obj747.GGLabel.setValue(11)
   self.obj747.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(260.0,200.0,self.obj747)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj747.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj747)
   self.obj747.postAction( cobj0.LHS.CREATE )

   self.obj748=operatingUnit(self)
   self.obj748.preAction( cobj0.LHS.CREATE )
   self.obj748.isGraphObjectVisual = True

   if(hasattr(self.obj748, '_setHierarchicalLink')):
     self.obj748._setHierarchicalLink(False)

   # OperCostProp
   self.obj748.OperCostProp.setNone()

   # name
   self.obj748.name.setValue('')
   self.obj748.name.setNone()

   # OperCostFix
   self.obj748.OperCostFix.setNone()

   self.obj748.GGLabel.setValue(7)
   self.obj748.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(280.0,100.0,self.obj748)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj748.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj748)
   self.obj748.postAction( cobj0.LHS.CREATE )

   self.obj749=operatingUnit(self)
   self.obj749.preAction( cobj0.LHS.CREATE )
   self.obj749.isGraphObjectVisual = True

   if(hasattr(self.obj749, '_setHierarchicalLink')):
     self.obj749._setHierarchicalLink(False)

   # OperCostProp
   self.obj749.OperCostProp.setNone()

   # name
   self.obj749.name.setValue('')
   self.obj749.name.setNone()

   # OperCostFix
   self.obj749.OperCostFix.setNone()

   self.obj749.GGLabel.setValue(12)
   self.obj749.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(360.0,260.0,self.obj749)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj749.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj749)
   self.obj749.postAction( cobj0.LHS.CREATE )

   self.obj750=fromRaw(self)
   self.obj750.preAction( cobj0.LHS.CREATE )
   self.obj750.isGraphObjectVisual = True

   if(hasattr(self.obj750, '_setHierarchicalLink')):
     self.obj750._setHierarchicalLink(False)

   # rate
   self.obj750.rate.setNone()

   self.obj750.GGLabel.setValue(8)
   self.obj750.graphClass_= graph_fromRaw
   if self.genGraphics:
      new_obj = graph_fromRaw(311.5,63.25,self.obj750)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj750.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj750)
   self.obj750.postAction( cobj0.LHS.CREATE )

   self.obj751=fromMaterial(self)
   self.obj751.preAction( cobj0.LHS.CREATE )
   self.obj751.isGraphObjectVisual = True

   if(hasattr(self.obj751, '_setHierarchicalLink')):
     self.obj751._setHierarchicalLink(False)

   # rate
   self.obj751.rate.setNone()

   self.obj751.GGLabel.setValue(14)
   self.obj751.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(379.5,235.25,self.obj751)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj751.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj751)
   self.obj751.postAction( cobj0.LHS.CREATE )

   self.obj752=CapableOf(self)
   self.obj752.preAction( cobj0.LHS.CREATE )
   self.obj752.isGraphObjectVisual = True

   if(hasattr(self.obj752, '_setHierarchicalLink')):
     self.obj752._setHierarchicalLink(False)

   # rate
   self.obj752.rate.setNone()

   self.obj752.GGLabel.setValue(3)
   self.obj752.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(84.5,131.5,self.obj752)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj752.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj752)
   self.obj752.postAction( cobj0.LHS.CREATE )

   self.obj753=Agent(self)
   self.obj753.preAction( cobj0.LHS.CREATE )
   self.obj753.isGraphObjectVisual = True

   if(hasattr(self.obj753, '_setHierarchicalLink')):
     self.obj753._setHierarchicalLink(False)

   # price
   self.obj753.price.setNone()

   # name
   self.obj753.name.setValue('')
   self.obj753.name.setNone()

   self.obj753.GGLabel.setValue(1)
   self.obj753.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(60.0,20.0,self.obj753)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj753.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj753)
   self.obj753.postAction( cobj0.LHS.CREATE )

   self.obj754=Role(self)
   self.obj754.preAction( cobj0.LHS.CREATE )
   self.obj754.isGraphObjectVisual = True

   if(hasattr(self.obj754, '_setHierarchicalLink')):
     self.obj754._setHierarchicalLink(False)

   # name
   self.obj754.name.setValue('')
   self.obj754.name.setNone()

   self.obj754.GGLabel.setValue(2)
   self.obj754.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(60.0,180.0,self.obj754)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj754.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj754)
   self.obj754.postAction( cobj0.LHS.CREATE )

   self.obj755=GenericGraphEdge(self)
   self.obj755.preAction( cobj0.LHS.CREATE )
   self.obj755.isGraphObjectVisual = True

   if(hasattr(self.obj755, '_setHierarchicalLink')):
     self.obj755._setHierarchicalLink(False)

   self.obj755.GGLabel.setValue(15)
   self.obj755.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(174.5,69.0,self.obj755)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj755.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj755)
   self.obj755.postAction( cobj0.LHS.CREATE )

   self.obj756=GenericGraphEdge(self)
   self.obj756.preAction( cobj0.LHS.CREATE )
   self.obj756.isGraphObjectVisual = True

   if(hasattr(self.obj756, '_setHierarchicalLink')):
     self.obj756._setHierarchicalLink(False)

   self.obj756.GGLabel.setValue(10)
   self.obj756.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(245.75,97.25,self.obj756)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj756.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj756)
   self.obj756.postAction( cobj0.LHS.CREATE )

   self.obj757=GenericGraphEdge(self)
   self.obj757.preAction( cobj0.LHS.CREATE )
   self.obj757.isGraphObjectVisual = True

   if(hasattr(self.obj757, '_setHierarchicalLink')):
     self.obj757._setHierarchicalLink(False)

   self.obj757.GGLabel.setValue(13)
   self.obj757.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(175.0,234.0,self.obj757)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj757.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj757)
   self.obj757.postAction( cobj0.LHS.CREATE )

   self.obj746.out_connections_.append(self.obj750)
   self.obj750.in_connections_.append(self.obj746)
   self.obj746.graphObject_.pendingConnections.append((self.obj746.graphObject_.tag, self.obj750.graphObject_.tag, [264.0, 56.0, 295.0, 49.5, 311.5, 63.25], 2, True))
   self.obj747.out_connections_.append(self.obj751)
   self.obj751.in_connections_.append(self.obj747)
   self.obj747.graphObject_.pendingConnections.append((self.obj747.graphObject_.tag, self.obj751.graphObject_.tag, [306.0, 210.0, 353.5, 220.0, 379.5, 235.25], 2, True))
   self.obj750.out_connections_.append(self.obj748)
   self.obj748.in_connections_.append(self.obj750)
   self.obj750.graphObject_.pendingConnections.append((self.obj750.graphObject_.tag, self.obj748.graphObject_.tag, [330.0, 111.0, 328.0, 77.0, 311.5, 63.25], 2, True))
   self.obj751.out_connections_.append(self.obj749)
   self.obj749.in_connections_.append(self.obj751)
   self.obj751.graphObject_.pendingConnections.append((self.obj751.graphObject_.tag, self.obj749.graphObject_.tag, [410.0, 271.0, 405.5, 250.5, 379.5, 235.25], 2, True))
   self.obj752.out_connections_.append(self.obj754)
   self.obj754.in_connections_.append(self.obj752)
   self.obj752.graphObject_.pendingConnections.append((self.obj752.graphObject_.tag, self.obj754.graphObject_.tag, [84.0, 181.0, 84.5, 131.5], 0, True))
   self.obj753.out_connections_.append(self.obj752)
   self.obj752.in_connections_.append(self.obj753)
   self.obj753.graphObject_.pendingConnections.append((self.obj753.graphObject_.tag, self.obj752.graphObject_.tag, [85.0, 82.0, 84.5, 131.5], 0, True))
   self.obj753.out_connections_.append(self.obj755)
   self.obj755.in_connections_.append(self.obj753)
   self.obj753.graphObject_.pendingConnections.append((self.obj753.graphObject_.tag, self.obj755.graphObject_.tag, [85.0, 82.0, 174.5, 69.0], 0, True))
   self.obj753.out_connections_.append(self.obj756)
   self.obj756.in_connections_.append(self.obj753)
   self.obj753.graphObject_.pendingConnections.append((self.obj753.graphObject_.tag, self.obj756.graphObject_.tag, [85.0, 82.0, 192.0, 90.0, 245.75, 97.25], 2, True))
   self.obj754.out_connections_.append(self.obj757)
   self.obj757.in_connections_.append(self.obj754)
   self.obj754.graphObject_.pendingConnections.append((self.obj754.graphObject_.tag, self.obj757.graphObject_.tag, [84.0, 226.0, 175.0, 234.0], 0, True))
   self.obj755.out_connections_.append(self.obj746)
   self.obj746.in_connections_.append(self.obj755)
   self.obj755.graphObject_.pendingConnections.append((self.obj755.graphObject_.tag, self.obj746.graphObject_.tag, [264.0, 56.0, 174.5, 69.0], 0, True))
   self.obj756.out_connections_.append(self.obj748)
   self.obj748.in_connections_.append(self.obj756)
   self.obj756.graphObject_.pendingConnections.append((self.obj756.graphObject_.tag, self.obj748.graphObject_.tag, [300.0, 111.0, 299.5, 104.5, 245.75, 97.25], 2, True))
   self.obj757.out_connections_.append(self.obj747)
   self.obj747.in_connections_.append(self.obj757)
   self.obj757.graphObject_.pendingConnections.append((self.obj757.graphObject_.tag, self.obj747.graphObject_.tag, [266.0, 242.0, 175.0, 234.0], 0, True))

   cobj0.RHS = ASG_pns(self)
   cobj0.RHS.merge(ASG_omacs(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj761=rawMaterial(self)
   self.obj761.preAction( cobj0.RHS.CREATE )
   self.obj761.isGraphObjectVisual = True

   if(hasattr(self.obj761, '_setHierarchicalLink')):
     self.obj761._setHierarchicalLink(False)

   # MaxFlow
   self.obj761.MaxFlow.setNone()

   # price
   self.obj761.price.setValue(0)

   # Name
   self.obj761.Name.setValue('')
   self.obj761.Name.setNone()

   # ReqFlow
   self.obj761.ReqFlow.setNone()

   self.obj761.GGLabel.setValue(6)
   self.obj761.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(240.0,0.0,self.obj761)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj761.graphObject_ = new_obj
   self.obj7610= AttrCalc()
   self.obj7610.Copy=ATOM3Boolean()
   self.obj7610.Copy.setValue(('Copy from LHS', 1))
   self.obj7610.Copy.config = 0
   self.obj7610.Specify=ATOM3Constraint()
   self.obj7610.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj761.GGset2Any['MaxFlow']= self.obj7610
   self.obj7611= AttrCalc()
   self.obj7611.Copy=ATOM3Boolean()
   self.obj7611.Copy.setValue(('Copy from LHS', 1))
   self.obj7611.Copy.config = 0
   self.obj7611.Specify=ATOM3Constraint()
   self.obj7611.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj761.GGset2Any['Name']= self.obj7611
   self.obj7612= AttrCalc()
   self.obj7612.Copy=ATOM3Boolean()
   self.obj7612.Copy.setValue(('Copy from LHS', 1))
   self.obj7612.Copy.config = 0
   self.obj7612.Specify=ATOM3Constraint()
   self.obj7612.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj761.GGset2Any['ReqFlow']= self.obj7612

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj761)
   self.obj761.postAction( cobj0.RHS.CREATE )

   self.obj762=metarial(self)
   self.obj762.preAction( cobj0.RHS.CREATE )
   self.obj762.isGraphObjectVisual = True

   if(hasattr(self.obj762, '_setHierarchicalLink')):
     self.obj762._setHierarchicalLink(False)

   # MaxFlow
   self.obj762.MaxFlow.setNone()

   # price
   self.obj762.price.setValue(0)

   # Name
   self.obj762.Name.setValue('')
   self.obj762.Name.setNone()

   # ReqFlow
   self.obj762.ReqFlow.setNone()

   self.obj762.GGLabel.setValue(11)
   self.obj762.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(260.0,200.0,self.obj762)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj762.graphObject_ = new_obj
   self.obj7620= AttrCalc()
   self.obj7620.Copy=ATOM3Boolean()
   self.obj7620.Copy.setValue(('Copy from LHS', 1))
   self.obj7620.Copy.config = 0
   self.obj7620.Specify=ATOM3Constraint()
   self.obj7620.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj762.GGset2Any['MaxFlow']= self.obj7620
   self.obj7621= AttrCalc()
   self.obj7621.Copy=ATOM3Boolean()
   self.obj7621.Copy.setValue(('Copy from LHS', 1))
   self.obj7621.Copy.config = 0
   self.obj7621.Specify=ATOM3Constraint()
   self.obj7621.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj762.GGset2Any['Name']= self.obj7621
   self.obj7622= AttrCalc()
   self.obj7622.Copy=ATOM3Boolean()
   self.obj7622.Copy.setValue(('Copy from LHS', 1))
   self.obj7622.Copy.config = 0
   self.obj7622.Specify=ATOM3Constraint()
   self.obj7622.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj762.GGset2Any['ReqFlow']= self.obj7622

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj762)
   self.obj762.postAction( cobj0.RHS.CREATE )

   self.obj763=operatingUnit(self)
   self.obj763.preAction( cobj0.RHS.CREATE )
   self.obj763.isGraphObjectVisual = True

   if(hasattr(self.obj763, '_setHierarchicalLink')):
     self.obj763._setHierarchicalLink(False)

   # OperCostProp
   self.obj763.OperCostProp.setNone()

   # name
   self.obj763.name.setValue('')
   self.obj763.name.setNone()

   # OperCostFix
   self.obj763.OperCostFix.setNone()

   self.obj763.GGLabel.setValue(7)
   self.obj763.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(280.0,100.0,self.obj763)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj763.graphObject_ = new_obj
   self.obj7630= AttrCalc()
   self.obj7630.Copy=ATOM3Boolean()
   self.obj7630.Copy.setValue(('Copy from LHS', 1))
   self.obj7630.Copy.config = 0
   self.obj7630.Specify=ATOM3Constraint()
   self.obj7630.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj763.GGset2Any['OperCostProp']= self.obj7630
   self.obj7631= AttrCalc()
   self.obj7631.Copy=ATOM3Boolean()
   self.obj7631.Copy.setValue(('Copy from LHS', 1))
   self.obj7631.Copy.config = 0
   self.obj7631.Specify=ATOM3Constraint()
   self.obj7631.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj763.GGset2Any['name']= self.obj7631
   self.obj7632= AttrCalc()
   self.obj7632.Copy=ATOM3Boolean()
   self.obj7632.Copy.setValue(('Copy from LHS', 1))
   self.obj7632.Copy.config = 0
   self.obj7632.Specify=ATOM3Constraint()
   self.obj7632.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj763.GGset2Any['OperCostFix']= self.obj7632

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj763)
   self.obj763.postAction( cobj0.RHS.CREATE )

   self.obj764=operatingUnit(self)
   self.obj764.preAction( cobj0.RHS.CREATE )
   self.obj764.isGraphObjectVisual = True

   if(hasattr(self.obj764, '_setHierarchicalLink')):
     self.obj764._setHierarchicalLink(False)

   # OperCostProp
   self.obj764.OperCostProp.setNone()

   # name
   self.obj764.name.setValue('')
   self.obj764.name.setNone()

   # OperCostFix
   self.obj764.OperCostFix.setNone()

   self.obj764.GGLabel.setValue(12)
   self.obj764.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(360.0,260.0,self.obj764)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj764.graphObject_ = new_obj
   self.obj7640= AttrCalc()
   self.obj7640.Copy=ATOM3Boolean()
   self.obj7640.Copy.setValue(('Copy from LHS', 1))
   self.obj7640.Copy.config = 0
   self.obj7640.Specify=ATOM3Constraint()
   self.obj7640.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj764.GGset2Any['OperCostProp']= self.obj7640
   self.obj7641= AttrCalc()
   self.obj7641.Copy=ATOM3Boolean()
   self.obj7641.Copy.setValue(('Copy from LHS', 1))
   self.obj7641.Copy.config = 0
   self.obj7641.Specify=ATOM3Constraint()
   self.obj7641.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj764.GGset2Any['name']= self.obj7641
   self.obj7642= AttrCalc()
   self.obj7642.Copy=ATOM3Boolean()
   self.obj7642.Copy.setValue(('Copy from LHS', 1))
   self.obj7642.Copy.config = 0
   self.obj7642.Specify=ATOM3Constraint()
   self.obj7642.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj764.GGset2Any['OperCostFix']= self.obj7642

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj764)
   self.obj764.postAction( cobj0.RHS.CREATE )

   self.obj765=fromRaw(self)
   self.obj765.preAction( cobj0.RHS.CREATE )
   self.obj765.isGraphObjectVisual = True

   if(hasattr(self.obj765, '_setHierarchicalLink')):
     self.obj765._setHierarchicalLink(False)

   # rate
   self.obj765.rate.setNone()

   self.obj765.GGLabel.setValue(8)
   self.obj765.graphClass_= graph_fromRaw
   if self.genGraphics:
      new_obj = graph_fromRaw(311.5,63.25,self.obj765)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj765.graphObject_ = new_obj
   self.obj7650= AttrCalc()
   self.obj7650.Copy=ATOM3Boolean()
   self.obj7650.Copy.setValue(('Copy from LHS', 1))
   self.obj7650.Copy.config = 0
   self.obj7650.Specify=ATOM3Constraint()
   self.obj7650.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj765.GGset2Any['rate']= self.obj7650

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj765)
   self.obj765.postAction( cobj0.RHS.CREATE )

   self.obj766=intoMaterial(self)
   self.obj766.preAction( cobj0.RHS.CREATE )
   self.obj766.isGraphObjectVisual = True

   if(hasattr(self.obj766, '_setHierarchicalLink')):
     self.obj766._setHierarchicalLink(False)

   # rate
   self.obj766.rate.setValue(0.0)

   self.obj766.GGLabel.setValue(17)
   self.obj766.graphClass_= graph_intoMaterial
   if self.genGraphics:
      new_obj = graph_intoMaterial(324.25,167.5,self.obj766)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj766.graphObject_ = new_obj
   self.obj7660= AttrCalc()
   self.obj7660.Copy=ATOM3Boolean()
   self.obj7660.Copy.setValue(('Copy from LHS', 0))
   self.obj7660.Copy.config = 0
   self.obj7660.Specify=ATOM3Constraint()
   self.obj7660.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'a = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) ).name.getValue()\nb = self.getMatched ( graphID , self.LHS.nodeWithLabel(2) ).name.getValue()\nreturn self.graphRewritingSystem.Dictag[ a ][b]\n\n'))
   self.obj766.GGset2Any['rate']= self.obj7660

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj766)
   self.obj766.postAction( cobj0.RHS.CREATE )

   self.obj767=fromMaterial(self)
   self.obj767.preAction( cobj0.RHS.CREATE )
   self.obj767.isGraphObjectVisual = True

   if(hasattr(self.obj767, '_setHierarchicalLink')):
     self.obj767._setHierarchicalLink(False)

   # rate
   self.obj767.rate.setNone()

   self.obj767.GGLabel.setValue(14)
   self.obj767.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(379.5,235.25,self.obj767)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj767.graphObject_ = new_obj
   self.obj7670= AttrCalc()
   self.obj7670.Copy=ATOM3Boolean()
   self.obj7670.Copy.setValue(('Copy from LHS', 1))
   self.obj7670.Copy.config = 0
   self.obj7670.Specify=ATOM3Constraint()
   self.obj7670.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj767.GGset2Any['rate']= self.obj7670

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj767)
   self.obj767.postAction( cobj0.RHS.CREATE )

   self.obj768=CapableOf(self)
   self.obj768.preAction( cobj0.RHS.CREATE )
   self.obj768.isGraphObjectVisual = True

   if(hasattr(self.obj768, '_setHierarchicalLink')):
     self.obj768._setHierarchicalLink(False)

   # rate
   self.obj768.rate.setNone()

   self.obj768.GGLabel.setValue(3)
   self.obj768.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(84.5,131.5,self.obj768)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj768.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj768)
   self.obj768.postAction( cobj0.RHS.CREATE )

   self.obj769=Agent(self)
   self.obj769.preAction( cobj0.RHS.CREATE )
   self.obj769.isGraphObjectVisual = True

   if(hasattr(self.obj769, '_setHierarchicalLink')):
     self.obj769._setHierarchicalLink(False)

   # price
   self.obj769.price.setNone()

   # name
   self.obj769.name.setValue('')
   self.obj769.name.setNone()

   self.obj769.GGLabel.setValue(1)
   self.obj769.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(60.0,20.0,self.obj769)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj769.graphObject_ = new_obj
   self.obj7690= AttrCalc()
   self.obj7690.Copy=ATOM3Boolean()
   self.obj7690.Copy.setValue(('Copy from LHS', 1))
   self.obj7690.Copy.config = 0
   self.obj7690.Specify=ATOM3Constraint()
   self.obj7690.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj769.GGset2Any['price']= self.obj7690
   self.obj7691= AttrCalc()
   self.obj7691.Copy=ATOM3Boolean()
   self.obj7691.Copy.setValue(('Copy from LHS', 1))
   self.obj7691.Copy.config = 0
   self.obj7691.Specify=ATOM3Constraint()
   self.obj7691.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj769.GGset2Any['name']= self.obj7691

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj769)
   self.obj769.postAction( cobj0.RHS.CREATE )

   self.obj770=Role(self)
   self.obj770.preAction( cobj0.RHS.CREATE )
   self.obj770.isGraphObjectVisual = True

   if(hasattr(self.obj770, '_setHierarchicalLink')):
     self.obj770._setHierarchicalLink(False)

   # name
   self.obj770.name.setValue('')
   self.obj770.name.setNone()

   self.obj770.GGLabel.setValue(2)
   self.obj770.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(60.0,180.0,self.obj770)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj770.graphObject_ = new_obj
   self.obj7700= AttrCalc()
   self.obj7700.Copy=ATOM3Boolean()
   self.obj7700.Copy.setValue(('Copy from LHS', 1))
   self.obj7700.Copy.config = 0
   self.obj7700.Specify=ATOM3Constraint()
   self.obj7700.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj770.GGset2Any['name']= self.obj7700

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj770)
   self.obj770.postAction( cobj0.RHS.CREATE )

   self.obj771=GenericGraphEdge(self)
   self.obj771.preAction( cobj0.RHS.CREATE )
   self.obj771.isGraphObjectVisual = True

   if(hasattr(self.obj771, '_setHierarchicalLink')):
     self.obj771._setHierarchicalLink(False)

   self.obj771.GGLabel.setValue(15)
   self.obj771.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(174.5,69.0,self.obj771)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj771.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj771)
   self.obj771.postAction( cobj0.RHS.CREATE )

   self.obj772=GenericGraphEdge(self)
   self.obj772.preAction( cobj0.RHS.CREATE )
   self.obj772.isGraphObjectVisual = True

   if(hasattr(self.obj772, '_setHierarchicalLink')):
     self.obj772._setHierarchicalLink(False)

   self.obj772.GGLabel.setValue(10)
   self.obj772.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(245.75,97.25,self.obj772)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj772.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj772)
   self.obj772.postAction( cobj0.RHS.CREATE )

   self.obj773=GenericGraphEdge(self)
   self.obj773.preAction( cobj0.RHS.CREATE )
   self.obj773.isGraphObjectVisual = True

   if(hasattr(self.obj773, '_setHierarchicalLink')):
     self.obj773._setHierarchicalLink(False)

   self.obj773.GGLabel.setValue(13)
   self.obj773.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(175.0,234.0,self.obj773)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj773.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj773)
   self.obj773.postAction( cobj0.RHS.CREATE )

   self.obj761.out_connections_.append(self.obj765)
   self.obj765.in_connections_.append(self.obj761)
   self.obj761.graphObject_.pendingConnections.append((self.obj761.graphObject_.tag, self.obj765.graphObject_.tag, [264.0, 50.0, 311.5, 63.25], 2, 0))
   self.obj762.out_connections_.append(self.obj767)
   self.obj767.in_connections_.append(self.obj762)
   self.obj762.graphObject_.pendingConnections.append((self.obj762.graphObject_.tag, self.obj767.graphObject_.tag, [306.0, 210.0, 379.5, 235.25], 2, 0))
   self.obj763.out_connections_.append(self.obj766)
   self.obj766.in_connections_.append(self.obj763)
   self.obj763.graphObject_.pendingConnections.append((self.obj763.graphObject_.tag, self.obj766.graphObject_.tag, [333.0, 108.0, 331.0, 142.0, 324.25, 167.5], 2, True))
   self.obj765.out_connections_.append(self.obj763)
   self.obj763.in_connections_.append(self.obj765)
   self.obj765.graphObject_.pendingConnections.append((self.obj765.graphObject_.tag, self.obj763.graphObject_.tag, [330.0, 101.0, 311.5, 63.25], 2, 0))
   self.obj766.out_connections_.append(self.obj762)
   self.obj762.in_connections_.append(self.obj766)
   self.obj766.graphObject_.pendingConnections.append((self.obj766.graphObject_.tag, self.obj762.graphObject_.tag, [306.0, 210.0, 317.5, 193.0, 324.25, 167.5], 2, True))
   self.obj767.out_connections_.append(self.obj764)
   self.obj764.in_connections_.append(self.obj767)
   self.obj767.graphObject_.pendingConnections.append((self.obj767.graphObject_.tag, self.obj764.graphObject_.tag, [413.0, 268.0, 379.5, 235.25], 2, 0))
   self.obj768.out_connections_.append(self.obj770)
   self.obj770.in_connections_.append(self.obj768)
   self.obj768.graphObject_.pendingConnections.append((self.obj768.graphObject_.tag, self.obj770.graphObject_.tag, [91.0, 180.0, 84.5, 131.5], 2, 0))
   self.obj769.out_connections_.append(self.obj768)
   self.obj768.in_connections_.append(self.obj769)
   self.obj769.graphObject_.pendingConnections.append((self.obj769.graphObject_.tag, self.obj768.graphObject_.tag, [97.0, 82.0, 84.5, 131.5], 2, 0))
   self.obj769.out_connections_.append(self.obj771)
   self.obj771.in_connections_.append(self.obj769)
   self.obj769.graphObject_.pendingConnections.append((self.obj769.graphObject_.tag, self.obj771.graphObject_.tag, [97.0, 82.0, 174.5, 69.0], 2, 0))
   self.obj769.out_connections_.append(self.obj772)
   self.obj772.in_connections_.append(self.obj769)
   self.obj769.graphObject_.pendingConnections.append((self.obj769.graphObject_.tag, self.obj772.graphObject_.tag, [97.0, 82.0, 245.75, 97.25], 2, 0))
   self.obj770.out_connections_.append(self.obj773)
   self.obj773.in_connections_.append(self.obj770)
   self.obj770.graphObject_.pendingConnections.append((self.obj770.graphObject_.tag, self.obj773.graphObject_.tag, [91.0, 225.0, 175.0, 234.0], 2, 0))
   self.obj771.out_connections_.append(self.obj761)
   self.obj761.in_connections_.append(self.obj771)
   self.obj771.graphObject_.pendingConnections.append((self.obj771.graphObject_.tag, self.obj761.graphObject_.tag, [264.0, 50.0, 174.5, 69.0], 2, 0))
   self.obj772.out_connections_.append(self.obj763)
   self.obj763.in_connections_.append(self.obj772)
   self.obj772.graphObject_.pendingConnections.append((self.obj772.graphObject_.tag, self.obj763.graphObject_.tag, [300.0, 101.0, 245.75, 97.25], 2, 0))
   self.obj773.out_connections_.append(self.obj762)
   self.obj762.in_connections_.append(self.obj773)
   self.obj773.graphObject_.pendingConnections.append((self.obj773.graphObject_.tag, self.obj762.graphObject_.tag, [266.0, 242.0, 175.0, 234.0], 2, 0))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'print \'Rule 21 \'\nnode7 = self.getMatched(graphID, self.LHS.nodeWithLabel(7))\n\nnode11 = self.getMatched(graphID, self.LHS.nodeWithLabel(11))\nnode1 = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\n\nprint node7.name.getValue()+\' in \'+ node11.Name.getValue() \nprint node7.name.getValue() in  node11.Name.getValue()\n\n\ntest = not ( hasattr(node11, "linkAux2") and hasattr(node7, "linkAux2") )\nprint test\nif test : \n return (node7.name.getValue() in node11.Name.getValue() )\nelse : \n return False\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# code action of rule\nnode = self.getMatched ( graphID , self.LHS.nodeWithLabel(7) )\nnode.linkAux2 = True \nnode = self.getMatched ( graphID , self.LHS.nodeWithLabel(11) )\nnode.linkAux2 = True \nself.graphRewritingSystem.finalStat = 21\n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('AssignPrice4Raw', 20)
   cobj0.Order=ATOM3Integer(22)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

   from Capabilitie import *
   from rawMaterial import *
   from GenericGraphEdge import *
   from Goal import *
   from ASG_pns import *
   from operatingUnit import *
   from metarial import *
   from GenericGraphNode import *
   from product import *
   from Agent import *
   from fromMaterial import *
   from CapableOf import *
   from intoProduct import *
   from Role import *
   from fromRaw import *
   from intoMaterial import *
   from ASG_GenericGraph import *
   from ASG_omacs import *
   from require import *
   from achieve import *
   from posses import *

   cobj0.LHS = ASG_pns(self)
   cobj0.LHS.merge(ASG_omacs(self))
   cobj0.LHS.merge(ASG_GenericGraph(self))

   self.obj780=rawMaterial(self)
   self.obj780.preAction( cobj0.LHS.CREATE )
   self.obj780.isGraphObjectVisual = True

   if(hasattr(self.obj780, '_setHierarchicalLink')):
     self.obj780._setHierarchicalLink(False)

   # MaxFlow
   self.obj780.MaxFlow.setNone()

   # price
   self.obj780.price.setNone()

   # Name
   self.obj780.Name.setValue('')
   self.obj780.Name.setNone()

   # ReqFlow
   self.obj780.ReqFlow.setNone()

   self.obj780.GGLabel.setValue(1)
   self.obj780.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(280.0,60.0,self.obj780)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['Text Scale'] = 0.5
      new_obj.layConstraints['scale'] = [0.5, 0.5]
   else: new_obj = None
   self.obj780.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj780)
   self.obj780.postAction( cobj0.LHS.CREATE )

   self.obj781=Agent(self)
   self.obj781.preAction( cobj0.LHS.CREATE )
   self.obj781.isGraphObjectVisual = True

   if(hasattr(self.obj781, '_setHierarchicalLink')):
     self.obj781._setHierarchicalLink(False)

   # price
   self.obj781.price.setNone()

   # name
   self.obj781.name.setValue('')
   self.obj781.name.setNone()

   self.obj781.GGLabel.setValue(2)
   self.obj781.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(120.0,60.0,self.obj781)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['Text Scale'] = 0.5
      new_obj.layConstraints['scale'] = [0.5, 0.5]
   else: new_obj = None
   self.obj781.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj781)
   self.obj781.postAction( cobj0.LHS.CREATE )

   self.obj782=GenericGraphEdge(self)
   self.obj782.preAction( cobj0.LHS.CREATE )
   self.obj782.isGraphObjectVisual = True

   if(hasattr(self.obj782, '_setHierarchicalLink')):
     self.obj782._setHierarchicalLink(False)

   self.obj782.GGLabel.setValue(3)
   self.obj782.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(198.5,126.5,self.obj782)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj782.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj782)
   self.obj782.postAction( cobj0.LHS.CREATE )

   self.obj781.out_connections_.append(self.obj782)
   self.obj782.in_connections_.append(self.obj781)
   self.obj781.graphObject_.pendingConnections.append((self.obj781.graphObject_.tag, self.obj782.graphObject_.tag, [105.0, 89.5, 130.0, 127.0, 198.5, 126.5], 2, True))
   self.obj782.out_connections_.append(self.obj780)
   self.obj780.in_connections_.append(self.obj782)
   self.obj782.graphObject_.pendingConnections.append((self.obj782.graphObject_.tag, self.obj780.graphObject_.tag, [290.5, 89.5, 267.0, 126.0, 198.5, 126.5], 2, True))

   cobj0.RHS = ASG_pns(self)
   cobj0.RHS.merge(ASG_omacs(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj786=rawMaterial(self)
   self.obj786.preAction( cobj0.RHS.CREATE )
   self.obj786.isGraphObjectVisual = True

   if(hasattr(self.obj786, '_setHierarchicalLink')):
     self.obj786._setHierarchicalLink(False)

   # MaxFlow
   self.obj786.MaxFlow.setNone()

   # price
   self.obj786.price.setNone()

   # Name
   self.obj786.Name.setValue('')
   self.obj786.Name.setNone()

   # ReqFlow
   self.obj786.ReqFlow.setNone()

   self.obj786.GGLabel.setValue(1)
   self.obj786.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(280.0,60.0,self.obj786)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj786.graphObject_ = new_obj
   self.obj7860= AttrCalc()
   self.obj7860.Copy=ATOM3Boolean()
   self.obj7860.Copy.setValue(('Copy from LHS', 1))
   self.obj7860.Copy.config = 0
   self.obj7860.Specify=ATOM3Constraint()
   self.obj7860.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj786.GGset2Any['MaxFlow']= self.obj7860
   self.obj7861= AttrCalc()
   self.obj7861.Copy=ATOM3Boolean()
   self.obj7861.Copy.setValue(('Copy from LHS', 0))
   self.obj7861.Copy.config = 0
   self.obj7861.Specify=ATOM3Constraint()
   self.obj7861.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(2)).price.getValue()\n\n\n\n\n\n\n'))
   self.obj786.GGset2Any['price']= self.obj7861
   self.obj7862= AttrCalc()
   self.obj7862.Copy=ATOM3Boolean()
   self.obj7862.Copy.setValue(('Copy from LHS', 1))
   self.obj7862.Copy.config = 0
   self.obj7862.Specify=ATOM3Constraint()
   self.obj7862.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj786.GGset2Any['Name']= self.obj7862
   self.obj7863= AttrCalc()
   self.obj7863.Copy=ATOM3Boolean()
   self.obj7863.Copy.setValue(('Copy from LHS', 1))
   self.obj7863.Copy.config = 0
   self.obj7863.Specify=ATOM3Constraint()
   self.obj7863.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj786.GGset2Any['ReqFlow']= self.obj7863

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj786)
   self.obj786.postAction( cobj0.RHS.CREATE )

   self.obj787=Agent(self)
   self.obj787.preAction( cobj0.RHS.CREATE )
   self.obj787.isGraphObjectVisual = True

   if(hasattr(self.obj787, '_setHierarchicalLink')):
     self.obj787._setHierarchicalLink(False)

   # price
   self.obj787.price.setNone()

   # name
   self.obj787.name.setValue('')
   self.obj787.name.setNone()

   self.obj787.GGLabel.setValue(2)
   self.obj787.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(120.0,60.0,self.obj787)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj787.graphObject_ = new_obj
   self.obj7870= AttrCalc()
   self.obj7870.Copy=ATOM3Boolean()
   self.obj7870.Copy.setValue(('Copy from LHS', 1))
   self.obj7870.Copy.config = 0
   self.obj7870.Specify=ATOM3Constraint()
   self.obj7870.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj787.GGset2Any['price']= self.obj7870
   self.obj7871= AttrCalc()
   self.obj7871.Copy=ATOM3Boolean()
   self.obj7871.Copy.setValue(('Copy from LHS', 1))
   self.obj7871.Copy.config = 0
   self.obj7871.Specify=ATOM3Constraint()
   self.obj7871.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj787.GGset2Any['name']= self.obj7871

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj787)
   self.obj787.postAction( cobj0.RHS.CREATE )

   self.obj788=GenericGraphEdge(self)
   self.obj788.preAction( cobj0.RHS.CREATE )
   self.obj788.isGraphObjectVisual = True

   if(hasattr(self.obj788, '_setHierarchicalLink')):
     self.obj788._setHierarchicalLink(False)

   self.obj788.GGLabel.setValue(3)
   self.obj788.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(198.5,126.5,self.obj788)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj788.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj788)
   self.obj788.postAction( cobj0.RHS.CREATE )

   self.obj787.out_connections_.append(self.obj788)
   self.obj788.in_connections_.append(self.obj787)
   self.obj787.graphObject_.pendingConnections.append((self.obj787.graphObject_.tag, self.obj788.graphObject_.tag, [157.0, 122.0, 198.5, 126.5], 2, 0))
   self.obj788.out_connections_.append(self.obj786)
   self.obj786.in_connections_.append(self.obj788)
   self.obj788.graphObject_.pendingConnections.append((self.obj788.graphObject_.tag, self.obj786.graphObject_.tag, [304.0, 110.0, 198.5, 126.5], 2, 0))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\nraw = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nreturn not ( hasattr(raw, "AssignPrice" ) )\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'raw = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nraw.AssignPrice=True\nprint \'######################## Assign Price for \'+raw.Name.getValue()\n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('AssignCost4AR', 20)
   cobj0.Order=ATOM3Integer(23)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

   from Capabilitie import *
   from rawMaterial import *
   from GenericGraphEdge import *
   from Goal import *
   from ASG_pns import *
   from operatingUnit import *
   from metarial import *
   from GenericGraphNode import *
   from product import *
   from Agent import *
   from fromMaterial import *
   from CapableOf import *
   from intoProduct import *
   from Role import *
   from fromRaw import *
   from intoMaterial import *
   from ASG_GenericGraph import *
   from ASG_omacs import *
   from require import *
   from achieve import *
   from posses import *

   cobj0.LHS = ASG_pns(self)
   cobj0.LHS.merge(ASG_omacs(self))
   cobj0.LHS.merge(ASG_GenericGraph(self))

   self.obj795=operatingUnit(self)
   self.obj795.preAction( cobj0.LHS.CREATE )
   self.obj795.isGraphObjectVisual = True

   if(hasattr(self.obj795, '_setHierarchicalLink')):
     self.obj795._setHierarchicalLink(False)

   # OperCostProp
   self.obj795.OperCostProp.setNone()

   # name
   self.obj795.name.setValue('')
   self.obj795.name.setNone()

   # OperCostFix
   self.obj795.OperCostFix.setNone()

   self.obj795.GGLabel.setValue(4)
   self.obj795.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(280.0,120.0,self.obj795)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj795.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj795)
   self.obj795.postAction( cobj0.LHS.CREATE )

   self.obj796=CapableOf(self)
   self.obj796.preAction( cobj0.LHS.CREATE )
   self.obj796.isGraphObjectVisual = True

   if(hasattr(self.obj796, '_setHierarchicalLink')):
     self.obj796._setHierarchicalLink(False)

   # rate
   self.obj796.rate.setNone()

   self.obj796.GGLabel.setValue(5)
   self.obj796.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(160.5,121.5,self.obj796)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj796.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj796)
   self.obj796.postAction( cobj0.LHS.CREATE )

   self.obj797=Agent(self)
   self.obj797.preAction( cobj0.LHS.CREATE )
   self.obj797.isGraphObjectVisual = True

   if(hasattr(self.obj797, '_setHierarchicalLink')):
     self.obj797._setHierarchicalLink(False)

   # price
   self.obj797.price.setNone()

   # name
   self.obj797.name.setValue('')
   self.obj797.name.setNone()

   self.obj797.GGLabel.setValue(1)
   self.obj797.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(120.0,40.0,self.obj797)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj797.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj797)
   self.obj797.postAction( cobj0.LHS.CREATE )

   self.obj798=Role(self)
   self.obj798.preAction( cobj0.LHS.CREATE )
   self.obj798.isGraphObjectVisual = True

   if(hasattr(self.obj798, '_setHierarchicalLink')):
     self.obj798._setHierarchicalLink(False)

   # name
   self.obj798.name.setValue('')
   self.obj798.name.setNone()

   self.obj798.GGLabel.setValue(2)
   self.obj798.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(140.0,140.0,self.obj798)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj798.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj798)
   self.obj798.postAction( cobj0.LHS.CREATE )

   self.obj799=GenericGraphEdge(self)
   self.obj799.preAction( cobj0.LHS.CREATE )
   self.obj799.isGraphObjectVisual = True

   if(hasattr(self.obj799, '_setHierarchicalLink')):
     self.obj799._setHierarchicalLink(False)

   self.obj799.GGLabel.setValue(3)
   self.obj799.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(264.75,85.25,self.obj799)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj799.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj799)
   self.obj799.postAction( cobj0.LHS.CREATE )

   self.obj796.out_connections_.append(self.obj798)
   self.obj798.in_connections_.append(self.obj796)
   self.obj796.graphObject_.pendingConnections.append((self.obj796.graphObject_.tag, self.obj798.graphObject_.tag, [164.0, 141.0, 160.5, 121.5], 0, True))
   self.obj797.out_connections_.append(self.obj799)
   self.obj799.in_connections_.append(self.obj797)
   self.obj797.graphObject_.pendingConnections.append((self.obj797.graphObject_.tag, self.obj799.graphObject_.tag, [145.0, 102.0, 226.0, 83.0, 264.75, 85.25], 2, True))
   self.obj797.out_connections_.append(self.obj796)
   self.obj796.in_connections_.append(self.obj797)
   self.obj797.graphObject_.pendingConnections.append((self.obj797.graphObject_.tag, self.obj796.graphObject_.tag, [157.0, 102.0, 160.5, 121.5], 0, True))
   self.obj799.out_connections_.append(self.obj795)
   self.obj795.in_connections_.append(self.obj799)
   self.obj799.graphObject_.pendingConnections.append((self.obj799.graphObject_.tag, self.obj795.graphObject_.tag, [300.0, 121.0, 264.75, 85.25], 2, 0))

   cobj0.RHS = ASG_pns(self)
   cobj0.RHS.merge(ASG_omacs(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj803=operatingUnit(self)
   self.obj803.preAction( cobj0.RHS.CREATE )
   self.obj803.isGraphObjectVisual = True

   if(hasattr(self.obj803, '_setHierarchicalLink')):
     self.obj803._setHierarchicalLink(False)

   # OperCostProp
   self.obj803.OperCostProp.setNone()

   # name
   self.obj803.name.setValue('')
   self.obj803.name.setNone()

   # OperCostFix
   self.obj803.OperCostFix.setNone()

   self.obj803.GGLabel.setValue(4)
   self.obj803.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(280.0,120.0,self.obj803)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj803.graphObject_ = new_obj
   self.obj8030= AttrCalc()
   self.obj8030.Copy=ATOM3Boolean()
   self.obj8030.Copy.setValue(('Copy from LHS', 0))
   self.obj8030.Copy.config = 0
   self.obj8030.Specify=ATOM3Constraint()
   self.obj8030.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'a = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) ).name.getValue()\nb = self.getMatched ( graphID , self.LHS.nodeWithLabel(2) ).name.getValue()\nreturn self.graphRewritingSystem.Dictag[ a ][b]\n\n'))
   self.obj803.GGset2Any['OperCostProp']= self.obj8030
   self.obj8031= AttrCalc()
   self.obj8031.Copy=ATOM3Boolean()
   self.obj8031.Copy.setValue(('Copy from LHS', 1))
   self.obj8031.Copy.config = 0
   self.obj8031.Specify=ATOM3Constraint()
   self.obj8031.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj803.GGset2Any['name']= self.obj8031
   self.obj8032= AttrCalc()
   self.obj8032.Copy=ATOM3Boolean()
   self.obj8032.Copy.setValue(('Copy from LHS', 0))
   self.obj8032.Copy.config = 0
   self.obj8032.Specify=ATOM3Constraint()
   self.obj8032.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj803.GGset2Any['OperCostFix']= self.obj8032

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj803)
   self.obj803.postAction( cobj0.RHS.CREATE )

   self.obj804=CapableOf(self)
   self.obj804.preAction( cobj0.RHS.CREATE )
   self.obj804.isGraphObjectVisual = True

   if(hasattr(self.obj804, '_setHierarchicalLink')):
     self.obj804._setHierarchicalLink(False)

   # rate
   self.obj804.rate.setNone()

   self.obj804.GGLabel.setValue(5)
   self.obj804.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(160.5,121.5,self.obj804)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj804.graphObject_ = new_obj
   self.obj8040= AttrCalc()
   self.obj8040.Copy=ATOM3Boolean()
   self.obj8040.Copy.setValue(('Copy from LHS', 1))
   self.obj8040.Copy.config = 0
   self.obj8040.Specify=ATOM3Constraint()
   self.obj8040.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj804.GGset2Any['rate']= self.obj8040

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj804)
   self.obj804.postAction( cobj0.RHS.CREATE )

   self.obj805=Agent(self)
   self.obj805.preAction( cobj0.RHS.CREATE )
   self.obj805.isGraphObjectVisual = True

   if(hasattr(self.obj805, '_setHierarchicalLink')):
     self.obj805._setHierarchicalLink(False)

   # price
   self.obj805.price.setNone()

   # name
   self.obj805.name.setValue('')
   self.obj805.name.setNone()

   self.obj805.GGLabel.setValue(1)
   self.obj805.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(120.0,40.0,self.obj805)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj805.graphObject_ = new_obj
   self.obj8050= AttrCalc()
   self.obj8050.Copy=ATOM3Boolean()
   self.obj8050.Copy.setValue(('Copy from LHS', 1))
   self.obj8050.Copy.config = 0
   self.obj8050.Specify=ATOM3Constraint()
   self.obj8050.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj805.GGset2Any['price']= self.obj8050
   self.obj8051= AttrCalc()
   self.obj8051.Copy=ATOM3Boolean()
   self.obj8051.Copy.setValue(('Copy from LHS', 1))
   self.obj8051.Copy.config = 0
   self.obj8051.Specify=ATOM3Constraint()
   self.obj8051.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj805.GGset2Any['name']= self.obj8051

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj805)
   self.obj805.postAction( cobj0.RHS.CREATE )

   self.obj806=Role(self)
   self.obj806.preAction( cobj0.RHS.CREATE )
   self.obj806.isGraphObjectVisual = True

   if(hasattr(self.obj806, '_setHierarchicalLink')):
     self.obj806._setHierarchicalLink(False)

   # name
   self.obj806.name.setValue('')
   self.obj806.name.setNone()

   self.obj806.GGLabel.setValue(2)
   self.obj806.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(140.0,140.0,self.obj806)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj806.graphObject_ = new_obj
   self.obj8060= AttrCalc()
   self.obj8060.Copy=ATOM3Boolean()
   self.obj8060.Copy.setValue(('Copy from LHS', 1))
   self.obj8060.Copy.config = 0
   self.obj8060.Specify=ATOM3Constraint()
   self.obj8060.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj806.GGset2Any['name']= self.obj8060

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj806)
   self.obj806.postAction( cobj0.RHS.CREATE )

   self.obj807=GenericGraphEdge(self)
   self.obj807.preAction( cobj0.RHS.CREATE )
   self.obj807.isGraphObjectVisual = True

   if(hasattr(self.obj807, '_setHierarchicalLink')):
     self.obj807._setHierarchicalLink(False)

   self.obj807.GGLabel.setValue(3)
   self.obj807.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(264.75,85.25,self.obj807)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj807.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj807)
   self.obj807.postAction( cobj0.RHS.CREATE )

   self.obj804.out_connections_.append(self.obj806)
   self.obj806.in_connections_.append(self.obj804)
   self.obj804.graphObject_.pendingConnections.append((self.obj804.graphObject_.tag, self.obj806.graphObject_.tag, [171.0, 140.0, 160.5, 121.5], 2, 0))
   self.obj805.out_connections_.append(self.obj807)
   self.obj807.in_connections_.append(self.obj805)
   self.obj805.graphObject_.pendingConnections.append((self.obj805.graphObject_.tag, self.obj807.graphObject_.tag, [157.0, 102.0, 264.75, 85.25], 2, 0))
   self.obj805.out_connections_.append(self.obj804)
   self.obj804.in_connections_.append(self.obj805)
   self.obj805.graphObject_.pendingConnections.append((self.obj805.graphObject_.tag, self.obj804.graphObject_.tag, [157.0, 102.0, 160.5, 121.5], 2, 0))
   self.obj807.out_connections_.append(self.obj803)
   self.obj803.in_connections_.append(self.obj807)
   self.obj807.graphObject_.pendingConnections.append((self.obj807.graphObject_.tag, self.obj803.graphObject_.tag, [300.0, 121.0, 264.75, 85.25], 2, 0))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'AR = self.getMatched(graphID, self.LHS.nodeWithLabel(4))\nreturn not ( hasattr(AR, "AssignCost" ) )\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'AR = self.getMatched(graphID, self.LHS.nodeWithLabel(4))\nAR.AssignCost=True\nprint \'######################## Assign Cost for \'+AR.name.getValue()\n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('RemoveGoal', 20)
   cobj0.Order=ATOM3Integer(25)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

   from Capabilitie import *
   from rawMaterial import *
   from GenericGraphEdge import *
   from Goal import *
   from ASG_pns import *
   from operatingUnit import *
   from metarial import *
   from GenericGraphNode import *
   from product import *
   from Agent import *
   from fromMaterial import *
   from CapableOf import *
   from intoProduct import *
   from Role import *
   from fromRaw import *
   from intoMaterial import *
   from ASG_GenericGraph import *
   from ASG_omacs import *
   from require import *
   from achieve import *
   from posses import *

   cobj0.LHS = ASG_pns(self)
   cobj0.LHS.merge(ASG_omacs(self))
   cobj0.LHS.merge(ASG_GenericGraph(self))

   self.obj814=metarial(self)
   self.obj814.preAction( cobj0.LHS.CREATE )
   self.obj814.isGraphObjectVisual = True

   if(hasattr(self.obj814, '_setHierarchicalLink')):
     self.obj814._setHierarchicalLink(False)

   # MaxFlow
   self.obj814.MaxFlow.setNone()

   # price
   self.obj814.price.setValue(0)

   # Name
   self.obj814.Name.setValue('')
   self.obj814.Name.setNone()

   # ReqFlow
   self.obj814.ReqFlow.setNone()

   self.obj814.GGLabel.setValue(1)
   self.obj814.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(280.0,60.0,self.obj814)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj814.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj814)
   self.obj814.postAction( cobj0.LHS.CREATE )

   self.obj815=Goal(self)
   self.obj815.preAction( cobj0.LHS.CREATE )
   self.obj815.isGraphObjectVisual = True

   if(hasattr(self.obj815, '_setHierarchicalLink')):
     self.obj815._setHierarchicalLink(False)

   # name
   self.obj815.name.setValue('')
   self.obj815.name.setNone()

   self.obj815.GGLabel.setValue(3)
   self.obj815.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(100.0,60.0,self.obj815)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj815.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj815)
   self.obj815.postAction( cobj0.LHS.CREATE )

   self.obj816=GenericGraphEdge(self)
   self.obj816.preAction( cobj0.LHS.CREATE )
   self.obj816.isGraphObjectVisual = True

   if(hasattr(self.obj816, '_setHierarchicalLink')):
     self.obj816._setHierarchicalLink(False)

   self.obj816.GGLabel.setValue(4)
   self.obj816.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(205.0,106.0,self.obj816)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj816.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj816)
   self.obj816.postAction( cobj0.LHS.CREATE )

   self.obj815.out_connections_.append(self.obj816)
   self.obj816.in_connections_.append(self.obj815)
   self.obj815.graphObject_.pendingConnections.append((self.obj815.graphObject_.tag, self.obj816.graphObject_.tag, [124.0, 110.0, 205.0, 106.0], 0, True))
   self.obj816.out_connections_.append(self.obj814)
   self.obj814.in_connections_.append(self.obj816)
   self.obj816.graphObject_.pendingConnections.append((self.obj816.graphObject_.tag, self.obj814.graphObject_.tag, [286.0, 102.0, 205.0, 106.0], 0, True))

   cobj0.RHS = ASG_pns(self)

   self.obj818=metarial(self)
   self.obj818.preAction( cobj0.RHS.CREATE )
   self.obj818.isGraphObjectVisual = True

   if(hasattr(self.obj818, '_setHierarchicalLink')):
     self.obj818._setHierarchicalLink(False)

   # MaxFlow
   self.obj818.MaxFlow.setNone()

   # price
   self.obj818.price.setValue(0)

   # Name
   self.obj818.Name.setValue('')
   self.obj818.Name.setNone()

   # ReqFlow
   self.obj818.ReqFlow.setNone()

   self.obj818.GGLabel.setValue(1)
   self.obj818.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(180.0,40.0,self.obj818)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj818.graphObject_ = new_obj
   self.obj8180= AttrCalc()
   self.obj8180.Copy=ATOM3Boolean()
   self.obj8180.Copy.setValue(('Copy from LHS', 1))
   self.obj8180.Copy.config = 0
   self.obj8180.Specify=ATOM3Constraint()
   self.obj8180.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj818.GGset2Any['MaxFlow']= self.obj8180
   self.obj8181= AttrCalc()
   self.obj8181.Copy=ATOM3Boolean()
   self.obj8181.Copy.setValue(('Copy from LHS', 1))
   self.obj8181.Copy.config = 0
   self.obj8181.Specify=ATOM3Constraint()
   self.obj8181.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj818.GGset2Any['Name']= self.obj8181
   self.obj8182= AttrCalc()
   self.obj8182.Copy=ATOM3Boolean()
   self.obj8182.Copy.setValue(('Copy from LHS', 1))
   self.obj8182.Copy.config = 0
   self.obj8182.Specify=ATOM3Constraint()
   self.obj8182.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj818.GGset2Any['ReqFlow']= self.obj8182

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj818)
   self.obj818.postAction( cobj0.RHS.CREATE )


   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.graphRewritingSystem.finalStat > 20 \n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# If you want to apply this rule at most once on asingle host graph node, \n# then uncomment the next two lines. Change the default GG label (1) if needed.\n\n# Make sure to enable the CONDITION code as well\n# And to use the same label & unique name in the ACTION\n# WARNING: _uniqueName503 is not guaranteed to be unique (so change it, be safe!)\n\n#node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\n#node._uniqueName503 = True\npass\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('RemoveAgent', 20)
   cobj0.Order=ATOM3Integer(26)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

   from Capabilitie import *
   from rawMaterial import *
   from GenericGraphEdge import *
   from Goal import *
   from ASG_pns import *
   from operatingUnit import *
   from metarial import *
   from GenericGraphNode import *
   from product import *
   from Agent import *
   from fromMaterial import *
   from CapableOf import *
   from intoProduct import *
   from Role import *
   from fromRaw import *
   from intoMaterial import *
   from ASG_GenericGraph import *
   from ASG_omacs import *
   from require import *
   from achieve import *
   from posses import *

   cobj0.LHS = ASG_pns(self)
   cobj0.LHS.merge(ASG_omacs(self))
   cobj0.LHS.merge(ASG_GenericGraph(self))

   self.obj825=rawMaterial(self)
   self.obj825.preAction( cobj0.LHS.CREATE )
   self.obj825.isGraphObjectVisual = True

   if(hasattr(self.obj825, '_setHierarchicalLink')):
     self.obj825._setHierarchicalLink(False)

   # MaxFlow
   self.obj825.MaxFlow.setNone()

   # price
   self.obj825.price.setNone()

   # Name
   self.obj825.Name.setValue('')
   self.obj825.Name.setNone()

   # ReqFlow
   self.obj825.ReqFlow.setNone()

   self.obj825.GGLabel.setValue(2)
   self.obj825.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(260.0,40.0,self.obj825)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj825.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj825)
   self.obj825.postAction( cobj0.LHS.CREATE )

   self.obj826=operatingUnit(self)
   self.obj826.preAction( cobj0.LHS.CREATE )
   self.obj826.isGraphObjectVisual = True

   if(hasattr(self.obj826, '_setHierarchicalLink')):
     self.obj826._setHierarchicalLink(False)

   # OperCostProp
   self.obj826.OperCostProp.setNone()

   # name
   self.obj826.name.setValue('')
   self.obj826.name.setNone()

   # OperCostFix
   self.obj826.OperCostFix.setNone()

   self.obj826.GGLabel.setValue(3)
   self.obj826.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(280.0,140.0,self.obj826)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj826.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj826)
   self.obj826.postAction( cobj0.LHS.CREATE )

   self.obj827=fromRaw(self)
   self.obj827.preAction( cobj0.LHS.CREATE )
   self.obj827.isGraphObjectVisual = True

   if(hasattr(self.obj827, '_setHierarchicalLink')):
     self.obj827._setHierarchicalLink(False)

   # rate
   self.obj827.rate.setNone()

   self.obj827.GGLabel.setValue(5)
   self.obj827.graphClass_= graph_fromRaw
   if self.genGraphics:
      new_obj = graph_fromRaw(292.0,123.5,self.obj827)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj827.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj827)
   self.obj827.postAction( cobj0.LHS.CREATE )

   self.obj828=Agent(self)
   self.obj828.preAction( cobj0.LHS.CREATE )
   self.obj828.isGraphObjectVisual = True

   if(hasattr(self.obj828, '_setHierarchicalLink')):
     self.obj828._setHierarchicalLink(False)

   # price
   self.obj828.price.setNone()

   # name
   self.obj828.name.setValue('')
   self.obj828.name.setNone()

   self.obj828.GGLabel.setValue(1)
   self.obj828.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(60.0,60.0,self.obj828)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj828.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj828)
   self.obj828.postAction( cobj0.LHS.CREATE )

   self.obj829=GenericGraphEdge(self)
   self.obj829.preAction( cobj0.LHS.CREATE )
   self.obj829.isGraphObjectVisual = True

   if(hasattr(self.obj829, '_setHierarchicalLink')):
     self.obj829._setHierarchicalLink(False)

   self.obj829.GGLabel.setValue(4)
   self.obj829.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(184.5,109.0,self.obj829)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj829.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj829)
   self.obj829.postAction( cobj0.LHS.CREATE )

   self.obj830=GenericGraphEdge(self)
   self.obj830.preAction( cobj0.LHS.CREATE )
   self.obj830.isGraphObjectVisual = True

   if(hasattr(self.obj830, '_setHierarchicalLink')):
     self.obj830._setHierarchicalLink(False)

   self.obj830.GGLabel.setValue(6)
   self.obj830.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(159.0,150.5,self.obj830)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj830.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj830)
   self.obj830.postAction( cobj0.LHS.CREATE )

   self.obj825.out_connections_.append(self.obj827)
   self.obj827.in_connections_.append(self.obj825)
   self.obj825.graphObject_.pendingConnections.append((self.obj825.graphObject_.tag, self.obj827.graphObject_.tag, [284.0, 96.0, 292.0, 123.5], 0, True))
   self.obj827.out_connections_.append(self.obj826)
   self.obj826.in_connections_.append(self.obj827)
   self.obj827.graphObject_.pendingConnections.append((self.obj827.graphObject_.tag, self.obj826.graphObject_.tag, [300.0, 151.0, 292.0, 123.5], 0, True))
   self.obj828.out_connections_.append(self.obj829)
   self.obj829.in_connections_.append(self.obj828)
   self.obj828.graphObject_.pendingConnections.append((self.obj828.graphObject_.tag, self.obj829.graphObject_.tag, [85.0, 122.0, 184.5, 109.0], 0, True))
   self.obj828.out_connections_.append(self.obj830)
   self.obj830.in_connections_.append(self.obj828)
   self.obj828.graphObject_.pendingConnections.append((self.obj828.graphObject_.tag, self.obj830.graphObject_.tag, [85.0, 122.0, 105.5, 141.5, 159.0, 150.5], 2, True))
   self.obj829.out_connections_.append(self.obj825)
   self.obj825.in_connections_.append(self.obj829)
   self.obj829.graphObject_.pendingConnections.append((self.obj829.graphObject_.tag, self.obj825.graphObject_.tag, [284.0, 96.0, 184.5, 109.0], 0, True))
   self.obj830.out_connections_.append(self.obj826)
   self.obj826.in_connections_.append(self.obj830)
   self.obj830.graphObject_.pendingConnections.append((self.obj830.graphObject_.tag, self.obj826.graphObject_.tag, [299.0, 158.0, 212.5, 159.5, 159.0, 150.5], 2, True))

   cobj0.RHS = ASG_pns(self)

   self.obj832=rawMaterial(self)
   self.obj832.preAction( cobj0.RHS.CREATE )
   self.obj832.isGraphObjectVisual = True

   if(hasattr(self.obj832, '_setHierarchicalLink')):
     self.obj832._setHierarchicalLink(False)

   # MaxFlow
   self.obj832.MaxFlow.setValue(999999)

   # price
   self.obj832.price.setValue(0)

   # Name
   self.obj832.Name.setValue('')
   self.obj832.Name.setNone()

   # ReqFlow
   self.obj832.ReqFlow.setValue(0)

   self.obj832.GGLabel.setValue(2)
   self.obj832.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(160.0,40.0,self.obj832)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['Text Scale'] = 1.0
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj832.graphObject_ = new_obj
   self.obj8320= AttrCalc()
   self.obj8320.Copy=ATOM3Boolean()
   self.obj8320.Copy.setValue(('Copy from LHS', 1))
   self.obj8320.Copy.config = 0
   self.obj8320.Specify=ATOM3Constraint()
   self.obj8320.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj832.GGset2Any['MaxFlow']= self.obj8320
   self.obj8321= AttrCalc()
   self.obj8321.Copy=ATOM3Boolean()
   self.obj8321.Copy.setValue(('Copy from LHS', 0))
   self.obj8321.Copy.config = 0
   self.obj8321.Specify=ATOM3Constraint()
   self.obj8321.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).price.getValue()\n'))
   self.obj832.GGset2Any['price']= self.obj8321
   self.obj8322= AttrCalc()
   self.obj8322.Copy=ATOM3Boolean()
   self.obj8322.Copy.setValue(('Copy from LHS', 1))
   self.obj8322.Copy.config = 0
   self.obj8322.Specify=ATOM3Constraint()
   self.obj8322.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj832.GGset2Any['Name']= self.obj8322
   self.obj8323= AttrCalc()
   self.obj8323.Copy=ATOM3Boolean()
   self.obj8323.Copy.setValue(('Copy from LHS', 1))
   self.obj8323.Copy.config = 0
   self.obj8323.Specify=ATOM3Constraint()
   self.obj8323.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj832.GGset2Any['ReqFlow']= self.obj8323

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj832)
   self.obj832.postAction( cobj0.RHS.CREATE )

   self.obj833=operatingUnit(self)
   self.obj833.preAction( cobj0.RHS.CREATE )
   self.obj833.isGraphObjectVisual = True

   if(hasattr(self.obj833, '_setHierarchicalLink')):
     self.obj833._setHierarchicalLink(False)

   # OperCostProp
   self.obj833.OperCostProp.setValue(0.0)

   # name
   self.obj833.name.setValue('')
   self.obj833.name.setNone()

   # OperCostFix
   self.obj833.OperCostFix.setValue(0.0)

   self.obj833.GGLabel.setValue(3)
   self.obj833.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(120.0,160.0,self.obj833)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj833.graphObject_ = new_obj
   self.obj8330= AttrCalc()
   self.obj8330.Copy=ATOM3Boolean()
   self.obj8330.Copy.setValue(('Copy from LHS', 1))
   self.obj8330.Copy.config = 0
   self.obj8330.Specify=ATOM3Constraint()
   self.obj8330.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj833.GGset2Any['OperCostProp']= self.obj8330
   self.obj8331= AttrCalc()
   self.obj8331.Copy=ATOM3Boolean()
   self.obj8331.Copy.setValue(('Copy from LHS', 1))
   self.obj8331.Copy.config = 0
   self.obj8331.Specify=ATOM3Constraint()
   self.obj8331.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj833.GGset2Any['name']= self.obj8331
   self.obj8332= AttrCalc()
   self.obj8332.Copy=ATOM3Boolean()
   self.obj8332.Copy.setValue(('Copy from LHS', 1))
   self.obj8332.Copy.config = 0
   self.obj8332.Specify=ATOM3Constraint()
   self.obj8332.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj833.GGset2Any['OperCostFix']= self.obj8332

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj833)
   self.obj833.postAction( cobj0.RHS.CREATE )

   self.obj834=fromRaw(self)
   self.obj834.preAction( cobj0.RHS.CREATE )
   self.obj834.isGraphObjectVisual = True

   if(hasattr(self.obj834, '_setHierarchicalLink')):
     self.obj834._setHierarchicalLink(False)

   # rate
   self.obj834.rate.setValue(0.0)

   self.obj834.GGLabel.setValue(5)
   self.obj834.graphClass_= graph_fromRaw
   if self.genGraphics:
      new_obj = graph_fromRaw(177.0,133.5,self.obj834)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj834.graphObject_ = new_obj
   self.obj8340= AttrCalc()
   self.obj8340.Copy=ATOM3Boolean()
   self.obj8340.Copy.setValue(('Copy from LHS', 1))
   self.obj8340.Copy.config = 0
   self.obj8340.Specify=ATOM3Constraint()
   self.obj8340.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj834.GGset2Any['rate']= self.obj8340

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj834)
   self.obj834.postAction( cobj0.RHS.CREATE )

   self.obj832.out_connections_.append(self.obj834)
   self.obj834.in_connections_.append(self.obj832)
   self.obj832.graphObject_.pendingConnections.append((self.obj832.graphObject_.tag, self.obj834.graphObject_.tag, [184.0, 96.0, 177.0, 133.5], 0, True))
   self.obj834.out_connections_.append(self.obj833)
   self.obj833.in_connections_.append(self.obj834)
   self.obj834.graphObject_.pendingConnections.append((self.obj834.graphObject_.tag, self.obj833.graphObject_.tag, [170.0, 171.0, 177.0, 133.5], 0, True))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.graphRewritingSystem.finalStat > 20 \n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('RemoveCap', 20)
   cobj0.Order=ATOM3Integer(27)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

   from Capabilitie import *
   from rawMaterial import *
   from Goal import *
   from ASG_pns import *
   from operatingUnit import *
   from metarial import *
   from product import *
   from Agent import *
   from fromMaterial import *
   from CapableOf import *
   from intoProduct import *
   from Role import *
   from fromRaw import *
   from intoMaterial import *
   from ASG_omacs import *
   from require import *
   from achieve import *
   from posses import *

   cobj0.LHS = ASG_pns(self)
   cobj0.LHS.merge(ASG_omacs(self))

   self.obj840=Capabilitie(self)
   self.obj840.preAction( cobj0.LHS.CREATE )
   self.obj840.isGraphObjectVisual = True

   if(hasattr(self.obj840, '_setHierarchicalLink')):
     self.obj840._setHierarchicalLink(False)

   # name
   self.obj840.name.setValue('')
   self.obj840.name.setNone()

   self.obj840.GGLabel.setValue(1)
   self.obj840.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(220.0,80.0,self.obj840)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj840.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj840)
   self.obj840.postAction( cobj0.LHS.CREATE )


   cobj0.RHS = ASG_pns(self)


   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.graphRewritingSystem.finalStat > 20 \n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('RemoveRole', 20)
   cobj0.Order=ATOM3Integer(28)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

   from Capabilitie import *
   from rawMaterial import *
   from GenericGraphEdge import *
   from Goal import *
   from ASG_pns import *
   from operatingUnit import *
   from metarial import *
   from GenericGraphNode import *
   from product import *
   from Agent import *
   from fromMaterial import *
   from CapableOf import *
   from intoProduct import *
   from Role import *
   from fromRaw import *
   from intoMaterial import *
   from ASG_GenericGraph import *
   from ASG_omacs import *
   from require import *
   from achieve import *
   from posses import *

   cobj0.LHS = ASG_pns(self)
   cobj0.LHS.merge(ASG_omacs(self))
   cobj0.LHS.merge(ASG_GenericGraph(self))

   self.obj848=metarial(self)
   self.obj848.preAction( cobj0.LHS.CREATE )
   self.obj848.isGraphObjectVisual = True

   if(hasattr(self.obj848, '_setHierarchicalLink')):
     self.obj848._setHierarchicalLink(False)

   # MaxFlow
   self.obj848.MaxFlow.setNone()

   # price
   self.obj848.price.setValue(0)

   # Name
   self.obj848.Name.setValue('')
   self.obj848.Name.setNone()

   # ReqFlow
   self.obj848.ReqFlow.setNone()

   self.obj848.GGLabel.setValue(2)
   self.obj848.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(280.0,40.0,self.obj848)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj848.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj848)
   self.obj848.postAction( cobj0.LHS.CREATE )

   self.obj849=operatingUnit(self)
   self.obj849.preAction( cobj0.LHS.CREATE )
   self.obj849.isGraphObjectVisual = True

   if(hasattr(self.obj849, '_setHierarchicalLink')):
     self.obj849._setHierarchicalLink(False)

   # OperCostProp
   self.obj849.OperCostProp.setNone()

   # name
   self.obj849.name.setValue('')
   self.obj849.name.setNone()

   # OperCostFix
   self.obj849.OperCostFix.setNone()

   self.obj849.GGLabel.setValue(3)
   self.obj849.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(300.0,140.0,self.obj849)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj849.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj849)
   self.obj849.postAction( cobj0.LHS.CREATE )

   self.obj850=fromMaterial(self)
   self.obj850.preAction( cobj0.LHS.CREATE )
   self.obj850.isGraphObjectVisual = True

   if(hasattr(self.obj850, '_setHierarchicalLink')):
     self.obj850._setHierarchicalLink(False)

   # rate
   self.obj850.rate.setNone()

   self.obj850.GGLabel.setValue(4)
   self.obj850.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(342.75,113.75,self.obj850)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj850.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj850)
   self.obj850.postAction( cobj0.LHS.CREATE )

   self.obj851=Role(self)
   self.obj851.preAction( cobj0.LHS.CREATE )
   self.obj851.isGraphObjectVisual = True

   if(hasattr(self.obj851, '_setHierarchicalLink')):
     self.obj851._setHierarchicalLink(False)

   # name
   self.obj851.name.setValue('')
   self.obj851.name.setNone()

   self.obj851.GGLabel.setValue(1)
   self.obj851.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(80.0,60.0,self.obj851)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj851.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj851)
   self.obj851.postAction( cobj0.LHS.CREATE )

   self.obj852=GenericGraphEdge(self)
   self.obj852.preAction( cobj0.LHS.CREATE )
   self.obj852.isGraphObjectVisual = True

   if(hasattr(self.obj852, '_setHierarchicalLink')):
     self.obj852._setHierarchicalLink(False)

   self.obj852.GGLabel.setValue(5)
   self.obj852.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(195.0,71.5,self.obj852)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj852.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj852)
   self.obj852.postAction( cobj0.LHS.CREATE )

   self.obj848.out_connections_.append(self.obj850)
   self.obj850.in_connections_.append(self.obj848)
   self.obj848.graphObject_.pendingConnections.append((self.obj848.graphObject_.tag, self.obj850.graphObject_.tag, [321.0, 82.0, 335.5, 96.5, 342.75, 113.75], 2, True))
   self.obj850.out_connections_.append(self.obj849)
   self.obj849.in_connections_.append(self.obj850)
   self.obj850.graphObject_.pendingConnections.append((self.obj850.graphObject_.tag, self.obj849.graphObject_.tag, [350.0, 151.0, 350.0, 131.0, 342.75, 113.75], 2, True))
   self.obj851.out_connections_.append(self.obj852)
   self.obj852.in_connections_.append(self.obj851)
   self.obj851.graphObject_.pendingConnections.append((self.obj851.graphObject_.tag, self.obj852.graphObject_.tag, [104.0, 61.0, 195.0, 71.5], 0, True))
   self.obj852.out_connections_.append(self.obj848)
   self.obj848.in_connections_.append(self.obj852)
   self.obj852.graphObject_.pendingConnections.append((self.obj852.graphObject_.tag, self.obj848.graphObject_.tag, [286.0, 82.0, 195.0, 71.5], 0, True))

   cobj0.RHS = ASG_pns(self)

   self.obj854=metarial(self)
   self.obj854.preAction( cobj0.RHS.CREATE )
   self.obj854.isGraphObjectVisual = True

   if(hasattr(self.obj854, '_setHierarchicalLink')):
     self.obj854._setHierarchicalLink(False)

   # MaxFlow
   self.obj854.MaxFlow.setValue(999999)

   # price
   self.obj854.price.setValue(0)

   # Name
   self.obj854.Name.setValue('')
   self.obj854.Name.setNone()

   # ReqFlow
   self.obj854.ReqFlow.setValue(0)

   self.obj854.GGLabel.setValue(2)
   self.obj854.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(160.0,40.0,self.obj854)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj854.graphObject_ = new_obj
   self.obj8540= AttrCalc()
   self.obj8540.Copy=ATOM3Boolean()
   self.obj8540.Copy.setValue(('Copy from LHS', 1))
   self.obj8540.Copy.config = 0
   self.obj8540.Specify=ATOM3Constraint()
   self.obj8540.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj854.GGset2Any['MaxFlow']= self.obj8540
   self.obj8541= AttrCalc()
   self.obj8541.Copy=ATOM3Boolean()
   self.obj8541.Copy.setValue(('Copy from LHS', 1))
   self.obj8541.Copy.config = 0
   self.obj8541.Specify=ATOM3Constraint()
   self.obj8541.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj854.GGset2Any['Name']= self.obj8541
   self.obj8542= AttrCalc()
   self.obj8542.Copy=ATOM3Boolean()
   self.obj8542.Copy.setValue(('Copy from LHS', 1))
   self.obj8542.Copy.config = 0
   self.obj8542.Specify=ATOM3Constraint()
   self.obj8542.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj854.GGset2Any['ReqFlow']= self.obj8542

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj854)
   self.obj854.postAction( cobj0.RHS.CREATE )

   self.obj855=operatingUnit(self)
   self.obj855.preAction( cobj0.RHS.CREATE )
   self.obj855.isGraphObjectVisual = True

   if(hasattr(self.obj855, '_setHierarchicalLink')):
     self.obj855._setHierarchicalLink(False)

   # OperCostProp
   self.obj855.OperCostProp.setValue(0.0)

   # name
   self.obj855.name.setValue('')
   self.obj855.name.setNone()

   # OperCostFix
   self.obj855.OperCostFix.setValue(0.0)

   self.obj855.GGLabel.setValue(3)
   self.obj855.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(200.0,140.0,self.obj855)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj855.graphObject_ = new_obj
   self.obj8550= AttrCalc()
   self.obj8550.Copy=ATOM3Boolean()
   self.obj8550.Copy.setValue(('Copy from LHS', 1))
   self.obj8550.Copy.config = 0
   self.obj8550.Specify=ATOM3Constraint()
   self.obj8550.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj855.GGset2Any['OperCostProp']= self.obj8550
   self.obj8551= AttrCalc()
   self.obj8551.Copy=ATOM3Boolean()
   self.obj8551.Copy.setValue(('Copy from LHS', 1))
   self.obj8551.Copy.config = 0
   self.obj8551.Specify=ATOM3Constraint()
   self.obj8551.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj855.GGset2Any['name']= self.obj8551
   self.obj8552= AttrCalc()
   self.obj8552.Copy=ATOM3Boolean()
   self.obj8552.Copy.setValue(('Copy from LHS', 1))
   self.obj8552.Copy.config = 0
   self.obj8552.Specify=ATOM3Constraint()
   self.obj8552.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj855.GGset2Any['OperCostFix']= self.obj8552

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj855)
   self.obj855.postAction( cobj0.RHS.CREATE )

   self.obj856=fromMaterial(self)
   self.obj856.preAction( cobj0.RHS.CREATE )
   self.obj856.isGraphObjectVisual = True

   if(hasattr(self.obj856, '_setHierarchicalLink')):
     self.obj856._setHierarchicalLink(False)

   # rate
   self.obj856.rate.setValue(0.0)

   self.obj856.GGLabel.setValue(4)
   self.obj856.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(238.75,106.25,self.obj856)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj856.graphObject_ = new_obj
   self.obj8560= AttrCalc()
   self.obj8560.Copy=ATOM3Boolean()
   self.obj8560.Copy.setValue(('Copy from LHS', 1))
   self.obj8560.Copy.config = 0
   self.obj8560.Specify=ATOM3Constraint()
   self.obj8560.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj856.GGset2Any['rate']= self.obj8560

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj856)
   self.obj856.postAction( cobj0.RHS.CREATE )

   self.obj854.out_connections_.append(self.obj856)
   self.obj856.in_connections_.append(self.obj854)
   self.obj854.graphObject_.pendingConnections.append((self.obj854.graphObject_.tag, self.obj856.graphObject_.tag, [201.0, 82.0, 226.5, 89.0, 238.75, 106.25], 2, True))
   self.obj856.out_connections_.append(self.obj855)
   self.obj855.in_connections_.append(self.obj856)
   self.obj856.graphObject_.pendingConnections.append((self.obj856.graphObject_.tag, self.obj855.graphObject_.tag, [250.0, 151.0, 251.0, 123.5, 238.75, 106.25], 2, True))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.graphRewritingSystem.finalStat > 20 \n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   lcobj0.append(cobj0)
   self.EditingGraphGrammar.Rules.setValue(lcobj0)
   self.EditingGraphGrammar.InitialAction=ATOM3Constraint()
   self.EditingGraphGrammar.InitialAction.setValue(('constraint', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'print \'Version 1Hahaha \'\nself.rewritingSystem.finalStat = 0\nself.rewritingSystem.Dictag = {}\nself.rewritingSystem.Dictro = {}\n \n\n'))
   self.EditingGraphGrammar.FinalAction=ATOM3Constraint()
   self.EditingGraphGrammar.FinalAction.setValue(('const', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))


