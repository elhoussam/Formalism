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

   self.obj935=Agent(self)
   self.obj935.preAction( cobj0.LHS.CREATE )
   self.obj935.isGraphObjectVisual = True

   if(hasattr(self.obj935, '_setHierarchicalLink')):
     self.obj935._setHierarchicalLink(False)

   # price
   self.obj935.price.setValue(0)

   # name
   self.obj935.name.setValue('')
   self.obj935.name.setNone()

   self.obj935.GGLabel.setValue(1)
   self.obj935.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(80.0,40.0,self.obj935)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj935.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj935)
   self.obj935.postAction( cobj0.LHS.CREATE )

   self.obj936=Capabilitie(self)
   self.obj936.preAction( cobj0.LHS.CREATE )
   self.obj936.isGraphObjectVisual = True

   if(hasattr(self.obj936, '_setHierarchicalLink')):
     self.obj936._setHierarchicalLink(False)

   # name
   self.obj936.name.setValue('')
   self.obj936.name.setNone()

   self.obj936.GGLabel.setValue(2)
   self.obj936.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(200.0,200.0,self.obj936)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj936.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj936)
   self.obj936.postAction( cobj0.LHS.CREATE )

   self.obj937=Role(self)
   self.obj937.preAction( cobj0.LHS.CREATE )
   self.obj937.isGraphObjectVisual = True

   if(hasattr(self.obj937, '_setHierarchicalLink')):
     self.obj937._setHierarchicalLink(False)

   # name
   self.obj937.name.setValue('')
   self.obj937.name.setNone()

   self.obj937.GGLabel.setValue(3)
   self.obj937.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(320.0,60.0,self.obj937)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj937.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj937)
   self.obj937.postAction( cobj0.LHS.CREATE )

   self.obj938=posses(self)
   self.obj938.preAction( cobj0.LHS.CREATE )
   self.obj938.isGraphObjectVisual = True

   if(hasattr(self.obj938, '_setHierarchicalLink')):
     self.obj938._setHierarchicalLink(False)

   # rate
   self.obj938.rate.setValue(0.0)

   self.obj938.GGLabel.setValue(4)
   self.obj938.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(163.0,150.5,self.obj938)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj938.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj938)
   self.obj938.postAction( cobj0.LHS.CREATE )

   self.obj939=requir(self)
   self.obj939.preAction( cobj0.LHS.CREATE )
   self.obj939.isGraphObjectVisual = True

   if(hasattr(self.obj939, '_setHierarchicalLink')):
     self.obj939._setHierarchicalLink(False)

   self.obj939.GGLabel.setValue(5)
   self.obj939.graphClass_= graph_requir
   if self.genGraphics:
      new_obj = graph_requir(282.5,152.5,self.obj939)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj939.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj939)
   self.obj939.postAction( cobj0.LHS.CREATE )

   self.obj935.out_connections_.append(self.obj938)
   self.obj938.in_connections_.append(self.obj935)
   self.obj935.graphObject_.pendingConnections.append((self.obj935.graphObject_.tag, self.obj938.graphObject_.tag, [105.0, 102.0, 163.0, 150.5], 0, True))
   self.obj937.out_connections_.append(self.obj939)
   self.obj939.in_connections_.append(self.obj937)
   self.obj937.graphObject_.pendingConnections.append((self.obj937.graphObject_.tag, self.obj939.graphObject_.tag, [344.0, 106.0, 282.5, 152.5], 0, True))
   self.obj938.out_connections_.append(self.obj936)
   self.obj936.in_connections_.append(self.obj938)
   self.obj938.graphObject_.pendingConnections.append((self.obj938.graphObject_.tag, self.obj936.graphObject_.tag, [221.0, 199.0, 163.0, 150.5], 0, True))
   self.obj939.out_connections_.append(self.obj936)
   self.obj936.in_connections_.append(self.obj939)
   self.obj939.graphObject_.pendingConnections.append((self.obj939.graphObject_.tag, self.obj936.graphObject_.tag, [221.0, 199.0, 282.5, 152.5], 0, True))

   cobj0.RHS = ASG_omacss(self)

   self.obj941=Agent(self)
   self.obj941.preAction( cobj0.RHS.CREATE )
   self.obj941.isGraphObjectVisual = True

   if(hasattr(self.obj941, '_setHierarchicalLink')):
     self.obj941._setHierarchicalLink(False)

   # price
   self.obj941.price.setValue(0)

   # name
   self.obj941.name.setValue('')
   self.obj941.name.setNone()

   self.obj941.GGLabel.setValue(1)
   self.obj941.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(80.0,40.0,self.obj941)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj941.graphObject_ = new_obj
   self.obj9410= AttrCalc()
   self.obj9410.Copy=ATOM3Boolean()
   self.obj9410.Copy.setValue(('Copy from LHS', 1))
   self.obj9410.Copy.config = 0
   self.obj9410.Specify=ATOM3Constraint()
   self.obj9410.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj941.GGset2Any['price']= self.obj9410
   self.obj9411= AttrCalc()
   self.obj9411.Copy=ATOM3Boolean()
   self.obj9411.Copy.setValue(('Copy from LHS', 1))
   self.obj9411.Copy.config = 0
   self.obj9411.Specify=ATOM3Constraint()
   self.obj9411.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj941.GGset2Any['name']= self.obj9411

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj941)
   self.obj941.postAction( cobj0.RHS.CREATE )

   self.obj942=Capabilitie(self)
   self.obj942.preAction( cobj0.RHS.CREATE )
   self.obj942.isGraphObjectVisual = True

   if(hasattr(self.obj942, '_setHierarchicalLink')):
     self.obj942._setHierarchicalLink(False)

   # name
   self.obj942.name.setValue('')
   self.obj942.name.setNone()

   self.obj942.GGLabel.setValue(2)
   self.obj942.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(200.0,200.0,self.obj942)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj942.graphObject_ = new_obj
   self.obj9420= AttrCalc()
   self.obj9420.Copy=ATOM3Boolean()
   self.obj9420.Copy.setValue(('Copy from LHS', 1))
   self.obj9420.Copy.config = 0
   self.obj9420.Specify=ATOM3Constraint()
   self.obj9420.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj942.GGset2Any['name']= self.obj9420

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj942)
   self.obj942.postAction( cobj0.RHS.CREATE )

   self.obj943=Role(self)
   self.obj943.preAction( cobj0.RHS.CREATE )
   self.obj943.isGraphObjectVisual = True

   if(hasattr(self.obj943, '_setHierarchicalLink')):
     self.obj943._setHierarchicalLink(False)

   # name
   self.obj943.name.setValue('')
   self.obj943.name.setNone()

   self.obj943.GGLabel.setValue(3)
   self.obj943.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(320.0,60.0,self.obj943)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj943.graphObject_ = new_obj
   self.obj9430= AttrCalc()
   self.obj9430.Copy=ATOM3Boolean()
   self.obj9430.Copy.setValue(('Copy from LHS', 1))
   self.obj9430.Copy.config = 0
   self.obj9430.Specify=ATOM3Constraint()
   self.obj9430.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj943.GGset2Any['name']= self.obj9430

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj943)
   self.obj943.postAction( cobj0.RHS.CREATE )

   self.obj944=posses(self)
   self.obj944.preAction( cobj0.RHS.CREATE )
   self.obj944.isGraphObjectVisual = True

   if(hasattr(self.obj944, '_setHierarchicalLink')):
     self.obj944._setHierarchicalLink(False)

   # rate
   self.obj944.rate.setValue(0.0)

   self.obj944.GGLabel.setValue(4)
   self.obj944.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(163.0,150.5,self.obj944)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj944.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj944)
   self.obj944.postAction( cobj0.RHS.CREATE )

   self.obj945=CapableOf(self)
   self.obj945.preAction( cobj0.RHS.CREATE )
   self.obj945.isGraphObjectVisual = True

   if(hasattr(self.obj945, '_setHierarchicalLink')):
     self.obj945._setHierarchicalLink(False)

   self.obj945.GGLabel.setValue(7)
   self.obj945.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(233.5,74.0,self.obj945)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj945.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj945)
   self.obj945.postAction( cobj0.RHS.CREATE )

   self.obj946=requir(self)
   self.obj946.preAction( cobj0.RHS.CREATE )
   self.obj946.isGraphObjectVisual = True

   if(hasattr(self.obj946, '_setHierarchicalLink')):
     self.obj946._setHierarchicalLink(False)

   self.obj946.GGLabel.setValue(5)
   self.obj946.graphClass_= graph_requir
   if self.genGraphics:
      new_obj = graph_requir(282.5,152.5,self.obj946)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj946.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj946)
   self.obj946.postAction( cobj0.RHS.CREATE )

   self.obj941.out_connections_.append(self.obj944)
   self.obj944.in_connections_.append(self.obj941)
   self.obj941.graphObject_.pendingConnections.append((self.obj941.graphObject_.tag, self.obj944.graphObject_.tag, [117.0, 102.0, 163.0, 150.5], 2, 0))
   self.obj941.out_connections_.append(self.obj945)
   self.obj945.in_connections_.append(self.obj941)
   self.obj941.graphObject_.pendingConnections.append((self.obj941.graphObject_.tag, self.obj945.graphObject_.tag, [117.0, 102.0, 175.0, 84.5, 233.5, 74.0], 2, True))
   self.obj943.out_connections_.append(self.obj946)
   self.obj946.in_connections_.append(self.obj943)
   self.obj943.graphObject_.pendingConnections.append((self.obj943.graphObject_.tag, self.obj946.graphObject_.tag, [351.0, 105.0, 282.5, 152.5], 2, 0))
   self.obj944.out_connections_.append(self.obj942)
   self.obj942.in_connections_.append(self.obj944)
   self.obj944.graphObject_.pendingConnections.append((self.obj944.graphObject_.tag, self.obj942.graphObject_.tag, [231.0, 203.0, 163.0, 150.5], 2, 0))
   self.obj945.out_connections_.append(self.obj943)
   self.obj943.in_connections_.append(self.obj945)
   self.obj945.graphObject_.pendingConnections.append((self.obj945.graphObject_.tag, self.obj943.graphObject_.tag, [351.0, 60.0, 292.0, 63.5, 233.5, 74.0], 2, True))
   self.obj946.out_connections_.append(self.obj942)
   self.obj942.in_connections_.append(self.obj946)
   self.obj946.graphObject_.pendingConnections.append((self.obj946.graphObject_.tag, self.obj942.graphObject_.tag, [231.0, 203.0, 282.5, 152.5], 2, 0))

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

   self.obj951=Agent(self)
   self.obj951.preAction( cobj0.LHS.CREATE )
   self.obj951.isGraphObjectVisual = True

   if(hasattr(self.obj951, '_setHierarchicalLink')):
     self.obj951._setHierarchicalLink(False)

   # price
   self.obj951.price.setValue(0)

   # name
   self.obj951.name.setValue('')
   self.obj951.name.setNone()

   self.obj951.GGLabel.setValue(1)
   self.obj951.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(60.0,20.0,self.obj951)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj951.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj951)
   self.obj951.postAction( cobj0.LHS.CREATE )

   self.obj952=Capabilitie(self)
   self.obj952.preAction( cobj0.LHS.CREATE )
   self.obj952.isGraphObjectVisual = True

   if(hasattr(self.obj952, '_setHierarchicalLink')):
     self.obj952._setHierarchicalLink(False)

   # name
   self.obj952.name.setValue('')
   self.obj952.name.setNone()

   self.obj952.GGLabel.setValue(2)
   self.obj952.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(80.0,160.0,self.obj952)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj952.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj952)
   self.obj952.postAction( cobj0.LHS.CREATE )

   self.obj953=Capabilitie(self)
   self.obj953.preAction( cobj0.LHS.CREATE )
   self.obj953.isGraphObjectVisual = True

   if(hasattr(self.obj953, '_setHierarchicalLink')):
     self.obj953._setHierarchicalLink(False)

   # name
   self.obj953.name.setValue('')
   self.obj953.name.setNone()

   self.obj953.GGLabel.setValue(3)
   self.obj953.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(260.0,20.0,self.obj953)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj953.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj953)
   self.obj953.postAction( cobj0.LHS.CREATE )

   self.obj954=Role(self)
   self.obj954.preAction( cobj0.LHS.CREATE )
   self.obj954.isGraphObjectVisual = True

   if(hasattr(self.obj954, '_setHierarchicalLink')):
     self.obj954._setHierarchicalLink(False)

   # name
   self.obj954.name.setValue('')
   self.obj954.name.setNone()

   self.obj954.GGLabel.setValue(4)
   self.obj954.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(280.0,140.0,self.obj954)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj954.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj954)
   self.obj954.postAction( cobj0.LHS.CREATE )

   self.obj955=posses(self)
   self.obj955.preAction( cobj0.LHS.CREATE )
   self.obj955.isGraphObjectVisual = True

   if(hasattr(self.obj955, '_setHierarchicalLink')):
     self.obj955._setHierarchicalLink(False)

   # rate
   self.obj955.rate.setValue(0.0)

   self.obj955.GGLabel.setValue(5)
   self.obj955.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(183.0,70.5,self.obj955)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj955.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj955)
   self.obj955.postAction( cobj0.LHS.CREATE )

   self.obj956=posses(self)
   self.obj956.preAction( cobj0.LHS.CREATE )
   self.obj956.isGraphObjectVisual = True

   if(hasattr(self.obj956, '_setHierarchicalLink')):
     self.obj956._setHierarchicalLink(False)

   # rate
   self.obj956.rate.setValue(0.0)

   self.obj956.GGLabel.setValue(6)
   self.obj956.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(93.0,120.5,self.obj956)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj956.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj956)
   self.obj956.postAction( cobj0.LHS.CREATE )

   self.obj957=CapableOf(self)
   self.obj957.preAction( cobj0.LHS.CREATE )
   self.obj957.isGraphObjectVisual = True

   if(hasattr(self.obj957, '_setHierarchicalLink')):
     self.obj957._setHierarchicalLink(False)

   self.obj957.GGLabel.setValue(9)
   self.obj957.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(194.5,111.5,self.obj957)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj957.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj957)
   self.obj957.postAction( cobj0.LHS.CREATE )

   self.obj958=requir(self)
   self.obj958.preAction( cobj0.LHS.CREATE )
   self.obj958.isGraphObjectVisual = True

   if(hasattr(self.obj958, '_setHierarchicalLink')):
     self.obj958._setHierarchicalLink(False)

   self.obj958.GGLabel.setValue(7)
   self.obj958.graphClass_= graph_requir
   if self.genGraphics:
      new_obj = graph_requir(202.5,192.5,self.obj958)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj958.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj958)
   self.obj958.postAction( cobj0.LHS.CREATE )

   self.obj959=requir(self)
   self.obj959.preAction( cobj0.LHS.CREATE )
   self.obj959.isGraphObjectVisual = True

   if(hasattr(self.obj959, '_setHierarchicalLink')):
     self.obj959._setHierarchicalLink(False)

   self.obj959.GGLabel.setValue(8)
   self.obj959.graphClass_= graph_requir
   if self.genGraphics:
      new_obj = graph_requir(292.5,100.0,self.obj959)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj959.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj959)
   self.obj959.postAction( cobj0.LHS.CREATE )

   self.obj951.out_connections_.append(self.obj955)
   self.obj955.in_connections_.append(self.obj951)
   self.obj951.graphObject_.pendingConnections.append((self.obj951.graphObject_.tag, self.obj955.graphObject_.tag, [85.0, 82.0, 183.0, 70.5], 0, True))
   self.obj951.out_connections_.append(self.obj956)
   self.obj956.in_connections_.append(self.obj951)
   self.obj951.graphObject_.pendingConnections.append((self.obj951.graphObject_.tag, self.obj956.graphObject_.tag, [85.0, 82.0, 93.0, 120.5], 0, True))
   self.obj951.out_connections_.append(self.obj957)
   self.obj957.in_connections_.append(self.obj951)
   self.obj951.graphObject_.pendingConnections.append((self.obj951.graphObject_.tag, self.obj957.graphObject_.tag, [85.0, 82.0, 194.5, 111.5], 0, True))
   self.obj954.out_connections_.append(self.obj958)
   self.obj958.in_connections_.append(self.obj954)
   self.obj954.graphObject_.pendingConnections.append((self.obj954.graphObject_.tag, self.obj958.graphObject_.tag, [304.0, 186.0, 202.5, 192.5], 0, True))
   self.obj954.out_connections_.append(self.obj959)
   self.obj959.in_connections_.append(self.obj954)
   self.obj954.graphObject_.pendingConnections.append((self.obj954.graphObject_.tag, self.obj959.graphObject_.tag, [304.0, 141.0, 292.5, 100.0], 0, True))
   self.obj955.out_connections_.append(self.obj953)
   self.obj953.in_connections_.append(self.obj955)
   self.obj955.graphObject_.pendingConnections.append((self.obj955.graphObject_.tag, self.obj953.graphObject_.tag, [281.0, 59.0, 183.0, 70.5], 0, True))
   self.obj956.out_connections_.append(self.obj952)
   self.obj952.in_connections_.append(self.obj956)
   self.obj956.graphObject_.pendingConnections.append((self.obj956.graphObject_.tag, self.obj952.graphObject_.tag, [101.0, 159.0, 93.0, 120.5], 0, True))
   self.obj957.out_connections_.append(self.obj954)
   self.obj954.in_connections_.append(self.obj957)
   self.obj957.graphObject_.pendingConnections.append((self.obj957.graphObject_.tag, self.obj954.graphObject_.tag, [311.0, 140.0, 194.5, 111.5], 2, 0))
   self.obj958.out_connections_.append(self.obj952)
   self.obj952.in_connections_.append(self.obj958)
   self.obj958.graphObject_.pendingConnections.append((self.obj958.graphObject_.tag, self.obj952.graphObject_.tag, [101.0, 199.0, 202.5, 192.5], 0, True))
   self.obj959.out_connections_.append(self.obj953)
   self.obj953.in_connections_.append(self.obj959)
   self.obj959.graphObject_.pendingConnections.append((self.obj959.graphObject_.tag, self.obj953.graphObject_.tag, [281.0, 59.0, 292.5, 100.0], 0, True))

   cobj0.RHS = ASG_omacss(self)

   self.obj961=Agent(self)
   self.obj961.preAction( cobj0.RHS.CREATE )
   self.obj961.isGraphObjectVisual = True

   if(hasattr(self.obj961, '_setHierarchicalLink')):
     self.obj961._setHierarchicalLink(False)

   # price
   self.obj961.price.setValue(0)

   # name
   self.obj961.name.setValue('')
   self.obj961.name.setNone()

   self.obj961.GGLabel.setValue(1)
   self.obj961.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(60.0,20.0,self.obj961)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj961.graphObject_ = new_obj
   self.obj9610= AttrCalc()
   self.obj9610.Copy=ATOM3Boolean()
   self.obj9610.Copy.setValue(('Copy from LHS', 1))
   self.obj9610.Copy.config = 0
   self.obj9610.Specify=ATOM3Constraint()
   self.obj9610.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj961.GGset2Any['price']= self.obj9610
   self.obj9611= AttrCalc()
   self.obj9611.Copy=ATOM3Boolean()
   self.obj9611.Copy.setValue(('Copy from LHS', 1))
   self.obj9611.Copy.config = 0
   self.obj9611.Specify=ATOM3Constraint()
   self.obj9611.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj961.GGset2Any['name']= self.obj9611

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj961)
   self.obj961.postAction( cobj0.RHS.CREATE )

   self.obj962=Capabilitie(self)
   self.obj962.preAction( cobj0.RHS.CREATE )
   self.obj962.isGraphObjectVisual = True

   if(hasattr(self.obj962, '_setHierarchicalLink')):
     self.obj962._setHierarchicalLink(False)

   # name
   self.obj962.name.setValue('')
   self.obj962.name.setNone()

   self.obj962.GGLabel.setValue(2)
   self.obj962.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(80.0,160.0,self.obj962)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj962.graphObject_ = new_obj
   self.obj9620= AttrCalc()
   self.obj9620.Copy=ATOM3Boolean()
   self.obj9620.Copy.setValue(('Copy from LHS', 1))
   self.obj9620.Copy.config = 0
   self.obj9620.Specify=ATOM3Constraint()
   self.obj9620.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj962.GGset2Any['name']= self.obj9620

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj962)
   self.obj962.postAction( cobj0.RHS.CREATE )

   self.obj963=Capabilitie(self)
   self.obj963.preAction( cobj0.RHS.CREATE )
   self.obj963.isGraphObjectVisual = True

   if(hasattr(self.obj963, '_setHierarchicalLink')):
     self.obj963._setHierarchicalLink(False)

   # name
   self.obj963.name.setValue('')
   self.obj963.name.setNone()

   self.obj963.GGLabel.setValue(3)
   self.obj963.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(260.0,20.0,self.obj963)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj963.graphObject_ = new_obj
   self.obj9630= AttrCalc()
   self.obj9630.Copy=ATOM3Boolean()
   self.obj9630.Copy.setValue(('Copy from LHS', 1))
   self.obj9630.Copy.config = 0
   self.obj9630.Specify=ATOM3Constraint()
   self.obj9630.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj963.GGset2Any['name']= self.obj9630

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj963)
   self.obj963.postAction( cobj0.RHS.CREATE )

   self.obj964=Role(self)
   self.obj964.preAction( cobj0.RHS.CREATE )
   self.obj964.isGraphObjectVisual = True

   if(hasattr(self.obj964, '_setHierarchicalLink')):
     self.obj964._setHierarchicalLink(False)

   # name
   self.obj964.name.setValue('')
   self.obj964.name.setNone()

   self.obj964.GGLabel.setValue(4)
   self.obj964.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(280.0,140.0,self.obj964)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj964.graphObject_ = new_obj
   self.obj9640= AttrCalc()
   self.obj9640.Copy=ATOM3Boolean()
   self.obj9640.Copy.setValue(('Copy from LHS', 1))
   self.obj9640.Copy.config = 0
   self.obj9640.Specify=ATOM3Constraint()
   self.obj9640.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj964.GGset2Any['name']= self.obj9640

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj964)
   self.obj964.postAction( cobj0.RHS.CREATE )

   self.obj965=posses(self)
   self.obj965.preAction( cobj0.RHS.CREATE )
   self.obj965.isGraphObjectVisual = True

   if(hasattr(self.obj965, '_setHierarchicalLink')):
     self.obj965._setHierarchicalLink(False)

   # rate
   self.obj965.rate.setValue(0.0)

   self.obj965.GGLabel.setValue(5)
   self.obj965.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(183.0,70.5,self.obj965)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj965.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj965)
   self.obj965.postAction( cobj0.RHS.CREATE )

   self.obj966=posses(self)
   self.obj966.preAction( cobj0.RHS.CREATE )
   self.obj966.isGraphObjectVisual = True

   if(hasattr(self.obj966, '_setHierarchicalLink')):
     self.obj966._setHierarchicalLink(False)

   # rate
   self.obj966.rate.setValue(0.0)

   self.obj966.GGLabel.setValue(6)
   self.obj966.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(93.0,120.5,self.obj966)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj966.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj966)
   self.obj966.postAction( cobj0.RHS.CREATE )

   self.obj967=CapableOf(self)
   self.obj967.preAction( cobj0.RHS.CREATE )
   self.obj967.isGraphObjectVisual = True

   if(hasattr(self.obj967, '_setHierarchicalLink')):
     self.obj967._setHierarchicalLink(False)

   self.obj967.GGLabel.setValue(9)
   self.obj967.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(194.5,111.5,self.obj967)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj967.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj967)
   self.obj967.postAction( cobj0.RHS.CREATE )

   self.obj968=requir(self)
   self.obj968.preAction( cobj0.RHS.CREATE )
   self.obj968.isGraphObjectVisual = True

   if(hasattr(self.obj968, '_setHierarchicalLink')):
     self.obj968._setHierarchicalLink(False)

   self.obj968.GGLabel.setValue(7)
   self.obj968.graphClass_= graph_requir
   if self.genGraphics:
      new_obj = graph_requir(202.5,192.5,self.obj968)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj968.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj968)
   self.obj968.postAction( cobj0.RHS.CREATE )

   self.obj969=requir(self)
   self.obj969.preAction( cobj0.RHS.CREATE )
   self.obj969.isGraphObjectVisual = True

   if(hasattr(self.obj969, '_setHierarchicalLink')):
     self.obj969._setHierarchicalLink(False)

   self.obj969.GGLabel.setValue(8)
   self.obj969.graphClass_= graph_requir
   if self.genGraphics:
      new_obj = graph_requir(292.5,100.0,self.obj969)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj969.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj969)
   self.obj969.postAction( cobj0.RHS.CREATE )

   self.obj961.out_connections_.append(self.obj965)
   self.obj965.in_connections_.append(self.obj961)
   self.obj961.graphObject_.pendingConnections.append((self.obj961.graphObject_.tag, self.obj965.graphObject_.tag, [97.0, 82.0, 183.0, 70.5], 2, 0))
   self.obj961.out_connections_.append(self.obj966)
   self.obj966.in_connections_.append(self.obj961)
   self.obj961.graphObject_.pendingConnections.append((self.obj961.graphObject_.tag, self.obj966.graphObject_.tag, [97.0, 82.0, 93.0, 120.5], 2, 0))
   self.obj961.out_connections_.append(self.obj967)
   self.obj967.in_connections_.append(self.obj961)
   self.obj961.graphObject_.pendingConnections.append((self.obj961.graphObject_.tag, self.obj967.graphObject_.tag, [97.0, 82.0, 194.5, 111.5], 2, 0))
   self.obj964.out_connections_.append(self.obj968)
   self.obj968.in_connections_.append(self.obj964)
   self.obj964.graphObject_.pendingConnections.append((self.obj964.graphObject_.tag, self.obj968.graphObject_.tag, [311.0, 185.0, 202.5, 192.5], 2, 0))
   self.obj964.out_connections_.append(self.obj969)
   self.obj969.in_connections_.append(self.obj964)
   self.obj964.graphObject_.pendingConnections.append((self.obj964.graphObject_.tag, self.obj969.graphObject_.tag, [311.0, 140.0, 292.5, 100.0], 2, 0))
   self.obj965.out_connections_.append(self.obj963)
   self.obj963.in_connections_.append(self.obj965)
   self.obj965.graphObject_.pendingConnections.append((self.obj965.graphObject_.tag, self.obj963.graphObject_.tag, [291.0, 63.0, 183.0, 70.5], 2, 0))
   self.obj966.out_connections_.append(self.obj962)
   self.obj962.in_connections_.append(self.obj966)
   self.obj966.graphObject_.pendingConnections.append((self.obj966.graphObject_.tag, self.obj962.graphObject_.tag, [111.0, 163.0, 93.0, 120.5], 2, 0))
   self.obj967.out_connections_.append(self.obj964)
   self.obj964.in_connections_.append(self.obj967)
   self.obj967.graphObject_.pendingConnections.append((self.obj967.graphObject_.tag, self.obj964.graphObject_.tag, [311.0, 140.0, 194.5, 111.5], 2, 0))
   self.obj968.out_connections_.append(self.obj962)
   self.obj962.in_connections_.append(self.obj968)
   self.obj968.graphObject_.pendingConnections.append((self.obj968.graphObject_.tag, self.obj962.graphObject_.tag, [111.0, 203.0, 202.5, 192.5], 2, 0))
   self.obj969.out_connections_.append(self.obj963)
   self.obj963.in_connections_.append(self.obj969)
   self.obj969.graphObject_.pendingConnections.append((self.obj969.graphObject_.tag, self.obj963.graphObject_.tag, [291.0, 63.0, 292.5, 100.0], 2, 0))

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

   self.obj974=Agent(self)
   self.obj974.preAction( cobj0.LHS.CREATE )
   self.obj974.isGraphObjectVisual = True

   if(hasattr(self.obj974, '_setHierarchicalLink')):
     self.obj974._setHierarchicalLink(False)

   # price
   self.obj974.price.setValue(0)

   # name
   self.obj974.name.setValue('')
   self.obj974.name.setNone()

   self.obj974.GGLabel.setValue(1)
   self.obj974.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(40.0,40.0,self.obj974)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj974.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj974)
   self.obj974.postAction( cobj0.LHS.CREATE )

   self.obj975=Capabilitie(self)
   self.obj975.preAction( cobj0.LHS.CREATE )
   self.obj975.isGraphObjectVisual = True

   if(hasattr(self.obj975, '_setHierarchicalLink')):
     self.obj975._setHierarchicalLink(False)

   # name
   self.obj975.name.setValue('')
   self.obj975.name.setNone()

   self.obj975.GGLabel.setValue(3)
   self.obj975.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(300.0,20.0,self.obj975)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj975.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj975)
   self.obj975.postAction( cobj0.LHS.CREATE )

   self.obj976=Capabilitie(self)
   self.obj976.preAction( cobj0.LHS.CREATE )
   self.obj976.isGraphObjectVisual = True

   if(hasattr(self.obj976, '_setHierarchicalLink')):
     self.obj976._setHierarchicalLink(False)

   # name
   self.obj976.name.setValue('')
   self.obj976.name.setNone()

   self.obj976.GGLabel.setValue(4)
   self.obj976.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(100.0,160.0,self.obj976)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj976.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj976)
   self.obj976.postAction( cobj0.LHS.CREATE )

   self.obj977=Role(self)
   self.obj977.preAction( cobj0.LHS.CREATE )
   self.obj977.isGraphObjectVisual = True

   if(hasattr(self.obj977, '_setHierarchicalLink')):
     self.obj977._setHierarchicalLink(False)

   # name
   self.obj977.name.setValue('')
   self.obj977.name.setNone()

   self.obj977.GGLabel.setValue(2)
   self.obj977.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(300.0,120.0,self.obj977)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj977.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj977)
   self.obj977.postAction( cobj0.LHS.CREATE )

   self.obj978=posses(self)
   self.obj978.preAction( cobj0.LHS.CREATE )
   self.obj978.isGraphObjectVisual = True

   if(hasattr(self.obj978, '_setHierarchicalLink')):
     self.obj978._setHierarchicalLink(False)

   # rate
   self.obj978.rate.setValue(0.0)

   self.obj978.GGLabel.setValue(5)
   self.obj978.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(93.0,130.5,self.obj978)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj978.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj978)
   self.obj978.postAction( cobj0.LHS.CREATE )

   self.obj979=CapableOf(self)
   self.obj979.preAction( cobj0.LHS.CREATE )
   self.obj979.isGraphObjectVisual = True

   if(hasattr(self.obj979, '_setHierarchicalLink')):
     self.obj979._setHierarchicalLink(False)

   self.obj979.GGLabel.setValue(6)
   self.obj979.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(194.5,111.5,self.obj979)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj979.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj979)
   self.obj979.postAction( cobj0.LHS.CREATE )

   self.obj980=requir(self)
   self.obj980.preAction( cobj0.LHS.CREATE )
   self.obj980.isGraphObjectVisual = True

   if(hasattr(self.obj980, '_setHierarchicalLink')):
     self.obj980._setHierarchicalLink(False)

   self.obj980.GGLabel.setValue(7)
   self.obj980.graphClass_= graph_requir
   if self.genGraphics:
      new_obj = graph_requir(222.5,162.5,self.obj980)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj980.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj980)
   self.obj980.postAction( cobj0.LHS.CREATE )

   self.obj981=requir(self)
   self.obj981.preAction( cobj0.LHS.CREATE )
   self.obj981.isGraphObjectVisual = True

   if(hasattr(self.obj981, '_setHierarchicalLink')):
     self.obj981._setHierarchicalLink(False)

   self.obj981.GGLabel.setValue(8)
   self.obj981.graphClass_= graph_requir
   if self.genGraphics:
      new_obj = graph_requir(322.5,90.0,self.obj981)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj981.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj981)
   self.obj981.postAction( cobj0.LHS.CREATE )

   self.obj974.out_connections_.append(self.obj978)
   self.obj978.in_connections_.append(self.obj974)
   self.obj974.graphObject_.pendingConnections.append((self.obj974.graphObject_.tag, self.obj978.graphObject_.tag, [77.0, 102.0, 93.0, 130.5], 2, 0))
   self.obj974.out_connections_.append(self.obj979)
   self.obj979.in_connections_.append(self.obj974)
   self.obj974.graphObject_.pendingConnections.append((self.obj974.graphObject_.tag, self.obj979.graphObject_.tag, [65.0, 102.0, 194.5, 111.5], 0, True))
   self.obj977.out_connections_.append(self.obj980)
   self.obj980.in_connections_.append(self.obj977)
   self.obj977.graphObject_.pendingConnections.append((self.obj977.graphObject_.tag, self.obj980.graphObject_.tag, [324.0, 166.0, 222.5, 162.5], 0, True))
   self.obj977.out_connections_.append(self.obj981)
   self.obj981.in_connections_.append(self.obj977)
   self.obj977.graphObject_.pendingConnections.append((self.obj977.graphObject_.tag, self.obj981.graphObject_.tag, [324.0, 121.0, 322.5, 90.0], 0, True))
   self.obj978.out_connections_.append(self.obj976)
   self.obj976.in_connections_.append(self.obj978)
   self.obj978.graphObject_.pendingConnections.append((self.obj978.graphObject_.tag, self.obj976.graphObject_.tag, [121.0, 159.0, 93.0, 130.5], 0, True))
   self.obj979.out_connections_.append(self.obj977)
   self.obj977.in_connections_.append(self.obj979)
   self.obj979.graphObject_.pendingConnections.append((self.obj979.graphObject_.tag, self.obj977.graphObject_.tag, [331.0, 120.0, 194.5, 111.5], 2, 0))
   self.obj980.out_connections_.append(self.obj976)
   self.obj976.in_connections_.append(self.obj980)
   self.obj980.graphObject_.pendingConnections.append((self.obj980.graphObject_.tag, self.obj976.graphObject_.tag, [121.0, 159.0, 222.5, 162.5], 0, True))
   self.obj981.out_connections_.append(self.obj975)
   self.obj975.in_connections_.append(self.obj981)
   self.obj981.graphObject_.pendingConnections.append((self.obj981.graphObject_.tag, self.obj975.graphObject_.tag, [321.0, 59.0, 322.5, 90.0], 0, True))

   cobj0.RHS = ASG_omacss(self)

   self.obj983=Agent(self)
   self.obj983.preAction( cobj0.RHS.CREATE )
   self.obj983.isGraphObjectVisual = True

   if(hasattr(self.obj983, '_setHierarchicalLink')):
     self.obj983._setHierarchicalLink(False)

   # price
   self.obj983.price.setValue(0)

   # name
   self.obj983.name.setValue('')
   self.obj983.name.setNone()

   self.obj983.GGLabel.setValue(1)
   self.obj983.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(40.0,40.0,self.obj983)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj983.graphObject_ = new_obj
   self.obj9830= AttrCalc()
   self.obj9830.Copy=ATOM3Boolean()
   self.obj9830.Copy.setValue(('Copy from LHS', 1))
   self.obj9830.Copy.config = 0
   self.obj9830.Specify=ATOM3Constraint()
   self.obj9830.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj983.GGset2Any['price']= self.obj9830
   self.obj9831= AttrCalc()
   self.obj9831.Copy=ATOM3Boolean()
   self.obj9831.Copy.setValue(('Copy from LHS', 1))
   self.obj9831.Copy.config = 0
   self.obj9831.Specify=ATOM3Constraint()
   self.obj9831.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj983.GGset2Any['name']= self.obj9831

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj983)
   self.obj983.postAction( cobj0.RHS.CREATE )

   self.obj984=Capabilitie(self)
   self.obj984.preAction( cobj0.RHS.CREATE )
   self.obj984.isGraphObjectVisual = True

   if(hasattr(self.obj984, '_setHierarchicalLink')):
     self.obj984._setHierarchicalLink(False)

   # name
   self.obj984.name.setValue('')
   self.obj984.name.setNone()

   self.obj984.GGLabel.setValue(3)
   self.obj984.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(300.0,20.0,self.obj984)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj984.graphObject_ = new_obj
   self.obj9840= AttrCalc()
   self.obj9840.Copy=ATOM3Boolean()
   self.obj9840.Copy.setValue(('Copy from LHS', 1))
   self.obj9840.Copy.config = 0
   self.obj9840.Specify=ATOM3Constraint()
   self.obj9840.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj984.GGset2Any['name']= self.obj9840

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj984)
   self.obj984.postAction( cobj0.RHS.CREATE )

   self.obj985=Capabilitie(self)
   self.obj985.preAction( cobj0.RHS.CREATE )
   self.obj985.isGraphObjectVisual = True

   if(hasattr(self.obj985, '_setHierarchicalLink')):
     self.obj985._setHierarchicalLink(False)

   # name
   self.obj985.name.setValue('')
   self.obj985.name.setNone()

   self.obj985.GGLabel.setValue(4)
   self.obj985.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(100.0,160.0,self.obj985)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj985.graphObject_ = new_obj
   self.obj9850= AttrCalc()
   self.obj9850.Copy=ATOM3Boolean()
   self.obj9850.Copy.setValue(('Copy from LHS', 1))
   self.obj9850.Copy.config = 0
   self.obj9850.Specify=ATOM3Constraint()
   self.obj9850.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj985.GGset2Any['name']= self.obj9850

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj985)
   self.obj985.postAction( cobj0.RHS.CREATE )

   self.obj986=Role(self)
   self.obj986.preAction( cobj0.RHS.CREATE )
   self.obj986.isGraphObjectVisual = True

   if(hasattr(self.obj986, '_setHierarchicalLink')):
     self.obj986._setHierarchicalLink(False)

   # name
   self.obj986.name.setValue('')
   self.obj986.name.setNone()

   self.obj986.GGLabel.setValue(2)
   self.obj986.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(300.0,120.0,self.obj986)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj986.graphObject_ = new_obj
   self.obj9860= AttrCalc()
   self.obj9860.Copy=ATOM3Boolean()
   self.obj9860.Copy.setValue(('Copy from LHS', 1))
   self.obj9860.Copy.config = 0
   self.obj9860.Specify=ATOM3Constraint()
   self.obj9860.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj986.GGset2Any['name']= self.obj9860

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj986)
   self.obj986.postAction( cobj0.RHS.CREATE )

   self.obj987=posses(self)
   self.obj987.preAction( cobj0.RHS.CREATE )
   self.obj987.isGraphObjectVisual = True

   if(hasattr(self.obj987, '_setHierarchicalLink')):
     self.obj987._setHierarchicalLink(False)

   # rate
   self.obj987.rate.setValue(0.0)

   self.obj987.GGLabel.setValue(5)
   self.obj987.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(93.0,130.5,self.obj987)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj987.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj987)
   self.obj987.postAction( cobj0.RHS.CREATE )

   self.obj988=requir(self)
   self.obj988.preAction( cobj0.RHS.CREATE )
   self.obj988.isGraphObjectVisual = True

   if(hasattr(self.obj988, '_setHierarchicalLink')):
     self.obj988._setHierarchicalLink(False)

   self.obj988.GGLabel.setValue(7)
   self.obj988.graphClass_= graph_requir
   if self.genGraphics:
      new_obj = graph_requir(222.5,162.5,self.obj988)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj988.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj988)
   self.obj988.postAction( cobj0.RHS.CREATE )

   self.obj989=requir(self)
   self.obj989.preAction( cobj0.RHS.CREATE )
   self.obj989.isGraphObjectVisual = True

   if(hasattr(self.obj989, '_setHierarchicalLink')):
     self.obj989._setHierarchicalLink(False)

   self.obj989.GGLabel.setValue(8)
   self.obj989.graphClass_= graph_requir
   if self.genGraphics:
      new_obj = graph_requir(322.5,90.0,self.obj989)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj989.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj989)
   self.obj989.postAction( cobj0.RHS.CREATE )

   self.obj983.out_connections_.append(self.obj987)
   self.obj987.in_connections_.append(self.obj983)
   self.obj983.graphObject_.pendingConnections.append((self.obj983.graphObject_.tag, self.obj987.graphObject_.tag, [77.0, 102.0, 93.0, 130.5], 2, 0))
   self.obj986.out_connections_.append(self.obj988)
   self.obj988.in_connections_.append(self.obj986)
   self.obj986.graphObject_.pendingConnections.append((self.obj986.graphObject_.tag, self.obj988.graphObject_.tag, [331.0, 165.0, 222.5, 162.5], 2, 0))
   self.obj986.out_connections_.append(self.obj989)
   self.obj989.in_connections_.append(self.obj986)
   self.obj986.graphObject_.pendingConnections.append((self.obj986.graphObject_.tag, self.obj989.graphObject_.tag, [331.0, 120.0, 322.5, 90.0], 2, 0))
   self.obj987.out_connections_.append(self.obj985)
   self.obj985.in_connections_.append(self.obj987)
   self.obj987.graphObject_.pendingConnections.append((self.obj987.graphObject_.tag, self.obj985.graphObject_.tag, [131.0, 163.0, 93.0, 130.5], 2, 0))
   self.obj988.out_connections_.append(self.obj985)
   self.obj985.in_connections_.append(self.obj988)
   self.obj988.graphObject_.pendingConnections.append((self.obj988.graphObject_.tag, self.obj985.graphObject_.tag, [131.0, 163.0, 222.5, 162.5], 2, 0))
   self.obj989.out_connections_.append(self.obj984)
   self.obj984.in_connections_.append(self.obj989)
   self.obj989.graphObject_.pendingConnections.append((self.obj989.graphObject_.tag, self.obj984.graphObject_.tag, [331.0, 63.0, 322.5, 90.0], 2, 0))

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

   self.obj995=Agent(self)
   self.obj995.preAction( cobj0.LHS.CREATE )
   self.obj995.isGraphObjectVisual = True

   if(hasattr(self.obj995, '_setHierarchicalLink')):
     self.obj995._setHierarchicalLink(False)

   # price
   self.obj995.price.setValue(0)

   # name
   self.obj995.name.setValue('')
   self.obj995.name.setNone()

   self.obj995.GGLabel.setValue(1)
   self.obj995.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(60.0,20.0,self.obj995)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj995.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj995)
   self.obj995.postAction( cobj0.LHS.CREATE )

   self.obj996=Role(self)
   self.obj996.preAction( cobj0.LHS.CREATE )
   self.obj996.isGraphObjectVisual = True

   if(hasattr(self.obj996, '_setHierarchicalLink')):
     self.obj996._setHierarchicalLink(False)

   # name
   self.obj996.name.setValue('')
   self.obj996.name.setNone()

   self.obj996.GGLabel.setValue(2)
   self.obj996.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(240.0,100.0,self.obj996)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj996.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj996)
   self.obj996.postAction( cobj0.LHS.CREATE )

   self.obj997=CapableOf(self)
   self.obj997.preAction( cobj0.LHS.CREATE )
   self.obj997.isGraphObjectVisual = True

   if(hasattr(self.obj997, '_setHierarchicalLink')):
     self.obj997._setHierarchicalLink(False)

   self.obj997.GGLabel.setValue(3)
   self.obj997.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(170.0,88.5,self.obj997)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj997.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj997)
   self.obj997.postAction( cobj0.LHS.CREATE )

   self.obj995.out_connections_.append(self.obj997)
   self.obj997.in_connections_.append(self.obj995)
   self.obj995.graphObject_.pendingConnections.append((self.obj995.graphObject_.tag, self.obj997.graphObject_.tag, [85.0, 82.0, 109.0, 127.0, 170.0, 88.5], 2, True))
   self.obj997.out_connections_.append(self.obj996)
   self.obj996.in_connections_.append(self.obj997)
   self.obj997.graphObject_.pendingConnections.append((self.obj997.graphObject_.tag, self.obj996.graphObject_.tag, [264.0, 101.0, 231.0, 50.0, 170.0, 88.5], 2, True))

   cobj0.RHS = ASG_omacss(self)
   cobj0.RHS.merge(ASG_pns2(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj1001=Agent(self)
   self.obj1001.preAction( cobj0.RHS.CREATE )
   self.obj1001.isGraphObjectVisual = True

   if(hasattr(self.obj1001, '_setHierarchicalLink')):
     self.obj1001._setHierarchicalLink(False)

   # price
   self.obj1001.price.setValue(0)

   # name
   self.obj1001.name.setValue('')
   self.obj1001.name.setNone()

   self.obj1001.GGLabel.setValue(1)
   self.obj1001.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(60.0,20.0,self.obj1001)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1001.graphObject_ = new_obj
   self.obj10010= AttrCalc()
   self.obj10010.Copy=ATOM3Boolean()
   self.obj10010.Copy.setValue(('Copy from LHS', 1))
   self.obj10010.Copy.config = 0
   self.obj10010.Specify=ATOM3Constraint()
   self.obj10010.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1001.GGset2Any['price']= self.obj10010
   self.obj10011= AttrCalc()
   self.obj10011.Copy=ATOM3Boolean()
   self.obj10011.Copy.setValue(('Copy from LHS', 1))
   self.obj10011.Copy.config = 0
   self.obj10011.Specify=ATOM3Constraint()
   self.obj10011.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1001.GGset2Any['name']= self.obj10011

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1001)
   self.obj1001.postAction( cobj0.RHS.CREATE )

   self.obj1002=Role(self)
   self.obj1002.preAction( cobj0.RHS.CREATE )
   self.obj1002.isGraphObjectVisual = True

   if(hasattr(self.obj1002, '_setHierarchicalLink')):
     self.obj1002._setHierarchicalLink(False)

   # name
   self.obj1002.name.setValue('')
   self.obj1002.name.setNone()

   self.obj1002.GGLabel.setValue(2)
   self.obj1002.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(240.0,100.0,self.obj1002)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1002.graphObject_ = new_obj
   self.obj10020= AttrCalc()
   self.obj10020.Copy=ATOM3Boolean()
   self.obj10020.Copy.setValue(('Copy from LHS', 1))
   self.obj10020.Copy.config = 0
   self.obj10020.Specify=ATOM3Constraint()
   self.obj10020.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1002.GGset2Any['name']= self.obj10020

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1002)
   self.obj1002.postAction( cobj0.RHS.CREATE )

   self.obj1003=CapableOf(self)
   self.obj1003.preAction( cobj0.RHS.CREATE )
   self.obj1003.isGraphObjectVisual = True

   if(hasattr(self.obj1003, '_setHierarchicalLink')):
     self.obj1003._setHierarchicalLink(False)

   self.obj1003.GGLabel.setValue(3)
   self.obj1003.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(170.0,88.5,self.obj1003)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1003.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1003)
   self.obj1003.postAction( cobj0.RHS.CREATE )

   self.obj1004=rawMaterial(self)
   self.obj1004.preAction( cobj0.RHS.CREATE )
   self.obj1004.isGraphObjectVisual = True

   if(hasattr(self.obj1004, '_setHierarchicalLink')):
     self.obj1004._setHierarchicalLink(False)

   # Name
   self.obj1004.Name.setValue('')
   self.obj1004.Name.setNone()

   self.obj1004.GGLabel.setValue(5)
   self.obj1004.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(20.0,140.0,self.obj1004)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1004.graphObject_ = new_obj
   self.obj10040= AttrCalc()
   self.obj10040.Copy=ATOM3Boolean()
   self.obj10040.Copy.setValue(('Copy from LHS', 0))
   self.obj10040.Copy.config = 0
   self.obj10040.Specify=ATOM3Constraint()
   self.obj10040.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()\n'))
   self.obj1004.GGset2Any['Name']= self.obj10040

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1004)
   self.obj1004.postAction( cobj0.RHS.CREATE )

   self.obj1005=GenericGraphEdge(self)
   self.obj1005.preAction( cobj0.RHS.CREATE )
   self.obj1005.isGraphObjectVisual = True

   if(hasattr(self.obj1005, '_setHierarchicalLink')):
     self.obj1005._setHierarchicalLink(False)

   self.obj1005.GGLabel.setValue(6)
   self.obj1005.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(93.5,165.0,self.obj1005)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1005.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1005)
   self.obj1005.postAction( cobj0.RHS.CREATE )

   self.obj1001.out_connections_.append(self.obj1003)
   self.obj1003.in_connections_.append(self.obj1001)
   self.obj1001.graphObject_.pendingConnections.append((self.obj1001.graphObject_.tag, self.obj1003.graphObject_.tag, [97.0, 82.0, 170.0, 88.5], 2, 0))
   self.obj1001.out_connections_.append(self.obj1005)
   self.obj1005.in_connections_.append(self.obj1001)
   self.obj1001.graphObject_.pendingConnections.append((self.obj1001.graphObject_.tag, self.obj1005.graphObject_.tag, [97.0, 82.0, 67.0, 166.0, 93.5, 165.0], 2, True))
   self.obj1003.out_connections_.append(self.obj1002)
   self.obj1002.in_connections_.append(self.obj1003)
   self.obj1003.graphObject_.pendingConnections.append((self.obj1003.graphObject_.tag, self.obj1002.graphObject_.tag, [271.0, 100.0, 170.0, 88.5], 2, 0))
   self.obj1005.out_connections_.append(self.obj1004)
   self.obj1004.in_connections_.append(self.obj1005)
   self.obj1005.graphObject_.pendingConnections.append((self.obj1005.graphObject_.tag, self.obj1004.graphObject_.tag, [44.0, 193.0, 120.0, 164.0, 93.5, 165.0], 2, True))

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

   self.obj1010=Agent(self)
   self.obj1010.preAction( cobj0.LHS.CREATE )
   self.obj1010.isGraphObjectVisual = True

   if(hasattr(self.obj1010, '_setHierarchicalLink')):
     self.obj1010._setHierarchicalLink(False)

   # price
   self.obj1010.price.setNone()

   # name
   self.obj1010.name.setValue('')
   self.obj1010.name.setNone()

   self.obj1010.GGLabel.setValue(1)
   self.obj1010.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(60.0,60.0,self.obj1010)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1010.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1010)
   self.obj1010.postAction( cobj0.LHS.CREATE )

   self.obj1011=Role(self)
   self.obj1011.preAction( cobj0.LHS.CREATE )
   self.obj1011.isGraphObjectVisual = True

   if(hasattr(self.obj1011, '_setHierarchicalLink')):
     self.obj1011._setHierarchicalLink(False)

   # name
   self.obj1011.name.setValue('')
   self.obj1011.name.setNone()

   self.obj1011.GGLabel.setValue(2)
   self.obj1011.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(320.0,140.0,self.obj1011)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1011.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1011)
   self.obj1011.postAction( cobj0.LHS.CREATE )

   self.obj1012=CapableOf(self)
   self.obj1012.preAction( cobj0.LHS.CREATE )
   self.obj1012.isGraphObjectVisual = True

   if(hasattr(self.obj1012, '_setHierarchicalLink')):
     self.obj1012._setHierarchicalLink(False)

   self.obj1012.GGLabel.setValue(3)
   self.obj1012.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(207.0,130.0,self.obj1012)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1012.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1012)
   self.obj1012.postAction( cobj0.LHS.CREATE )

   self.obj1010.out_connections_.append(self.obj1012)
   self.obj1012.in_connections_.append(self.obj1010)
   self.obj1010.graphObject_.pendingConnections.append((self.obj1010.graphObject_.tag, self.obj1012.graphObject_.tag, [85.0, 122.0, 117.0, 172.0, 207.0, 130.0], 2, True))
   self.obj1012.out_connections_.append(self.obj1011)
   self.obj1011.in_connections_.append(self.obj1012)
   self.obj1012.graphObject_.pendingConnections.append((self.obj1012.graphObject_.tag, self.obj1011.graphObject_.tag, [344.0, 141.0, 297.0, 88.0, 207.0, 130.0], 2, True))

   cobj0.RHS = ASG_omacss(self)
   cobj0.RHS.merge(ASG_pns2(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj1016=Agent(self)
   self.obj1016.preAction( cobj0.RHS.CREATE )
   self.obj1016.isGraphObjectVisual = True

   if(hasattr(self.obj1016, '_setHierarchicalLink')):
     self.obj1016._setHierarchicalLink(False)

   # price
   self.obj1016.price.setNone()

   # name
   self.obj1016.name.setValue('')
   self.obj1016.name.setNone()

   self.obj1016.GGLabel.setValue(1)
   self.obj1016.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(60.0,60.0,self.obj1016)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1016.graphObject_ = new_obj
   self.obj10160= AttrCalc()
   self.obj10160.Copy=ATOM3Boolean()
   self.obj10160.Copy.setValue(('Copy from LHS', 1))
   self.obj10160.Copy.config = 0
   self.obj10160.Specify=ATOM3Constraint()
   self.obj10160.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1016.GGset2Any['price']= self.obj10160
   self.obj10161= AttrCalc()
   self.obj10161.Copy=ATOM3Boolean()
   self.obj10161.Copy.setValue(('Copy from LHS', 1))
   self.obj10161.Copy.config = 0
   self.obj10161.Specify=ATOM3Constraint()
   self.obj10161.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1016.GGset2Any['name']= self.obj10161

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1016)
   self.obj1016.postAction( cobj0.RHS.CREATE )

   self.obj1017=Role(self)
   self.obj1017.preAction( cobj0.RHS.CREATE )
   self.obj1017.isGraphObjectVisual = True

   if(hasattr(self.obj1017, '_setHierarchicalLink')):
     self.obj1017._setHierarchicalLink(False)

   # name
   self.obj1017.name.setValue('')
   self.obj1017.name.setNone()

   self.obj1017.GGLabel.setValue(2)
   self.obj1017.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(320.0,140.0,self.obj1017)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1017.graphObject_ = new_obj
   self.obj10170= AttrCalc()
   self.obj10170.Copy=ATOM3Boolean()
   self.obj10170.Copy.setValue(('Copy from LHS', 1))
   self.obj10170.Copy.config = 0
   self.obj10170.Specify=ATOM3Constraint()
   self.obj10170.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1017.GGset2Any['name']= self.obj10170

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1017)
   self.obj1017.postAction( cobj0.RHS.CREATE )

   self.obj1018=CapableOf(self)
   self.obj1018.preAction( cobj0.RHS.CREATE )
   self.obj1018.isGraphObjectVisual = True

   if(hasattr(self.obj1018, '_setHierarchicalLink')):
     self.obj1018._setHierarchicalLink(False)

   self.obj1018.GGLabel.setValue(3)
   self.obj1018.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(207.0,130.0,self.obj1018)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1018.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1018)
   self.obj1018.postAction( cobj0.RHS.CREATE )

   self.obj1019=operatingUnit(self)
   self.obj1019.preAction( cobj0.RHS.CREATE )
   self.obj1019.isGraphObjectVisual = True

   if(hasattr(self.obj1019, '_setHierarchicalLink')):
     self.obj1019._setHierarchicalLink(False)

   # name
   self.obj1019.name.setValue('')
   self.obj1019.name.setNone()

   self.obj1019.GGLabel.setValue(6)
   self.obj1019.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(220.0,80.0,self.obj1019)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1019.graphObject_ = new_obj
   self.obj10190= AttrCalc()
   self.obj10190.Copy=ATOM3Boolean()
   self.obj10190.Copy.setValue(('Copy from LHS', 0))
   self.obj10190.Copy.config = 0
   self.obj10190.Specify=ATOM3Constraint()
   self.obj10190.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()+\' \'+self.getMatched(graphID, self.LHS.nodeWithLabel(2)).name.getValue()\n\n\n\n'))
   self.obj1019.GGset2Any['name']= self.obj10190

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1019)
   self.obj1019.postAction( cobj0.RHS.CREATE )

   self.obj1020=GenericGraphEdge(self)
   self.obj1020.preAction( cobj0.RHS.CREATE )
   self.obj1020.isGraphObjectVisual = True

   if(hasattr(self.obj1020, '_setHierarchicalLink')):
     self.obj1020._setHierarchicalLink(False)

   self.obj1020.GGLabel.setValue(7)
   self.obj1020.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(196.5,66.5,self.obj1020)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1020.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1020)
   self.obj1020.postAction( cobj0.RHS.CREATE )

   self.obj1016.out_connections_.append(self.obj1018)
   self.obj1018.in_connections_.append(self.obj1016)
   self.obj1016.graphObject_.pendingConnections.append((self.obj1016.graphObject_.tag, self.obj1018.graphObject_.tag, [97.0, 122.0, 207.0, 130.0], 2, 0))
   self.obj1016.out_connections_.append(self.obj1020)
   self.obj1020.in_connections_.append(self.obj1016)
   self.obj1016.graphObject_.pendingConnections.append((self.obj1016.graphObject_.tag, self.obj1020.graphObject_.tag, [97.0, 122.0, 173.0, 79.0, 167.0, 103.0, 196.5, 66.5], 4, True))
   self.obj1018.out_connections_.append(self.obj1017)
   self.obj1017.in_connections_.append(self.obj1018)
   self.obj1018.graphObject_.pendingConnections.append((self.obj1018.graphObject_.tag, self.obj1017.graphObject_.tag, [351.0, 140.0, 207.0, 130.0], 2, 0))
   self.obj1020.out_connections_.append(self.obj1019)
   self.obj1019.in_connections_.append(self.obj1020)
   self.obj1020.graphObject_.pendingConnections.append((self.obj1020.graphObject_.tag, self.obj1019.graphObject_.tag, [261.32710280373834, 87.47368421052629, 220.0, 54.0, 261.0, 53.0, 196.5, 66.5], 4, True))

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

   self.obj1025=Goal(self)
   self.obj1025.preAction( cobj0.LHS.CREATE )
   self.obj1025.isGraphObjectVisual = True

   if(hasattr(self.obj1025, '_setHierarchicalLink')):
     self.obj1025._setHierarchicalLink(False)

   # name
   self.obj1025.name.setValue('')
   self.obj1025.name.setNone()

   self.obj1025.GGLabel.setValue(1)
   self.obj1025.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(100.0,80.0,self.obj1025)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1025.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1025)
   self.obj1025.postAction( cobj0.LHS.CREATE )


   cobj0.RHS = ASG_omacss(self)
   cobj0.RHS.merge(ASG_pns2(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj1029=Goal(self)
   self.obj1029.preAction( cobj0.RHS.CREATE )
   self.obj1029.isGraphObjectVisual = True

   if(hasattr(self.obj1029, '_setHierarchicalLink')):
     self.obj1029._setHierarchicalLink(False)

   # name
   self.obj1029.name.setValue('')
   self.obj1029.name.setNone()

   self.obj1029.GGLabel.setValue(1)
   self.obj1029.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(60.0,80.0,self.obj1029)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1029.graphObject_ = new_obj
   self.obj10290= AttrCalc()
   self.obj10290.Copy=ATOM3Boolean()
   self.obj10290.Copy.setValue(('Copy from LHS', 1))
   self.obj10290.Copy.config = 0
   self.obj10290.Specify=ATOM3Constraint()
   self.obj10290.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1029.GGset2Any['name']= self.obj10290

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1029)
   self.obj1029.postAction( cobj0.RHS.CREATE )

   self.obj1030=metarial(self)
   self.obj1030.preAction( cobj0.RHS.CREATE )
   self.obj1030.isGraphObjectVisual = True

   if(hasattr(self.obj1030, '_setHierarchicalLink')):
     self.obj1030._setHierarchicalLink(False)

   # Name
   self.obj1030.Name.setValue('')
   self.obj1030.Name.setNone()

   self.obj1030.GGLabel.setValue(3)
   self.obj1030.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(220.0,80.0,self.obj1030)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1030.graphObject_ = new_obj
   self.obj10300= AttrCalc()
   self.obj10300.Copy=ATOM3Boolean()
   self.obj10300.Copy.setValue(('Copy from LHS', 0))
   self.obj10300.Copy.config = 0
   self.obj10300.Specify=ATOM3Constraint()
   self.obj10300.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()\n'))
   self.obj1030.GGset2Any['Name']= self.obj10300

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1030)
   self.obj1030.postAction( cobj0.RHS.CREATE )

   self.obj1031=GenericGraphEdge(self)
   self.obj1031.preAction( cobj0.RHS.CREATE )
   self.obj1031.isGraphObjectVisual = True

   if(hasattr(self.obj1031, '_setHierarchicalLink')):
     self.obj1031._setHierarchicalLink(False)

   self.obj1031.GGLabel.setValue(4)
   self.obj1031.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(162.0,127.0,self.obj1031)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1031.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1031)
   self.obj1031.postAction( cobj0.RHS.CREATE )

   self.obj1029.out_connections_.append(self.obj1031)
   self.obj1031.in_connections_.append(self.obj1029)
   self.obj1029.graphObject_.pendingConnections.append((self.obj1029.graphObject_.tag, self.obj1031.graphObject_.tag, [94.0, 130.0, 162.0, 127.0], 0, True))
   self.obj1031.out_connections_.append(self.obj1030)
   self.obj1030.in_connections_.append(self.obj1031)
   self.obj1031.graphObject_.pendingConnections.append((self.obj1031.graphObject_.tag, self.obj1030.graphObject_.tag, [230.0, 124.0, 162.0, 127.0], 0, True))

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

   self.obj1038=Agent(self)
   self.obj1038.preAction( cobj0.LHS.CREATE )
   self.obj1038.isGraphObjectVisual = True

   if(hasattr(self.obj1038, '_setHierarchicalLink')):
     self.obj1038._setHierarchicalLink(False)

   # price
   self.obj1038.price.setValue(0)

   # name
   self.obj1038.name.setValue('')
   self.obj1038.name.setNone()

   self.obj1038.GGLabel.setValue(1)
   self.obj1038.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(100.0,40.0,self.obj1038)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1038.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1038)
   self.obj1038.postAction( cobj0.LHS.CREATE )

   self.obj1039=rawMaterial(self)
   self.obj1039.preAction( cobj0.LHS.CREATE )
   self.obj1039.isGraphObjectVisual = True

   if(hasattr(self.obj1039, '_setHierarchicalLink')):
     self.obj1039._setHierarchicalLink(False)

   # Name
   self.obj1039.Name.setValue('')
   self.obj1039.Name.setNone()

   self.obj1039.GGLabel.setValue(3)
   self.obj1039.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(280.0,20.0,self.obj1039)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1039.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1039)
   self.obj1039.postAction( cobj0.LHS.CREATE )

   self.obj1040=operatingUnit(self)
   self.obj1040.preAction( cobj0.LHS.CREATE )
   self.obj1040.isGraphObjectVisual = True

   if(hasattr(self.obj1040, '_setHierarchicalLink')):
     self.obj1040._setHierarchicalLink(False)

   # name
   self.obj1040.name.setValue('')
   self.obj1040.name.setNone()

   self.obj1040.GGLabel.setValue(2)
   self.obj1040.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(260.0,160.0,self.obj1040)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1040.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1040)
   self.obj1040.postAction( cobj0.LHS.CREATE )

   self.obj1041=GenericGraphEdge(self)
   self.obj1041.preAction( cobj0.LHS.CREATE )
   self.obj1041.isGraphObjectVisual = True

   if(hasattr(self.obj1041, '_setHierarchicalLink')):
     self.obj1041._setHierarchicalLink(False)

   self.obj1041.GGLabel.setValue(4)
   self.obj1041.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(214.75,92.75,self.obj1041)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1041.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1041)
   self.obj1041.postAction( cobj0.LHS.CREATE )

   self.obj1042=GenericGraphEdge(self)
   self.obj1042.preAction( cobj0.LHS.CREATE )
   self.obj1042.isGraphObjectVisual = True

   if(hasattr(self.obj1042, '_setHierarchicalLink')):
     self.obj1042._setHierarchicalLink(False)

   self.obj1042.GGLabel.setValue(5)
   self.obj1042.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(241.642523364,131.105263158,self.obj1042)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1042.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1042)
   self.obj1042.postAction( cobj0.LHS.CREATE )

   self.obj1038.out_connections_.append(self.obj1041)
   self.obj1041.in_connections_.append(self.obj1038)
   self.obj1038.graphObject_.pendingConnections.append((self.obj1038.graphObject_.tag, self.obj1041.graphObject_.tag, [125.0, 102.0, 170.0, 100.0, 214.75, 92.75], 2, True))
   self.obj1038.out_connections_.append(self.obj1042)
   self.obj1042.in_connections_.append(self.obj1038)
   self.obj1038.graphObject_.pendingConnections.append((self.obj1038.graphObject_.tag, self.obj1042.graphObject_.tag, [125.0, 102.0, 204.5, 114.5, 241.64252336448598, 131.10526315789474], 2, True))
   self.obj1041.out_connections_.append(self.obj1039)
   self.obj1039.in_connections_.append(self.obj1041)
   self.obj1041.graphObject_.pendingConnections.append((self.obj1041.graphObject_.tag, self.obj1039.graphObject_.tag, [304.0, 73.0, 259.5, 85.5, 214.75, 92.75], 2, True))
   self.obj1042.out_connections_.append(self.obj1040)
   self.obj1040.in_connections_.append(self.obj1042)
   self.obj1042.graphObject_.pendingConnections.append((self.obj1042.graphObject_.tag, self.obj1040.graphObject_.tag, [273.5700934579439, 168.42105263157896, 278.78504672897196, 147.71052631578948, 241.64252336448598, 131.10526315789474], 2, True))

   cobj0.RHS = ASG_omacss(self)
   cobj0.RHS.merge(ASG_pns2(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj1046=Agent(self)
   self.obj1046.preAction( cobj0.RHS.CREATE )
   self.obj1046.isGraphObjectVisual = True

   if(hasattr(self.obj1046, '_setHierarchicalLink')):
     self.obj1046._setHierarchicalLink(False)

   # price
   self.obj1046.price.setValue(0)

   # name
   self.obj1046.name.setValue('')
   self.obj1046.name.setNone()

   self.obj1046.GGLabel.setValue(1)
   self.obj1046.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(60.0,60.0,self.obj1046)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1046.graphObject_ = new_obj
   self.obj10460= AttrCalc()
   self.obj10460.Copy=ATOM3Boolean()
   self.obj10460.Copy.setValue(('Copy from LHS', 1))
   self.obj10460.Copy.config = 0
   self.obj10460.Specify=ATOM3Constraint()
   self.obj10460.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1046.GGset2Any['price']= self.obj10460
   self.obj10461= AttrCalc()
   self.obj10461.Copy=ATOM3Boolean()
   self.obj10461.Copy.setValue(('Copy from LHS', 1))
   self.obj10461.Copy.config = 0
   self.obj10461.Specify=ATOM3Constraint()
   self.obj10461.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1046.GGset2Any['name']= self.obj10461

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1046)
   self.obj1046.postAction( cobj0.RHS.CREATE )

   self.obj1047=rawMaterial(self)
   self.obj1047.preAction( cobj0.RHS.CREATE )
   self.obj1047.isGraphObjectVisual = True

   if(hasattr(self.obj1047, '_setHierarchicalLink')):
     self.obj1047._setHierarchicalLink(False)

   # Name
   self.obj1047.Name.setValue('')
   self.obj1047.Name.setNone()

   self.obj1047.GGLabel.setValue(3)
   self.obj1047.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(240.0,20.0,self.obj1047)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1047.graphObject_ = new_obj
   self.obj10470= AttrCalc()
   self.obj10470.Copy=ATOM3Boolean()
   self.obj10470.Copy.setValue(('Copy from LHS', 1))
   self.obj10470.Copy.config = 0
   self.obj10470.Specify=ATOM3Constraint()
   self.obj10470.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1047.GGset2Any['Name']= self.obj10470

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1047)
   self.obj1047.postAction( cobj0.RHS.CREATE )

   self.obj1048=operatingUnit(self)
   self.obj1048.preAction( cobj0.RHS.CREATE )
   self.obj1048.isGraphObjectVisual = True

   if(hasattr(self.obj1048, '_setHierarchicalLink')):
     self.obj1048._setHierarchicalLink(False)

   # name
   self.obj1048.name.setValue('')
   self.obj1048.name.setNone()

   self.obj1048.GGLabel.setValue(2)
   self.obj1048.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(260.0,160.0,self.obj1048)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1048.graphObject_ = new_obj
   self.obj10480= AttrCalc()
   self.obj10480.Copy=ATOM3Boolean()
   self.obj10480.Copy.setValue(('Copy from LHS', 1))
   self.obj10480.Copy.config = 0
   self.obj10480.Specify=ATOM3Constraint()
   self.obj10480.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1048.GGset2Any['name']= self.obj10480

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1048)
   self.obj1048.postAction( cobj0.RHS.CREATE )

   self.obj1049=fromRaw(self)
   self.obj1049.preAction( cobj0.RHS.CREATE )
   self.obj1049.isGraphObjectVisual = True

   if(hasattr(self.obj1049, '_setHierarchicalLink')):
     self.obj1049._setHierarchicalLink(False)

   # rate
   self.obj1049.rate.setValue(1.0)

   self.obj1049.GGLabel.setValue(6)
   self.obj1049.graphClass_= graph_fromRaw
   if self.genGraphics:
      new_obj = graph_fromRaw(268.785046729,120.710526316,self.obj1049)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1049.graphObject_ = new_obj
   self.obj10490= AttrCalc()
   self.obj10490.Copy=ATOM3Boolean()
   self.obj10490.Copy.setValue(('Copy from LHS', 0))
   self.obj10490.Copy.config = 0
   self.obj10490.Specify=ATOM3Constraint()
   self.obj10490.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1049.GGset2Any['rate']= self.obj10490

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1049)
   self.obj1049.postAction( cobj0.RHS.CREATE )

   self.obj1050=GenericGraphEdge(self)
   self.obj1050.preAction( cobj0.RHS.CREATE )
   self.obj1050.isGraphObjectVisual = True

   if(hasattr(self.obj1050, '_setHierarchicalLink')):
     self.obj1050._setHierarchicalLink(False)

   self.obj1050.GGLabel.setValue(4)
   self.obj1050.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(174.5,97.5,self.obj1050)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1050.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1050)
   self.obj1050.postAction( cobj0.RHS.CREATE )

   self.obj1051=GenericGraphEdge(self)
   self.obj1051.preAction( cobj0.RHS.CREATE )
   self.obj1051.isGraphObjectVisual = True

   if(hasattr(self.obj1051, '_setHierarchicalLink')):
     self.obj1051._setHierarchicalLink(False)

   self.obj1051.GGLabel.setValue(5)
   self.obj1051.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(179.285046729,145.210526316,self.obj1051)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1051.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1051)
   self.obj1051.postAction( cobj0.RHS.CREATE )

   self.obj1046.out_connections_.append(self.obj1050)
   self.obj1050.in_connections_.append(self.obj1046)
   self.obj1046.graphObject_.pendingConnections.append((self.obj1046.graphObject_.tag, self.obj1050.graphObject_.tag, [85.0, 122.0, 174.5, 97.5], 0, True))
   self.obj1046.out_connections_.append(self.obj1051)
   self.obj1051.in_connections_.append(self.obj1046)
   self.obj1046.graphObject_.pendingConnections.append((self.obj1046.graphObject_.tag, self.obj1051.graphObject_.tag, [85.0, 122.0, 179.28504672897196, 145.21052631578948], 0, True))
   self.obj1047.out_connections_.append(self.obj1049)
   self.obj1049.in_connections_.append(self.obj1047)
   self.obj1047.graphObject_.pendingConnections.append((self.obj1047.graphObject_.tag, self.obj1049.graphObject_.tag, [264.0, 73.0, 268.78504672897196, 120.71052631578948], 0, True))
   self.obj1049.out_connections_.append(self.obj1048)
   self.obj1048.in_connections_.append(self.obj1049)
   self.obj1049.graphObject_.pendingConnections.append((self.obj1049.graphObject_.tag, self.obj1048.graphObject_.tag, [273.5700934579439, 168.42105263157896, 268.78504672897196, 120.71052631578948], 0, True))
   self.obj1050.out_connections_.append(self.obj1047)
   self.obj1047.in_connections_.append(self.obj1050)
   self.obj1050.graphObject_.pendingConnections.append((self.obj1050.graphObject_.tag, self.obj1047.graphObject_.tag, [264.0, 73.0, 174.5, 97.5], 0, True))
   self.obj1051.out_connections_.append(self.obj1048)
   self.obj1048.in_connections_.append(self.obj1051)
   self.obj1051.graphObject_.pendingConnections.append((self.obj1051.graphObject_.tag, self.obj1048.graphObject_.tag, [273.5700934579439, 168.42105263157896, 179.28504672897196, 145.21052631578948], 0, True))

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

   self.obj1058=product(self)
   self.obj1058.preAction( cobj0.RHS.CREATE )
   self.obj1058.isGraphObjectVisual = True

   if(hasattr(self.obj1058, '_setHierarchicalLink')):
     self.obj1058._setHierarchicalLink(False)

   # Name
   self.obj1058.Name.setValue('OAF')

   self.obj1058.GGLabel.setValue(1)
   self.obj1058.graphClass_= graph_product
   if self.genGraphics:
      new_obj = graph_product(180.0,40.0,self.obj1058)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1058.graphObject_ = new_obj
   self.obj10580= AttrCalc()
   self.obj10580.Copy=ATOM3Boolean()
   self.obj10580.Copy.setValue(('Copy from LHS', 0))
   self.obj10580.Copy.config = 0
   self.obj10580.Specify=ATOM3Constraint()
   self.obj10580.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1058.GGset2Any['Name']= self.obj10580

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1058)
   self.obj1058.postAction( cobj0.RHS.CREATE )


   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.graphRewritingSystem.finalStat == 0\n\n\n\n'))
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

   self.obj1065=Goal(self)
   self.obj1065.preAction( cobj0.LHS.CREATE )
   self.obj1065.isGraphObjectVisual = True

   if(hasattr(self.obj1065, '_setHierarchicalLink')):
     self.obj1065._setHierarchicalLink(False)

   # name
   self.obj1065.name.setValue('')
   self.obj1065.name.setNone()

   self.obj1065.GGLabel.setValue(2)
   self.obj1065.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(80.0,40.0,self.obj1065)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1065.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1065)
   self.obj1065.postAction( cobj0.LHS.CREATE )

   self.obj1066=metarial(self)
   self.obj1066.preAction( cobj0.LHS.CREATE )
   self.obj1066.isGraphObjectVisual = True

   if(hasattr(self.obj1066, '_setHierarchicalLink')):
     self.obj1066._setHierarchicalLink(False)

   # Name
   self.obj1066.Name.setValue('')
   self.obj1066.Name.setNone()

   self.obj1066.GGLabel.setValue(3)
   self.obj1066.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(220.0,40.0,self.obj1066)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1066.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1066)
   self.obj1066.postAction( cobj0.LHS.CREATE )

   self.obj1067=product(self)
   self.obj1067.preAction( cobj0.LHS.CREATE )
   self.obj1067.isGraphObjectVisual = True

   if(hasattr(self.obj1067, '_setHierarchicalLink')):
     self.obj1067._setHierarchicalLink(False)

   # Name
   self.obj1067.Name.setValue('')
   self.obj1067.Name.setNone()

   self.obj1067.GGLabel.setValue(5)
   self.obj1067.graphClass_= graph_product
   if self.genGraphics:
      new_obj = graph_product(160.0,180.0,self.obj1067)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1067.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1067)
   self.obj1067.postAction( cobj0.LHS.CREATE )

   self.obj1068=GenericGraphEdge(self)
   self.obj1068.preAction( cobj0.LHS.CREATE )
   self.obj1068.isGraphObjectVisual = True

   if(hasattr(self.obj1068, '_setHierarchicalLink')):
     self.obj1068._setHierarchicalLink(False)

   self.obj1068.GGLabel.setValue(4)
   self.obj1068.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(167.0,87.0,self.obj1068)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1068.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1068)
   self.obj1068.postAction( cobj0.LHS.CREATE )

   self.obj1065.out_connections_.append(self.obj1068)
   self.obj1068.in_connections_.append(self.obj1065)
   self.obj1065.graphObject_.pendingConnections.append((self.obj1065.graphObject_.tag, self.obj1068.graphObject_.tag, [104.0, 90.0, 167.0, 87.0], 0, True))
   self.obj1068.out_connections_.append(self.obj1066)
   self.obj1066.in_connections_.append(self.obj1068)
   self.obj1068.graphObject_.pendingConnections.append((self.obj1068.graphObject_.tag, self.obj1066.graphObject_.tag, [230.0, 84.0, 167.0, 87.0], 0, True))

   cobj0.RHS = ASG_omacss(self)
   cobj0.RHS.merge(ASG_pns2(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj1072=Goal(self)
   self.obj1072.preAction( cobj0.RHS.CREATE )
   self.obj1072.isGraphObjectVisual = True

   if(hasattr(self.obj1072, '_setHierarchicalLink')):
     self.obj1072._setHierarchicalLink(False)

   # name
   self.obj1072.name.setValue('')
   self.obj1072.name.setNone()

   self.obj1072.GGLabel.setValue(2)
   self.obj1072.graphClass_= graph_Goal
   if self.genGraphics:
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

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1072)
   self.obj1072.postAction( cobj0.RHS.CREATE )

   self.obj1073=intoProduct(self)
   self.obj1073.preAction( cobj0.RHS.CREATE )
   self.obj1073.isGraphObjectVisual = True

   if(hasattr(self.obj1073, '_setHierarchicalLink')):
     self.obj1073._setHierarchicalLink(False)

   # rate
   self.obj1073.rate.setValue(1.0)

   self.obj1073.GGLabel.setValue(6)
   self.obj1073.graphClass_= graph_intoProduct
   if self.genGraphics:
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

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1073)
   self.obj1073.postAction( cobj0.RHS.CREATE )

   self.obj1074=operatingUnit(self)
   self.obj1074.preAction( cobj0.RHS.CREATE )
   self.obj1074.isGraphObjectVisual = True

   if(hasattr(self.obj1074, '_setHierarchicalLink')):
     self.obj1074._setHierarchicalLink(False)

   # name
   self.obj1074.name.setValue('')
   self.obj1074.name.setNone()

   self.obj1074.GGLabel.setValue(1)
   self.obj1074.graphClass_= graph_operatingUnit
   if self.genGraphics:
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

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1074)
   self.obj1074.postAction( cobj0.RHS.CREATE )

   self.obj1075=metarial(self)
   self.obj1075.preAction( cobj0.RHS.CREATE )
   self.obj1075.isGraphObjectVisual = True

   if(hasattr(self.obj1075, '_setHierarchicalLink')):
     self.obj1075._setHierarchicalLink(False)

   # Name
   self.obj1075.Name.setValue('')
   self.obj1075.Name.setNone()

   self.obj1075.GGLabel.setValue(3)
   self.obj1075.graphClass_= graph_metarial
   if self.genGraphics:
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

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1075)
   self.obj1075.postAction( cobj0.RHS.CREATE )

   self.obj1076=product(self)
   self.obj1076.preAction( cobj0.RHS.CREATE )
   self.obj1076.isGraphObjectVisual = True

   if(hasattr(self.obj1076, '_setHierarchicalLink')):
     self.obj1076._setHierarchicalLink(False)

   # Name
   self.obj1076.Name.setValue('')
   self.obj1076.Name.setNone()

   self.obj1076.GGLabel.setValue(5)
   self.obj1076.graphClass_= graph_product
   if self.genGraphics:
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

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1076)
   self.obj1076.postAction( cobj0.RHS.CREATE )

   self.obj1077=fromMaterial(self)
   self.obj1077.preAction( cobj0.RHS.CREATE )
   self.obj1077.isGraphObjectVisual = True

   if(hasattr(self.obj1077, '_setHierarchicalLink')):
     self.obj1077._setHierarchicalLink(False)

   # rate
   self.obj1077.rate.setValue(1.0)

   self.obj1077.GGLabel.setValue(7)
   self.obj1077.graphClass_= graph_fromMaterial
   if self.genGraphics:
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

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1077)
   self.obj1077.postAction( cobj0.RHS.CREATE )

   self.obj1078=GenericGraphEdge(self)
   self.obj1078.preAction( cobj0.RHS.CREATE )
   self.obj1078.isGraphObjectVisual = True

   if(hasattr(self.obj1078, '_setHierarchicalLink')):
     self.obj1078._setHierarchicalLink(False)

   self.obj1078.GGLabel.setValue(4)
   self.obj1078.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(137.5,43.0,self.obj1078)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1078.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1078)
   self.obj1078.postAction( cobj0.RHS.CREATE )

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

   self.obj1083=Agent(self)
   self.obj1083.preAction( cobj0.LHS.CREATE )
   self.obj1083.isGraphObjectVisual = True

   if(hasattr(self.obj1083, '_setHierarchicalLink')):
     self.obj1083._setHierarchicalLink(False)

   # price
   self.obj1083.price.setValue(0)

   # name
   self.obj1083.name.setValue('')
   self.obj1083.name.setNone()

   self.obj1083.GGLabel.setValue(1)
   self.obj1083.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(80.0,20.0,self.obj1083)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1083.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1083)
   self.obj1083.postAction( cobj0.LHS.CREATE )

   self.obj1084=Role(self)
   self.obj1084.preAction( cobj0.LHS.CREATE )
   self.obj1084.isGraphObjectVisual = True

   if(hasattr(self.obj1084, '_setHierarchicalLink')):
     self.obj1084._setHierarchicalLink(False)

   # name
   self.obj1084.name.setValue('')
   self.obj1084.name.setNone()

   self.obj1084.GGLabel.setValue(2)
   self.obj1084.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(200.0,100.0,self.obj1084)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1084.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1084)
   self.obj1084.postAction( cobj0.LHS.CREATE )

   self.obj1085=Goal(self)
   self.obj1085.preAction( cobj0.LHS.CREATE )
   self.obj1085.isGraphObjectVisual = True

   if(hasattr(self.obj1085, '_setHierarchicalLink')):
     self.obj1085._setHierarchicalLink(False)

   # name
   self.obj1085.name.setValue('')
   self.obj1085.name.setNone()

   self.obj1085.GGLabel.setValue(3)
   self.obj1085.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(100.0,180.0,self.obj1085)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1085.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1085)
   self.obj1085.postAction( cobj0.LHS.CREATE )

   self.obj1086=CapableOf(self)
   self.obj1086.preAction( cobj0.LHS.CREATE )
   self.obj1086.isGraphObjectVisual = True

   if(hasattr(self.obj1086, '_setHierarchicalLink')):
     self.obj1086._setHierarchicalLink(False)

   self.obj1086.GGLabel.setValue(4)
   self.obj1086.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(164.5,91.5,self.obj1086)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1086.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1086)
   self.obj1086.postAction( cobj0.LHS.CREATE )

   self.obj1087=achieve(self)
   self.obj1087.preAction( cobj0.LHS.CREATE )
   self.obj1087.isGraphObjectVisual = True

   if(hasattr(self.obj1087, '_setHierarchicalLink')):
     self.obj1087._setHierarchicalLink(False)

   # rate
   self.obj1087.rate.setValue(0.0)

   self.obj1087.GGLabel.setValue(5)
   self.obj1087.graphClass_= graph_achieve
   if self.genGraphics:
      new_obj = graph_achieve(173.5,163.5,self.obj1087)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1087.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1087)
   self.obj1087.postAction( cobj0.LHS.CREATE )

   self.obj1083.out_connections_.append(self.obj1086)
   self.obj1086.in_connections_.append(self.obj1083)
   self.obj1083.graphObject_.pendingConnections.append((self.obj1083.graphObject_.tag, self.obj1086.graphObject_.tag, [105.0, 82.0, 164.5, 91.5], 0, True))
   self.obj1084.out_connections_.append(self.obj1087)
   self.obj1087.in_connections_.append(self.obj1084)
   self.obj1084.graphObject_.pendingConnections.append((self.obj1084.graphObject_.tag, self.obj1087.graphObject_.tag, [224.0, 146.0, 173.5, 163.5], 0, True))
   self.obj1086.out_connections_.append(self.obj1084)
   self.obj1084.in_connections_.append(self.obj1086)
   self.obj1086.graphObject_.pendingConnections.append((self.obj1086.graphObject_.tag, self.obj1084.graphObject_.tag, [224.0, 101.0, 164.5, 91.5], 0, True))
   self.obj1087.out_connections_.append(self.obj1085)
   self.obj1085.in_connections_.append(self.obj1087)
   self.obj1087.graphObject_.pendingConnections.append((self.obj1087.graphObject_.tag, self.obj1085.graphObject_.tag, [123.0, 181.0, 173.5, 163.5], 0, True))

   cobj0.RHS = ASG_omacss(self)
   cobj0.RHS.merge(ASG_pns2(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj1091=Agent(self)
   self.obj1091.preAction( cobj0.RHS.CREATE )
   self.obj1091.isGraphObjectVisual = True

   if(hasattr(self.obj1091, '_setHierarchicalLink')):
     self.obj1091._setHierarchicalLink(False)

   # price
   self.obj1091.price.setValue(0)

   # name
   self.obj1091.name.setValue('')
   self.obj1091.name.setNone()

   self.obj1091.GGLabel.setValue(1)
   self.obj1091.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(80.0,20.0,self.obj1091)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1091.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1091)
   self.obj1091.postAction( cobj0.RHS.CREATE )

   self.obj1092=Role(self)
   self.obj1092.preAction( cobj0.RHS.CREATE )
   self.obj1092.isGraphObjectVisual = True

   if(hasattr(self.obj1092, '_setHierarchicalLink')):
     self.obj1092._setHierarchicalLink(False)

   # name
   self.obj1092.name.setValue('')
   self.obj1092.name.setNone()

   self.obj1092.GGLabel.setValue(2)
   self.obj1092.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(200.0,100.0,self.obj1092)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1092.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1092)
   self.obj1092.postAction( cobj0.RHS.CREATE )

   self.obj1093=Goal(self)
   self.obj1093.preAction( cobj0.RHS.CREATE )
   self.obj1093.isGraphObjectVisual = True

   if(hasattr(self.obj1093, '_setHierarchicalLink')):
     self.obj1093._setHierarchicalLink(False)

   # name
   self.obj1093.name.setValue('')
   self.obj1093.name.setNone()

   self.obj1093.GGLabel.setValue(3)
   self.obj1093.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(100.0,180.0,self.obj1093)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1093.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1093)
   self.obj1093.postAction( cobj0.RHS.CREATE )

   self.obj1094=CapableOf(self)
   self.obj1094.preAction( cobj0.RHS.CREATE )
   self.obj1094.isGraphObjectVisual = True

   if(hasattr(self.obj1094, '_setHierarchicalLink')):
     self.obj1094._setHierarchicalLink(False)

   self.obj1094.GGLabel.setValue(4)
   self.obj1094.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(164.5,91.5,self.obj1094)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1094.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1094)
   self.obj1094.postAction( cobj0.RHS.CREATE )

   self.obj1095=achieve(self)
   self.obj1095.preAction( cobj0.RHS.CREATE )
   self.obj1095.isGraphObjectVisual = True

   if(hasattr(self.obj1095, '_setHierarchicalLink')):
     self.obj1095._setHierarchicalLink(False)

   # rate
   self.obj1095.rate.setValue(0.0)

   self.obj1095.GGLabel.setValue(5)
   self.obj1095.graphClass_= graph_achieve
   if self.genGraphics:
      new_obj = graph_achieve(173.5,163.5,self.obj1095)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1095.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1095)
   self.obj1095.postAction( cobj0.RHS.CREATE )

   self.obj1096=operatingUnit(self)
   self.obj1096.preAction( cobj0.RHS.CREATE )
   self.obj1096.isGraphObjectVisual = True

   if(hasattr(self.obj1096, '_setHierarchicalLink')):
     self.obj1096._setHierarchicalLink(False)

   # name
   self.obj1096.name.setValue('')
   self.obj1096.name.setNone()

   self.obj1096.GGLabel.setValue(7)
   self.obj1096.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(320.0,140.0,self.obj1096)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1096.graphObject_ = new_obj
   self.obj10960= AttrCalc()
   self.obj10960.Copy=ATOM3Boolean()
   self.obj10960.Copy.setValue(('Copy from LHS', 0))
   self.obj10960.Copy.config = 0
   self.obj10960.Specify=ATOM3Constraint()
   self.obj10960.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()+\' \'+ self.getMatched(graphID, self.LHS.nodeWithLabel(2)).name.getValue()+\' \'+ self.getMatched(graphID, self.LHS.nodeWithLabel(3)).name.getValue()\n'))
   self.obj1096.GGset2Any['name']= self.obj10960

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1096)
   self.obj1096.postAction( cobj0.RHS.CREATE )

   self.obj1097=metarial(self)
   self.obj1097.preAction( cobj0.RHS.CREATE )
   self.obj1097.isGraphObjectVisual = True

   if(hasattr(self.obj1097, '_setHierarchicalLink')):
     self.obj1097._setHierarchicalLink(False)

   # Name
   self.obj1097.Name.setValue('')
   self.obj1097.Name.setNone()

   self.obj1097.GGLabel.setValue(8)
   self.obj1097.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(320.0,40.0,self.obj1097)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1097.graphObject_ = new_obj
   self.obj10970= AttrCalc()
   self.obj10970.Copy=ATOM3Boolean()
   self.obj10970.Copy.setValue(('Copy from LHS', 0))
   self.obj10970.Copy.config = 0
   self.obj10970.Specify=ATOM3Constraint()
   self.obj10970.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()+\' \'+ self.getMatched(graphID, self.LHS.nodeWithLabel(2)).name.getValue()+\' \'+ self.getMatched(graphID, self.LHS.nodeWithLabel(3)).name.getValue()\n'))
   self.obj1097.GGset2Any['Name']= self.obj10970

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1097)
   self.obj1097.postAction( cobj0.RHS.CREATE )

   self.obj1098=fromMaterial(self)
   self.obj1098.preAction( cobj0.RHS.CREATE )
   self.obj1098.isGraphObjectVisual = True

   if(hasattr(self.obj1098, '_setHierarchicalLink')):
     self.obj1098._setHierarchicalLink(False)

   # rate
   self.obj1098.rate.setValue(1.0)

   self.obj1098.GGLabel.setValue(9)
   self.obj1098.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(338.785046729,119.210526316,self.obj1098)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1098.graphObject_ = new_obj
   self.obj10980= AttrCalc()
   self.obj10980.Copy=ATOM3Boolean()
   self.obj10980.Copy.setValue(('Copy from LHS', 0))
   self.obj10980.Copy.config = 0
   self.obj10980.Specify=ATOM3Constraint()
   self.obj10980.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1098.GGset2Any['rate']= self.obj10980

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1098)
   self.obj1098.postAction( cobj0.RHS.CREATE )

   self.obj1099=GenericGraphEdge(self)
   self.obj1099.preAction( cobj0.RHS.CREATE )
   self.obj1099.isGraphObjectVisual = True

   if(hasattr(self.obj1099, '_setHierarchicalLink')):
     self.obj1099._setHierarchicalLink(False)

   self.obj1099.GGLabel.setValue(10)
   self.obj1099.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(280.5,92.0,self.obj1099)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1099.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1099)
   self.obj1099.postAction( cobj0.RHS.CREATE )

   self.obj1091.out_connections_.append(self.obj1094)
   self.obj1094.in_connections_.append(self.obj1091)
   self.obj1091.graphObject_.pendingConnections.append((self.obj1091.graphObject_.tag, self.obj1094.graphObject_.tag, [117.0, 82.0, 164.5, 91.5], 2, 0))
   self.obj1092.out_connections_.append(self.obj1095)
   self.obj1095.in_connections_.append(self.obj1092)
   self.obj1092.graphObject_.pendingConnections.append((self.obj1092.graphObject_.tag, self.obj1095.graphObject_.tag, [231.0, 145.0, 173.5, 163.5], 2, 0))
   self.obj1092.out_connections_.append(self.obj1099)
   self.obj1099.in_connections_.append(self.obj1092)
   self.obj1092.graphObject_.pendingConnections.append((self.obj1092.graphObject_.tag, self.obj1099.graphObject_.tag, [231.0, 100.0, 280.5, 92.0], 0, True))
   self.obj1094.out_connections_.append(self.obj1092)
   self.obj1092.in_connections_.append(self.obj1094)
   self.obj1094.graphObject_.pendingConnections.append((self.obj1094.graphObject_.tag, self.obj1092.graphObject_.tag, [231.0, 100.0, 164.5, 91.5], 2, 0))
   self.obj1095.out_connections_.append(self.obj1093)
   self.obj1093.in_connections_.append(self.obj1095)
   self.obj1095.graphObject_.pendingConnections.append((self.obj1095.graphObject_.tag, self.obj1093.graphObject_.tag, [133.0, 181.0, 173.5, 163.5], 2, 0))
   self.obj1097.out_connections_.append(self.obj1098)
   self.obj1098.in_connections_.append(self.obj1097)
   self.obj1097.graphObject_.pendingConnections.append((self.obj1097.graphObject_.tag, self.obj1098.graphObject_.tag, [344.0, 90.0, 338.78504672897196, 119.21052631578948], 0, True))
   self.obj1098.out_connections_.append(self.obj1096)
   self.obj1096.in_connections_.append(self.obj1098)
   self.obj1098.graphObject_.pendingConnections.append((self.obj1098.graphObject_.tag, self.obj1096.graphObject_.tag, [333.5700934579439, 148.42105263157896, 338.78504672897196, 119.21052631578948], 0, True))
   self.obj1099.out_connections_.append(self.obj1097)
   self.obj1097.in_connections_.append(self.obj1099)
   self.obj1099.graphObject_.pendingConnections.append((self.obj1099.graphObject_.tag, self.obj1097.graphObject_.tag, [330.0, 84.0, 280.5, 92.0], 0, True))

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

   self.obj1106=Role(self)
   self.obj1106.preAction( cobj0.LHS.CREATE )
   self.obj1106.isGraphObjectVisual = True

   if(hasattr(self.obj1106, '_setHierarchicalLink')):
     self.obj1106._setHierarchicalLink(False)

   # name
   self.obj1106.name.setValue('')
   self.obj1106.name.setNone()

   self.obj1106.GGLabel.setValue(1)
   self.obj1106.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(80.0,20.0,self.obj1106)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1106.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1106)
   self.obj1106.postAction( cobj0.LHS.CREATE )

   self.obj1107=Goal(self)
   self.obj1107.preAction( cobj0.LHS.CREATE )
   self.obj1107.isGraphObjectVisual = True

   if(hasattr(self.obj1107, '_setHierarchicalLink')):
     self.obj1107._setHierarchicalLink(False)

   # name
   self.obj1107.name.setValue('')
   self.obj1107.name.setNone()

   self.obj1107.GGLabel.setValue(2)
   self.obj1107.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(100.0,180.0,self.obj1107)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1107.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1107)
   self.obj1107.postAction( cobj0.LHS.CREATE )

   self.obj1108=achieve(self)
   self.obj1108.preAction( cobj0.LHS.CREATE )
   self.obj1108.isGraphObjectVisual = True

   if(hasattr(self.obj1108, '_setHierarchicalLink')):
     self.obj1108._setHierarchicalLink(False)

   # rate
   self.obj1108.rate.setNone()

   self.obj1108.GGLabel.setValue(3)
   self.obj1108.graphClass_= graph_achieve
   if self.genGraphics:
      new_obj = graph_achieve(113.5,123.5,self.obj1108)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1108.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1108)
   self.obj1108.postAction( cobj0.LHS.CREATE )

   self.obj1109=operatingUnit(self)
   self.obj1109.preAction( cobj0.LHS.CREATE )
   self.obj1109.isGraphObjectVisual = True

   if(hasattr(self.obj1109, '_setHierarchicalLink')):
     self.obj1109._setHierarchicalLink(False)

   # name
   self.obj1109.name.setValue('')
   self.obj1109.name.setNone()

   self.obj1109.GGLabel.setValue(5)
   self.obj1109.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(280.0,100.0,self.obj1109)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1109.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1109)
   self.obj1109.postAction( cobj0.LHS.CREATE )

   self.obj1110=metarial(self)
   self.obj1110.preAction( cobj0.LHS.CREATE )
   self.obj1110.isGraphObjectVisual = True

   if(hasattr(self.obj1110, '_setHierarchicalLink')):
     self.obj1110._setHierarchicalLink(False)

   # Name
   self.obj1110.Name.setValue('')
   self.obj1110.Name.setNone()

   self.obj1110.GGLabel.setValue(4)
   self.obj1110.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(280.0,20.0,self.obj1110)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1110.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1110)
   self.obj1110.postAction( cobj0.LHS.CREATE )

   self.obj1111=metarial(self)
   self.obj1111.preAction( cobj0.LHS.CREATE )
   self.obj1111.isGraphObjectVisual = True

   if(hasattr(self.obj1111, '_setHierarchicalLink')):
     self.obj1111._setHierarchicalLink(False)

   # Name
   self.obj1111.Name.setValue('')
   self.obj1111.Name.setNone()

   self.obj1111.GGLabel.setValue(6)
   self.obj1111.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(320.0,220.0,self.obj1111)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1111.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1111)
   self.obj1111.postAction( cobj0.LHS.CREATE )

   self.obj1112=fromMaterial(self)
   self.obj1112.preAction( cobj0.LHS.CREATE )
   self.obj1112.isGraphObjectVisual = True

   if(hasattr(self.obj1112, '_setHierarchicalLink')):
     self.obj1112._setHierarchicalLink(False)

   # rate
   self.obj1112.rate.setNone()

   self.obj1112.GGLabel.setValue(8)
   self.obj1112.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(298.785046729,89.2105263158,self.obj1112)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1112.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1112)
   self.obj1112.postAction( cobj0.LHS.CREATE )

   self.obj1113=GenericGraphEdge(self)
   self.obj1113.preAction( cobj0.LHS.CREATE )
   self.obj1113.isGraphObjectVisual = True

   if(hasattr(self.obj1113, '_setHierarchicalLink')):
     self.obj1113._setHierarchicalLink(False)

   self.obj1113.GGLabel.setValue(7)
   self.obj1113.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(198.0,23.0,self.obj1113)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1113.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1113)
   self.obj1113.postAction( cobj0.LHS.CREATE )

   self.obj1114=GenericGraphEdge(self)
   self.obj1114.preAction( cobj0.LHS.CREATE )
   self.obj1114.isGraphObjectVisual = True

   if(hasattr(self.obj1114, '_setHierarchicalLink')):
     self.obj1114._setHierarchicalLink(False)

   self.obj1114.GGLabel.setValue(9)
   self.obj1114.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(228.0,227.5,self.obj1114)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1114.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1114)
   self.obj1114.postAction( cobj0.LHS.CREATE )

   self.obj1106.out_connections_.append(self.obj1108)
   self.obj1108.in_connections_.append(self.obj1106)
   self.obj1106.graphObject_.pendingConnections.append((self.obj1106.graphObject_.tag, self.obj1108.graphObject_.tag, [104.0, 66.0, 113.5, 123.5], 0, True))
   self.obj1106.out_connections_.append(self.obj1113)
   self.obj1113.in_connections_.append(self.obj1106)
   self.obj1106.graphObject_.pendingConnections.append((self.obj1106.graphObject_.tag, self.obj1113.graphObject_.tag, [104.0, 21.0, 198.0, 23.0], 0, True))
   self.obj1107.out_connections_.append(self.obj1114)
   self.obj1114.in_connections_.append(self.obj1107)
   self.obj1107.graphObject_.pendingConnections.append((self.obj1107.graphObject_.tag, self.obj1114.graphObject_.tag, [124.0, 230.0, 228.0, 227.5], 0, True))
   self.obj1108.out_connections_.append(self.obj1107)
   self.obj1107.in_connections_.append(self.obj1108)
   self.obj1108.graphObject_.pendingConnections.append((self.obj1108.graphObject_.tag, self.obj1107.graphObject_.tag, [123.0, 181.0, 113.5, 123.5], 0, True))
   self.obj1110.out_connections_.append(self.obj1112)
   self.obj1112.in_connections_.append(self.obj1110)
   self.obj1110.graphObject_.pendingConnections.append((self.obj1110.graphObject_.tag, self.obj1112.graphObject_.tag, [304.0, 70.0, 298.78504672897196, 89.21052631578948], 0, True))
   self.obj1112.out_connections_.append(self.obj1109)
   self.obj1109.in_connections_.append(self.obj1112)
   self.obj1112.graphObject_.pendingConnections.append((self.obj1112.graphObject_.tag, self.obj1109.graphObject_.tag, [293.5700934579439, 108.42105263157895, 298.78504672897196, 89.21052631578948], 0, True))
   self.obj1113.out_connections_.append(self.obj1110)
   self.obj1110.in_connections_.append(self.obj1113)
   self.obj1113.graphObject_.pendingConnections.append((self.obj1113.graphObject_.tag, self.obj1110.graphObject_.tag, [292.0, 25.0, 198.0, 23.0], 0, True))
   self.obj1114.out_connections_.append(self.obj1111)
   self.obj1111.in_connections_.append(self.obj1114)
   self.obj1114.graphObject_.pendingConnections.append((self.obj1114.graphObject_.tag, self.obj1111.graphObject_.tag, [332.0, 225.0, 228.0, 227.5], 0, True))

   cobj0.RHS = ASG_omacss(self)
   cobj0.RHS.merge(ASG_pns2(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj1118=Role(self)
   self.obj1118.preAction( cobj0.RHS.CREATE )
   self.obj1118.isGraphObjectVisual = True

   if(hasattr(self.obj1118, '_setHierarchicalLink')):
     self.obj1118._setHierarchicalLink(False)

   # name
   self.obj1118.name.setValue('')
   self.obj1118.name.setNone()

   self.obj1118.GGLabel.setValue(1)
   self.obj1118.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(100.0,40.0,self.obj1118)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1118.graphObject_ = new_obj
   self.obj11180= AttrCalc()
   self.obj11180.Copy=ATOM3Boolean()
   self.obj11180.Copy.setValue(('Copy from LHS', 1))
   self.obj11180.Copy.config = 0
   self.obj11180.Specify=ATOM3Constraint()
   self.obj11180.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1118.GGset2Any['name']= self.obj11180

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1118)
   self.obj1118.postAction( cobj0.RHS.CREATE )

   self.obj1119=Goal(self)
   self.obj1119.preAction( cobj0.RHS.CREATE )
   self.obj1119.isGraphObjectVisual = True

   if(hasattr(self.obj1119, '_setHierarchicalLink')):
     self.obj1119._setHierarchicalLink(False)

   # name
   self.obj1119.name.setValue('')
   self.obj1119.name.setNone()

   self.obj1119.GGLabel.setValue(2)
   self.obj1119.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(120.0,160.0,self.obj1119)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1119.graphObject_ = new_obj
   self.obj11190= AttrCalc()
   self.obj11190.Copy=ATOM3Boolean()
   self.obj11190.Copy.setValue(('Copy from LHS', 1))
   self.obj11190.Copy.config = 0
   self.obj11190.Specify=ATOM3Constraint()
   self.obj11190.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1119.GGset2Any['name']= self.obj11190

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1119)
   self.obj1119.postAction( cobj0.RHS.CREATE )

   self.obj1120=achieve(self)
   self.obj1120.preAction( cobj0.RHS.CREATE )
   self.obj1120.isGraphObjectVisual = True

   if(hasattr(self.obj1120, '_setHierarchicalLink')):
     self.obj1120._setHierarchicalLink(False)

   # rate
   self.obj1120.rate.setValue(0.0)

   self.obj1120.GGLabel.setValue(3)
   self.obj1120.graphClass_= graph_achieve
   if self.genGraphics:
      new_obj = graph_achieve(133.5,123.5,self.obj1120)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1120.graphObject_ = new_obj
   self.obj11200= AttrCalc()
   self.obj11200.Copy=ATOM3Boolean()
   self.obj11200.Copy.setValue(('Copy from LHS', 1))
   self.obj11200.Copy.config = 0
   self.obj11200.Specify=ATOM3Constraint()
   self.obj11200.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1120.GGset2Any['rate']= self.obj11200

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1120)
   self.obj1120.postAction( cobj0.RHS.CREATE )

   self.obj1121=operatingUnit(self)
   self.obj1121.preAction( cobj0.RHS.CREATE )
   self.obj1121.isGraphObjectVisual = True

   if(hasattr(self.obj1121, '_setHierarchicalLink')):
     self.obj1121._setHierarchicalLink(False)

   # name
   self.obj1121.name.setValue('')
   self.obj1121.name.setNone()

   self.obj1121.GGLabel.setValue(5)
   self.obj1121.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(280.0,120.0,self.obj1121)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1121.graphObject_ = new_obj
   self.obj11210= AttrCalc()
   self.obj11210.Copy=ATOM3Boolean()
   self.obj11210.Copy.setValue(('Copy from LHS', 1))
   self.obj11210.Copy.config = 0
   self.obj11210.Specify=ATOM3Constraint()
   self.obj11210.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1121.GGset2Any['name']= self.obj11210

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1121)
   self.obj1121.postAction( cobj0.RHS.CREATE )

   self.obj1122=metarial(self)
   self.obj1122.preAction( cobj0.RHS.CREATE )
   self.obj1122.isGraphObjectVisual = True

   if(hasattr(self.obj1122, '_setHierarchicalLink')):
     self.obj1122._setHierarchicalLink(False)

   # Name
   self.obj1122.Name.setValue('')
   self.obj1122.Name.setNone()

   self.obj1122.GGLabel.setValue(4)
   self.obj1122.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(280.0,40.0,self.obj1122)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1122.graphObject_ = new_obj
   self.obj11220= AttrCalc()
   self.obj11220.Copy=ATOM3Boolean()
   self.obj11220.Copy.setValue(('Copy from LHS', 1))
   self.obj11220.Copy.config = 0
   self.obj11220.Specify=ATOM3Constraint()
   self.obj11220.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1122.GGset2Any['Name']= self.obj11220

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1122)
   self.obj1122.postAction( cobj0.RHS.CREATE )

   self.obj1123=metarial(self)
   self.obj1123.preAction( cobj0.RHS.CREATE )
   self.obj1123.isGraphObjectVisual = True

   if(hasattr(self.obj1123, '_setHierarchicalLink')):
     self.obj1123._setHierarchicalLink(False)

   # Name
   self.obj1123.Name.setValue('')
   self.obj1123.Name.setNone()

   self.obj1123.GGLabel.setValue(6)
   self.obj1123.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(280.0,200.0,self.obj1123)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1123.graphObject_ = new_obj
   self.obj11230= AttrCalc()
   self.obj11230.Copy=ATOM3Boolean()
   self.obj11230.Copy.setValue(('Copy from LHS', 1))
   self.obj11230.Copy.config = 0
   self.obj11230.Specify=ATOM3Constraint()
   self.obj11230.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1123.GGset2Any['Name']= self.obj11230

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1123)
   self.obj1123.postAction( cobj0.RHS.CREATE )

   self.obj1124=fromMaterial(self)
   self.obj1124.preAction( cobj0.RHS.CREATE )
   self.obj1124.isGraphObjectVisual = True

   if(hasattr(self.obj1124, '_setHierarchicalLink')):
     self.obj1124._setHierarchicalLink(False)

   # rate
   self.obj1124.rate.setValue(0.0)

   self.obj1124.GGLabel.setValue(8)
   self.obj1124.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(298.785046729,109.210526316,self.obj1124)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1124.graphObject_ = new_obj
   self.obj11240= AttrCalc()
   self.obj11240.Copy=ATOM3Boolean()
   self.obj11240.Copy.setValue(('Copy from LHS', 1))
   self.obj11240.Copy.config = 0
   self.obj11240.Specify=ATOM3Constraint()
   self.obj11240.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1124.GGset2Any['rate']= self.obj11240

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1124)
   self.obj1124.postAction( cobj0.RHS.CREATE )

   self.obj1125=intoMaterial(self)
   self.obj1125.preAction( cobj0.RHS.CREATE )
   self.obj1125.isGraphObjectVisual = True

   if(hasattr(self.obj1125, '_setHierarchicalLink')):
     self.obj1125._setHierarchicalLink(False)

   # rate
   self.obj1125.rate.setValue(0.0)

   self.obj1125.GGLabel.setValue(10)
   self.obj1125.graphClass_= graph_intoMaterial
   if self.genGraphics:
      new_obj = graph_intoMaterial(301.093457944,168.263157895,self.obj1125)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1125.graphObject_ = new_obj
   self.obj11250= AttrCalc()
   self.obj11250.Copy=ATOM3Boolean()
   self.obj11250.Copy.setValue(('Copy from LHS', 0))
   self.obj11250.Copy.config = 0
   self.obj11250.Specify=ATOM3Constraint()
   self.obj11250.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(3)).rate.getValue()\n'))
   self.obj1125.GGset2Any['rate']= self.obj11250

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1125)
   self.obj1125.postAction( cobj0.RHS.CREATE )

   self.obj1126=GenericGraphEdge(self)
   self.obj1126.preAction( cobj0.RHS.CREATE )
   self.obj1126.isGraphObjectVisual = True

   if(hasattr(self.obj1126, '_setHierarchicalLink')):
     self.obj1126._setHierarchicalLink(False)

   self.obj1126.GGLabel.setValue(7)
   self.obj1126.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(208.0,43.0,self.obj1126)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1126.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1126)
   self.obj1126.postAction( cobj0.RHS.CREATE )

   self.obj1127=GenericGraphEdge(self)
   self.obj1127.preAction( cobj0.RHS.CREATE )
   self.obj1127.isGraphObjectVisual = True

   if(hasattr(self.obj1127, '_setHierarchicalLink')):
     self.obj1127._setHierarchicalLink(False)

   self.obj1127.GGLabel.setValue(9)
   self.obj1127.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(223.0,207.5,self.obj1127)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1127.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1127)
   self.obj1127.postAction( cobj0.RHS.CREATE )

   self.obj1118.out_connections_.append(self.obj1120)
   self.obj1120.in_connections_.append(self.obj1118)
   self.obj1118.graphObject_.pendingConnections.append((self.obj1118.graphObject_.tag, self.obj1120.graphObject_.tag, [124.0, 86.0, 133.5, 123.5], 0, True))
   self.obj1118.out_connections_.append(self.obj1126)
   self.obj1126.in_connections_.append(self.obj1118)
   self.obj1118.graphObject_.pendingConnections.append((self.obj1118.graphObject_.tag, self.obj1126.graphObject_.tag, [124.0, 41.0, 208.0, 43.0], 0, True))
   self.obj1119.out_connections_.append(self.obj1127)
   self.obj1127.in_connections_.append(self.obj1119)
   self.obj1119.graphObject_.pendingConnections.append((self.obj1119.graphObject_.tag, self.obj1127.graphObject_.tag, [154.0, 210.0, 223.0, 207.5], 0, True))
   self.obj1120.out_connections_.append(self.obj1119)
   self.obj1119.in_connections_.append(self.obj1120)
   self.obj1120.graphObject_.pendingConnections.append((self.obj1120.graphObject_.tag, self.obj1119.graphObject_.tag, [143.0, 161.0, 133.5, 123.5], 0, True))
   self.obj1121.out_connections_.append(self.obj1125)
   self.obj1125.in_connections_.append(self.obj1121)
   self.obj1121.graphObject_.pendingConnections.append((self.obj1121.graphObject_.tag, self.obj1125.graphObject_.tag, [295.1869158878505, 135.5263157894737, 301.0934579439253, 168.26315789473685], 0, True))
   self.obj1122.out_connections_.append(self.obj1124)
   self.obj1124.in_connections_.append(self.obj1122)
   self.obj1122.graphObject_.pendingConnections.append((self.obj1122.graphObject_.tag, self.obj1124.graphObject_.tag, [304.0, 90.0, 298.78504672897196, 109.21052631578948], 0, True))
   self.obj1124.out_connections_.append(self.obj1121)
   self.obj1121.in_connections_.append(self.obj1124)
   self.obj1124.graphObject_.pendingConnections.append((self.obj1124.graphObject_.tag, self.obj1121.graphObject_.tag, [293.5700934579439, 128.42105263157896, 298.78504672897196, 109.21052631578948], 0, True))
   self.obj1125.out_connections_.append(self.obj1123)
   self.obj1123.in_connections_.append(self.obj1125)
   self.obj1125.graphObject_.pendingConnections.append((self.obj1125.graphObject_.tag, self.obj1123.graphObject_.tag, [307.0, 201.0, 301.0934579439253, 168.26315789473685], 0, True))
   self.obj1126.out_connections_.append(self.obj1122)
   self.obj1122.in_connections_.append(self.obj1126)
   self.obj1126.graphObject_.pendingConnections.append((self.obj1126.graphObject_.tag, self.obj1122.graphObject_.tag, [292.0, 45.0, 208.0, 43.0], 0, True))
   self.obj1127.out_connections_.append(self.obj1123)
   self.obj1123.in_connections_.append(self.obj1127)
   self.obj1127.graphObject_.pendingConnections.append((self.obj1127.graphObject_.tag, self.obj1123.graphObject_.tag, [292.0, 205.0, 223.0, 207.5], 2, 0))

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

   self.obj1134=Agent(self)
   self.obj1134.preAction( cobj0.LHS.CREATE )
   self.obj1134.isGraphObjectVisual = True

   if(hasattr(self.obj1134, '_setHierarchicalLink')):
     self.obj1134._setHierarchicalLink(False)

   # price
   self.obj1134.price.setNone()

   # name
   self.obj1134.name.setValue('')
   self.obj1134.name.setNone()

   self.obj1134.GGLabel.setValue(1)
   self.obj1134.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(40.0,20.0,self.obj1134)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1134.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1134)
   self.obj1134.postAction( cobj0.LHS.CREATE )

   self.obj1135=Role(self)
   self.obj1135.preAction( cobj0.LHS.CREATE )
   self.obj1135.isGraphObjectVisual = True

   if(hasattr(self.obj1135, '_setHierarchicalLink')):
     self.obj1135._setHierarchicalLink(False)

   # name
   self.obj1135.name.setValue('')
   self.obj1135.name.setNone()

   self.obj1135.GGLabel.setValue(2)
   self.obj1135.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(60.0,140.0,self.obj1135)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1135.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1135)
   self.obj1135.postAction( cobj0.LHS.CREATE )

   self.obj1136=CapableOf(self)
   self.obj1136.preAction( cobj0.LHS.CREATE )
   self.obj1136.isGraphObjectVisual = True

   if(hasattr(self.obj1136, '_setHierarchicalLink')):
     self.obj1136._setHierarchicalLink(False)

   self.obj1136.GGLabel.setValue(3)
   self.obj1136.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(74.5,111.5,self.obj1136)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1136.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1136)
   self.obj1136.postAction( cobj0.LHS.CREATE )

   self.obj1137=rawMaterial(self)
   self.obj1137.preAction( cobj0.LHS.CREATE )
   self.obj1137.isGraphObjectVisual = True

   if(hasattr(self.obj1137, '_setHierarchicalLink')):
     self.obj1137._setHierarchicalLink(False)

   # Name
   self.obj1137.Name.setValue('')
   self.obj1137.Name.setNone()

   self.obj1137.GGLabel.setValue(6)
   self.obj1137.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(240.0,20.0,self.obj1137)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1137.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1137)
   self.obj1137.postAction( cobj0.LHS.CREATE )

   self.obj1138=operatingUnit(self)
   self.obj1138.preAction( cobj0.LHS.CREATE )
   self.obj1138.isGraphObjectVisual = True

   if(hasattr(self.obj1138, '_setHierarchicalLink')):
     self.obj1138._setHierarchicalLink(False)

   # name
   self.obj1138.name.setValue('')
   self.obj1138.name.setNone()

   self.obj1138.GGLabel.setValue(12)
   self.obj1138.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(320.0,240.0,self.obj1138)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1138.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1138)
   self.obj1138.postAction( cobj0.LHS.CREATE )

   self.obj1139=operatingUnit(self)
   self.obj1139.preAction( cobj0.LHS.CREATE )
   self.obj1139.isGraphObjectVisual = True

   if(hasattr(self.obj1139, '_setHierarchicalLink')):
     self.obj1139._setHierarchicalLink(False)

   # name
   self.obj1139.name.setValue('')
   self.obj1139.name.setNone()

   self.obj1139.GGLabel.setValue(7)
   self.obj1139.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(320.0,100.0,self.obj1139)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1139.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1139)
   self.obj1139.postAction( cobj0.LHS.CREATE )

   self.obj1140=metarial(self)
   self.obj1140.preAction( cobj0.LHS.CREATE )
   self.obj1140.isGraphObjectVisual = True

   if(hasattr(self.obj1140, '_setHierarchicalLink')):
     self.obj1140._setHierarchicalLink(False)

   # Name
   self.obj1140.Name.setValue('')
   self.obj1140.Name.setNone()

   self.obj1140.GGLabel.setValue(11)
   self.obj1140.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(240.0,160.0,self.obj1140)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1140.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1140)
   self.obj1140.postAction( cobj0.LHS.CREATE )

   self.obj1141=fromMaterial(self)
   self.obj1141.preAction( cobj0.LHS.CREATE )
   self.obj1141.isGraphObjectVisual = True

   if(hasattr(self.obj1141, '_setHierarchicalLink')):
     self.obj1141._setHierarchicalLink(False)

   # rate
   self.obj1141.rate.setNone()

   self.obj1141.GGLabel.setValue(14)
   self.obj1141.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(340.0,197.0,self.obj1141)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1141.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1141)
   self.obj1141.postAction( cobj0.LHS.CREATE )

   self.obj1142=fromRaw(self)
   self.obj1142.preAction( cobj0.LHS.CREATE )
   self.obj1142.isGraphObjectVisual = True

   if(hasattr(self.obj1142, '_setHierarchicalLink')):
     self.obj1142._setHierarchicalLink(False)

   # rate
   self.obj1142.rate.setNone()

   self.obj1142.GGLabel.setValue(9)
   self.obj1142.graphClass_= graph_fromRaw
   if self.genGraphics:
      new_obj = graph_fromRaw(329.081775701,37.1184210526,self.obj1142)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1142.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1142)
   self.obj1142.postAction( cobj0.LHS.CREATE )

   self.obj1143=GenericGraphEdge(self)
   self.obj1143.preAction( cobj0.LHS.CREATE )
   self.obj1143.isGraphObjectVisual = True

   if(hasattr(self.obj1143, '_setHierarchicalLink')):
     self.obj1143._setHierarchicalLink(False)

   self.obj1143.GGLabel.setValue(13)
   self.obj1143.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(167.0,195.0,self.obj1143)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1143.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1143)
   self.obj1143.postAction( cobj0.LHS.CREATE )

   self.obj1144=GenericGraphEdge(self)
   self.obj1144.preAction( cobj0.LHS.CREATE )
   self.obj1144.isGraphObjectVisual = True

   if(hasattr(self.obj1144, '_setHierarchicalLink')):
     self.obj1144._setHierarchicalLink(False)

   self.obj1144.GGLabel.setValue(10)
   self.obj1144.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(288.198598131,95.0,self.obj1144)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1144.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1144)
   self.obj1144.postAction( cobj0.LHS.CREATE )

   self.obj1145=GenericGraphEdge(self)
   self.obj1145.preAction( cobj0.LHS.CREATE )
   self.obj1145.isGraphObjectVisual = True

   if(hasattr(self.obj1145, '_setHierarchicalLink')):
     self.obj1145._setHierarchicalLink(False)

   self.obj1145.GGLabel.setValue(15)
   self.obj1145.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(170.5,76.0,self.obj1145)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1145.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1145)
   self.obj1145.postAction( cobj0.LHS.CREATE )

   self.obj1134.out_connections_.append(self.obj1136)
   self.obj1136.in_connections_.append(self.obj1134)
   self.obj1134.graphObject_.pendingConnections.append((self.obj1134.graphObject_.tag, self.obj1136.graphObject_.tag, [65.0, 82.0, 74.5, 111.5], 0, True))
   self.obj1134.out_connections_.append(self.obj1144)
   self.obj1144.in_connections_.append(self.obj1134)
   self.obj1134.graphObject_.pendingConnections.append((self.obj1134.graphObject_.tag, self.obj1144.graphObject_.tag, [77.0, 82.0, 216.5, 96.5, 288.1985981308411, 95.0], 2, True))
   self.obj1134.out_connections_.append(self.obj1145)
   self.obj1145.in_connections_.append(self.obj1134)
   self.obj1134.graphObject_.pendingConnections.append((self.obj1134.graphObject_.tag, self.obj1145.graphObject_.tag, [77.0, 82.0, 170.5, 76.0], 0, True))
   self.obj1135.out_connections_.append(self.obj1143)
   self.obj1143.in_connections_.append(self.obj1135)
   self.obj1135.graphObject_.pendingConnections.append((self.obj1135.graphObject_.tag, self.obj1143.graphObject_.tag, [84.0, 186.0, 167.0, 195.0], 0, True))
   self.obj1136.out_connections_.append(self.obj1135)
   self.obj1135.in_connections_.append(self.obj1136)
   self.obj1136.graphObject_.pendingConnections.append((self.obj1136.graphObject_.tag, self.obj1135.graphObject_.tag, [91.0, 140.0, 74.5, 111.5], 2, 0))
   self.obj1137.out_connections_.append(self.obj1142)
   self.obj1142.in_connections_.append(self.obj1137)
   self.obj1137.graphObject_.pendingConnections.append((self.obj1137.graphObject_.tag, self.obj1142.graphObject_.tag, [264.0, 73.0, 299.5, 33.5, 329.0817757009346, 37.118421052631575], 2, True))
   self.obj1140.out_connections_.append(self.obj1141)
   self.obj1141.in_connections_.append(self.obj1140)
   self.obj1140.graphObject_.pendingConnections.append((self.obj1140.graphObject_.tag, self.obj1141.graphObject_.tag, [281.0, 167.0, 372.0, 226.0, 328.0, 153.0], 2, True))
   self.obj1141.out_connections_.append(self.obj1138)
   self.obj1138.in_connections_.append(self.obj1141)
   self.obj1141.graphObject_.pendingConnections.append((self.obj1141.graphObject_.tag, self.obj1138.graphObject_.tag, [333.5700934579439, 248.42105263157896, 296.0, 124.0, 328.0, 153.0], 2, True))
   self.obj1142.out_connections_.append(self.obj1139)
   self.obj1139.in_connections_.append(self.obj1142)
   self.obj1142.graphObject_.pendingConnections.append((self.obj1142.graphObject_.tag, self.obj1139.graphObject_.tag, [362.32710280373834, 107.47368421052629, 358.6635514018692, 40.73684210526314, 329.0817757009346, 37.118421052631575], 2, True))
   self.obj1143.out_connections_.append(self.obj1140)
   self.obj1140.in_connections_.append(self.obj1143)
   self.obj1143.graphObject_.pendingConnections.append((self.obj1143.graphObject_.tag, self.obj1140.graphObject_.tag, [250.0, 204.0, 167.0, 195.0], 2, 0))
   self.obj1144.out_connections_.append(self.obj1139)
   self.obj1139.in_connections_.append(self.obj1144)
   self.obj1144.graphObject_.pendingConnections.append((self.obj1144.graphObject_.tag, self.obj1139.graphObject_.tag, [335.1869158878505, 115.5263157894737, 288.198598131, 95.0], 2, 0))
   self.obj1145.out_connections_.append(self.obj1137)
   self.obj1137.in_connections_.append(self.obj1145)
   self.obj1145.graphObject_.pendingConnections.append((self.obj1145.graphObject_.tag, self.obj1137.graphObject_.tag, [264.0, 70.0, 170.5, 76.0], 2, 0))

   cobj0.RHS = ASG_omacss(self)
   cobj0.RHS.merge(ASG_pns2(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj1149=Agent(self)
   self.obj1149.preAction( cobj0.RHS.CREATE )
   self.obj1149.isGraphObjectVisual = True

   if(hasattr(self.obj1149, '_setHierarchicalLink')):
     self.obj1149._setHierarchicalLink(False)

   # price
   self.obj1149.price.setValue(0)

   # name
   self.obj1149.name.setValue('')
   self.obj1149.name.setNone()

   self.obj1149.GGLabel.setValue(1)
   self.obj1149.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(60.0,20.0,self.obj1149)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1149.graphObject_ = new_obj
   self.obj11490= AttrCalc()
   self.obj11490.Copy=ATOM3Boolean()
   self.obj11490.Copy.setValue(('Copy from LHS', 1))
   self.obj11490.Copy.config = 0
   self.obj11490.Specify=ATOM3Constraint()
   self.obj11490.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1149.GGset2Any['price']= self.obj11490
   self.obj11491= AttrCalc()
   self.obj11491.Copy=ATOM3Boolean()
   self.obj11491.Copy.setValue(('Copy from LHS', 1))
   self.obj11491.Copy.config = 0
   self.obj11491.Specify=ATOM3Constraint()
   self.obj11491.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1149.GGset2Any['name']= self.obj11491

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1149)
   self.obj1149.postAction( cobj0.RHS.CREATE )

   self.obj1150=Role(self)
   self.obj1150.preAction( cobj0.RHS.CREATE )
   self.obj1150.isGraphObjectVisual = True

   if(hasattr(self.obj1150, '_setHierarchicalLink')):
     self.obj1150._setHierarchicalLink(False)

   # name
   self.obj1150.name.setValue('')
   self.obj1150.name.setNone()

   self.obj1150.GGLabel.setValue(2)
   self.obj1150.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(80.0,160.0,self.obj1150)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1150.graphObject_ = new_obj
   self.obj11500= AttrCalc()
   self.obj11500.Copy=ATOM3Boolean()
   self.obj11500.Copy.setValue(('Copy from LHS', 1))
   self.obj11500.Copy.config = 0
   self.obj11500.Specify=ATOM3Constraint()
   self.obj11500.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1150.GGset2Any['name']= self.obj11500

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1150)
   self.obj1150.postAction( cobj0.RHS.CREATE )

   self.obj1151=CapableOf(self)
   self.obj1151.preAction( cobj0.RHS.CREATE )
   self.obj1151.isGraphObjectVisual = True

   if(hasattr(self.obj1151, '_setHierarchicalLink')):
     self.obj1151._setHierarchicalLink(False)

   self.obj1151.GGLabel.setValue(3)
   self.obj1151.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(104.5,111.5,self.obj1151)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1151.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1151)
   self.obj1151.postAction( cobj0.RHS.CREATE )

   self.obj1152=rawMaterial(self)
   self.obj1152.preAction( cobj0.RHS.CREATE )
   self.obj1152.isGraphObjectVisual = True

   if(hasattr(self.obj1152, '_setHierarchicalLink')):
     self.obj1152._setHierarchicalLink(False)

   # Name
   self.obj1152.Name.setValue('')
   self.obj1152.Name.setNone()

   self.obj1152.GGLabel.setValue(6)
   self.obj1152.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(300.0,20.0,self.obj1152)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1152.graphObject_ = new_obj
   self.obj11520= AttrCalc()
   self.obj11520.Copy=ATOM3Boolean()
   self.obj11520.Copy.setValue(('Copy from LHS', 1))
   self.obj11520.Copy.config = 0
   self.obj11520.Specify=ATOM3Constraint()
   self.obj11520.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1152.GGset2Any['Name']= self.obj11520

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1152)
   self.obj1152.postAction( cobj0.RHS.CREATE )

   self.obj1153=operatingUnit(self)
   self.obj1153.preAction( cobj0.RHS.CREATE )
   self.obj1153.isGraphObjectVisual = True

   if(hasattr(self.obj1153, '_setHierarchicalLink')):
     self.obj1153._setHierarchicalLink(False)

   # name
   self.obj1153.name.setValue('')
   self.obj1153.name.setNone()

   self.obj1153.GGLabel.setValue(7)
   self.obj1153.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(300.0,100.0,self.obj1153)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1153.graphObject_ = new_obj
   self.obj11530= AttrCalc()
   self.obj11530.Copy=ATOM3Boolean()
   self.obj11530.Copy.setValue(('Copy from LHS', 1))
   self.obj11530.Copy.config = 0
   self.obj11530.Specify=ATOM3Constraint()
   self.obj11530.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1153.GGset2Any['name']= self.obj11530

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1153)
   self.obj1153.postAction( cobj0.RHS.CREATE )

   self.obj1154=operatingUnit(self)
   self.obj1154.preAction( cobj0.RHS.CREATE )
   self.obj1154.isGraphObjectVisual = True

   if(hasattr(self.obj1154, '_setHierarchicalLink')):
     self.obj1154._setHierarchicalLink(False)

   # name
   self.obj1154.name.setValue('')
   self.obj1154.name.setNone()

   self.obj1154.GGLabel.setValue(12)
   self.obj1154.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(240.0,260.0,self.obj1154)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1154.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1154)
   self.obj1154.postAction( cobj0.RHS.CREATE )

   self.obj1155=metarial(self)
   self.obj1155.preAction( cobj0.RHS.CREATE )
   self.obj1155.isGraphObjectVisual = True

   if(hasattr(self.obj1155, '_setHierarchicalLink')):
     self.obj1155._setHierarchicalLink(False)

   # Name
   self.obj1155.Name.setValue('')
   self.obj1155.Name.setNone()

   self.obj1155.GGLabel.setValue(11)
   self.obj1155.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(320.0,160.0,self.obj1155)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1155.graphObject_ = new_obj
   self.obj11550= AttrCalc()
   self.obj11550.Copy=ATOM3Boolean()
   self.obj11550.Copy.setValue(('Copy from LHS', 1))
   self.obj11550.Copy.config = 0
   self.obj11550.Specify=ATOM3Constraint()
   self.obj11550.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1155.GGset2Any['Name']= self.obj11550

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1155)
   self.obj1155.postAction( cobj0.RHS.CREATE )

   self.obj1156=fromMaterial(self)
   self.obj1156.preAction( cobj0.RHS.CREATE )
   self.obj1156.isGraphObjectVisual = True

   if(hasattr(self.obj1156, '_setHierarchicalLink')):
     self.obj1156._setHierarchicalLink(False)

   # rate
   self.obj1156.rate.setValue(0.0)

   self.obj1156.GGLabel.setValue(14)
   self.obj1156.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(317.285046729,218.710526316,self.obj1156)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1156.graphObject_ = new_obj
   self.obj11560= AttrCalc()
   self.obj11560.Copy=ATOM3Boolean()
   self.obj11560.Copy.setValue(('Copy from LHS', 1))
   self.obj11560.Copy.config = 0
   self.obj11560.Specify=ATOM3Constraint()
   self.obj11560.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1156.GGset2Any['rate']= self.obj11560

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1156)
   self.obj1156.postAction( cobj0.RHS.CREATE )

   self.obj1157=fromRaw(self)
   self.obj1157.preAction( cobj0.RHS.CREATE )
   self.obj1157.isGraphObjectVisual = True

   if(hasattr(self.obj1157, '_setHierarchicalLink')):
     self.obj1157._setHierarchicalLink(False)

   # rate
   self.obj1157.rate.setValue(0.0)

   self.obj1157.GGLabel.setValue(9)
   self.obj1157.graphClass_= graph_fromRaw
   if self.genGraphics:
      new_obj = graph_fromRaw(318.285046729,90.7105263158,self.obj1157)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1157.graphObject_ = new_obj
   self.obj11570= AttrCalc()
   self.obj11570.Copy=ATOM3Boolean()
   self.obj11570.Copy.setValue(('Copy from LHS', 1))
   self.obj11570.Copy.config = 0
   self.obj11570.Specify=ATOM3Constraint()
   self.obj11570.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1157.GGset2Any['rate']= self.obj11570

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1157)
   self.obj1157.postAction( cobj0.RHS.CREATE )

   self.obj1158=intoMaterial(self)
   self.obj1158.preAction( cobj0.RHS.CREATE )
   self.obj1158.isGraphObjectVisual = True

   if(hasattr(self.obj1158, '_setHierarchicalLink')):
     self.obj1158._setHierarchicalLink(False)

   # rate
   self.obj1158.rate.setValue(0.0)

   self.obj1158.GGLabel.setValue(16)
   self.obj1158.graphClass_= graph_intoMaterial
   if self.genGraphics:
      new_obj = graph_intoMaterial(322.093457944,135.263157895,self.obj1158)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1158.graphObject_ = new_obj
   self.obj11580= AttrCalc()
   self.obj11580.Copy=ATOM3Boolean()
   self.obj11580.Copy.setValue(('Copy from LHS', 0))
   self.obj11580.Copy.config = 0
   self.obj11580.Specify=ATOM3Constraint()
   self.obj11580.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1158.GGset2Any['rate']= self.obj11580

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1158)
   self.obj1158.postAction( cobj0.RHS.CREATE )

   self.obj1159=GenericGraphEdge(self)
   self.obj1159.preAction( cobj0.RHS.CREATE )
   self.obj1159.isGraphObjectVisual = True

   if(hasattr(self.obj1159, '_setHierarchicalLink')):
     self.obj1159._setHierarchicalLink(False)

   self.obj1159.GGLabel.setValue(10)
   self.obj1159.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(199.285046729,85.2105263158,self.obj1159)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1159.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1159)
   self.obj1159.postAction( cobj0.RHS.CREATE )

   self.obj1160=GenericGraphEdge(self)
   self.obj1160.preAction( cobj0.RHS.CREATE )
   self.obj1160.isGraphObjectVisual = True

   if(hasattr(self.obj1160, '_setHierarchicalLink')):
     self.obj1160._setHierarchicalLink(False)

   self.obj1160.GGLabel.setValue(13)
   self.obj1160.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(208.0,174.0,self.obj1160)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1160.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1160)
   self.obj1160.postAction( cobj0.RHS.CREATE )

   self.obj1161=GenericGraphEdge(self)
   self.obj1161.preAction( cobj0.RHS.CREATE )
   self.obj1161.isGraphObjectVisual = True

   if(hasattr(self.obj1161, '_setHierarchicalLink')):
     self.obj1161._setHierarchicalLink(False)

   self.obj1161.GGLabel.setValue(15)
   self.obj1161.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(229.5,47.0,self.obj1161)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1161.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1161)
   self.obj1161.postAction( cobj0.RHS.CREATE )

   self.obj1149.out_connections_.append(self.obj1151)
   self.obj1151.in_connections_.append(self.obj1149)
   self.obj1149.graphObject_.pendingConnections.append((self.obj1149.graphObject_.tag, self.obj1151.graphObject_.tag, [85.0, 82.0, 104.5, 111.5], 0, True))
   self.obj1149.out_connections_.append(self.obj1159)
   self.obj1159.in_connections_.append(self.obj1149)
   self.obj1149.graphObject_.pendingConnections.append((self.obj1149.graphObject_.tag, self.obj1159.graphObject_.tag, [85.0, 82.0, 199.28504672897196, 85.21052631578948], 0, True))
   self.obj1149.out_connections_.append(self.obj1161)
   self.obj1161.in_connections_.append(self.obj1149)
   self.obj1149.graphObject_.pendingConnections.append((self.obj1149.graphObject_.tag, self.obj1161.graphObject_.tag, [97.0, 82.0, 229.5, 47.0], 0, True))
   self.obj1150.out_connections_.append(self.obj1160)
   self.obj1160.in_connections_.append(self.obj1150)
   self.obj1150.graphObject_.pendingConnections.append((self.obj1150.graphObject_.tag, self.obj1160.graphObject_.tag, [104.0, 161.0, 208.0, 174.0], 0, True))
   self.obj1151.out_connections_.append(self.obj1150)
   self.obj1150.in_connections_.append(self.obj1151)
   self.obj1151.graphObject_.pendingConnections.append((self.obj1151.graphObject_.tag, self.obj1150.graphObject_.tag, [111.0, 160.0, 104.5, 111.5], 2, 0))
   self.obj1152.out_connections_.append(self.obj1157)
   self.obj1157.in_connections_.append(self.obj1152)
   self.obj1152.graphObject_.pendingConnections.append((self.obj1152.graphObject_.tag, self.obj1157.graphObject_.tag, [324.0, 73.0, 318.28504672897196, 90.71052631578948], 0, True))
   self.obj1153.out_connections_.append(self.obj1158)
   self.obj1158.in_connections_.append(self.obj1153)
   self.obj1153.graphObject_.pendingConnections.append((self.obj1153.graphObject_.tag, self.obj1158.graphObject_.tag, [315.1869158878505, 115.5263157894737, 322.0934579439253, 135.26315789473685], 0, True))
   self.obj1155.out_connections_.append(self.obj1156)
   self.obj1156.in_connections_.append(self.obj1155)
   self.obj1155.graphObject_.pendingConnections.append((self.obj1155.graphObject_.tag, self.obj1156.graphObject_.tag, [357.0, 205.0, 317.28504672897196, 218.71052631578948], 0, True))
   self.obj1156.out_connections_.append(self.obj1154)
   self.obj1154.in_connections_.append(self.obj1156)
   self.obj1156.graphObject_.pendingConnections.append((self.obj1156.graphObject_.tag, self.obj1154.graphObject_.tag, [253.57009345794393, 248.42105263157896, 315.28504672897196, 206.71052631578948], 0, True))
   self.obj1157.out_connections_.append(self.obj1153)
   self.obj1153.in_connections_.append(self.obj1157)
   self.obj1157.graphObject_.pendingConnections.append((self.obj1157.graphObject_.tag, self.obj1153.graphObject_.tag, [314.5700934579439, 108.42105263157895, 319.28504672897196, 90.71052631578948], 0, True))
   self.obj1158.out_connections_.append(self.obj1155)
   self.obj1155.in_connections_.append(self.obj1158)
   self.obj1158.graphObject_.pendingConnections.append((self.obj1158.graphObject_.tag, self.obj1155.graphObject_.tag, [347.0, 161.0, 311.0934579439253, 128.26315789473685], 0, True))
   self.obj1159.out_connections_.append(self.obj1153)
   self.obj1153.in_connections_.append(self.obj1159)
   self.obj1159.graphObject_.pendingConnections.append((self.obj1159.graphObject_.tag, self.obj1153.graphObject_.tag, [314.5700934579439, 108.42105263157895, 199.285046729, 85.2105263158], 2, 0))
   self.obj1160.out_connections_.append(self.obj1155)
   self.obj1155.in_connections_.append(self.obj1160)
   self.obj1160.graphObject_.pendingConnections.append((self.obj1160.graphObject_.tag, self.obj1155.graphObject_.tag, [332.0, 165.0, 208.0, 143.0], 2, 0))
   self.obj1161.out_connections_.append(self.obj1152)
   self.obj1152.in_connections_.append(self.obj1161)
   self.obj1161.graphObject_.pendingConnections.append((self.obj1161.graphObject_.tag, self.obj1152.graphObject_.tag, [324.0, 70.0, 210.5, 76.0], 0, True))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\nnode7 = self.getMatched(graphID, self.LHS.nodeWithLabel(7))\n\nnode11 = self.getMatched(graphID, self.LHS.nodeWithLabel(11))\nnode1 = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\n\nprint node7.name.getValue()+\' in \'+ node11.Name.getValue() \nprint node7.name.getValue() in  node11.Name.getValue()\nprint \'Rule 20 \'\n\ntest = not ( hasattr(node11, "linkAux2") and hasattr(node7, "linkAux2") )\nprint test\nif test : \n return (node7.name.getValue() in node11.Name.getValue() )\nelse : \n return False\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# code action of rule\nnode = self.getMatched ( graphID , self.LHS.nodeWithLabel(7) )\nnode.linkAux2 = True \nnode = self.getMatched ( graphID , self.LHS.nodeWithLabel(11) )\nnode.linkAux2 = True \nself.graphRewritingSystem.finalStat = 21\n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('RemoveGoals', 20)
   cobj0.Order=ATOM3Integer(21)
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

   self.obj1168=Goal(self)
   self.obj1168.preAction( cobj0.LHS.CREATE )
   self.obj1168.isGraphObjectVisual = True

   if(hasattr(self.obj1168, '_setHierarchicalLink')):
     self.obj1168._setHierarchicalLink(False)

   # name
   self.obj1168.name.setValue('')
   self.obj1168.name.setNone()

   self.obj1168.GGLabel.setValue(1)
   self.obj1168.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(200.0,60.0,self.obj1168)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1168.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1168)
   self.obj1168.postAction( cobj0.LHS.CREATE )

   self.obj1169=metarial(self)
   self.obj1169.preAction( cobj0.LHS.CREATE )
   self.obj1169.isGraphObjectVisual = True

   if(hasattr(self.obj1169, '_setHierarchicalLink')):
     self.obj1169._setHierarchicalLink(False)

   # Name
   self.obj1169.Name.setValue('')
   self.obj1169.Name.setNone()

   self.obj1169.GGLabel.setValue(2)
   self.obj1169.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(340.0,60.0,self.obj1169)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1169.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1169)
   self.obj1169.postAction( cobj0.LHS.CREATE )

   self.obj1170=GenericGraphEdge(self)
   self.obj1170.preAction( cobj0.LHS.CREATE )
   self.obj1170.isGraphObjectVisual = True

   if(hasattr(self.obj1170, '_setHierarchicalLink')):
     self.obj1170._setHierarchicalLink(False)

   self.obj1170.GGLabel.setValue(3)
   self.obj1170.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(292.0,107.0,self.obj1170)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1170.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1170)
   self.obj1170.postAction( cobj0.LHS.CREATE )

   self.obj1168.out_connections_.append(self.obj1170)
   self.obj1170.in_connections_.append(self.obj1168)
   self.obj1168.graphObject_.pendingConnections.append((self.obj1168.graphObject_.tag, self.obj1170.graphObject_.tag, [234.0, 110.0, 292.0, 107.0], 0, True))
   self.obj1170.out_connections_.append(self.obj1169)
   self.obj1169.in_connections_.append(self.obj1170)
   self.obj1170.graphObject_.pendingConnections.append((self.obj1170.graphObject_.tag, self.obj1169.graphObject_.tag, [350.0, 104.0, 292.0, 107.0], 0, True))

   cobj0.RHS = ASG_omacss(self)
   cobj0.RHS.merge(ASG_pns2(self))

   self.obj1173=metarial(self)
   self.obj1173.preAction( cobj0.RHS.CREATE )
   self.obj1173.isGraphObjectVisual = True

   if(hasattr(self.obj1173, '_setHierarchicalLink')):
     self.obj1173._setHierarchicalLink(False)

   # Name
   self.obj1173.Name.setValue('')
   self.obj1173.Name.setNone()

   self.obj1173.GGLabel.setValue(2)
   self.obj1173.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(280.0,60.0,self.obj1173)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1173.graphObject_ = new_obj
   self.obj11730= AttrCalc()
   self.obj11730.Copy=ATOM3Boolean()
   self.obj11730.Copy.setValue(('Copy from LHS', 1))
   self.obj11730.Copy.config = 0
   self.obj11730.Specify=ATOM3Constraint()
   self.obj11730.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1173.GGset2Any['Name']= self.obj11730

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1173)
   self.obj1173.postAction( cobj0.RHS.CREATE )


   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.graphRewritingSystem.finalStat > 20 \n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('RemoveAGent', 20)
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

   self.obj1180=Agent(self)
   self.obj1180.preAction( cobj0.LHS.CREATE )
   self.obj1180.isGraphObjectVisual = True

   if(hasattr(self.obj1180, '_setHierarchicalLink')):
     self.obj1180._setHierarchicalLink(False)

   # price
   self.obj1180.price.setNone()

   # name
   self.obj1180.name.setValue('')
   self.obj1180.name.setNone()

   self.obj1180.GGLabel.setValue(1)
   self.obj1180.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(100.0,60.0,self.obj1180)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1180.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1180)
   self.obj1180.postAction( cobj0.LHS.CREATE )

   self.obj1181=rawMaterial(self)
   self.obj1181.preAction( cobj0.LHS.CREATE )
   self.obj1181.isGraphObjectVisual = True

   if(hasattr(self.obj1181, '_setHierarchicalLink')):
     self.obj1181._setHierarchicalLink(False)

   # Name
   self.obj1181.Name.setValue('')
   self.obj1181.Name.setNone()

   self.obj1181.GGLabel.setValue(2)
   self.obj1181.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(280.0,20.0,self.obj1181)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1181.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1181)
   self.obj1181.postAction( cobj0.LHS.CREATE )

   self.obj1182=operatingUnit(self)
   self.obj1182.preAction( cobj0.LHS.CREATE )
   self.obj1182.isGraphObjectVisual = True

   if(hasattr(self.obj1182, '_setHierarchicalLink')):
     self.obj1182._setHierarchicalLink(False)

   # name
   self.obj1182.name.setValue('')
   self.obj1182.name.setNone()

   self.obj1182.GGLabel.setValue(3)
   self.obj1182.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(280.0,140.0,self.obj1182)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1182.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1182)
   self.obj1182.postAction( cobj0.LHS.CREATE )

   self.obj1183=fromRaw(self)
   self.obj1183.preAction( cobj0.LHS.CREATE )
   self.obj1183.isGraphObjectVisual = True

   if(hasattr(self.obj1183, '_setHierarchicalLink')):
     self.obj1183._setHierarchicalLink(False)

   # rate
   self.obj1183.rate.setNone()

   self.obj1183.GGLabel.setValue(6)
   self.obj1183.graphClass_= graph_fromRaw
   if self.genGraphics:
      new_obj = graph_fromRaw(298.785046729,110.710526316,self.obj1183)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1183.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1183)
   self.obj1183.postAction( cobj0.LHS.CREATE )

   self.obj1184=GenericGraphEdge(self)
   self.obj1184.preAction( cobj0.LHS.CREATE )
   self.obj1184.isGraphObjectVisual = True

   if(hasattr(self.obj1184, '_setHierarchicalLink')):
     self.obj1184._setHierarchicalLink(False)

   self.obj1184.GGLabel.setValue(4)
   self.obj1184.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(220.5,97.5,self.obj1184)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1184.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1184)
   self.obj1184.postAction( cobj0.LHS.CREATE )

   self.obj1185=GenericGraphEdge(self)
   self.obj1185.preAction( cobj0.LHS.CREATE )
   self.obj1185.isGraphObjectVisual = True

   if(hasattr(self.obj1185, '_setHierarchicalLink')):
     self.obj1185._setHierarchicalLink(False)

   self.obj1185.GGLabel.setValue(5)
   self.obj1185.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(215.285046729,135.210526316,self.obj1185)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj1185.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1185)
   self.obj1185.postAction( cobj0.LHS.CREATE )

   self.obj1180.out_connections_.append(self.obj1184)
   self.obj1184.in_connections_.append(self.obj1180)
   self.obj1180.graphObject_.pendingConnections.append((self.obj1180.graphObject_.tag, self.obj1184.graphObject_.tag, [137.0, 122.0, 220.5, 97.5], 0, True))
   self.obj1180.out_connections_.append(self.obj1185)
   self.obj1185.in_connections_.append(self.obj1180)
   self.obj1180.graphObject_.pendingConnections.append((self.obj1180.graphObject_.tag, self.obj1185.graphObject_.tag, [137.0, 122.0, 215.285046729, 135.210526316], 2, 0))
   self.obj1181.out_connections_.append(self.obj1183)
   self.obj1183.in_connections_.append(self.obj1181)
   self.obj1181.graphObject_.pendingConnections.append((self.obj1181.graphObject_.tag, self.obj1183.graphObject_.tag, [304.0, 73.0, 298.78504672897196, 110.71052631578948], 0, True))
   self.obj1183.out_connections_.append(self.obj1182)
   self.obj1182.in_connections_.append(self.obj1183)
   self.obj1183.graphObject_.pendingConnections.append((self.obj1183.graphObject_.tag, self.obj1182.graphObject_.tag, [293.5700934579439, 148.42105263157896, 298.78504672897196, 110.71052631578948], 0, True))
   self.obj1184.out_connections_.append(self.obj1181)
   self.obj1181.in_connections_.append(self.obj1184)
   self.obj1184.graphObject_.pendingConnections.append((self.obj1184.graphObject_.tag, self.obj1181.graphObject_.tag, [304.0, 73.0, 220.5, 97.5], 0, True))
   self.obj1185.out_connections_.append(self.obj1182)
   self.obj1182.in_connections_.append(self.obj1185)
   self.obj1185.graphObject_.pendingConnections.append((self.obj1185.graphObject_.tag, self.obj1182.graphObject_.tag, [294.5700934579439, 148.42105263157896, 215.285046729, 135.210526316], 2, 0))

   cobj0.RHS = ASG_omacss(self)
   cobj0.RHS.merge(ASG_pns2(self))

   self.obj1188=rawMaterial(self)
   self.obj1188.preAction( cobj0.RHS.CREATE )
   self.obj1188.isGraphObjectVisual = True

   if(hasattr(self.obj1188, '_setHierarchicalLink')):
     self.obj1188._setHierarchicalLink(False)

   # Name
   self.obj1188.Name.setValue('')
   self.obj1188.Name.setNone()

   self.obj1188.GGLabel.setValue(2)
   self.obj1188.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(200.0,20.0,self.obj1188)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1188.graphObject_ = new_obj
   self.obj11880= AttrCalc()
   self.obj11880.Copy=ATOM3Boolean()
   self.obj11880.Copy.setValue(('Copy from LHS', 1))
   self.obj11880.Copy.config = 0
   self.obj11880.Specify=ATOM3Constraint()
   self.obj11880.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1188.GGset2Any['Name']= self.obj11880

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1188)
   self.obj1188.postAction( cobj0.RHS.CREATE )

   self.obj1189=operatingUnit(self)
   self.obj1189.preAction( cobj0.RHS.CREATE )
   self.obj1189.isGraphObjectVisual = True

   if(hasattr(self.obj1189, '_setHierarchicalLink')):
     self.obj1189._setHierarchicalLink(False)

   # name
   self.obj1189.name.setValue('')
   self.obj1189.name.setNone()

   self.obj1189.GGLabel.setValue(3)
   self.obj1189.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(200.0,160.0,self.obj1189)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1189.graphObject_ = new_obj
   self.obj11890= AttrCalc()
   self.obj11890.Copy=ATOM3Boolean()
   self.obj11890.Copy.setValue(('Copy from LHS', 1))
   self.obj11890.Copy.config = 0
   self.obj11890.Specify=ATOM3Constraint()
   self.obj11890.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1189.GGset2Any['name']= self.obj11890

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1189)
   self.obj1189.postAction( cobj0.RHS.CREATE )

   self.obj1190=fromRaw(self)
   self.obj1190.preAction( cobj0.RHS.CREATE )
   self.obj1190.isGraphObjectVisual = True

   if(hasattr(self.obj1190, '_setHierarchicalLink')):
     self.obj1190._setHierarchicalLink(False)

   # rate
   self.obj1190.rate.setValue(0.0)

   self.obj1190.GGLabel.setValue(6)
   self.obj1190.graphClass_= graph_fromRaw
   if self.genGraphics:
      new_obj = graph_fromRaw(228.785046729,120.710526316,self.obj1190)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1190.graphObject_ = new_obj
   self.obj11900= AttrCalc()
   self.obj11900.Copy=ATOM3Boolean()
   self.obj11900.Copy.setValue(('Copy from LHS', 1))
   self.obj11900.Copy.config = 0
   self.obj11900.Specify=ATOM3Constraint()
   self.obj11900.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1190.GGset2Any['rate']= self.obj11900

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1190)
   self.obj1190.postAction( cobj0.RHS.CREATE )

   self.obj1188.out_connections_.append(self.obj1190)
   self.obj1190.in_connections_.append(self.obj1188)
   self.obj1188.graphObject_.pendingConnections.append((self.obj1188.graphObject_.tag, self.obj1190.graphObject_.tag, [224.0, 73.0, 228.78504672897196, 120.71052631578948], 0, True))
   self.obj1190.out_connections_.append(self.obj1189)
   self.obj1189.in_connections_.append(self.obj1190)
   self.obj1190.graphObject_.pendingConnections.append((self.obj1190.graphObject_.tag, self.obj1189.graphObject_.tag, [213.57009345794393, 168.42105263157896, 228.78504672897196, 120.71052631578948], 0, True))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.graphRewritingSystem.finalStat > 20 \n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('RemoveCap', 20)
   cobj0.Order=ATOM3Integer(23)
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

   self.obj1195=Capabilitie(self)
   self.obj1195.preAction( cobj0.LHS.CREATE )
   self.obj1195.isGraphObjectVisual = True

   if(hasattr(self.obj1195, '_setHierarchicalLink')):
     self.obj1195._setHierarchicalLink(False)

   # name
   self.obj1195.name.setValue('')
   self.obj1195.name.setNone()

   self.obj1195.GGLabel.setValue(1)
   self.obj1195.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(200.0,100.0,self.obj1195)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1195.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1195)
   self.obj1195.postAction( cobj0.LHS.CREATE )


   cobj0.RHS = ASG_omacss(self)


   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.graphRewritingSystem.finalStat > 20 \n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('RemoveRolez', 20)
   cobj0.Order=ATOM3Integer(24)
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

   self.obj1203=Role(self)
   self.obj1203.preAction( cobj0.LHS.CREATE )
   self.obj1203.isGraphObjectVisual = True

   if(hasattr(self.obj1203, '_setHierarchicalLink')):
     self.obj1203._setHierarchicalLink(False)

   # name
   self.obj1203.name.setValue('')
   self.obj1203.name.setNone()

   self.obj1203.GGLabel.setValue(1)
   self.obj1203.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(60.0,60.0,self.obj1203)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1203.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1203)
   self.obj1203.postAction( cobj0.LHS.CREATE )

   self.obj1204=operatingUnit(self)
   self.obj1204.preAction( cobj0.LHS.CREATE )
   self.obj1204.isGraphObjectVisual = True

   if(hasattr(self.obj1204, '_setHierarchicalLink')):
     self.obj1204._setHierarchicalLink(False)

   # name
   self.obj1204.name.setValue('')
   self.obj1204.name.setNone()

   self.obj1204.GGLabel.setValue(2)
   self.obj1204.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(260.0,160.0,self.obj1204)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1204.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1204)
   self.obj1204.postAction( cobj0.LHS.CREATE )

   self.obj1205=metarial(self)
   self.obj1205.preAction( cobj0.LHS.CREATE )
   self.obj1205.isGraphObjectVisual = True

   if(hasattr(self.obj1205, '_setHierarchicalLink')):
     self.obj1205._setHierarchicalLink(False)

   # Name
   self.obj1205.Name.setValue('')
   self.obj1205.Name.setNone()

   self.obj1205.GGLabel.setValue(5)
   self.obj1205.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(260.0,60.0,self.obj1205)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1205.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1205)
   self.obj1205.postAction( cobj0.LHS.CREATE )

   self.obj1206=fromMaterial(self)
   self.obj1206.preAction( cobj0.LHS.CREATE )
   self.obj1206.isGraphObjectVisual = True

   if(hasattr(self.obj1206, '_setHierarchicalLink')):
     self.obj1206._setHierarchicalLink(False)

   # rate
   self.obj1206.rate.setNone()

   self.obj1206.GGLabel.setValue(3)
   self.obj1206.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(288.785046729,139.210526316,self.obj1206)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1206.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj1206)
   self.obj1206.postAction( cobj0.LHS.CREATE )

   self.obj1205.out_connections_.append(self.obj1206)
   self.obj1206.in_connections_.append(self.obj1205)
   self.obj1205.graphObject_.pendingConnections.append((self.obj1205.graphObject_.tag, self.obj1206.graphObject_.tag, [284.0, 110.0, 288.78504672897196, 139.21052631578948], 0, True))
   self.obj1206.out_connections_.append(self.obj1204)
   self.obj1204.in_connections_.append(self.obj1206)
   self.obj1206.graphObject_.pendingConnections.append((self.obj1206.graphObject_.tag, self.obj1204.graphObject_.tag, [273.5700934579439, 168.42105263157896, 288.78504672897196, 139.21052631578948], 0, True))

   cobj0.RHS = ASG_omacss(self)
   cobj0.RHS.merge(ASG_pns2(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj1210=operatingUnit(self)
   self.obj1210.preAction( cobj0.RHS.CREATE )
   self.obj1210.isGraphObjectVisual = True

   if(hasattr(self.obj1210, '_setHierarchicalLink')):
     self.obj1210._setHierarchicalLink(False)

   # name
   self.obj1210.name.setValue('')
   self.obj1210.name.setNone()

   self.obj1210.GGLabel.setValue(2)
   self.obj1210.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(240.0,160.0,self.obj1210)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1210.graphObject_ = new_obj
   self.obj12100= AttrCalc()
   self.obj12100.Copy=ATOM3Boolean()
   self.obj12100.Copy.setValue(('Copy from LHS', 1))
   self.obj12100.Copy.config = 0
   self.obj12100.Specify=ATOM3Constraint()
   self.obj12100.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1210.GGset2Any['name']= self.obj12100

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1210)
   self.obj1210.postAction( cobj0.RHS.CREATE )

   self.obj1211=metarial(self)
   self.obj1211.preAction( cobj0.RHS.CREATE )
   self.obj1211.isGraphObjectVisual = True

   if(hasattr(self.obj1211, '_setHierarchicalLink')):
     self.obj1211._setHierarchicalLink(False)

   # Name
   self.obj1211.Name.setValue('')
   self.obj1211.Name.setNone()

   self.obj1211.GGLabel.setValue(5)
   self.obj1211.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(240.0,40.0,self.obj1211)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1211.graphObject_ = new_obj
   self.obj12110= AttrCalc()
   self.obj12110.Copy=ATOM3Boolean()
   self.obj12110.Copy.setValue(('Copy from LHS', 1))
   self.obj12110.Copy.config = 0
   self.obj12110.Specify=ATOM3Constraint()
   self.obj12110.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1211.GGset2Any['Name']= self.obj12110

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1211)
   self.obj1211.postAction( cobj0.RHS.CREATE )

   self.obj1212=fromMaterial(self)
   self.obj1212.preAction( cobj0.RHS.CREATE )
   self.obj1212.isGraphObjectVisual = True

   if(hasattr(self.obj1212, '_setHierarchicalLink')):
     self.obj1212._setHierarchicalLink(False)

   # rate
   self.obj1212.rate.setValue(0.0)

   self.obj1212.GGLabel.setValue(3)
   self.obj1212.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(258.785046729,129.210526316,self.obj1212)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj1212.graphObject_ = new_obj
   self.obj12120= AttrCalc()
   self.obj12120.Copy=ATOM3Boolean()
   self.obj12120.Copy.setValue(('Copy from LHS', 1))
   self.obj12120.Copy.config = 0
   self.obj12120.Specify=ATOM3Constraint()
   self.obj12120.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj1212.GGset2Any['rate']= self.obj12120

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj1212)
   self.obj1212.postAction( cobj0.RHS.CREATE )

   self.obj1211.out_connections_.append(self.obj1212)
   self.obj1212.in_connections_.append(self.obj1211)
   self.obj1211.graphObject_.pendingConnections.append((self.obj1211.graphObject_.tag, self.obj1212.graphObject_.tag, [264.0, 90.0, 258.78504672897196, 129.21052631578948], 0, True))
   self.obj1212.out_connections_.append(self.obj1210)
   self.obj1210.in_connections_.append(self.obj1212)
   self.obj1212.graphObject_.pendingConnections.append((self.obj1212.graphObject_.tag, self.obj1210.graphObject_.tag, [253.57009345794393, 168.42105263157896, 258.78504672897196, 129.21052631578948], 0, True))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.graphRewritingSystem.finalStat > 20 \n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   lcobj0.append(cobj0)
   self.EditingGraphGrammar.Rules.setValue(lcobj0)
   self.EditingGraphGrammar.InitialAction=ATOM3Constraint()
   self.EditingGraphGrammar.InitialAction.setValue(('constraint', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'self.rewritingSystem.finalStat = 0\n\n'))
   self.EditingGraphGrammar.FinalAction=ATOM3Constraint()
   self.EditingGraphGrammar.FinalAction.setValue(('const', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))


