from GraphGrammarEdit import *
from GGruleEdit import *

def savedTrans(self):
   self.EditingGraphGrammar= GraphGrammarEdit(None, self)
   self.EditingGraphGrammar.Name=ATOM3String('omacs2pnsV3', 20)
   self.EditingGraphGrammar.Rules=ATOM3List([ 1, 1, 1, 0],GGruleEdit,None, self)
   lcobj0=[]
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('linkAgent2Role1', 20)
   cobj0.Order=ATOM3Integer(1)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

   from CapableOf import *
   from Goal import *
   from ASG_omacss import *
   from Agent import *
   from Capabilitie import *
   from Role import *
   from requir import *
   from achieve import *
   from posses import *

   cobj0.LHS = ASG_omacss(self)

   self.obj138=Agent(self)
   self.obj138.preAction( cobj0.LHS.CREATE )
   self.obj138.isGraphObjectVisual = True

   if(hasattr(self.obj138, '_setHierarchicalLink')):
     self.obj138._setHierarchicalLink(False)

   # price
   self.obj138.price.setValue(0)

   # name
   self.obj138.name.setValue('')
   self.obj138.name.setNone()

   self.obj138.GGLabel.setValue(1)
   self.obj138.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(80.0,40.0,self.obj138)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj138.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj138)
   self.obj138.postAction( cobj0.LHS.CREATE )

   self.obj139=Capabilitie(self)
   self.obj139.preAction( cobj0.LHS.CREATE )
   self.obj139.isGraphObjectVisual = True

   if(hasattr(self.obj139, '_setHierarchicalLink')):
     self.obj139._setHierarchicalLink(False)

   # name
   self.obj139.name.setValue('')
   self.obj139.name.setNone()

   self.obj139.GGLabel.setValue(2)
   self.obj139.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(200.0,200.0,self.obj139)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj139.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj139)
   self.obj139.postAction( cobj0.LHS.CREATE )

   self.obj140=Role(self)
   self.obj140.preAction( cobj0.LHS.CREATE )
   self.obj140.isGraphObjectVisual = True

   if(hasattr(self.obj140, '_setHierarchicalLink')):
     self.obj140._setHierarchicalLink(False)

   # name
   self.obj140.name.setValue('')
   self.obj140.name.setNone()

   self.obj140.GGLabel.setValue(3)
   self.obj140.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(320.0,60.0,self.obj140)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj140.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj140)
   self.obj140.postAction( cobj0.LHS.CREATE )

   self.obj141=posses(self)
   self.obj141.preAction( cobj0.LHS.CREATE )
   self.obj141.isGraphObjectVisual = True

   if(hasattr(self.obj141, '_setHierarchicalLink')):
     self.obj141._setHierarchicalLink(False)

   # rate
   self.obj141.rate.setNone()

   self.obj141.GGLabel.setValue(4)
   self.obj141.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(163.0,150.5,self.obj141)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj141.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj141)
   self.obj141.postAction( cobj0.LHS.CREATE )

   self.obj142=requir(self)
   self.obj142.preAction( cobj0.LHS.CREATE )
   self.obj142.isGraphObjectVisual = True

   if(hasattr(self.obj142, '_setHierarchicalLink')):
     self.obj142._setHierarchicalLink(False)

   self.obj142.GGLabel.setValue(5)
   self.obj142.graphClass_= graph_requir
   if self.genGraphics:
      new_obj = graph_requir(282.5,152.5,self.obj142)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj142.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj142)
   self.obj142.postAction( cobj0.LHS.CREATE )

   self.obj138.out_connections_.append(self.obj141)
   self.obj141.in_connections_.append(self.obj138)
   self.obj138.graphObject_.pendingConnections.append((self.obj138.graphObject_.tag, self.obj141.graphObject_.tag, [105.0, 102.0, 163.0, 150.5], 0, True))
   self.obj140.out_connections_.append(self.obj142)
   self.obj142.in_connections_.append(self.obj140)
   self.obj140.graphObject_.pendingConnections.append((self.obj140.graphObject_.tag, self.obj142.graphObject_.tag, [344.0, 106.0, 282.5, 152.5], 0, True))
   self.obj141.out_connections_.append(self.obj139)
   self.obj139.in_connections_.append(self.obj141)
   self.obj141.graphObject_.pendingConnections.append((self.obj141.graphObject_.tag, self.obj139.graphObject_.tag, [221.0, 199.0, 163.0, 150.5], 0, True))
   self.obj142.out_connections_.append(self.obj139)
   self.obj139.in_connections_.append(self.obj142)
   self.obj142.graphObject_.pendingConnections.append((self.obj142.graphObject_.tag, self.obj139.graphObject_.tag, [221.0, 199.0, 282.5, 152.5], 0, True))

   cobj0.RHS = ASG_omacss(self)

   self.obj144=Agent(self)
   self.obj144.preAction( cobj0.RHS.CREATE )
   self.obj144.isGraphObjectVisual = True

   if(hasattr(self.obj144, '_setHierarchicalLink')):
     self.obj144._setHierarchicalLink(False)

   # price
   self.obj144.price.setValue(0)

   # name
   self.obj144.name.setValue('')
   self.obj144.name.setNone()

   self.obj144.GGLabel.setValue(1)
   self.obj144.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(80.0,40.0,self.obj144)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj144.graphObject_ = new_obj
   self.obj1440= AttrCalc()
   self.obj1440.Copy=ATOM3Boolean()
   self.obj1440.Copy.setValue(('Copy from LHS', 1))
   self.obj1440.Copy.config = 0
   self.obj1440.Specify=ATOM3Constraint()
   self.obj1440.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj144.GGset2Any['price']= self.obj1440
   self.obj1441= AttrCalc()
   self.obj1441.Copy=ATOM3Boolean()
   self.obj1441.Copy.setValue(('Copy from LHS', 1))
   self.obj1441.Copy.config = 0
   self.obj1441.Specify=ATOM3Constraint()
   self.obj1441.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj144.GGset2Any['name']= self.obj1441

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj144)
   self.obj144.postAction( cobj0.RHS.CREATE )

   self.obj145=Capabilitie(self)
   self.obj145.preAction( cobj0.RHS.CREATE )
   self.obj145.isGraphObjectVisual = True

   if(hasattr(self.obj145, '_setHierarchicalLink')):
     self.obj145._setHierarchicalLink(False)

   # name
   self.obj145.name.setValue('')
   self.obj145.name.setNone()

   self.obj145.GGLabel.setValue(2)
   self.obj145.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(200.0,200.0,self.obj145)
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
   self.obj145.GGset2Any['name']= self.obj1450

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj145)
   self.obj145.postAction( cobj0.RHS.CREATE )

   self.obj146=Role(self)
   self.obj146.preAction( cobj0.RHS.CREATE )
   self.obj146.isGraphObjectVisual = True

   if(hasattr(self.obj146, '_setHierarchicalLink')):
     self.obj146._setHierarchicalLink(False)

   # name
   self.obj146.name.setValue('')
   self.obj146.name.setNone()

   self.obj146.GGLabel.setValue(3)
   self.obj146.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(320.0,60.0,self.obj146)
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
   self.obj146.GGset2Any['name']= self.obj1460

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj146)
   self.obj146.postAction( cobj0.RHS.CREATE )

   self.obj147=posses(self)
   self.obj147.preAction( cobj0.RHS.CREATE )
   self.obj147.isGraphObjectVisual = True

   if(hasattr(self.obj147, '_setHierarchicalLink')):
     self.obj147._setHierarchicalLink(False)

   # rate
   self.obj147.rate.setValue(0.0)

   self.obj147.GGLabel.setValue(4)
   self.obj147.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(163.0,150.5,self.obj147)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj147.graphObject_ = new_obj
   self.obj1470= AttrCalc()
   self.obj1470.Copy=ATOM3Boolean()
   self.obj1470.Copy.setValue(('Copy from LHS', 1))
   self.obj1470.Copy.config = 0
   self.obj1470.Specify=ATOM3Constraint()
   self.obj1470.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj147.GGset2Any['rate']= self.obj1470

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj147)
   self.obj147.postAction( cobj0.RHS.CREATE )

   self.obj148=CapableOf(self)
   self.obj148.preAction( cobj0.RHS.CREATE )
   self.obj148.isGraphObjectVisual = True

   if(hasattr(self.obj148, '_setHierarchicalLink')):
     self.obj148._setHierarchicalLink(False)

   self.obj148.GGLabel.setValue(7)
   self.obj148.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(233.5,74.0,self.obj148)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj148.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj148)
   self.obj148.postAction( cobj0.RHS.CREATE )

   self.obj149=requir(self)
   self.obj149.preAction( cobj0.RHS.CREATE )
   self.obj149.isGraphObjectVisual = True

   if(hasattr(self.obj149, '_setHierarchicalLink')):
     self.obj149._setHierarchicalLink(False)

   self.obj149.GGLabel.setValue(5)
   self.obj149.graphClass_= graph_requir
   if self.genGraphics:
      new_obj = graph_requir(282.5,152.5,self.obj149)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj149.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj149)
   self.obj149.postAction( cobj0.RHS.CREATE )

   self.obj144.out_connections_.append(self.obj147)
   self.obj147.in_connections_.append(self.obj144)
   self.obj144.graphObject_.pendingConnections.append((self.obj144.graphObject_.tag, self.obj147.graphObject_.tag, [117.0, 102.0, 163.0, 150.5], 2, 0))
   self.obj144.out_connections_.append(self.obj148)
   self.obj148.in_connections_.append(self.obj144)
   self.obj144.graphObject_.pendingConnections.append((self.obj144.graphObject_.tag, self.obj148.graphObject_.tag, [117.0, 102.0, 175.0, 84.5, 233.5, 74.0], 2, True))
   self.obj146.out_connections_.append(self.obj149)
   self.obj149.in_connections_.append(self.obj146)
   self.obj146.graphObject_.pendingConnections.append((self.obj146.graphObject_.tag, self.obj149.graphObject_.tag, [351.0, 105.0, 282.5, 152.5], 2, 0))
   self.obj147.out_connections_.append(self.obj145)
   self.obj145.in_connections_.append(self.obj147)
   self.obj147.graphObject_.pendingConnections.append((self.obj147.graphObject_.tag, self.obj145.graphObject_.tag, [231.0, 203.0, 163.0, 150.5], 2, 0))
   self.obj148.out_connections_.append(self.obj146)
   self.obj146.in_connections_.append(self.obj148)
   self.obj148.graphObject_.pendingConnections.append((self.obj148.graphObject_.tag, self.obj146.graphObject_.tag, [351.0, 60.0, 292.0, 63.5, 233.5, 74.0], 2, True))
   self.obj149.out_connections_.append(self.obj145)
   self.obj145.in_connections_.append(self.obj149)
   self.obj149.graphObject_.pendingConnections.append((self.obj149.graphObject_.tag, self.obj145.graphObject_.tag, [231.0, 203.0, 282.5, 152.5], 2, 0))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'agent = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\n\nrole = self.getMatched(graphID, self.LHS.nodeWithLabel(3))\nreturn not ( hasattr(agent, role.name.getValue()) and hasattr(role, agent.name.getValue() ) )\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'agent = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) )\n\nc1 = self.getMatched ( graphID , self.LHS.nodeWithLabel(2) )\nrole = self.getMatched ( graphID , self.LHS.nodeWithLabel(3) )\nsetattr(agent ,role.name.getValue(),True )\nsetattr(role ,agent.name.getValue(),True )\n\nsetattr( c1 ,  agent.name.getValue() , True )\nsetattr( c1 ,  role.name.getValue() , True )\n\nprint \'connCt (\'+agent.name.getValue()+\',\'+role.name.getValue()+\')\'\n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('linkAgent2Role2', 20)
   cobj0.Order=ATOM3Integer(2)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

   from CapableOf import *
   from Goal import *
   from ASG_omacss import *
   from Agent import *
   from Capabilitie import *
   from Role import *
   from requir import *
   from achieve import *
   from posses import *

   cobj0.LHS = ASG_omacss(self)

   self.obj154=Agent(self)
   self.obj154.preAction( cobj0.LHS.CREATE )
   self.obj154.isGraphObjectVisual = True

   if(hasattr(self.obj154, '_setHierarchicalLink')):
     self.obj154._setHierarchicalLink(False)

   # price
   self.obj154.price.setValue(0)

   # name
   self.obj154.name.setValue('')
   self.obj154.name.setNone()

   self.obj154.GGLabel.setValue(1)
   self.obj154.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(60.0,20.0,self.obj154)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj154.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj154)
   self.obj154.postAction( cobj0.LHS.CREATE )

   self.obj155=Capabilitie(self)
   self.obj155.preAction( cobj0.LHS.CREATE )
   self.obj155.isGraphObjectVisual = True

   if(hasattr(self.obj155, '_setHierarchicalLink')):
     self.obj155._setHierarchicalLink(False)

   # name
   self.obj155.name.setValue('')
   self.obj155.name.setNone()

   self.obj155.GGLabel.setValue(2)
   self.obj155.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(80.0,160.0,self.obj155)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj155.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj155)
   self.obj155.postAction( cobj0.LHS.CREATE )

   self.obj156=Capabilitie(self)
   self.obj156.preAction( cobj0.LHS.CREATE )
   self.obj156.isGraphObjectVisual = True

   if(hasattr(self.obj156, '_setHierarchicalLink')):
     self.obj156._setHierarchicalLink(False)

   # name
   self.obj156.name.setValue('')
   self.obj156.name.setNone()

   self.obj156.GGLabel.setValue(3)
   self.obj156.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(260.0,20.0,self.obj156)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj156.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj156)
   self.obj156.postAction( cobj0.LHS.CREATE )

   self.obj157=Role(self)
   self.obj157.preAction( cobj0.LHS.CREATE )
   self.obj157.isGraphObjectVisual = True

   if(hasattr(self.obj157, '_setHierarchicalLink')):
     self.obj157._setHierarchicalLink(False)

   # name
   self.obj157.name.setValue('')
   self.obj157.name.setNone()

   self.obj157.GGLabel.setValue(4)
   self.obj157.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(280.0,140.0,self.obj157)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj157.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj157)
   self.obj157.postAction( cobj0.LHS.CREATE )

   self.obj158=posses(self)
   self.obj158.preAction( cobj0.LHS.CREATE )
   self.obj158.isGraphObjectVisual = True

   if(hasattr(self.obj158, '_setHierarchicalLink')):
     self.obj158._setHierarchicalLink(False)

   # rate
   self.obj158.rate.setNone()

   self.obj158.GGLabel.setValue(5)
   self.obj158.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(183.0,70.5,self.obj158)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj158.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj158)
   self.obj158.postAction( cobj0.LHS.CREATE )

   self.obj159=posses(self)
   self.obj159.preAction( cobj0.LHS.CREATE )
   self.obj159.isGraphObjectVisual = True

   if(hasattr(self.obj159, '_setHierarchicalLink')):
     self.obj159._setHierarchicalLink(False)

   # rate
   self.obj159.rate.setNone()

   self.obj159.GGLabel.setValue(6)
   self.obj159.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(93.0,120.5,self.obj159)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj159.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj159)
   self.obj159.postAction( cobj0.LHS.CREATE )

   self.obj160=CapableOf(self)
   self.obj160.preAction( cobj0.LHS.CREATE )
   self.obj160.isGraphObjectVisual = True

   if(hasattr(self.obj160, '_setHierarchicalLink')):
     self.obj160._setHierarchicalLink(False)

   self.obj160.GGLabel.setValue(9)
   self.obj160.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(194.5,111.5,self.obj160)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj160.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj160)
   self.obj160.postAction( cobj0.LHS.CREATE )

   self.obj161=requir(self)
   self.obj161.preAction( cobj0.LHS.CREATE )
   self.obj161.isGraphObjectVisual = True

   if(hasattr(self.obj161, '_setHierarchicalLink')):
     self.obj161._setHierarchicalLink(False)

   self.obj161.GGLabel.setValue(7)
   self.obj161.graphClass_= graph_requir
   if self.genGraphics:
      new_obj = graph_requir(202.5,192.5,self.obj161)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj161.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj161)
   self.obj161.postAction( cobj0.LHS.CREATE )

   self.obj162=requir(self)
   self.obj162.preAction( cobj0.LHS.CREATE )
   self.obj162.isGraphObjectVisual = True

   if(hasattr(self.obj162, '_setHierarchicalLink')):
     self.obj162._setHierarchicalLink(False)

   self.obj162.GGLabel.setValue(8)
   self.obj162.graphClass_= graph_requir
   if self.genGraphics:
      new_obj = graph_requir(292.5,100.0,self.obj162)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj162.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj162)
   self.obj162.postAction( cobj0.LHS.CREATE )

   self.obj154.out_connections_.append(self.obj158)
   self.obj158.in_connections_.append(self.obj154)
   self.obj154.graphObject_.pendingConnections.append((self.obj154.graphObject_.tag, self.obj158.graphObject_.tag, [85.0, 82.0, 183.0, 70.5], 0, True))
   self.obj154.out_connections_.append(self.obj159)
   self.obj159.in_connections_.append(self.obj154)
   self.obj154.graphObject_.pendingConnections.append((self.obj154.graphObject_.tag, self.obj159.graphObject_.tag, [85.0, 82.0, 93.0, 120.5], 0, True))
   self.obj154.out_connections_.append(self.obj160)
   self.obj160.in_connections_.append(self.obj154)
   self.obj154.graphObject_.pendingConnections.append((self.obj154.graphObject_.tag, self.obj160.graphObject_.tag, [85.0, 82.0, 194.5, 111.5], 0, True))
   self.obj157.out_connections_.append(self.obj161)
   self.obj161.in_connections_.append(self.obj157)
   self.obj157.graphObject_.pendingConnections.append((self.obj157.graphObject_.tag, self.obj161.graphObject_.tag, [304.0, 186.0, 202.5, 192.5], 0, True))
   self.obj157.out_connections_.append(self.obj162)
   self.obj162.in_connections_.append(self.obj157)
   self.obj157.graphObject_.pendingConnections.append((self.obj157.graphObject_.tag, self.obj162.graphObject_.tag, [304.0, 141.0, 292.5, 100.0], 0, True))
   self.obj158.out_connections_.append(self.obj156)
   self.obj156.in_connections_.append(self.obj158)
   self.obj158.graphObject_.pendingConnections.append((self.obj158.graphObject_.tag, self.obj156.graphObject_.tag, [281.0, 59.0, 183.0, 70.5], 0, True))
   self.obj159.out_connections_.append(self.obj155)
   self.obj155.in_connections_.append(self.obj159)
   self.obj159.graphObject_.pendingConnections.append((self.obj159.graphObject_.tag, self.obj155.graphObject_.tag, [101.0, 159.0, 93.0, 120.5], 0, True))
   self.obj160.out_connections_.append(self.obj157)
   self.obj157.in_connections_.append(self.obj160)
   self.obj160.graphObject_.pendingConnections.append((self.obj160.graphObject_.tag, self.obj157.graphObject_.tag, [311.0, 140.0, 194.5, 111.5], 2, 0))
   self.obj161.out_connections_.append(self.obj155)
   self.obj155.in_connections_.append(self.obj161)
   self.obj161.graphObject_.pendingConnections.append((self.obj161.graphObject_.tag, self.obj155.graphObject_.tag, [101.0, 199.0, 202.5, 192.5], 0, True))
   self.obj162.out_connections_.append(self.obj156)
   self.obj156.in_connections_.append(self.obj162)
   self.obj162.graphObject_.pendingConnections.append((self.obj162.graphObject_.tag, self.obj156.graphObject_.tag, [281.0, 59.0, 292.5, 100.0], 0, True))

   cobj0.RHS = ASG_omacss(self)

   self.obj164=Agent(self)
   self.obj164.preAction( cobj0.RHS.CREATE )
   self.obj164.isGraphObjectVisual = True

   if(hasattr(self.obj164, '_setHierarchicalLink')):
     self.obj164._setHierarchicalLink(False)

   # price
   self.obj164.price.setValue(0)

   # name
   self.obj164.name.setValue('')
   self.obj164.name.setNone()

   self.obj164.GGLabel.setValue(1)
   self.obj164.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(60.0,20.0,self.obj164)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj164.graphObject_ = new_obj
   self.obj1640= AttrCalc()
   self.obj1640.Copy=ATOM3Boolean()
   self.obj1640.Copy.setValue(('Copy from LHS', 1))
   self.obj1640.Copy.config = 0
   self.obj1640.Specify=ATOM3Constraint()
   self.obj1640.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj164.GGset2Any['price']= self.obj1640
   self.obj1641= AttrCalc()
   self.obj1641.Copy=ATOM3Boolean()
   self.obj1641.Copy.setValue(('Copy from LHS', 1))
   self.obj1641.Copy.config = 0
   self.obj1641.Specify=ATOM3Constraint()
   self.obj1641.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj164.GGset2Any['name']= self.obj1641

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj164)
   self.obj164.postAction( cobj0.RHS.CREATE )

   self.obj165=Capabilitie(self)
   self.obj165.preAction( cobj0.RHS.CREATE )
   self.obj165.isGraphObjectVisual = True

   if(hasattr(self.obj165, '_setHierarchicalLink')):
     self.obj165._setHierarchicalLink(False)

   # name
   self.obj165.name.setValue('')
   self.obj165.name.setNone()

   self.obj165.GGLabel.setValue(2)
   self.obj165.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(80.0,160.0,self.obj165)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj165.graphObject_ = new_obj
   self.obj1650= AttrCalc()
   self.obj1650.Copy=ATOM3Boolean()
   self.obj1650.Copy.setValue(('Copy from LHS', 1))
   self.obj1650.Copy.config = 0
   self.obj1650.Specify=ATOM3Constraint()
   self.obj1650.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj165.GGset2Any['name']= self.obj1650

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj165)
   self.obj165.postAction( cobj0.RHS.CREATE )

   self.obj166=Capabilitie(self)
   self.obj166.preAction( cobj0.RHS.CREATE )
   self.obj166.isGraphObjectVisual = True

   if(hasattr(self.obj166, '_setHierarchicalLink')):
     self.obj166._setHierarchicalLink(False)

   # name
   self.obj166.name.setValue('')
   self.obj166.name.setNone()

   self.obj166.GGLabel.setValue(3)
   self.obj166.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(260.0,20.0,self.obj166)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj166.graphObject_ = new_obj
   self.obj1660= AttrCalc()
   self.obj1660.Copy=ATOM3Boolean()
   self.obj1660.Copy.setValue(('Copy from LHS', 1))
   self.obj1660.Copy.config = 0
   self.obj1660.Specify=ATOM3Constraint()
   self.obj1660.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj166.GGset2Any['name']= self.obj1660

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj166)
   self.obj166.postAction( cobj0.RHS.CREATE )

   self.obj167=Role(self)
   self.obj167.preAction( cobj0.RHS.CREATE )
   self.obj167.isGraphObjectVisual = True

   if(hasattr(self.obj167, '_setHierarchicalLink')):
     self.obj167._setHierarchicalLink(False)

   # name
   self.obj167.name.setValue('')
   self.obj167.name.setNone()

   self.obj167.GGLabel.setValue(4)
   self.obj167.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(280.0,140.0,self.obj167)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj167.graphObject_ = new_obj
   self.obj1670= AttrCalc()
   self.obj1670.Copy=ATOM3Boolean()
   self.obj1670.Copy.setValue(('Copy from LHS', 1))
   self.obj1670.Copy.config = 0
   self.obj1670.Specify=ATOM3Constraint()
   self.obj1670.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj167.GGset2Any['name']= self.obj1670

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj167)
   self.obj167.postAction( cobj0.RHS.CREATE )

   self.obj168=posses(self)
   self.obj168.preAction( cobj0.RHS.CREATE )
   self.obj168.isGraphObjectVisual = True

   if(hasattr(self.obj168, '_setHierarchicalLink')):
     self.obj168._setHierarchicalLink(False)

   # rate
   self.obj168.rate.setValue(0.0)

   self.obj168.GGLabel.setValue(5)
   self.obj168.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(183.0,70.5,self.obj168)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj168.graphObject_ = new_obj
   self.obj1680= AttrCalc()
   self.obj1680.Copy=ATOM3Boolean()
   self.obj1680.Copy.setValue(('Copy from LHS', 1))
   self.obj1680.Copy.config = 0
   self.obj1680.Specify=ATOM3Constraint()
   self.obj1680.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj168.GGset2Any['rate']= self.obj1680

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj168)
   self.obj168.postAction( cobj0.RHS.CREATE )

   self.obj169=posses(self)
   self.obj169.preAction( cobj0.RHS.CREATE )
   self.obj169.isGraphObjectVisual = True

   if(hasattr(self.obj169, '_setHierarchicalLink')):
     self.obj169._setHierarchicalLink(False)

   # rate
   self.obj169.rate.setValue(0.0)

   self.obj169.GGLabel.setValue(6)
   self.obj169.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(93.0,120.5,self.obj169)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj169.graphObject_ = new_obj
   self.obj1690= AttrCalc()
   self.obj1690.Copy=ATOM3Boolean()
   self.obj1690.Copy.setValue(('Copy from LHS', 1))
   self.obj1690.Copy.config = 0
   self.obj1690.Specify=ATOM3Constraint()
   self.obj1690.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj169.GGset2Any['rate']= self.obj1690

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj169)
   self.obj169.postAction( cobj0.RHS.CREATE )

   self.obj170=CapableOf(self)
   self.obj170.preAction( cobj0.RHS.CREATE )
   self.obj170.isGraphObjectVisual = True

   if(hasattr(self.obj170, '_setHierarchicalLink')):
     self.obj170._setHierarchicalLink(False)

   self.obj170.GGLabel.setValue(9)
   self.obj170.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(194.5,111.5,self.obj170)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj170.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj170)
   self.obj170.postAction( cobj0.RHS.CREATE )

   self.obj171=requir(self)
   self.obj171.preAction( cobj0.RHS.CREATE )
   self.obj171.isGraphObjectVisual = True

   if(hasattr(self.obj171, '_setHierarchicalLink')):
     self.obj171._setHierarchicalLink(False)

   self.obj171.GGLabel.setValue(7)
   self.obj171.graphClass_= graph_requir
   if self.genGraphics:
      new_obj = graph_requir(202.5,192.5,self.obj171)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj171.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj171)
   self.obj171.postAction( cobj0.RHS.CREATE )

   self.obj172=requir(self)
   self.obj172.preAction( cobj0.RHS.CREATE )
   self.obj172.isGraphObjectVisual = True

   if(hasattr(self.obj172, '_setHierarchicalLink')):
     self.obj172._setHierarchicalLink(False)

   self.obj172.GGLabel.setValue(8)
   self.obj172.graphClass_= graph_requir
   if self.genGraphics:
      new_obj = graph_requir(292.5,100.0,self.obj172)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj172.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj172)
   self.obj172.postAction( cobj0.RHS.CREATE )

   self.obj164.out_connections_.append(self.obj168)
   self.obj168.in_connections_.append(self.obj164)
   self.obj164.graphObject_.pendingConnections.append((self.obj164.graphObject_.tag, self.obj168.graphObject_.tag, [97.0, 82.0, 183.0, 70.5], 2, 0))
   self.obj164.out_connections_.append(self.obj169)
   self.obj169.in_connections_.append(self.obj164)
   self.obj164.graphObject_.pendingConnections.append((self.obj164.graphObject_.tag, self.obj169.graphObject_.tag, [97.0, 82.0, 93.0, 120.5], 2, 0))
   self.obj164.out_connections_.append(self.obj170)
   self.obj170.in_connections_.append(self.obj164)
   self.obj164.graphObject_.pendingConnections.append((self.obj164.graphObject_.tag, self.obj170.graphObject_.tag, [97.0, 82.0, 194.5, 111.5], 2, 0))
   self.obj167.out_connections_.append(self.obj171)
   self.obj171.in_connections_.append(self.obj167)
   self.obj167.graphObject_.pendingConnections.append((self.obj167.graphObject_.tag, self.obj171.graphObject_.tag, [311.0, 185.0, 202.5, 192.5], 2, 0))
   self.obj167.out_connections_.append(self.obj172)
   self.obj172.in_connections_.append(self.obj167)
   self.obj167.graphObject_.pendingConnections.append((self.obj167.graphObject_.tag, self.obj172.graphObject_.tag, [311.0, 140.0, 292.5, 100.0], 2, 0))
   self.obj168.out_connections_.append(self.obj166)
   self.obj166.in_connections_.append(self.obj168)
   self.obj168.graphObject_.pendingConnections.append((self.obj168.graphObject_.tag, self.obj166.graphObject_.tag, [291.0, 63.0, 183.0, 70.5], 2, 0))
   self.obj169.out_connections_.append(self.obj165)
   self.obj165.in_connections_.append(self.obj169)
   self.obj169.graphObject_.pendingConnections.append((self.obj169.graphObject_.tag, self.obj165.graphObject_.tag, [111.0, 163.0, 93.0, 120.5], 2, 0))
   self.obj170.out_connections_.append(self.obj167)
   self.obj167.in_connections_.append(self.obj170)
   self.obj170.graphObject_.pendingConnections.append((self.obj170.graphObject_.tag, self.obj167.graphObject_.tag, [311.0, 140.0, 194.5, 111.5], 2, 0))
   self.obj171.out_connections_.append(self.obj165)
   self.obj165.in_connections_.append(self.obj171)
   self.obj171.graphObject_.pendingConnections.append((self.obj171.graphObject_.tag, self.obj165.graphObject_.tag, [111.0, 203.0, 202.5, 192.5], 2, 0))
   self.obj172.out_connections_.append(self.obj166)
   self.obj166.in_connections_.append(self.obj172)
   self.obj172.graphObject_.pendingConnections.append((self.obj172.graphObject_.tag, self.obj166.graphObject_.tag, [291.0, 63.0, 292.5, 100.0], 2, 0))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\nagent = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nc1 = self.getMatched(graphID, self.LHS.nodeWithLabel(2))\nc2 = self.getMatched(graphID, self.LHS.nodeWithLabel(3))\nrole = self.getMatched(graphID, self.LHS.nodeWithLabel(4))\n\nreturn not ( hasattr(c1, agent.name.getValue() ) and \nhasattr(c1, role.name.getValue() ) and\nhasattr(c2, agent.name.getValue() ) and  hasattr(c2,  role.name.getValue()  ) )\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'agent = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nc1 = self.getMatched(graphID, self.LHS.nodeWithLabel(2))\nc2 = self.getMatched(graphID, self.LHS.nodeWithLabel(3))\nrole = self.getMatched(graphID, self.LHS.nodeWithLabel(4))\n\nsetattr( c1 ,  agent.name.getValue() , True )\nsetattr( c1 ,  role.name.getValue() , True )\n\nsetattr( c2 ,  agent.name.getValue() , True )\nsetattr( c2 ,  role.name.getValue() , True )\nprint\' Mark :(\'+agent.name.getValue()+\',\'+c1.name.getValue()+\',\'+c2.name.getValue()+\',\'+role.name.getValue()+\')\'\n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('linkAgent2Role3', 20)
   cobj0.Order=ATOM3Integer(3)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

   from CapableOf import *
   from Goal import *
   from ASG_omacss import *
   from Agent import *
   from Capabilitie import *
   from Role import *
   from requir import *
   from achieve import *
   from posses import *

   cobj0.LHS = ASG_omacss(self)

   self.obj177=Agent(self)
   self.obj177.preAction( cobj0.LHS.CREATE )
   self.obj177.isGraphObjectVisual = True

   if(hasattr(self.obj177, '_setHierarchicalLink')):
     self.obj177._setHierarchicalLink(False)

   # price
   self.obj177.price.setValue(0)

   # name
   self.obj177.name.setValue('')
   self.obj177.name.setNone()

   self.obj177.GGLabel.setValue(1)
   self.obj177.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(40.0,40.0,self.obj177)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj177.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj177)
   self.obj177.postAction( cobj0.LHS.CREATE )

   self.obj178=Capabilitie(self)
   self.obj178.preAction( cobj0.LHS.CREATE )
   self.obj178.isGraphObjectVisual = True

   if(hasattr(self.obj178, '_setHierarchicalLink')):
     self.obj178._setHierarchicalLink(False)

   # name
   self.obj178.name.setValue('')
   self.obj178.name.setNone()

   self.obj178.GGLabel.setValue(3)
   self.obj178.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(300.0,20.0,self.obj178)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj178.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj178)
   self.obj178.postAction( cobj0.LHS.CREATE )

   self.obj179=Capabilitie(self)
   self.obj179.preAction( cobj0.LHS.CREATE )
   self.obj179.isGraphObjectVisual = True

   if(hasattr(self.obj179, '_setHierarchicalLink')):
     self.obj179._setHierarchicalLink(False)

   # name
   self.obj179.name.setValue('')
   self.obj179.name.setNone()

   self.obj179.GGLabel.setValue(4)
   self.obj179.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(100.0,160.0,self.obj179)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj179.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj179)
   self.obj179.postAction( cobj0.LHS.CREATE )

   self.obj180=Role(self)
   self.obj180.preAction( cobj0.LHS.CREATE )
   self.obj180.isGraphObjectVisual = True

   if(hasattr(self.obj180, '_setHierarchicalLink')):
     self.obj180._setHierarchicalLink(False)

   # name
   self.obj180.name.setValue('')
   self.obj180.name.setNone()

   self.obj180.GGLabel.setValue(2)
   self.obj180.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(300.0,120.0,self.obj180)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj180.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj180)
   self.obj180.postAction( cobj0.LHS.CREATE )

   self.obj181=posses(self)
   self.obj181.preAction( cobj0.LHS.CREATE )
   self.obj181.isGraphObjectVisual = True

   if(hasattr(self.obj181, '_setHierarchicalLink')):
     self.obj181._setHierarchicalLink(False)

   # rate
   self.obj181.rate.setNone()

   self.obj181.GGLabel.setValue(5)
   self.obj181.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(93.0,130.5,self.obj181)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj181.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj181)
   self.obj181.postAction( cobj0.LHS.CREATE )

   self.obj182=CapableOf(self)
   self.obj182.preAction( cobj0.LHS.CREATE )
   self.obj182.isGraphObjectVisual = True

   if(hasattr(self.obj182, '_setHierarchicalLink')):
     self.obj182._setHierarchicalLink(False)

   self.obj182.GGLabel.setValue(6)
   self.obj182.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(194.5,111.5,self.obj182)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj182.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj182)
   self.obj182.postAction( cobj0.LHS.CREATE )

   self.obj183=requir(self)
   self.obj183.preAction( cobj0.LHS.CREATE )
   self.obj183.isGraphObjectVisual = True

   if(hasattr(self.obj183, '_setHierarchicalLink')):
     self.obj183._setHierarchicalLink(False)

   self.obj183.GGLabel.setValue(7)
   self.obj183.graphClass_= graph_requir
   if self.genGraphics:
      new_obj = graph_requir(222.5,162.5,self.obj183)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj183.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj183)
   self.obj183.postAction( cobj0.LHS.CREATE )

   self.obj184=requir(self)
   self.obj184.preAction( cobj0.LHS.CREATE )
   self.obj184.isGraphObjectVisual = True

   if(hasattr(self.obj184, '_setHierarchicalLink')):
     self.obj184._setHierarchicalLink(False)

   self.obj184.GGLabel.setValue(8)
   self.obj184.graphClass_= graph_requir
   if self.genGraphics:
      new_obj = graph_requir(322.5,90.0,self.obj184)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj184.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj184)
   self.obj184.postAction( cobj0.LHS.CREATE )

   self.obj177.out_connections_.append(self.obj181)
   self.obj181.in_connections_.append(self.obj177)
   self.obj177.graphObject_.pendingConnections.append((self.obj177.graphObject_.tag, self.obj181.graphObject_.tag, [77.0, 102.0, 93.0, 130.5], 2, 0))
   self.obj177.out_connections_.append(self.obj182)
   self.obj182.in_connections_.append(self.obj177)
   self.obj177.graphObject_.pendingConnections.append((self.obj177.graphObject_.tag, self.obj182.graphObject_.tag, [65.0, 102.0, 194.5, 111.5], 0, True))
   self.obj180.out_connections_.append(self.obj183)
   self.obj183.in_connections_.append(self.obj180)
   self.obj180.graphObject_.pendingConnections.append((self.obj180.graphObject_.tag, self.obj183.graphObject_.tag, [324.0, 166.0, 222.5, 162.5], 0, True))
   self.obj180.out_connections_.append(self.obj184)
   self.obj184.in_connections_.append(self.obj180)
   self.obj180.graphObject_.pendingConnections.append((self.obj180.graphObject_.tag, self.obj184.graphObject_.tag, [324.0, 121.0, 322.5, 90.0], 0, True))
   self.obj181.out_connections_.append(self.obj179)
   self.obj179.in_connections_.append(self.obj181)
   self.obj181.graphObject_.pendingConnections.append((self.obj181.graphObject_.tag, self.obj179.graphObject_.tag, [121.0, 159.0, 93.0, 130.5], 0, True))
   self.obj182.out_connections_.append(self.obj180)
   self.obj180.in_connections_.append(self.obj182)
   self.obj182.graphObject_.pendingConnections.append((self.obj182.graphObject_.tag, self.obj180.graphObject_.tag, [331.0, 120.0, 194.5, 111.5], 2, 0))
   self.obj183.out_connections_.append(self.obj179)
   self.obj179.in_connections_.append(self.obj183)
   self.obj183.graphObject_.pendingConnections.append((self.obj183.graphObject_.tag, self.obj179.graphObject_.tag, [121.0, 159.0, 222.5, 162.5], 0, True))
   self.obj184.out_connections_.append(self.obj178)
   self.obj178.in_connections_.append(self.obj184)
   self.obj184.graphObject_.pendingConnections.append((self.obj184.graphObject_.tag, self.obj178.graphObject_.tag, [321.0, 59.0, 322.5, 90.0], 0, True))

   cobj0.RHS = ASG_omacss(self)

   self.obj186=Agent(self)
   self.obj186.preAction( cobj0.RHS.CREATE )
   self.obj186.isGraphObjectVisual = True

   if(hasattr(self.obj186, '_setHierarchicalLink')):
     self.obj186._setHierarchicalLink(False)

   # price
   self.obj186.price.setValue(0)

   # name
   self.obj186.name.setValue('')
   self.obj186.name.setNone()

   self.obj186.GGLabel.setValue(1)
   self.obj186.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(40.0,40.0,self.obj186)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj186.graphObject_ = new_obj
   self.obj1860= AttrCalc()
   self.obj1860.Copy=ATOM3Boolean()
   self.obj1860.Copy.setValue(('Copy from LHS', 1))
   self.obj1860.Copy.config = 0
   self.obj1860.Specify=ATOM3Constraint()
   self.obj1860.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj186.GGset2Any['price']= self.obj1860
   self.obj1861= AttrCalc()
   self.obj1861.Copy=ATOM3Boolean()
   self.obj1861.Copy.setValue(('Copy from LHS', 1))
   self.obj1861.Copy.config = 0
   self.obj1861.Specify=ATOM3Constraint()
   self.obj1861.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj186.GGset2Any['name']= self.obj1861

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj186)
   self.obj186.postAction( cobj0.RHS.CREATE )

   self.obj187=Capabilitie(self)
   self.obj187.preAction( cobj0.RHS.CREATE )
   self.obj187.isGraphObjectVisual = True

   if(hasattr(self.obj187, '_setHierarchicalLink')):
     self.obj187._setHierarchicalLink(False)

   # name
   self.obj187.name.setValue('')
   self.obj187.name.setNone()

   self.obj187.GGLabel.setValue(3)
   self.obj187.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(300.0,20.0,self.obj187)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj187.graphObject_ = new_obj
   self.obj1870= AttrCalc()
   self.obj1870.Copy=ATOM3Boolean()
   self.obj1870.Copy.setValue(('Copy from LHS', 1))
   self.obj1870.Copy.config = 0
   self.obj1870.Specify=ATOM3Constraint()
   self.obj1870.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj187.GGset2Any['name']= self.obj1870

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj187)
   self.obj187.postAction( cobj0.RHS.CREATE )

   self.obj188=Capabilitie(self)
   self.obj188.preAction( cobj0.RHS.CREATE )
   self.obj188.isGraphObjectVisual = True

   if(hasattr(self.obj188, '_setHierarchicalLink')):
     self.obj188._setHierarchicalLink(False)

   # name
   self.obj188.name.setValue('')
   self.obj188.name.setNone()

   self.obj188.GGLabel.setValue(4)
   self.obj188.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(100.0,160.0,self.obj188)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj188.graphObject_ = new_obj
   self.obj1880= AttrCalc()
   self.obj1880.Copy=ATOM3Boolean()
   self.obj1880.Copy.setValue(('Copy from LHS', 1))
   self.obj1880.Copy.config = 0
   self.obj1880.Specify=ATOM3Constraint()
   self.obj1880.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj188.GGset2Any['name']= self.obj1880

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj188)
   self.obj188.postAction( cobj0.RHS.CREATE )

   self.obj189=Role(self)
   self.obj189.preAction( cobj0.RHS.CREATE )
   self.obj189.isGraphObjectVisual = True

   if(hasattr(self.obj189, '_setHierarchicalLink')):
     self.obj189._setHierarchicalLink(False)

   # name
   self.obj189.name.setValue('')
   self.obj189.name.setNone()

   self.obj189.GGLabel.setValue(2)
   self.obj189.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(300.0,120.0,self.obj189)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj189.graphObject_ = new_obj
   self.obj1890= AttrCalc()
   self.obj1890.Copy=ATOM3Boolean()
   self.obj1890.Copy.setValue(('Copy from LHS', 1))
   self.obj1890.Copy.config = 0
   self.obj1890.Specify=ATOM3Constraint()
   self.obj1890.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj189.GGset2Any['name']= self.obj1890

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj189)
   self.obj189.postAction( cobj0.RHS.CREATE )

   self.obj190=posses(self)
   self.obj190.preAction( cobj0.RHS.CREATE )
   self.obj190.isGraphObjectVisual = True

   if(hasattr(self.obj190, '_setHierarchicalLink')):
     self.obj190._setHierarchicalLink(False)

   # rate
   self.obj190.rate.setValue(0.0)

   self.obj190.GGLabel.setValue(5)
   self.obj190.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(93.0,130.5,self.obj190)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj190.graphObject_ = new_obj
   self.obj1900= AttrCalc()
   self.obj1900.Copy=ATOM3Boolean()
   self.obj1900.Copy.setValue(('Copy from LHS', 1))
   self.obj1900.Copy.config = 0
   self.obj1900.Specify=ATOM3Constraint()
   self.obj1900.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj190.GGset2Any['rate']= self.obj1900

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj190)
   self.obj190.postAction( cobj0.RHS.CREATE )

   self.obj191=requir(self)
   self.obj191.preAction( cobj0.RHS.CREATE )
   self.obj191.isGraphObjectVisual = True

   if(hasattr(self.obj191, '_setHierarchicalLink')):
     self.obj191._setHierarchicalLink(False)

   self.obj191.GGLabel.setValue(7)
   self.obj191.graphClass_= graph_requir
   if self.genGraphics:
      new_obj = graph_requir(222.5,162.5,self.obj191)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj191.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj191)
   self.obj191.postAction( cobj0.RHS.CREATE )

   self.obj192=requir(self)
   self.obj192.preAction( cobj0.RHS.CREATE )
   self.obj192.isGraphObjectVisual = True

   if(hasattr(self.obj192, '_setHierarchicalLink')):
     self.obj192._setHierarchicalLink(False)

   self.obj192.GGLabel.setValue(8)
   self.obj192.graphClass_= graph_requir
   if self.genGraphics:
      new_obj = graph_requir(322.5,90.0,self.obj192)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj192.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj192)
   self.obj192.postAction( cobj0.RHS.CREATE )

   self.obj186.out_connections_.append(self.obj190)
   self.obj190.in_connections_.append(self.obj186)
   self.obj186.graphObject_.pendingConnections.append((self.obj186.graphObject_.tag, self.obj190.graphObject_.tag, [77.0, 102.0, 93.0, 130.5], 2, 0))
   self.obj189.out_connections_.append(self.obj191)
   self.obj191.in_connections_.append(self.obj189)
   self.obj189.graphObject_.pendingConnections.append((self.obj189.graphObject_.tag, self.obj191.graphObject_.tag, [331.0, 165.0, 222.5, 162.5], 2, 0))
   self.obj189.out_connections_.append(self.obj192)
   self.obj192.in_connections_.append(self.obj189)
   self.obj189.graphObject_.pendingConnections.append((self.obj189.graphObject_.tag, self.obj192.graphObject_.tag, [331.0, 120.0, 322.5, 90.0], 2, 0))
   self.obj190.out_connections_.append(self.obj188)
   self.obj188.in_connections_.append(self.obj190)
   self.obj190.graphObject_.pendingConnections.append((self.obj190.graphObject_.tag, self.obj188.graphObject_.tag, [131.0, 163.0, 93.0, 130.5], 2, 0))
   self.obj191.out_connections_.append(self.obj188)
   self.obj188.in_connections_.append(self.obj191)
   self.obj191.graphObject_.pendingConnections.append((self.obj191.graphObject_.tag, self.obj188.graphObject_.tag, [131.0, 163.0, 222.5, 162.5], 2, 0))
   self.obj192.out_connections_.append(self.obj187)
   self.obj187.in_connections_.append(self.obj192)
   self.obj192.graphObject_.pendingConnections.append((self.obj192.graphObject_.tag, self.obj187.graphObject_.tag, [331.0, 63.0, 322.5, 90.0], 2, 0))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'agent = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nrole  = self.getMatched(graphID, self.LHS.nodeWithLabel(2))\nc1 = self.getMatched(graphID, self.LHS.nodeWithLabel(3))\nc2 = self.getMatched(graphID, self.LHS.nodeWithLabel(4))\n\nreturn not ( hasattr(c1,  agent.name.getValue() ) and \nhasattr(c1,  role.name.getValue() ) and\nhasattr(c2,  agent.name.getValue() ) and  hasattr(c2, role.name.getValue() ) )\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'agent = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nc1 = self.getMatched(graphID, self.LHS.nodeWithLabel(4))\nc2 = self.getMatched(graphID, self.LHS.nodeWithLabel(3))\nrole = self.getMatched(graphID, self.LHS.nodeWithLabel(2))\n\nsetattr( c1 ,  agent.name.getValue() , True )\nsetattr( c1 ,  role.name.getValue() , True )\n\nsetattr( c2 ,  agent.name.getValue() , True )\nsetattr( c2 ,  role.name.getValue() , True )\nprint\' Eli : (\'+agent.name.getValue()+\',\'+c1.name.getValue()+\',\'+c2.name.getValue()+\',\'+role.name.getValue()+\')\'\n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('TransformAGent2Raw', 20)
   cobj0.Order=ATOM3Integer(5)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

   from CapableOf import *
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
   from product import *
   from achieve import *
   from posses import *
   from GenericGraphEdge import *
   from ASG_GenericGraph import *
   from GenericGraphNode import *

   cobj0.LHS = ASG_omacss(self)
   cobj0.LHS.merge(ASG_pns2(self))

   self.obj198=Agent(self)
   self.obj198.preAction( cobj0.LHS.CREATE )
   self.obj198.isGraphObjectVisual = True

   if(hasattr(self.obj198, '_setHierarchicalLink')):
     self.obj198._setHierarchicalLink(False)

   # price
   self.obj198.price.setValue(0)

   # name
   self.obj198.name.setValue('')
   self.obj198.name.setNone()

   self.obj198.GGLabel.setValue(1)
   self.obj198.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(60.0,20.0,self.obj198)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj198.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj198)
   self.obj198.postAction( cobj0.LHS.CREATE )

   self.obj199=Role(self)
   self.obj199.preAction( cobj0.LHS.CREATE )
   self.obj199.isGraphObjectVisual = True

   if(hasattr(self.obj199, '_setHierarchicalLink')):
     self.obj199._setHierarchicalLink(False)

   # name
   self.obj199.name.setValue('')
   self.obj199.name.setNone()

   self.obj199.GGLabel.setValue(2)
   self.obj199.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(240.0,100.0,self.obj199)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj199.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj199)
   self.obj199.postAction( cobj0.LHS.CREATE )

   self.obj200=CapableOf(self)
   self.obj200.preAction( cobj0.LHS.CREATE )
   self.obj200.isGraphObjectVisual = True

   if(hasattr(self.obj200, '_setHierarchicalLink')):
     self.obj200._setHierarchicalLink(False)

   self.obj200.GGLabel.setValue(3)
   self.obj200.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(170.0,88.5,self.obj200)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj200.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj200)
   self.obj200.postAction( cobj0.LHS.CREATE )

   self.obj198.out_connections_.append(self.obj200)
   self.obj200.in_connections_.append(self.obj198)
   self.obj198.graphObject_.pendingConnections.append((self.obj198.graphObject_.tag, self.obj200.graphObject_.tag, [85.0, 82.0, 109.0, 127.0, 170.0, 88.5], 2, True))
   self.obj200.out_connections_.append(self.obj199)
   self.obj199.in_connections_.append(self.obj200)
   self.obj200.graphObject_.pendingConnections.append((self.obj200.graphObject_.tag, self.obj199.graphObject_.tag, [264.0, 101.0, 231.0, 50.0, 170.0, 88.5], 2, True))

   cobj0.RHS = ASG_omacss(self)
   cobj0.RHS.merge(ASG_pns2(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj204=Agent(self)
   self.obj204.preAction( cobj0.RHS.CREATE )
   self.obj204.isGraphObjectVisual = True

   if(hasattr(self.obj204, '_setHierarchicalLink')):
     self.obj204._setHierarchicalLink(False)

   # price
   self.obj204.price.setValue(0)

   # name
   self.obj204.name.setValue('')
   self.obj204.name.setNone()

   self.obj204.GGLabel.setValue(1)
   self.obj204.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(60.0,20.0,self.obj204)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj204.graphObject_ = new_obj
   self.obj2040= AttrCalc()
   self.obj2040.Copy=ATOM3Boolean()
   self.obj2040.Copy.setValue(('Copy from LHS', 1))
   self.obj2040.Copy.config = 0
   self.obj2040.Specify=ATOM3Constraint()
   self.obj2040.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj204.GGset2Any['price']= self.obj2040
   self.obj2041= AttrCalc()
   self.obj2041.Copy=ATOM3Boolean()
   self.obj2041.Copy.setValue(('Copy from LHS', 1))
   self.obj2041.Copy.config = 0
   self.obj2041.Specify=ATOM3Constraint()
   self.obj2041.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj204.GGset2Any['name']= self.obj2041

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj204)
   self.obj204.postAction( cobj0.RHS.CREATE )

   self.obj205=Role(self)
   self.obj205.preAction( cobj0.RHS.CREATE )
   self.obj205.isGraphObjectVisual = True

   if(hasattr(self.obj205, '_setHierarchicalLink')):
     self.obj205._setHierarchicalLink(False)

   # name
   self.obj205.name.setValue('')
   self.obj205.name.setNone()

   self.obj205.GGLabel.setValue(2)
   self.obj205.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(240.0,100.0,self.obj205)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj205.graphObject_ = new_obj
   self.obj2050= AttrCalc()
   self.obj2050.Copy=ATOM3Boolean()
   self.obj2050.Copy.setValue(('Copy from LHS', 1))
   self.obj2050.Copy.config = 0
   self.obj2050.Specify=ATOM3Constraint()
   self.obj2050.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj205.GGset2Any['name']= self.obj2050

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj205)
   self.obj205.postAction( cobj0.RHS.CREATE )

   self.obj206=CapableOf(self)
   self.obj206.preAction( cobj0.RHS.CREATE )
   self.obj206.isGraphObjectVisual = True

   if(hasattr(self.obj206, '_setHierarchicalLink')):
     self.obj206._setHierarchicalLink(False)

   self.obj206.GGLabel.setValue(3)
   self.obj206.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(170.0,88.5,self.obj206)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj206.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj206)
   self.obj206.postAction( cobj0.RHS.CREATE )

   self.obj207=rawMaterial(self)
   self.obj207.preAction( cobj0.RHS.CREATE )
   self.obj207.isGraphObjectVisual = True

   if(hasattr(self.obj207, '_setHierarchicalLink')):
     self.obj207._setHierarchicalLink(False)

   # Name
   self.obj207.Name.setValue('')
   self.obj207.Name.setNone()

   self.obj207.GGLabel.setValue(5)
   self.obj207.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(20.0,140.0,self.obj207)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj207.graphObject_ = new_obj
   self.obj2070= AttrCalc()
   self.obj2070.Copy=ATOM3Boolean()
   self.obj2070.Copy.setValue(('Copy from LHS', 0))
   self.obj2070.Copy.config = 0
   self.obj2070.Specify=ATOM3Constraint()
   self.obj2070.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()\n'))
   self.obj207.GGset2Any['Name']= self.obj2070

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj207)
   self.obj207.postAction( cobj0.RHS.CREATE )

   self.obj208=GenericGraphEdge(self)
   self.obj208.preAction( cobj0.RHS.CREATE )
   self.obj208.isGraphObjectVisual = True

   if(hasattr(self.obj208, '_setHierarchicalLink')):
     self.obj208._setHierarchicalLink(False)

   self.obj208.GGLabel.setValue(6)
   self.obj208.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(93.5,165.0,self.obj208)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj208.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj208)
   self.obj208.postAction( cobj0.RHS.CREATE )

   self.obj204.out_connections_.append(self.obj206)
   self.obj206.in_connections_.append(self.obj204)
   self.obj204.graphObject_.pendingConnections.append((self.obj204.graphObject_.tag, self.obj206.graphObject_.tag, [97.0, 82.0, 170.0, 88.5], 2, 0))
   self.obj204.out_connections_.append(self.obj208)
   self.obj208.in_connections_.append(self.obj204)
   self.obj204.graphObject_.pendingConnections.append((self.obj204.graphObject_.tag, self.obj208.graphObject_.tag, [97.0, 82.0, 67.0, 166.0, 93.5, 165.0], 2, True))
   self.obj206.out_connections_.append(self.obj205)
   self.obj205.in_connections_.append(self.obj206)
   self.obj206.graphObject_.pendingConnections.append((self.obj206.graphObject_.tag, self.obj205.graphObject_.tag, [271.0, 100.0, 170.0, 88.5], 2, 0))
   self.obj208.out_connections_.append(self.obj207)
   self.obj207.in_connections_.append(self.obj208)
   self.obj208.graphObject_.pendingConnections.append((self.obj208.graphObject_.tag, self.obj207.graphObject_.tag, [44.0, 193.0, 120.0, 164.0, 93.5, 165.0], 2, True))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nreturn not hasattr(node, "Agent2Raw")\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'node = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) )\nnode.Agent2Raw = True \n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('TransformLinkAR2OpUnit', 20)
   cobj0.Order=ATOM3Integer(7)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

   from CapableOf import *
   from Goal import *
   from ASG_omacss import *
   from Agent import *
   from Capabilitie import *
   from Role import *
   from requir import *
   from achieve import *
   from posses import *
   from GenericGraphEdge import *
   from intoProduct import *
   from operatingUnit import *
   from metarial import *
   from rawMaterial import *
   from fromMaterial import *
   from fromRaw import *
   from ASG_pns2 import *
   from intoMaterial import *
   from ASG_GenericGraph import *
   from product import *
   from GenericGraphNode import *

   cobj0.LHS = ASG_omacss(self)

   self.obj213=Agent(self)
   self.obj213.preAction( cobj0.LHS.CREATE )
   self.obj213.isGraphObjectVisual = True

   if(hasattr(self.obj213, '_setHierarchicalLink')):
     self.obj213._setHierarchicalLink(False)

   # price
   self.obj213.price.setNone()

   # name
   self.obj213.name.setValue('')
   self.obj213.name.setNone()

   self.obj213.GGLabel.setValue(1)
   self.obj213.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(60.0,60.0,self.obj213)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj213.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj213)
   self.obj213.postAction( cobj0.LHS.CREATE )

   self.obj214=Role(self)
   self.obj214.preAction( cobj0.LHS.CREATE )
   self.obj214.isGraphObjectVisual = True

   if(hasattr(self.obj214, '_setHierarchicalLink')):
     self.obj214._setHierarchicalLink(False)

   # name
   self.obj214.name.setValue('')
   self.obj214.name.setNone()

   self.obj214.GGLabel.setValue(2)
   self.obj214.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(320.0,140.0,self.obj214)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj214.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj214)
   self.obj214.postAction( cobj0.LHS.CREATE )

   self.obj215=CapableOf(self)
   self.obj215.preAction( cobj0.LHS.CREATE )
   self.obj215.isGraphObjectVisual = True

   if(hasattr(self.obj215, '_setHierarchicalLink')):
     self.obj215._setHierarchicalLink(False)

   self.obj215.GGLabel.setValue(3)
   self.obj215.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(207.0,130.0,self.obj215)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj215.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj215)
   self.obj215.postAction( cobj0.LHS.CREATE )

   self.obj213.out_connections_.append(self.obj215)
   self.obj215.in_connections_.append(self.obj213)
   self.obj213.graphObject_.pendingConnections.append((self.obj213.graphObject_.tag, self.obj215.graphObject_.tag, [85.0, 122.0, 117.0, 172.0, 207.0, 130.0], 2, True))
   self.obj215.out_connections_.append(self.obj214)
   self.obj214.in_connections_.append(self.obj215)
   self.obj215.graphObject_.pendingConnections.append((self.obj215.graphObject_.tag, self.obj214.graphObject_.tag, [344.0, 141.0, 297.0, 88.0, 207.0, 130.0], 2, True))

   cobj0.RHS = ASG_omacss(self)
   cobj0.RHS.merge(ASG_pns2(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj219=Agent(self)
   self.obj219.preAction( cobj0.RHS.CREATE )
   self.obj219.isGraphObjectVisual = True

   if(hasattr(self.obj219, '_setHierarchicalLink')):
     self.obj219._setHierarchicalLink(False)

   # price
   self.obj219.price.setNone()

   # name
   self.obj219.name.setValue('')
   self.obj219.name.setNone()

   self.obj219.GGLabel.setValue(1)
   self.obj219.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(60.0,60.0,self.obj219)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj219.graphObject_ = new_obj
   self.obj2190= AttrCalc()
   self.obj2190.Copy=ATOM3Boolean()
   self.obj2190.Copy.setValue(('Copy from LHS', 1))
   self.obj2190.Copy.config = 0
   self.obj2190.Specify=ATOM3Constraint()
   self.obj2190.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj219.GGset2Any['price']= self.obj2190
   self.obj2191= AttrCalc()
   self.obj2191.Copy=ATOM3Boolean()
   self.obj2191.Copy.setValue(('Copy from LHS', 1))
   self.obj2191.Copy.config = 0
   self.obj2191.Specify=ATOM3Constraint()
   self.obj2191.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj219.GGset2Any['name']= self.obj2191

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj219)
   self.obj219.postAction( cobj0.RHS.CREATE )

   self.obj220=Role(self)
   self.obj220.preAction( cobj0.RHS.CREATE )
   self.obj220.isGraphObjectVisual = True

   if(hasattr(self.obj220, '_setHierarchicalLink')):
     self.obj220._setHierarchicalLink(False)

   # name
   self.obj220.name.setValue('')
   self.obj220.name.setNone()

   self.obj220.GGLabel.setValue(2)
   self.obj220.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(320.0,140.0,self.obj220)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj220.graphObject_ = new_obj
   self.obj2200= AttrCalc()
   self.obj2200.Copy=ATOM3Boolean()
   self.obj2200.Copy.setValue(('Copy from LHS', 1))
   self.obj2200.Copy.config = 0
   self.obj2200.Specify=ATOM3Constraint()
   self.obj2200.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj220.GGset2Any['name']= self.obj2200

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj220)
   self.obj220.postAction( cobj0.RHS.CREATE )

   self.obj221=CapableOf(self)
   self.obj221.preAction( cobj0.RHS.CREATE )
   self.obj221.isGraphObjectVisual = True

   if(hasattr(self.obj221, '_setHierarchicalLink')):
     self.obj221._setHierarchicalLink(False)

   self.obj221.GGLabel.setValue(3)
   self.obj221.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(207.0,130.0,self.obj221)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj221.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj221)
   self.obj221.postAction( cobj0.RHS.CREATE )

   self.obj222=operatingUnit(self)
   self.obj222.preAction( cobj0.RHS.CREATE )
   self.obj222.isGraphObjectVisual = True

   if(hasattr(self.obj222, '_setHierarchicalLink')):
     self.obj222._setHierarchicalLink(False)

   # name
   self.obj222.name.setValue('')
   self.obj222.name.setNone()

   self.obj222.GGLabel.setValue(6)
   self.obj222.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(220.0,80.0,self.obj222)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj222.graphObject_ = new_obj
   self.obj2220= AttrCalc()
   self.obj2220.Copy=ATOM3Boolean()
   self.obj2220.Copy.setValue(('Copy from LHS', 0))
   self.obj2220.Copy.config = 0
   self.obj2220.Specify=ATOM3Constraint()
   self.obj2220.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()+\' \'+self.getMatched(graphID, self.LHS.nodeWithLabel(2)).name.getValue()\n\n\n\n\n\n\n'))
   self.obj222.GGset2Any['name']= self.obj2220

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj222)
   self.obj222.postAction( cobj0.RHS.CREATE )

   self.obj223=GenericGraphEdge(self)
   self.obj223.preAction( cobj0.RHS.CREATE )
   self.obj223.isGraphObjectVisual = True

   if(hasattr(self.obj223, '_setHierarchicalLink')):
     self.obj223._setHierarchicalLink(False)

   self.obj223.GGLabel.setValue(7)
   self.obj223.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(196.5,66.5,self.obj223)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj223.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj223)
   self.obj223.postAction( cobj0.RHS.CREATE )

   self.obj219.out_connections_.append(self.obj221)
   self.obj221.in_connections_.append(self.obj219)
   self.obj219.graphObject_.pendingConnections.append((self.obj219.graphObject_.tag, self.obj221.graphObject_.tag, [97.0, 122.0, 207.0, 130.0], 2, 0))
   self.obj219.out_connections_.append(self.obj223)
   self.obj223.in_connections_.append(self.obj219)
   self.obj219.graphObject_.pendingConnections.append((self.obj219.graphObject_.tag, self.obj223.graphObject_.tag, [97.0, 122.0, 173.0, 79.0, 167.0, 103.0, 196.5, 66.5], 4, True))
   self.obj221.out_connections_.append(self.obj220)
   self.obj220.in_connections_.append(self.obj221)
   self.obj221.graphObject_.pendingConnections.append((self.obj221.graphObject_.tag, self.obj220.graphObject_.tag, [351.0, 140.0, 207.0, 130.0], 2, 0))
   self.obj223.out_connections_.append(self.obj222)
   self.obj222.in_connections_.append(self.obj223)
   self.obj223.graphObject_.pendingConnections.append((self.obj223.graphObject_.tag, self.obj222.graphObject_.tag, [261.32710280373834, 87.47368421052629, 220.0, 54.0, 261.0, 53.0, 196.5, 66.5], 4, True))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nnode2 = self.getMatched(graphID, self.LHS.nodeWithLabel(2))\nreturn not(  hasattr(node, "LinkAR2OpUnit") and hasattr(node2, "LinkAR2OpUnit") )\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'node = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) )\nnode.LinkAR2OpUnit = True \nnode = self.getMatched ( graphID , self.LHS.nodeWithLabel(2) )\nnode.LinkAR2OpUnit = True \n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('TransformGoal2Mat', 20)
   cobj0.Order=ATOM3Integer(9)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

   from CapableOf import *
   from Goal import *
   from ASG_omacss import *
   from Agent import *
   from Capabilitie import *
   from Role import *
   from requir import *
   from achieve import *
   from posses import *
   from GenericGraphEdge import *
   from intoProduct import *
   from operatingUnit import *
   from metarial import *
   from rawMaterial import *
   from fromMaterial import *
   from fromRaw import *
   from ASG_pns2 import *
   from intoMaterial import *
   from ASG_GenericGraph import *
   from product import *
   from GenericGraphNode import *

   cobj0.LHS = ASG_omacss(self)

   self.obj228=Goal(self)
   self.obj228.preAction( cobj0.LHS.CREATE )
   self.obj228.isGraphObjectVisual = True

   if(hasattr(self.obj228, '_setHierarchicalLink')):
     self.obj228._setHierarchicalLink(False)

   # name
   self.obj228.name.setValue('')
   self.obj228.name.setNone()

   self.obj228.GGLabel.setValue(1)
   self.obj228.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(100.0,80.0,self.obj228)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj228.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj228)
   self.obj228.postAction( cobj0.LHS.CREATE )


   cobj0.RHS = ASG_omacss(self)
   cobj0.RHS.merge(ASG_pns2(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj232=Goal(self)
   self.obj232.preAction( cobj0.RHS.CREATE )
   self.obj232.isGraphObjectVisual = True

   if(hasattr(self.obj232, '_setHierarchicalLink')):
     self.obj232._setHierarchicalLink(False)

   # name
   self.obj232.name.setValue('')
   self.obj232.name.setNone()

   self.obj232.GGLabel.setValue(1)
   self.obj232.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(60.0,80.0,self.obj232)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj232.graphObject_ = new_obj
   self.obj2320= AttrCalc()
   self.obj2320.Copy=ATOM3Boolean()
   self.obj2320.Copy.setValue(('Copy from LHS', 1))
   self.obj2320.Copy.config = 0
   self.obj2320.Specify=ATOM3Constraint()
   self.obj2320.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj232.GGset2Any['name']= self.obj2320

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj232)
   self.obj232.postAction( cobj0.RHS.CREATE )

   self.obj233=metarial(self)
   self.obj233.preAction( cobj0.RHS.CREATE )
   self.obj233.isGraphObjectVisual = True

   if(hasattr(self.obj233, '_setHierarchicalLink')):
     self.obj233._setHierarchicalLink(False)

   # Name
   self.obj233.Name.setValue('')
   self.obj233.Name.setNone()

   self.obj233.GGLabel.setValue(3)
   self.obj233.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(220.0,80.0,self.obj233)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj233.graphObject_ = new_obj
   self.obj2330= AttrCalc()
   self.obj2330.Copy=ATOM3Boolean()
   self.obj2330.Copy.setValue(('Copy from LHS', 0))
   self.obj2330.Copy.config = 0
   self.obj2330.Specify=ATOM3Constraint()
   self.obj2330.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()\n'))
   self.obj233.GGset2Any['Name']= self.obj2330

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj233)
   self.obj233.postAction( cobj0.RHS.CREATE )

   self.obj234=GenericGraphEdge(self)
   self.obj234.preAction( cobj0.RHS.CREATE )
   self.obj234.isGraphObjectVisual = True

   if(hasattr(self.obj234, '_setHierarchicalLink')):
     self.obj234._setHierarchicalLink(False)

   self.obj234.GGLabel.setValue(4)
   self.obj234.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(162.0,127.0,self.obj234)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj234.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj234)
   self.obj234.postAction( cobj0.RHS.CREATE )

   self.obj232.out_connections_.append(self.obj234)
   self.obj234.in_connections_.append(self.obj232)
   self.obj232.graphObject_.pendingConnections.append((self.obj232.graphObject_.tag, self.obj234.graphObject_.tag, [94.0, 130.0, 162.0, 127.0], 0, True))
   self.obj234.out_connections_.append(self.obj233)
   self.obj233.in_connections_.append(self.obj234)
   self.obj234.graphObject_.pendingConnections.append((self.obj234.graphObject_.tag, self.obj233.graphObject_.tag, [230.0, 124.0, 162.0, 127.0], 0, True))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nreturn not hasattr(node, "Goal2Mat")\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'node = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) )\nnode.Goal2Mat = True\n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('CreatLinkRaw2AR', 20)
   cobj0.Order=ATOM3Integer(11)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

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

   cobj0.LHS = ASG_omacss(self)
   cobj0.LHS.merge(ASG_pns2(self))
   cobj0.LHS.merge(ASG_GenericGraph(self))

   self.obj241=Agent(self)
   self.obj241.preAction( cobj0.LHS.CREATE )
   self.obj241.isGraphObjectVisual = True

   if(hasattr(self.obj241, '_setHierarchicalLink')):
     self.obj241._setHierarchicalLink(False)

   # price
   self.obj241.price.setValue(0)

   # name
   self.obj241.name.setValue('')
   self.obj241.name.setNone()

   self.obj241.GGLabel.setValue(1)
   self.obj241.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(100.0,40.0,self.obj241)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj241.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj241)
   self.obj241.postAction( cobj0.LHS.CREATE )

   self.obj242=rawMaterial(self)
   self.obj242.preAction( cobj0.LHS.CREATE )
   self.obj242.isGraphObjectVisual = True

   if(hasattr(self.obj242, '_setHierarchicalLink')):
     self.obj242._setHierarchicalLink(False)

   # Name
   self.obj242.Name.setValue('')
   self.obj242.Name.setNone()

   self.obj242.GGLabel.setValue(3)
   self.obj242.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(280.0,20.0,self.obj242)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj242.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj242)
   self.obj242.postAction( cobj0.LHS.CREATE )

   self.obj243=operatingUnit(self)
   self.obj243.preAction( cobj0.LHS.CREATE )
   self.obj243.isGraphObjectVisual = True

   if(hasattr(self.obj243, '_setHierarchicalLink')):
     self.obj243._setHierarchicalLink(False)

   # name
   self.obj243.name.setValue('')
   self.obj243.name.setNone()

   self.obj243.GGLabel.setValue(2)
   self.obj243.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(260.0,160.0,self.obj243)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj243.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj243)
   self.obj243.postAction( cobj0.LHS.CREATE )

   self.obj244=GenericGraphEdge(self)
   self.obj244.preAction( cobj0.LHS.CREATE )
   self.obj244.isGraphObjectVisual = True

   if(hasattr(self.obj244, '_setHierarchicalLink')):
     self.obj244._setHierarchicalLink(False)

   self.obj244.GGLabel.setValue(4)
   self.obj244.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(214.75,92.75,self.obj244)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj244.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj244)
   self.obj244.postAction( cobj0.LHS.CREATE )

   self.obj245=GenericGraphEdge(self)
   self.obj245.preAction( cobj0.LHS.CREATE )
   self.obj245.isGraphObjectVisual = True

   if(hasattr(self.obj245, '_setHierarchicalLink')):
     self.obj245._setHierarchicalLink(False)

   self.obj245.GGLabel.setValue(5)
   self.obj245.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(241.642523364,131.105263158,self.obj245)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj245.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj245)
   self.obj245.postAction( cobj0.LHS.CREATE )

   self.obj241.out_connections_.append(self.obj244)
   self.obj244.in_connections_.append(self.obj241)
   self.obj241.graphObject_.pendingConnections.append((self.obj241.graphObject_.tag, self.obj244.graphObject_.tag, [125.0, 102.0, 170.0, 100.0, 214.75, 92.75], 2, True))
   self.obj241.out_connections_.append(self.obj245)
   self.obj245.in_connections_.append(self.obj241)
   self.obj241.graphObject_.pendingConnections.append((self.obj241.graphObject_.tag, self.obj245.graphObject_.tag, [125.0, 102.0, 204.5, 114.5, 241.64252336448598, 131.10526315789474], 2, True))
   self.obj244.out_connections_.append(self.obj242)
   self.obj242.in_connections_.append(self.obj244)
   self.obj244.graphObject_.pendingConnections.append((self.obj244.graphObject_.tag, self.obj242.graphObject_.tag, [304.0, 73.0, 259.5, 85.5, 214.75, 92.75], 2, True))
   self.obj245.out_connections_.append(self.obj243)
   self.obj243.in_connections_.append(self.obj245)
   self.obj245.graphObject_.pendingConnections.append((self.obj245.graphObject_.tag, self.obj243.graphObject_.tag, [273.5700934579439, 168.42105263157896, 278.78504672897196, 147.71052631578948, 241.64252336448598, 131.10526315789474], 2, True))

   cobj0.RHS = ASG_omacss(self)
   cobj0.RHS.merge(ASG_pns2(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj249=Agent(self)
   self.obj249.preAction( cobj0.RHS.CREATE )
   self.obj249.isGraphObjectVisual = True

   if(hasattr(self.obj249, '_setHierarchicalLink')):
     self.obj249._setHierarchicalLink(False)

   # price
   self.obj249.price.setValue(0)

   # name
   self.obj249.name.setValue('')
   self.obj249.name.setNone()

   self.obj249.GGLabel.setValue(1)
   self.obj249.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(60.0,60.0,self.obj249)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj249.graphObject_ = new_obj
   self.obj2490= AttrCalc()
   self.obj2490.Copy=ATOM3Boolean()
   self.obj2490.Copy.setValue(('Copy from LHS', 1))
   self.obj2490.Copy.config = 0
   self.obj2490.Specify=ATOM3Constraint()
   self.obj2490.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj249.GGset2Any['price']= self.obj2490
   self.obj2491= AttrCalc()
   self.obj2491.Copy=ATOM3Boolean()
   self.obj2491.Copy.setValue(('Copy from LHS', 1))
   self.obj2491.Copy.config = 0
   self.obj2491.Specify=ATOM3Constraint()
   self.obj2491.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj249.GGset2Any['name']= self.obj2491

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj249)
   self.obj249.postAction( cobj0.RHS.CREATE )

   self.obj250=rawMaterial(self)
   self.obj250.preAction( cobj0.RHS.CREATE )
   self.obj250.isGraphObjectVisual = True

   if(hasattr(self.obj250, '_setHierarchicalLink')):
     self.obj250._setHierarchicalLink(False)

   # Name
   self.obj250.Name.setValue('')
   self.obj250.Name.setNone()

   self.obj250.GGLabel.setValue(3)
   self.obj250.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(240.0,20.0,self.obj250)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj250.graphObject_ = new_obj
   self.obj2500= AttrCalc()
   self.obj2500.Copy=ATOM3Boolean()
   self.obj2500.Copy.setValue(('Copy from LHS', 1))
   self.obj2500.Copy.config = 0
   self.obj2500.Specify=ATOM3Constraint()
   self.obj2500.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj250.GGset2Any['Name']= self.obj2500

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj250)
   self.obj250.postAction( cobj0.RHS.CREATE )

   self.obj251=operatingUnit(self)
   self.obj251.preAction( cobj0.RHS.CREATE )
   self.obj251.isGraphObjectVisual = True

   if(hasattr(self.obj251, '_setHierarchicalLink')):
     self.obj251._setHierarchicalLink(False)

   # name
   self.obj251.name.setValue('')
   self.obj251.name.setNone()

   self.obj251.GGLabel.setValue(2)
   self.obj251.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(260.0,160.0,self.obj251)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj251.graphObject_ = new_obj
   self.obj2510= AttrCalc()
   self.obj2510.Copy=ATOM3Boolean()
   self.obj2510.Copy.setValue(('Copy from LHS', 1))
   self.obj2510.Copy.config = 0
   self.obj2510.Specify=ATOM3Constraint()
   self.obj2510.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj251.GGset2Any['name']= self.obj2510

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj251)
   self.obj251.postAction( cobj0.RHS.CREATE )

   self.obj252=fromRaw(self)
   self.obj252.preAction( cobj0.RHS.CREATE )
   self.obj252.isGraphObjectVisual = True

   if(hasattr(self.obj252, '_setHierarchicalLink')):
     self.obj252._setHierarchicalLink(False)

   # rate
   self.obj252.rate.setValue(1.0)

   self.obj252.GGLabel.setValue(6)
   self.obj252.graphClass_= graph_fromRaw
   if self.genGraphics:
      new_obj = graph_fromRaw(268.785046729,120.710526316,self.obj252)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj252.graphObject_ = new_obj
   self.obj2520= AttrCalc()
   self.obj2520.Copy=ATOM3Boolean()
   self.obj2520.Copy.setValue(('Copy from LHS', 0))
   self.obj2520.Copy.config = 0
   self.obj2520.Specify=ATOM3Constraint()
   self.obj2520.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj252.GGset2Any['rate']= self.obj2520

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj252)
   self.obj252.postAction( cobj0.RHS.CREATE )

   self.obj253=GenericGraphEdge(self)
   self.obj253.preAction( cobj0.RHS.CREATE )
   self.obj253.isGraphObjectVisual = True

   if(hasattr(self.obj253, '_setHierarchicalLink')):
     self.obj253._setHierarchicalLink(False)

   self.obj253.GGLabel.setValue(4)
   self.obj253.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(174.5,97.5,self.obj253)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj253.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj253)
   self.obj253.postAction( cobj0.RHS.CREATE )

   self.obj254=GenericGraphEdge(self)
   self.obj254.preAction( cobj0.RHS.CREATE )
   self.obj254.isGraphObjectVisual = True

   if(hasattr(self.obj254, '_setHierarchicalLink')):
     self.obj254._setHierarchicalLink(False)

   self.obj254.GGLabel.setValue(5)
   self.obj254.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(179.285046729,145.210526316,self.obj254)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj254.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj254)
   self.obj254.postAction( cobj0.RHS.CREATE )

   self.obj249.out_connections_.append(self.obj253)
   self.obj253.in_connections_.append(self.obj249)
   self.obj249.graphObject_.pendingConnections.append((self.obj249.graphObject_.tag, self.obj253.graphObject_.tag, [85.0, 122.0, 174.5, 97.5], 0, True))
   self.obj249.out_connections_.append(self.obj254)
   self.obj254.in_connections_.append(self.obj249)
   self.obj249.graphObject_.pendingConnections.append((self.obj249.graphObject_.tag, self.obj254.graphObject_.tag, [85.0, 122.0, 179.28504672897196, 145.21052631578948], 0, True))
   self.obj250.out_connections_.append(self.obj252)
   self.obj252.in_connections_.append(self.obj250)
   self.obj250.graphObject_.pendingConnections.append((self.obj250.graphObject_.tag, self.obj252.graphObject_.tag, [264.0, 73.0, 268.78504672897196, 120.71052631578948], 0, True))
   self.obj252.out_connections_.append(self.obj251)
   self.obj251.in_connections_.append(self.obj252)
   self.obj252.graphObject_.pendingConnections.append((self.obj252.graphObject_.tag, self.obj251.graphObject_.tag, [273.5700934579439, 168.42105263157896, 268.78504672897196, 120.71052631578948], 0, True))
   self.obj253.out_connections_.append(self.obj250)
   self.obj250.in_connections_.append(self.obj253)
   self.obj253.graphObject_.pendingConnections.append((self.obj253.graphObject_.tag, self.obj250.graphObject_.tag, [264.0, 73.0, 174.5, 97.5], 0, True))
   self.obj254.out_connections_.append(self.obj251)
   self.obj251.in_connections_.append(self.obj254)
   self.obj254.graphObject_.pendingConnections.append((self.obj254.graphObject_.tag, self.obj251.graphObject_.tag, [273.5700934579439, 168.42105263157896, 179.28504672897196, 145.21052631578948], 0, True))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'node = self.getMatched(graphID, self.LHS.nodeWithLabel(2))\nreturn not hasattr(node, "LinkRaw2AR")\n\n'))
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

   from CapableOf import *
   from Goal import *
   from ASG_omacss import *
   from Agent import *
   from Capabilitie import *
   from Role import *
   from requir import *
   from achieve import *
   from posses import *
   from intoProduct import *
   from operatingUnit import *
   from metarial import *
   from rawMaterial import *
   from fromMaterial import *
   from fromRaw import *
   from ASG_pns2 import *
   from intoMaterial import *
   from product import *

   cobj0.LHS = ASG_omacss(self)


   cobj0.RHS = ASG_omacss(self)
   cobj0.RHS.merge(ASG_pns2(self))

   self.obj261=product(self)
   self.obj261.preAction( cobj0.RHS.CREATE )
   self.obj261.isGraphObjectVisual = True

   if(hasattr(self.obj261, '_setHierarchicalLink')):
     self.obj261._setHierarchicalLink(False)

   # Name
   self.obj261.Name.setValue('OAF')

   self.obj261.GGLabel.setValue(1)
   self.obj261.graphClass_= graph_product
   if self.genGraphics:
      new_obj = graph_product(180.0,40.0,self.obj261)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj261.graphObject_ = new_obj
   self.obj2610= AttrCalc()
   self.obj2610.Copy=ATOM3Boolean()
   self.obj2610.Copy.setValue(('Copy from LHS', 0))
   self.obj2610.Copy.config = 0
   self.obj2610.Specify=ATOM3Constraint()
   self.obj2610.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj261.GGset2Any['Name']= self.obj2610

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj261)
   self.obj261.postAction( cobj0.RHS.CREATE )


   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.graphRewritingSystem.finalStat == 0\n\n\n\n\n\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'self.graphRewritingSystem.finalStat = 1 \n\n\n\n\n\n\n\n\n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('CreateLinkMatr2OAF', 20)
   cobj0.Order=ATOM3Integer(15)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

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

   cobj0.LHS = ASG_omacss(self)
   cobj0.LHS.merge(ASG_pns2(self))
   cobj0.LHS.merge(ASG_GenericGraph(self))

   self.obj268=Goal(self)
   self.obj268.preAction( cobj0.LHS.CREATE )
   self.obj268.isGraphObjectVisual = True

   if(hasattr(self.obj268, '_setHierarchicalLink')):
     self.obj268._setHierarchicalLink(False)

   # name
   self.obj268.name.setValue('')
   self.obj268.name.setNone()

   self.obj268.GGLabel.setValue(2)
   self.obj268.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(80.0,40.0,self.obj268)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj268.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj268)
   self.obj268.postAction( cobj0.LHS.CREATE )

   self.obj269=metarial(self)
   self.obj269.preAction( cobj0.LHS.CREATE )
   self.obj269.isGraphObjectVisual = True

   if(hasattr(self.obj269, '_setHierarchicalLink')):
     self.obj269._setHierarchicalLink(False)

   # Name
   self.obj269.Name.setValue('')
   self.obj269.Name.setNone()

   self.obj269.GGLabel.setValue(3)
   self.obj269.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(220.0,40.0,self.obj269)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj269.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj269)
   self.obj269.postAction( cobj0.LHS.CREATE )

   self.obj270=product(self)
   self.obj270.preAction( cobj0.LHS.CREATE )
   self.obj270.isGraphObjectVisual = True

   if(hasattr(self.obj270, '_setHierarchicalLink')):
     self.obj270._setHierarchicalLink(False)

   # Name
   self.obj270.Name.setValue('')
   self.obj270.Name.setNone()

   self.obj270.GGLabel.setValue(5)
   self.obj270.graphClass_= graph_product
   if self.genGraphics:
      new_obj = graph_product(160.0,180.0,self.obj270)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj270.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj270)
   self.obj270.postAction( cobj0.LHS.CREATE )

   self.obj271=GenericGraphEdge(self)
   self.obj271.preAction( cobj0.LHS.CREATE )
   self.obj271.isGraphObjectVisual = True

   if(hasattr(self.obj271, '_setHierarchicalLink')):
     self.obj271._setHierarchicalLink(False)

   self.obj271.GGLabel.setValue(4)
   self.obj271.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(167.0,87.0,self.obj271)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj271.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj271)
   self.obj271.postAction( cobj0.LHS.CREATE )

   self.obj268.out_connections_.append(self.obj271)
   self.obj271.in_connections_.append(self.obj268)
   self.obj268.graphObject_.pendingConnections.append((self.obj268.graphObject_.tag, self.obj271.graphObject_.tag, [104.0, 90.0, 167.0, 87.0], 0, True))
   self.obj271.out_connections_.append(self.obj269)
   self.obj269.in_connections_.append(self.obj271)
   self.obj271.graphObject_.pendingConnections.append((self.obj271.graphObject_.tag, self.obj269.graphObject_.tag, [230.0, 84.0, 167.0, 87.0], 0, True))

   cobj0.RHS = ASG_omacss(self)
   cobj0.RHS.merge(ASG_pns2(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj275=Goal(self)
   self.obj275.preAction( cobj0.RHS.CREATE )
   self.obj275.isGraphObjectVisual = True

   if(hasattr(self.obj275, '_setHierarchicalLink')):
     self.obj275._setHierarchicalLink(False)

   # name
   self.obj275.name.setValue('')
   self.obj275.name.setNone()

   self.obj275.GGLabel.setValue(2)
   self.obj275.graphClass_= graph_Goal
   if self.genGraphics:
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

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj275)
   self.obj275.postAction( cobj0.RHS.CREATE )

   self.obj276=intoProduct(self)
   self.obj276.preAction( cobj0.RHS.CREATE )
   self.obj276.isGraphObjectVisual = True

   if(hasattr(self.obj276, '_setHierarchicalLink')):
     self.obj276._setHierarchicalLink(False)

   # rate
   self.obj276.rate.setValue(1.0)

   self.obj276.GGLabel.setValue(6)
   self.obj276.graphClass_= graph_intoProduct
   if self.genGraphics:
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

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj276)
   self.obj276.postAction( cobj0.RHS.CREATE )

   self.obj277=operatingUnit(self)
   self.obj277.preAction( cobj0.RHS.CREATE )
   self.obj277.isGraphObjectVisual = True

   if(hasattr(self.obj277, '_setHierarchicalLink')):
     self.obj277._setHierarchicalLink(False)

   # name
   self.obj277.name.setValue('')
   self.obj277.name.setNone()

   self.obj277.GGLabel.setValue(1)
   self.obj277.graphClass_= graph_operatingUnit
   if self.genGraphics:
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

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj277)
   self.obj277.postAction( cobj0.RHS.CREATE )

   self.obj278=metarial(self)
   self.obj278.preAction( cobj0.RHS.CREATE )
   self.obj278.isGraphObjectVisual = True

   if(hasattr(self.obj278, '_setHierarchicalLink')):
     self.obj278._setHierarchicalLink(False)

   # Name
   self.obj278.Name.setValue('')
   self.obj278.Name.setNone()

   self.obj278.GGLabel.setValue(3)
   self.obj278.graphClass_= graph_metarial
   if self.genGraphics:
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

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj278)
   self.obj278.postAction( cobj0.RHS.CREATE )

   self.obj279=product(self)
   self.obj279.preAction( cobj0.RHS.CREATE )
   self.obj279.isGraphObjectVisual = True

   if(hasattr(self.obj279, '_setHierarchicalLink')):
     self.obj279._setHierarchicalLink(False)

   # Name
   self.obj279.Name.setValue('')
   self.obj279.Name.setNone()

   self.obj279.GGLabel.setValue(5)
   self.obj279.graphClass_= graph_product
   if self.genGraphics:
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

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj279)
   self.obj279.postAction( cobj0.RHS.CREATE )

   self.obj280=fromMaterial(self)
   self.obj280.preAction( cobj0.RHS.CREATE )
   self.obj280.isGraphObjectVisual = True

   if(hasattr(self.obj280, '_setHierarchicalLink')):
     self.obj280._setHierarchicalLink(False)

   # rate
   self.obj280.rate.setValue(1.0)

   self.obj280.GGLabel.setValue(7)
   self.obj280.graphClass_= graph_fromMaterial
   if self.genGraphics:
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

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj280)
   self.obj280.postAction( cobj0.RHS.CREATE )

   self.obj281=GenericGraphEdge(self)
   self.obj281.preAction( cobj0.RHS.CREATE )
   self.obj281.isGraphObjectVisual = True

   if(hasattr(self.obj281, '_setHierarchicalLink')):
     self.obj281._setHierarchicalLink(False)

   self.obj281.GGLabel.setValue(4)
   self.obj281.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(137.5,43.0,self.obj281)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj281.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj281)
   self.obj281.postAction( cobj0.RHS.CREATE )

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

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'node = self.getMatched(graphID, self.LHS.nodeWithLabel(3))\nreturn not hasattr(node, "link2oaf")\n\n'))
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

   from CapableOf import *
   from Goal import *
   from ASG_omacss import *
   from Agent import *
   from Capabilitie import *
   from Role import *
   from requir import *
   from achieve import *
   from posses import *
   from GenericGraphEdge import *
   from intoProduct import *
   from operatingUnit import *
   from metarial import *
   from rawMaterial import *
   from fromMaterial import *
   from fromRaw import *
   from ASG_pns2 import *
   from intoMaterial import *
   from ASG_GenericGraph import *
   from product import *
   from GenericGraphNode import *

   cobj0.LHS = ASG_omacss(self)

   self.obj286=Agent(self)
   self.obj286.preAction( cobj0.LHS.CREATE )
   self.obj286.isGraphObjectVisual = True

   if(hasattr(self.obj286, '_setHierarchicalLink')):
     self.obj286._setHierarchicalLink(False)

   # price
   self.obj286.price.setValue(0)

   # name
   self.obj286.name.setValue('')
   self.obj286.name.setNone()

   self.obj286.GGLabel.setValue(1)
   self.obj286.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(80.0,20.0,self.obj286)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj286.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj286)
   self.obj286.postAction( cobj0.LHS.CREATE )

   self.obj287=Role(self)
   self.obj287.preAction( cobj0.LHS.CREATE )
   self.obj287.isGraphObjectVisual = True

   if(hasattr(self.obj287, '_setHierarchicalLink')):
     self.obj287._setHierarchicalLink(False)

   # name
   self.obj287.name.setValue('')
   self.obj287.name.setNone()

   self.obj287.GGLabel.setValue(2)
   self.obj287.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(200.0,100.0,self.obj287)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj287.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj287)
   self.obj287.postAction( cobj0.LHS.CREATE )

   self.obj288=Goal(self)
   self.obj288.preAction( cobj0.LHS.CREATE )
   self.obj288.isGraphObjectVisual = True

   if(hasattr(self.obj288, '_setHierarchicalLink')):
     self.obj288._setHierarchicalLink(False)

   # name
   self.obj288.name.setValue('')
   self.obj288.name.setNone()

   self.obj288.GGLabel.setValue(3)
   self.obj288.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(100.0,180.0,self.obj288)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj288.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj288)
   self.obj288.postAction( cobj0.LHS.CREATE )

   self.obj289=CapableOf(self)
   self.obj289.preAction( cobj0.LHS.CREATE )
   self.obj289.isGraphObjectVisual = True

   if(hasattr(self.obj289, '_setHierarchicalLink')):
     self.obj289._setHierarchicalLink(False)

   self.obj289.GGLabel.setValue(4)
   self.obj289.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(164.5,91.5,self.obj289)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj289.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj289)
   self.obj289.postAction( cobj0.LHS.CREATE )

   self.obj290=achieve(self)
   self.obj290.preAction( cobj0.LHS.CREATE )
   self.obj290.isGraphObjectVisual = True

   if(hasattr(self.obj290, '_setHierarchicalLink')):
     self.obj290._setHierarchicalLink(False)

   # rate
   self.obj290.rate.setNone()

   self.obj290.GGLabel.setValue(5)
   self.obj290.graphClass_= graph_achieve
   if self.genGraphics:
      new_obj = graph_achieve(173.5,163.5,self.obj290)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj290.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj290)
   self.obj290.postAction( cobj0.LHS.CREATE )

   self.obj286.out_connections_.append(self.obj289)
   self.obj289.in_connections_.append(self.obj286)
   self.obj286.graphObject_.pendingConnections.append((self.obj286.graphObject_.tag, self.obj289.graphObject_.tag, [105.0, 82.0, 164.5, 91.5], 0, True))
   self.obj287.out_connections_.append(self.obj290)
   self.obj290.in_connections_.append(self.obj287)
   self.obj287.graphObject_.pendingConnections.append((self.obj287.graphObject_.tag, self.obj290.graphObject_.tag, [224.0, 146.0, 173.5, 163.5], 0, True))
   self.obj289.out_connections_.append(self.obj287)
   self.obj287.in_connections_.append(self.obj289)
   self.obj289.graphObject_.pendingConnections.append((self.obj289.graphObject_.tag, self.obj287.graphObject_.tag, [224.0, 101.0, 164.5, 91.5], 0, True))
   self.obj290.out_connections_.append(self.obj288)
   self.obj288.in_connections_.append(self.obj290)
   self.obj290.graphObject_.pendingConnections.append((self.obj290.graphObject_.tag, self.obj288.graphObject_.tag, [123.0, 181.0, 173.5, 163.5], 0, True))

   cobj0.RHS = ASG_omacss(self)
   cobj0.RHS.merge(ASG_pns2(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj294=Agent(self)
   self.obj294.preAction( cobj0.RHS.CREATE )
   self.obj294.isGraphObjectVisual = True

   if(hasattr(self.obj294, '_setHierarchicalLink')):
     self.obj294._setHierarchicalLink(False)

   # price
   self.obj294.price.setValue(0)

   # name
   self.obj294.name.setValue('')
   self.obj294.name.setNone()

   self.obj294.GGLabel.setValue(1)
   self.obj294.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(80.0,20.0,self.obj294)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj294.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj294)
   self.obj294.postAction( cobj0.RHS.CREATE )

   self.obj295=Role(self)
   self.obj295.preAction( cobj0.RHS.CREATE )
   self.obj295.isGraphObjectVisual = True

   if(hasattr(self.obj295, '_setHierarchicalLink')):
     self.obj295._setHierarchicalLink(False)

   # name
   self.obj295.name.setValue('')
   self.obj295.name.setNone()

   self.obj295.GGLabel.setValue(2)
   self.obj295.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(200.0,100.0,self.obj295)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj295.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj295)
   self.obj295.postAction( cobj0.RHS.CREATE )

   self.obj296=Goal(self)
   self.obj296.preAction( cobj0.RHS.CREATE )
   self.obj296.isGraphObjectVisual = True

   if(hasattr(self.obj296, '_setHierarchicalLink')):
     self.obj296._setHierarchicalLink(False)

   # name
   self.obj296.name.setValue('')
   self.obj296.name.setNone()

   self.obj296.GGLabel.setValue(3)
   self.obj296.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(100.0,180.0,self.obj296)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj296.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj296)
   self.obj296.postAction( cobj0.RHS.CREATE )

   self.obj297=CapableOf(self)
   self.obj297.preAction( cobj0.RHS.CREATE )
   self.obj297.isGraphObjectVisual = True

   if(hasattr(self.obj297, '_setHierarchicalLink')):
     self.obj297._setHierarchicalLink(False)

   self.obj297.GGLabel.setValue(4)
   self.obj297.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(164.5,91.5,self.obj297)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj297.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj297)
   self.obj297.postAction( cobj0.RHS.CREATE )

   self.obj298=achieve(self)
   self.obj298.preAction( cobj0.RHS.CREATE )
   self.obj298.isGraphObjectVisual = True

   if(hasattr(self.obj298, '_setHierarchicalLink')):
     self.obj298._setHierarchicalLink(False)

   # rate
   self.obj298.rate.setValue(0.0)

   self.obj298.GGLabel.setValue(5)
   self.obj298.graphClass_= graph_achieve
   if self.genGraphics:
      new_obj = graph_achieve(173.5,163.5,self.obj298)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj298.graphObject_ = new_obj
   self.obj2980= AttrCalc()
   self.obj2980.Copy=ATOM3Boolean()
   self.obj2980.Copy.setValue(('Copy from LHS', 1))
   self.obj2980.Copy.config = 0
   self.obj2980.Specify=ATOM3Constraint()
   self.obj2980.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj298.GGset2Any['rate']= self.obj2980

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj298)
   self.obj298.postAction( cobj0.RHS.CREATE )

   self.obj299=operatingUnit(self)
   self.obj299.preAction( cobj0.RHS.CREATE )
   self.obj299.isGraphObjectVisual = True

   if(hasattr(self.obj299, '_setHierarchicalLink')):
     self.obj299._setHierarchicalLink(False)

   # name
   self.obj299.name.setValue('')
   self.obj299.name.setNone()

   self.obj299.GGLabel.setValue(7)
   self.obj299.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(320.0,140.0,self.obj299)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj299.graphObject_ = new_obj
   self.obj2990= AttrCalc()
   self.obj2990.Copy=ATOM3Boolean()
   self.obj2990.Copy.setValue(('Copy from LHS', 0))
   self.obj2990.Copy.config = 0
   self.obj2990.Specify=ATOM3Constraint()
   self.obj2990.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()+\' \'+ self.getMatched(graphID, self.LHS.nodeWithLabel(2)).name.getValue()+\' \'+ self.getMatched(graphID, self.LHS.nodeWithLabel(3)).name.getValue()\n'))
   self.obj299.GGset2Any['name']= self.obj2990

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj299)
   self.obj299.postAction( cobj0.RHS.CREATE )

   self.obj300=metarial(self)
   self.obj300.preAction( cobj0.RHS.CREATE )
   self.obj300.isGraphObjectVisual = True

   if(hasattr(self.obj300, '_setHierarchicalLink')):
     self.obj300._setHierarchicalLink(False)

   # Name
   self.obj300.Name.setValue('')
   self.obj300.Name.setNone()

   self.obj300.GGLabel.setValue(8)
   self.obj300.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(320.0,40.0,self.obj300)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj300.graphObject_ = new_obj
   self.obj3000= AttrCalc()
   self.obj3000.Copy=ATOM3Boolean()
   self.obj3000.Copy.setValue(('Copy from LHS', 0))
   self.obj3000.Copy.config = 0
   self.obj3000.Specify=ATOM3Constraint()
   self.obj3000.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()+\' \'+ self.getMatched(graphID, self.LHS.nodeWithLabel(2)).name.getValue()+\' \'+ self.getMatched(graphID, self.LHS.nodeWithLabel(3)).name.getValue()\n'))
   self.obj300.GGset2Any['Name']= self.obj3000

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj300)
   self.obj300.postAction( cobj0.RHS.CREATE )

   self.obj301=fromMaterial(self)
   self.obj301.preAction( cobj0.RHS.CREATE )
   self.obj301.isGraphObjectVisual = True

   if(hasattr(self.obj301, '_setHierarchicalLink')):
     self.obj301._setHierarchicalLink(False)

   # rate
   self.obj301.rate.setValue(1.0)

   self.obj301.GGLabel.setValue(9)
   self.obj301.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(338.785046729,119.210526316,self.obj301)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj301.graphObject_ = new_obj
   self.obj3010= AttrCalc()
   self.obj3010.Copy=ATOM3Boolean()
   self.obj3010.Copy.setValue(('Copy from LHS', 0))
   self.obj3010.Copy.config = 0
   self.obj3010.Specify=ATOM3Constraint()
   self.obj3010.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj301.GGset2Any['rate']= self.obj3010

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj301)
   self.obj301.postAction( cobj0.RHS.CREATE )

   self.obj302=GenericGraphEdge(self)
   self.obj302.preAction( cobj0.RHS.CREATE )
   self.obj302.isGraphObjectVisual = True

   if(hasattr(self.obj302, '_setHierarchicalLink')):
     self.obj302._setHierarchicalLink(False)

   self.obj302.GGLabel.setValue(10)
   self.obj302.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(280.5,92.0,self.obj302)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj302.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj302)
   self.obj302.postAction( cobj0.RHS.CREATE )

   self.obj294.out_connections_.append(self.obj297)
   self.obj297.in_connections_.append(self.obj294)
   self.obj294.graphObject_.pendingConnections.append((self.obj294.graphObject_.tag, self.obj297.graphObject_.tag, [117.0, 82.0, 164.5, 91.5], 2, 0))
   self.obj295.out_connections_.append(self.obj298)
   self.obj298.in_connections_.append(self.obj295)
   self.obj295.graphObject_.pendingConnections.append((self.obj295.graphObject_.tag, self.obj298.graphObject_.tag, [231.0, 145.0, 173.5, 163.5], 2, 0))
   self.obj295.out_connections_.append(self.obj302)
   self.obj302.in_connections_.append(self.obj295)
   self.obj295.graphObject_.pendingConnections.append((self.obj295.graphObject_.tag, self.obj302.graphObject_.tag, [231.0, 100.0, 280.5, 92.0], 0, True))
   self.obj297.out_connections_.append(self.obj295)
   self.obj295.in_connections_.append(self.obj297)
   self.obj297.graphObject_.pendingConnections.append((self.obj297.graphObject_.tag, self.obj295.graphObject_.tag, [231.0, 100.0, 164.5, 91.5], 2, 0))
   self.obj298.out_connections_.append(self.obj296)
   self.obj296.in_connections_.append(self.obj298)
   self.obj298.graphObject_.pendingConnections.append((self.obj298.graphObject_.tag, self.obj296.graphObject_.tag, [133.0, 181.0, 173.5, 163.5], 2, 0))
   self.obj300.out_connections_.append(self.obj301)
   self.obj301.in_connections_.append(self.obj300)
   self.obj300.graphObject_.pendingConnections.append((self.obj300.graphObject_.tag, self.obj301.graphObject_.tag, [344.0, 90.0, 338.78504672897196, 119.21052631578948], 0, True))
   self.obj301.out_connections_.append(self.obj299)
   self.obj299.in_connections_.append(self.obj301)
   self.obj301.graphObject_.pendingConnections.append((self.obj301.graphObject_.tag, self.obj299.graphObject_.tag, [333.5700934579439, 148.42105263157896, 338.78504672897196, 119.21052631578948], 0, True))
   self.obj302.out_connections_.append(self.obj300)
   self.obj300.in_connections_.append(self.obj302)
   self.obj302.graphObject_.pendingConnections.append((self.obj302.graphObject_.tag, self.obj300.graphObject_.tag, [330.0, 84.0, 280.5, 92.0], 0, True))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'print \'======> GenAux1 Condition\'\na = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\naN = a.name.getValue()\n#print a.name.getValue()+\' has att AUX : \'+str( hasattr(a, "AUX") )\nr = self.getMatched(graphID, self.LHS.nodeWithLabel(2))\nRn = r.name.getValue()\ng = self.getMatched(graphID, self.LHS.nodeWithLabel(3))\nGn = g.name.getValue()\n# add list to the Agent Node\nif not hasattr(a,\'markedNode\') : \n	a.markedNode = []\n	print \'add List to \'+aN\n\nprint \'CHeck if \'+aN+\'Have\'\nfor ele in a.markedNode : \n    if ele == (Rn,Gn) : return False\nreturn True\n#        print \'Check if \'+aN+\'Have \'\n#        for ele in a.markedNode : \n#            if ele == (Rn,Gn) : return False \n#        return True\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'print \'======> GenAux1 ACtion\'\na = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\naN = a.name.getValue()\n#print a.name.getValue()+\' has att AUX : \'+str( hasattr(a, "AUX") )\nr = self.getMatched(graphID, self.LHS.nodeWithLabel(2))\nRn = r.name.getValue()\ng = self.getMatched(graphID, self.LHS.nodeWithLabel(3))\nGn = g.name.getValue()\n# add ele list to the Agent Node\nprint \'Add Ele into list of \'+aN\na.markedNode.append( (Rn,Gn) )\nprint \'List of MarkedNode\'\nfor ele in a.markedNode : \n	print ele\n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('CreateLinkMat_ARG2Goal', 20)
   cobj0.Order=ATOM3Integer(19)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

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

   cobj0.LHS = ASG_omacss(self)
   cobj0.LHS.merge(ASG_pns2(self))
   cobj0.LHS.merge(ASG_GenericGraph(self))

   self.obj309=Role(self)
   self.obj309.preAction( cobj0.LHS.CREATE )
   self.obj309.isGraphObjectVisual = True

   if(hasattr(self.obj309, '_setHierarchicalLink')):
     self.obj309._setHierarchicalLink(False)

   # name
   self.obj309.name.setValue('')
   self.obj309.name.setNone()

   self.obj309.GGLabel.setValue(1)
   self.obj309.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(80.0,20.0,self.obj309)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj309.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj309)
   self.obj309.postAction( cobj0.LHS.CREATE )

   self.obj310=Goal(self)
   self.obj310.preAction( cobj0.LHS.CREATE )
   self.obj310.isGraphObjectVisual = True

   if(hasattr(self.obj310, '_setHierarchicalLink')):
     self.obj310._setHierarchicalLink(False)

   # name
   self.obj310.name.setValue('')
   self.obj310.name.setNone()

   self.obj310.GGLabel.setValue(2)
   self.obj310.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(100.0,180.0,self.obj310)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj310.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj310)
   self.obj310.postAction( cobj0.LHS.CREATE )

   self.obj311=achieve(self)
   self.obj311.preAction( cobj0.LHS.CREATE )
   self.obj311.isGraphObjectVisual = True

   if(hasattr(self.obj311, '_setHierarchicalLink')):
     self.obj311._setHierarchicalLink(False)

   # rate
   self.obj311.rate.setNone()

   self.obj311.GGLabel.setValue(3)
   self.obj311.graphClass_= graph_achieve
   if self.genGraphics:
      new_obj = graph_achieve(113.5,123.5,self.obj311)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj311.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj311)
   self.obj311.postAction( cobj0.LHS.CREATE )

   self.obj312=operatingUnit(self)
   self.obj312.preAction( cobj0.LHS.CREATE )
   self.obj312.isGraphObjectVisual = True

   if(hasattr(self.obj312, '_setHierarchicalLink')):
     self.obj312._setHierarchicalLink(False)

   # name
   self.obj312.name.setValue('')
   self.obj312.name.setNone()

   self.obj312.GGLabel.setValue(5)
   self.obj312.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(280.0,100.0,self.obj312)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj312.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj312)
   self.obj312.postAction( cobj0.LHS.CREATE )

   self.obj313=metarial(self)
   self.obj313.preAction( cobj0.LHS.CREATE )
   self.obj313.isGraphObjectVisual = True

   if(hasattr(self.obj313, '_setHierarchicalLink')):
     self.obj313._setHierarchicalLink(False)

   # Name
   self.obj313.Name.setValue('')
   self.obj313.Name.setNone()

   self.obj313.GGLabel.setValue(4)
   self.obj313.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(280.0,20.0,self.obj313)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj313.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj313)
   self.obj313.postAction( cobj0.LHS.CREATE )

   self.obj314=metarial(self)
   self.obj314.preAction( cobj0.LHS.CREATE )
   self.obj314.isGraphObjectVisual = True

   if(hasattr(self.obj314, '_setHierarchicalLink')):
     self.obj314._setHierarchicalLink(False)

   # Name
   self.obj314.Name.setValue('')
   self.obj314.Name.setNone()

   self.obj314.GGLabel.setValue(6)
   self.obj314.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(320.0,220.0,self.obj314)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj314.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj314)
   self.obj314.postAction( cobj0.LHS.CREATE )

   self.obj315=fromMaterial(self)
   self.obj315.preAction( cobj0.LHS.CREATE )
   self.obj315.isGraphObjectVisual = True

   if(hasattr(self.obj315, '_setHierarchicalLink')):
     self.obj315._setHierarchicalLink(False)

   # rate
   self.obj315.rate.setNone()

   self.obj315.GGLabel.setValue(8)
   self.obj315.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(298.785046729,89.2105263158,self.obj315)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj315.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj315)
   self.obj315.postAction( cobj0.LHS.CREATE )

   self.obj316=GenericGraphEdge(self)
   self.obj316.preAction( cobj0.LHS.CREATE )
   self.obj316.isGraphObjectVisual = True

   if(hasattr(self.obj316, '_setHierarchicalLink')):
     self.obj316._setHierarchicalLink(False)

   self.obj316.GGLabel.setValue(7)
   self.obj316.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(198.0,23.0,self.obj316)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj316.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj316)
   self.obj316.postAction( cobj0.LHS.CREATE )

   self.obj317=GenericGraphEdge(self)
   self.obj317.preAction( cobj0.LHS.CREATE )
   self.obj317.isGraphObjectVisual = True

   if(hasattr(self.obj317, '_setHierarchicalLink')):
     self.obj317._setHierarchicalLink(False)

   self.obj317.GGLabel.setValue(9)
   self.obj317.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(228.0,227.5,self.obj317)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj317.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj317)
   self.obj317.postAction( cobj0.LHS.CREATE )

   self.obj309.out_connections_.append(self.obj311)
   self.obj311.in_connections_.append(self.obj309)
   self.obj309.graphObject_.pendingConnections.append((self.obj309.graphObject_.tag, self.obj311.graphObject_.tag, [104.0, 66.0, 113.5, 123.5], 0, True))
   self.obj309.out_connections_.append(self.obj316)
   self.obj316.in_connections_.append(self.obj309)
   self.obj309.graphObject_.pendingConnections.append((self.obj309.graphObject_.tag, self.obj316.graphObject_.tag, [104.0, 21.0, 198.0, 23.0], 0, True))
   self.obj310.out_connections_.append(self.obj317)
   self.obj317.in_connections_.append(self.obj310)
   self.obj310.graphObject_.pendingConnections.append((self.obj310.graphObject_.tag, self.obj317.graphObject_.tag, [124.0, 230.0, 228.0, 227.5], 0, True))
   self.obj311.out_connections_.append(self.obj310)
   self.obj310.in_connections_.append(self.obj311)
   self.obj311.graphObject_.pendingConnections.append((self.obj311.graphObject_.tag, self.obj310.graphObject_.tag, [123.0, 181.0, 113.5, 123.5], 0, True))
   self.obj313.out_connections_.append(self.obj315)
   self.obj315.in_connections_.append(self.obj313)
   self.obj313.graphObject_.pendingConnections.append((self.obj313.graphObject_.tag, self.obj315.graphObject_.tag, [304.0, 70.0, 298.78504672897196, 89.21052631578948], 0, True))
   self.obj315.out_connections_.append(self.obj312)
   self.obj312.in_connections_.append(self.obj315)
   self.obj315.graphObject_.pendingConnections.append((self.obj315.graphObject_.tag, self.obj312.graphObject_.tag, [293.5700934579439, 108.42105263157895, 298.78504672897196, 89.21052631578948], 0, True))
   self.obj316.out_connections_.append(self.obj313)
   self.obj313.in_connections_.append(self.obj316)
   self.obj316.graphObject_.pendingConnections.append((self.obj316.graphObject_.tag, self.obj313.graphObject_.tag, [292.0, 25.0, 198.0, 23.0], 0, True))
   self.obj317.out_connections_.append(self.obj314)
   self.obj314.in_connections_.append(self.obj317)
   self.obj317.graphObject_.pendingConnections.append((self.obj317.graphObject_.tag, self.obj314.graphObject_.tag, [332.0, 225.0, 228.0, 227.5], 0, True))

   cobj0.RHS = ASG_omacss(self)
   cobj0.RHS.merge(ASG_pns2(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj321=Role(self)
   self.obj321.preAction( cobj0.RHS.CREATE )
   self.obj321.isGraphObjectVisual = True

   if(hasattr(self.obj321, '_setHierarchicalLink')):
     self.obj321._setHierarchicalLink(False)

   # name
   self.obj321.name.setValue('')
   self.obj321.name.setNone()

   self.obj321.GGLabel.setValue(1)
   self.obj321.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(100.0,40.0,self.obj321)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj321.graphObject_ = new_obj
   self.obj3210= AttrCalc()
   self.obj3210.Copy=ATOM3Boolean()
   self.obj3210.Copy.setValue(('Copy from LHS', 1))
   self.obj3210.Copy.config = 0
   self.obj3210.Specify=ATOM3Constraint()
   self.obj3210.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj321.GGset2Any['name']= self.obj3210

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj321)
   self.obj321.postAction( cobj0.RHS.CREATE )

   self.obj322=Goal(self)
   self.obj322.preAction( cobj0.RHS.CREATE )
   self.obj322.isGraphObjectVisual = True

   if(hasattr(self.obj322, '_setHierarchicalLink')):
     self.obj322._setHierarchicalLink(False)

   # name
   self.obj322.name.setValue('')
   self.obj322.name.setNone()

   self.obj322.GGLabel.setValue(2)
   self.obj322.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(120.0,160.0,self.obj322)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj322.graphObject_ = new_obj
   self.obj3220= AttrCalc()
   self.obj3220.Copy=ATOM3Boolean()
   self.obj3220.Copy.setValue(('Copy from LHS', 1))
   self.obj3220.Copy.config = 0
   self.obj3220.Specify=ATOM3Constraint()
   self.obj3220.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj322.GGset2Any['name']= self.obj3220

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj322)
   self.obj322.postAction( cobj0.RHS.CREATE )

   self.obj323=achieve(self)
   self.obj323.preAction( cobj0.RHS.CREATE )
   self.obj323.isGraphObjectVisual = True

   if(hasattr(self.obj323, '_setHierarchicalLink')):
     self.obj323._setHierarchicalLink(False)

   # rate
   self.obj323.rate.setValue(0.0)

   self.obj323.GGLabel.setValue(3)
   self.obj323.graphClass_= graph_achieve
   if self.genGraphics:
      new_obj = graph_achieve(133.5,123.5,self.obj323)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj323.graphObject_ = new_obj
   self.obj3230= AttrCalc()
   self.obj3230.Copy=ATOM3Boolean()
   self.obj3230.Copy.setValue(('Copy from LHS', 1))
   self.obj3230.Copy.config = 0
   self.obj3230.Specify=ATOM3Constraint()
   self.obj3230.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj323.GGset2Any['rate']= self.obj3230

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj323)
   self.obj323.postAction( cobj0.RHS.CREATE )

   self.obj324=operatingUnit(self)
   self.obj324.preAction( cobj0.RHS.CREATE )
   self.obj324.isGraphObjectVisual = True

   if(hasattr(self.obj324, '_setHierarchicalLink')):
     self.obj324._setHierarchicalLink(False)

   # name
   self.obj324.name.setValue('')
   self.obj324.name.setNone()

   self.obj324.GGLabel.setValue(5)
   self.obj324.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(280.0,120.0,self.obj324)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj324.graphObject_ = new_obj
   self.obj3240= AttrCalc()
   self.obj3240.Copy=ATOM3Boolean()
   self.obj3240.Copy.setValue(('Copy from LHS', 1))
   self.obj3240.Copy.config = 0
   self.obj3240.Specify=ATOM3Constraint()
   self.obj3240.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj324.GGset2Any['name']= self.obj3240

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj324)
   self.obj324.postAction( cobj0.RHS.CREATE )

   self.obj325=metarial(self)
   self.obj325.preAction( cobj0.RHS.CREATE )
   self.obj325.isGraphObjectVisual = True

   if(hasattr(self.obj325, '_setHierarchicalLink')):
     self.obj325._setHierarchicalLink(False)

   # Name
   self.obj325.Name.setValue('')
   self.obj325.Name.setNone()

   self.obj325.GGLabel.setValue(4)
   self.obj325.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(280.0,40.0,self.obj325)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj325.graphObject_ = new_obj
   self.obj3250= AttrCalc()
   self.obj3250.Copy=ATOM3Boolean()
   self.obj3250.Copy.setValue(('Copy from LHS', 1))
   self.obj3250.Copy.config = 0
   self.obj3250.Specify=ATOM3Constraint()
   self.obj3250.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj325.GGset2Any['Name']= self.obj3250

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj325)
   self.obj325.postAction( cobj0.RHS.CREATE )

   self.obj326=metarial(self)
   self.obj326.preAction( cobj0.RHS.CREATE )
   self.obj326.isGraphObjectVisual = True

   if(hasattr(self.obj326, '_setHierarchicalLink')):
     self.obj326._setHierarchicalLink(False)

   # Name
   self.obj326.Name.setValue('')
   self.obj326.Name.setNone()

   self.obj326.GGLabel.setValue(6)
   self.obj326.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(280.0,200.0,self.obj326)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj326.graphObject_ = new_obj
   self.obj3260= AttrCalc()
   self.obj3260.Copy=ATOM3Boolean()
   self.obj3260.Copy.setValue(('Copy from LHS', 1))
   self.obj3260.Copy.config = 0
   self.obj3260.Specify=ATOM3Constraint()
   self.obj3260.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj326.GGset2Any['Name']= self.obj3260

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj326)
   self.obj326.postAction( cobj0.RHS.CREATE )

   self.obj327=fromMaterial(self)
   self.obj327.preAction( cobj0.RHS.CREATE )
   self.obj327.isGraphObjectVisual = True

   if(hasattr(self.obj327, '_setHierarchicalLink')):
     self.obj327._setHierarchicalLink(False)

   # rate
   self.obj327.rate.setValue(0.0)

   self.obj327.GGLabel.setValue(8)
   self.obj327.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(298.785046729,109.210526316,self.obj327)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj327.graphObject_ = new_obj
   self.obj3270= AttrCalc()
   self.obj3270.Copy=ATOM3Boolean()
   self.obj3270.Copy.setValue(('Copy from LHS', 1))
   self.obj3270.Copy.config = 0
   self.obj3270.Specify=ATOM3Constraint()
   self.obj3270.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj327.GGset2Any['rate']= self.obj3270

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj327)
   self.obj327.postAction( cobj0.RHS.CREATE )

   self.obj328=intoMaterial(self)
   self.obj328.preAction( cobj0.RHS.CREATE )
   self.obj328.isGraphObjectVisual = True

   if(hasattr(self.obj328, '_setHierarchicalLink')):
     self.obj328._setHierarchicalLink(False)

   # rate
   self.obj328.rate.setValue(0.0)

   self.obj328.GGLabel.setValue(10)
   self.obj328.graphClass_= graph_intoMaterial
   if self.genGraphics:
      new_obj = graph_intoMaterial(301.093457944,168.263157895,self.obj328)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj328.graphObject_ = new_obj
   self.obj3280= AttrCalc()
   self.obj3280.Copy=ATOM3Boolean()
   self.obj3280.Copy.setValue(('Copy from LHS', 0))
   self.obj3280.Copy.config = 0
   self.obj3280.Specify=ATOM3Constraint()
   self.obj3280.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(3)).rate.getValue()\n\n\n\n'))
   self.obj328.GGset2Any['rate']= self.obj3280

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj328)
   self.obj328.postAction( cobj0.RHS.CREATE )

   self.obj329=GenericGraphEdge(self)
   self.obj329.preAction( cobj0.RHS.CREATE )
   self.obj329.isGraphObjectVisual = True

   if(hasattr(self.obj329, '_setHierarchicalLink')):
     self.obj329._setHierarchicalLink(False)

   self.obj329.GGLabel.setValue(7)
   self.obj329.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(208.0,43.0,self.obj329)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj329.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj329)
   self.obj329.postAction( cobj0.RHS.CREATE )

   self.obj330=GenericGraphEdge(self)
   self.obj330.preAction( cobj0.RHS.CREATE )
   self.obj330.isGraphObjectVisual = True

   if(hasattr(self.obj330, '_setHierarchicalLink')):
     self.obj330._setHierarchicalLink(False)

   self.obj330.GGLabel.setValue(9)
   self.obj330.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(223.0,207.5,self.obj330)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj330.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj330)
   self.obj330.postAction( cobj0.RHS.CREATE )

   self.obj321.out_connections_.append(self.obj323)
   self.obj323.in_connections_.append(self.obj321)
   self.obj321.graphObject_.pendingConnections.append((self.obj321.graphObject_.tag, self.obj323.graphObject_.tag, [124.0, 86.0, 133.5, 123.5], 0, True))
   self.obj321.out_connections_.append(self.obj329)
   self.obj329.in_connections_.append(self.obj321)
   self.obj321.graphObject_.pendingConnections.append((self.obj321.graphObject_.tag, self.obj329.graphObject_.tag, [124.0, 41.0, 208.0, 43.0], 0, True))
   self.obj322.out_connections_.append(self.obj330)
   self.obj330.in_connections_.append(self.obj322)
   self.obj322.graphObject_.pendingConnections.append((self.obj322.graphObject_.tag, self.obj330.graphObject_.tag, [154.0, 210.0, 223.0, 207.5], 0, True))
   self.obj323.out_connections_.append(self.obj322)
   self.obj322.in_connections_.append(self.obj323)
   self.obj323.graphObject_.pendingConnections.append((self.obj323.graphObject_.tag, self.obj322.graphObject_.tag, [143.0, 161.0, 133.5, 123.5], 0, True))
   self.obj324.out_connections_.append(self.obj328)
   self.obj328.in_connections_.append(self.obj324)
   self.obj324.graphObject_.pendingConnections.append((self.obj324.graphObject_.tag, self.obj328.graphObject_.tag, [295.1869158878505, 135.5263157894737, 301.0934579439253, 168.26315789473685], 0, True))
   self.obj325.out_connections_.append(self.obj327)
   self.obj327.in_connections_.append(self.obj325)
   self.obj325.graphObject_.pendingConnections.append((self.obj325.graphObject_.tag, self.obj327.graphObject_.tag, [304.0, 90.0, 298.78504672897196, 109.21052631578948], 0, True))
   self.obj327.out_connections_.append(self.obj324)
   self.obj324.in_connections_.append(self.obj327)
   self.obj327.graphObject_.pendingConnections.append((self.obj327.graphObject_.tag, self.obj324.graphObject_.tag, [293.5700934579439, 128.42105263157896, 298.78504672897196, 109.21052631578948], 0, True))
   self.obj328.out_connections_.append(self.obj326)
   self.obj326.in_connections_.append(self.obj328)
   self.obj328.graphObject_.pendingConnections.append((self.obj328.graphObject_.tag, self.obj326.graphObject_.tag, [307.0, 201.0, 301.0934579439253, 168.26315789473685], 0, True))
   self.obj329.out_connections_.append(self.obj325)
   self.obj325.in_connections_.append(self.obj329)
   self.obj329.graphObject_.pendingConnections.append((self.obj329.graphObject_.tag, self.obj325.graphObject_.tag, [292.0, 45.0, 208.0, 43.0], 0, True))
   self.obj330.out_connections_.append(self.obj326)
   self.obj326.in_connections_.append(self.obj330)
   self.obj330.graphObject_.pendingConnections.append((self.obj330.graphObject_.tag, self.obj326.graphObject_.tag, [292.0, 205.0, 223.0, 207.5], 2, 0))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'print \'======> Link Aux Condition\'# _ Agent2Raw_GG_rule.py _\naRg = self.getMatched ( graphID , self.LHS.nodeWithLabel(4) )\nnameARG = aRg.Name.getValue()\ng = self.getMatched ( graphID , self.LHS.nodeWithLabel(6) )\n# test if nameARG  end with name of Goal \nprint  nameARG +\' END WITH \'+g.Name.getValue()\nprint nameARG.endswith( g.Name.getValue() )\nif nameARG.endswith( g.Name.getValue() ) and not hasattr(aRg,\'LinkAux\'): \n return True\nelse : \n return False\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'print \'======> Link Aux Action\'\naRg = self.getMatched ( graphID , self.LHS.nodeWithLabel(4) )\naRg.LinkAux = True \n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('CreateLinkAR2Mat', 20)
   cobj0.Order=ATOM3Integer(20)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

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

   cobj0.LHS = ASG_omacss(self)
   cobj0.LHS.merge(ASG_pns2(self))
   cobj0.LHS.merge(ASG_GenericGraph(self))

   self.obj337=Agent(self)
   self.obj337.preAction( cobj0.LHS.CREATE )
   self.obj337.isGraphObjectVisual = True

   if(hasattr(self.obj337, '_setHierarchicalLink')):
     self.obj337._setHierarchicalLink(False)

   # price
   self.obj337.price.setNone()

   # name
   self.obj337.name.setValue('')
   self.obj337.name.setNone()

   self.obj337.GGLabel.setValue(1)
   self.obj337.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(40.0,20.0,self.obj337)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj337.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj337)
   self.obj337.postAction( cobj0.LHS.CREATE )

   self.obj338=Role(self)
   self.obj338.preAction( cobj0.LHS.CREATE )
   self.obj338.isGraphObjectVisual = True

   if(hasattr(self.obj338, '_setHierarchicalLink')):
     self.obj338._setHierarchicalLink(False)

   # name
   self.obj338.name.setValue('')
   self.obj338.name.setNone()

   self.obj338.GGLabel.setValue(2)
   self.obj338.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(60.0,140.0,self.obj338)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj338.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj338)
   self.obj338.postAction( cobj0.LHS.CREATE )

   self.obj339=CapableOf(self)
   self.obj339.preAction( cobj0.LHS.CREATE )
   self.obj339.isGraphObjectVisual = True

   if(hasattr(self.obj339, '_setHierarchicalLink')):
     self.obj339._setHierarchicalLink(False)

   self.obj339.GGLabel.setValue(3)
   self.obj339.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(74.5,111.5,self.obj339)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj339.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj339)
   self.obj339.postAction( cobj0.LHS.CREATE )

   self.obj340=rawMaterial(self)
   self.obj340.preAction( cobj0.LHS.CREATE )
   self.obj340.isGraphObjectVisual = True

   if(hasattr(self.obj340, '_setHierarchicalLink')):
     self.obj340._setHierarchicalLink(False)

   # Name
   self.obj340.Name.setValue('')
   self.obj340.Name.setNone()

   self.obj340.GGLabel.setValue(6)
   self.obj340.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(240.0,20.0,self.obj340)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj340.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj340)
   self.obj340.postAction( cobj0.LHS.CREATE )

   self.obj341=operatingUnit(self)
   self.obj341.preAction( cobj0.LHS.CREATE )
   self.obj341.isGraphObjectVisual = True

   if(hasattr(self.obj341, '_setHierarchicalLink')):
     self.obj341._setHierarchicalLink(False)

   # name
   self.obj341.name.setValue('')
   self.obj341.name.setNone()

   self.obj341.GGLabel.setValue(12)
   self.obj341.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(320.0,240.0,self.obj341)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj341.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj341)
   self.obj341.postAction( cobj0.LHS.CREATE )

   self.obj342=operatingUnit(self)
   self.obj342.preAction( cobj0.LHS.CREATE )
   self.obj342.isGraphObjectVisual = True

   if(hasattr(self.obj342, '_setHierarchicalLink')):
     self.obj342._setHierarchicalLink(False)

   # name
   self.obj342.name.setValue('')
   self.obj342.name.setNone()

   self.obj342.GGLabel.setValue(7)
   self.obj342.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(320.0,100.0,self.obj342)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj342.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj342)
   self.obj342.postAction( cobj0.LHS.CREATE )

   self.obj343=metarial(self)
   self.obj343.preAction( cobj0.LHS.CREATE )
   self.obj343.isGraphObjectVisual = True

   if(hasattr(self.obj343, '_setHierarchicalLink')):
     self.obj343._setHierarchicalLink(False)

   # Name
   self.obj343.Name.setValue('')
   self.obj343.Name.setNone()

   self.obj343.GGLabel.setValue(11)
   self.obj343.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(240.0,160.0,self.obj343)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj343.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj343)
   self.obj343.postAction( cobj0.LHS.CREATE )

   self.obj344=fromMaterial(self)
   self.obj344.preAction( cobj0.LHS.CREATE )
   self.obj344.isGraphObjectVisual = True

   if(hasattr(self.obj344, '_setHierarchicalLink')):
     self.obj344._setHierarchicalLink(False)

   # rate
   self.obj344.rate.setNone()

   self.obj344.GGLabel.setValue(14)
   self.obj344.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(340.0,197.0,self.obj344)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj344.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj344)
   self.obj344.postAction( cobj0.LHS.CREATE )

   self.obj345=fromRaw(self)
   self.obj345.preAction( cobj0.LHS.CREATE )
   self.obj345.isGraphObjectVisual = True

   if(hasattr(self.obj345, '_setHierarchicalLink')):
     self.obj345._setHierarchicalLink(False)

   # rate
   self.obj345.rate.setNone()

   self.obj345.GGLabel.setValue(9)
   self.obj345.graphClass_= graph_fromRaw
   if self.genGraphics:
      new_obj = graph_fromRaw(329.081775701,37.1184210526,self.obj345)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj345.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj345)
   self.obj345.postAction( cobj0.LHS.CREATE )

   self.obj346=GenericGraphEdge(self)
   self.obj346.preAction( cobj0.LHS.CREATE )
   self.obj346.isGraphObjectVisual = True

   if(hasattr(self.obj346, '_setHierarchicalLink')):
     self.obj346._setHierarchicalLink(False)

   self.obj346.GGLabel.setValue(13)
   self.obj346.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(167.0,195.0,self.obj346)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj346.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj346)
   self.obj346.postAction( cobj0.LHS.CREATE )

   self.obj347=GenericGraphEdge(self)
   self.obj347.preAction( cobj0.LHS.CREATE )
   self.obj347.isGraphObjectVisual = True

   if(hasattr(self.obj347, '_setHierarchicalLink')):
     self.obj347._setHierarchicalLink(False)

   self.obj347.GGLabel.setValue(10)
   self.obj347.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(288.198598131,95.0,self.obj347)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj347.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj347)
   self.obj347.postAction( cobj0.LHS.CREATE )

   self.obj348=GenericGraphEdge(self)
   self.obj348.preAction( cobj0.LHS.CREATE )
   self.obj348.isGraphObjectVisual = True

   if(hasattr(self.obj348, '_setHierarchicalLink')):
     self.obj348._setHierarchicalLink(False)

   self.obj348.GGLabel.setValue(15)
   self.obj348.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(170.5,76.0,self.obj348)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj348.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj348)
   self.obj348.postAction( cobj0.LHS.CREATE )

   self.obj337.out_connections_.append(self.obj339)
   self.obj339.in_connections_.append(self.obj337)
   self.obj337.graphObject_.pendingConnections.append((self.obj337.graphObject_.tag, self.obj339.graphObject_.tag, [65.0, 82.0, 74.5, 111.5], 0, True))
   self.obj337.out_connections_.append(self.obj347)
   self.obj347.in_connections_.append(self.obj337)
   self.obj337.graphObject_.pendingConnections.append((self.obj337.graphObject_.tag, self.obj347.graphObject_.tag, [77.0, 82.0, 216.5, 96.5, 288.1985981308411, 95.0], 2, True))
   self.obj337.out_connections_.append(self.obj348)
   self.obj348.in_connections_.append(self.obj337)
   self.obj337.graphObject_.pendingConnections.append((self.obj337.graphObject_.tag, self.obj348.graphObject_.tag, [77.0, 82.0, 170.5, 76.0], 0, True))
   self.obj338.out_connections_.append(self.obj346)
   self.obj346.in_connections_.append(self.obj338)
   self.obj338.graphObject_.pendingConnections.append((self.obj338.graphObject_.tag, self.obj346.graphObject_.tag, [84.0, 186.0, 167.0, 195.0], 0, True))
   self.obj339.out_connections_.append(self.obj338)
   self.obj338.in_connections_.append(self.obj339)
   self.obj339.graphObject_.pendingConnections.append((self.obj339.graphObject_.tag, self.obj338.graphObject_.tag, [91.0, 140.0, 74.5, 111.5], 2, 0))
   self.obj340.out_connections_.append(self.obj345)
   self.obj345.in_connections_.append(self.obj340)
   self.obj340.graphObject_.pendingConnections.append((self.obj340.graphObject_.tag, self.obj345.graphObject_.tag, [264.0, 73.0, 299.5, 33.5, 329.0817757009346, 37.118421052631575], 2, True))
   self.obj343.out_connections_.append(self.obj344)
   self.obj344.in_connections_.append(self.obj343)
   self.obj343.graphObject_.pendingConnections.append((self.obj343.graphObject_.tag, self.obj344.graphObject_.tag, [281.0, 167.0, 372.0, 226.0, 328.0, 153.0], 2, True))
   self.obj344.out_connections_.append(self.obj341)
   self.obj341.in_connections_.append(self.obj344)
   self.obj344.graphObject_.pendingConnections.append((self.obj344.graphObject_.tag, self.obj341.graphObject_.tag, [333.5700934579439, 248.42105263157896, 296.0, 124.0, 328.0, 153.0], 2, True))
   self.obj345.out_connections_.append(self.obj342)
   self.obj342.in_connections_.append(self.obj345)
   self.obj345.graphObject_.pendingConnections.append((self.obj345.graphObject_.tag, self.obj342.graphObject_.tag, [362.32710280373834, 107.47368421052629, 358.6635514018692, 40.73684210526314, 329.0817757009346, 37.118421052631575], 2, True))
   self.obj346.out_connections_.append(self.obj343)
   self.obj343.in_connections_.append(self.obj346)
   self.obj346.graphObject_.pendingConnections.append((self.obj346.graphObject_.tag, self.obj343.graphObject_.tag, [250.0, 204.0, 167.0, 195.0], 2, 0))
   self.obj347.out_connections_.append(self.obj342)
   self.obj342.in_connections_.append(self.obj347)
   self.obj347.graphObject_.pendingConnections.append((self.obj347.graphObject_.tag, self.obj342.graphObject_.tag, [335.1869158878505, 115.5263157894737, 288.198598131, 95.0], 2, 0))
   self.obj348.out_connections_.append(self.obj340)
   self.obj340.in_connections_.append(self.obj348)
   self.obj348.graphObject_.pendingConnections.append((self.obj348.graphObject_.tag, self.obj340.graphObject_.tag, [264.0, 70.0, 170.5, 76.0], 2, 0))

   cobj0.RHS = ASG_omacss(self)
   cobj0.RHS.merge(ASG_pns2(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj352=Agent(self)
   self.obj352.preAction( cobj0.RHS.CREATE )
   self.obj352.isGraphObjectVisual = True

   if(hasattr(self.obj352, '_setHierarchicalLink')):
     self.obj352._setHierarchicalLink(False)

   # price
   self.obj352.price.setValue(0)

   # name
   self.obj352.name.setValue('')
   self.obj352.name.setNone()

   self.obj352.GGLabel.setValue(1)
   self.obj352.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(60.0,20.0,self.obj352)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj352.graphObject_ = new_obj
   self.obj3520= AttrCalc()
   self.obj3520.Copy=ATOM3Boolean()
   self.obj3520.Copy.setValue(('Copy from LHS', 1))
   self.obj3520.Copy.config = 0
   self.obj3520.Specify=ATOM3Constraint()
   self.obj3520.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj352.GGset2Any['price']= self.obj3520
   self.obj3521= AttrCalc()
   self.obj3521.Copy=ATOM3Boolean()
   self.obj3521.Copy.setValue(('Copy from LHS', 1))
   self.obj3521.Copy.config = 0
   self.obj3521.Specify=ATOM3Constraint()
   self.obj3521.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj352.GGset2Any['name']= self.obj3521

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj352)
   self.obj352.postAction( cobj0.RHS.CREATE )

   self.obj353=Role(self)
   self.obj353.preAction( cobj0.RHS.CREATE )
   self.obj353.isGraphObjectVisual = True

   if(hasattr(self.obj353, '_setHierarchicalLink')):
     self.obj353._setHierarchicalLink(False)

   # name
   self.obj353.name.setValue('')
   self.obj353.name.setNone()

   self.obj353.GGLabel.setValue(2)
   self.obj353.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(80.0,160.0,self.obj353)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj353.graphObject_ = new_obj
   self.obj3530= AttrCalc()
   self.obj3530.Copy=ATOM3Boolean()
   self.obj3530.Copy.setValue(('Copy from LHS', 1))
   self.obj3530.Copy.config = 0
   self.obj3530.Specify=ATOM3Constraint()
   self.obj3530.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj353.GGset2Any['name']= self.obj3530

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj353)
   self.obj353.postAction( cobj0.RHS.CREATE )

   self.obj354=CapableOf(self)
   self.obj354.preAction( cobj0.RHS.CREATE )
   self.obj354.isGraphObjectVisual = True

   if(hasattr(self.obj354, '_setHierarchicalLink')):
     self.obj354._setHierarchicalLink(False)

   self.obj354.GGLabel.setValue(3)
   self.obj354.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(104.5,111.5,self.obj354)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj354.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj354)
   self.obj354.postAction( cobj0.RHS.CREATE )

   self.obj355=rawMaterial(self)
   self.obj355.preAction( cobj0.RHS.CREATE )
   self.obj355.isGraphObjectVisual = True

   if(hasattr(self.obj355, '_setHierarchicalLink')):
     self.obj355._setHierarchicalLink(False)

   # Name
   self.obj355.Name.setValue('')
   self.obj355.Name.setNone()

   self.obj355.GGLabel.setValue(6)
   self.obj355.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(300.0,20.0,self.obj355)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj355.graphObject_ = new_obj
   self.obj3550= AttrCalc()
   self.obj3550.Copy=ATOM3Boolean()
   self.obj3550.Copy.setValue(('Copy from LHS', 1))
   self.obj3550.Copy.config = 0
   self.obj3550.Specify=ATOM3Constraint()
   self.obj3550.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj355.GGset2Any['Name']= self.obj3550

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj355)
   self.obj355.postAction( cobj0.RHS.CREATE )

   self.obj356=operatingUnit(self)
   self.obj356.preAction( cobj0.RHS.CREATE )
   self.obj356.isGraphObjectVisual = True

   if(hasattr(self.obj356, '_setHierarchicalLink')):
     self.obj356._setHierarchicalLink(False)

   # name
   self.obj356.name.setValue('')
   self.obj356.name.setNone()

   self.obj356.GGLabel.setValue(7)
   self.obj356.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(300.0,100.0,self.obj356)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj356.graphObject_ = new_obj
   self.obj3560= AttrCalc()
   self.obj3560.Copy=ATOM3Boolean()
   self.obj3560.Copy.setValue(('Copy from LHS', 1))
   self.obj3560.Copy.config = 0
   self.obj3560.Specify=ATOM3Constraint()
   self.obj3560.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj356.GGset2Any['name']= self.obj3560

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj356)
   self.obj356.postAction( cobj0.RHS.CREATE )

   self.obj357=operatingUnit(self)
   self.obj357.preAction( cobj0.RHS.CREATE )
   self.obj357.isGraphObjectVisual = True

   if(hasattr(self.obj357, '_setHierarchicalLink')):
     self.obj357._setHierarchicalLink(False)

   # name
   self.obj357.name.setValue('')
   self.obj357.name.setNone()

   self.obj357.GGLabel.setValue(12)
   self.obj357.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(240.0,260.0,self.obj357)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj357.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj357)
   self.obj357.postAction( cobj0.RHS.CREATE )

   self.obj358=metarial(self)
   self.obj358.preAction( cobj0.RHS.CREATE )
   self.obj358.isGraphObjectVisual = True

   if(hasattr(self.obj358, '_setHierarchicalLink')):
     self.obj358._setHierarchicalLink(False)

   # Name
   self.obj358.Name.setValue('')
   self.obj358.Name.setNone()

   self.obj358.GGLabel.setValue(11)
   self.obj358.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(320.0,160.0,self.obj358)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj358.graphObject_ = new_obj
   self.obj3580= AttrCalc()
   self.obj3580.Copy=ATOM3Boolean()
   self.obj3580.Copy.setValue(('Copy from LHS', 1))
   self.obj3580.Copy.config = 0
   self.obj3580.Specify=ATOM3Constraint()
   self.obj3580.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj358.GGset2Any['Name']= self.obj3580

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj358)
   self.obj358.postAction( cobj0.RHS.CREATE )

   self.obj359=fromMaterial(self)
   self.obj359.preAction( cobj0.RHS.CREATE )
   self.obj359.isGraphObjectVisual = True

   if(hasattr(self.obj359, '_setHierarchicalLink')):
     self.obj359._setHierarchicalLink(False)

   # rate
   self.obj359.rate.setValue(0.0)

   self.obj359.GGLabel.setValue(14)
   self.obj359.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(317.285046729,218.710526316,self.obj359)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj359.graphObject_ = new_obj
   self.obj3590= AttrCalc()
   self.obj3590.Copy=ATOM3Boolean()
   self.obj3590.Copy.setValue(('Copy from LHS', 1))
   self.obj3590.Copy.config = 0
   self.obj3590.Specify=ATOM3Constraint()
   self.obj3590.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj359.GGset2Any['rate']= self.obj3590

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj359)
   self.obj359.postAction( cobj0.RHS.CREATE )

   self.obj360=fromRaw(self)
   self.obj360.preAction( cobj0.RHS.CREATE )
   self.obj360.isGraphObjectVisual = True

   if(hasattr(self.obj360, '_setHierarchicalLink')):
     self.obj360._setHierarchicalLink(False)

   # rate
   self.obj360.rate.setValue(0.0)

   self.obj360.GGLabel.setValue(9)
   self.obj360.graphClass_= graph_fromRaw
   if self.genGraphics:
      new_obj = graph_fromRaw(318.285046729,90.7105263158,self.obj360)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj360.graphObject_ = new_obj
   self.obj3600= AttrCalc()
   self.obj3600.Copy=ATOM3Boolean()
   self.obj3600.Copy.setValue(('Copy from LHS', 1))
   self.obj3600.Copy.config = 0
   self.obj3600.Specify=ATOM3Constraint()
   self.obj3600.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj360.GGset2Any['rate']= self.obj3600

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj360)
   self.obj360.postAction( cobj0.RHS.CREATE )

   self.obj361=intoMaterial(self)
   self.obj361.preAction( cobj0.RHS.CREATE )
   self.obj361.isGraphObjectVisual = True

   if(hasattr(self.obj361, '_setHierarchicalLink')):
     self.obj361._setHierarchicalLink(False)

   # rate
   self.obj361.rate.setValue(16.16)

   self.obj361.GGLabel.setValue(16)
   self.obj361.graphClass_= graph_intoMaterial
   if self.genGraphics:
      new_obj = graph_intoMaterial(322.093457944,135.263157895,self.obj361)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj361.graphObject_ = new_obj
   self.obj3610= AttrCalc()
   self.obj3610.Copy=ATOM3Boolean()
   self.obj3610.Copy.setValue(('Copy from LHS', 0))
   self.obj3610.Copy.config = 0
   self.obj3610.Specify=ATOM3Constraint()
   self.obj3610.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return 16.16\n\n\n\n\n\n\n\n\n\n\n\n\n'))
   self.obj361.GGset2Any['rate']= self.obj3610

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj361)
   self.obj361.postAction( cobj0.RHS.CREATE )

   self.obj362=GenericGraphEdge(self)
   self.obj362.preAction( cobj0.RHS.CREATE )
   self.obj362.isGraphObjectVisual = True

   if(hasattr(self.obj362, '_setHierarchicalLink')):
     self.obj362._setHierarchicalLink(False)

   self.obj362.GGLabel.setValue(10)
   self.obj362.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(199.285046729,85.2105263158,self.obj362)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj362.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj362)
   self.obj362.postAction( cobj0.RHS.CREATE )

   self.obj363=GenericGraphEdge(self)
   self.obj363.preAction( cobj0.RHS.CREATE )
   self.obj363.isGraphObjectVisual = True

   if(hasattr(self.obj363, '_setHierarchicalLink')):
     self.obj363._setHierarchicalLink(False)

   self.obj363.GGLabel.setValue(13)
   self.obj363.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(208.0,174.0,self.obj363)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj363.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj363)
   self.obj363.postAction( cobj0.RHS.CREATE )

   self.obj364=GenericGraphEdge(self)
   self.obj364.preAction( cobj0.RHS.CREATE )
   self.obj364.isGraphObjectVisual = True

   if(hasattr(self.obj364, '_setHierarchicalLink')):
     self.obj364._setHierarchicalLink(False)

   self.obj364.GGLabel.setValue(15)
   self.obj364.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(229.5,47.0,self.obj364)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj364.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj364)
   self.obj364.postAction( cobj0.RHS.CREATE )

   self.obj352.out_connections_.append(self.obj354)
   self.obj354.in_connections_.append(self.obj352)
   self.obj352.graphObject_.pendingConnections.append((self.obj352.graphObject_.tag, self.obj354.graphObject_.tag, [85.0, 82.0, 104.5, 111.5], 0, True))
   self.obj352.out_connections_.append(self.obj362)
   self.obj362.in_connections_.append(self.obj352)
   self.obj352.graphObject_.pendingConnections.append((self.obj352.graphObject_.tag, self.obj362.graphObject_.tag, [85.0, 82.0, 199.28504672897196, 85.21052631578948], 0, True))
   self.obj352.out_connections_.append(self.obj364)
   self.obj364.in_connections_.append(self.obj352)
   self.obj352.graphObject_.pendingConnections.append((self.obj352.graphObject_.tag, self.obj364.graphObject_.tag, [97.0, 82.0, 229.5, 47.0], 0, True))
   self.obj353.out_connections_.append(self.obj363)
   self.obj363.in_connections_.append(self.obj353)
   self.obj353.graphObject_.pendingConnections.append((self.obj353.graphObject_.tag, self.obj363.graphObject_.tag, [104.0, 161.0, 208.0, 174.0], 0, True))
   self.obj354.out_connections_.append(self.obj353)
   self.obj353.in_connections_.append(self.obj354)
   self.obj354.graphObject_.pendingConnections.append((self.obj354.graphObject_.tag, self.obj353.graphObject_.tag, [111.0, 160.0, 104.5, 111.5], 2, 0))
   self.obj355.out_connections_.append(self.obj360)
   self.obj360.in_connections_.append(self.obj355)
   self.obj355.graphObject_.pendingConnections.append((self.obj355.graphObject_.tag, self.obj360.graphObject_.tag, [324.0, 73.0, 318.28504672897196, 90.71052631578948], 0, True))
   self.obj356.out_connections_.append(self.obj361)
   self.obj361.in_connections_.append(self.obj356)
   self.obj356.graphObject_.pendingConnections.append((self.obj356.graphObject_.tag, self.obj361.graphObject_.tag, [315.1869158878505, 115.5263157894737, 322.0934579439253, 135.26315789473685], 0, True))
   self.obj358.out_connections_.append(self.obj359)
   self.obj359.in_connections_.append(self.obj358)
   self.obj358.graphObject_.pendingConnections.append((self.obj358.graphObject_.tag, self.obj359.graphObject_.tag, [357.0, 205.0, 317.28504672897196, 218.71052631578948], 0, True))
   self.obj359.out_connections_.append(self.obj357)
   self.obj357.in_connections_.append(self.obj359)
   self.obj359.graphObject_.pendingConnections.append((self.obj359.graphObject_.tag, self.obj357.graphObject_.tag, [253.57009345794393, 248.42105263157896, 315.28504672897196, 206.71052631578948], 0, True))
   self.obj360.out_connections_.append(self.obj356)
   self.obj356.in_connections_.append(self.obj360)
   self.obj360.graphObject_.pendingConnections.append((self.obj360.graphObject_.tag, self.obj356.graphObject_.tag, [314.5700934579439, 108.42105263157895, 319.28504672897196, 90.71052631578948], 0, True))
   self.obj361.out_connections_.append(self.obj358)
   self.obj358.in_connections_.append(self.obj361)
   self.obj361.graphObject_.pendingConnections.append((self.obj361.graphObject_.tag, self.obj358.graphObject_.tag, [347.0, 161.0, 311.0934579439253, 128.26315789473685], 0, True))
   self.obj362.out_connections_.append(self.obj356)
   self.obj356.in_connections_.append(self.obj362)
   self.obj362.graphObject_.pendingConnections.append((self.obj362.graphObject_.tag, self.obj356.graphObject_.tag, [314.5700934579439, 108.42105263157895, 199.285046729, 85.2105263158], 2, 0))
   self.obj363.out_connections_.append(self.obj358)
   self.obj358.in_connections_.append(self.obj363)
   self.obj363.graphObject_.pendingConnections.append((self.obj363.graphObject_.tag, self.obj358.graphObject_.tag, [332.0, 165.0, 208.0, 143.0], 2, 0))
   self.obj364.out_connections_.append(self.obj355)
   self.obj355.in_connections_.append(self.obj364)
   self.obj364.graphObject_.pendingConnections.append((self.obj364.graphObject_.tag, self.obj355.graphObject_.tag, [324.0, 70.0, 210.5, 76.0], 0, True))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\nnode7 = self.getMatched(graphID, self.LHS.nodeWithLabel(7))\n\nnode11 = self.getMatched(graphID, self.LHS.nodeWithLabel(11))\nnode1 = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\n\nprint node7.name.getValue()+\' in \'+ node11.Name.getValue() \nprint node7.name.getValue() in  node11.Name.getValue()\nprint \'Rule 20 \'\n\ntest = not ( hasattr(node11, "linkAux2") and hasattr(node7, "linkAux2") )\nprint test\nif test : \n return (node7.name.getValue() in node11.Name.getValue() )\nelse : \n return False\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# code action of rule\nnode = self.getMatched ( graphID , self.LHS.nodeWithLabel(7) )\nnode.linkAux2 = True \nnode = self.getMatched ( graphID , self.LHS.nodeWithLabel(11) )\nnode.linkAux2 = True \nself.graphRewritingSystem.finalStat = 21\n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('AssigneValuestoLinks1', 20)
   cobj0.Order=ATOM3Integer(22)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

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

   cobj0.LHS = ASG_omacss(self)
   cobj0.LHS.merge(ASG_pns2(self))
   cobj0.LHS.merge(ASG_GenericGraph(self))

   self.obj371=Agent(self)
   self.obj371.preAction( cobj0.LHS.CREATE )
   self.obj371.isGraphObjectVisual = True

   if(hasattr(self.obj371, '_setHierarchicalLink')):
     self.obj371._setHierarchicalLink(False)

   # price
   self.obj371.price.setNone()

   # name
   self.obj371.name.setValue('')
   self.obj371.name.setNone()

   self.obj371.GGLabel.setValue(1)
   self.obj371.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(100.0,20.0,self.obj371)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj371.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj371)
   self.obj371.postAction( cobj0.LHS.CREATE )

   self.obj372=Role(self)
   self.obj372.preAction( cobj0.LHS.CREATE )
   self.obj372.isGraphObjectVisual = True

   if(hasattr(self.obj372, '_setHierarchicalLink')):
     self.obj372._setHierarchicalLink(False)

   # name
   self.obj372.name.setValue('')
   self.obj372.name.setNone()

   self.obj372.GGLabel.setValue(2)
   self.obj372.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(60.0,160.0,self.obj372)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj372.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj372)
   self.obj372.postAction( cobj0.LHS.CREATE )

   self.obj373=rawMaterial(self)
   self.obj373.preAction( cobj0.LHS.CREATE )
   self.obj373.isGraphObjectVisual = True

   if(hasattr(self.obj373, '_setHierarchicalLink')):
     self.obj373._setHierarchicalLink(False)

   # Name
   self.obj373.Name.setValue('')
   self.obj373.Name.setNone()

   self.obj373.GGLabel.setValue(3)
   self.obj373.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(240.0,20.0,self.obj373)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj373.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj373)
   self.obj373.postAction( cobj0.LHS.CREATE )

   self.obj374=operatingUnit(self)
   self.obj374.preAction( cobj0.LHS.CREATE )
   self.obj374.isGraphObjectVisual = True

   if(hasattr(self.obj374, '_setHierarchicalLink')):
     self.obj374._setHierarchicalLink(False)

   # name
   self.obj374.name.setValue('')
   self.obj374.name.setNone()

   self.obj374.GGLabel.setValue(4)
   self.obj374.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(260.0,100.0,self.obj374)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj374.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj374)
   self.obj374.postAction( cobj0.LHS.CREATE )

   self.obj375=operatingUnit(self)
   self.obj375.preAction( cobj0.LHS.CREATE )
   self.obj375.isGraphObjectVisual = True

   if(hasattr(self.obj375, '_setHierarchicalLink')):
     self.obj375._setHierarchicalLink(False)

   # name
   self.obj375.name.setValue('')
   self.obj375.name.setNone()

   self.obj375.GGLabel.setValue(9)
   self.obj375.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(220.0,260.0,self.obj375)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj375.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj375)
   self.obj375.postAction( cobj0.LHS.CREATE )

   self.obj376=metarial(self)
   self.obj376.preAction( cobj0.LHS.CREATE )
   self.obj376.isGraphObjectVisual = True

   if(hasattr(self.obj376, '_setHierarchicalLink')):
     self.obj376._setHierarchicalLink(False)

   # Name
   self.obj376.Name.setValue('')
   self.obj376.Name.setNone()

   self.obj376.GGLabel.setValue(7)
   self.obj376.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(240.0,160.0,self.obj376)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj376.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj376)
   self.obj376.postAction( cobj0.LHS.CREATE )

   self.obj377=fromMaterial(self)
   self.obj377.preAction( cobj0.LHS.CREATE )
   self.obj377.isGraphObjectVisual = True

   if(hasattr(self.obj377, '_setHierarchicalLink')):
     self.obj377._setHierarchicalLink(False)

   # rate
   self.obj377.rate.setNone()

   self.obj377.GGLabel.setValue(10)
   self.obj377.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(262.663551402,238.736842105,self.obj377)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj377.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj377)
   self.obj377.postAction( cobj0.LHS.CREATE )

   self.obj378=fromRaw(self)
   self.obj378.preAction( cobj0.LHS.CREATE )
   self.obj378.isGraphObjectVisual = True

   if(hasattr(self.obj378, '_setHierarchicalLink')):
     self.obj378._setHierarchicalLink(False)

   # rate
   self.obj378.rate.setNone()

   self.obj378.GGLabel.setValue(5)
   self.obj378.graphClass_= graph_fromRaw
   if self.genGraphics:
      new_obj = graph_fromRaw(268.785046729,90.7105263158,self.obj378)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj378.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj378)
   self.obj378.postAction( cobj0.LHS.CREATE )

   self.obj379=intoMaterial(self)
   self.obj379.preAction( cobj0.LHS.CREATE )
   self.obj379.isGraphObjectVisual = True

   if(hasattr(self.obj379, '_setHierarchicalLink')):
     self.obj379._setHierarchicalLink(False)

   # rate
   self.obj379.rate.setNone()

   self.obj379.GGLabel.setValue(11)
   self.obj379.graphClass_= graph_intoMaterial
   if self.genGraphics:
      new_obj = graph_intoMaterial(271.093457944,138.263157895,self.obj379)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj379.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj379)
   self.obj379.postAction( cobj0.LHS.CREATE )

   self.obj380=GenericGraphEdge(self)
   self.obj380.preAction( cobj0.LHS.CREATE )
   self.obj380.isGraphObjectVisual = True

   if(hasattr(self.obj380, '_setHierarchicalLink')):
     self.obj380._setHierarchicalLink(False)

   self.obj380.GGLabel.setValue(6)
   self.obj380.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(194.5,77.5,self.obj380)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj380.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj380)
   self.obj380.postAction( cobj0.LHS.CREATE )

   self.obj381=GenericGraphEdge(self)
   self.obj381.preAction( cobj0.LHS.CREATE )
   self.obj381.isGraphObjectVisual = True

   if(hasattr(self.obj381, '_setHierarchicalLink')):
     self.obj381._setHierarchicalLink(False)

   self.obj381.GGLabel.setValue(8)
   self.obj381.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(168.0,163.0,self.obj381)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj381.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj381)
   self.obj381.postAction( cobj0.LHS.CREATE )

   self.obj382=GenericGraphEdge(self)
   self.obj382.preAction( cobj0.LHS.CREATE )
   self.obj382.isGraphObjectVisual = True

   if(hasattr(self.obj382, '_setHierarchicalLink')):
     self.obj382._setHierarchicalLink(False)

   self.obj382.GGLabel.setValue(12)
   self.obj382.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(205.785046729,95.2105263158,self.obj382)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj382.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj382)
   self.obj382.postAction( cobj0.LHS.CREATE )

   self.obj371.out_connections_.append(self.obj380)
   self.obj380.in_connections_.append(self.obj371)
   self.obj371.graphObject_.pendingConnections.append((self.obj371.graphObject_.tag, self.obj380.graphObject_.tag, [125.0, 82.0, 194.5, 77.5], 0, True))
   self.obj371.out_connections_.append(self.obj382)
   self.obj382.in_connections_.append(self.obj371)
   self.obj371.graphObject_.pendingConnections.append((self.obj371.graphObject_.tag, self.obj382.graphObject_.tag, [137.0, 82.0, 205.78504672897196, 95.21052631578948], 0, True))
   self.obj372.out_connections_.append(self.obj381)
   self.obj381.in_connections_.append(self.obj372)
   self.obj372.graphObject_.pendingConnections.append((self.obj372.graphObject_.tag, self.obj381.graphObject_.tag, [84.0, 161.0, 168.0, 163.0], 0, True))
   self.obj373.out_connections_.append(self.obj378)
   self.obj378.in_connections_.append(self.obj373)
   self.obj373.graphObject_.pendingConnections.append((self.obj373.graphObject_.tag, self.obj378.graphObject_.tag, [264.0, 73.0, 268.78504672897196, 90.71052631578948], 0, True))
   self.obj374.out_connections_.append(self.obj379)
   self.obj379.in_connections_.append(self.obj374)
   self.obj374.graphObject_.pendingConnections.append((self.obj374.graphObject_.tag, self.obj379.graphObject_.tag, [275.1869158878505, 115.5263157894737, 271.0934579439253, 138.26315789473685], 0, True))
   self.obj376.out_connections_.append(self.obj377)
   self.obj377.in_connections_.append(self.obj376)
   self.obj376.graphObject_.pendingConnections.append((self.obj376.graphObject_.tag, self.obj377.graphObject_.tag, [264.0, 210.0, 262.6635514018692, 238.73684210526315], 0, True))
   self.obj377.out_connections_.append(self.obj375)
   self.obj375.in_connections_.append(self.obj377)
   self.obj377.graphObject_.pendingConnections.append((self.obj377.graphObject_.tag, self.obj375.graphObject_.tag, [261.32710280373834, 267.4736842105263, 262.6635514018692, 238.73684210526315], 0, True))
   self.obj378.out_connections_.append(self.obj374)
   self.obj374.in_connections_.append(self.obj378)
   self.obj378.graphObject_.pendingConnections.append((self.obj378.graphObject_.tag, self.obj374.graphObject_.tag, [273.5700934579439, 108.42105263157895, 268.78504672897196, 90.71052631578948], 0, True))
   self.obj379.out_connections_.append(self.obj376)
   self.obj376.in_connections_.append(self.obj379)
   self.obj379.graphObject_.pendingConnections.append((self.obj379.graphObject_.tag, self.obj376.graphObject_.tag, [267.0, 161.0, 271.0934579439253, 138.26315789473685], 0, True))
   self.obj380.out_connections_.append(self.obj373)
   self.obj373.in_connections_.append(self.obj380)
   self.obj380.graphObject_.pendingConnections.append((self.obj380.graphObject_.tag, self.obj373.graphObject_.tag, [264.0, 73.0, 194.5, 77.5], 0, True))
   self.obj381.out_connections_.append(self.obj376)
   self.obj376.in_connections_.append(self.obj381)
   self.obj381.graphObject_.pendingConnections.append((self.obj381.graphObject_.tag, self.obj376.graphObject_.tag, [252.0, 165.0, 168.0, 163.0], 0, True))
   self.obj382.out_connections_.append(self.obj374)
   self.obj374.in_connections_.append(self.obj382)
   self.obj382.graphObject_.pendingConnections.append((self.obj382.graphObject_.tag, self.obj374.graphObject_.tag, [274.5700934579439, 108.42105263157895, 205.78504672897196, 95.21052631578948], 0, True))

   cobj0.RHS = ASG_omacss(self)
   cobj0.RHS.merge(ASG_pns2(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj386=Agent(self)
   self.obj386.preAction( cobj0.RHS.CREATE )
   self.obj386.isGraphObjectVisual = True

   if(hasattr(self.obj386, '_setHierarchicalLink')):
     self.obj386._setHierarchicalLink(False)

   # price
   self.obj386.price.setValue(0)

   # name
   self.obj386.name.setValue('')
   self.obj386.name.setNone()

   self.obj386.GGLabel.setValue(1)
   self.obj386.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(40.0,40.0,self.obj386)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj386.graphObject_ = new_obj
   self.obj3860= AttrCalc()
   self.obj3860.Copy=ATOM3Boolean()
   self.obj3860.Copy.setValue(('Copy from LHS', 1))
   self.obj3860.Copy.config = 0
   self.obj3860.Specify=ATOM3Constraint()
   self.obj3860.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj386.GGset2Any['price']= self.obj3860
   self.obj3861= AttrCalc()
   self.obj3861.Copy=ATOM3Boolean()
   self.obj3861.Copy.setValue(('Copy from LHS', 1))
   self.obj3861.Copy.config = 0
   self.obj3861.Specify=ATOM3Constraint()
   self.obj3861.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj386.GGset2Any['name']= self.obj3861

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj386)
   self.obj386.postAction( cobj0.RHS.CREATE )

   self.obj387=Role(self)
   self.obj387.preAction( cobj0.RHS.CREATE )
   self.obj387.isGraphObjectVisual = True

   if(hasattr(self.obj387, '_setHierarchicalLink')):
     self.obj387._setHierarchicalLink(False)

   # name
   self.obj387.name.setValue('')
   self.obj387.name.setNone()

   self.obj387.GGLabel.setValue(2)
   self.obj387.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(20.0,180.0,self.obj387)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj387.graphObject_ = new_obj
   self.obj3870= AttrCalc()
   self.obj3870.Copy=ATOM3Boolean()
   self.obj3870.Copy.setValue(('Copy from LHS', 1))
   self.obj3870.Copy.config = 0
   self.obj3870.Specify=ATOM3Constraint()
   self.obj3870.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj387.GGset2Any['name']= self.obj3870

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj387)
   self.obj387.postAction( cobj0.RHS.CREATE )

   self.obj388=rawMaterial(self)
   self.obj388.preAction( cobj0.RHS.CREATE )
   self.obj388.isGraphObjectVisual = True

   if(hasattr(self.obj388, '_setHierarchicalLink')):
     self.obj388._setHierarchicalLink(False)

   # Name
   self.obj388.Name.setValue('')
   self.obj388.Name.setNone()

   self.obj388.GGLabel.setValue(3)
   self.obj388.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(200.0,20.0,self.obj388)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj388.graphObject_ = new_obj
   self.obj3880= AttrCalc()
   self.obj3880.Copy=ATOM3Boolean()
   self.obj3880.Copy.setValue(('Copy from LHS', 1))
   self.obj3880.Copy.config = 0
   self.obj3880.Specify=ATOM3Constraint()
   self.obj3880.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj388.GGset2Any['Name']= self.obj3880

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj388)
   self.obj388.postAction( cobj0.RHS.CREATE )

   self.obj389=operatingUnit(self)
   self.obj389.preAction( cobj0.RHS.CREATE )
   self.obj389.isGraphObjectVisual = True

   if(hasattr(self.obj389, '_setHierarchicalLink')):
     self.obj389._setHierarchicalLink(False)

   # name
   self.obj389.name.setValue('')
   self.obj389.name.setNone()

   self.obj389.GGLabel.setValue(4)
   self.obj389.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(200.0,100.0,self.obj389)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj389.graphObject_ = new_obj
   self.obj3890= AttrCalc()
   self.obj3890.Copy=ATOM3Boolean()
   self.obj3890.Copy.setValue(('Copy from LHS', 1))
   self.obj3890.Copy.config = 0
   self.obj3890.Specify=ATOM3Constraint()
   self.obj3890.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj389.GGset2Any['name']= self.obj3890

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj389)
   self.obj389.postAction( cobj0.RHS.CREATE )

   self.obj390=operatingUnit(self)
   self.obj390.preAction( cobj0.RHS.CREATE )
   self.obj390.isGraphObjectVisual = True

   if(hasattr(self.obj390, '_setHierarchicalLink')):
     self.obj390._setHierarchicalLink(False)

   # name
   self.obj390.name.setValue('')
   self.obj390.name.setNone()

   self.obj390.GGLabel.setValue(9)
   self.obj390.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(220.0,260.0,self.obj390)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj390.graphObject_ = new_obj
   self.obj3900= AttrCalc()
   self.obj3900.Copy=ATOM3Boolean()
   self.obj3900.Copy.setValue(('Copy from LHS', 1))
   self.obj3900.Copy.config = 0
   self.obj3900.Specify=ATOM3Constraint()
   self.obj3900.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj390.GGset2Any['name']= self.obj3900

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj390)
   self.obj390.postAction( cobj0.RHS.CREATE )

   self.obj391=metarial(self)
   self.obj391.preAction( cobj0.RHS.CREATE )
   self.obj391.isGraphObjectVisual = True

   if(hasattr(self.obj391, '_setHierarchicalLink')):
     self.obj391._setHierarchicalLink(False)

   # Name
   self.obj391.Name.setValue('')
   self.obj391.Name.setNone()

   self.obj391.GGLabel.setValue(7)
   self.obj391.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(200.0,180.0,self.obj391)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj391.graphObject_ = new_obj
   self.obj3910= AttrCalc()
   self.obj3910.Copy=ATOM3Boolean()
   self.obj3910.Copy.setValue(('Copy from LHS', 1))
   self.obj3910.Copy.config = 0
   self.obj3910.Specify=ATOM3Constraint()
   self.obj3910.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj391.GGset2Any['Name']= self.obj3910

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj391)
   self.obj391.postAction( cobj0.RHS.CREATE )

   self.obj392=fromMaterial(self)
   self.obj392.preAction( cobj0.RHS.CREATE )
   self.obj392.isGraphObjectVisual = True

   if(hasattr(self.obj392, '_setHierarchicalLink')):
     self.obj392._setHierarchicalLink(False)

   # rate
   self.obj392.rate.setValue(0.0)

   self.obj392.GGLabel.setValue(10)
   self.obj392.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(228.785046729,249.210526316,self.obj392)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj392.graphObject_ = new_obj
   self.obj3920= AttrCalc()
   self.obj3920.Copy=ATOM3Boolean()
   self.obj3920.Copy.setValue(('Copy from LHS', 1))
   self.obj3920.Copy.config = 0
   self.obj3920.Specify=ATOM3Constraint()
   self.obj3920.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj392.GGset2Any['rate']= self.obj3920

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj392)
   self.obj392.postAction( cobj0.RHS.CREATE )

   self.obj393=fromRaw(self)
   self.obj393.preAction( cobj0.RHS.CREATE )
   self.obj393.isGraphObjectVisual = True

   if(hasattr(self.obj393, '_setHierarchicalLink')):
     self.obj393._setHierarchicalLink(False)

   # rate
   self.obj393.rate.setValue(0.0)

   self.obj393.GGLabel.setValue(5)
   self.obj393.graphClass_= graph_fromRaw
   if self.genGraphics:
      new_obj = graph_fromRaw(218.785046729,90.7105263158,self.obj393)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj393.graphObject_ = new_obj
   self.obj3930= AttrCalc()
   self.obj3930.Copy=ATOM3Boolean()
   self.obj3930.Copy.setValue(('Copy from LHS', 1))
   self.obj3930.Copy.config = 0
   self.obj3930.Specify=ATOM3Constraint()
   self.obj3930.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj393.GGset2Any['rate']= self.obj3930

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj393)
   self.obj393.postAction( cobj0.RHS.CREATE )

   self.obj394=intoMaterial(self)
   self.obj394.preAction( cobj0.RHS.CREATE )
   self.obj394.isGraphObjectVisual = True

   if(hasattr(self.obj394, '_setHierarchicalLink')):
     self.obj394._setHierarchicalLink(False)

   # rate
   self.obj394.rate.setValue(0.0)

   self.obj394.GGLabel.setValue(11)
   self.obj394.graphClass_= graph_intoMaterial
   if self.genGraphics:
      new_obj = graph_intoMaterial(220.593457944,148.263157895,self.obj394)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj394.graphObject_ = new_obj
   self.obj3940= AttrCalc()
   self.obj3940.Copy=ATOM3Boolean()
   self.obj3940.Copy.setValue(('Copy from LHS', 0))
   self.obj3940.Copy.config = 0
   self.obj3940.Specify=ATOM3Constraint()
   self.obj3940.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.graphRewritingSystem.Dictag[ self.getMatched ( graphID , self.LHS.nodeWithLabel(1) ).name.getValue() ]\n\n\n\n\n\n\n\n\n\n'))
   self.obj394.GGset2Any['rate']= self.obj3940

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj394)
   self.obj394.postAction( cobj0.RHS.CREATE )

   self.obj395=GenericGraphEdge(self)
   self.obj395.preAction( cobj0.RHS.CREATE )
   self.obj395.isGraphObjectVisual = True

   if(hasattr(self.obj395, '_setHierarchicalLink')):
     self.obj395._setHierarchicalLink(False)

   self.obj395.GGLabel.setValue(6)
   self.obj395.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(144.5,87.5,self.obj395)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj395.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj395)
   self.obj395.postAction( cobj0.RHS.CREATE )

   self.obj396=GenericGraphEdge(self)
   self.obj396.preAction( cobj0.RHS.CREATE )
   self.obj396.isGraphObjectVisual = True

   if(hasattr(self.obj396, '_setHierarchicalLink')):
     self.obj396._setHierarchicalLink(False)

   self.obj396.GGLabel.setValue(8)
   self.obj396.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(128.0,183.0,self.obj396)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj396.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj396)
   self.obj396.postAction( cobj0.RHS.CREATE )

   self.obj397=GenericGraphEdge(self)
   self.obj397.preAction( cobj0.RHS.CREATE )
   self.obj397.isGraphObjectVisual = True

   if(hasattr(self.obj397, '_setHierarchicalLink')):
     self.obj397._setHierarchicalLink(False)

   self.obj397.GGLabel.setValue(12)
   self.obj397.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(145.785046729,105.210526316,self.obj397)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj397.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj397)
   self.obj397.postAction( cobj0.RHS.CREATE )

   self.obj386.out_connections_.append(self.obj395)
   self.obj395.in_connections_.append(self.obj386)
   self.obj386.graphObject_.pendingConnections.append((self.obj386.graphObject_.tag, self.obj395.graphObject_.tag, [65.0, 102.0, 144.5, 87.5], 0, True))
   self.obj386.out_connections_.append(self.obj397)
   self.obj397.in_connections_.append(self.obj386)
   self.obj386.graphObject_.pendingConnections.append((self.obj386.graphObject_.tag, self.obj397.graphObject_.tag, [77.0, 102.0, 145.78504672897196, 105.21052631578948], 0, True))
   self.obj387.out_connections_.append(self.obj396)
   self.obj396.in_connections_.append(self.obj387)
   self.obj387.graphObject_.pendingConnections.append((self.obj387.graphObject_.tag, self.obj396.graphObject_.tag, [44.0, 181.0, 128.0, 183.0], 0, True))
   self.obj388.out_connections_.append(self.obj393)
   self.obj393.in_connections_.append(self.obj388)
   self.obj388.graphObject_.pendingConnections.append((self.obj388.graphObject_.tag, self.obj393.graphObject_.tag, [224.0, 73.0, 218.78504672897196, 90.71052631578948], 0, True))
   self.obj389.out_connections_.append(self.obj394)
   self.obj394.in_connections_.append(self.obj389)
   self.obj389.graphObject_.pendingConnections.append((self.obj389.graphObject_.tag, self.obj394.graphObject_.tag, [214.1869158878505, 115.5263157894737, 220.59345794392524, 148.26315789473685], 0, True))
   self.obj391.out_connections_.append(self.obj392)
   self.obj392.in_connections_.append(self.obj391)
   self.obj391.graphObject_.pendingConnections.append((self.obj391.graphObject_.tag, self.obj392.graphObject_.tag, [224.0, 230.0, 228.78504672897196, 249.21052631578948], 0, True))
   self.obj392.out_connections_.append(self.obj390)
   self.obj390.in_connections_.append(self.obj392)
   self.obj392.graphObject_.pendingConnections.append((self.obj392.graphObject_.tag, self.obj390.graphObject_.tag, [233.57009345794393, 268.42105263157896, 228.78504672897196, 249.21052631578948], 0, True))
   self.obj393.out_connections_.append(self.obj389)
   self.obj389.in_connections_.append(self.obj393)
   self.obj393.graphObject_.pendingConnections.append((self.obj393.graphObject_.tag, self.obj389.graphObject_.tag, [213.57009345794393, 108.42105263157895, 218.78504672897196, 90.71052631578948], 0, True))
   self.obj394.out_connections_.append(self.obj391)
   self.obj391.in_connections_.append(self.obj394)
   self.obj394.graphObject_.pendingConnections.append((self.obj394.graphObject_.tag, self.obj391.graphObject_.tag, [227.0, 181.0, 220.59345794392524, 148.26315789473685], 0, True))
   self.obj395.out_connections_.append(self.obj388)
   self.obj388.in_connections_.append(self.obj395)
   self.obj395.graphObject_.pendingConnections.append((self.obj395.graphObject_.tag, self.obj388.graphObject_.tag, [224.0, 73.0, 144.5, 87.5], 0, True))
   self.obj396.out_connections_.append(self.obj391)
   self.obj391.in_connections_.append(self.obj396)
   self.obj396.graphObject_.pendingConnections.append((self.obj396.graphObject_.tag, self.obj391.graphObject_.tag, [212.0, 185.0, 128.0, 183.0], 0, True))
   self.obj397.out_connections_.append(self.obj389)
   self.obj389.in_connections_.append(self.obj397)
   self.obj397.graphObject_.pendingConnections.append((self.obj397.graphObject_.tag, self.obj389.graphObject_.tag, [214.57009345794393, 108.42105263157895, 145.78504672897196, 105.21052631578948], 0, True))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'print \'Rule 22 :\'\nprint str(self.graphRewritingSystem.Dictag[ self.getMatched ( graphID , self.LHS.nodeWithLabel(1) ).name.getValue() ]) +\' for \'+ self.getMatched ( graphID , self.LHS.nodeWithLabel(1) ).name.getValue()\n\nno4 = self.getMatched(graphID, self.LHS.nodeWithLabel(4))\nno7 = self.getMatched(graphID, self.LHS.nodeWithLabel(7))\nreturn not( hasattr(no4, "assign1Rule") and hasattr(no7, "assign1Rule") )\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'nod4 = self.getMatched(graphID, self.LHS.nodeWithLabel(4))\nnod7 = self.getMatched(graphID, self.LHS.nodeWithLabel(7))\nnod4.assign1Rule = True \nnod7.assign1Rule = True \n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('RemoveGoals', 20)
   cobj0.Order=ATOM3Integer(25)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

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

   cobj0.LHS = ASG_omacss(self)
   cobj0.LHS.merge(ASG_pns2(self))
   cobj0.LHS.merge(ASG_GenericGraph(self))

   self.obj404=Goal(self)
   self.obj404.preAction( cobj0.LHS.CREATE )
   self.obj404.isGraphObjectVisual = True

   if(hasattr(self.obj404, '_setHierarchicalLink')):
     self.obj404._setHierarchicalLink(False)

   # name
   self.obj404.name.setValue('')
   self.obj404.name.setNone()

   self.obj404.GGLabel.setValue(1)
   self.obj404.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(200.0,60.0,self.obj404)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj404.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj404)
   self.obj404.postAction( cobj0.LHS.CREATE )

   self.obj405=metarial(self)
   self.obj405.preAction( cobj0.LHS.CREATE )
   self.obj405.isGraphObjectVisual = True

   if(hasattr(self.obj405, '_setHierarchicalLink')):
     self.obj405._setHierarchicalLink(False)

   # Name
   self.obj405.Name.setValue('')
   self.obj405.Name.setNone()

   self.obj405.GGLabel.setValue(2)
   self.obj405.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(340.0,60.0,self.obj405)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj405.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj405)
   self.obj405.postAction( cobj0.LHS.CREATE )

   self.obj406=GenericGraphEdge(self)
   self.obj406.preAction( cobj0.LHS.CREATE )
   self.obj406.isGraphObjectVisual = True

   if(hasattr(self.obj406, '_setHierarchicalLink')):
     self.obj406._setHierarchicalLink(False)

   self.obj406.GGLabel.setValue(3)
   self.obj406.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(292.0,107.0,self.obj406)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj406.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj406)
   self.obj406.postAction( cobj0.LHS.CREATE )

   self.obj404.out_connections_.append(self.obj406)
   self.obj406.in_connections_.append(self.obj404)
   self.obj404.graphObject_.pendingConnections.append((self.obj404.graphObject_.tag, self.obj406.graphObject_.tag, [234.0, 110.0, 292.0, 107.0], 0, True))
   self.obj406.out_connections_.append(self.obj405)
   self.obj405.in_connections_.append(self.obj406)
   self.obj406.graphObject_.pendingConnections.append((self.obj406.graphObject_.tag, self.obj405.graphObject_.tag, [350.0, 104.0, 292.0, 107.0], 0, True))

   cobj0.RHS = ASG_omacss(self)
   cobj0.RHS.merge(ASG_pns2(self))

   self.obj409=metarial(self)
   self.obj409.preAction( cobj0.RHS.CREATE )
   self.obj409.isGraphObjectVisual = True

   if(hasattr(self.obj409, '_setHierarchicalLink')):
     self.obj409._setHierarchicalLink(False)

   # Name
   self.obj409.Name.setValue('')
   self.obj409.Name.setNone()

   self.obj409.GGLabel.setValue(2)
   self.obj409.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(280.0,60.0,self.obj409)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj409.graphObject_ = new_obj
   self.obj4090= AttrCalc()
   self.obj4090.Copy=ATOM3Boolean()
   self.obj4090.Copy.setValue(('Copy from LHS', 1))
   self.obj4090.Copy.config = 0
   self.obj4090.Specify=ATOM3Constraint()
   self.obj4090.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj409.GGset2Any['Name']= self.obj4090

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj409)
   self.obj409.postAction( cobj0.RHS.CREATE )


   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.graphRewritingSystem.finalStat > 20 \n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('RemoveAGent', 20)
   cobj0.Order=ATOM3Integer(26)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

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

   cobj0.LHS = ASG_omacss(self)
   cobj0.LHS.merge(ASG_pns2(self))
   cobj0.LHS.merge(ASG_GenericGraph(self))

   self.obj416=Agent(self)
   self.obj416.preAction( cobj0.LHS.CREATE )
   self.obj416.isGraphObjectVisual = True

   if(hasattr(self.obj416, '_setHierarchicalLink')):
     self.obj416._setHierarchicalLink(False)

   # price
   self.obj416.price.setNone()

   # name
   self.obj416.name.setValue('')
   self.obj416.name.setNone()

   self.obj416.GGLabel.setValue(1)
   self.obj416.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(100.0,60.0,self.obj416)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj416.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj416)
   self.obj416.postAction( cobj0.LHS.CREATE )

   self.obj417=rawMaterial(self)
   self.obj417.preAction( cobj0.LHS.CREATE )
   self.obj417.isGraphObjectVisual = True

   if(hasattr(self.obj417, '_setHierarchicalLink')):
     self.obj417._setHierarchicalLink(False)

   # Name
   self.obj417.Name.setValue('')
   self.obj417.Name.setNone()

   self.obj417.GGLabel.setValue(2)
   self.obj417.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(280.0,20.0,self.obj417)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj417.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj417)
   self.obj417.postAction( cobj0.LHS.CREATE )

   self.obj418=operatingUnit(self)
   self.obj418.preAction( cobj0.LHS.CREATE )
   self.obj418.isGraphObjectVisual = True

   if(hasattr(self.obj418, '_setHierarchicalLink')):
     self.obj418._setHierarchicalLink(False)

   # name
   self.obj418.name.setValue('')
   self.obj418.name.setNone()

   self.obj418.GGLabel.setValue(3)
   self.obj418.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(280.0,140.0,self.obj418)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj418.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj418)
   self.obj418.postAction( cobj0.LHS.CREATE )

   self.obj419=fromRaw(self)
   self.obj419.preAction( cobj0.LHS.CREATE )
   self.obj419.isGraphObjectVisual = True

   if(hasattr(self.obj419, '_setHierarchicalLink')):
     self.obj419._setHierarchicalLink(False)

   # rate
   self.obj419.rate.setNone()

   self.obj419.GGLabel.setValue(6)
   self.obj419.graphClass_= graph_fromRaw
   if self.genGraphics:
      new_obj = graph_fromRaw(298.785046729,110.710526316,self.obj419)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj419.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj419)
   self.obj419.postAction( cobj0.LHS.CREATE )

   self.obj420=GenericGraphEdge(self)
   self.obj420.preAction( cobj0.LHS.CREATE )
   self.obj420.isGraphObjectVisual = True

   if(hasattr(self.obj420, '_setHierarchicalLink')):
     self.obj420._setHierarchicalLink(False)

   self.obj420.GGLabel.setValue(4)
   self.obj420.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(220.5,97.5,self.obj420)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj420.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj420)
   self.obj420.postAction( cobj0.LHS.CREATE )

   self.obj421=GenericGraphEdge(self)
   self.obj421.preAction( cobj0.LHS.CREATE )
   self.obj421.isGraphObjectVisual = True

   if(hasattr(self.obj421, '_setHierarchicalLink')):
     self.obj421._setHierarchicalLink(False)

   self.obj421.GGLabel.setValue(5)
   self.obj421.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(215.285046729,135.210526316,self.obj421)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj421.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj421)
   self.obj421.postAction( cobj0.LHS.CREATE )

   self.obj416.out_connections_.append(self.obj420)
   self.obj420.in_connections_.append(self.obj416)
   self.obj416.graphObject_.pendingConnections.append((self.obj416.graphObject_.tag, self.obj420.graphObject_.tag, [137.0, 122.0, 220.5, 97.5], 0, True))
   self.obj416.out_connections_.append(self.obj421)
   self.obj421.in_connections_.append(self.obj416)
   self.obj416.graphObject_.pendingConnections.append((self.obj416.graphObject_.tag, self.obj421.graphObject_.tag, [137.0, 122.0, 215.285046729, 135.210526316], 2, 0))
   self.obj417.out_connections_.append(self.obj419)
   self.obj419.in_connections_.append(self.obj417)
   self.obj417.graphObject_.pendingConnections.append((self.obj417.graphObject_.tag, self.obj419.graphObject_.tag, [304.0, 73.0, 298.78504672897196, 110.71052631578948], 0, True))
   self.obj419.out_connections_.append(self.obj418)
   self.obj418.in_connections_.append(self.obj419)
   self.obj419.graphObject_.pendingConnections.append((self.obj419.graphObject_.tag, self.obj418.graphObject_.tag, [293.5700934579439, 148.42105263157896, 298.78504672897196, 110.71052631578948], 0, True))
   self.obj420.out_connections_.append(self.obj417)
   self.obj417.in_connections_.append(self.obj420)
   self.obj420.graphObject_.pendingConnections.append((self.obj420.graphObject_.tag, self.obj417.graphObject_.tag, [304.0, 73.0, 220.5, 97.5], 0, True))
   self.obj421.out_connections_.append(self.obj418)
   self.obj418.in_connections_.append(self.obj421)
   self.obj421.graphObject_.pendingConnections.append((self.obj421.graphObject_.tag, self.obj418.graphObject_.tag, [294.5700934579439, 148.42105263157896, 215.285046729, 135.210526316], 2, 0))

   cobj0.RHS = ASG_omacss(self)
   cobj0.RHS.merge(ASG_pns2(self))

   self.obj424=rawMaterial(self)
   self.obj424.preAction( cobj0.RHS.CREATE )
   self.obj424.isGraphObjectVisual = True

   if(hasattr(self.obj424, '_setHierarchicalLink')):
     self.obj424._setHierarchicalLink(False)

   # Name
   self.obj424.Name.setValue('')
   self.obj424.Name.setNone()

   self.obj424.GGLabel.setValue(2)
   self.obj424.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(200.0,20.0,self.obj424)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj424.graphObject_ = new_obj
   self.obj4240= AttrCalc()
   self.obj4240.Copy=ATOM3Boolean()
   self.obj4240.Copy.setValue(('Copy from LHS', 1))
   self.obj4240.Copy.config = 0
   self.obj4240.Specify=ATOM3Constraint()
   self.obj4240.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj424.GGset2Any['Name']= self.obj4240

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj424)
   self.obj424.postAction( cobj0.RHS.CREATE )

   self.obj425=operatingUnit(self)
   self.obj425.preAction( cobj0.RHS.CREATE )
   self.obj425.isGraphObjectVisual = True

   if(hasattr(self.obj425, '_setHierarchicalLink')):
     self.obj425._setHierarchicalLink(False)

   # name
   self.obj425.name.setValue('')
   self.obj425.name.setNone()

   self.obj425.GGLabel.setValue(3)
   self.obj425.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(200.0,160.0,self.obj425)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj425.graphObject_ = new_obj
   self.obj4250= AttrCalc()
   self.obj4250.Copy=ATOM3Boolean()
   self.obj4250.Copy.setValue(('Copy from LHS', 1))
   self.obj4250.Copy.config = 0
   self.obj4250.Specify=ATOM3Constraint()
   self.obj4250.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj425.GGset2Any['name']= self.obj4250

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj425)
   self.obj425.postAction( cobj0.RHS.CREATE )

   self.obj426=fromRaw(self)
   self.obj426.preAction( cobj0.RHS.CREATE )
   self.obj426.isGraphObjectVisual = True

   if(hasattr(self.obj426, '_setHierarchicalLink')):
     self.obj426._setHierarchicalLink(False)

   # rate
   self.obj426.rate.setValue(0.0)

   self.obj426.GGLabel.setValue(6)
   self.obj426.graphClass_= graph_fromRaw
   if self.genGraphics:
      new_obj = graph_fromRaw(228.785046729,120.710526316,self.obj426)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj426.graphObject_ = new_obj
   self.obj4260= AttrCalc()
   self.obj4260.Copy=ATOM3Boolean()
   self.obj4260.Copy.setValue(('Copy from LHS', 1))
   self.obj4260.Copy.config = 0
   self.obj4260.Specify=ATOM3Constraint()
   self.obj4260.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj426.GGset2Any['rate']= self.obj4260

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj426)
   self.obj426.postAction( cobj0.RHS.CREATE )

   self.obj424.out_connections_.append(self.obj426)
   self.obj426.in_connections_.append(self.obj424)
   self.obj424.graphObject_.pendingConnections.append((self.obj424.graphObject_.tag, self.obj426.graphObject_.tag, [224.0, 73.0, 228.78504672897196, 120.71052631578948], 0, True))
   self.obj426.out_connections_.append(self.obj425)
   self.obj425.in_connections_.append(self.obj426)
   self.obj426.graphObject_.pendingConnections.append((self.obj426.graphObject_.tag, self.obj425.graphObject_.tag, [213.57009345794393, 168.42105263157896, 228.78504672897196, 120.71052631578948], 0, True))

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

   from CapableOf import *
   from Goal import *
   from ASG_omacss import *
   from Agent import *
   from Capabilitie import *
   from Role import *
   from requir import *
   from achieve import *
   from posses import *

   cobj0.LHS = ASG_omacss(self)

   self.obj431=Capabilitie(self)
   self.obj431.preAction( cobj0.LHS.CREATE )
   self.obj431.isGraphObjectVisual = True

   if(hasattr(self.obj431, '_setHierarchicalLink')):
     self.obj431._setHierarchicalLink(False)

   # name
   self.obj431.name.setValue('')
   self.obj431.name.setNone()

   self.obj431.GGLabel.setValue(1)
   self.obj431.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(200.0,100.0,self.obj431)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj431.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj431)
   self.obj431.postAction( cobj0.LHS.CREATE )


   cobj0.RHS = ASG_omacss(self)


   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.graphRewritingSystem.finalStat > 20 \n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('RemoveRolez', 20)
   cobj0.Order=ATOM3Integer(28)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

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

   cobj0.LHS = ASG_omacss(self)
   cobj0.LHS.merge(ASG_pns2(self))
   cobj0.LHS.merge(ASG_GenericGraph(self))

   self.obj439=Role(self)
   self.obj439.preAction( cobj0.LHS.CREATE )
   self.obj439.isGraphObjectVisual = True

   if(hasattr(self.obj439, '_setHierarchicalLink')):
     self.obj439._setHierarchicalLink(False)

   # name
   self.obj439.name.setValue('')
   self.obj439.name.setNone()

   self.obj439.GGLabel.setValue(1)
   self.obj439.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(60.0,60.0,self.obj439)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj439.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj439)
   self.obj439.postAction( cobj0.LHS.CREATE )

   self.obj440=operatingUnit(self)
   self.obj440.preAction( cobj0.LHS.CREATE )
   self.obj440.isGraphObjectVisual = True

   if(hasattr(self.obj440, '_setHierarchicalLink')):
     self.obj440._setHierarchicalLink(False)

   # name
   self.obj440.name.setValue('')
   self.obj440.name.setNone()

   self.obj440.GGLabel.setValue(2)
   self.obj440.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(260.0,160.0,self.obj440)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj440.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj440)
   self.obj440.postAction( cobj0.LHS.CREATE )

   self.obj441=metarial(self)
   self.obj441.preAction( cobj0.LHS.CREATE )
   self.obj441.isGraphObjectVisual = True

   if(hasattr(self.obj441, '_setHierarchicalLink')):
     self.obj441._setHierarchicalLink(False)

   # Name
   self.obj441.Name.setValue('')
   self.obj441.Name.setNone()

   self.obj441.GGLabel.setValue(5)
   self.obj441.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(260.0,60.0,self.obj441)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj441.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj441)
   self.obj441.postAction( cobj0.LHS.CREATE )

   self.obj442=fromMaterial(self)
   self.obj442.preAction( cobj0.LHS.CREATE )
   self.obj442.isGraphObjectVisual = True

   if(hasattr(self.obj442, '_setHierarchicalLink')):
     self.obj442._setHierarchicalLink(False)

   # rate
   self.obj442.rate.setNone()

   self.obj442.GGLabel.setValue(3)
   self.obj442.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(288.785046729,139.210526316,self.obj442)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj442.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj442)
   self.obj442.postAction( cobj0.LHS.CREATE )

   self.obj441.out_connections_.append(self.obj442)
   self.obj442.in_connections_.append(self.obj441)
   self.obj441.graphObject_.pendingConnections.append((self.obj441.graphObject_.tag, self.obj442.graphObject_.tag, [284.0, 110.0, 288.78504672897196, 139.21052631578948], 0, True))
   self.obj442.out_connections_.append(self.obj440)
   self.obj440.in_connections_.append(self.obj442)
   self.obj442.graphObject_.pendingConnections.append((self.obj442.graphObject_.tag, self.obj440.graphObject_.tag, [273.5700934579439, 168.42105263157896, 288.78504672897196, 139.21052631578948], 0, True))

   cobj0.RHS = ASG_omacss(self)
   cobj0.RHS.merge(ASG_pns2(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj446=operatingUnit(self)
   self.obj446.preAction( cobj0.RHS.CREATE )
   self.obj446.isGraphObjectVisual = True

   if(hasattr(self.obj446, '_setHierarchicalLink')):
     self.obj446._setHierarchicalLink(False)

   # name
   self.obj446.name.setValue('')
   self.obj446.name.setNone()

   self.obj446.GGLabel.setValue(2)
   self.obj446.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(240.0,160.0,self.obj446)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj446.graphObject_ = new_obj
   self.obj4460= AttrCalc()
   self.obj4460.Copy=ATOM3Boolean()
   self.obj4460.Copy.setValue(('Copy from LHS', 1))
   self.obj4460.Copy.config = 0
   self.obj4460.Specify=ATOM3Constraint()
   self.obj4460.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj446.GGset2Any['name']= self.obj4460

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj446)
   self.obj446.postAction( cobj0.RHS.CREATE )

   self.obj447=metarial(self)
   self.obj447.preAction( cobj0.RHS.CREATE )
   self.obj447.isGraphObjectVisual = True

   if(hasattr(self.obj447, '_setHierarchicalLink')):
     self.obj447._setHierarchicalLink(False)

   # Name
   self.obj447.Name.setValue('')
   self.obj447.Name.setNone()

   self.obj447.GGLabel.setValue(5)
   self.obj447.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(240.0,40.0,self.obj447)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj447.graphObject_ = new_obj
   self.obj4470= AttrCalc()
   self.obj4470.Copy=ATOM3Boolean()
   self.obj4470.Copy.setValue(('Copy from LHS', 1))
   self.obj4470.Copy.config = 0
   self.obj4470.Specify=ATOM3Constraint()
   self.obj4470.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj447.GGset2Any['Name']= self.obj4470

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj447)
   self.obj447.postAction( cobj0.RHS.CREATE )

   self.obj448=fromMaterial(self)
   self.obj448.preAction( cobj0.RHS.CREATE )
   self.obj448.isGraphObjectVisual = True

   if(hasattr(self.obj448, '_setHierarchicalLink')):
     self.obj448._setHierarchicalLink(False)

   # rate
   self.obj448.rate.setValue(0.0)

   self.obj448.GGLabel.setValue(3)
   self.obj448.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(258.785046729,129.210526316,self.obj448)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj448.graphObject_ = new_obj
   self.obj4480= AttrCalc()
   self.obj4480.Copy=ATOM3Boolean()
   self.obj4480.Copy.setValue(('Copy from LHS', 1))
   self.obj4480.Copy.config = 0
   self.obj4480.Specify=ATOM3Constraint()
   self.obj4480.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj448.GGset2Any['rate']= self.obj4480

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj448)
   self.obj448.postAction( cobj0.RHS.CREATE )

   self.obj447.out_connections_.append(self.obj448)
   self.obj448.in_connections_.append(self.obj447)
   self.obj447.graphObject_.pendingConnections.append((self.obj447.graphObject_.tag, self.obj448.graphObject_.tag, [264.0, 90.0, 258.78504672897196, 129.21052631578948], 0, True))
   self.obj448.out_connections_.append(self.obj446)
   self.obj446.in_connections_.append(self.obj448)
   self.obj448.graphObject_.pendingConnections.append((self.obj448.graphObject_.tag, self.obj446.graphObject_.tag, [253.57009345794393, 168.42105263157896, 258.78504672897196, 129.21052631578948], 0, True))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.graphRewritingSystem.finalStat > 20 \n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   lcobj0.append(cobj0)
   self.EditingGraphGrammar.Rules.setValue(lcobj0)
   self.EditingGraphGrammar.InitialAction=ATOM3Constraint()
   self.EditingGraphGrammar.InitialAction.setValue(('constraint', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'print \'Version 19:02 \'\nself.rewritingSystem.finalStat = 0\nself.rewritingSystem.Dictag = {}\nself.rewritingSystem.Dictro = {}\nAgentDict = {}\nRoleDict = {} \natom3i = self.rewritingSystem.parent\nfor nodeType in atom3i.ASGroot.listNodes.keys():\n   for node in atom3i.ASGroot.listNodes[nodeType]:\n       if node.__class__.__name__ == \'Agent\' : \n           nodeName = node.name.getValue()\n           AgentDict[nodeName]=0  \n           for link in node.out_connections_ : \n               if hasattr(link,\'rate\') : \n                   AgentDict[nodeName] += link.rate.getValue()   \n           AgentDict[nodeName]= AgentDict[nodeName]/ len(node.out_connections_)\n       elif node.__class__.__name__ == \'Role\' :\n           nodeName = node.name.getValue()\n           RoleDict[nodeName]={} \n           lisst = RoleDict[nodeName]\n           for link in node.out_connections_ : \n               if hasattr(link,\'rate\') :\n                   for nodes in link.out_connections_ :  \n                    RoleDict[nodeName][nodes.name.getValue()]=link.rate.getValue()\n                       #lisst.append( {nodes.name.getValue():link.rate.getValue()} ) \n           #RoleDict[nodeName] = lisst  \n\nprint \'Agent Dict for his Value  : \'+str(AgentDict)\nprint \'Role Dict for his Value  : \'+str(RoleDict)\n\nself.rewritingSystem.Dictag = AgentDict\nself.rewritingSystem.Dictro = RoleDict\n\n'))
   self.EditingGraphGrammar.FinalAction=ATOM3Constraint()
   self.EditingGraphGrammar.FinalAction.setValue(('constraint', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))


