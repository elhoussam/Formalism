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

   self.obj1509=Agent(self)
   self.obj1509.preAction( cobj0.LHS.CREATE )
   self.obj1509.isGraphObjectVisual = True

   if(hasattr(self.obj1509, '_setHierarchicalLink')):
     self.obj1509._setHierarchicalLink(False)

   # price
   self.obj1509.price.setNone()

   # name
   self.obj1509.name.setValue('')
   self.obj1509.name.setNone()

   self.obj1509.GGLabel.setValue(1)
   self.obj1509.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(80.0,20.0,self.obj1509)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1509.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1509)
   self.obj1509.postAction( cobj0.LHS.CREATE )

   self.obj1510=Capabilitie(self)
   self.obj1510.preAction( cobj0.LHS.CREATE )
   self.obj1510.isGraphObjectVisual = True

   if(hasattr(self.obj1510, '_setHierarchicalLink')):
     self.obj1510._setHierarchicalLink(False)

   # name
   self.obj1510.name.setValue('')
   self.obj1510.name.setNone()

   self.obj1510.GGLabel.setValue(2)
   self.obj1510.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(160.0,180.0,self.obj1510)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1510.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1510)
   self.obj1510.postAction( cobj0.LHS.CREATE )

   self.obj1511=Role(self)
   self.obj1511.preAction( cobj0.LHS.CREATE )
   self.obj1511.isGraphObjectVisual = True

   if(hasattr(self.obj1511, '_setHierarchicalLink')):
     self.obj1511._setHierarchicalLink(False)

   # name
   self.obj1511.name.setValue('')
   self.obj1511.name.setNone()

   self.obj1511.GGLabel.setValue(3)
   self.obj1511.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(280.0,40.0,self.obj1511)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1511.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1511)
   self.obj1511.postAction( cobj0.LHS.CREATE )

   self.obj1512=posses(self)
   self.obj1512.preAction( cobj0.LHS.CREATE )
   self.obj1512.isGraphObjectVisual = True

   if(hasattr(self.obj1512, '_setHierarchicalLink')):
     self.obj1512._setHierarchicalLink(False)

   # rate
   self.obj1512.rate.setNone()

   self.obj1512.GGLabel.setValue(4)
   self.obj1512.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(143.0,130.5,self.obj1512)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1512.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1512)
   self.obj1512.postAction( cobj0.LHS.CREATE )

   self.obj1513=require(self)
   self.obj1513.preAction( cobj0.LHS.CREATE )
   self.obj1513.isGraphObjectVisual = True

   if(hasattr(self.obj1513, '_setHierarchicalLink')):
     self.obj1513._setHierarchicalLink(False)

   self.obj1513.GGLabel.setValue(5)
   self.obj1513.graphClass_= graph_require
   if self.genGraphics:
      new_obj = graph_require(242.5,132.5,self.obj1513)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1513.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1513)
   self.obj1513.postAction( cobj0.LHS.CREATE )

   self.obj1509.out_connections_.append(self.obj1512)
   self.obj1512.in_connections_.append(self.obj1509)
   self.obj1509.graphObject_.pendingConnections.append((self.obj1509.graphObject_.tag, self.obj1512.graphObject_.tag, [105.0, 82.0, 143.0, 130.5], 0, True))
   self.obj1511.out_connections_.append(self.obj1513)
   self.obj1513.in_connections_.append(self.obj1511)
   self.obj1511.graphObject_.pendingConnections.append((self.obj1511.graphObject_.tag, self.obj1513.graphObject_.tag, [304.0, 86.0, 242.5, 132.5], 0, True))
   self.obj1512.out_connections_.append(self.obj1510)
   self.obj1510.in_connections_.append(self.obj1512)
   self.obj1512.graphObject_.pendingConnections.append((self.obj1512.graphObject_.tag, self.obj1510.graphObject_.tag, [181.0, 179.0, 143.0, 130.5], 0, True))
   self.obj1513.out_connections_.append(self.obj1510)
   self.obj1510.in_connections_.append(self.obj1513)
   self.obj1513.graphObject_.pendingConnections.append((self.obj1513.graphObject_.tag, self.obj1510.graphObject_.tag, [181.0, 179.0, 242.5, 132.5], 0, True))

   cobj0.RHS = ASG_omacs(self)

   self.obj1515=Agent(self)
   self.obj1515.preAction( cobj0.RHS.CREATE )
   self.obj1515.isGraphObjectVisual = True

   if(hasattr(self.obj1515, '_setHierarchicalLink')):
     self.obj1515._setHierarchicalLink(False)

   # price
   self.obj1515.price.setNone()

   # name
   self.obj1515.name.setValue('')
   self.obj1515.name.setNone()

   self.obj1515.GGLabel.setValue(1)
   self.obj1515.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(80.0,20.0,self.obj1515)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1515.graphObject_ = new_obj
   self.obj15150= AttrCalc()
   self.obj15150.Copy=ATOM3Boolean()
   self.obj15150.Copy.setValue(('Copy from LHS', 1))
   self.obj15150.Copy.config = 0
   self.obj15150.Specify=ATOM3Constraint()
   self.obj15150.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1515.GGset2Any['price']= self.obj15150
   self.obj15151= AttrCalc()
   self.obj15151.Copy=ATOM3Boolean()
   self.obj15151.Copy.setValue(('Copy from LHS', 1))
   self.obj15151.Copy.config = 0
   self.obj15151.Specify=ATOM3Constraint()
   self.obj15151.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1515.GGset2Any['name']= self.obj15151

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1515)
   self.obj1515.postAction( cobj0.RHS.CREATE )

   self.obj1516=Capabilitie(self)
   self.obj1516.preAction( cobj0.RHS.CREATE )
   self.obj1516.isGraphObjectVisual = True

   if(hasattr(self.obj1516, '_setHierarchicalLink')):
     self.obj1516._setHierarchicalLink(False)

   # name
   self.obj1516.name.setValue('')
   self.obj1516.name.setNone()

   self.obj1516.GGLabel.setValue(2)
   self.obj1516.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(160.0,180.0,self.obj1516)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1516.graphObject_ = new_obj
   self.obj15160= AttrCalc()
   self.obj15160.Copy=ATOM3Boolean()
   self.obj15160.Copy.setValue(('Copy from LHS', 1))
   self.obj15160.Copy.config = 0
   self.obj15160.Specify=ATOM3Constraint()
   self.obj15160.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1516.GGset2Any['name']= self.obj15160

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1516)
   self.obj1516.postAction( cobj0.RHS.CREATE )

   self.obj1517=Role(self)
   self.obj1517.preAction( cobj0.RHS.CREATE )
   self.obj1517.isGraphObjectVisual = True

   if(hasattr(self.obj1517, '_setHierarchicalLink')):
     self.obj1517._setHierarchicalLink(False)

   # name
   self.obj1517.name.setValue('')
   self.obj1517.name.setNone()

   self.obj1517.GGLabel.setValue(3)
   self.obj1517.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(280.0,40.0,self.obj1517)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1517.graphObject_ = new_obj
   self.obj15170= AttrCalc()
   self.obj15170.Copy=ATOM3Boolean()
   self.obj15170.Copy.setValue(('Copy from LHS', 1))
   self.obj15170.Copy.config = 0
   self.obj15170.Specify=ATOM3Constraint()
   self.obj15170.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1517.GGset2Any['name']= self.obj15170

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1517)
   self.obj1517.postAction( cobj0.RHS.CREATE )

   self.obj1518=posses(self)
   self.obj1518.preAction( cobj0.RHS.CREATE )
   self.obj1518.isGraphObjectVisual = True

   if(hasattr(self.obj1518, '_setHierarchicalLink')):
     self.obj1518._setHierarchicalLink(False)

   # rate
   self.obj1518.rate.setNone()

   self.obj1518.GGLabel.setValue(4)
   self.obj1518.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(143.0,130.5,self.obj1518)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1518.graphObject_ = new_obj
   self.obj15180= AttrCalc()
   self.obj15180.Copy=ATOM3Boolean()
   self.obj15180.Copy.setValue(('Copy from LHS', 1))
   self.obj15180.Copy.config = 0
   self.obj15180.Specify=ATOM3Constraint()
   self.obj15180.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1518.GGset2Any['rate']= self.obj15180

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1518)
   self.obj1518.postAction( cobj0.RHS.CREATE )

   self.obj1519=CapableOf(self)
   self.obj1519.preAction( cobj0.RHS.CREATE )
   self.obj1519.isGraphObjectVisual = True

   if(hasattr(self.obj1519, '_setHierarchicalLink')):
     self.obj1519._setHierarchicalLink(False)

   # rate
   self.obj1519.rate.setValue(0.0)

   self.obj1519.GGLabel.setValue(7)
   self.obj1519.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(214.0,83.5,self.obj1519)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1519.graphObject_ = new_obj
   self.obj15190= AttrCalc()
   self.obj15190.Copy=ATOM3Boolean()
   self.obj15190.Copy.setValue(('Copy from LHS', 1))
   self.obj15190.Copy.config = 0
   self.obj15190.Specify=ATOM3Constraint()
   self.obj15190.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1519.GGset2Any['rate']= self.obj15190

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1519)
   self.obj1519.postAction( cobj0.RHS.CREATE )

   self.obj1520=require(self)
   self.obj1520.preAction( cobj0.RHS.CREATE )
   self.obj1520.isGraphObjectVisual = True

   if(hasattr(self.obj1520, '_setHierarchicalLink')):
     self.obj1520._setHierarchicalLink(False)

   self.obj1520.GGLabel.setValue(5)
   self.obj1520.graphClass_= graph_require
   if self.genGraphics:
      new_obj = graph_require(242.5,132.5,self.obj1520)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1520.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1520)
   self.obj1520.postAction( cobj0.RHS.CREATE )

   self.obj1515.out_connections_.append(self.obj1518)
   self.obj1518.in_connections_.append(self.obj1515)
   self.obj1515.graphObject_.pendingConnections.append((self.obj1515.graphObject_.tag, self.obj1518.graphObject_.tag, [117.0, 82.0, 143.0, 130.5], 2, 0))
   self.obj1515.out_connections_.append(self.obj1519)
   self.obj1519.in_connections_.append(self.obj1515)
   self.obj1515.graphObject_.pendingConnections.append((self.obj1515.graphObject_.tag, self.obj1519.graphObject_.tag, [117.0, 82.0, 214.0, 83.5], 0, True))
   self.obj1517.out_connections_.append(self.obj1520)
   self.obj1520.in_connections_.append(self.obj1517)
   self.obj1517.graphObject_.pendingConnections.append((self.obj1517.graphObject_.tag, self.obj1520.graphObject_.tag, [311.0, 85.0, 242.5, 132.5], 2, 0))
   self.obj1518.out_connections_.append(self.obj1516)
   self.obj1516.in_connections_.append(self.obj1518)
   self.obj1518.graphObject_.pendingConnections.append((self.obj1518.graphObject_.tag, self.obj1516.graphObject_.tag, [191.0, 183.0, 143.0, 130.5], 2, 0))
   self.obj1519.out_connections_.append(self.obj1517)
   self.obj1517.in_connections_.append(self.obj1519)
   self.obj1519.graphObject_.pendingConnections.append((self.obj1519.graphObject_.tag, self.obj1517.graphObject_.tag, [311.0, 85.0, 214.0, 83.5], 0, True))
   self.obj1520.out_connections_.append(self.obj1516)
   self.obj1516.in_connections_.append(self.obj1520)
   self.obj1520.graphObject_.pendingConnections.append((self.obj1520.graphObject_.tag, self.obj1516.graphObject_.tag, [191.0, 183.0, 242.5, 132.5], 2, 0))

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

   self.obj1525=Agent(self)
   self.obj1525.preAction( cobj0.LHS.CREATE )
   self.obj1525.isGraphObjectVisual = True

   if(hasattr(self.obj1525, '_setHierarchicalLink')):
     self.obj1525._setHierarchicalLink(False)

   # price
   self.obj1525.price.setNone()

   # name
   self.obj1525.name.setValue('')
   self.obj1525.name.setNone()

   self.obj1525.GGLabel.setValue(1)
   self.obj1525.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(60.0,20.0,self.obj1525)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1525.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1525)
   self.obj1525.postAction( cobj0.LHS.CREATE )

   self.obj1526=Capabilitie(self)
   self.obj1526.preAction( cobj0.LHS.CREATE )
   self.obj1526.isGraphObjectVisual = True

   if(hasattr(self.obj1526, '_setHierarchicalLink')):
     self.obj1526._setHierarchicalLink(False)

   # name
   self.obj1526.name.setValue('')
   self.obj1526.name.setNone()

   self.obj1526.GGLabel.setValue(2)
   self.obj1526.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(80.0,180.0,self.obj1526)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1526.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1526)
   self.obj1526.postAction( cobj0.LHS.CREATE )

   self.obj1527=Capabilitie(self)
   self.obj1527.preAction( cobj0.LHS.CREATE )
   self.obj1527.isGraphObjectVisual = True

   if(hasattr(self.obj1527, '_setHierarchicalLink')):
     self.obj1527._setHierarchicalLink(False)

   # name
   self.obj1527.name.setValue('')
   self.obj1527.name.setNone()

   self.obj1527.GGLabel.setValue(3)
   self.obj1527.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(300.0,20.0,self.obj1527)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1527.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1527)
   self.obj1527.postAction( cobj0.LHS.CREATE )

   self.obj1528=Role(self)
   self.obj1528.preAction( cobj0.LHS.CREATE )
   self.obj1528.isGraphObjectVisual = True

   if(hasattr(self.obj1528, '_setHierarchicalLink')):
     self.obj1528._setHierarchicalLink(False)

   # name
   self.obj1528.name.setValue('')
   self.obj1528.name.setNone()

   self.obj1528.GGLabel.setValue(4)
   self.obj1528.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(320.0,180.0,self.obj1528)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1528.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1528)
   self.obj1528.postAction( cobj0.LHS.CREATE )

   self.obj1529=posses(self)
   self.obj1529.preAction( cobj0.LHS.CREATE )
   self.obj1529.isGraphObjectVisual = True

   if(hasattr(self.obj1529, '_setHierarchicalLink')):
     self.obj1529._setHierarchicalLink(False)

   # rate
   self.obj1529.rate.setNone()

   self.obj1529.GGLabel.setValue(5)
   self.obj1529.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(203.0,70.5,self.obj1529)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1529.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1529)
   self.obj1529.postAction( cobj0.LHS.CREATE )

   self.obj1530=posses(self)
   self.obj1530.preAction( cobj0.LHS.CREATE )
   self.obj1530.isGraphObjectVisual = True

   if(hasattr(self.obj1530, '_setHierarchicalLink')):
     self.obj1530._setHierarchicalLink(False)

   # rate
   self.obj1530.rate.setNone()

   self.obj1530.GGLabel.setValue(6)
   self.obj1530.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(93.0,130.5,self.obj1530)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1530.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1530)
   self.obj1530.postAction( cobj0.LHS.CREATE )

   self.obj1531=CapableOf(self)
   self.obj1531.preAction( cobj0.LHS.CREATE )
   self.obj1531.isGraphObjectVisual = True

   if(hasattr(self.obj1531, '_setHierarchicalLink')):
     self.obj1531._setHierarchicalLink(False)

   # rate
   self.obj1531.rate.setNone()

   self.obj1531.GGLabel.setValue(9)
   self.obj1531.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(209.5,129.5,self.obj1531)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1531.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1531)
   self.obj1531.postAction( cobj0.LHS.CREATE )

   self.obj1532=require(self)
   self.obj1532.preAction( cobj0.LHS.CREATE )
   self.obj1532.isGraphObjectVisual = True

   if(hasattr(self.obj1532, '_setHierarchicalLink')):
     self.obj1532._setHierarchicalLink(False)

   self.obj1532.GGLabel.setValue(7)
   self.obj1532.graphClass_= graph_require
   if self.genGraphics:
      new_obj = graph_require(222.5,180.0,self.obj1532)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1532.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1532)
   self.obj1532.postAction( cobj0.LHS.CREATE )

   self.obj1533=require(self)
   self.obj1533.preAction( cobj0.LHS.CREATE )
   self.obj1533.isGraphObjectVisual = True

   if(hasattr(self.obj1533, '_setHierarchicalLink')):
     self.obj1533._setHierarchicalLink(False)

   self.obj1533.GGLabel.setValue(8)
   self.obj1533.graphClass_= graph_require
   if self.genGraphics:
      new_obj = graph_require(332.5,120.0,self.obj1533)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1533.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1533)
   self.obj1533.postAction( cobj0.LHS.CREATE )

   self.obj1525.out_connections_.append(self.obj1529)
   self.obj1529.in_connections_.append(self.obj1525)
   self.obj1525.out_connections_.append(self.obj1530)
   self.obj1530.in_connections_.append(self.obj1525)
   self.obj1525.graphObject_.pendingConnections.append((self.obj1525.graphObject_.tag, self.obj1530.graphObject_.tag, [85.0, 82.0, 93.0, 130.5], 0, True))
   self.obj1525.out_connections_.append(self.obj1531)
   self.obj1531.in_connections_.append(self.obj1525)
   self.obj1525.graphObject_.pendingConnections.append((self.obj1525.graphObject_.tag, self.obj1531.graphObject_.tag, [85.0, 82.0, 163.0, 138.0, 209.5, 129.5], 2, True))
   self.obj1528.out_connections_.append(self.obj1532)
   self.obj1532.in_connections_.append(self.obj1528)
   self.obj1528.graphObject_.pendingConnections.append((self.obj1528.graphObject_.tag, self.obj1532.graphObject_.tag, [344.0, 181.0, 222.5, 180.0], 0, True))
   self.obj1528.out_connections_.append(self.obj1533)
   self.obj1533.in_connections_.append(self.obj1528)
   self.obj1528.graphObject_.pendingConnections.append((self.obj1528.graphObject_.tag, self.obj1533.graphObject_.tag, [344.0, 181.0, 332.5, 120.0], 0, True))
   self.obj1529.out_connections_.append(self.obj1527)
   self.obj1527.in_connections_.append(self.obj1529)
   self.obj1529.graphObject_.pendingConnections.append((self.obj1529.graphObject_.tag, self.obj1527.graphObject_.tag, [321.0, 59.0, 203.0, 70.5], 0, True))
   self.obj1530.out_connections_.append(self.obj1526)
   self.obj1526.in_connections_.append(self.obj1530)
   self.obj1530.graphObject_.pendingConnections.append((self.obj1530.graphObject_.tag, self.obj1526.graphObject_.tag, [101.0, 179.0, 93.0, 130.5], 0, True))
   self.obj1531.out_connections_.append(self.obj1528)
   self.obj1528.in_connections_.append(self.obj1531)
   self.obj1531.graphObject_.pendingConnections.append((self.obj1531.graphObject_.tag, self.obj1528.graphObject_.tag, [344.0, 181.0, 256.0, 121.0, 209.5, 129.5], 2, True))
   self.obj1532.out_connections_.append(self.obj1526)
   self.obj1526.in_connections_.append(self.obj1532)
   self.obj1532.graphObject_.pendingConnections.append((self.obj1532.graphObject_.tag, self.obj1526.graphObject_.tag, [101.0, 179.0, 222.5, 180.0], 0, True))
   self.obj1533.out_connections_.append(self.obj1527)
   self.obj1527.in_connections_.append(self.obj1533)

   cobj0.RHS = ASG_omacs(self)

   self.obj1535=Agent(self)
   self.obj1535.preAction( cobj0.RHS.CREATE )
   self.obj1535.isGraphObjectVisual = True

   if(hasattr(self.obj1535, '_setHierarchicalLink')):
     self.obj1535._setHierarchicalLink(False)

   # price
   self.obj1535.price.setNone()

   # name
   self.obj1535.name.setValue('')
   self.obj1535.name.setNone()

   self.obj1535.GGLabel.setValue(1)
   self.obj1535.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(60.0,20.0,self.obj1535)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1535.graphObject_ = new_obj
   self.obj15350= AttrCalc()
   self.obj15350.Copy=ATOM3Boolean()
   self.obj15350.Copy.setValue(('Copy from LHS', 1))
   self.obj15350.Copy.config = 0
   self.obj15350.Specify=ATOM3Constraint()
   self.obj15350.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1535.GGset2Any['price']= self.obj15350
   self.obj15351= AttrCalc()
   self.obj15351.Copy=ATOM3Boolean()
   self.obj15351.Copy.setValue(('Copy from LHS', 1))
   self.obj15351.Copy.config = 0
   self.obj15351.Specify=ATOM3Constraint()
   self.obj15351.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1535.GGset2Any['name']= self.obj15351

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1535)
   self.obj1535.postAction( cobj0.RHS.CREATE )

   self.obj1536=Capabilitie(self)
   self.obj1536.preAction( cobj0.RHS.CREATE )
   self.obj1536.isGraphObjectVisual = True

   if(hasattr(self.obj1536, '_setHierarchicalLink')):
     self.obj1536._setHierarchicalLink(False)

   # name
   self.obj1536.name.setValue('')
   self.obj1536.name.setNone()

   self.obj1536.GGLabel.setValue(2)
   self.obj1536.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(80.0,180.0,self.obj1536)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1536.graphObject_ = new_obj
   self.obj15360= AttrCalc()
   self.obj15360.Copy=ATOM3Boolean()
   self.obj15360.Copy.setValue(('Copy from LHS', 1))
   self.obj15360.Copy.config = 0
   self.obj15360.Specify=ATOM3Constraint()
   self.obj15360.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1536.GGset2Any['name']= self.obj15360

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1536)
   self.obj1536.postAction( cobj0.RHS.CREATE )

   self.obj1537=Capabilitie(self)
   self.obj1537.preAction( cobj0.RHS.CREATE )
   self.obj1537.isGraphObjectVisual = True

   if(hasattr(self.obj1537, '_setHierarchicalLink')):
     self.obj1537._setHierarchicalLink(False)

   # name
   self.obj1537.name.setValue('')
   self.obj1537.name.setNone()

   self.obj1537.GGLabel.setValue(3)
   self.obj1537.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(300.0,20.0,self.obj1537)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1537.graphObject_ = new_obj
   self.obj15370= AttrCalc()
   self.obj15370.Copy=ATOM3Boolean()
   self.obj15370.Copy.setValue(('Copy from LHS', 1))
   self.obj15370.Copy.config = 0
   self.obj15370.Specify=ATOM3Constraint()
   self.obj15370.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1537.GGset2Any['name']= self.obj15370

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1537)
   self.obj1537.postAction( cobj0.RHS.CREATE )

   self.obj1538=Role(self)
   self.obj1538.preAction( cobj0.RHS.CREATE )
   self.obj1538.isGraphObjectVisual = True

   if(hasattr(self.obj1538, '_setHierarchicalLink')):
     self.obj1538._setHierarchicalLink(False)

   # name
   self.obj1538.name.setValue('')
   self.obj1538.name.setNone()

   self.obj1538.GGLabel.setValue(4)
   self.obj1538.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(320.0,180.0,self.obj1538)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1538.graphObject_ = new_obj
   self.obj15380= AttrCalc()
   self.obj15380.Copy=ATOM3Boolean()
   self.obj15380.Copy.setValue(('Copy from LHS', 1))
   self.obj15380.Copy.config = 0
   self.obj15380.Specify=ATOM3Constraint()
   self.obj15380.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1538.GGset2Any['name']= self.obj15380

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1538)
   self.obj1538.postAction( cobj0.RHS.CREATE )

   self.obj1539=posses(self)
   self.obj1539.preAction( cobj0.RHS.CREATE )
   self.obj1539.isGraphObjectVisual = True

   if(hasattr(self.obj1539, '_setHierarchicalLink')):
     self.obj1539._setHierarchicalLink(False)

   # rate
   self.obj1539.rate.setNone()

   self.obj1539.GGLabel.setValue(5)
   self.obj1539.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(203.0,70.5,self.obj1539)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1539.graphObject_ = new_obj
   self.obj15390= AttrCalc()
   self.obj15390.Copy=ATOM3Boolean()
   self.obj15390.Copy.setValue(('Copy from LHS', 1))
   self.obj15390.Copy.config = 0
   self.obj15390.Specify=ATOM3Constraint()
   self.obj15390.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1539.GGset2Any['rate']= self.obj15390

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1539)
   self.obj1539.postAction( cobj0.RHS.CREATE )

   self.obj1540=posses(self)
   self.obj1540.preAction( cobj0.RHS.CREATE )
   self.obj1540.isGraphObjectVisual = True

   if(hasattr(self.obj1540, '_setHierarchicalLink')):
     self.obj1540._setHierarchicalLink(False)

   # rate
   self.obj1540.rate.setNone()

   self.obj1540.GGLabel.setValue(6)
   self.obj1540.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(93.0,130.5,self.obj1540)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1540.graphObject_ = new_obj
   self.obj15400= AttrCalc()
   self.obj15400.Copy=ATOM3Boolean()
   self.obj15400.Copy.setValue(('Copy from LHS', 1))
   self.obj15400.Copy.config = 0
   self.obj15400.Specify=ATOM3Constraint()
   self.obj15400.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1540.GGset2Any['rate']= self.obj15400

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1540)
   self.obj1540.postAction( cobj0.RHS.CREATE )

   self.obj1541=CapableOf(self)
   self.obj1541.preAction( cobj0.RHS.CREATE )
   self.obj1541.isGraphObjectVisual = True

   if(hasattr(self.obj1541, '_setHierarchicalLink')):
     self.obj1541._setHierarchicalLink(False)

   # rate
   self.obj1541.rate.setValue(0.0)

   self.obj1541.GGLabel.setValue(9)
   self.obj1541.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(209.5,129.5,self.obj1541)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1541.graphObject_ = new_obj
   self.obj15410= AttrCalc()
   self.obj15410.Copy=ATOM3Boolean()
   self.obj15410.Copy.setValue(('Copy from LHS', 1))
   self.obj15410.Copy.config = 0
   self.obj15410.Specify=ATOM3Constraint()
   self.obj15410.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1541.GGset2Any['rate']= self.obj15410

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1541)
   self.obj1541.postAction( cobj0.RHS.CREATE )

   self.obj1542=require(self)
   self.obj1542.preAction( cobj0.RHS.CREATE )
   self.obj1542.isGraphObjectVisual = True

   if(hasattr(self.obj1542, '_setHierarchicalLink')):
     self.obj1542._setHierarchicalLink(False)

   self.obj1542.GGLabel.setValue(7)
   self.obj1542.graphClass_= graph_require
   if self.genGraphics:
      new_obj = graph_require(222.5,180.0,self.obj1542)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1542.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1542)
   self.obj1542.postAction( cobj0.RHS.CREATE )

   self.obj1543=require(self)
   self.obj1543.preAction( cobj0.RHS.CREATE )
   self.obj1543.isGraphObjectVisual = True

   if(hasattr(self.obj1543, '_setHierarchicalLink')):
     self.obj1543._setHierarchicalLink(False)

   self.obj1543.GGLabel.setValue(8)
   self.obj1543.graphClass_= graph_require
   if self.genGraphics:
      new_obj = graph_require(332.5,120.0,self.obj1543)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1543.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1543)
   self.obj1543.postAction( cobj0.RHS.CREATE )

   self.obj1535.out_connections_.append(self.obj1539)
   self.obj1539.in_connections_.append(self.obj1535)
   self.obj1535.out_connections_.append(self.obj1540)
   self.obj1540.in_connections_.append(self.obj1535)
   self.obj1535.graphObject_.pendingConnections.append((self.obj1535.graphObject_.tag, self.obj1540.graphObject_.tag, [97.0, 82.0, 93.0, 130.5], 2, 0))
   self.obj1535.out_connections_.append(self.obj1541)
   self.obj1541.in_connections_.append(self.obj1535)
   self.obj1535.graphObject_.pendingConnections.append((self.obj1535.graphObject_.tag, self.obj1541.graphObject_.tag, [97.0, 82.0, 209.5, 129.5], 2, 0))
   self.obj1538.out_connections_.append(self.obj1542)
   self.obj1542.in_connections_.append(self.obj1538)
   self.obj1538.graphObject_.pendingConnections.append((self.obj1538.graphObject_.tag, self.obj1542.graphObject_.tag, [351.0, 180.0, 222.5, 180.0], 2, 0))
   self.obj1538.out_connections_.append(self.obj1543)
   self.obj1543.in_connections_.append(self.obj1538)
   self.obj1538.graphObject_.pendingConnections.append((self.obj1538.graphObject_.tag, self.obj1543.graphObject_.tag, [351.0, 180.0, 332.5, 120.0], 2, 0))
   self.obj1539.out_connections_.append(self.obj1537)
   self.obj1537.in_connections_.append(self.obj1539)
   self.obj1539.graphObject_.pendingConnections.append((self.obj1539.graphObject_.tag, self.obj1537.graphObject_.tag, [331.0, 63.0, 203.0, 70.5], 2, 0))
   self.obj1540.out_connections_.append(self.obj1536)
   self.obj1536.in_connections_.append(self.obj1540)
   self.obj1540.graphObject_.pendingConnections.append((self.obj1540.graphObject_.tag, self.obj1536.graphObject_.tag, [111.0, 183.0, 93.0, 130.5], 2, 0))
   self.obj1541.out_connections_.append(self.obj1538)
   self.obj1538.in_connections_.append(self.obj1541)
   self.obj1541.graphObject_.pendingConnections.append((self.obj1541.graphObject_.tag, self.obj1538.graphObject_.tag, [351.0, 180.0, 209.5, 129.5], 2, 0))
   self.obj1542.out_connections_.append(self.obj1536)
   self.obj1536.in_connections_.append(self.obj1542)
   self.obj1542.graphObject_.pendingConnections.append((self.obj1542.graphObject_.tag, self.obj1536.graphObject_.tag, [111.0, 183.0, 222.5, 180.0], 2, 0))
   self.obj1543.out_connections_.append(self.obj1537)
   self.obj1537.in_connections_.append(self.obj1543)

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

   self.obj1548=Agent(self)
   self.obj1548.preAction( cobj0.LHS.CREATE )
   self.obj1548.isGraphObjectVisual = True

   if(hasattr(self.obj1548, '_setHierarchicalLink')):
     self.obj1548._setHierarchicalLink(False)

   # price
   self.obj1548.price.setNone()

   # name
   self.obj1548.name.setValue('')
   self.obj1548.name.setNone()

   self.obj1548.GGLabel.setValue(1)
   self.obj1548.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(100.0,20.0,self.obj1548)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1548.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1548)
   self.obj1548.postAction( cobj0.LHS.CREATE )

   self.obj1549=Capabilitie(self)
   self.obj1549.preAction( cobj0.LHS.CREATE )
   self.obj1549.isGraphObjectVisual = True

   if(hasattr(self.obj1549, '_setHierarchicalLink')):
     self.obj1549._setHierarchicalLink(False)

   # name
   self.obj1549.name.setValue('')
   self.obj1549.name.setNone()

   self.obj1549.GGLabel.setValue(3)
   self.obj1549.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(340.0,40.0,self.obj1549)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1549.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1549)
   self.obj1549.postAction( cobj0.LHS.CREATE )

   self.obj1550=Capabilitie(self)
   self.obj1550.preAction( cobj0.LHS.CREATE )
   self.obj1550.isGraphObjectVisual = True

   if(hasattr(self.obj1550, '_setHierarchicalLink')):
     self.obj1550._setHierarchicalLink(False)

   # name
   self.obj1550.name.setValue('')
   self.obj1550.name.setNone()

   self.obj1550.GGLabel.setValue(4)
   self.obj1550.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(140.0,160.0,self.obj1550)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1550.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1550)
   self.obj1550.postAction( cobj0.LHS.CREATE )

   self.obj1551=Role(self)
   self.obj1551.preAction( cobj0.LHS.CREATE )
   self.obj1551.isGraphObjectVisual = True

   if(hasattr(self.obj1551, '_setHierarchicalLink')):
     self.obj1551._setHierarchicalLink(False)

   # name
   self.obj1551.name.setValue('')
   self.obj1551.name.setNone()

   self.obj1551.GGLabel.setValue(2)
   self.obj1551.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(300.0,140.0,self.obj1551)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1551.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1551)
   self.obj1551.postAction( cobj0.LHS.CREATE )

   self.obj1552=posses(self)
   self.obj1552.preAction( cobj0.LHS.CREATE )
   self.obj1552.isGraphObjectVisual = True

   if(hasattr(self.obj1552, '_setHierarchicalLink')):
     self.obj1552._setHierarchicalLink(False)

   # rate
   self.obj1552.rate.setNone()

   self.obj1552.GGLabel.setValue(5)
   self.obj1552.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(143.0,120.5,self.obj1552)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1552.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1552)
   self.obj1552.postAction( cobj0.LHS.CREATE )

   self.obj1553=CapableOf(self)
   self.obj1553.preAction( cobj0.LHS.CREATE )
   self.obj1553.isGraphObjectVisual = True

   if(hasattr(self.obj1553, '_setHierarchicalLink')):
     self.obj1553._setHierarchicalLink(False)

   # rate
   self.obj1553.rate.setNone()

   self.obj1553.GGLabel.setValue(8)
   self.obj1553.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(224.5,111.5,self.obj1553)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1553.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1553)
   self.obj1553.postAction( cobj0.LHS.CREATE )

   self.obj1554=require(self)
   self.obj1554.preAction( cobj0.LHS.CREATE )
   self.obj1554.isGraphObjectVisual = True

   if(hasattr(self.obj1554, '_setHierarchicalLink')):
     self.obj1554._setHierarchicalLink(False)

   self.obj1554.GGLabel.setValue(7)
   self.obj1554.graphClass_= graph_require
   if self.genGraphics:
      new_obj = graph_require(242.5,192.5,self.obj1554)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1554.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1554)
   self.obj1554.postAction( cobj0.LHS.CREATE )

   self.obj1555=require(self)
   self.obj1555.preAction( cobj0.LHS.CREATE )
   self.obj1555.isGraphObjectVisual = True

   if(hasattr(self.obj1555, '_setHierarchicalLink')):
     self.obj1555._setHierarchicalLink(False)

   self.obj1555.GGLabel.setValue(9)
   self.obj1555.graphClass_= graph_require
   if self.genGraphics:
      new_obj = graph_require(351.0,111.5,self.obj1555)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1555.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1555)
   self.obj1555.postAction( cobj0.LHS.CREATE )

   self.obj1548.out_connections_.append(self.obj1552)
   self.obj1552.in_connections_.append(self.obj1548)
   self.obj1548.graphObject_.pendingConnections.append((self.obj1548.graphObject_.tag, self.obj1552.graphObject_.tag, [137.0, 82.0, 143.0, 120.5], 2, 0))
   self.obj1548.out_connections_.append(self.obj1553)
   self.obj1553.in_connections_.append(self.obj1548)
   self.obj1548.graphObject_.pendingConnections.append((self.obj1548.graphObject_.tag, self.obj1553.graphObject_.tag, [125.0, 82.0, 224.5, 111.5], 0, True))
   self.obj1551.out_connections_.append(self.obj1554)
   self.obj1554.in_connections_.append(self.obj1551)
   self.obj1551.graphObject_.pendingConnections.append((self.obj1551.graphObject_.tag, self.obj1554.graphObject_.tag, [324.0, 186.0, 242.5, 192.5], 0, True))
   self.obj1551.out_connections_.append(self.obj1555)
   self.obj1555.in_connections_.append(self.obj1551)
   self.obj1551.graphObject_.pendingConnections.append((self.obj1551.graphObject_.tag, self.obj1555.graphObject_.tag, [331.0, 140.0, 351.0, 111.5], 0, True))
   self.obj1552.out_connections_.append(self.obj1550)
   self.obj1550.in_connections_.append(self.obj1552)
   self.obj1552.graphObject_.pendingConnections.append((self.obj1552.graphObject_.tag, self.obj1550.graphObject_.tag, [161.0, 159.0, 143.0, 120.5], 0, True))
   self.obj1553.out_connections_.append(self.obj1551)
   self.obj1551.in_connections_.append(self.obj1553)
   self.obj1553.graphObject_.pendingConnections.append((self.obj1553.graphObject_.tag, self.obj1551.graphObject_.tag, [324.0, 141.0, 224.5, 111.5], 0, True))
   self.obj1554.out_connections_.append(self.obj1550)
   self.obj1550.in_connections_.append(self.obj1554)
   self.obj1554.graphObject_.pendingConnections.append((self.obj1554.graphObject_.tag, self.obj1550.graphObject_.tag, [161.0, 199.0, 242.5, 192.5], 0, True))
   self.obj1555.out_connections_.append(self.obj1549)
   self.obj1549.in_connections_.append(self.obj1555)
   self.obj1555.graphObject_.pendingConnections.append((self.obj1555.graphObject_.tag, self.obj1549.graphObject_.tag, [371.0, 83.0, 351.0, 111.5], 0, True))

   cobj0.RHS = ASG_omacs(self)

   self.obj1557=Agent(self)
   self.obj1557.preAction( cobj0.RHS.CREATE )
   self.obj1557.isGraphObjectVisual = True

   if(hasattr(self.obj1557, '_setHierarchicalLink')):
     self.obj1557._setHierarchicalLink(False)

   # price
   self.obj1557.price.setNone()

   # name
   self.obj1557.name.setValue('')
   self.obj1557.name.setNone()

   self.obj1557.GGLabel.setValue(1)
   self.obj1557.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(100.0,20.0,self.obj1557)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1557.graphObject_ = new_obj
   self.obj15570= AttrCalc()
   self.obj15570.Copy=ATOM3Boolean()
   self.obj15570.Copy.setValue(('Copy from LHS', 1))
   self.obj15570.Copy.config = 0
   self.obj15570.Specify=ATOM3Constraint()
   self.obj15570.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1557.GGset2Any['price']= self.obj15570
   self.obj15571= AttrCalc()
   self.obj15571.Copy=ATOM3Boolean()
   self.obj15571.Copy.setValue(('Copy from LHS', 1))
   self.obj15571.Copy.config = 0
   self.obj15571.Specify=ATOM3Constraint()
   self.obj15571.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1557.GGset2Any['name']= self.obj15571

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1557)
   self.obj1557.postAction( cobj0.RHS.CREATE )

   self.obj1558=Capabilitie(self)
   self.obj1558.preAction( cobj0.RHS.CREATE )
   self.obj1558.isGraphObjectVisual = True

   if(hasattr(self.obj1558, '_setHierarchicalLink')):
     self.obj1558._setHierarchicalLink(False)

   # name
   self.obj1558.name.setValue('')
   self.obj1558.name.setNone()

   self.obj1558.GGLabel.setValue(3)
   self.obj1558.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(340.0,40.0,self.obj1558)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1558.graphObject_ = new_obj
   self.obj15580= AttrCalc()
   self.obj15580.Copy=ATOM3Boolean()
   self.obj15580.Copy.setValue(('Copy from LHS', 1))
   self.obj15580.Copy.config = 0
   self.obj15580.Specify=ATOM3Constraint()
   self.obj15580.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1558.GGset2Any['name']= self.obj15580

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1558)
   self.obj1558.postAction( cobj0.RHS.CREATE )

   self.obj1559=Capabilitie(self)
   self.obj1559.preAction( cobj0.RHS.CREATE )
   self.obj1559.isGraphObjectVisual = True

   if(hasattr(self.obj1559, '_setHierarchicalLink')):
     self.obj1559._setHierarchicalLink(False)

   # name
   self.obj1559.name.setValue('')
   self.obj1559.name.setNone()

   self.obj1559.GGLabel.setValue(4)
   self.obj1559.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(140.0,160.0,self.obj1559)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1559.graphObject_ = new_obj
   self.obj15590= AttrCalc()
   self.obj15590.Copy=ATOM3Boolean()
   self.obj15590.Copy.setValue(('Copy from LHS', 1))
   self.obj15590.Copy.config = 0
   self.obj15590.Specify=ATOM3Constraint()
   self.obj15590.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1559.GGset2Any['name']= self.obj15590

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1559)
   self.obj1559.postAction( cobj0.RHS.CREATE )

   self.obj1560=Role(self)
   self.obj1560.preAction( cobj0.RHS.CREATE )
   self.obj1560.isGraphObjectVisual = True

   if(hasattr(self.obj1560, '_setHierarchicalLink')):
     self.obj1560._setHierarchicalLink(False)

   # name
   self.obj1560.name.setValue('')
   self.obj1560.name.setNone()

   self.obj1560.GGLabel.setValue(2)
   self.obj1560.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(300.0,140.0,self.obj1560)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1560.graphObject_ = new_obj
   self.obj15600= AttrCalc()
   self.obj15600.Copy=ATOM3Boolean()
   self.obj15600.Copy.setValue(('Copy from LHS', 1))
   self.obj15600.Copy.config = 0
   self.obj15600.Specify=ATOM3Constraint()
   self.obj15600.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1560.GGset2Any['name']= self.obj15600

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1560)
   self.obj1560.postAction( cobj0.RHS.CREATE )

   self.obj1561=posses(self)
   self.obj1561.preAction( cobj0.RHS.CREATE )
   self.obj1561.isGraphObjectVisual = True

   if(hasattr(self.obj1561, '_setHierarchicalLink')):
     self.obj1561._setHierarchicalLink(False)

   # rate
   self.obj1561.rate.setNone()

   self.obj1561.GGLabel.setValue(5)
   self.obj1561.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(143.0,120.5,self.obj1561)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1561.graphObject_ = new_obj
   self.obj15610= AttrCalc()
   self.obj15610.Copy=ATOM3Boolean()
   self.obj15610.Copy.setValue(('Copy from LHS', 1))
   self.obj15610.Copy.config = 0
   self.obj15610.Specify=ATOM3Constraint()
   self.obj15610.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1561.GGset2Any['rate']= self.obj15610

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1561)
   self.obj1561.postAction( cobj0.RHS.CREATE )

   self.obj1562=require(self)
   self.obj1562.preAction( cobj0.RHS.CREATE )
   self.obj1562.isGraphObjectVisual = True

   if(hasattr(self.obj1562, '_setHierarchicalLink')):
     self.obj1562._setHierarchicalLink(False)

   self.obj1562.GGLabel.setValue(7)
   self.obj1562.graphClass_= graph_require
   if self.genGraphics:
      new_obj = graph_require(242.5,192.5,self.obj1562)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1562.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1562)
   self.obj1562.postAction( cobj0.RHS.CREATE )

   self.obj1563=require(self)
   self.obj1563.preAction( cobj0.RHS.CREATE )
   self.obj1563.isGraphObjectVisual = True

   if(hasattr(self.obj1563, '_setHierarchicalLink')):
     self.obj1563._setHierarchicalLink(False)

   self.obj1563.GGLabel.setValue(9)
   self.obj1563.graphClass_= graph_require
   if self.genGraphics:
      new_obj = graph_require(351.0,111.5,self.obj1563)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1563.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1563)
   self.obj1563.postAction( cobj0.RHS.CREATE )

   self.obj1557.out_connections_.append(self.obj1561)
   self.obj1561.in_connections_.append(self.obj1557)
   self.obj1557.graphObject_.pendingConnections.append((self.obj1557.graphObject_.tag, self.obj1561.graphObject_.tag, [137.0, 82.0, 143.0, 120.5], 2, 0))
   self.obj1560.out_connections_.append(self.obj1562)
   self.obj1562.in_connections_.append(self.obj1560)
   self.obj1560.graphObject_.pendingConnections.append((self.obj1560.graphObject_.tag, self.obj1562.graphObject_.tag, [331.0, 185.0, 242.5, 192.5], 2, 0))
   self.obj1560.out_connections_.append(self.obj1563)
   self.obj1563.in_connections_.append(self.obj1560)
   self.obj1560.graphObject_.pendingConnections.append((self.obj1560.graphObject_.tag, self.obj1563.graphObject_.tag, [331.0, 140.0, 351.0, 111.5], 0, True))
   self.obj1561.out_connections_.append(self.obj1559)
   self.obj1559.in_connections_.append(self.obj1561)
   self.obj1561.graphObject_.pendingConnections.append((self.obj1561.graphObject_.tag, self.obj1559.graphObject_.tag, [171.0, 163.0, 143.0, 120.5], 2, 0))
   self.obj1562.out_connections_.append(self.obj1559)
   self.obj1559.in_connections_.append(self.obj1562)
   self.obj1562.graphObject_.pendingConnections.append((self.obj1562.graphObject_.tag, self.obj1559.graphObject_.tag, [171.0, 203.0, 242.5, 192.5], 2, 0))
   self.obj1563.out_connections_.append(self.obj1558)
   self.obj1558.in_connections_.append(self.obj1563)
   self.obj1563.graphObject_.pendingConnections.append((self.obj1563.graphObject_.tag, self.obj1558.graphObject_.tag, [371.0, 83.0, 351.0, 111.5], 0, True))

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

   self.obj1568=Agent(self)
   self.obj1568.preAction( cobj0.LHS.CREATE )
   self.obj1568.isGraphObjectVisual = True

   if(hasattr(self.obj1568, '_setHierarchicalLink')):
     self.obj1568._setHierarchicalLink(False)

   # price
   self.obj1568.price.setNone()

   # name
   self.obj1568.name.setValue('')
   self.obj1568.name.setNone()

   self.obj1568.GGLabel.setValue(1)
   self.obj1568.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(20.0,20.0,self.obj1568)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1568.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1568)
   self.obj1568.postAction( cobj0.LHS.CREATE )

   self.obj1569=Capabilitie(self)
   self.obj1569.preAction( cobj0.LHS.CREATE )
   self.obj1569.isGraphObjectVisual = True

   if(hasattr(self.obj1569, '_setHierarchicalLink')):
     self.obj1569._setHierarchicalLink(False)

   # name
   self.obj1569.name.setValue('')
   self.obj1569.name.setNone()

   self.obj1569.GGLabel.setValue(3)
   self.obj1569.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(140.0,160.0,self.obj1569)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1569.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1569)
   self.obj1569.postAction( cobj0.LHS.CREATE )

   self.obj1570=Role(self)
   self.obj1570.preAction( cobj0.LHS.CREATE )
   self.obj1570.isGraphObjectVisual = True

   if(hasattr(self.obj1570, '_setHierarchicalLink')):
     self.obj1570._setHierarchicalLink(False)

   # name
   self.obj1570.name.setValue('')
   self.obj1570.name.setNone()

   self.obj1570.GGLabel.setValue(2)
   self.obj1570.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(380.0,180.0,self.obj1570)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1570.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1570)
   self.obj1570.postAction( cobj0.LHS.CREATE )

   self.obj1571=posses(self)
   self.obj1571.preAction( cobj0.LHS.CREATE )
   self.obj1571.isGraphObjectVisual = True

   if(hasattr(self.obj1571, '_setHierarchicalLink')):
     self.obj1571._setHierarchicalLink(False)

   # rate
   self.obj1571.rate.setNone()

   self.obj1571.GGLabel.setValue(4)
   self.obj1571.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(78.5,145.75,self.obj1571)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1571.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1571)
   self.obj1571.postAction( cobj0.LHS.CREATE )

   self.obj1572=CapableOf(self)
   self.obj1572.preAction( cobj0.LHS.CREATE )
   self.obj1572.isGraphObjectVisual = True

   if(hasattr(self.obj1572, '_setHierarchicalLink')):
     self.obj1572._setHierarchicalLink(False)

   # rate
   self.obj1572.rate.setNone()

   self.obj1572.GGLabel.setValue(6)
   self.obj1572.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(295.25,111.25,self.obj1572)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1572.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1572)
   self.obj1572.postAction( cobj0.LHS.CREATE )

   self.obj1573=require(self)
   self.obj1573.preAction( cobj0.LHS.CREATE )
   self.obj1573.isGraphObjectVisual = True

   if(hasattr(self.obj1573, '_setHierarchicalLink')):
     self.obj1573._setHierarchicalLink(False)

   self.obj1573.GGLabel.setValue(5)
   self.obj1573.graphClass_= graph_require
   if self.genGraphics:
      new_obj = graph_require(291.0,171.5,self.obj1573)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1573.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1573)
   self.obj1573.postAction( cobj0.LHS.CREATE )

   self.obj1568.out_connections_.append(self.obj1571)
   self.obj1571.in_connections_.append(self.obj1568)
   self.obj1568.graphObject_.pendingConnections.append((self.obj1568.graphObject_.tag, self.obj1571.graphObject_.tag, [45.0, 82.0, 49.5, 126.5, 78.5, 145.75], 2, True))
   self.obj1568.out_connections_.append(self.obj1572)
   self.obj1572.in_connections_.append(self.obj1568)
   self.obj1568.graphObject_.pendingConnections.append((self.obj1568.graphObject_.tag, self.obj1572.graphObject_.tag, [45.0, 82.0, 205.5, 86.5, 295.25, 111.25], 2, True))
   self.obj1570.out_connections_.append(self.obj1573)
   self.obj1573.in_connections_.append(self.obj1570)
   self.obj1570.graphObject_.pendingConnections.append((self.obj1570.graphObject_.tag, self.obj1573.graphObject_.tag, [404.0, 181.0, 374.0, 146.0, 291.0, 171.5], 2, True))
   self.obj1571.out_connections_.append(self.obj1569)
   self.obj1569.in_connections_.append(self.obj1571)
   self.obj1571.graphObject_.pendingConnections.append((self.obj1571.graphObject_.tag, self.obj1569.graphObject_.tag, [161.0, 159.0, 107.5, 165.0, 78.5, 145.75], 2, True))
   self.obj1572.out_connections_.append(self.obj1570)
   self.obj1570.in_connections_.append(self.obj1572)
   self.obj1572.graphObject_.pendingConnections.append((self.obj1572.graphObject_.tag, self.obj1570.graphObject_.tag, [404.0, 181.0, 385.0, 136.0, 295.25, 111.25], 2, True))
   self.obj1573.out_connections_.append(self.obj1569)
   self.obj1569.in_connections_.append(self.obj1573)
   self.obj1573.graphObject_.pendingConnections.append((self.obj1573.graphObject_.tag, self.obj1569.graphObject_.tag, [161.0, 199.0, 208.0, 197.0, 291.0, 171.5], 2, True))

   cobj0.RHS = ASG_omacs(self)

   self.obj1575=Agent(self)
   self.obj1575.preAction( cobj0.RHS.CREATE )
   self.obj1575.isGraphObjectVisual = True

   if(hasattr(self.obj1575, '_setHierarchicalLink')):
     self.obj1575._setHierarchicalLink(False)

   # price
   self.obj1575.price.setNone()

   # name
   self.obj1575.name.setValue('')
   self.obj1575.name.setNone()

   self.obj1575.GGLabel.setValue(1)
   self.obj1575.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(20.0,20.0,self.obj1575)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1575.graphObject_ = new_obj
   self.obj15750= AttrCalc()
   self.obj15750.Copy=ATOM3Boolean()
   self.obj15750.Copy.setValue(('Copy from LHS', 1))
   self.obj15750.Copy.config = 0
   self.obj15750.Specify=ATOM3Constraint()
   self.obj15750.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1575.GGset2Any['price']= self.obj15750
   self.obj15751= AttrCalc()
   self.obj15751.Copy=ATOM3Boolean()
   self.obj15751.Copy.setValue(('Copy from LHS', 1))
   self.obj15751.Copy.config = 0
   self.obj15751.Specify=ATOM3Constraint()
   self.obj15751.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1575.GGset2Any['name']= self.obj15751

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1575)
   self.obj1575.postAction( cobj0.RHS.CREATE )

   self.obj1576=Capabilitie(self)
   self.obj1576.preAction( cobj0.RHS.CREATE )
   self.obj1576.isGraphObjectVisual = True

   if(hasattr(self.obj1576, '_setHierarchicalLink')):
     self.obj1576._setHierarchicalLink(False)

   # name
   self.obj1576.name.setValue('')
   self.obj1576.name.setNone()

   self.obj1576.GGLabel.setValue(3)
   self.obj1576.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(140.0,160.0,self.obj1576)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1576.graphObject_ = new_obj
   self.obj15760= AttrCalc()
   self.obj15760.Copy=ATOM3Boolean()
   self.obj15760.Copy.setValue(('Copy from LHS', 1))
   self.obj15760.Copy.config = 0
   self.obj15760.Specify=ATOM3Constraint()
   self.obj15760.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1576.GGset2Any['name']= self.obj15760

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1576)
   self.obj1576.postAction( cobj0.RHS.CREATE )

   self.obj1577=Role(self)
   self.obj1577.preAction( cobj0.RHS.CREATE )
   self.obj1577.isGraphObjectVisual = True

   if(hasattr(self.obj1577, '_setHierarchicalLink')):
     self.obj1577._setHierarchicalLink(False)

   # name
   self.obj1577.name.setValue('')
   self.obj1577.name.setNone()

   self.obj1577.GGLabel.setValue(2)
   self.obj1577.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(380.0,180.0,self.obj1577)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1577.graphObject_ = new_obj
   self.obj15770= AttrCalc()
   self.obj15770.Copy=ATOM3Boolean()
   self.obj15770.Copy.setValue(('Copy from LHS', 1))
   self.obj15770.Copy.config = 0
   self.obj15770.Specify=ATOM3Constraint()
   self.obj15770.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1577.GGset2Any['name']= self.obj15770

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1577)
   self.obj1577.postAction( cobj0.RHS.CREATE )

   self.obj1578=posses(self)
   self.obj1578.preAction( cobj0.RHS.CREATE )
   self.obj1578.isGraphObjectVisual = True

   if(hasattr(self.obj1578, '_setHierarchicalLink')):
     self.obj1578._setHierarchicalLink(False)

   # rate
   self.obj1578.rate.setNone()

   self.obj1578.GGLabel.setValue(4)
   self.obj1578.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(78.5,145.75,self.obj1578)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1578.graphObject_ = new_obj
   self.obj15780= AttrCalc()
   self.obj15780.Copy=ATOM3Boolean()
   self.obj15780.Copy.setValue(('Copy from LHS', 1))
   self.obj15780.Copy.config = 0
   self.obj15780.Specify=ATOM3Constraint()
   self.obj15780.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1578.GGset2Any['rate']= self.obj15780

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1578)
   self.obj1578.postAction( cobj0.RHS.CREATE )

   self.obj1579=CapableOf(self)
   self.obj1579.preAction( cobj0.RHS.CREATE )
   self.obj1579.isGraphObjectVisual = True

   if(hasattr(self.obj1579, '_setHierarchicalLink')):
     self.obj1579._setHierarchicalLink(False)

   # rate
   self.obj1579.rate.setNone()

   self.obj1579.GGLabel.setValue(6)
   self.obj1579.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(295.25,111.25,self.obj1579)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1579.graphObject_ = new_obj
   self.obj15790= AttrCalc()
   self.obj15790.Copy=ATOM3Boolean()
   self.obj15790.Copy.setValue(('Copy from LHS', 1))
   self.obj15790.Copy.config = 0
   self.obj15790.Specify=ATOM3Constraint()
   self.obj15790.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1579.GGset2Any['rate']= self.obj15790

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1579)
   self.obj1579.postAction( cobj0.RHS.CREATE )

   self.obj1580=require(self)
   self.obj1580.preAction( cobj0.RHS.CREATE )
   self.obj1580.isGraphObjectVisual = True

   if(hasattr(self.obj1580, '_setHierarchicalLink')):
     self.obj1580._setHierarchicalLink(False)

   self.obj1580.GGLabel.setValue(5)
   self.obj1580.graphClass_= graph_require
   if self.genGraphics:
      new_obj = graph_require(291.0,171.5,self.obj1580)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1580.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1580)
   self.obj1580.postAction( cobj0.RHS.CREATE )

   self.obj1575.out_connections_.append(self.obj1578)
   self.obj1578.in_connections_.append(self.obj1575)
   self.obj1575.graphObject_.pendingConnections.append((self.obj1575.graphObject_.tag, self.obj1578.graphObject_.tag, [57.0, 82.0, 78.5, 145.75], 2, 0))
   self.obj1575.out_connections_.append(self.obj1579)
   self.obj1579.in_connections_.append(self.obj1575)
   self.obj1575.graphObject_.pendingConnections.append((self.obj1575.graphObject_.tag, self.obj1579.graphObject_.tag, [57.0, 82.0, 295.25, 111.25], 2, 0))
   self.obj1577.out_connections_.append(self.obj1580)
   self.obj1580.in_connections_.append(self.obj1577)
   self.obj1577.graphObject_.pendingConnections.append((self.obj1577.graphObject_.tag, self.obj1580.graphObject_.tag, [411.0, 180.0, 291.0, 171.5], 2, 0))
   self.obj1578.out_connections_.append(self.obj1576)
   self.obj1576.in_connections_.append(self.obj1578)
   self.obj1578.graphObject_.pendingConnections.append((self.obj1578.graphObject_.tag, self.obj1576.graphObject_.tag, [171.0, 163.0, 78.5, 145.75], 2, 0))
   self.obj1579.out_connections_.append(self.obj1577)
   self.obj1577.in_connections_.append(self.obj1579)
   self.obj1579.graphObject_.pendingConnections.append((self.obj1579.graphObject_.tag, self.obj1577.graphObject_.tag, [411.0, 180.0, 295.25, 111.25], 2, 0))
   self.obj1580.out_connections_.append(self.obj1576)
   self.obj1576.in_connections_.append(self.obj1580)
   self.obj1580.graphObject_.pendingConnections.append((self.obj1580.graphObject_.tag, self.obj1576.graphObject_.tag, [171.0, 163.0, 291.0, 171.5], 2, 0))

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

   self.obj1585=Agent(self)
   self.obj1585.preAction( cobj0.LHS.CREATE )
   self.obj1585.isGraphObjectVisual = True

   if(hasattr(self.obj1585, '_setHierarchicalLink')):
     self.obj1585._setHierarchicalLink(False)

   # price
   self.obj1585.price.setNone()

   # name
   self.obj1585.name.setValue('')
   self.obj1585.name.setNone()

   self.obj1585.GGLabel.setValue(1)
   self.obj1585.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(40.0,20.0,self.obj1585)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1585.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1585)
   self.obj1585.postAction( cobj0.LHS.CREATE )

   self.obj1586=Role(self)
   self.obj1586.preAction( cobj0.LHS.CREATE )
   self.obj1586.isGraphObjectVisual = True

   if(hasattr(self.obj1586, '_setHierarchicalLink')):
     self.obj1586._setHierarchicalLink(False)

   # name
   self.obj1586.name.setValue('')
   self.obj1586.name.setNone()

   self.obj1586.GGLabel.setValue(2)
   self.obj1586.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(360.0,160.0,self.obj1586)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1586.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1586)
   self.obj1586.postAction( cobj0.LHS.CREATE )

   self.obj1587=CapableOf(self)
   self.obj1587.preAction( cobj0.LHS.CREATE )
   self.obj1587.isGraphObjectVisual = True

   if(hasattr(self.obj1587, '_setHierarchicalLink')):
     self.obj1587._setHierarchicalLink(False)

   # rate
   self.obj1587.rate.setNone()

   self.obj1587.GGLabel.setValue(3)
   self.obj1587.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(220.0,114.5,self.obj1587)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1587.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1587)
   self.obj1587.postAction( cobj0.LHS.CREATE )

   self.obj1585.out_connections_.append(self.obj1587)
   self.obj1587.in_connections_.append(self.obj1585)
   self.obj1585.graphObject_.pendingConnections.append((self.obj1585.graphObject_.tag, self.obj1587.graphObject_.tag, [65.0, 82.0, 84.0, 138.0, 220.0, 114.5], 2, True))
   self.obj1587.out_connections_.append(self.obj1586)
   self.obj1586.in_connections_.append(self.obj1587)
   self.obj1587.graphObject_.pendingConnections.append((self.obj1587.graphObject_.tag, self.obj1586.graphObject_.tag, [384.0, 161.0, 356.0, 91.0, 220.0, 114.5], 2, True))

   cobj0.RHS = ASG_omacs(self)

   self.obj1589=Agent(self)
   self.obj1589.preAction( cobj0.RHS.CREATE )
   self.obj1589.isGraphObjectVisual = True

   if(hasattr(self.obj1589, '_setHierarchicalLink')):
     self.obj1589._setHierarchicalLink(False)

   # price
   self.obj1589.price.setNone()

   # name
   self.obj1589.name.setValue('')
   self.obj1589.name.setNone()

   self.obj1589.GGLabel.setValue(1)
   self.obj1589.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(40.0,20.0,self.obj1589)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1589.graphObject_ = new_obj
   self.obj15890= AttrCalc()
   self.obj15890.Copy=ATOM3Boolean()
   self.obj15890.Copy.setValue(('Copy from LHS', 1))
   self.obj15890.Copy.config = 0
   self.obj15890.Specify=ATOM3Constraint()
   self.obj15890.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1589.GGset2Any['price']= self.obj15890
   self.obj15891= AttrCalc()
   self.obj15891.Copy=ATOM3Boolean()
   self.obj15891.Copy.setValue(('Copy from LHS', 1))
   self.obj15891.Copy.config = 0
   self.obj15891.Specify=ATOM3Constraint()
   self.obj15891.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1589.GGset2Any['name']= self.obj15891

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1589)
   self.obj1589.postAction( cobj0.RHS.CREATE )

   self.obj1590=Role(self)
   self.obj1590.preAction( cobj0.RHS.CREATE )
   self.obj1590.isGraphObjectVisual = True

   if(hasattr(self.obj1590, '_setHierarchicalLink')):
     self.obj1590._setHierarchicalLink(False)

   # name
   self.obj1590.name.setValue('')
   self.obj1590.name.setNone()

   self.obj1590.GGLabel.setValue(2)
   self.obj1590.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(360.0,160.0,self.obj1590)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1590.graphObject_ = new_obj
   self.obj15900= AttrCalc()
   self.obj15900.Copy=ATOM3Boolean()
   self.obj15900.Copy.setValue(('Copy from LHS', 1))
   self.obj15900.Copy.config = 0
   self.obj15900.Specify=ATOM3Constraint()
   self.obj15900.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1590.GGset2Any['name']= self.obj15900

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1590)
   self.obj1590.postAction( cobj0.RHS.CREATE )

   self.obj1591=CapableOf(self)
   self.obj1591.preAction( cobj0.RHS.CREATE )
   self.obj1591.isGraphObjectVisual = True

   if(hasattr(self.obj1591, '_setHierarchicalLink')):
     self.obj1591._setHierarchicalLink(False)

   # rate
   self.obj1591.rate.setNone()

   self.obj1591.GGLabel.setValue(3)
   self.obj1591.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(220.0,114.5,self.obj1591)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1591.graphObject_ = new_obj
   self.obj15910= AttrCalc()
   self.obj15910.Copy=ATOM3Boolean()
   self.obj15910.Copy.setValue(('Copy from LHS', 1))
   self.obj15910.Copy.config = 0
   self.obj15910.Specify=ATOM3Constraint()
   self.obj15910.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1591.GGset2Any['rate']= self.obj15910

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1591)
   self.obj1591.postAction( cobj0.RHS.CREATE )

   self.obj1589.out_connections_.append(self.obj1591)
   self.obj1591.in_connections_.append(self.obj1589)
   self.obj1589.graphObject_.pendingConnections.append((self.obj1589.graphObject_.tag, self.obj1591.graphObject_.tag, [77.0, 82.0, 220.0, 114.5], 2, 0))
   self.obj1591.out_connections_.append(self.obj1590)
   self.obj1590.in_connections_.append(self.obj1591)
   self.obj1591.graphObject_.pendingConnections.append((self.obj1591.graphObject_.tag, self.obj1590.graphObject_.tag, [391.0, 160.0, 220.0, 114.5], 2, 0))

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

   self.obj1596=Role(self)
   self.obj1596.preAction( cobj0.LHS.CREATE )
   self.obj1596.isGraphObjectVisual = True

   if(hasattr(self.obj1596, '_setHierarchicalLink')):
     self.obj1596._setHierarchicalLink(False)

   # name
   self.obj1596.name.setValue('')
   self.obj1596.name.setNone()

   self.obj1596.GGLabel.setValue(2)
   self.obj1596.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(40.0,40.0,self.obj1596)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1596.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1596)
   self.obj1596.postAction( cobj0.LHS.CREATE )

   self.obj1597=Goal(self)
   self.obj1597.preAction( cobj0.LHS.CREATE )
   self.obj1597.isGraphObjectVisual = True

   if(hasattr(self.obj1597, '_setHierarchicalLink')):
     self.obj1597._setHierarchicalLink(False)

   # name
   self.obj1597.name.setValue('')
   self.obj1597.name.setNone()

   self.obj1597.GGLabel.setValue(1)
   self.obj1597.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(300.0,160.0,self.obj1597)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1597.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1597)
   self.obj1597.postAction( cobj0.LHS.CREATE )

   self.obj1598=achieve(self)
   self.obj1598.preAction( cobj0.LHS.CREATE )
   self.obj1598.isGraphObjectVisual = True

   if(hasattr(self.obj1598, '_setHierarchicalLink')):
     self.obj1598._setHierarchicalLink(False)

   # rate
   self.obj1598.rate.setNone()

   self.obj1598.GGLabel.setValue(3)
   self.obj1598.graphClass_= graph_achieve
   if self.genGraphics:
      new_obj = graph_achieve(171.25,141.25,self.obj1598)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1598.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1598)
   self.obj1598.postAction( cobj0.LHS.CREATE )

   self.obj1596.out_connections_.append(self.obj1598)
   self.obj1598.in_connections_.append(self.obj1596)
   self.obj1596.graphObject_.pendingConnections.append((self.obj1596.graphObject_.tag, self.obj1598.graphObject_.tag, [64.0, 86.0, 106.5, 122.5, 171.25, 141.25], 2, True))
   self.obj1598.out_connections_.append(self.obj1597)
   self.obj1597.in_connections_.append(self.obj1598)
   self.obj1598.graphObject_.pendingConnections.append((self.obj1598.graphObject_.tag, self.obj1597.graphObject_.tag, [323.0, 161.0, 236.0, 160.0, 171.25, 141.25], 2, True))

   cobj0.RHS = ASG_omacs(self)

   self.obj1600=Role(self)
   self.obj1600.preAction( cobj0.RHS.CREATE )
   self.obj1600.isGraphObjectVisual = True

   if(hasattr(self.obj1600, '_setHierarchicalLink')):
     self.obj1600._setHierarchicalLink(False)

   # name
   self.obj1600.name.setValue('')
   self.obj1600.name.setNone()

   self.obj1600.GGLabel.setValue(2)
   self.obj1600.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(40.0,40.0,self.obj1600)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1600.graphObject_ = new_obj
   self.obj16000= AttrCalc()
   self.obj16000.Copy=ATOM3Boolean()
   self.obj16000.Copy.setValue(('Copy from LHS', 1))
   self.obj16000.Copy.config = 0
   self.obj16000.Specify=ATOM3Constraint()
   self.obj16000.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1600.GGset2Any['name']= self.obj16000

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1600)
   self.obj1600.postAction( cobj0.RHS.CREATE )

   self.obj1601=Goal(self)
   self.obj1601.preAction( cobj0.RHS.CREATE )
   self.obj1601.isGraphObjectVisual = True

   if(hasattr(self.obj1601, '_setHierarchicalLink')):
     self.obj1601._setHierarchicalLink(False)

   # name
   self.obj1601.name.setValue('')
   self.obj1601.name.setNone()

   self.obj1601.GGLabel.setValue(1)
   self.obj1601.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(300.0,160.0,self.obj1601)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1601.graphObject_ = new_obj
   self.obj16010= AttrCalc()
   self.obj16010.Copy=ATOM3Boolean()
   self.obj16010.Copy.setValue(('Copy from LHS', 1))
   self.obj16010.Copy.config = 0
   self.obj16010.Specify=ATOM3Constraint()
   self.obj16010.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1601.GGset2Any['name']= self.obj16010

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1601)
   self.obj1601.postAction( cobj0.RHS.CREATE )

   self.obj1602=achieve(self)
   self.obj1602.preAction( cobj0.RHS.CREATE )
   self.obj1602.isGraphObjectVisual = True

   if(hasattr(self.obj1602, '_setHierarchicalLink')):
     self.obj1602._setHierarchicalLink(False)

   # rate
   self.obj1602.rate.setNone()

   self.obj1602.GGLabel.setValue(3)
   self.obj1602.graphClass_= graph_achieve
   if self.genGraphics:
      new_obj = graph_achieve(171.25,141.25,self.obj1602)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1602.graphObject_ = new_obj
   self.obj16020= AttrCalc()
   self.obj16020.Copy=ATOM3Boolean()
   self.obj16020.Copy.setValue(('Copy from LHS', 1))
   self.obj16020.Copy.config = 0
   self.obj16020.Specify=ATOM3Constraint()
   self.obj16020.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1602.GGset2Any['rate']= self.obj16020

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1602)
   self.obj1602.postAction( cobj0.RHS.CREATE )

   self.obj1600.out_connections_.append(self.obj1602)
   self.obj1602.in_connections_.append(self.obj1600)
   self.obj1600.graphObject_.pendingConnections.append((self.obj1600.graphObject_.tag, self.obj1602.graphObject_.tag, [71.0, 85.0, 171.25, 141.25], 2, 0))
   self.obj1602.out_connections_.append(self.obj1601)
   self.obj1601.in_connections_.append(self.obj1602)
   self.obj1602.graphObject_.pendingConnections.append((self.obj1602.graphObject_.tag, self.obj1601.graphObject_.tag, [333.0, 161.0, 171.25, 141.25], 2, 0))

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

   self.obj1607=Agent(self)
   self.obj1607.preAction( cobj0.LHS.CREATE )
   self.obj1607.isGraphObjectVisual = True

   if(hasattr(self.obj1607, '_setHierarchicalLink')):
     self.obj1607._setHierarchicalLink(False)

   # price
   self.obj1607.price.setNone()

   # name
   self.obj1607.name.setValue('')
   self.obj1607.name.setNone()

   self.obj1607.GGLabel.setValue(1)
   self.obj1607.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(100.0,20.0,self.obj1607)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1607.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1607)
   self.obj1607.postAction( cobj0.LHS.CREATE )

   self.obj1608=Role(self)
   self.obj1608.preAction( cobj0.LHS.CREATE )
   self.obj1608.isGraphObjectVisual = True

   if(hasattr(self.obj1608, '_setHierarchicalLink')):
     self.obj1608._setHierarchicalLink(False)

   # name
   self.obj1608.name.setValue('')
   self.obj1608.name.setNone()

   self.obj1608.GGLabel.setValue(2)
   self.obj1608.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(360.0,160.0,self.obj1608)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1608.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1608)
   self.obj1608.postAction( cobj0.LHS.CREATE )

   self.obj1609=CapableOf(self)
   self.obj1609.preAction( cobj0.LHS.CREATE )
   self.obj1609.isGraphObjectVisual = True

   if(hasattr(self.obj1609, '_setHierarchicalLink')):
     self.obj1609._setHierarchicalLink(False)

   # rate
   self.obj1609.rate.setNone()

   self.obj1609.GGLabel.setValue(3)
   self.obj1609.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(281.5,134.0,self.obj1609)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1609.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1609)
   self.obj1609.postAction( cobj0.LHS.CREATE )

   self.obj1607.out_connections_.append(self.obj1609)
   self.obj1609.in_connections_.append(self.obj1607)
   self.obj1607.graphObject_.pendingConnections.append((self.obj1607.graphObject_.tag, self.obj1609.graphObject_.tag, [125.0, 82.0, 161.0, 153.0, 281.5, 134.0], 2, True))
   self.obj1609.out_connections_.append(self.obj1608)
   self.obj1608.in_connections_.append(self.obj1609)
   self.obj1609.graphObject_.pendingConnections.append((self.obj1609.graphObject_.tag, self.obj1608.graphObject_.tag, [384.0, 161.0, 402.0, 115.0, 281.5, 134.0], 2, True))

   cobj0.RHS = ASG_omacs(self)
   cobj0.RHS.merge(ASG_pns(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj1613=Agent(self)
   self.obj1613.preAction( cobj0.RHS.CREATE )
   self.obj1613.isGraphObjectVisual = True

   if(hasattr(self.obj1613, '_setHierarchicalLink')):
     self.obj1613._setHierarchicalLink(False)

   # price
   self.obj1613.price.setNone()

   # name
   self.obj1613.name.setValue('')
   self.obj1613.name.setNone()

   self.obj1613.GGLabel.setValue(1)
   self.obj1613.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(100.0,20.0,self.obj1613)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1613.graphObject_ = new_obj
   self.obj16130= AttrCalc()
   self.obj16130.Copy=ATOM3Boolean()
   self.obj16130.Copy.setValue(('Copy from LHS', 1))
   self.obj16130.Copy.config = 0
   self.obj16130.Specify=ATOM3Constraint()
   self.obj16130.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1613.GGset2Any['price']= self.obj16130
   self.obj16131= AttrCalc()
   self.obj16131.Copy=ATOM3Boolean()
   self.obj16131.Copy.setValue(('Copy from LHS', 1))
   self.obj16131.Copy.config = 0
   self.obj16131.Specify=ATOM3Constraint()
   self.obj16131.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1613.GGset2Any['name']= self.obj16131

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1613)
   self.obj1613.postAction( cobj0.RHS.CREATE )

   self.obj1614=Role(self)
   self.obj1614.preAction( cobj0.RHS.CREATE )
   self.obj1614.isGraphObjectVisual = True

   if(hasattr(self.obj1614, '_setHierarchicalLink')):
     self.obj1614._setHierarchicalLink(False)

   # name
   self.obj1614.name.setValue('')
   self.obj1614.name.setNone()

   self.obj1614.GGLabel.setValue(2)
   self.obj1614.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(360.0,160.0,self.obj1614)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1614.graphObject_ = new_obj
   self.obj16140= AttrCalc()
   self.obj16140.Copy=ATOM3Boolean()
   self.obj16140.Copy.setValue(('Copy from LHS', 1))
   self.obj16140.Copy.config = 0
   self.obj16140.Specify=ATOM3Constraint()
   self.obj16140.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1614.GGset2Any['name']= self.obj16140

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1614)
   self.obj1614.postAction( cobj0.RHS.CREATE )

   self.obj1615=CapableOf(self)
   self.obj1615.preAction( cobj0.RHS.CREATE )
   self.obj1615.isGraphObjectVisual = True

   if(hasattr(self.obj1615, '_setHierarchicalLink')):
     self.obj1615._setHierarchicalLink(False)

   # rate
   self.obj1615.rate.setValue(0.0)

   self.obj1615.GGLabel.setValue(3)
   self.obj1615.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(281.5,134.0,self.obj1615)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1615.graphObject_ = new_obj
   self.obj16150= AttrCalc()
   self.obj16150.Copy=ATOM3Boolean()
   self.obj16150.Copy.setValue(('Copy from LHS', 1))
   self.obj16150.Copy.config = 0
   self.obj16150.Specify=ATOM3Constraint()
   self.obj16150.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1615.GGset2Any['rate']= self.obj16150

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1615)
   self.obj1615.postAction( cobj0.RHS.CREATE )

   self.obj1616=rawMaterial(self)
   self.obj1616.preAction( cobj0.RHS.CREATE )
   self.obj1616.isGraphObjectVisual = True

   if(hasattr(self.obj1616, '_setHierarchicalLink')):
     self.obj1616._setHierarchicalLink(False)

   # MaxFlow
   self.obj1616.MaxFlow.setValue(999999)

   # price
   self.obj1616.price.setValue(0)

   # Name
   self.obj1616.Name.setValue('')
   self.obj1616.Name.setNone()

   # ReqFlow
   self.obj1616.ReqFlow.setValue(0)

   self.obj1616.GGLabel.setValue(6)
   self.obj1616.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(280.0,20.0,self.obj1616)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1616.graphObject_ = new_obj
   self.obj16160= AttrCalc()
   self.obj16160.Copy=ATOM3Boolean()
   self.obj16160.Copy.setValue(('Copy from LHS', 1))
   self.obj16160.Copy.config = 0
   self.obj16160.Specify=ATOM3Constraint()
   self.obj16160.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1616.GGset2Any['MaxFlow']= self.obj16160
   self.obj16161= AttrCalc()
   self.obj16161.Copy=ATOM3Boolean()
   self.obj16161.Copy.setValue(('Copy from LHS', 1))
   self.obj16161.Copy.config = 0
   self.obj16161.Specify=ATOM3Constraint()
   self.obj16161.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1616.GGset2Any['price']= self.obj16161
   self.obj16162= AttrCalc()
   self.obj16162.Copy=ATOM3Boolean()
   self.obj16162.Copy.setValue(('Copy from LHS', 0))
   self.obj16162.Copy.config = 0
   self.obj16162.Specify=ATOM3Constraint()
   self.obj16162.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()\n\n\n\n'))
   self.obj1616.GGset2Any['Name']= self.obj16162
   self.obj16163= AttrCalc()
   self.obj16163.Copy=ATOM3Boolean()
   self.obj16163.Copy.setValue(('Copy from LHS', 1))
   self.obj16163.Copy.config = 0
   self.obj16163.Specify=ATOM3Constraint()
   self.obj16163.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1616.GGset2Any['ReqFlow']= self.obj16163

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1616)
   self.obj1616.postAction( cobj0.RHS.CREATE )

   self.obj1617=GenericGraphEdge(self)
   self.obj1617.preAction( cobj0.RHS.CREATE )
   self.obj1617.isGraphObjectVisual = True

   if(hasattr(self.obj1617, '_setHierarchicalLink')):
     self.obj1617._setHierarchicalLink(False)

   self.obj1617.GGLabel.setValue(7)
   self.obj1617.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(220.5,79.0,self.obj1617)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1617.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1617)
   self.obj1617.postAction( cobj0.RHS.CREATE )

   self.obj1613.out_connections_.append(self.obj1615)
   self.obj1615.in_connections_.append(self.obj1613)
   self.obj1613.graphObject_.pendingConnections.append((self.obj1613.graphObject_.tag, self.obj1615.graphObject_.tag, [137.0, 82.0, 281.5, 134.0], 2, 0))
   self.obj1613.out_connections_.append(self.obj1617)
   self.obj1617.in_connections_.append(self.obj1613)
   self.obj1613.graphObject_.pendingConnections.append((self.obj1613.graphObject_.tag, self.obj1617.graphObject_.tag, [137.0, 82.0, 220.5, 79.0], 0, True))
   self.obj1615.out_connections_.append(self.obj1614)
   self.obj1614.in_connections_.append(self.obj1615)
   self.obj1615.graphObject_.pendingConnections.append((self.obj1615.graphObject_.tag, self.obj1614.graphObject_.tag, [391.0, 160.0, 281.5, 134.0], 2, 0))
   self.obj1617.out_connections_.append(self.obj1616)
   self.obj1616.in_connections_.append(self.obj1617)
   self.obj1617.graphObject_.pendingConnections.append((self.obj1617.graphObject_.tag, self.obj1616.graphObject_.tag, [304.0, 76.0, 220.5, 79.0], 0, True))

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

   self.obj1622=Agent(self)
   self.obj1622.preAction( cobj0.LHS.CREATE )
   self.obj1622.isGraphObjectVisual = True

   if(hasattr(self.obj1622, '_setHierarchicalLink')):
     self.obj1622._setHierarchicalLink(False)

   # price
   self.obj1622.price.setNone()

   # name
   self.obj1622.name.setValue('')
   self.obj1622.name.setNone()

   self.obj1622.GGLabel.setValue(1)
   self.obj1622.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(60.0,40.0,self.obj1622)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1622.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1622)
   self.obj1622.postAction( cobj0.LHS.CREATE )

   self.obj1623=Role(self)
   self.obj1623.preAction( cobj0.LHS.CREATE )
   self.obj1623.isGraphObjectVisual = True

   if(hasattr(self.obj1623, '_setHierarchicalLink')):
     self.obj1623._setHierarchicalLink(False)

   # name
   self.obj1623.name.setValue('')
   self.obj1623.name.setNone()

   self.obj1623.GGLabel.setValue(2)
   self.obj1623.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(320.0,220.0,self.obj1623)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1623.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1623)
   self.obj1623.postAction( cobj0.LHS.CREATE )

   self.obj1624=CapableOf(self)
   self.obj1624.preAction( cobj0.LHS.CREATE )
   self.obj1624.isGraphObjectVisual = True

   if(hasattr(self.obj1624, '_setHierarchicalLink')):
     self.obj1624._setHierarchicalLink(False)

   # rate
   self.obj1624.rate.setNone()

   self.obj1624.GGLabel.setValue(3)
   self.obj1624.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(230.0,173.0,self.obj1624)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1624.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1624)
   self.obj1624.postAction( cobj0.LHS.CREATE )

   self.obj1622.out_connections_.append(self.obj1624)
   self.obj1624.in_connections_.append(self.obj1622)
   self.obj1622.graphObject_.pendingConnections.append((self.obj1622.graphObject_.tag, self.obj1624.graphObject_.tag, [85.0, 102.0, 117.0, 188.0, 230.0, 173.0], 2, True))
   self.obj1624.out_connections_.append(self.obj1623)
   self.obj1623.in_connections_.append(self.obj1624)
   self.obj1624.graphObject_.pendingConnections.append((self.obj1624.graphObject_.tag, self.obj1623.graphObject_.tag, [344.0, 221.0, 343.0, 158.0, 230.0, 173.0], 2, True))

   cobj0.RHS = ASG_omacs(self)
   cobj0.RHS.merge(ASG_pns(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj1628=Agent(self)
   self.obj1628.preAction( cobj0.RHS.CREATE )
   self.obj1628.isGraphObjectVisual = True

   if(hasattr(self.obj1628, '_setHierarchicalLink')):
     self.obj1628._setHierarchicalLink(False)

   # price
   self.obj1628.price.setNone()

   # name
   self.obj1628.name.setValue('')
   self.obj1628.name.setNone()

   self.obj1628.GGLabel.setValue(1)
   self.obj1628.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(60.0,40.0,self.obj1628)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1628.graphObject_ = new_obj
   self.obj16280= AttrCalc()
   self.obj16280.Copy=ATOM3Boolean()
   self.obj16280.Copy.setValue(('Copy from LHS', 1))
   self.obj16280.Copy.config = 0
   self.obj16280.Specify=ATOM3Constraint()
   self.obj16280.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1628.GGset2Any['price']= self.obj16280
   self.obj16281= AttrCalc()
   self.obj16281.Copy=ATOM3Boolean()
   self.obj16281.Copy.setValue(('Copy from LHS', 1))
   self.obj16281.Copy.config = 0
   self.obj16281.Specify=ATOM3Constraint()
   self.obj16281.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1628.GGset2Any['name']= self.obj16281

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1628)
   self.obj1628.postAction( cobj0.RHS.CREATE )

   self.obj1629=Role(self)
   self.obj1629.preAction( cobj0.RHS.CREATE )
   self.obj1629.isGraphObjectVisual = True

   if(hasattr(self.obj1629, '_setHierarchicalLink')):
     self.obj1629._setHierarchicalLink(False)

   # name
   self.obj1629.name.setValue('')
   self.obj1629.name.setNone()

   self.obj1629.GGLabel.setValue(2)
   self.obj1629.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(320.0,220.0,self.obj1629)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1629.graphObject_ = new_obj
   self.obj16290= AttrCalc()
   self.obj16290.Copy=ATOM3Boolean()
   self.obj16290.Copy.setValue(('Copy from LHS', 1))
   self.obj16290.Copy.config = 0
   self.obj16290.Specify=ATOM3Constraint()
   self.obj16290.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1629.GGset2Any['name']= self.obj16290

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1629)
   self.obj1629.postAction( cobj0.RHS.CREATE )

   self.obj1630=CapableOf(self)
   self.obj1630.preAction( cobj0.RHS.CREATE )
   self.obj1630.isGraphObjectVisual = True

   if(hasattr(self.obj1630, '_setHierarchicalLink')):
     self.obj1630._setHierarchicalLink(False)

   # rate
   self.obj1630.rate.setNone()

   self.obj1630.GGLabel.setValue(3)
   self.obj1630.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(230.0,173.0,self.obj1630)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1630.graphObject_ = new_obj
   self.obj16300= AttrCalc()
   self.obj16300.Copy=ATOM3Boolean()
   self.obj16300.Copy.setValue(('Copy from LHS', 1))
   self.obj16300.Copy.config = 0
   self.obj16300.Specify=ATOM3Constraint()
   self.obj16300.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1630.GGset2Any['rate']= self.obj16300

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1630)
   self.obj1630.postAction( cobj0.RHS.CREATE )

   self.obj1631=operatingUnit(self)
   self.obj1631.preAction( cobj0.RHS.CREATE )
   self.obj1631.isGraphObjectVisual = True

   if(hasattr(self.obj1631, '_setHierarchicalLink')):
     self.obj1631._setHierarchicalLink(False)

   # OperCostProp
   self.obj1631.OperCostProp.setValue(0.0)

   # name
   self.obj1631.name.setValue('')
   self.obj1631.name.setNone()

   # OperCostFix
   self.obj1631.OperCostFix.setValue(0.0)

   self.obj1631.GGLabel.setValue(5)
   self.obj1631.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(60.0,220.0,self.obj1631)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1631.graphObject_ = new_obj
   self.obj16310= AttrCalc()
   self.obj16310.Copy=ATOM3Boolean()
   self.obj16310.Copy.setValue(('Copy from LHS', 1))
   self.obj16310.Copy.config = 0
   self.obj16310.Specify=ATOM3Constraint()
   self.obj16310.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1631.GGset2Any['OperCostProp']= self.obj16310
   self.obj16311= AttrCalc()
   self.obj16311.Copy=ATOM3Boolean()
   self.obj16311.Copy.setValue(('Copy from LHS', 0))
   self.obj16311.Copy.config = 0
   self.obj16311.Specify=ATOM3Constraint()
   self.obj16311.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()+\' \'+self.getMatched(graphID, self.LHS.nodeWithLabel(2)).name.getValue()\n\n\n\n'))
   self.obj1631.GGset2Any['name']= self.obj16311
   self.obj16312= AttrCalc()
   self.obj16312.Copy=ATOM3Boolean()
   self.obj16312.Copy.setValue(('Copy from LHS', 1))
   self.obj16312.Copy.config = 0
   self.obj16312.Specify=ATOM3Constraint()
   self.obj16312.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1631.GGset2Any['OperCostFix']= self.obj16312

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1631)
   self.obj1631.postAction( cobj0.RHS.CREATE )

   self.obj1632=GenericGraphEdge(self)
   self.obj1632.preAction( cobj0.RHS.CREATE )
   self.obj1632.isGraphObjectVisual = True

   if(hasattr(self.obj1632, '_setHierarchicalLink')):
     self.obj1632._setHierarchicalLink(False)

   self.obj1632.GGLabel.setValue(6)
   self.obj1632.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(103.5,161.5,self.obj1632)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1632.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1632)
   self.obj1632.postAction( cobj0.RHS.CREATE )

   self.obj1628.out_connections_.append(self.obj1630)
   self.obj1630.in_connections_.append(self.obj1628)
   self.obj1628.graphObject_.pendingConnections.append((self.obj1628.graphObject_.tag, self.obj1630.graphObject_.tag, [97.0, 102.0, 230.0, 173.0], 2, 0))
   self.obj1628.out_connections_.append(self.obj1632)
   self.obj1632.in_connections_.append(self.obj1628)
   self.obj1628.graphObject_.pendingConnections.append((self.obj1628.graphObject_.tag, self.obj1632.graphObject_.tag, [97.0, 102.0, 103.5, 161.5], 0, True))
   self.obj1630.out_connections_.append(self.obj1629)
   self.obj1629.in_connections_.append(self.obj1630)
   self.obj1630.graphObject_.pendingConnections.append((self.obj1630.graphObject_.tag, self.obj1629.graphObject_.tag, [351.0, 220.0, 230.0, 173.0], 2, 0))
   self.obj1632.out_connections_.append(self.obj1631)
   self.obj1631.in_connections_.append(self.obj1632)
   self.obj1632.graphObject_.pendingConnections.append((self.obj1632.graphObject_.tag, self.obj1631.graphObject_.tag, [110.0, 221.0, 103.5, 161.5], 0, True))

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

   self.obj1638=Goal(self)
   self.obj1638.preAction( cobj0.LHS.CREATE )
   self.obj1638.isGraphObjectVisual = True

   if(hasattr(self.obj1638, '_setHierarchicalLink')):
     self.obj1638._setHierarchicalLink(False)

   # name
   self.obj1638.name.setValue('')
   self.obj1638.name.setNone()

   self.obj1638.GGLabel.setValue(1)
   self.obj1638.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(80.0,80.0,self.obj1638)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1638.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1638)
   self.obj1638.postAction( cobj0.LHS.CREATE )


   cobj0.RHS = ASG_pns(self)
   cobj0.RHS.merge(ASG_omacs(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj1642=metarial(self)
   self.obj1642.preAction( cobj0.RHS.CREATE )
   self.obj1642.isGraphObjectVisual = True

   if(hasattr(self.obj1642, '_setHierarchicalLink')):
     self.obj1642._setHierarchicalLink(False)

   # MaxFlow
   self.obj1642.MaxFlow.setValue(999999)

   # price
   self.obj1642.price.setValue(0)

   # Name
   self.obj1642.Name.setValue('')
   self.obj1642.Name.setNone()

   # ReqFlow
   self.obj1642.ReqFlow.setValue(0)

   self.obj1642.GGLabel.setValue(2)
   self.obj1642.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(300.0,60.0,self.obj1642)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1642.graphObject_ = new_obj
   self.obj16420= AttrCalc()
   self.obj16420.Copy=ATOM3Boolean()
   self.obj16420.Copy.setValue(('Copy from LHS', 1))
   self.obj16420.Copy.config = 0
   self.obj16420.Specify=ATOM3Constraint()
   self.obj16420.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1642.GGset2Any['MaxFlow']= self.obj16420
   self.obj16421= AttrCalc()
   self.obj16421.Copy=ATOM3Boolean()
   self.obj16421.Copy.setValue(('Copy from LHS', 0))
   self.obj16421.Copy.config = 0
   self.obj16421.Specify=ATOM3Constraint()
   self.obj16421.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()\n'))
   self.obj1642.GGset2Any['Name']= self.obj16421
   self.obj16422= AttrCalc()
   self.obj16422.Copy=ATOM3Boolean()
   self.obj16422.Copy.setValue(('Copy from LHS', 1))
   self.obj16422.Copy.config = 0
   self.obj16422.Specify=ATOM3Constraint()
   self.obj16422.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1642.GGset2Any['ReqFlow']= self.obj16422

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1642)
   self.obj1642.postAction( cobj0.RHS.CREATE )

   self.obj1643=Goal(self)
   self.obj1643.preAction( cobj0.RHS.CREATE )
   self.obj1643.isGraphObjectVisual = True

   if(hasattr(self.obj1643, '_setHierarchicalLink')):
     self.obj1643._setHierarchicalLink(False)

   # name
   self.obj1643.name.setValue('')
   self.obj1643.name.setNone()

   self.obj1643.GGLabel.setValue(1)
   self.obj1643.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(80.0,80.0,self.obj1643)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1643.graphObject_ = new_obj
   self.obj16430= AttrCalc()
   self.obj16430.Copy=ATOM3Boolean()
   self.obj16430.Copy.setValue(('Copy from LHS', 1))
   self.obj16430.Copy.config = 0
   self.obj16430.Specify=ATOM3Constraint()
   self.obj16430.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1643.GGset2Any['name']= self.obj16430

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1643)
   self.obj1643.postAction( cobj0.RHS.CREATE )

   self.obj1644=GenericGraphEdge(self)
   self.obj1644.preAction( cobj0.RHS.CREATE )
   self.obj1644.isGraphObjectVisual = True

   if(hasattr(self.obj1644, '_setHierarchicalLink')):
     self.obj1644._setHierarchicalLink(False)

   self.obj1644.GGLabel.setValue(4)
   self.obj1644.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(209.5,91.5,self.obj1644)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1644.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1644)
   self.obj1644.postAction( cobj0.RHS.CREATE )

   self.obj1643.out_connections_.append(self.obj1644)
   self.obj1644.in_connections_.append(self.obj1643)
   self.obj1643.graphObject_.pendingConnections.append((self.obj1643.graphObject_.tag, self.obj1644.graphObject_.tag, [113.0, 81.0, 209.5, 91.5], 0, True))
   self.obj1644.out_connections_.append(self.obj1642)
   self.obj1642.in_connections_.append(self.obj1644)
   self.obj1644.graphObject_.pendingConnections.append((self.obj1644.graphObject_.tag, self.obj1642.graphObject_.tag, [306.0, 102.0, 209.5, 91.5], 0, True))

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

   self.obj1651=rawMaterial(self)
   self.obj1651.preAction( cobj0.LHS.CREATE )
   self.obj1651.isGraphObjectVisual = True

   if(hasattr(self.obj1651, '_setHierarchicalLink')):
     self.obj1651._setHierarchicalLink(False)

   # MaxFlow
   self.obj1651.MaxFlow.setValue(999999)

   # price
   self.obj1651.price.setValue(0)

   # Name
   self.obj1651.Name.setValue('')
   self.obj1651.Name.setNone()

   # ReqFlow
   self.obj1651.ReqFlow.setValue(0)

   self.obj1651.GGLabel.setValue(3)
   self.obj1651.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(220.0,20.0,self.obj1651)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1651.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1651)
   self.obj1651.postAction( cobj0.LHS.CREATE )

   self.obj1652=operatingUnit(self)
   self.obj1652.preAction( cobj0.LHS.CREATE )
   self.obj1652.isGraphObjectVisual = True

   if(hasattr(self.obj1652, '_setHierarchicalLink')):
     self.obj1652._setHierarchicalLink(False)

   # OperCostProp
   self.obj1652.OperCostProp.setValue(0.0)

   # name
   self.obj1652.name.setValue('')
   self.obj1652.name.setNone()

   # OperCostFix
   self.obj1652.OperCostFix.setValue(0.0)

   self.obj1652.GGLabel.setValue(2)
   self.obj1652.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(260.0,160.0,self.obj1652)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1652.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1652)
   self.obj1652.postAction( cobj0.LHS.CREATE )

   self.obj1653=Agent(self)
   self.obj1653.preAction( cobj0.LHS.CREATE )
   self.obj1653.isGraphObjectVisual = True

   if(hasattr(self.obj1653, '_setHierarchicalLink')):
     self.obj1653._setHierarchicalLink(False)

   # price
   self.obj1653.price.setNone()

   # name
   self.obj1653.name.setValue('')
   self.obj1653.name.setNone()

   self.obj1653.GGLabel.setValue(1)
   self.obj1653.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(80.0,120.0,self.obj1653)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1653.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1653)
   self.obj1653.postAction( cobj0.LHS.CREATE )

   self.obj1654=GenericGraphEdge(self)
   self.obj1654.preAction( cobj0.LHS.CREATE )
   self.obj1654.isGraphObjectVisual = True

   if(hasattr(self.obj1654, '_setHierarchicalLink')):
     self.obj1654._setHierarchicalLink(False)

   self.obj1654.GGLabel.setValue(4)
   self.obj1654.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(181.75,114.0,self.obj1654)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1654.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1654)
   self.obj1654.postAction( cobj0.LHS.CREATE )

   self.obj1655=GenericGraphEdge(self)
   self.obj1655.preAction( cobj0.LHS.CREATE )
   self.obj1655.isGraphObjectVisual = True

   if(hasattr(self.obj1655, '_setHierarchicalLink')):
     self.obj1655._setHierarchicalLink(False)

   self.obj1655.GGLabel.setValue(5)
   self.obj1655.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(229.25,150.25,self.obj1655)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1655.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1655)
   self.obj1655.postAction( cobj0.LHS.CREATE )

   self.obj1653.out_connections_.append(self.obj1654)
   self.obj1654.in_connections_.append(self.obj1653)
   self.obj1653.graphObject_.pendingConnections.append((self.obj1653.graphObject_.tag, self.obj1654.graphObject_.tag, [105.0, 182.0, 147.0, 140.5, 181.75, 114.0], 2, True))
   self.obj1653.out_connections_.append(self.obj1655)
   self.obj1655.in_connections_.append(self.obj1653)
   self.obj1653.graphObject_.pendingConnections.append((self.obj1653.graphObject_.tag, self.obj1655.graphObject_.tag, [105.0, 182.0, 185.5, 153.0, 229.25, 150.25], 2, True))
   self.obj1654.out_connections_.append(self.obj1651)
   self.obj1651.in_connections_.append(self.obj1654)
   self.obj1654.graphObject_.pendingConnections.append((self.obj1654.graphObject_.tag, self.obj1651.graphObject_.tag, [244.0, 76.0, 216.5, 87.5, 181.75, 114.0], 2, True))
   self.obj1655.out_connections_.append(self.obj1652)
   self.obj1652.in_connections_.append(self.obj1655)
   self.obj1655.graphObject_.pendingConnections.append((self.obj1655.graphObject_.tag, self.obj1652.graphObject_.tag, [280.0, 171.0, 273.0, 147.5, 229.25, 150.25], 2, True))

   cobj0.RHS = ASG_pns(self)
   cobj0.RHS.merge(ASG_omacs(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj1659=rawMaterial(self)
   self.obj1659.preAction( cobj0.RHS.CREATE )
   self.obj1659.isGraphObjectVisual = True

   if(hasattr(self.obj1659, '_setHierarchicalLink')):
     self.obj1659._setHierarchicalLink(False)

   # MaxFlow
   self.obj1659.MaxFlow.setValue(999999)

   # price
   self.obj1659.price.setValue(0)

   # Name
   self.obj1659.Name.setValue('')
   self.obj1659.Name.setNone()

   # ReqFlow
   self.obj1659.ReqFlow.setValue(0)

   self.obj1659.GGLabel.setValue(3)
   self.obj1659.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(220.0,20.0,self.obj1659)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1659.graphObject_ = new_obj
   self.obj16590= AttrCalc()
   self.obj16590.Copy=ATOM3Boolean()
   self.obj16590.Copy.setValue(('Copy from LHS', 1))
   self.obj16590.Copy.config = 0
   self.obj16590.Specify=ATOM3Constraint()
   self.obj16590.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1659.GGset2Any['MaxFlow']= self.obj16590
   self.obj16591= AttrCalc()
   self.obj16591.Copy=ATOM3Boolean()
   self.obj16591.Copy.setValue(('Copy from LHS', 1))
   self.obj16591.Copy.config = 0
   self.obj16591.Specify=ATOM3Constraint()
   self.obj16591.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1659.GGset2Any['Name']= self.obj16591
   self.obj16592= AttrCalc()
   self.obj16592.Copy=ATOM3Boolean()
   self.obj16592.Copy.setValue(('Copy from LHS', 1))
   self.obj16592.Copy.config = 0
   self.obj16592.Specify=ATOM3Constraint()
   self.obj16592.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1659.GGset2Any['ReqFlow']= self.obj16592

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1659)
   self.obj1659.postAction( cobj0.RHS.CREATE )

   self.obj1660=operatingUnit(self)
   self.obj1660.preAction( cobj0.RHS.CREATE )
   self.obj1660.isGraphObjectVisual = True

   if(hasattr(self.obj1660, '_setHierarchicalLink')):
     self.obj1660._setHierarchicalLink(False)

   # OperCostProp
   self.obj1660.OperCostProp.setValue(0.0)

   # name
   self.obj1660.name.setValue('')
   self.obj1660.name.setNone()

   # OperCostFix
   self.obj1660.OperCostFix.setValue(0.0)

   self.obj1660.GGLabel.setValue(2)
   self.obj1660.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(260.0,160.0,self.obj1660)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1660.graphObject_ = new_obj
   self.obj16600= AttrCalc()
   self.obj16600.Copy=ATOM3Boolean()
   self.obj16600.Copy.setValue(('Copy from LHS', 1))
   self.obj16600.Copy.config = 0
   self.obj16600.Specify=ATOM3Constraint()
   self.obj16600.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1660.GGset2Any['OperCostProp']= self.obj16600
   self.obj16601= AttrCalc()
   self.obj16601.Copy=ATOM3Boolean()
   self.obj16601.Copy.setValue(('Copy from LHS', 1))
   self.obj16601.Copy.config = 0
   self.obj16601.Specify=ATOM3Constraint()
   self.obj16601.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1660.GGset2Any['name']= self.obj16601
   self.obj16602= AttrCalc()
   self.obj16602.Copy=ATOM3Boolean()
   self.obj16602.Copy.setValue(('Copy from LHS', 1))
   self.obj16602.Copy.config = 0
   self.obj16602.Specify=ATOM3Constraint()
   self.obj16602.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1660.GGset2Any['OperCostFix']= self.obj16602

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1660)
   self.obj1660.postAction( cobj0.RHS.CREATE )

   self.obj1661=fromRaw(self)
   self.obj1661.preAction( cobj0.RHS.CREATE )
   self.obj1661.isGraphObjectVisual = True

   if(hasattr(self.obj1661, '_setHierarchicalLink')):
     self.obj1661._setHierarchicalLink(False)

   # rate
   self.obj1661.rate.setValue(1.0)

   self.obj1661.GGLabel.setValue(7)
   self.obj1661.graphClass_= graph_fromRaw
   if self.genGraphics:
      new_obj = graph_fromRaw(262.0,115.5,self.obj1661)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1661.graphObject_ = new_obj
   self.obj16610= AttrCalc()
   self.obj16610.Copy=ATOM3Boolean()
   self.obj16610.Copy.setValue(('Copy from LHS', 0))
   self.obj16610.Copy.config = 0
   self.obj16610.Specify=ATOM3Constraint()
   self.obj16610.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1661.GGset2Any['rate']= self.obj16610

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1661)
   self.obj1661.postAction( cobj0.RHS.CREATE )

   self.obj1662=Agent(self)
   self.obj1662.preAction( cobj0.RHS.CREATE )
   self.obj1662.isGraphObjectVisual = True

   if(hasattr(self.obj1662, '_setHierarchicalLink')):
     self.obj1662._setHierarchicalLink(False)

   # price
   self.obj1662.price.setNone()

   # name
   self.obj1662.name.setValue('')
   self.obj1662.name.setNone()

   self.obj1662.GGLabel.setValue(1)
   self.obj1662.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(80.0,120.0,self.obj1662)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1662.graphObject_ = new_obj
   self.obj16620= AttrCalc()
   self.obj16620.Copy=ATOM3Boolean()
   self.obj16620.Copy.setValue(('Copy from LHS', 1))
   self.obj16620.Copy.config = 0
   self.obj16620.Specify=ATOM3Constraint()
   self.obj16620.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1662.GGset2Any['price']= self.obj16620
   self.obj16621= AttrCalc()
   self.obj16621.Copy=ATOM3Boolean()
   self.obj16621.Copy.setValue(('Copy from LHS', 1))
   self.obj16621.Copy.config = 0
   self.obj16621.Specify=ATOM3Constraint()
   self.obj16621.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1662.GGset2Any['name']= self.obj16621

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1662)
   self.obj1662.postAction( cobj0.RHS.CREATE )

   self.obj1663=GenericGraphEdge(self)
   self.obj1663.preAction( cobj0.RHS.CREATE )
   self.obj1663.isGraphObjectVisual = True

   if(hasattr(self.obj1663, '_setHierarchicalLink')):
     self.obj1663._setHierarchicalLink(False)

   self.obj1663.GGLabel.setValue(4)
   self.obj1663.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(181.75,114.0,self.obj1663)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1663.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1663)
   self.obj1663.postAction( cobj0.RHS.CREATE )

   self.obj1664=GenericGraphEdge(self)
   self.obj1664.preAction( cobj0.RHS.CREATE )
   self.obj1664.isGraphObjectVisual = True

   if(hasattr(self.obj1664, '_setHierarchicalLink')):
     self.obj1664._setHierarchicalLink(False)

   self.obj1664.GGLabel.setValue(5)
   self.obj1664.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(229.25,150.25,self.obj1664)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1664.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1664)
   self.obj1664.postAction( cobj0.RHS.CREATE )

   self.obj1659.out_connections_.append(self.obj1661)
   self.obj1661.in_connections_.append(self.obj1659)
   self.obj1659.graphObject_.pendingConnections.append((self.obj1659.graphObject_.tag, self.obj1661.graphObject_.tag, [244.0, 70.0, 262.0, 115.5], 0, True))
   self.obj1661.out_connections_.append(self.obj1660)
   self.obj1660.in_connections_.append(self.obj1661)
   self.obj1661.graphObject_.pendingConnections.append((self.obj1661.graphObject_.tag, self.obj1660.graphObject_.tag, [280.0, 161.0, 262.0, 115.5], 0, True))
   self.obj1662.out_connections_.append(self.obj1663)
   self.obj1663.in_connections_.append(self.obj1662)
   self.obj1662.graphObject_.pendingConnections.append((self.obj1662.graphObject_.tag, self.obj1663.graphObject_.tag, [117.0, 182.0, 181.75, 114.0], 2, 0))
   self.obj1662.out_connections_.append(self.obj1664)
   self.obj1664.in_connections_.append(self.obj1662)
   self.obj1662.graphObject_.pendingConnections.append((self.obj1662.graphObject_.tag, self.obj1664.graphObject_.tag, [117.0, 182.0, 229.25, 150.25], 2, 0))
   self.obj1663.out_connections_.append(self.obj1659)
   self.obj1659.in_connections_.append(self.obj1663)
   self.obj1663.graphObject_.pendingConnections.append((self.obj1663.graphObject_.tag, self.obj1659.graphObject_.tag, [244.0, 70.0, 181.75, 114.0], 2, 0))
   self.obj1664.out_connections_.append(self.obj1660)
   self.obj1660.in_connections_.append(self.obj1664)
   self.obj1664.graphObject_.pendingConnections.append((self.obj1664.graphObject_.tag, self.obj1660.graphObject_.tag, [280.0, 161.0, 229.25, 150.25], 2, 0))

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

   self.obj1670=product(self)
   self.obj1670.preAction( cobj0.RHS.CREATE )
   self.obj1670.isGraphObjectVisual = True

   if(hasattr(self.obj1670, '_setHierarchicalLink')):
     self.obj1670._setHierarchicalLink(False)

   # MaxFlow
   self.obj1670.MaxFlow.setValue(999999)

   # price
   self.obj1670.price.setValue(0)

   # Name
   self.obj1670.Name.setValue('OAF')

   # ReqFlow
   self.obj1670.ReqFlow.setValue(0)

   self.obj1670.GGLabel.setValue(1)
   self.obj1670.graphClass_= graph_product
   if self.genGraphics:
      new_obj = graph_product(100.0,80.0,self.obj1670)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1670.graphObject_ = new_obj
   self.obj16700= AttrCalc()
   self.obj16700.Copy=ATOM3Boolean()
   self.obj16700.Copy.setValue(('Copy from LHS', 1))
   self.obj16700.Copy.config = 0
   self.obj16700.Specify=ATOM3Constraint()
   self.obj16700.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1670.GGset2Any['MaxFlow']= self.obj16700
   self.obj16701= AttrCalc()
   self.obj16701.Copy=ATOM3Boolean()
   self.obj16701.Copy.setValue(('Copy from LHS', 0))
   self.obj16701.Copy.config = 0
   self.obj16701.Specify=ATOM3Constraint()
   self.obj16701.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1670.GGset2Any['Name']= self.obj16701
   self.obj16702= AttrCalc()
   self.obj16702.Copy=ATOM3Boolean()
   self.obj16702.Copy.setValue(('Copy from LHS', 1))
   self.obj16702.Copy.config = 0
   self.obj16702.Specify=ATOM3Constraint()
   self.obj16702.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1670.GGset2Any['ReqFlow']= self.obj16702

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1670)
   self.obj1670.postAction( cobj0.RHS.CREATE )


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

   self.obj1677=product(self)
   self.obj1677.preAction( cobj0.LHS.CREATE )
   self.obj1677.isGraphObjectVisual = True

   if(hasattr(self.obj1677, '_setHierarchicalLink')):
     self.obj1677._setHierarchicalLink(False)

   # MaxFlow
   self.obj1677.MaxFlow.setNone()

   # price
   self.obj1677.price.setValue(0)

   # Name
   self.obj1677.Name.setValue('')
   self.obj1677.Name.setNone()

   # ReqFlow
   self.obj1677.ReqFlow.setNone()

   self.obj1677.GGLabel.setValue(5)
   self.obj1677.graphClass_= graph_product
   if self.genGraphics:
      new_obj = graph_product(280.0,220.0,self.obj1677)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1677.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1677)
   self.obj1677.postAction( cobj0.LHS.CREATE )

   self.obj1678=metarial(self)
   self.obj1678.preAction( cobj0.LHS.CREATE )
   self.obj1678.isGraphObjectVisual = True

   if(hasattr(self.obj1678, '_setHierarchicalLink')):
     self.obj1678._setHierarchicalLink(False)

   # MaxFlow
   self.obj1678.MaxFlow.setNone()

   # price
   self.obj1678.price.setValue(0)

   # Name
   self.obj1678.Name.setValue('')
   self.obj1678.Name.setNone()

   # ReqFlow
   self.obj1678.ReqFlow.setNone()

   self.obj1678.GGLabel.setValue(3)
   self.obj1678.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(320.0,40.0,self.obj1678)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1678.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1678)
   self.obj1678.postAction( cobj0.LHS.CREATE )

   self.obj1679=Goal(self)
   self.obj1679.preAction( cobj0.LHS.CREATE )
   self.obj1679.isGraphObjectVisual = True

   if(hasattr(self.obj1679, '_setHierarchicalLink')):
     self.obj1679._setHierarchicalLink(False)

   # name
   self.obj1679.name.setValue('')
   self.obj1679.name.setNone()

   self.obj1679.GGLabel.setValue(2)
   self.obj1679.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(180.0,60.0,self.obj1679)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1679.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1679)
   self.obj1679.postAction( cobj0.LHS.CREATE )

   self.obj1680=GenericGraphEdge(self)
   self.obj1680.preAction( cobj0.LHS.CREATE )
   self.obj1680.isGraphObjectVisual = True

   if(hasattr(self.obj1680, '_setHierarchicalLink')):
     self.obj1680._setHierarchicalLink(False)

   self.obj1680.GGLabel.setValue(4)
   self.obj1680.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(264.5,71.5,self.obj1680)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1680.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1680)
   self.obj1680.postAction( cobj0.LHS.CREATE )

   self.obj1679.out_connections_.append(self.obj1680)
   self.obj1680.in_connections_.append(self.obj1679)
   self.obj1679.graphObject_.pendingConnections.append((self.obj1679.graphObject_.tag, self.obj1680.graphObject_.tag, [203.0, 61.0, 264.5, 71.5], 0, True))
   self.obj1680.out_connections_.append(self.obj1678)
   self.obj1678.in_connections_.append(self.obj1680)
   self.obj1680.graphObject_.pendingConnections.append((self.obj1680.graphObject_.tag, self.obj1678.graphObject_.tag, [326.0, 82.0, 264.5, 71.5], 0, True))

   cobj0.RHS = ASG_pns(self)
   cobj0.RHS.merge(ASG_omacs(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj1684=product(self)
   self.obj1684.preAction( cobj0.RHS.CREATE )
   self.obj1684.isGraphObjectVisual = True

   if(hasattr(self.obj1684, '_setHierarchicalLink')):
     self.obj1684._setHierarchicalLink(False)

   # MaxFlow
   self.obj1684.MaxFlow.setNone()

   # price
   self.obj1684.price.setValue(0)

   # Name
   self.obj1684.Name.setValue('')
   self.obj1684.Name.setNone()

   # ReqFlow
   self.obj1684.ReqFlow.setNone()

   self.obj1684.GGLabel.setValue(5)
   self.obj1684.graphClass_= graph_product
   if self.genGraphics:
      new_obj = graph_product(280.0,220.0,self.obj1684)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1684.graphObject_ = new_obj
   self.obj16840= AttrCalc()
   self.obj16840.Copy=ATOM3Boolean()
   self.obj16840.Copy.setValue(('Copy from LHS', 1))
   self.obj16840.Copy.config = 0
   self.obj16840.Specify=ATOM3Constraint()
   self.obj16840.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1684.GGset2Any['MaxFlow']= self.obj16840
   self.obj16841= AttrCalc()
   self.obj16841.Copy=ATOM3Boolean()
   self.obj16841.Copy.setValue(('Copy from LHS', 1))
   self.obj16841.Copy.config = 0
   self.obj16841.Specify=ATOM3Constraint()
   self.obj16841.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1684.GGset2Any['Name']= self.obj16841
   self.obj16842= AttrCalc()
   self.obj16842.Copy=ATOM3Boolean()
   self.obj16842.Copy.setValue(('Copy from LHS', 1))
   self.obj16842.Copy.config = 0
   self.obj16842.Specify=ATOM3Constraint()
   self.obj16842.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1684.GGset2Any['ReqFlow']= self.obj16842

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1684)
   self.obj1684.postAction( cobj0.RHS.CREATE )

   self.obj1685=metarial(self)
   self.obj1685.preAction( cobj0.RHS.CREATE )
   self.obj1685.isGraphObjectVisual = True

   if(hasattr(self.obj1685, '_setHierarchicalLink')):
     self.obj1685._setHierarchicalLink(False)

   # MaxFlow
   self.obj1685.MaxFlow.setNone()

   # price
   self.obj1685.price.setValue(0)

   # Name
   self.obj1685.Name.setValue('')
   self.obj1685.Name.setNone()

   # ReqFlow
   self.obj1685.ReqFlow.setNone()

   self.obj1685.GGLabel.setValue(3)
   self.obj1685.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(320.0,40.0,self.obj1685)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1685.graphObject_ = new_obj
   self.obj16850= AttrCalc()
   self.obj16850.Copy=ATOM3Boolean()
   self.obj16850.Copy.setValue(('Copy from LHS', 1))
   self.obj16850.Copy.config = 0
   self.obj16850.Specify=ATOM3Constraint()
   self.obj16850.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1685.GGset2Any['MaxFlow']= self.obj16850
   self.obj16851= AttrCalc()
   self.obj16851.Copy=ATOM3Boolean()
   self.obj16851.Copy.setValue(('Copy from LHS', 1))
   self.obj16851.Copy.config = 0
   self.obj16851.Specify=ATOM3Constraint()
   self.obj16851.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1685.GGset2Any['Name']= self.obj16851
   self.obj16852= AttrCalc()
   self.obj16852.Copy=ATOM3Boolean()
   self.obj16852.Copy.setValue(('Copy from LHS', 1))
   self.obj16852.Copy.config = 0
   self.obj16852.Specify=ATOM3Constraint()
   self.obj16852.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1685.GGset2Any['ReqFlow']= self.obj16852

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1685)
   self.obj1685.postAction( cobj0.RHS.CREATE )

   self.obj1686=operatingUnit(self)
   self.obj1686.preAction( cobj0.RHS.CREATE )
   self.obj1686.isGraphObjectVisual = True

   if(hasattr(self.obj1686, '_setHierarchicalLink')):
     self.obj1686._setHierarchicalLink(False)

   # OperCostProp
   self.obj1686.OperCostProp.setValue(1.0)

   # name
   self.obj1686.name.setValue('')
   self.obj1686.name.setNone()

   # OperCostFix
   self.obj1686.OperCostFix.setValue(2.0)

   self.obj1686.GGLabel.setValue(7)
   self.obj1686.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(320.0,140.0,self.obj1686)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1686.graphObject_ = new_obj
   self.obj16860= AttrCalc()
   self.obj16860.Copy=ATOM3Boolean()
   self.obj16860.Copy.setValue(('Copy from LHS', 0))
   self.obj16860.Copy.config = 0
   self.obj16860.Specify=ATOM3Constraint()
   self.obj16860.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1686.GGset2Any['OperCostProp']= self.obj16860
   self.obj16861= AttrCalc()
   self.obj16861.Copy=ATOM3Boolean()
   self.obj16861.Copy.setValue(('Copy from LHS', 0))
   self.obj16861.Copy.config = 0
   self.obj16861.Specify=ATOM3Constraint()
   self.obj16861.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(2)).name.getValue()+\' OAF\'\n'))
   self.obj1686.GGset2Any['name']= self.obj16861
   self.obj16862= AttrCalc()
   self.obj16862.Copy=ATOM3Boolean()
   self.obj16862.Copy.setValue(('Copy from LHS', 0))
   self.obj16862.Copy.config = 0
   self.obj16862.Specify=ATOM3Constraint()
   self.obj16862.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1686.GGset2Any['OperCostFix']= self.obj16862

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1686)
   self.obj1686.postAction( cobj0.RHS.CREATE )

   self.obj1687=intoProduct(self)
   self.obj1687.preAction( cobj0.RHS.CREATE )
   self.obj1687.isGraphObjectVisual = True

   if(hasattr(self.obj1687, '_setHierarchicalLink')):
     self.obj1687._setHierarchicalLink(False)

   # rate
   self.obj1687.rate.setValue(1.0)

   self.obj1687.GGLabel.setValue(9)
   self.obj1687.graphClass_= graph_intoProduct
   if self.genGraphics:
      new_obj = graph_intoProduct(322.0,179.0,self.obj1687)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1687.graphObject_ = new_obj
   self.obj16870= AttrCalc()
   self.obj16870.Copy=ATOM3Boolean()
   self.obj16870.Copy.setValue(('Copy from LHS', 0))
   self.obj16870.Copy.config = 0
   self.obj16870.Specify=ATOM3Constraint()
   self.obj16870.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1687.GGset2Any['rate']= self.obj16870

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1687)
   self.obj1687.postAction( cobj0.RHS.CREATE )

   self.obj1688=fromMaterial(self)
   self.obj1688.preAction( cobj0.RHS.CREATE )
   self.obj1688.isGraphObjectVisual = True

   if(hasattr(self.obj1688, '_setHierarchicalLink')):
     self.obj1688._setHierarchicalLink(False)

   # rate
   self.obj1688.rate.setValue(1.0)

   self.obj1688.GGLabel.setValue(8)
   self.obj1688.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(342.0,110.0,self.obj1688)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1688.graphObject_ = new_obj
   self.obj16880= AttrCalc()
   self.obj16880.Copy=ATOM3Boolean()
   self.obj16880.Copy.setValue(('Copy from LHS', 0))
   self.obj16880.Copy.config = 0
   self.obj16880.Specify=ATOM3Constraint()
   self.obj16880.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1688.GGset2Any['rate']= self.obj16880

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1688)
   self.obj1688.postAction( cobj0.RHS.CREATE )

   self.obj1689=Goal(self)
   self.obj1689.preAction( cobj0.RHS.CREATE )
   self.obj1689.isGraphObjectVisual = True

   if(hasattr(self.obj1689, '_setHierarchicalLink')):
     self.obj1689._setHierarchicalLink(False)

   # name
   self.obj1689.name.setValue('')
   self.obj1689.name.setNone()

   self.obj1689.GGLabel.setValue(2)
   self.obj1689.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(180.0,60.0,self.obj1689)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1689.graphObject_ = new_obj
   self.obj16890= AttrCalc()
   self.obj16890.Copy=ATOM3Boolean()
   self.obj16890.Copy.setValue(('Copy from LHS', 1))
   self.obj16890.Copy.config = 0
   self.obj16890.Specify=ATOM3Constraint()
   self.obj16890.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1689.GGset2Any['name']= self.obj16890

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1689)
   self.obj1689.postAction( cobj0.RHS.CREATE )

   self.obj1690=GenericGraphEdge(self)
   self.obj1690.preAction( cobj0.RHS.CREATE )
   self.obj1690.isGraphObjectVisual = True

   if(hasattr(self.obj1690, '_setHierarchicalLink')):
     self.obj1690._setHierarchicalLink(False)

   self.obj1690.GGLabel.setValue(4)
   self.obj1690.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(264.5,71.5,self.obj1690)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1690.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1690)
   self.obj1690.postAction( cobj0.RHS.CREATE )

   self.obj1685.out_connections_.append(self.obj1688)
   self.obj1688.in_connections_.append(self.obj1685)
   self.obj1685.graphObject_.pendingConnections.append((self.obj1685.graphObject_.tag, self.obj1688.graphObject_.tag, [244.0, 89.0, 342.0, 110.0], 0, True))
   self.obj1686.out_connections_.append(self.obj1687)
   self.obj1687.in_connections_.append(self.obj1686)
   self.obj1686.graphObject_.pendingConnections.append((self.obj1686.graphObject_.tag, self.obj1687.graphObject_.tag, [339.0, 158.0, 322.0, 179.0], 0, True))
   self.obj1687.out_connections_.append(self.obj1684)
   self.obj1684.in_connections_.append(self.obj1687)
   self.obj1687.graphObject_.pendingConnections.append((self.obj1687.graphObject_.tag, self.obj1684.graphObject_.tag, [305.0, 220.0, 322.0, 179.0], 0, True))
   self.obj1688.out_connections_.append(self.obj1686)
   self.obj1686.in_connections_.append(self.obj1688)
   self.obj1688.graphObject_.pendingConnections.append((self.obj1688.graphObject_.tag, self.obj1686.graphObject_.tag, [340.0, 151.0, 342.0, 110.0], 0, True))
   self.obj1689.out_connections_.append(self.obj1690)
   self.obj1690.in_connections_.append(self.obj1689)
   self.obj1689.graphObject_.pendingConnections.append((self.obj1689.graphObject_.tag, self.obj1690.graphObject_.tag, [93.0, 61.0, 264.5, 71.5], 2, 0))
   self.obj1690.out_connections_.append(self.obj1685)
   self.obj1685.in_connections_.append(self.obj1690)
   self.obj1690.graphObject_.pendingConnections.append((self.obj1690.graphObject_.tag, self.obj1685.graphObject_.tag, [226.0, 82.0, 264.5, 71.5], 2, 0))

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

   self.obj1696=CapableOf(self)
   self.obj1696.preAction( cobj0.LHS.CREATE )
   self.obj1696.isGraphObjectVisual = True

   if(hasattr(self.obj1696, '_setHierarchicalLink')):
     self.obj1696._setHierarchicalLink(False)

   # rate
   self.obj1696.rate.setNone()

   self.obj1696.GGLabel.setValue(4)
   self.obj1696.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(250.75,110.75,self.obj1696)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1696.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1696)
   self.obj1696.postAction( cobj0.LHS.CREATE )

   self.obj1697=Goal(self)
   self.obj1697.preAction( cobj0.LHS.CREATE )
   self.obj1697.isGraphObjectVisual = True

   if(hasattr(self.obj1697, '_setHierarchicalLink')):
     self.obj1697._setHierarchicalLink(False)

   # name
   self.obj1697.name.setValue('')
   self.obj1697.name.setNone()

   self.obj1697.GGLabel.setValue(3)
   self.obj1697.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(100.0,240.0,self.obj1697)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1697.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1697)
   self.obj1697.postAction( cobj0.LHS.CREATE )

   self.obj1698=Agent(self)
   self.obj1698.preAction( cobj0.LHS.CREATE )
   self.obj1698.isGraphObjectVisual = True

   if(hasattr(self.obj1698, '_setHierarchicalLink')):
     self.obj1698._setHierarchicalLink(False)

   # price
   self.obj1698.price.setNone()

   # name
   self.obj1698.name.setValue('')
   self.obj1698.name.setNone()

   self.obj1698.GGLabel.setValue(1)
   self.obj1698.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(80.0,40.0,self.obj1698)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1698.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1698)
   self.obj1698.postAction( cobj0.LHS.CREATE )

   self.obj1699=Role(self)
   self.obj1699.preAction( cobj0.LHS.CREATE )
   self.obj1699.isGraphObjectVisual = True

   if(hasattr(self.obj1699, '_setHierarchicalLink')):
     self.obj1699._setHierarchicalLink(False)

   # name
   self.obj1699.name.setValue('')
   self.obj1699.name.setNone()

   self.obj1699.GGLabel.setValue(2)
   self.obj1699.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(280.0,140.0,self.obj1699)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1699.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1699)
   self.obj1699.postAction( cobj0.LHS.CREATE )

   self.obj1700=achieve(self)
   self.obj1700.preAction( cobj0.LHS.CREATE )
   self.obj1700.isGraphObjectVisual = True

   if(hasattr(self.obj1700, '_setHierarchicalLink')):
     self.obj1700._setHierarchicalLink(False)

   # rate
   self.obj1700.rate.setNone()

   self.obj1700.GGLabel.setValue(5)
   self.obj1700.graphClass_= graph_achieve
   if self.genGraphics:
      new_obj = graph_achieve(258.5,259.0,self.obj1700)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1700.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1700)
   self.obj1700.postAction( cobj0.LHS.CREATE )

   self.obj1696.out_connections_.append(self.obj1699)
   self.obj1699.in_connections_.append(self.obj1696)
   self.obj1696.graphObject_.pendingConnections.append((self.obj1696.graphObject_.tag, self.obj1699.graphObject_.tag, [304.0, 141.0, 300.5, 120.5, 250.75, 110.75], 2, True))
   self.obj1698.out_connections_.append(self.obj1696)
   self.obj1696.in_connections_.append(self.obj1698)
   self.obj1698.graphObject_.pendingConnections.append((self.obj1698.graphObject_.tag, self.obj1696.graphObject_.tag, [105.0, 102.0, 201.0, 101.0, 250.75, 110.75], 2, True))
   self.obj1699.out_connections_.append(self.obj1700)
   self.obj1700.in_connections_.append(self.obj1699)
   self.obj1699.graphObject_.pendingConnections.append((self.obj1699.graphObject_.tag, self.obj1700.graphObject_.tag, [304.0, 186.0, 303.5, 233.0, 258.5, 259.0], 2, True))
   self.obj1700.out_connections_.append(self.obj1697)
   self.obj1697.in_connections_.append(self.obj1700)
   self.obj1700.graphObject_.pendingConnections.append((self.obj1700.graphObject_.tag, self.obj1697.graphObject_.tag, [124.0, 290.0, 213.5, 285.0, 258.5, 259.0], 2, True))

   cobj0.RHS = ASG_pns(self)
   cobj0.RHS.merge(ASG_omacs(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj1704=metarial(self)
   self.obj1704.preAction( cobj0.RHS.CREATE )
   self.obj1704.isGraphObjectVisual = True

   if(hasattr(self.obj1704, '_setHierarchicalLink')):
     self.obj1704._setHierarchicalLink(False)

   # MaxFlow
   self.obj1704.MaxFlow.setValue(999999)

   # price
   self.obj1704.price.setValue(0)

   # Name
   self.obj1704.Name.setValue('')
   self.obj1704.Name.setNone()

   # ReqFlow
   self.obj1704.ReqFlow.setValue(0)

   self.obj1704.GGLabel.setValue(8)
   self.obj1704.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(400.0,80.0,self.obj1704)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1704.graphObject_ = new_obj
   self.obj17040= AttrCalc()
   self.obj17040.Copy=ATOM3Boolean()
   self.obj17040.Copy.setValue(('Copy from LHS', 1))
   self.obj17040.Copy.config = 0
   self.obj17040.Specify=ATOM3Constraint()
   self.obj17040.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1704.GGset2Any['MaxFlow']= self.obj17040
   self.obj17041= AttrCalc()
   self.obj17041.Copy=ATOM3Boolean()
   self.obj17041.Copy.setValue(('Copy from LHS', 0))
   self.obj17041.Copy.config = 0
   self.obj17041.Specify=ATOM3Constraint()
   self.obj17041.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()+\' \'+ self.getMatched(graphID, self.LHS.nodeWithLabel(2)).name.getValue()+\' \'+ self.getMatched(graphID, self.LHS.nodeWithLabel(3)).name.getValue()\n\n'))
   self.obj1704.GGset2Any['Name']= self.obj17041
   self.obj17042= AttrCalc()
   self.obj17042.Copy=ATOM3Boolean()
   self.obj17042.Copy.setValue(('Copy from LHS', 1))
   self.obj17042.Copy.config = 0
   self.obj17042.Specify=ATOM3Constraint()
   self.obj17042.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1704.GGset2Any['ReqFlow']= self.obj17042

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1704)
   self.obj1704.postAction( cobj0.RHS.CREATE )

   self.obj1705=operatingUnit(self)
   self.obj1705.preAction( cobj0.RHS.CREATE )
   self.obj1705.isGraphObjectVisual = True

   if(hasattr(self.obj1705, '_setHierarchicalLink')):
     self.obj1705._setHierarchicalLink(False)

   # OperCostProp
   self.obj1705.OperCostProp.setValue(0.0)

   # name
   self.obj1705.name.setValue('')
   self.obj1705.name.setNone()

   # OperCostFix
   self.obj1705.OperCostFix.setValue(0.0)

   self.obj1705.GGLabel.setValue(7)
   self.obj1705.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(400.0,240.0,self.obj1705)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1705.graphObject_ = new_obj
   self.obj17050= AttrCalc()
   self.obj17050.Copy=ATOM3Boolean()
   self.obj17050.Copy.setValue(('Copy from LHS', 0))
   self.obj17050.Copy.config = 0
   self.obj17050.Specify=ATOM3Constraint()
   self.obj17050.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(5)).rate.getValue()\n'))
   self.obj1705.GGset2Any['OperCostProp']= self.obj17050
   self.obj17051= AttrCalc()
   self.obj17051.Copy=ATOM3Boolean()
   self.obj17051.Copy.setValue(('Copy from LHS', 0))
   self.obj17051.Copy.config = 0
   self.obj17051.Specify=ATOM3Constraint()
   self.obj17051.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()+\' \'+ self.getMatched(graphID, self.LHS.nodeWithLabel(2)).name.getValue()+\' \'+ self.getMatched(graphID, self.LHS.nodeWithLabel(3)).name.getValue()\n\n\n\n\n\n\n'))
   self.obj1705.GGset2Any['name']= self.obj17051
   self.obj17052= AttrCalc()
   self.obj17052.Copy=ATOM3Boolean()
   self.obj17052.Copy.setValue(('Copy from LHS', 0))
   self.obj17052.Copy.config = 0
   self.obj17052.Specify=ATOM3Constraint()
   self.obj17052.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return 2.0\n'))
   self.obj1705.GGset2Any['OperCostFix']= self.obj17052

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1705)
   self.obj1705.postAction( cobj0.RHS.CREATE )

   self.obj1706=fromMaterial(self)
   self.obj1706.preAction( cobj0.RHS.CREATE )
   self.obj1706.isGraphObjectVisual = True

   if(hasattr(self.obj1706, '_setHierarchicalLink')):
     self.obj1706._setHierarchicalLink(False)

   # rate
   self.obj1706.rate.setValue(1.0)

   self.obj1706.GGLabel.setValue(9)
   self.obj1706.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(422.0,190.0,self.obj1706)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1706.graphObject_ = new_obj
   self.obj17060= AttrCalc()
   self.obj17060.Copy=ATOM3Boolean()
   self.obj17060.Copy.setValue(('Copy from LHS', 0))
   self.obj17060.Copy.config = 0
   self.obj17060.Specify=ATOM3Constraint()
   self.obj17060.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1706.GGset2Any['rate']= self.obj17060

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1706)
   self.obj1706.postAction( cobj0.RHS.CREATE )

   self.obj1707=CapableOf(self)
   self.obj1707.preAction( cobj0.RHS.CREATE )
   self.obj1707.isGraphObjectVisual = True

   if(hasattr(self.obj1707, '_setHierarchicalLink')):
     self.obj1707._setHierarchicalLink(False)

   # rate
   self.obj1707.rate.setNone()

   self.obj1707.GGLabel.setValue(4)
   self.obj1707.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(250.75,110.75,self.obj1707)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1707.graphObject_ = new_obj
   self.obj17070= AttrCalc()
   self.obj17070.Copy=ATOM3Boolean()
   self.obj17070.Copy.setValue(('Copy from LHS', 1))
   self.obj17070.Copy.config = 0
   self.obj17070.Specify=ATOM3Constraint()
   self.obj17070.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1707.GGset2Any['rate']= self.obj17070

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1707)
   self.obj1707.postAction( cobj0.RHS.CREATE )

   self.obj1708=Goal(self)
   self.obj1708.preAction( cobj0.RHS.CREATE )
   self.obj1708.isGraphObjectVisual = True

   if(hasattr(self.obj1708, '_setHierarchicalLink')):
     self.obj1708._setHierarchicalLink(False)

   # name
   self.obj1708.name.setValue('')
   self.obj1708.name.setNone()

   self.obj1708.GGLabel.setValue(3)
   self.obj1708.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(100.0,240.0,self.obj1708)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1708.graphObject_ = new_obj
   self.obj17080= AttrCalc()
   self.obj17080.Copy=ATOM3Boolean()
   self.obj17080.Copy.setValue(('Copy from LHS', 1))
   self.obj17080.Copy.config = 0
   self.obj17080.Specify=ATOM3Constraint()
   self.obj17080.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1708.GGset2Any['name']= self.obj17080

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1708)
   self.obj1708.postAction( cobj0.RHS.CREATE )

   self.obj1709=Agent(self)
   self.obj1709.preAction( cobj0.RHS.CREATE )
   self.obj1709.isGraphObjectVisual = True

   if(hasattr(self.obj1709, '_setHierarchicalLink')):
     self.obj1709._setHierarchicalLink(False)

   # price
   self.obj1709.price.setNone()

   # name
   self.obj1709.name.setValue('')
   self.obj1709.name.setNone()

   self.obj1709.GGLabel.setValue(1)
   self.obj1709.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(80.0,40.0,self.obj1709)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1709.graphObject_ = new_obj
   self.obj17090= AttrCalc()
   self.obj17090.Copy=ATOM3Boolean()
   self.obj17090.Copy.setValue(('Copy from LHS', 1))
   self.obj17090.Copy.config = 0
   self.obj17090.Specify=ATOM3Constraint()
   self.obj17090.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1709.GGset2Any['price']= self.obj17090
   self.obj17091= AttrCalc()
   self.obj17091.Copy=ATOM3Boolean()
   self.obj17091.Copy.setValue(('Copy from LHS', 1))
   self.obj17091.Copy.config = 0
   self.obj17091.Specify=ATOM3Constraint()
   self.obj17091.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1709.GGset2Any['name']= self.obj17091

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1709)
   self.obj1709.postAction( cobj0.RHS.CREATE )

   self.obj1710=Role(self)
   self.obj1710.preAction( cobj0.RHS.CREATE )
   self.obj1710.isGraphObjectVisual = True

   if(hasattr(self.obj1710, '_setHierarchicalLink')):
     self.obj1710._setHierarchicalLink(False)

   # name
   self.obj1710.name.setValue('')
   self.obj1710.name.setNone()

   self.obj1710.GGLabel.setValue(2)
   self.obj1710.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(280.0,140.0,self.obj1710)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1710.graphObject_ = new_obj
   self.obj17100= AttrCalc()
   self.obj17100.Copy=ATOM3Boolean()
   self.obj17100.Copy.setValue(('Copy from LHS', 1))
   self.obj17100.Copy.config = 0
   self.obj17100.Specify=ATOM3Constraint()
   self.obj17100.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1710.GGset2Any['name']= self.obj17100

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1710)
   self.obj1710.postAction( cobj0.RHS.CREATE )

   self.obj1711=achieve(self)
   self.obj1711.preAction( cobj0.RHS.CREATE )
   self.obj1711.isGraphObjectVisual = True

   if(hasattr(self.obj1711, '_setHierarchicalLink')):
     self.obj1711._setHierarchicalLink(False)

   # rate
   self.obj1711.rate.setNone()

   self.obj1711.GGLabel.setValue(5)
   self.obj1711.graphClass_= graph_achieve
   if self.genGraphics:
      new_obj = graph_achieve(258.5,259.0,self.obj1711)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1711.graphObject_ = new_obj
   self.obj17110= AttrCalc()
   self.obj17110.Copy=ATOM3Boolean()
   self.obj17110.Copy.setValue(('Copy from LHS', 1))
   self.obj17110.Copy.config = 0
   self.obj17110.Specify=ATOM3Constraint()
   self.obj17110.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1711.GGset2Any['rate']= self.obj17110

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1711)
   self.obj1711.postAction( cobj0.RHS.CREATE )

   self.obj1712=GenericGraphEdge(self)
   self.obj1712.preAction( cobj0.RHS.CREATE )
   self.obj1712.isGraphObjectVisual = True

   if(hasattr(self.obj1712, '_setHierarchicalLink')):
     self.obj1712._setHierarchicalLink(False)

   self.obj1712.GGLabel.setValue(10)
   self.obj1712.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(358.5,131.0,self.obj1712)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1712.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1712)
   self.obj1712.postAction( cobj0.RHS.CREATE )

   self.obj1704.out_connections_.append(self.obj1706)
   self.obj1706.in_connections_.append(self.obj1704)
   self.obj1704.graphObject_.pendingConnections.append((self.obj1704.graphObject_.tag, self.obj1706.graphObject_.tag, [424.0, 129.0, 422.0, 190.0], 0, True))
   self.obj1706.out_connections_.append(self.obj1705)
   self.obj1705.in_connections_.append(self.obj1706)
   self.obj1706.graphObject_.pendingConnections.append((self.obj1706.graphObject_.tag, self.obj1705.graphObject_.tag, [420.0, 251.0, 422.0, 190.0], 0, True))
   self.obj1707.out_connections_.append(self.obj1710)
   self.obj1710.in_connections_.append(self.obj1707)
   self.obj1707.graphObject_.pendingConnections.append((self.obj1707.graphObject_.tag, self.obj1710.graphObject_.tag, [311.0, 140.0, 250.75, 110.75], 2, 0))
   self.obj1709.out_connections_.append(self.obj1707)
   self.obj1707.in_connections_.append(self.obj1709)
   self.obj1709.graphObject_.pendingConnections.append((self.obj1709.graphObject_.tag, self.obj1707.graphObject_.tag, [117.0, 102.0, 250.75, 110.75], 2, 0))
   self.obj1710.out_connections_.append(self.obj1711)
   self.obj1711.in_connections_.append(self.obj1710)
   self.obj1710.graphObject_.pendingConnections.append((self.obj1710.graphObject_.tag, self.obj1711.graphObject_.tag, [311.0, 185.0, 258.5, 259.0], 2, 0))
   self.obj1710.out_connections_.append(self.obj1712)
   self.obj1712.in_connections_.append(self.obj1710)
   self.obj1710.graphObject_.pendingConnections.append((self.obj1710.graphObject_.tag, self.obj1712.graphObject_.tag, [311.0, 140.0, 358.5, 131.0], 0, True))
   self.obj1711.out_connections_.append(self.obj1708)
   self.obj1708.in_connections_.append(self.obj1711)
   self.obj1711.graphObject_.pendingConnections.append((self.obj1711.graphObject_.tag, self.obj1708.graphObject_.tag, [134.0, 290.0, 258.5, 259.0], 2, 0))
   self.obj1712.out_connections_.append(self.obj1704)
   self.obj1704.in_connections_.append(self.obj1712)
   self.obj1712.graphObject_.pendingConnections.append((self.obj1712.graphObject_.tag, self.obj1704.graphObject_.tag, [406.0, 122.0, 358.5, 131.0], 0, True))

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

   self.obj1719=metarial(self)
   self.obj1719.preAction( cobj0.LHS.CREATE )
   self.obj1719.isGraphObjectVisual = True

   if(hasattr(self.obj1719, '_setHierarchicalLink')):
     self.obj1719._setHierarchicalLink(False)

   # MaxFlow
   self.obj1719.MaxFlow.setNone()

   # price
   self.obj1719.price.setValue(0)

   # Name
   self.obj1719.Name.setValue('')
   self.obj1719.Name.setNone()

   # ReqFlow
   self.obj1719.ReqFlow.setNone()

   self.obj1719.GGLabel.setValue(4)
   self.obj1719.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(240.0,20.0,self.obj1719)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1719.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1719)
   self.obj1719.postAction( cobj0.LHS.CREATE )

   self.obj1720=metarial(self)
   self.obj1720.preAction( cobj0.LHS.CREATE )
   self.obj1720.isGraphObjectVisual = True

   if(hasattr(self.obj1720, '_setHierarchicalLink')):
     self.obj1720._setHierarchicalLink(False)

   # MaxFlow
   self.obj1720.MaxFlow.setNone()

   # price
   self.obj1720.price.setValue(0)

   # Name
   self.obj1720.Name.setValue('')
   self.obj1720.Name.setNone()

   # ReqFlow
   self.obj1720.ReqFlow.setNone()

   self.obj1720.GGLabel.setValue(6)
   self.obj1720.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(240.0,240.0,self.obj1720)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1720.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1720)
   self.obj1720.postAction( cobj0.LHS.CREATE )

   self.obj1721=operatingUnit(self)
   self.obj1721.preAction( cobj0.LHS.CREATE )
   self.obj1721.isGraphObjectVisual = True

   if(hasattr(self.obj1721, '_setHierarchicalLink')):
     self.obj1721._setHierarchicalLink(False)

   # OperCostProp
   self.obj1721.OperCostProp.setNone()

   # name
   self.obj1721.name.setValue('')
   self.obj1721.name.setNone()

   # OperCostFix
   self.obj1721.OperCostFix.setNone()

   self.obj1721.GGLabel.setValue(5)
   self.obj1721.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(240.0,140.0,self.obj1721)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1721.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1721)
   self.obj1721.postAction( cobj0.LHS.CREATE )

   self.obj1722=fromMaterial(self)
   self.obj1722.preAction( cobj0.LHS.CREATE )
   self.obj1722.isGraphObjectVisual = True

   if(hasattr(self.obj1722, '_setHierarchicalLink')):
     self.obj1722._setHierarchicalLink(False)

   # rate
   self.obj1722.rate.setNone()

   self.obj1722.GGLabel.setValue(8)
   self.obj1722.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(265.0,100.0,self.obj1722)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1722.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1722)
   self.obj1722.postAction( cobj0.LHS.CREATE )

   self.obj1723=Goal(self)
   self.obj1723.preAction( cobj0.LHS.CREATE )
   self.obj1723.isGraphObjectVisual = True

   if(hasattr(self.obj1723, '_setHierarchicalLink')):
     self.obj1723._setHierarchicalLink(False)

   # name
   self.obj1723.name.setValue('')
   self.obj1723.name.setNone()

   self.obj1723.GGLabel.setValue(2)
   self.obj1723.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(60.0,220.0,self.obj1723)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1723.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1723)
   self.obj1723.postAction( cobj0.LHS.CREATE )

   self.obj1724=Role(self)
   self.obj1724.preAction( cobj0.LHS.CREATE )
   self.obj1724.isGraphObjectVisual = True

   if(hasattr(self.obj1724, '_setHierarchicalLink')):
     self.obj1724._setHierarchicalLink(False)

   # name
   self.obj1724.name.setValue('')
   self.obj1724.name.setNone()

   self.obj1724.GGLabel.setValue(1)
   self.obj1724.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(60.0,40.0,self.obj1724)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1724.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1724)
   self.obj1724.postAction( cobj0.LHS.CREATE )

   self.obj1725=achieve(self)
   self.obj1725.preAction( cobj0.LHS.CREATE )
   self.obj1725.isGraphObjectVisual = True

   if(hasattr(self.obj1725, '_setHierarchicalLink')):
     self.obj1725._setHierarchicalLink(False)

   # rate
   self.obj1725.rate.setNone()

   self.obj1725.GGLabel.setValue(3)
   self.obj1725.graphClass_= graph_achieve
   if self.genGraphics:
      new_obj = graph_achieve(97.5,137.5,self.obj1725)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1725.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1725)
   self.obj1725.postAction( cobj0.LHS.CREATE )

   self.obj1726=GenericGraphEdge(self)
   self.obj1726.preAction( cobj0.LHS.CREATE )
   self.obj1726.isGraphObjectVisual = True

   if(hasattr(self.obj1726, '_setHierarchicalLink')):
     self.obj1726._setHierarchicalLink(False)

   self.obj1726.GGLabel.setValue(7)
   self.obj1726.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(215.0,41.5,self.obj1726)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1726.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1726)
   self.obj1726.postAction( cobj0.LHS.CREATE )

   self.obj1727=GenericGraphEdge(self)
   self.obj1727.preAction( cobj0.LHS.CREATE )
   self.obj1727.isGraphObjectVisual = True

   if(hasattr(self.obj1727, '_setHierarchicalLink')):
     self.obj1727._setHierarchicalLink(False)

   self.obj1727.GGLabel.setValue(9)
   self.obj1727.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(185.0,276.0,self.obj1727)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1727.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1727)
   self.obj1727.postAction( cobj0.LHS.CREATE )

   self.obj1719.out_connections_.append(self.obj1722)
   self.obj1722.in_connections_.append(self.obj1719)
   self.obj1719.graphObject_.pendingConnections.append((self.obj1719.graphObject_.tag, self.obj1722.graphObject_.tag, [264.0, 69.0, 265.0, 100.0], 0, True))
   self.obj1722.out_connections_.append(self.obj1721)
   self.obj1721.in_connections_.append(self.obj1722)
   self.obj1722.graphObject_.pendingConnections.append((self.obj1722.graphObject_.tag, self.obj1721.graphObject_.tag, [260.0, 151.0, 352.0, 90.0], 0, True))
   self.obj1723.out_connections_.append(self.obj1727)
   self.obj1727.in_connections_.append(self.obj1723)
   self.obj1723.graphObject_.pendingConnections.append((self.obj1723.graphObject_.tag, self.obj1727.graphObject_.tag, [84.0, 270.0, 185.0, 276.0], 0, True))
   self.obj1724.out_connections_.append(self.obj1725)
   self.obj1725.in_connections_.append(self.obj1724)
   self.obj1724.graphObject_.pendingConnections.append((self.obj1724.graphObject_.tag, self.obj1725.graphObject_.tag, [84.0, 86.0, 97.5, 137.5], 0, True))
   self.obj1724.out_connections_.append(self.obj1726)
   self.obj1726.in_connections_.append(self.obj1724)
   self.obj1724.graphObject_.pendingConnections.append((self.obj1724.graphObject_.tag, self.obj1726.graphObject_.tag, [84.0, 41.0, 215.0, 41.5], 0, True))
   self.obj1725.out_connections_.append(self.obj1723)
   self.obj1723.in_connections_.append(self.obj1725)
   self.obj1725.graphObject_.pendingConnections.append((self.obj1725.graphObject_.tag, self.obj1723.graphObject_.tag, [83.0, 221.0, 93.5, 143.5], 0, True))
   self.obj1726.out_connections_.append(self.obj1719)
   self.obj1719.in_connections_.append(self.obj1726)
   self.obj1726.graphObject_.pendingConnections.append((self.obj1726.graphObject_.tag, self.obj1719.graphObject_.tag, [246.0, 62.0, 215.0, 41.5], 0, True))
   self.obj1727.out_connections_.append(self.obj1720)
   self.obj1720.in_connections_.append(self.obj1727)
   self.obj1727.graphObject_.pendingConnections.append((self.obj1727.graphObject_.tag, self.obj1720.graphObject_.tag, [246.0, 282.0, 185.0, 276.0], 0, True))

   cobj0.RHS = ASG_pns(self)
   cobj0.RHS.merge(ASG_omacs(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj1731=metarial(self)
   self.obj1731.preAction( cobj0.RHS.CREATE )
   self.obj1731.isGraphObjectVisual = True

   if(hasattr(self.obj1731, '_setHierarchicalLink')):
     self.obj1731._setHierarchicalLink(False)

   # MaxFlow
   self.obj1731.MaxFlow.setNone()

   # price
   self.obj1731.price.setValue(0)

   # Name
   self.obj1731.Name.setValue('')
   self.obj1731.Name.setNone()

   # ReqFlow
   self.obj1731.ReqFlow.setNone()

   self.obj1731.GGLabel.setValue(4)
   self.obj1731.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(280.0,20.0,self.obj1731)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1731.graphObject_ = new_obj
   self.obj17310= AttrCalc()
   self.obj17310.Copy=ATOM3Boolean()
   self.obj17310.Copy.setValue(('Copy from LHS', 1))
   self.obj17310.Copy.config = 0
   self.obj17310.Specify=ATOM3Constraint()
   self.obj17310.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1731.GGset2Any['MaxFlow']= self.obj17310
   self.obj17311= AttrCalc()
   self.obj17311.Copy=ATOM3Boolean()
   self.obj17311.Copy.setValue(('Copy from LHS', 1))
   self.obj17311.Copy.config = 0
   self.obj17311.Specify=ATOM3Constraint()
   self.obj17311.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1731.GGset2Any['Name']= self.obj17311
   self.obj17312= AttrCalc()
   self.obj17312.Copy=ATOM3Boolean()
   self.obj17312.Copy.setValue(('Copy from LHS', 1))
   self.obj17312.Copy.config = 0
   self.obj17312.Specify=ATOM3Constraint()
   self.obj17312.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1731.GGset2Any['ReqFlow']= self.obj17312

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1731)
   self.obj1731.postAction( cobj0.RHS.CREATE )

   self.obj1732=metarial(self)
   self.obj1732.preAction( cobj0.RHS.CREATE )
   self.obj1732.isGraphObjectVisual = True

   if(hasattr(self.obj1732, '_setHierarchicalLink')):
     self.obj1732._setHierarchicalLink(False)

   # MaxFlow
   self.obj1732.MaxFlow.setNone()

   # price
   self.obj1732.price.setValue(0)

   # Name
   self.obj1732.Name.setValue('')
   self.obj1732.Name.setNone()

   # ReqFlow
   self.obj1732.ReqFlow.setNone()

   self.obj1732.GGLabel.setValue(6)
   self.obj1732.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(280.0,240.0,self.obj1732)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1732.graphObject_ = new_obj
   self.obj17320= AttrCalc()
   self.obj17320.Copy=ATOM3Boolean()
   self.obj17320.Copy.setValue(('Copy from LHS', 1))
   self.obj17320.Copy.config = 0
   self.obj17320.Specify=ATOM3Constraint()
   self.obj17320.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1732.GGset2Any['MaxFlow']= self.obj17320
   self.obj17321= AttrCalc()
   self.obj17321.Copy=ATOM3Boolean()
   self.obj17321.Copy.setValue(('Copy from LHS', 1))
   self.obj17321.Copy.config = 0
   self.obj17321.Specify=ATOM3Constraint()
   self.obj17321.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1732.GGset2Any['Name']= self.obj17321
   self.obj17322= AttrCalc()
   self.obj17322.Copy=ATOM3Boolean()
   self.obj17322.Copy.setValue(('Copy from LHS', 1))
   self.obj17322.Copy.config = 0
   self.obj17322.Specify=ATOM3Constraint()
   self.obj17322.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1732.GGset2Any['ReqFlow']= self.obj17322

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1732)
   self.obj1732.postAction( cobj0.RHS.CREATE )

   self.obj1733=operatingUnit(self)
   self.obj1733.preAction( cobj0.RHS.CREATE )
   self.obj1733.isGraphObjectVisual = True

   if(hasattr(self.obj1733, '_setHierarchicalLink')):
     self.obj1733._setHierarchicalLink(False)

   # OperCostProp
   self.obj1733.OperCostProp.setNone()

   # name
   self.obj1733.name.setValue('')
   self.obj1733.name.setNone()

   # OperCostFix
   self.obj1733.OperCostFix.setNone()

   self.obj1733.GGLabel.setValue(5)
   self.obj1733.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(280.0,140.0,self.obj1733)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1733.graphObject_ = new_obj
   self.obj17330= AttrCalc()
   self.obj17330.Copy=ATOM3Boolean()
   self.obj17330.Copy.setValue(('Copy from LHS', 1))
   self.obj17330.Copy.config = 0
   self.obj17330.Specify=ATOM3Constraint()
   self.obj17330.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1733.GGset2Any['OperCostProp']= self.obj17330
   self.obj17331= AttrCalc()
   self.obj17331.Copy=ATOM3Boolean()
   self.obj17331.Copy.setValue(('Copy from LHS', 1))
   self.obj17331.Copy.config = 0
   self.obj17331.Specify=ATOM3Constraint()
   self.obj17331.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1733.GGset2Any['name']= self.obj17331
   self.obj17332= AttrCalc()
   self.obj17332.Copy=ATOM3Boolean()
   self.obj17332.Copy.setValue(('Copy from LHS', 1))
   self.obj17332.Copy.config = 0
   self.obj17332.Specify=ATOM3Constraint()
   self.obj17332.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1733.GGset2Any['OperCostFix']= self.obj17332

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1733)
   self.obj1733.postAction( cobj0.RHS.CREATE )

   self.obj1734=intoMaterial(self)
   self.obj1734.preAction( cobj0.RHS.CREATE )
   self.obj1734.isGraphObjectVisual = True

   if(hasattr(self.obj1734, '_setHierarchicalLink')):
     self.obj1734._setHierarchicalLink(False)

   # rate
   self.obj1734.rate.setValue(0.0)

   self.obj1734.GGLabel.setValue(10)
   self.obj1734.graphClass_= graph_intoMaterial
   if self.genGraphics:
      new_obj = graph_intoMaterial(315.25,202.5,self.obj1734)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1734.graphObject_ = new_obj
   self.obj17340= AttrCalc()
   self.obj17340.Copy=ATOM3Boolean()
   self.obj17340.Copy.setValue(('Copy from LHS', 0))
   self.obj17340.Copy.config = 0
   self.obj17340.Specify=ATOM3Constraint()
   self.obj17340.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(3)).rate.getValue()\n\n\n\n\n\n\n\n\n\n'))
   self.obj1734.GGset2Any['rate']= self.obj17340

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1734)
   self.obj1734.postAction( cobj0.RHS.CREATE )

   self.obj1735=fromMaterial(self)
   self.obj1735.preAction( cobj0.RHS.CREATE )
   self.obj1735.isGraphObjectVisual = True

   if(hasattr(self.obj1735, '_setHierarchicalLink')):
     self.obj1735._setHierarchicalLink(False)

   # rate
   self.obj1735.rate.setNone()

   self.obj1735.GGLabel.setValue(8)
   self.obj1735.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(323.0,83.0,self.obj1735)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1735.graphObject_ = new_obj
   self.obj17350= AttrCalc()
   self.obj17350.Copy=ATOM3Boolean()
   self.obj17350.Copy.setValue(('Copy from LHS', 1))
   self.obj17350.Copy.config = 0
   self.obj17350.Specify=ATOM3Constraint()
   self.obj17350.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1735.GGset2Any['rate']= self.obj17350

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1735)
   self.obj1735.postAction( cobj0.RHS.CREATE )

   self.obj1736=Goal(self)
   self.obj1736.preAction( cobj0.RHS.CREATE )
   self.obj1736.isGraphObjectVisual = True

   if(hasattr(self.obj1736, '_setHierarchicalLink')):
     self.obj1736._setHierarchicalLink(False)

   # name
   self.obj1736.name.setValue('')
   self.obj1736.name.setNone()

   self.obj1736.GGLabel.setValue(2)
   self.obj1736.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(60.0,220.0,self.obj1736)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1736.graphObject_ = new_obj
   self.obj17360= AttrCalc()
   self.obj17360.Copy=ATOM3Boolean()
   self.obj17360.Copy.setValue(('Copy from LHS', 1))
   self.obj17360.Copy.config = 0
   self.obj17360.Specify=ATOM3Constraint()
   self.obj17360.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1736.GGset2Any['name']= self.obj17360

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1736)
   self.obj1736.postAction( cobj0.RHS.CREATE )

   self.obj1737=Role(self)
   self.obj1737.preAction( cobj0.RHS.CREATE )
   self.obj1737.isGraphObjectVisual = True

   if(hasattr(self.obj1737, '_setHierarchicalLink')):
     self.obj1737._setHierarchicalLink(False)

   # name
   self.obj1737.name.setValue('')
   self.obj1737.name.setNone()

   self.obj1737.GGLabel.setValue(1)
   self.obj1737.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(60.0,40.0,self.obj1737)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1737.graphObject_ = new_obj
   self.obj17370= AttrCalc()
   self.obj17370.Copy=ATOM3Boolean()
   self.obj17370.Copy.setValue(('Copy from LHS', 1))
   self.obj17370.Copy.config = 0
   self.obj17370.Specify=ATOM3Constraint()
   self.obj17370.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1737.GGset2Any['name']= self.obj17370

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1737)
   self.obj1737.postAction( cobj0.RHS.CREATE )

   self.obj1738=achieve(self)
   self.obj1738.preAction( cobj0.RHS.CREATE )
   self.obj1738.isGraphObjectVisual = True

   if(hasattr(self.obj1738, '_setHierarchicalLink')):
     self.obj1738._setHierarchicalLink(False)

   # rate
   self.obj1738.rate.setNone()

   self.obj1738.GGLabel.setValue(3)
   self.obj1738.graphClass_= graph_achieve
   if self.genGraphics:
      new_obj = graph_achieve(93.5,143.5,self.obj1738)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1738.graphObject_ = new_obj
   self.obj17380= AttrCalc()
   self.obj17380.Copy=ATOM3Boolean()
   self.obj17380.Copy.setValue(('Copy from LHS', 1))
   self.obj17380.Copy.config = 0
   self.obj17380.Specify=ATOM3Constraint()
   self.obj17380.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1738.GGset2Any['rate']= self.obj17380

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1738)
   self.obj1738.postAction( cobj0.RHS.CREATE )

   self.obj1739=GenericGraphEdge(self)
   self.obj1739.preAction( cobj0.RHS.CREATE )
   self.obj1739.isGraphObjectVisual = True

   if(hasattr(self.obj1739, '_setHierarchicalLink')):
     self.obj1739._setHierarchicalLink(False)

   self.obj1739.GGLabel.setValue(7)
   self.obj1739.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(215.0,41.5,self.obj1739)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1739.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1739)
   self.obj1739.postAction( cobj0.RHS.CREATE )

   self.obj1740=GenericGraphEdge(self)
   self.obj1740.preAction( cobj0.RHS.CREATE )
   self.obj1740.isGraphObjectVisual = True

   if(hasattr(self.obj1740, '_setHierarchicalLink')):
     self.obj1740._setHierarchicalLink(False)

   self.obj1740.GGLabel.setValue(9)
   self.obj1740.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(185.0,276.0,self.obj1740)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1740.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1740)
   self.obj1740.postAction( cobj0.RHS.CREATE )

   self.obj1731.out_connections_.append(self.obj1735)
   self.obj1735.in_connections_.append(self.obj1731)
   self.obj1731.graphObject_.pendingConnections.append((self.obj1731.graphObject_.tag, self.obj1735.graphObject_.tag, [284.0, 69.0, 323.0, 83.0], 2, 0))
   self.obj1733.out_connections_.append(self.obj1734)
   self.obj1734.in_connections_.append(self.obj1733)
   self.obj1733.graphObject_.pendingConnections.append((self.obj1733.graphObject_.tag, self.obj1734.graphObject_.tag, [333.0, 148.0, 332.0, 167.0, 371.25, 179.5], 2, True))
   self.obj1734.out_connections_.append(self.obj1732)
   self.obj1732.in_connections_.append(self.obj1734)
   self.obj1734.graphObject_.pendingConnections.append((self.obj1734.graphObject_.tag, self.obj1732.graphObject_.tag, [326.0, 250.0, 354.5, 215.0, 371.25, 179.5], 2, True))
   self.obj1735.out_connections_.append(self.obj1733)
   self.obj1733.in_connections_.append(self.obj1735)
   self.obj1735.graphObject_.pendingConnections.append((self.obj1735.graphObject_.tag, self.obj1733.graphObject_.tag, [333.0, 148.0, 352.0, 90.0], 2, 0))
   self.obj1736.out_connections_.append(self.obj1740)
   self.obj1740.in_connections_.append(self.obj1736)
   self.obj1736.graphObject_.pendingConnections.append((self.obj1736.graphObject_.tag, self.obj1740.graphObject_.tag, [94.0, 270.0, 185.0, 276.0], 2, 0))
   self.obj1737.out_connections_.append(self.obj1738)
   self.obj1738.in_connections_.append(self.obj1737)
   self.obj1737.graphObject_.pendingConnections.append((self.obj1737.graphObject_.tag, self.obj1738.graphObject_.tag, [91.0, 85.0, 93.5, 143.5], 2, 0))
   self.obj1737.out_connections_.append(self.obj1739)
   self.obj1739.in_connections_.append(self.obj1737)
   self.obj1737.graphObject_.pendingConnections.append((self.obj1737.graphObject_.tag, self.obj1739.graphObject_.tag, [91.0, 40.0, 215.0, 41.5], 2, 0))
   self.obj1738.out_connections_.append(self.obj1736)
   self.obj1736.in_connections_.append(self.obj1738)
   self.obj1738.graphObject_.pendingConnections.append((self.obj1738.graphObject_.tag, self.obj1736.graphObject_.tag, [93.0, 221.0, 93.5, 143.5], 2, 0))
   self.obj1739.out_connections_.append(self.obj1731)
   self.obj1731.in_connections_.append(self.obj1739)
   self.obj1739.graphObject_.pendingConnections.append((self.obj1739.graphObject_.tag, self.obj1731.graphObject_.tag, [266.0, 62.0, 215.0, 41.5], 2, 0))
   self.obj1740.out_connections_.append(self.obj1732)
   self.obj1732.in_connections_.append(self.obj1740)
   self.obj1740.graphObject_.pendingConnections.append((self.obj1740.graphObject_.tag, self.obj1732.graphObject_.tag, [286.0, 282.0, 185.0, 276.0], 2, 0))

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

   self.obj1747=rawMaterial(self)
   self.obj1747.preAction( cobj0.LHS.CREATE )
   self.obj1747.isGraphObjectVisual = True

   if(hasattr(self.obj1747, '_setHierarchicalLink')):
     self.obj1747._setHierarchicalLink(False)

   # MaxFlow
   self.obj1747.MaxFlow.setNone()

   # price
   self.obj1747.price.setValue(0)

   # Name
   self.obj1747.Name.setValue('')
   self.obj1747.Name.setNone()

   # ReqFlow
   self.obj1747.ReqFlow.setNone()

   self.obj1747.GGLabel.setValue(6)
   self.obj1747.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(240.0,0.0,self.obj1747)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1747.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1747)
   self.obj1747.postAction( cobj0.LHS.CREATE )

   self.obj1748=metarial(self)
   self.obj1748.preAction( cobj0.LHS.CREATE )
   self.obj1748.isGraphObjectVisual = True

   if(hasattr(self.obj1748, '_setHierarchicalLink')):
     self.obj1748._setHierarchicalLink(False)

   # MaxFlow
   self.obj1748.MaxFlow.setNone()

   # price
   self.obj1748.price.setValue(0)

   # Name
   self.obj1748.Name.setValue('')
   self.obj1748.Name.setNone()

   # ReqFlow
   self.obj1748.ReqFlow.setNone()

   self.obj1748.GGLabel.setValue(11)
   self.obj1748.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(260.0,200.0,self.obj1748)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1748.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1748)
   self.obj1748.postAction( cobj0.LHS.CREATE )

   self.obj1749=operatingUnit(self)
   self.obj1749.preAction( cobj0.LHS.CREATE )
   self.obj1749.isGraphObjectVisual = True

   if(hasattr(self.obj1749, '_setHierarchicalLink')):
     self.obj1749._setHierarchicalLink(False)

   # OperCostProp
   self.obj1749.OperCostProp.setNone()

   # name
   self.obj1749.name.setValue('')
   self.obj1749.name.setNone()

   # OperCostFix
   self.obj1749.OperCostFix.setNone()

   self.obj1749.GGLabel.setValue(7)
   self.obj1749.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(280.0,100.0,self.obj1749)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1749.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1749)
   self.obj1749.postAction( cobj0.LHS.CREATE )

   self.obj1750=operatingUnit(self)
   self.obj1750.preAction( cobj0.LHS.CREATE )
   self.obj1750.isGraphObjectVisual = True

   if(hasattr(self.obj1750, '_setHierarchicalLink')):
     self.obj1750._setHierarchicalLink(False)

   # OperCostProp
   self.obj1750.OperCostProp.setNone()

   # name
   self.obj1750.name.setValue('')
   self.obj1750.name.setNone()

   # OperCostFix
   self.obj1750.OperCostFix.setNone()

   self.obj1750.GGLabel.setValue(12)
   self.obj1750.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(360.0,260.0,self.obj1750)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1750.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1750)
   self.obj1750.postAction( cobj0.LHS.CREATE )

   self.obj1751=fromRaw(self)
   self.obj1751.preAction( cobj0.LHS.CREATE )
   self.obj1751.isGraphObjectVisual = True

   if(hasattr(self.obj1751, '_setHierarchicalLink')):
     self.obj1751._setHierarchicalLink(False)

   # rate
   self.obj1751.rate.setNone()

   self.obj1751.GGLabel.setValue(8)
   self.obj1751.graphClass_= graph_fromRaw
   if self.genGraphics:
      new_obj = graph_fromRaw(311.5,63.25,self.obj1751)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1751.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1751)
   self.obj1751.postAction( cobj0.LHS.CREATE )

   self.obj1752=fromMaterial(self)
   self.obj1752.preAction( cobj0.LHS.CREATE )
   self.obj1752.isGraphObjectVisual = True

   if(hasattr(self.obj1752, '_setHierarchicalLink')):
     self.obj1752._setHierarchicalLink(False)

   # rate
   self.obj1752.rate.setNone()

   self.obj1752.GGLabel.setValue(14)
   self.obj1752.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(379.5,235.25,self.obj1752)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1752.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1752)
   self.obj1752.postAction( cobj0.LHS.CREATE )

   self.obj1753=CapableOf(self)
   self.obj1753.preAction( cobj0.LHS.CREATE )
   self.obj1753.isGraphObjectVisual = True

   if(hasattr(self.obj1753, '_setHierarchicalLink')):
     self.obj1753._setHierarchicalLink(False)

   # rate
   self.obj1753.rate.setNone()

   self.obj1753.GGLabel.setValue(3)
   self.obj1753.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(84.5,131.5,self.obj1753)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1753.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1753)
   self.obj1753.postAction( cobj0.LHS.CREATE )

   self.obj1754=Agent(self)
   self.obj1754.preAction( cobj0.LHS.CREATE )
   self.obj1754.isGraphObjectVisual = True

   if(hasattr(self.obj1754, '_setHierarchicalLink')):
     self.obj1754._setHierarchicalLink(False)

   # price
   self.obj1754.price.setNone()

   # name
   self.obj1754.name.setValue('')
   self.obj1754.name.setNone()

   self.obj1754.GGLabel.setValue(1)
   self.obj1754.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(60.0,20.0,self.obj1754)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1754.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1754)
   self.obj1754.postAction( cobj0.LHS.CREATE )

   self.obj1755=Role(self)
   self.obj1755.preAction( cobj0.LHS.CREATE )
   self.obj1755.isGraphObjectVisual = True

   if(hasattr(self.obj1755, '_setHierarchicalLink')):
     self.obj1755._setHierarchicalLink(False)

   # name
   self.obj1755.name.setValue('')
   self.obj1755.name.setNone()

   self.obj1755.GGLabel.setValue(2)
   self.obj1755.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(60.0,180.0,self.obj1755)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1755.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1755)
   self.obj1755.postAction( cobj0.LHS.CREATE )

   self.obj1756=GenericGraphEdge(self)
   self.obj1756.preAction( cobj0.LHS.CREATE )
   self.obj1756.isGraphObjectVisual = True

   if(hasattr(self.obj1756, '_setHierarchicalLink')):
     self.obj1756._setHierarchicalLink(False)

   self.obj1756.GGLabel.setValue(15)
   self.obj1756.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(174.5,69.0,self.obj1756)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1756.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1756)
   self.obj1756.postAction( cobj0.LHS.CREATE )

   self.obj1757=GenericGraphEdge(self)
   self.obj1757.preAction( cobj0.LHS.CREATE )
   self.obj1757.isGraphObjectVisual = True

   if(hasattr(self.obj1757, '_setHierarchicalLink')):
     self.obj1757._setHierarchicalLink(False)

   self.obj1757.GGLabel.setValue(10)
   self.obj1757.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(245.75,97.25,self.obj1757)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1757.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1757)
   self.obj1757.postAction( cobj0.LHS.CREATE )

   self.obj1758=GenericGraphEdge(self)
   self.obj1758.preAction( cobj0.LHS.CREATE )
   self.obj1758.isGraphObjectVisual = True

   if(hasattr(self.obj1758, '_setHierarchicalLink')):
     self.obj1758._setHierarchicalLink(False)

   self.obj1758.GGLabel.setValue(13)
   self.obj1758.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(175.0,234.0,self.obj1758)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1758.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1758)
   self.obj1758.postAction( cobj0.LHS.CREATE )

   self.obj1747.out_connections_.append(self.obj1751)
   self.obj1751.in_connections_.append(self.obj1747)
   self.obj1747.graphObject_.pendingConnections.append((self.obj1747.graphObject_.tag, self.obj1751.graphObject_.tag, [264.0, 56.0, 295.0, 49.5, 311.5, 63.25], 2, True))
   self.obj1748.out_connections_.append(self.obj1752)
   self.obj1752.in_connections_.append(self.obj1748)
   self.obj1748.graphObject_.pendingConnections.append((self.obj1748.graphObject_.tag, self.obj1752.graphObject_.tag, [306.0, 210.0, 353.5, 220.0, 379.5, 235.25], 2, True))
   self.obj1751.out_connections_.append(self.obj1749)
   self.obj1749.in_connections_.append(self.obj1751)
   self.obj1751.graphObject_.pendingConnections.append((self.obj1751.graphObject_.tag, self.obj1749.graphObject_.tag, [330.0, 111.0, 328.0, 77.0, 311.5, 63.25], 2, True))
   self.obj1752.out_connections_.append(self.obj1750)
   self.obj1750.in_connections_.append(self.obj1752)
   self.obj1752.graphObject_.pendingConnections.append((self.obj1752.graphObject_.tag, self.obj1750.graphObject_.tag, [410.0, 271.0, 405.5, 250.5, 379.5, 235.25], 2, True))
   self.obj1753.out_connections_.append(self.obj1755)
   self.obj1755.in_connections_.append(self.obj1753)
   self.obj1753.graphObject_.pendingConnections.append((self.obj1753.graphObject_.tag, self.obj1755.graphObject_.tag, [84.0, 181.0, 84.5, 131.5], 0, True))
   self.obj1754.out_connections_.append(self.obj1753)
   self.obj1753.in_connections_.append(self.obj1754)
   self.obj1754.graphObject_.pendingConnections.append((self.obj1754.graphObject_.tag, self.obj1753.graphObject_.tag, [85.0, 82.0, 84.5, 131.5], 0, True))
   self.obj1754.out_connections_.append(self.obj1756)
   self.obj1756.in_connections_.append(self.obj1754)
   self.obj1754.graphObject_.pendingConnections.append((self.obj1754.graphObject_.tag, self.obj1756.graphObject_.tag, [85.0, 82.0, 174.5, 69.0], 0, True))
   self.obj1754.out_connections_.append(self.obj1757)
   self.obj1757.in_connections_.append(self.obj1754)
   self.obj1754.graphObject_.pendingConnections.append((self.obj1754.graphObject_.tag, self.obj1757.graphObject_.tag, [85.0, 82.0, 192.0, 90.0, 245.75, 97.25], 2, True))
   self.obj1755.out_connections_.append(self.obj1758)
   self.obj1758.in_connections_.append(self.obj1755)
   self.obj1755.graphObject_.pendingConnections.append((self.obj1755.graphObject_.tag, self.obj1758.graphObject_.tag, [84.0, 226.0, 175.0, 234.0], 0, True))
   self.obj1756.out_connections_.append(self.obj1747)
   self.obj1747.in_connections_.append(self.obj1756)
   self.obj1756.graphObject_.pendingConnections.append((self.obj1756.graphObject_.tag, self.obj1747.graphObject_.tag, [264.0, 56.0, 174.5, 69.0], 0, True))
   self.obj1757.out_connections_.append(self.obj1749)
   self.obj1749.in_connections_.append(self.obj1757)
   self.obj1757.graphObject_.pendingConnections.append((self.obj1757.graphObject_.tag, self.obj1749.graphObject_.tag, [300.0, 111.0, 299.5, 104.5, 245.75, 97.25], 2, True))
   self.obj1758.out_connections_.append(self.obj1748)
   self.obj1748.in_connections_.append(self.obj1758)
   self.obj1758.graphObject_.pendingConnections.append((self.obj1758.graphObject_.tag, self.obj1748.graphObject_.tag, [266.0, 242.0, 175.0, 234.0], 0, True))

   cobj0.RHS = ASG_pns(self)
   cobj0.RHS.merge(ASG_omacs(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj1762=rawMaterial(self)
   self.obj1762.preAction( cobj0.RHS.CREATE )
   self.obj1762.isGraphObjectVisual = True

   if(hasattr(self.obj1762, '_setHierarchicalLink')):
     self.obj1762._setHierarchicalLink(False)

   # MaxFlow
   self.obj1762.MaxFlow.setNone()

   # price
   self.obj1762.price.setValue(0)

   # Name
   self.obj1762.Name.setValue('')
   self.obj1762.Name.setNone()

   # ReqFlow
   self.obj1762.ReqFlow.setNone()

   self.obj1762.GGLabel.setValue(6)
   self.obj1762.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(240.0,0.0,self.obj1762)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1762.graphObject_ = new_obj
   self.obj17620= AttrCalc()
   self.obj17620.Copy=ATOM3Boolean()
   self.obj17620.Copy.setValue(('Copy from LHS', 1))
   self.obj17620.Copy.config = 0
   self.obj17620.Specify=ATOM3Constraint()
   self.obj17620.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1762.GGset2Any['MaxFlow']= self.obj17620
   self.obj17621= AttrCalc()
   self.obj17621.Copy=ATOM3Boolean()
   self.obj17621.Copy.setValue(('Copy from LHS', 1))
   self.obj17621.Copy.config = 0
   self.obj17621.Specify=ATOM3Constraint()
   self.obj17621.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1762.GGset2Any['Name']= self.obj17621
   self.obj17622= AttrCalc()
   self.obj17622.Copy=ATOM3Boolean()
   self.obj17622.Copy.setValue(('Copy from LHS', 1))
   self.obj17622.Copy.config = 0
   self.obj17622.Specify=ATOM3Constraint()
   self.obj17622.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1762.GGset2Any['ReqFlow']= self.obj17622

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1762)
   self.obj1762.postAction( cobj0.RHS.CREATE )

   self.obj1763=metarial(self)
   self.obj1763.preAction( cobj0.RHS.CREATE )
   self.obj1763.isGraphObjectVisual = True

   if(hasattr(self.obj1763, '_setHierarchicalLink')):
     self.obj1763._setHierarchicalLink(False)

   # MaxFlow
   self.obj1763.MaxFlow.setNone()

   # price
   self.obj1763.price.setValue(0)

   # Name
   self.obj1763.Name.setValue('')
   self.obj1763.Name.setNone()

   # ReqFlow
   self.obj1763.ReqFlow.setNone()

   self.obj1763.GGLabel.setValue(11)
   self.obj1763.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(260.0,200.0,self.obj1763)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1763.graphObject_ = new_obj
   self.obj17630= AttrCalc()
   self.obj17630.Copy=ATOM3Boolean()
   self.obj17630.Copy.setValue(('Copy from LHS', 1))
   self.obj17630.Copy.config = 0
   self.obj17630.Specify=ATOM3Constraint()
   self.obj17630.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1763.GGset2Any['MaxFlow']= self.obj17630
   self.obj17631= AttrCalc()
   self.obj17631.Copy=ATOM3Boolean()
   self.obj17631.Copy.setValue(('Copy from LHS', 1))
   self.obj17631.Copy.config = 0
   self.obj17631.Specify=ATOM3Constraint()
   self.obj17631.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1763.GGset2Any['Name']= self.obj17631
   self.obj17632= AttrCalc()
   self.obj17632.Copy=ATOM3Boolean()
   self.obj17632.Copy.setValue(('Copy from LHS', 1))
   self.obj17632.Copy.config = 0
   self.obj17632.Specify=ATOM3Constraint()
   self.obj17632.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1763.GGset2Any['ReqFlow']= self.obj17632

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1763)
   self.obj1763.postAction( cobj0.RHS.CREATE )

   self.obj1764=operatingUnit(self)
   self.obj1764.preAction( cobj0.RHS.CREATE )
   self.obj1764.isGraphObjectVisual = True

   if(hasattr(self.obj1764, '_setHierarchicalLink')):
     self.obj1764._setHierarchicalLink(False)

   # OperCostProp
   self.obj1764.OperCostProp.setNone()

   # name
   self.obj1764.name.setValue('')
   self.obj1764.name.setNone()

   # OperCostFix
   self.obj1764.OperCostFix.setNone()

   self.obj1764.GGLabel.setValue(7)
   self.obj1764.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(280.0,100.0,self.obj1764)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1764.graphObject_ = new_obj
   self.obj17640= AttrCalc()
   self.obj17640.Copy=ATOM3Boolean()
   self.obj17640.Copy.setValue(('Copy from LHS', 1))
   self.obj17640.Copy.config = 0
   self.obj17640.Specify=ATOM3Constraint()
   self.obj17640.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1764.GGset2Any['OperCostProp']= self.obj17640
   self.obj17641= AttrCalc()
   self.obj17641.Copy=ATOM3Boolean()
   self.obj17641.Copy.setValue(('Copy from LHS', 1))
   self.obj17641.Copy.config = 0
   self.obj17641.Specify=ATOM3Constraint()
   self.obj17641.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1764.GGset2Any['name']= self.obj17641
   self.obj17642= AttrCalc()
   self.obj17642.Copy=ATOM3Boolean()
   self.obj17642.Copy.setValue(('Copy from LHS', 1))
   self.obj17642.Copy.config = 0
   self.obj17642.Specify=ATOM3Constraint()
   self.obj17642.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1764.GGset2Any['OperCostFix']= self.obj17642

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1764)
   self.obj1764.postAction( cobj0.RHS.CREATE )

   self.obj1765=operatingUnit(self)
   self.obj1765.preAction( cobj0.RHS.CREATE )
   self.obj1765.isGraphObjectVisual = True

   if(hasattr(self.obj1765, '_setHierarchicalLink')):
     self.obj1765._setHierarchicalLink(False)

   # OperCostProp
   self.obj1765.OperCostProp.setNone()

   # name
   self.obj1765.name.setValue('')
   self.obj1765.name.setNone()

   # OperCostFix
   self.obj1765.OperCostFix.setNone()

   self.obj1765.GGLabel.setValue(12)
   self.obj1765.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(360.0,260.0,self.obj1765)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1765.graphObject_ = new_obj
   self.obj17650= AttrCalc()
   self.obj17650.Copy=ATOM3Boolean()
   self.obj17650.Copy.setValue(('Copy from LHS', 1))
   self.obj17650.Copy.config = 0
   self.obj17650.Specify=ATOM3Constraint()
   self.obj17650.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1765.GGset2Any['OperCostProp']= self.obj17650
   self.obj17651= AttrCalc()
   self.obj17651.Copy=ATOM3Boolean()
   self.obj17651.Copy.setValue(('Copy from LHS', 1))
   self.obj17651.Copy.config = 0
   self.obj17651.Specify=ATOM3Constraint()
   self.obj17651.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1765.GGset2Any['name']= self.obj17651
   self.obj17652= AttrCalc()
   self.obj17652.Copy=ATOM3Boolean()
   self.obj17652.Copy.setValue(('Copy from LHS', 1))
   self.obj17652.Copy.config = 0
   self.obj17652.Specify=ATOM3Constraint()
   self.obj17652.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1765.GGset2Any['OperCostFix']= self.obj17652

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1765)
   self.obj1765.postAction( cobj0.RHS.CREATE )

   self.obj1766=fromRaw(self)
   self.obj1766.preAction( cobj0.RHS.CREATE )
   self.obj1766.isGraphObjectVisual = True

   if(hasattr(self.obj1766, '_setHierarchicalLink')):
     self.obj1766._setHierarchicalLink(False)

   # rate
   self.obj1766.rate.setNone()

   self.obj1766.GGLabel.setValue(8)
   self.obj1766.graphClass_= graph_fromRaw
   if self.genGraphics:
      new_obj = graph_fromRaw(311.5,63.25,self.obj1766)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1766.graphObject_ = new_obj
   self.obj17660= AttrCalc()
   self.obj17660.Copy=ATOM3Boolean()
   self.obj17660.Copy.setValue(('Copy from LHS', 1))
   self.obj17660.Copy.config = 0
   self.obj17660.Specify=ATOM3Constraint()
   self.obj17660.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1766.GGset2Any['rate']= self.obj17660

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1766)
   self.obj1766.postAction( cobj0.RHS.CREATE )

   self.obj1767=intoMaterial(self)
   self.obj1767.preAction( cobj0.RHS.CREATE )
   self.obj1767.isGraphObjectVisual = True

   if(hasattr(self.obj1767, '_setHierarchicalLink')):
     self.obj1767._setHierarchicalLink(False)

   # rate
   self.obj1767.rate.setValue(0.0)

   self.obj1767.GGLabel.setValue(17)
   self.obj1767.graphClass_= graph_intoMaterial
   if self.genGraphics:
      new_obj = graph_intoMaterial(324.25,167.5,self.obj1767)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1767.graphObject_ = new_obj
   self.obj17670= AttrCalc()
   self.obj17670.Copy=ATOM3Boolean()
   self.obj17670.Copy.setValue(('Copy from LHS', 0))
   self.obj17670.Copy.config = 0
   self.obj17670.Specify=ATOM3Constraint()
   self.obj17670.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'a = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) ).name.getValue()\nb = self.getMatched ( graphID , self.LHS.nodeWithLabel(2) ).name.getValue()\nreturn self.graphRewritingSystem.Dictag[ a ][b]\n\n'))
   self.obj1767.GGset2Any['rate']= self.obj17670

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1767)
   self.obj1767.postAction( cobj0.RHS.CREATE )

   self.obj1768=fromMaterial(self)
   self.obj1768.preAction( cobj0.RHS.CREATE )
   self.obj1768.isGraphObjectVisual = True

   if(hasattr(self.obj1768, '_setHierarchicalLink')):
     self.obj1768._setHierarchicalLink(False)

   # rate
   self.obj1768.rate.setNone()

   self.obj1768.GGLabel.setValue(14)
   self.obj1768.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(379.5,235.25,self.obj1768)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1768.graphObject_ = new_obj
   self.obj17680= AttrCalc()
   self.obj17680.Copy=ATOM3Boolean()
   self.obj17680.Copy.setValue(('Copy from LHS', 1))
   self.obj17680.Copy.config = 0
   self.obj17680.Specify=ATOM3Constraint()
   self.obj17680.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1768.GGset2Any['rate']= self.obj17680

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1768)
   self.obj1768.postAction( cobj0.RHS.CREATE )

   self.obj1769=CapableOf(self)
   self.obj1769.preAction( cobj0.RHS.CREATE )
   self.obj1769.isGraphObjectVisual = True

   if(hasattr(self.obj1769, '_setHierarchicalLink')):
     self.obj1769._setHierarchicalLink(False)

   # rate
   self.obj1769.rate.setNone()

   self.obj1769.GGLabel.setValue(3)
   self.obj1769.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(84.5,131.5,self.obj1769)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1769.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1769)
   self.obj1769.postAction( cobj0.RHS.CREATE )

   self.obj1770=Agent(self)
   self.obj1770.preAction( cobj0.RHS.CREATE )
   self.obj1770.isGraphObjectVisual = True

   if(hasattr(self.obj1770, '_setHierarchicalLink')):
     self.obj1770._setHierarchicalLink(False)

   # price
   self.obj1770.price.setNone()

   # name
   self.obj1770.name.setValue('')
   self.obj1770.name.setNone()

   self.obj1770.GGLabel.setValue(1)
   self.obj1770.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(60.0,20.0,self.obj1770)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1770.graphObject_ = new_obj
   self.obj17700= AttrCalc()
   self.obj17700.Copy=ATOM3Boolean()
   self.obj17700.Copy.setValue(('Copy from LHS', 1))
   self.obj17700.Copy.config = 0
   self.obj17700.Specify=ATOM3Constraint()
   self.obj17700.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1770.GGset2Any['price']= self.obj17700
   self.obj17701= AttrCalc()
   self.obj17701.Copy=ATOM3Boolean()
   self.obj17701.Copy.setValue(('Copy from LHS', 1))
   self.obj17701.Copy.config = 0
   self.obj17701.Specify=ATOM3Constraint()
   self.obj17701.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1770.GGset2Any['name']= self.obj17701

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1770)
   self.obj1770.postAction( cobj0.RHS.CREATE )

   self.obj1771=Role(self)
   self.obj1771.preAction( cobj0.RHS.CREATE )
   self.obj1771.isGraphObjectVisual = True

   if(hasattr(self.obj1771, '_setHierarchicalLink')):
     self.obj1771._setHierarchicalLink(False)

   # name
   self.obj1771.name.setValue('')
   self.obj1771.name.setNone()

   self.obj1771.GGLabel.setValue(2)
   self.obj1771.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(60.0,180.0,self.obj1771)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1771.graphObject_ = new_obj
   self.obj17710= AttrCalc()
   self.obj17710.Copy=ATOM3Boolean()
   self.obj17710.Copy.setValue(('Copy from LHS', 1))
   self.obj17710.Copy.config = 0
   self.obj17710.Specify=ATOM3Constraint()
   self.obj17710.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1771.GGset2Any['name']= self.obj17710

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1771)
   self.obj1771.postAction( cobj0.RHS.CREATE )

   self.obj1772=GenericGraphEdge(self)
   self.obj1772.preAction( cobj0.RHS.CREATE )
   self.obj1772.isGraphObjectVisual = True

   if(hasattr(self.obj1772, '_setHierarchicalLink')):
     self.obj1772._setHierarchicalLink(False)

   self.obj1772.GGLabel.setValue(15)
   self.obj1772.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(174.5,69.0,self.obj1772)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1772.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1772)
   self.obj1772.postAction( cobj0.RHS.CREATE )

   self.obj1773=GenericGraphEdge(self)
   self.obj1773.preAction( cobj0.RHS.CREATE )
   self.obj1773.isGraphObjectVisual = True

   if(hasattr(self.obj1773, '_setHierarchicalLink')):
     self.obj1773._setHierarchicalLink(False)

   self.obj1773.GGLabel.setValue(10)
   self.obj1773.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(245.75,97.25,self.obj1773)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1773.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1773)
   self.obj1773.postAction( cobj0.RHS.CREATE )

   self.obj1774=GenericGraphEdge(self)
   self.obj1774.preAction( cobj0.RHS.CREATE )
   self.obj1774.isGraphObjectVisual = True

   if(hasattr(self.obj1774, '_setHierarchicalLink')):
     self.obj1774._setHierarchicalLink(False)

   self.obj1774.GGLabel.setValue(13)
   self.obj1774.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(175.0,234.0,self.obj1774)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1774.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1774)
   self.obj1774.postAction( cobj0.RHS.CREATE )

   self.obj1762.out_connections_.append(self.obj1766)
   self.obj1766.in_connections_.append(self.obj1762)
   self.obj1762.graphObject_.pendingConnections.append((self.obj1762.graphObject_.tag, self.obj1766.graphObject_.tag, [264.0, 50.0, 311.5, 63.25], 2, 0))
   self.obj1763.out_connections_.append(self.obj1768)
   self.obj1768.in_connections_.append(self.obj1763)
   self.obj1763.graphObject_.pendingConnections.append((self.obj1763.graphObject_.tag, self.obj1768.graphObject_.tag, [306.0, 210.0, 379.5, 235.25], 2, 0))
   self.obj1764.out_connections_.append(self.obj1767)
   self.obj1767.in_connections_.append(self.obj1764)
   self.obj1764.graphObject_.pendingConnections.append((self.obj1764.graphObject_.tag, self.obj1767.graphObject_.tag, [333.0, 108.0, 331.0, 142.0, 324.25, 167.5], 2, True))
   self.obj1766.out_connections_.append(self.obj1764)
   self.obj1764.in_connections_.append(self.obj1766)
   self.obj1766.graphObject_.pendingConnections.append((self.obj1766.graphObject_.tag, self.obj1764.graphObject_.tag, [330.0, 101.0, 311.5, 63.25], 2, 0))
   self.obj1767.out_connections_.append(self.obj1763)
   self.obj1763.in_connections_.append(self.obj1767)
   self.obj1767.graphObject_.pendingConnections.append((self.obj1767.graphObject_.tag, self.obj1763.graphObject_.tag, [306.0, 210.0, 317.5, 193.0, 324.25, 167.5], 2, True))
   self.obj1768.out_connections_.append(self.obj1765)
   self.obj1765.in_connections_.append(self.obj1768)
   self.obj1768.graphObject_.pendingConnections.append((self.obj1768.graphObject_.tag, self.obj1765.graphObject_.tag, [413.0, 268.0, 379.5, 235.25], 2, 0))
   self.obj1769.out_connections_.append(self.obj1771)
   self.obj1771.in_connections_.append(self.obj1769)
   self.obj1769.graphObject_.pendingConnections.append((self.obj1769.graphObject_.tag, self.obj1771.graphObject_.tag, [91.0, 180.0, 84.5, 131.5], 2, 0))
   self.obj1770.out_connections_.append(self.obj1769)
   self.obj1769.in_connections_.append(self.obj1770)
   self.obj1770.graphObject_.pendingConnections.append((self.obj1770.graphObject_.tag, self.obj1769.graphObject_.tag, [97.0, 82.0, 84.5, 131.5], 2, 0))
   self.obj1770.out_connections_.append(self.obj1772)
   self.obj1772.in_connections_.append(self.obj1770)
   self.obj1770.graphObject_.pendingConnections.append((self.obj1770.graphObject_.tag, self.obj1772.graphObject_.tag, [97.0, 82.0, 174.5, 69.0], 2, 0))
   self.obj1770.out_connections_.append(self.obj1773)
   self.obj1773.in_connections_.append(self.obj1770)
   self.obj1770.graphObject_.pendingConnections.append((self.obj1770.graphObject_.tag, self.obj1773.graphObject_.tag, [97.0, 82.0, 245.75, 97.25], 2, 0))
   self.obj1771.out_connections_.append(self.obj1774)
   self.obj1774.in_connections_.append(self.obj1771)
   self.obj1771.graphObject_.pendingConnections.append((self.obj1771.graphObject_.tag, self.obj1774.graphObject_.tag, [91.0, 225.0, 175.0, 234.0], 2, 0))
   self.obj1772.out_connections_.append(self.obj1762)
   self.obj1762.in_connections_.append(self.obj1772)
   self.obj1772.graphObject_.pendingConnections.append((self.obj1772.graphObject_.tag, self.obj1762.graphObject_.tag, [264.0, 50.0, 174.5, 69.0], 2, 0))
   self.obj1773.out_connections_.append(self.obj1764)
   self.obj1764.in_connections_.append(self.obj1773)
   self.obj1773.graphObject_.pendingConnections.append((self.obj1773.graphObject_.tag, self.obj1764.graphObject_.tag, [300.0, 101.0, 245.75, 97.25], 2, 0))
   self.obj1774.out_connections_.append(self.obj1763)
   self.obj1763.in_connections_.append(self.obj1774)
   self.obj1774.graphObject_.pendingConnections.append((self.obj1774.graphObject_.tag, self.obj1763.graphObject_.tag, [266.0, 242.0, 175.0, 234.0], 2, 0))

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

   self.obj1781=rawMaterial(self)
   self.obj1781.preAction( cobj0.LHS.CREATE )
   self.obj1781.isGraphObjectVisual = True

   if(hasattr(self.obj1781, '_setHierarchicalLink')):
     self.obj1781._setHierarchicalLink(False)

   # MaxFlow
   self.obj1781.MaxFlow.setNone()

   # price
   self.obj1781.price.setNone()

   # Name
   self.obj1781.Name.setValue('')
   self.obj1781.Name.setNone()

   # ReqFlow
   self.obj1781.ReqFlow.setNone()

   self.obj1781.GGLabel.setValue(1)
   self.obj1781.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(280.0,60.0,self.obj1781)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['Text Scale'] = 0.5
      new_obj.layConstraints['scale'] = [0.5, 0.5]
   else: new_obj = None
   self.obj1781.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1781)
   self.obj1781.postAction( cobj0.LHS.CREATE )

   self.obj1782=Agent(self)
   self.obj1782.preAction( cobj0.LHS.CREATE )
   self.obj1782.isGraphObjectVisual = True

   if(hasattr(self.obj1782, '_setHierarchicalLink')):
     self.obj1782._setHierarchicalLink(False)

   # price
   self.obj1782.price.setNone()

   # name
   self.obj1782.name.setValue('')
   self.obj1782.name.setNone()

   self.obj1782.GGLabel.setValue(2)
   self.obj1782.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(120.0,60.0,self.obj1782)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['Text Scale'] = 0.5
      new_obj.layConstraints['scale'] = [0.5, 0.5]
   else: new_obj = None
   self.obj1782.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1782)
   self.obj1782.postAction( cobj0.LHS.CREATE )

   self.obj1783=GenericGraphEdge(self)
   self.obj1783.preAction( cobj0.LHS.CREATE )
   self.obj1783.isGraphObjectVisual = True

   if(hasattr(self.obj1783, '_setHierarchicalLink')):
     self.obj1783._setHierarchicalLink(False)

   self.obj1783.GGLabel.setValue(3)
   self.obj1783.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(198.5,126.5,self.obj1783)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1783.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1783)
   self.obj1783.postAction( cobj0.LHS.CREATE )

   self.obj1782.out_connections_.append(self.obj1783)
   self.obj1783.in_connections_.append(self.obj1782)
   self.obj1782.graphObject_.pendingConnections.append((self.obj1782.graphObject_.tag, self.obj1783.graphObject_.tag, [105.0, 89.5, 130.0, 127.0, 198.5, 126.5], 2, True))
   self.obj1783.out_connections_.append(self.obj1781)
   self.obj1781.in_connections_.append(self.obj1783)
   self.obj1783.graphObject_.pendingConnections.append((self.obj1783.graphObject_.tag, self.obj1781.graphObject_.tag, [290.5, 89.5, 267.0, 126.0, 198.5, 126.5], 2, True))

   cobj0.RHS = ASG_pns(self)
   cobj0.RHS.merge(ASG_omacs(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj1787=rawMaterial(self)
   self.obj1787.preAction( cobj0.RHS.CREATE )
   self.obj1787.isGraphObjectVisual = True

   if(hasattr(self.obj1787, '_setHierarchicalLink')):
     self.obj1787._setHierarchicalLink(False)

   # MaxFlow
   self.obj1787.MaxFlow.setNone()

   # price
   self.obj1787.price.setNone()

   # Name
   self.obj1787.Name.setValue('')
   self.obj1787.Name.setNone()

   # ReqFlow
   self.obj1787.ReqFlow.setNone()

   self.obj1787.GGLabel.setValue(1)
   self.obj1787.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(280.0,60.0,self.obj1787)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1787.graphObject_ = new_obj
   self.obj17870= AttrCalc()
   self.obj17870.Copy=ATOM3Boolean()
   self.obj17870.Copy.setValue(('Copy from LHS', 1))
   self.obj17870.Copy.config = 0
   self.obj17870.Specify=ATOM3Constraint()
   self.obj17870.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1787.GGset2Any['MaxFlow']= self.obj17870
   self.obj17871= AttrCalc()
   self.obj17871.Copy=ATOM3Boolean()
   self.obj17871.Copy.setValue(('Copy from LHS', 0))
   self.obj17871.Copy.config = 0
   self.obj17871.Specify=ATOM3Constraint()
   self.obj17871.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(2)).price.getValue()\n\n\n\n\n\n\n'))
   self.obj1787.GGset2Any['price']= self.obj17871
   self.obj17872= AttrCalc()
   self.obj17872.Copy=ATOM3Boolean()
   self.obj17872.Copy.setValue(('Copy from LHS', 1))
   self.obj17872.Copy.config = 0
   self.obj17872.Specify=ATOM3Constraint()
   self.obj17872.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1787.GGset2Any['Name']= self.obj17872
   self.obj17873= AttrCalc()
   self.obj17873.Copy=ATOM3Boolean()
   self.obj17873.Copy.setValue(('Copy from LHS', 1))
   self.obj17873.Copy.config = 0
   self.obj17873.Specify=ATOM3Constraint()
   self.obj17873.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1787.GGset2Any['ReqFlow']= self.obj17873

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1787)
   self.obj1787.postAction( cobj0.RHS.CREATE )

   self.obj1788=Agent(self)
   self.obj1788.preAction( cobj0.RHS.CREATE )
   self.obj1788.isGraphObjectVisual = True

   if(hasattr(self.obj1788, '_setHierarchicalLink')):
     self.obj1788._setHierarchicalLink(False)

   # price
   self.obj1788.price.setNone()

   # name
   self.obj1788.name.setValue('')
   self.obj1788.name.setNone()

   self.obj1788.GGLabel.setValue(2)
   self.obj1788.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(120.0,60.0,self.obj1788)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1788.graphObject_ = new_obj
   self.obj17880= AttrCalc()
   self.obj17880.Copy=ATOM3Boolean()
   self.obj17880.Copy.setValue(('Copy from LHS', 1))
   self.obj17880.Copy.config = 0
   self.obj17880.Specify=ATOM3Constraint()
   self.obj17880.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1788.GGset2Any['price']= self.obj17880
   self.obj17881= AttrCalc()
   self.obj17881.Copy=ATOM3Boolean()
   self.obj17881.Copy.setValue(('Copy from LHS', 1))
   self.obj17881.Copy.config = 0
   self.obj17881.Specify=ATOM3Constraint()
   self.obj17881.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1788.GGset2Any['name']= self.obj17881

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1788)
   self.obj1788.postAction( cobj0.RHS.CREATE )

   self.obj1789=GenericGraphEdge(self)
   self.obj1789.preAction( cobj0.RHS.CREATE )
   self.obj1789.isGraphObjectVisual = True

   if(hasattr(self.obj1789, '_setHierarchicalLink')):
     self.obj1789._setHierarchicalLink(False)

   self.obj1789.GGLabel.setValue(3)
   self.obj1789.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(198.5,126.5,self.obj1789)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1789.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1789)
   self.obj1789.postAction( cobj0.RHS.CREATE )

   self.obj1788.out_connections_.append(self.obj1789)
   self.obj1789.in_connections_.append(self.obj1788)
   self.obj1788.graphObject_.pendingConnections.append((self.obj1788.graphObject_.tag, self.obj1789.graphObject_.tag, [157.0, 122.0, 198.5, 126.5], 2, 0))
   self.obj1789.out_connections_.append(self.obj1787)
   self.obj1787.in_connections_.append(self.obj1789)
   self.obj1789.graphObject_.pendingConnections.append((self.obj1789.graphObject_.tag, self.obj1787.graphObject_.tag, [304.0, 110.0, 198.5, 126.5], 2, 0))

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

   self.obj1796=operatingUnit(self)
   self.obj1796.preAction( cobj0.LHS.CREATE )
   self.obj1796.isGraphObjectVisual = True

   if(hasattr(self.obj1796, '_setHierarchicalLink')):
     self.obj1796._setHierarchicalLink(False)

   # OperCostProp
   self.obj1796.OperCostProp.setNone()

   # name
   self.obj1796.name.setValue('')
   self.obj1796.name.setNone()

   # OperCostFix
   self.obj1796.OperCostFix.setNone()

   self.obj1796.GGLabel.setValue(4)
   self.obj1796.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(280.0,120.0,self.obj1796)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1796.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1796)
   self.obj1796.postAction( cobj0.LHS.CREATE )

   self.obj1797=CapableOf(self)
   self.obj1797.preAction( cobj0.LHS.CREATE )
   self.obj1797.isGraphObjectVisual = True

   if(hasattr(self.obj1797, '_setHierarchicalLink')):
     self.obj1797._setHierarchicalLink(False)

   # rate
   self.obj1797.rate.setNone()

   self.obj1797.GGLabel.setValue(5)
   self.obj1797.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(160.5,121.5,self.obj1797)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1797.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1797)
   self.obj1797.postAction( cobj0.LHS.CREATE )

   self.obj1798=Agent(self)
   self.obj1798.preAction( cobj0.LHS.CREATE )
   self.obj1798.isGraphObjectVisual = True

   if(hasattr(self.obj1798, '_setHierarchicalLink')):
     self.obj1798._setHierarchicalLink(False)

   # price
   self.obj1798.price.setNone()

   # name
   self.obj1798.name.setValue('')
   self.obj1798.name.setNone()

   self.obj1798.GGLabel.setValue(1)
   self.obj1798.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(120.0,40.0,self.obj1798)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1798.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1798)
   self.obj1798.postAction( cobj0.LHS.CREATE )

   self.obj1799=Role(self)
   self.obj1799.preAction( cobj0.LHS.CREATE )
   self.obj1799.isGraphObjectVisual = True

   if(hasattr(self.obj1799, '_setHierarchicalLink')):
     self.obj1799._setHierarchicalLink(False)

   # name
   self.obj1799.name.setValue('')
   self.obj1799.name.setNone()

   self.obj1799.GGLabel.setValue(2)
   self.obj1799.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(140.0,140.0,self.obj1799)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1799.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1799)
   self.obj1799.postAction( cobj0.LHS.CREATE )

   self.obj1800=GenericGraphEdge(self)
   self.obj1800.preAction( cobj0.LHS.CREATE )
   self.obj1800.isGraphObjectVisual = True

   if(hasattr(self.obj1800, '_setHierarchicalLink')):
     self.obj1800._setHierarchicalLink(False)

   self.obj1800.GGLabel.setValue(3)
   self.obj1800.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(264.75,85.25,self.obj1800)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1800.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1800)
   self.obj1800.postAction( cobj0.LHS.CREATE )

   self.obj1797.out_connections_.append(self.obj1799)
   self.obj1799.in_connections_.append(self.obj1797)
   self.obj1797.graphObject_.pendingConnections.append((self.obj1797.graphObject_.tag, self.obj1799.graphObject_.tag, [164.0, 141.0, 160.5, 121.5], 0, True))
   self.obj1798.out_connections_.append(self.obj1800)
   self.obj1800.in_connections_.append(self.obj1798)
   self.obj1798.graphObject_.pendingConnections.append((self.obj1798.graphObject_.tag, self.obj1800.graphObject_.tag, [145.0, 102.0, 226.0, 83.0, 264.75, 85.25], 2, True))
   self.obj1798.out_connections_.append(self.obj1797)
   self.obj1797.in_connections_.append(self.obj1798)
   self.obj1798.graphObject_.pendingConnections.append((self.obj1798.graphObject_.tag, self.obj1797.graphObject_.tag, [157.0, 102.0, 160.5, 121.5], 0, True))
   self.obj1800.out_connections_.append(self.obj1796)
   self.obj1796.in_connections_.append(self.obj1800)
   self.obj1800.graphObject_.pendingConnections.append((self.obj1800.graphObject_.tag, self.obj1796.graphObject_.tag, [300.0, 121.0, 264.75, 85.25], 2, 0))

   cobj0.RHS = ASG_pns(self)
   cobj0.RHS.merge(ASG_omacs(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj1804=operatingUnit(self)
   self.obj1804.preAction( cobj0.RHS.CREATE )
   self.obj1804.isGraphObjectVisual = True

   if(hasattr(self.obj1804, '_setHierarchicalLink')):
     self.obj1804._setHierarchicalLink(False)

   # OperCostProp
   self.obj1804.OperCostProp.setNone()

   # name
   self.obj1804.name.setValue('')
   self.obj1804.name.setNone()

   # OperCostFix
   self.obj1804.OperCostFix.setNone()

   self.obj1804.GGLabel.setValue(4)
   self.obj1804.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(280.0,120.0,self.obj1804)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1804.graphObject_ = new_obj
   self.obj18040= AttrCalc()
   self.obj18040.Copy=ATOM3Boolean()
   self.obj18040.Copy.setValue(('Copy from LHS', 0))
   self.obj18040.Copy.config = 0
   self.obj18040.Specify=ATOM3Constraint()
   self.obj18040.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'a = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) ).name.getValue()\nb = self.getMatched ( graphID , self.LHS.nodeWithLabel(2) ).name.getValue()\nreturn self.graphRewritingSystem.Dictag[ a ][b]\n\n'))
   self.obj1804.GGset2Any['OperCostProp']= self.obj18040
   self.obj18041= AttrCalc()
   self.obj18041.Copy=ATOM3Boolean()
   self.obj18041.Copy.setValue(('Copy from LHS', 1))
   self.obj18041.Copy.config = 0
   self.obj18041.Specify=ATOM3Constraint()
   self.obj18041.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1804.GGset2Any['name']= self.obj18041
   self.obj18042= AttrCalc()
   self.obj18042.Copy=ATOM3Boolean()
   self.obj18042.Copy.setValue(('Copy from LHS', 0))
   self.obj18042.Copy.config = 0
   self.obj18042.Specify=ATOM3Constraint()
   self.obj18042.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1804.GGset2Any['OperCostFix']= self.obj18042

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1804)
   self.obj1804.postAction( cobj0.RHS.CREATE )

   self.obj1805=CapableOf(self)
   self.obj1805.preAction( cobj0.RHS.CREATE )
   self.obj1805.isGraphObjectVisual = True

   if(hasattr(self.obj1805, '_setHierarchicalLink')):
     self.obj1805._setHierarchicalLink(False)

   # rate
   self.obj1805.rate.setNone()

   self.obj1805.GGLabel.setValue(5)
   self.obj1805.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(160.5,121.5,self.obj1805)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1805.graphObject_ = new_obj
   self.obj18050= AttrCalc()
   self.obj18050.Copy=ATOM3Boolean()
   self.obj18050.Copy.setValue(('Copy from LHS', 1))
   self.obj18050.Copy.config = 0
   self.obj18050.Specify=ATOM3Constraint()
   self.obj18050.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1805.GGset2Any['rate']= self.obj18050

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1805)
   self.obj1805.postAction( cobj0.RHS.CREATE )

   self.obj1806=Agent(self)
   self.obj1806.preAction( cobj0.RHS.CREATE )
   self.obj1806.isGraphObjectVisual = True

   if(hasattr(self.obj1806, '_setHierarchicalLink')):
     self.obj1806._setHierarchicalLink(False)

   # price
   self.obj1806.price.setNone()

   # name
   self.obj1806.name.setValue('')
   self.obj1806.name.setNone()

   self.obj1806.GGLabel.setValue(1)
   self.obj1806.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(120.0,40.0,self.obj1806)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1806.graphObject_ = new_obj
   self.obj18060= AttrCalc()
   self.obj18060.Copy=ATOM3Boolean()
   self.obj18060.Copy.setValue(('Copy from LHS', 1))
   self.obj18060.Copy.config = 0
   self.obj18060.Specify=ATOM3Constraint()
   self.obj18060.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1806.GGset2Any['price']= self.obj18060
   self.obj18061= AttrCalc()
   self.obj18061.Copy=ATOM3Boolean()
   self.obj18061.Copy.setValue(('Copy from LHS', 1))
   self.obj18061.Copy.config = 0
   self.obj18061.Specify=ATOM3Constraint()
   self.obj18061.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1806.GGset2Any['name']= self.obj18061

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1806)
   self.obj1806.postAction( cobj0.RHS.CREATE )

   self.obj1807=Role(self)
   self.obj1807.preAction( cobj0.RHS.CREATE )
   self.obj1807.isGraphObjectVisual = True

   if(hasattr(self.obj1807, '_setHierarchicalLink')):
     self.obj1807._setHierarchicalLink(False)

   # name
   self.obj1807.name.setValue('')
   self.obj1807.name.setNone()

   self.obj1807.GGLabel.setValue(2)
   self.obj1807.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(140.0,140.0,self.obj1807)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1807.graphObject_ = new_obj
   self.obj18070= AttrCalc()
   self.obj18070.Copy=ATOM3Boolean()
   self.obj18070.Copy.setValue(('Copy from LHS', 1))
   self.obj18070.Copy.config = 0
   self.obj18070.Specify=ATOM3Constraint()
   self.obj18070.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1807.GGset2Any['name']= self.obj18070

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1807)
   self.obj1807.postAction( cobj0.RHS.CREATE )

   self.obj1808=GenericGraphEdge(self)
   self.obj1808.preAction( cobj0.RHS.CREATE )
   self.obj1808.isGraphObjectVisual = True

   if(hasattr(self.obj1808, '_setHierarchicalLink')):
     self.obj1808._setHierarchicalLink(False)

   self.obj1808.GGLabel.setValue(3)
   self.obj1808.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(264.75,85.25,self.obj1808)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1808.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1808)
   self.obj1808.postAction( cobj0.RHS.CREATE )

   self.obj1805.out_connections_.append(self.obj1807)
   self.obj1807.in_connections_.append(self.obj1805)
   self.obj1805.graphObject_.pendingConnections.append((self.obj1805.graphObject_.tag, self.obj1807.graphObject_.tag, [171.0, 140.0, 160.5, 121.5], 2, 0))
   self.obj1806.out_connections_.append(self.obj1808)
   self.obj1808.in_connections_.append(self.obj1806)
   self.obj1806.graphObject_.pendingConnections.append((self.obj1806.graphObject_.tag, self.obj1808.graphObject_.tag, [157.0, 102.0, 264.75, 85.25], 2, 0))
   self.obj1806.out_connections_.append(self.obj1805)
   self.obj1805.in_connections_.append(self.obj1806)
   self.obj1806.graphObject_.pendingConnections.append((self.obj1806.graphObject_.tag, self.obj1805.graphObject_.tag, [157.0, 102.0, 160.5, 121.5], 2, 0))
   self.obj1808.out_connections_.append(self.obj1804)
   self.obj1804.in_connections_.append(self.obj1808)
   self.obj1808.graphObject_.pendingConnections.append((self.obj1808.graphObject_.tag, self.obj1804.graphObject_.tag, [300.0, 121.0, 264.75, 85.25], 2, 0))

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

   self.obj1815=metarial(self)
   self.obj1815.preAction( cobj0.LHS.CREATE )
   self.obj1815.isGraphObjectVisual = True

   if(hasattr(self.obj1815, '_setHierarchicalLink')):
     self.obj1815._setHierarchicalLink(False)

   # MaxFlow
   self.obj1815.MaxFlow.setNone()

   # price
   self.obj1815.price.setValue(0)

   # Name
   self.obj1815.Name.setValue('')
   self.obj1815.Name.setNone()

   # ReqFlow
   self.obj1815.ReqFlow.setNone()

   self.obj1815.GGLabel.setValue(1)
   self.obj1815.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(280.0,60.0,self.obj1815)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1815.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1815)
   self.obj1815.postAction( cobj0.LHS.CREATE )

   self.obj1816=Goal(self)
   self.obj1816.preAction( cobj0.LHS.CREATE )
   self.obj1816.isGraphObjectVisual = True

   if(hasattr(self.obj1816, '_setHierarchicalLink')):
     self.obj1816._setHierarchicalLink(False)

   # name
   self.obj1816.name.setValue('')
   self.obj1816.name.setNone()

   self.obj1816.GGLabel.setValue(3)
   self.obj1816.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(100.0,60.0,self.obj1816)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1816.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1816)
   self.obj1816.postAction( cobj0.LHS.CREATE )

   self.obj1817=GenericGraphEdge(self)
   self.obj1817.preAction( cobj0.LHS.CREATE )
   self.obj1817.isGraphObjectVisual = True

   if(hasattr(self.obj1817, '_setHierarchicalLink')):
     self.obj1817._setHierarchicalLink(False)

   self.obj1817.GGLabel.setValue(4)
   self.obj1817.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(205.0,106.0,self.obj1817)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1817.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1817)
   self.obj1817.postAction( cobj0.LHS.CREATE )

   self.obj1816.out_connections_.append(self.obj1817)
   self.obj1817.in_connections_.append(self.obj1816)
   self.obj1816.graphObject_.pendingConnections.append((self.obj1816.graphObject_.tag, self.obj1817.graphObject_.tag, [124.0, 110.0, 205.0, 106.0], 0, True))
   self.obj1817.out_connections_.append(self.obj1815)
   self.obj1815.in_connections_.append(self.obj1817)
   self.obj1817.graphObject_.pendingConnections.append((self.obj1817.graphObject_.tag, self.obj1815.graphObject_.tag, [286.0, 102.0, 205.0, 106.0], 0, True))

   cobj0.RHS = ASG_pns(self)

   self.obj1819=metarial(self)
   self.obj1819.preAction( cobj0.RHS.CREATE )
   self.obj1819.isGraphObjectVisual = True

   if(hasattr(self.obj1819, '_setHierarchicalLink')):
     self.obj1819._setHierarchicalLink(False)

   # MaxFlow
   self.obj1819.MaxFlow.setNone()

   # price
   self.obj1819.price.setValue(0)

   # Name
   self.obj1819.Name.setValue('')
   self.obj1819.Name.setNone()

   # ReqFlow
   self.obj1819.ReqFlow.setNone()

   self.obj1819.GGLabel.setValue(1)
   self.obj1819.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(180.0,40.0,self.obj1819)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1819.graphObject_ = new_obj
   self.obj18190= AttrCalc()
   self.obj18190.Copy=ATOM3Boolean()
   self.obj18190.Copy.setValue(('Copy from LHS', 1))
   self.obj18190.Copy.config = 0
   self.obj18190.Specify=ATOM3Constraint()
   self.obj18190.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1819.GGset2Any['MaxFlow']= self.obj18190
   self.obj18191= AttrCalc()
   self.obj18191.Copy=ATOM3Boolean()
   self.obj18191.Copy.setValue(('Copy from LHS', 1))
   self.obj18191.Copy.config = 0
   self.obj18191.Specify=ATOM3Constraint()
   self.obj18191.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1819.GGset2Any['Name']= self.obj18191
   self.obj18192= AttrCalc()
   self.obj18192.Copy=ATOM3Boolean()
   self.obj18192.Copy.setValue(('Copy from LHS', 1))
   self.obj18192.Copy.config = 0
   self.obj18192.Specify=ATOM3Constraint()
   self.obj18192.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1819.GGset2Any['ReqFlow']= self.obj18192

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1819)
   self.obj1819.postAction( cobj0.RHS.CREATE )


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

   self.obj1826=rawMaterial(self)
   self.obj1826.preAction( cobj0.LHS.CREATE )
   self.obj1826.isGraphObjectVisual = True

   if(hasattr(self.obj1826, '_setHierarchicalLink')):
     self.obj1826._setHierarchicalLink(False)

   # MaxFlow
   self.obj1826.MaxFlow.setNone()

   # price
   self.obj1826.price.setNone()

   # Name
   self.obj1826.Name.setValue('')
   self.obj1826.Name.setNone()

   # ReqFlow
   self.obj1826.ReqFlow.setNone()

   self.obj1826.GGLabel.setValue(2)
   self.obj1826.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(260.0,40.0,self.obj1826)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1826.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1826)
   self.obj1826.postAction( cobj0.LHS.CREATE )

   self.obj1827=operatingUnit(self)
   self.obj1827.preAction( cobj0.LHS.CREATE )
   self.obj1827.isGraphObjectVisual = True

   if(hasattr(self.obj1827, '_setHierarchicalLink')):
     self.obj1827._setHierarchicalLink(False)

   # OperCostProp
   self.obj1827.OperCostProp.setNone()

   # name
   self.obj1827.name.setValue('')
   self.obj1827.name.setNone()

   # OperCostFix
   self.obj1827.OperCostFix.setNone()

   self.obj1827.GGLabel.setValue(3)
   self.obj1827.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(280.0,140.0,self.obj1827)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1827.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1827)
   self.obj1827.postAction( cobj0.LHS.CREATE )

   self.obj1828=fromRaw(self)
   self.obj1828.preAction( cobj0.LHS.CREATE )
   self.obj1828.isGraphObjectVisual = True

   if(hasattr(self.obj1828, '_setHierarchicalLink')):
     self.obj1828._setHierarchicalLink(False)

   # rate
   self.obj1828.rate.setNone()

   self.obj1828.GGLabel.setValue(5)
   self.obj1828.graphClass_= graph_fromRaw
   if self.genGraphics:
      new_obj = graph_fromRaw(292.0,123.5,self.obj1828)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1828.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1828)
   self.obj1828.postAction( cobj0.LHS.CREATE )

   self.obj1829=Agent(self)
   self.obj1829.preAction( cobj0.LHS.CREATE )
   self.obj1829.isGraphObjectVisual = True

   if(hasattr(self.obj1829, '_setHierarchicalLink')):
     self.obj1829._setHierarchicalLink(False)

   # price
   self.obj1829.price.setNone()

   # name
   self.obj1829.name.setValue('')
   self.obj1829.name.setNone()

   self.obj1829.GGLabel.setValue(1)
   self.obj1829.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(60.0,60.0,self.obj1829)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1829.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1829)
   self.obj1829.postAction( cobj0.LHS.CREATE )

   self.obj1830=GenericGraphEdge(self)
   self.obj1830.preAction( cobj0.LHS.CREATE )
   self.obj1830.isGraphObjectVisual = True

   if(hasattr(self.obj1830, '_setHierarchicalLink')):
     self.obj1830._setHierarchicalLink(False)

   self.obj1830.GGLabel.setValue(4)
   self.obj1830.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(184.5,109.0,self.obj1830)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1830.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1830)
   self.obj1830.postAction( cobj0.LHS.CREATE )

   self.obj1831=GenericGraphEdge(self)
   self.obj1831.preAction( cobj0.LHS.CREATE )
   self.obj1831.isGraphObjectVisual = True

   if(hasattr(self.obj1831, '_setHierarchicalLink')):
     self.obj1831._setHierarchicalLink(False)

   self.obj1831.GGLabel.setValue(6)
   self.obj1831.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(159.0,150.5,self.obj1831)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1831.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1831)
   self.obj1831.postAction( cobj0.LHS.CREATE )

   self.obj1826.out_connections_.append(self.obj1828)
   self.obj1828.in_connections_.append(self.obj1826)
   self.obj1826.graphObject_.pendingConnections.append((self.obj1826.graphObject_.tag, self.obj1828.graphObject_.tag, [284.0, 96.0, 292.0, 123.5], 0, True))
   self.obj1828.out_connections_.append(self.obj1827)
   self.obj1827.in_connections_.append(self.obj1828)
   self.obj1828.graphObject_.pendingConnections.append((self.obj1828.graphObject_.tag, self.obj1827.graphObject_.tag, [300.0, 151.0, 292.0, 123.5], 0, True))
   self.obj1829.out_connections_.append(self.obj1830)
   self.obj1830.in_connections_.append(self.obj1829)
   self.obj1829.graphObject_.pendingConnections.append((self.obj1829.graphObject_.tag, self.obj1830.graphObject_.tag, [85.0, 122.0, 184.5, 109.0], 0, True))
   self.obj1829.out_connections_.append(self.obj1831)
   self.obj1831.in_connections_.append(self.obj1829)
   self.obj1829.graphObject_.pendingConnections.append((self.obj1829.graphObject_.tag, self.obj1831.graphObject_.tag, [85.0, 122.0, 105.5, 141.5, 159.0, 150.5], 2, True))
   self.obj1830.out_connections_.append(self.obj1826)
   self.obj1826.in_connections_.append(self.obj1830)
   self.obj1830.graphObject_.pendingConnections.append((self.obj1830.graphObject_.tag, self.obj1826.graphObject_.tag, [284.0, 96.0, 184.5, 109.0], 0, True))
   self.obj1831.out_connections_.append(self.obj1827)
   self.obj1827.in_connections_.append(self.obj1831)
   self.obj1831.graphObject_.pendingConnections.append((self.obj1831.graphObject_.tag, self.obj1827.graphObject_.tag, [299.0, 158.0, 212.5, 159.5, 159.0, 150.5], 2, True))

   cobj0.RHS = ASG_pns(self)

   self.obj1833=rawMaterial(self)
   self.obj1833.preAction( cobj0.RHS.CREATE )
   self.obj1833.isGraphObjectVisual = True

   if(hasattr(self.obj1833, '_setHierarchicalLink')):
     self.obj1833._setHierarchicalLink(False)

   # MaxFlow
   self.obj1833.MaxFlow.setValue(999999)

   # price
   self.obj1833.price.setValue(0)

   # Name
   self.obj1833.Name.setValue('')
   self.obj1833.Name.setNone()

   # ReqFlow
   self.obj1833.ReqFlow.setValue(0)

   self.obj1833.GGLabel.setValue(2)
   self.obj1833.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(160.0,40.0,self.obj1833)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['Text Scale'] = 1.0
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1833.graphObject_ = new_obj
   self.obj18330= AttrCalc()
   self.obj18330.Copy=ATOM3Boolean()
   self.obj18330.Copy.setValue(('Copy from LHS', 1))
   self.obj18330.Copy.config = 0
   self.obj18330.Specify=ATOM3Constraint()
   self.obj18330.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1833.GGset2Any['MaxFlow']= self.obj18330
   self.obj18331= AttrCalc()
   self.obj18331.Copy=ATOM3Boolean()
   self.obj18331.Copy.setValue(('Copy from LHS', 0))
   self.obj18331.Copy.config = 0
   self.obj18331.Specify=ATOM3Constraint()
   self.obj18331.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).price.getValue()\n'))
   self.obj1833.GGset2Any['price']= self.obj18331
   self.obj18332= AttrCalc()
   self.obj18332.Copy=ATOM3Boolean()
   self.obj18332.Copy.setValue(('Copy from LHS', 1))
   self.obj18332.Copy.config = 0
   self.obj18332.Specify=ATOM3Constraint()
   self.obj18332.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1833.GGset2Any['Name']= self.obj18332
   self.obj18333= AttrCalc()
   self.obj18333.Copy=ATOM3Boolean()
   self.obj18333.Copy.setValue(('Copy from LHS', 1))
   self.obj18333.Copy.config = 0
   self.obj18333.Specify=ATOM3Constraint()
   self.obj18333.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1833.GGset2Any['ReqFlow']= self.obj18333

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1833)
   self.obj1833.postAction( cobj0.RHS.CREATE )

   self.obj1834=operatingUnit(self)
   self.obj1834.preAction( cobj0.RHS.CREATE )
   self.obj1834.isGraphObjectVisual = True

   if(hasattr(self.obj1834, '_setHierarchicalLink')):
     self.obj1834._setHierarchicalLink(False)

   # OperCostProp
   self.obj1834.OperCostProp.setValue(0.0)

   # name
   self.obj1834.name.setValue('')
   self.obj1834.name.setNone()

   # OperCostFix
   self.obj1834.OperCostFix.setValue(0.0)

   self.obj1834.GGLabel.setValue(3)
   self.obj1834.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(120.0,160.0,self.obj1834)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1834.graphObject_ = new_obj
   self.obj18340= AttrCalc()
   self.obj18340.Copy=ATOM3Boolean()
   self.obj18340.Copy.setValue(('Copy from LHS', 1))
   self.obj18340.Copy.config = 0
   self.obj18340.Specify=ATOM3Constraint()
   self.obj18340.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1834.GGset2Any['OperCostProp']= self.obj18340
   self.obj18341= AttrCalc()
   self.obj18341.Copy=ATOM3Boolean()
   self.obj18341.Copy.setValue(('Copy from LHS', 1))
   self.obj18341.Copy.config = 0
   self.obj18341.Specify=ATOM3Constraint()
   self.obj18341.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1834.GGset2Any['name']= self.obj18341
   self.obj18342= AttrCalc()
   self.obj18342.Copy=ATOM3Boolean()
   self.obj18342.Copy.setValue(('Copy from LHS', 1))
   self.obj18342.Copy.config = 0
   self.obj18342.Specify=ATOM3Constraint()
   self.obj18342.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1834.GGset2Any['OperCostFix']= self.obj18342

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1834)
   self.obj1834.postAction( cobj0.RHS.CREATE )

   self.obj1835=fromRaw(self)
   self.obj1835.preAction( cobj0.RHS.CREATE )
   self.obj1835.isGraphObjectVisual = True

   if(hasattr(self.obj1835, '_setHierarchicalLink')):
     self.obj1835._setHierarchicalLink(False)

   # rate
   self.obj1835.rate.setValue(0.0)

   self.obj1835.GGLabel.setValue(5)
   self.obj1835.graphClass_= graph_fromRaw
   if self.genGraphics:
      new_obj = graph_fromRaw(177.0,133.5,self.obj1835)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1835.graphObject_ = new_obj
   self.obj18350= AttrCalc()
   self.obj18350.Copy=ATOM3Boolean()
   self.obj18350.Copy.setValue(('Copy from LHS', 1))
   self.obj18350.Copy.config = 0
   self.obj18350.Specify=ATOM3Constraint()
   self.obj18350.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1835.GGset2Any['rate']= self.obj18350

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1835)
   self.obj1835.postAction( cobj0.RHS.CREATE )

   self.obj1833.out_connections_.append(self.obj1835)
   self.obj1835.in_connections_.append(self.obj1833)
   self.obj1833.graphObject_.pendingConnections.append((self.obj1833.graphObject_.tag, self.obj1835.graphObject_.tag, [184.0, 96.0, 177.0, 133.5], 0, True))
   self.obj1835.out_connections_.append(self.obj1834)
   self.obj1834.in_connections_.append(self.obj1835)
   self.obj1835.graphObject_.pendingConnections.append((self.obj1835.graphObject_.tag, self.obj1834.graphObject_.tag, [170.0, 171.0, 177.0, 133.5], 0, True))

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

   self.obj1841=Capabilitie(self)
   self.obj1841.preAction( cobj0.LHS.CREATE )
   self.obj1841.isGraphObjectVisual = True

   if(hasattr(self.obj1841, '_setHierarchicalLink')):
     self.obj1841._setHierarchicalLink(False)

   # name
   self.obj1841.name.setValue('')
   self.obj1841.name.setNone()

   self.obj1841.GGLabel.setValue(1)
   self.obj1841.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(220.0,80.0,self.obj1841)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1841.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1841)
   self.obj1841.postAction( cobj0.LHS.CREATE )


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

   self.obj1849=metarial(self)
   self.obj1849.preAction( cobj0.LHS.CREATE )
   self.obj1849.isGraphObjectVisual = True

   if(hasattr(self.obj1849, '_setHierarchicalLink')):
     self.obj1849._setHierarchicalLink(False)

   # MaxFlow
   self.obj1849.MaxFlow.setNone()

   # price
   self.obj1849.price.setValue(0)

   # Name
   self.obj1849.Name.setValue('')
   self.obj1849.Name.setNone()

   # ReqFlow
   self.obj1849.ReqFlow.setNone()

   self.obj1849.GGLabel.setValue(2)
   self.obj1849.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(280.0,40.0,self.obj1849)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1849.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1849)
   self.obj1849.postAction( cobj0.LHS.CREATE )

   self.obj1850=operatingUnit(self)
   self.obj1850.preAction( cobj0.LHS.CREATE )
   self.obj1850.isGraphObjectVisual = True

   if(hasattr(self.obj1850, '_setHierarchicalLink')):
     self.obj1850._setHierarchicalLink(False)

   # OperCostProp
   self.obj1850.OperCostProp.setNone()

   # name
   self.obj1850.name.setValue('')
   self.obj1850.name.setNone()

   # OperCostFix
   self.obj1850.OperCostFix.setNone()

   self.obj1850.GGLabel.setValue(3)
   self.obj1850.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(300.0,140.0,self.obj1850)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1850.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1850)
   self.obj1850.postAction( cobj0.LHS.CREATE )

   self.obj1851=fromMaterial(self)
   self.obj1851.preAction( cobj0.LHS.CREATE )
   self.obj1851.isGraphObjectVisual = True

   if(hasattr(self.obj1851, '_setHierarchicalLink')):
     self.obj1851._setHierarchicalLink(False)

   # rate
   self.obj1851.rate.setNone()

   self.obj1851.GGLabel.setValue(4)
   self.obj1851.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(342.75,113.75,self.obj1851)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1851.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1851)
   self.obj1851.postAction( cobj0.LHS.CREATE )

   self.obj1852=Role(self)
   self.obj1852.preAction( cobj0.LHS.CREATE )
   self.obj1852.isGraphObjectVisual = True

   if(hasattr(self.obj1852, '_setHierarchicalLink')):
     self.obj1852._setHierarchicalLink(False)

   # name
   self.obj1852.name.setValue('')
   self.obj1852.name.setNone()

   self.obj1852.GGLabel.setValue(1)
   self.obj1852.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(80.0,60.0,self.obj1852)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1852.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1852)
   self.obj1852.postAction( cobj0.LHS.CREATE )

   self.obj1853=GenericGraphEdge(self)
   self.obj1853.preAction( cobj0.LHS.CREATE )
   self.obj1853.isGraphObjectVisual = True

   if(hasattr(self.obj1853, '_setHierarchicalLink')):
     self.obj1853._setHierarchicalLink(False)

   self.obj1853.GGLabel.setValue(5)
   self.obj1853.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(195.0,71.5,self.obj1853)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1853.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1853)
   self.obj1853.postAction( cobj0.LHS.CREATE )

   self.obj1849.out_connections_.append(self.obj1851)
   self.obj1851.in_connections_.append(self.obj1849)
   self.obj1849.graphObject_.pendingConnections.append((self.obj1849.graphObject_.tag, self.obj1851.graphObject_.tag, [321.0, 82.0, 335.5, 96.5, 342.75, 113.75], 2, True))
   self.obj1851.out_connections_.append(self.obj1850)
   self.obj1850.in_connections_.append(self.obj1851)
   self.obj1851.graphObject_.pendingConnections.append((self.obj1851.graphObject_.tag, self.obj1850.graphObject_.tag, [350.0, 151.0, 350.0, 131.0, 342.75, 113.75], 2, True))
   self.obj1852.out_connections_.append(self.obj1853)
   self.obj1853.in_connections_.append(self.obj1852)
   self.obj1852.graphObject_.pendingConnections.append((self.obj1852.graphObject_.tag, self.obj1853.graphObject_.tag, [104.0, 61.0, 195.0, 71.5], 0, True))
   self.obj1853.out_connections_.append(self.obj1849)
   self.obj1849.in_connections_.append(self.obj1853)
   self.obj1853.graphObject_.pendingConnections.append((self.obj1853.graphObject_.tag, self.obj1849.graphObject_.tag, [286.0, 82.0, 195.0, 71.5], 0, True))

   cobj0.RHS = ASG_pns(self)

   self.obj1855=metarial(self)
   self.obj1855.preAction( cobj0.RHS.CREATE )
   self.obj1855.isGraphObjectVisual = True

   if(hasattr(self.obj1855, '_setHierarchicalLink')):
     self.obj1855._setHierarchicalLink(False)

   # MaxFlow
   self.obj1855.MaxFlow.setValue(999999)

   # price
   self.obj1855.price.setValue(0)

   # Name
   self.obj1855.Name.setValue('')
   self.obj1855.Name.setNone()

   # ReqFlow
   self.obj1855.ReqFlow.setValue(0)

   self.obj1855.GGLabel.setValue(2)
   self.obj1855.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(160.0,40.0,self.obj1855)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1855.graphObject_ = new_obj
   self.obj18550= AttrCalc()
   self.obj18550.Copy=ATOM3Boolean()
   self.obj18550.Copy.setValue(('Copy from LHS', 1))
   self.obj18550.Copy.config = 0
   self.obj18550.Specify=ATOM3Constraint()
   self.obj18550.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1855.GGset2Any['MaxFlow']= self.obj18550
   self.obj18551= AttrCalc()
   self.obj18551.Copy=ATOM3Boolean()
   self.obj18551.Copy.setValue(('Copy from LHS', 1))
   self.obj18551.Copy.config = 0
   self.obj18551.Specify=ATOM3Constraint()
   self.obj18551.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1855.GGset2Any['Name']= self.obj18551
   self.obj18552= AttrCalc()
   self.obj18552.Copy=ATOM3Boolean()
   self.obj18552.Copy.setValue(('Copy from LHS', 1))
   self.obj18552.Copy.config = 0
   self.obj18552.Specify=ATOM3Constraint()
   self.obj18552.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1855.GGset2Any['ReqFlow']= self.obj18552

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1855)
   self.obj1855.postAction( cobj0.RHS.CREATE )

   self.obj1856=operatingUnit(self)
   self.obj1856.preAction( cobj0.RHS.CREATE )
   self.obj1856.isGraphObjectVisual = True

   if(hasattr(self.obj1856, '_setHierarchicalLink')):
     self.obj1856._setHierarchicalLink(False)

   # OperCostProp
   self.obj1856.OperCostProp.setValue(0.0)

   # name
   self.obj1856.name.setValue('')
   self.obj1856.name.setNone()

   # OperCostFix
   self.obj1856.OperCostFix.setValue(0.0)

   self.obj1856.GGLabel.setValue(3)
   self.obj1856.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(200.0,140.0,self.obj1856)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1856.graphObject_ = new_obj
   self.obj18560= AttrCalc()
   self.obj18560.Copy=ATOM3Boolean()
   self.obj18560.Copy.setValue(('Copy from LHS', 1))
   self.obj18560.Copy.config = 0
   self.obj18560.Specify=ATOM3Constraint()
   self.obj18560.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1856.GGset2Any['OperCostProp']= self.obj18560
   self.obj18561= AttrCalc()
   self.obj18561.Copy=ATOM3Boolean()
   self.obj18561.Copy.setValue(('Copy from LHS', 1))
   self.obj18561.Copy.config = 0
   self.obj18561.Specify=ATOM3Constraint()
   self.obj18561.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1856.GGset2Any['name']= self.obj18561
   self.obj18562= AttrCalc()
   self.obj18562.Copy=ATOM3Boolean()
   self.obj18562.Copy.setValue(('Copy from LHS', 1))
   self.obj18562.Copy.config = 0
   self.obj18562.Specify=ATOM3Constraint()
   self.obj18562.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1856.GGset2Any['OperCostFix']= self.obj18562

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1856)
   self.obj1856.postAction( cobj0.RHS.CREATE )

   self.obj1857=fromMaterial(self)
   self.obj1857.preAction( cobj0.RHS.CREATE )
   self.obj1857.isGraphObjectVisual = True

   if(hasattr(self.obj1857, '_setHierarchicalLink')):
     self.obj1857._setHierarchicalLink(False)

   # rate
   self.obj1857.rate.setValue(0.0)

   self.obj1857.GGLabel.setValue(4)
   self.obj1857.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(238.75,106.25,self.obj1857)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1857.graphObject_ = new_obj
   self.obj18570= AttrCalc()
   self.obj18570.Copy=ATOM3Boolean()
   self.obj18570.Copy.setValue(('Copy from LHS', 1))
   self.obj18570.Copy.config = 0
   self.obj18570.Specify=ATOM3Constraint()
   self.obj18570.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1857.GGset2Any['rate']= self.obj18570

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1857)
   self.obj1857.postAction( cobj0.RHS.CREATE )

   self.obj1855.out_connections_.append(self.obj1857)
   self.obj1857.in_connections_.append(self.obj1855)
   self.obj1855.graphObject_.pendingConnections.append((self.obj1855.graphObject_.tag, self.obj1857.graphObject_.tag, [201.0, 82.0, 226.5, 89.0, 238.75, 106.25], 2, True))
   self.obj1857.out_connections_.append(self.obj1856)
   self.obj1856.in_connections_.append(self.obj1857)
   self.obj1857.graphObject_.pendingConnections.append((self.obj1857.graphObject_.tag, self.obj1856.graphObject_.tag, [250.0, 151.0, 251.0, 123.5, 238.75, 106.25], 2, True))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.graphRewritingSystem.finalStat > 20 \n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('RemoveRole2', 20)
   cobj0.Order=ATOM3Integer(29)
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

   self.obj2255=Role(self)
   self.obj2255.preAction( cobj0.LHS.CREATE )
   self.obj2255.isGraphObjectVisual = True

   if(hasattr(self.obj2255, '_setHierarchicalLink')):
     self.obj2255._setHierarchicalLink(False)

   # name
   self.obj2255.name.setValue('')
   self.obj2255.name.setNone()

   self.obj2255.GGLabel.setValue(1)
   self.obj2255.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(100.0,60.0,self.obj2255)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj2255.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj2255)
   self.obj2255.postAction( cobj0.LHS.CREATE )


   cobj0.RHS = ASG_omacs(self)


   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.graphRewritingSystem.finalStat > 20 \n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('RemoveAgent2', 20)
   cobj0.Order=ATOM3Integer(30)
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

   self.obj2423=Agent(self)
   self.obj2423.preAction( cobj0.LHS.CREATE )
   self.obj2423.isGraphObjectVisual = True

   if(hasattr(self.obj2423, '_setHierarchicalLink')):
     self.obj2423._setHierarchicalLink(False)

   # price
   self.obj2423.price.setNone()

   # name
   self.obj2423.name.setValue('')
   self.obj2423.name.setNone()

   self.obj2423.GGLabel.setValue(1)
   self.obj2423.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(160.0,60.0,self.obj2423)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj2423.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj2423)
   self.obj2423.postAction( cobj0.LHS.CREATE )


   cobj0.RHS = ASG_omacs(self)


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


