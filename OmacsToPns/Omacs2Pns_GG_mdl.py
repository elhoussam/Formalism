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

   self.obj75=Agent(self)
   self.obj75.preAction( cobj0.LHS.CREATE )
   self.obj75.isGraphObjectVisual = True

   if(hasattr(self.obj75, '_setHierarchicalLink')):
     self.obj75._setHierarchicalLink(False)

   # price
   self.obj75.price.setNone()

   # name
   self.obj75.name.setValue('')
   self.obj75.name.setNone()

   self.obj75.GGLabel.setValue(1)
   self.obj75.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(80.0,20.0,self.obj75)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj75.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj75)
   self.obj75.postAction( cobj0.LHS.CREATE )

   self.obj76=Capabilitie(self)
   self.obj76.preAction( cobj0.LHS.CREATE )
   self.obj76.isGraphObjectVisual = True

   if(hasattr(self.obj76, '_setHierarchicalLink')):
     self.obj76._setHierarchicalLink(False)

   # name
   self.obj76.name.setValue('')
   self.obj76.name.setNone()

   self.obj76.GGLabel.setValue(2)
   self.obj76.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(160.0,180.0,self.obj76)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj76.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj76)
   self.obj76.postAction( cobj0.LHS.CREATE )

   self.obj77=Role(self)
   self.obj77.preAction( cobj0.LHS.CREATE )
   self.obj77.isGraphObjectVisual = True

   if(hasattr(self.obj77, '_setHierarchicalLink')):
     self.obj77._setHierarchicalLink(False)

   # name
   self.obj77.name.setValue('')
   self.obj77.name.setNone()

   self.obj77.GGLabel.setValue(3)
   self.obj77.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(280.0,40.0,self.obj77)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj77.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj77)
   self.obj77.postAction( cobj0.LHS.CREATE )

   self.obj78=posses(self)
   self.obj78.preAction( cobj0.LHS.CREATE )
   self.obj78.isGraphObjectVisual = True

   if(hasattr(self.obj78, '_setHierarchicalLink')):
     self.obj78._setHierarchicalLink(False)

   # rate
   self.obj78.rate.setNone()

   self.obj78.GGLabel.setValue(4)
   self.obj78.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(143.0,130.5,self.obj78)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj78.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj78)
   self.obj78.postAction( cobj0.LHS.CREATE )

   self.obj79=require(self)
   self.obj79.preAction( cobj0.LHS.CREATE )
   self.obj79.isGraphObjectVisual = True

   if(hasattr(self.obj79, '_setHierarchicalLink')):
     self.obj79._setHierarchicalLink(False)

   self.obj79.GGLabel.setValue(5)
   self.obj79.graphClass_= graph_require
   if self.genGraphics:
      new_obj = graph_require(242.5,132.5,self.obj79)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj79.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj79)
   self.obj79.postAction( cobj0.LHS.CREATE )

   self.obj75.out_connections_.append(self.obj78)
   self.obj78.in_connections_.append(self.obj75)
   self.obj75.graphObject_.pendingConnections.append((self.obj75.graphObject_.tag, self.obj78.graphObject_.tag, [105.0, 82.0, 143.0, 130.5], 0, True))
   self.obj77.out_connections_.append(self.obj79)
   self.obj79.in_connections_.append(self.obj77)
   self.obj77.graphObject_.pendingConnections.append((self.obj77.graphObject_.tag, self.obj79.graphObject_.tag, [304.0, 86.0, 242.5, 132.5], 0, True))
   self.obj78.out_connections_.append(self.obj76)
   self.obj76.in_connections_.append(self.obj78)
   self.obj78.graphObject_.pendingConnections.append((self.obj78.graphObject_.tag, self.obj76.graphObject_.tag, [181.0, 179.0, 143.0, 130.5], 0, True))
   self.obj79.out_connections_.append(self.obj76)
   self.obj76.in_connections_.append(self.obj79)
   self.obj79.graphObject_.pendingConnections.append((self.obj79.graphObject_.tag, self.obj76.graphObject_.tag, [181.0, 179.0, 242.5, 132.5], 0, True))

   cobj0.RHS = ASG_omacs(self)

   self.obj81=Agent(self)
   self.obj81.preAction( cobj0.RHS.CREATE )
   self.obj81.isGraphObjectVisual = True

   if(hasattr(self.obj81, '_setHierarchicalLink')):
     self.obj81._setHierarchicalLink(False)

   # price
   self.obj81.price.setNone()

   # name
   self.obj81.name.setValue('')
   self.obj81.name.setNone()

   self.obj81.GGLabel.setValue(1)
   self.obj81.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(80.0,20.0,self.obj81)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj81.graphObject_ = new_obj
   self.obj810= AttrCalc()
   self.obj810.Copy=ATOM3Boolean()
   self.obj810.Copy.setValue(('Copy from LHS', 1))
   self.obj810.Copy.config = 0
   self.obj810.Specify=ATOM3Constraint()
   self.obj810.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj81.GGset2Any['price']= self.obj810
   self.obj811= AttrCalc()
   self.obj811.Copy=ATOM3Boolean()
   self.obj811.Copy.setValue(('Copy from LHS', 1))
   self.obj811.Copy.config = 0
   self.obj811.Specify=ATOM3Constraint()
   self.obj811.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj81.GGset2Any['name']= self.obj811

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj81)
   self.obj81.postAction( cobj0.RHS.CREATE )

   self.obj82=Capabilitie(self)
   self.obj82.preAction( cobj0.RHS.CREATE )
   self.obj82.isGraphObjectVisual = True

   if(hasattr(self.obj82, '_setHierarchicalLink')):
     self.obj82._setHierarchicalLink(False)

   # name
   self.obj82.name.setValue('')
   self.obj82.name.setNone()

   self.obj82.GGLabel.setValue(2)
   self.obj82.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(160.0,180.0,self.obj82)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj82.graphObject_ = new_obj
   self.obj820= AttrCalc()
   self.obj820.Copy=ATOM3Boolean()
   self.obj820.Copy.setValue(('Copy from LHS', 1))
   self.obj820.Copy.config = 0
   self.obj820.Specify=ATOM3Constraint()
   self.obj820.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj82.GGset2Any['name']= self.obj820

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj82)
   self.obj82.postAction( cobj0.RHS.CREATE )

   self.obj83=Role(self)
   self.obj83.preAction( cobj0.RHS.CREATE )
   self.obj83.isGraphObjectVisual = True

   if(hasattr(self.obj83, '_setHierarchicalLink')):
     self.obj83._setHierarchicalLink(False)

   # name
   self.obj83.name.setValue('')
   self.obj83.name.setNone()

   self.obj83.GGLabel.setValue(3)
   self.obj83.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(280.0,40.0,self.obj83)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj83.graphObject_ = new_obj
   self.obj830= AttrCalc()
   self.obj830.Copy=ATOM3Boolean()
   self.obj830.Copy.setValue(('Copy from LHS', 1))
   self.obj830.Copy.config = 0
   self.obj830.Specify=ATOM3Constraint()
   self.obj830.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj83.GGset2Any['name']= self.obj830

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj83)
   self.obj83.postAction( cobj0.RHS.CREATE )

   self.obj84=posses(self)
   self.obj84.preAction( cobj0.RHS.CREATE )
   self.obj84.isGraphObjectVisual = True

   if(hasattr(self.obj84, '_setHierarchicalLink')):
     self.obj84._setHierarchicalLink(False)

   # rate
   self.obj84.rate.setNone()

   self.obj84.GGLabel.setValue(4)
   self.obj84.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(143.0,130.5,self.obj84)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj84.graphObject_ = new_obj
   self.obj840= AttrCalc()
   self.obj840.Copy=ATOM3Boolean()
   self.obj840.Copy.setValue(('Copy from LHS', 1))
   self.obj840.Copy.config = 0
   self.obj840.Specify=ATOM3Constraint()
   self.obj840.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj84.GGset2Any['rate']= self.obj840

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj84)
   self.obj84.postAction( cobj0.RHS.CREATE )

   self.obj85=CapableOf(self)
   self.obj85.preAction( cobj0.RHS.CREATE )
   self.obj85.isGraphObjectVisual = True

   if(hasattr(self.obj85, '_setHierarchicalLink')):
     self.obj85._setHierarchicalLink(False)

   # rate
   self.obj85.rate.setValue(0.0)

   self.obj85.GGLabel.setValue(7)
   self.obj85.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(214.0,83.5,self.obj85)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj85.graphObject_ = new_obj
   self.obj850= AttrCalc()
   self.obj850.Copy=ATOM3Boolean()
   self.obj850.Copy.setValue(('Copy from LHS', 1))
   self.obj850.Copy.config = 0
   self.obj850.Specify=ATOM3Constraint()
   self.obj850.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj85.GGset2Any['rate']= self.obj850

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj85)
   self.obj85.postAction( cobj0.RHS.CREATE )

   self.obj86=require(self)
   self.obj86.preAction( cobj0.RHS.CREATE )
   self.obj86.isGraphObjectVisual = True

   if(hasattr(self.obj86, '_setHierarchicalLink')):
     self.obj86._setHierarchicalLink(False)

   self.obj86.GGLabel.setValue(5)
   self.obj86.graphClass_= graph_require
   if self.genGraphics:
      new_obj = graph_require(242.5,132.5,self.obj86)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj86.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj86)
   self.obj86.postAction( cobj0.RHS.CREATE )

   self.obj81.out_connections_.append(self.obj84)
   self.obj84.in_connections_.append(self.obj81)
   self.obj81.graphObject_.pendingConnections.append((self.obj81.graphObject_.tag, self.obj84.graphObject_.tag, [117.0, 82.0, 143.0, 130.5], 2, 0))
   self.obj81.out_connections_.append(self.obj85)
   self.obj85.in_connections_.append(self.obj81)
   self.obj81.graphObject_.pendingConnections.append((self.obj81.graphObject_.tag, self.obj85.graphObject_.tag, [117.0, 82.0, 214.0, 83.5], 0, True))
   self.obj83.out_connections_.append(self.obj86)
   self.obj86.in_connections_.append(self.obj83)
   self.obj83.graphObject_.pendingConnections.append((self.obj83.graphObject_.tag, self.obj86.graphObject_.tag, [311.0, 85.0, 242.5, 132.5], 2, 0))
   self.obj84.out_connections_.append(self.obj82)
   self.obj82.in_connections_.append(self.obj84)
   self.obj84.graphObject_.pendingConnections.append((self.obj84.graphObject_.tag, self.obj82.graphObject_.tag, [191.0, 183.0, 143.0, 130.5], 2, 0))
   self.obj85.out_connections_.append(self.obj83)
   self.obj83.in_connections_.append(self.obj85)
   self.obj85.graphObject_.pendingConnections.append((self.obj85.graphObject_.tag, self.obj83.graphObject_.tag, [311.0, 85.0, 214.0, 83.5], 0, True))
   self.obj86.out_connections_.append(self.obj82)
   self.obj82.in_connections_.append(self.obj86)
   self.obj86.graphObject_.pendingConnections.append((self.obj86.graphObject_.tag, self.obj82.graphObject_.tag, [191.0, 183.0, 242.5, 132.5], 2, 0))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'agent = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\n\nrole = self.getMatched(graphID, self.LHS.nodeWithLabel(3))\nreturn not ( hasattr(agent, role.name.getValue()) and hasattr(role, agent.name.getValue() ) )\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'agent = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) )\n\nc1 = self.getMatched ( graphID , self.LHS.nodeWithLabel(2) )\nrole = self.getMatched ( graphID , self.LHS.nodeWithLabel(3) )\nsetattr(agent ,role.name.getValue(),True )\nsetattr(role ,agent.name.getValue(),True )\n\nsetattr( c1 ,  agent.name.getValue() , True )\nsetattr( c1 ,  role.name.getValue() , True )\n\nprint \'connCt (\'+agent.name.getValue()+\',\'+role.name.getValue()+\')\'\n'))
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

   self.obj91=Agent(self)
   self.obj91.preAction( cobj0.LHS.CREATE )
   self.obj91.isGraphObjectVisual = True

   if(hasattr(self.obj91, '_setHierarchicalLink')):
     self.obj91._setHierarchicalLink(False)

   # price
   self.obj91.price.setNone()

   # name
   self.obj91.name.setValue('')
   self.obj91.name.setNone()

   self.obj91.GGLabel.setValue(1)
   self.obj91.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(60.0,20.0,self.obj91)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj91.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj91)
   self.obj91.postAction( cobj0.LHS.CREATE )

   self.obj92=Capabilitie(self)
   self.obj92.preAction( cobj0.LHS.CREATE )
   self.obj92.isGraphObjectVisual = True

   if(hasattr(self.obj92, '_setHierarchicalLink')):
     self.obj92._setHierarchicalLink(False)

   # name
   self.obj92.name.setValue('')
   self.obj92.name.setNone()

   self.obj92.GGLabel.setValue(2)
   self.obj92.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(80.0,180.0,self.obj92)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj92.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj92)
   self.obj92.postAction( cobj0.LHS.CREATE )

   self.obj93=Capabilitie(self)
   self.obj93.preAction( cobj0.LHS.CREATE )
   self.obj93.isGraphObjectVisual = True

   if(hasattr(self.obj93, '_setHierarchicalLink')):
     self.obj93._setHierarchicalLink(False)

   # name
   self.obj93.name.setValue('')
   self.obj93.name.setNone()

   self.obj93.GGLabel.setValue(3)
   self.obj93.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(300.0,20.0,self.obj93)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj93.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj93)
   self.obj93.postAction( cobj0.LHS.CREATE )

   self.obj94=Role(self)
   self.obj94.preAction( cobj0.LHS.CREATE )
   self.obj94.isGraphObjectVisual = True

   if(hasattr(self.obj94, '_setHierarchicalLink')):
     self.obj94._setHierarchicalLink(False)

   # name
   self.obj94.name.setValue('')
   self.obj94.name.setNone()

   self.obj94.GGLabel.setValue(4)
   self.obj94.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(320.0,180.0,self.obj94)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj94.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj94)
   self.obj94.postAction( cobj0.LHS.CREATE )

   self.obj95=posses(self)
   self.obj95.preAction( cobj0.LHS.CREATE )
   self.obj95.isGraphObjectVisual = True

   if(hasattr(self.obj95, '_setHierarchicalLink')):
     self.obj95._setHierarchicalLink(False)

   # rate
   self.obj95.rate.setNone()

   self.obj95.GGLabel.setValue(5)
   self.obj95.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(203.0,70.5,self.obj95)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj95.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj95)
   self.obj95.postAction( cobj0.LHS.CREATE )

   self.obj96=posses(self)
   self.obj96.preAction( cobj0.LHS.CREATE )
   self.obj96.isGraphObjectVisual = True

   if(hasattr(self.obj96, '_setHierarchicalLink')):
     self.obj96._setHierarchicalLink(False)

   # rate
   self.obj96.rate.setNone()

   self.obj96.GGLabel.setValue(6)
   self.obj96.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(93.0,130.5,self.obj96)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj96.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj96)
   self.obj96.postAction( cobj0.LHS.CREATE )

   self.obj97=CapableOf(self)
   self.obj97.preAction( cobj0.LHS.CREATE )
   self.obj97.isGraphObjectVisual = True

   if(hasattr(self.obj97, '_setHierarchicalLink')):
     self.obj97._setHierarchicalLink(False)

   # rate
   self.obj97.rate.setNone()

   self.obj97.GGLabel.setValue(9)
   self.obj97.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(209.5,129.5,self.obj97)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj97.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj97)
   self.obj97.postAction( cobj0.LHS.CREATE )

   self.obj98=require(self)
   self.obj98.preAction( cobj0.LHS.CREATE )
   self.obj98.isGraphObjectVisual = True

   if(hasattr(self.obj98, '_setHierarchicalLink')):
     self.obj98._setHierarchicalLink(False)

   self.obj98.GGLabel.setValue(7)
   self.obj98.graphClass_= graph_require
   if self.genGraphics:
      new_obj = graph_require(222.5,180.0,self.obj98)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj98.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj98)
   self.obj98.postAction( cobj0.LHS.CREATE )

   self.obj99=require(self)
   self.obj99.preAction( cobj0.LHS.CREATE )
   self.obj99.isGraphObjectVisual = True

   if(hasattr(self.obj99, '_setHierarchicalLink')):
     self.obj99._setHierarchicalLink(False)

   self.obj99.GGLabel.setValue(8)
   self.obj99.graphClass_= graph_require
   if self.genGraphics:
      new_obj = graph_require(332.5,120.0,self.obj99)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj99.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj99)
   self.obj99.postAction( cobj0.LHS.CREATE )

   self.obj91.out_connections_.append(self.obj95)
   self.obj95.in_connections_.append(self.obj91)
   self.obj91.out_connections_.append(self.obj96)
   self.obj96.in_connections_.append(self.obj91)
   self.obj91.graphObject_.pendingConnections.append((self.obj91.graphObject_.tag, self.obj96.graphObject_.tag, [85.0, 82.0, 93.0, 130.5], 0, True))
   self.obj91.out_connections_.append(self.obj97)
   self.obj97.in_connections_.append(self.obj91)
   self.obj91.graphObject_.pendingConnections.append((self.obj91.graphObject_.tag, self.obj97.graphObject_.tag, [85.0, 82.0, 163.0, 138.0, 209.5, 129.5], 2, True))
   self.obj94.out_connections_.append(self.obj98)
   self.obj98.in_connections_.append(self.obj94)
   self.obj94.graphObject_.pendingConnections.append((self.obj94.graphObject_.tag, self.obj98.graphObject_.tag, [344.0, 181.0, 222.5, 180.0], 0, True))
   self.obj94.out_connections_.append(self.obj99)
   self.obj99.in_connections_.append(self.obj94)
   self.obj94.graphObject_.pendingConnections.append((self.obj94.graphObject_.tag, self.obj99.graphObject_.tag, [344.0, 181.0, 332.5, 120.0], 0, True))
   self.obj95.out_connections_.append(self.obj93)
   self.obj93.in_connections_.append(self.obj95)
   self.obj95.graphObject_.pendingConnections.append((self.obj95.graphObject_.tag, self.obj93.graphObject_.tag, [321.0, 59.0, 203.0, 70.5], 0, True))
   self.obj96.out_connections_.append(self.obj92)
   self.obj92.in_connections_.append(self.obj96)
   self.obj96.graphObject_.pendingConnections.append((self.obj96.graphObject_.tag, self.obj92.graphObject_.tag, [101.0, 179.0, 93.0, 130.5], 0, True))
   self.obj97.out_connections_.append(self.obj94)
   self.obj94.in_connections_.append(self.obj97)
   self.obj97.graphObject_.pendingConnections.append((self.obj97.graphObject_.tag, self.obj94.graphObject_.tag, [344.0, 181.0, 256.0, 121.0, 209.5, 129.5], 2, True))
   self.obj98.out_connections_.append(self.obj92)
   self.obj92.in_connections_.append(self.obj98)
   self.obj98.graphObject_.pendingConnections.append((self.obj98.graphObject_.tag, self.obj92.graphObject_.tag, [101.0, 179.0, 222.5, 180.0], 0, True))
   self.obj99.out_connections_.append(self.obj93)
   self.obj93.in_connections_.append(self.obj99)

   cobj0.RHS = ASG_omacs(self)

   self.obj101=Agent(self)
   self.obj101.preAction( cobj0.RHS.CREATE )
   self.obj101.isGraphObjectVisual = True

   if(hasattr(self.obj101, '_setHierarchicalLink')):
     self.obj101._setHierarchicalLink(False)

   # price
   self.obj101.price.setNone()

   # name
   self.obj101.name.setValue('')
   self.obj101.name.setNone()

   self.obj101.GGLabel.setValue(1)
   self.obj101.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(60.0,20.0,self.obj101)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj101.graphObject_ = new_obj
   self.obj1010= AttrCalc()
   self.obj1010.Copy=ATOM3Boolean()
   self.obj1010.Copy.setValue(('Copy from LHS', 1))
   self.obj1010.Copy.config = 0
   self.obj1010.Specify=ATOM3Constraint()
   self.obj1010.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj101.GGset2Any['price']= self.obj1010
   self.obj1011= AttrCalc()
   self.obj1011.Copy=ATOM3Boolean()
   self.obj1011.Copy.setValue(('Copy from LHS', 1))
   self.obj1011.Copy.config = 0
   self.obj1011.Specify=ATOM3Constraint()
   self.obj1011.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj101.GGset2Any['name']= self.obj1011

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj101)
   self.obj101.postAction( cobj0.RHS.CREATE )

   self.obj102=Capabilitie(self)
   self.obj102.preAction( cobj0.RHS.CREATE )
   self.obj102.isGraphObjectVisual = True

   if(hasattr(self.obj102, '_setHierarchicalLink')):
     self.obj102._setHierarchicalLink(False)

   # name
   self.obj102.name.setValue('')
   self.obj102.name.setNone()

   self.obj102.GGLabel.setValue(2)
   self.obj102.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(80.0,180.0,self.obj102)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj102.graphObject_ = new_obj
   self.obj1020= AttrCalc()
   self.obj1020.Copy=ATOM3Boolean()
   self.obj1020.Copy.setValue(('Copy from LHS', 1))
   self.obj1020.Copy.config = 0
   self.obj1020.Specify=ATOM3Constraint()
   self.obj1020.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj102.GGset2Any['name']= self.obj1020

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj102)
   self.obj102.postAction( cobj0.RHS.CREATE )

   self.obj103=Capabilitie(self)
   self.obj103.preAction( cobj0.RHS.CREATE )
   self.obj103.isGraphObjectVisual = True

   if(hasattr(self.obj103, '_setHierarchicalLink')):
     self.obj103._setHierarchicalLink(False)

   # name
   self.obj103.name.setValue('')
   self.obj103.name.setNone()

   self.obj103.GGLabel.setValue(3)
   self.obj103.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(300.0,20.0,self.obj103)
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

   self.obj104=Role(self)
   self.obj104.preAction( cobj0.RHS.CREATE )
   self.obj104.isGraphObjectVisual = True

   if(hasattr(self.obj104, '_setHierarchicalLink')):
     self.obj104._setHierarchicalLink(False)

   # name
   self.obj104.name.setValue('')
   self.obj104.name.setNone()

   self.obj104.GGLabel.setValue(4)
   self.obj104.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(320.0,180.0,self.obj104)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj104.graphObject_ = new_obj
   self.obj1040= AttrCalc()
   self.obj1040.Copy=ATOM3Boolean()
   self.obj1040.Copy.setValue(('Copy from LHS', 1))
   self.obj1040.Copy.config = 0
   self.obj1040.Specify=ATOM3Constraint()
   self.obj1040.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj104.GGset2Any['name']= self.obj1040

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj104)
   self.obj104.postAction( cobj0.RHS.CREATE )

   self.obj105=posses(self)
   self.obj105.preAction( cobj0.RHS.CREATE )
   self.obj105.isGraphObjectVisual = True

   if(hasattr(self.obj105, '_setHierarchicalLink')):
     self.obj105._setHierarchicalLink(False)

   # rate
   self.obj105.rate.setNone()

   self.obj105.GGLabel.setValue(5)
   self.obj105.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(203.0,70.5,self.obj105)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj105.graphObject_ = new_obj
   self.obj1050= AttrCalc()
   self.obj1050.Copy=ATOM3Boolean()
   self.obj1050.Copy.setValue(('Copy from LHS', 1))
   self.obj1050.Copy.config = 0
   self.obj1050.Specify=ATOM3Constraint()
   self.obj1050.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj105.GGset2Any['rate']= self.obj1050

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj105)
   self.obj105.postAction( cobj0.RHS.CREATE )

   self.obj106=posses(self)
   self.obj106.preAction( cobj0.RHS.CREATE )
   self.obj106.isGraphObjectVisual = True

   if(hasattr(self.obj106, '_setHierarchicalLink')):
     self.obj106._setHierarchicalLink(False)

   # rate
   self.obj106.rate.setNone()

   self.obj106.GGLabel.setValue(6)
   self.obj106.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(93.0,130.5,self.obj106)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj106.graphObject_ = new_obj
   self.obj1060= AttrCalc()
   self.obj1060.Copy=ATOM3Boolean()
   self.obj1060.Copy.setValue(('Copy from LHS', 1))
   self.obj1060.Copy.config = 0
   self.obj1060.Specify=ATOM3Constraint()
   self.obj1060.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj106.GGset2Any['rate']= self.obj1060

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj106)
   self.obj106.postAction( cobj0.RHS.CREATE )

   self.obj107=CapableOf(self)
   self.obj107.preAction( cobj0.RHS.CREATE )
   self.obj107.isGraphObjectVisual = True

   if(hasattr(self.obj107, '_setHierarchicalLink')):
     self.obj107._setHierarchicalLink(False)

   # rate
   self.obj107.rate.setValue(0.0)

   self.obj107.GGLabel.setValue(9)
   self.obj107.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(209.5,129.5,self.obj107)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj107.graphObject_ = new_obj
   self.obj1070= AttrCalc()
   self.obj1070.Copy=ATOM3Boolean()
   self.obj1070.Copy.setValue(('Copy from LHS', 1))
   self.obj1070.Copy.config = 0
   self.obj1070.Specify=ATOM3Constraint()
   self.obj1070.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj107.GGset2Any['rate']= self.obj1070

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj107)
   self.obj107.postAction( cobj0.RHS.CREATE )

   self.obj108=require(self)
   self.obj108.preAction( cobj0.RHS.CREATE )
   self.obj108.isGraphObjectVisual = True

   if(hasattr(self.obj108, '_setHierarchicalLink')):
     self.obj108._setHierarchicalLink(False)

   self.obj108.GGLabel.setValue(7)
   self.obj108.graphClass_= graph_require
   if self.genGraphics:
      new_obj = graph_require(222.5,180.0,self.obj108)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj108.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj108)
   self.obj108.postAction( cobj0.RHS.CREATE )

   self.obj109=require(self)
   self.obj109.preAction( cobj0.RHS.CREATE )
   self.obj109.isGraphObjectVisual = True

   if(hasattr(self.obj109, '_setHierarchicalLink')):
     self.obj109._setHierarchicalLink(False)

   self.obj109.GGLabel.setValue(8)
   self.obj109.graphClass_= graph_require
   if self.genGraphics:
      new_obj = graph_require(332.5,120.0,self.obj109)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj109.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj109)
   self.obj109.postAction( cobj0.RHS.CREATE )

   self.obj101.out_connections_.append(self.obj105)
   self.obj105.in_connections_.append(self.obj101)
   self.obj101.out_connections_.append(self.obj106)
   self.obj106.in_connections_.append(self.obj101)
   self.obj101.graphObject_.pendingConnections.append((self.obj101.graphObject_.tag, self.obj106.graphObject_.tag, [97.0, 82.0, 93.0, 130.5], 2, 0))
   self.obj101.out_connections_.append(self.obj107)
   self.obj107.in_connections_.append(self.obj101)
   self.obj101.graphObject_.pendingConnections.append((self.obj101.graphObject_.tag, self.obj107.graphObject_.tag, [97.0, 82.0, 209.5, 129.5], 2, 0))
   self.obj104.out_connections_.append(self.obj108)
   self.obj108.in_connections_.append(self.obj104)
   self.obj104.graphObject_.pendingConnections.append((self.obj104.graphObject_.tag, self.obj108.graphObject_.tag, [351.0, 180.0, 222.5, 180.0], 2, 0))
   self.obj104.out_connections_.append(self.obj109)
   self.obj109.in_connections_.append(self.obj104)
   self.obj104.graphObject_.pendingConnections.append((self.obj104.graphObject_.tag, self.obj109.graphObject_.tag, [351.0, 180.0, 332.5, 120.0], 2, 0))
   self.obj105.out_connections_.append(self.obj103)
   self.obj103.in_connections_.append(self.obj105)
   self.obj105.graphObject_.pendingConnections.append((self.obj105.graphObject_.tag, self.obj103.graphObject_.tag, [331.0, 63.0, 203.0, 70.5], 2, 0))
   self.obj106.out_connections_.append(self.obj102)
   self.obj102.in_connections_.append(self.obj106)
   self.obj106.graphObject_.pendingConnections.append((self.obj106.graphObject_.tag, self.obj102.graphObject_.tag, [111.0, 183.0, 93.0, 130.5], 2, 0))
   self.obj107.out_connections_.append(self.obj104)
   self.obj104.in_connections_.append(self.obj107)
   self.obj107.graphObject_.pendingConnections.append((self.obj107.graphObject_.tag, self.obj104.graphObject_.tag, [351.0, 180.0, 209.5, 129.5], 2, 0))
   self.obj108.out_connections_.append(self.obj102)
   self.obj102.in_connections_.append(self.obj108)
   self.obj108.graphObject_.pendingConnections.append((self.obj108.graphObject_.tag, self.obj102.graphObject_.tag, [111.0, 183.0, 222.5, 180.0], 2, 0))
   self.obj109.out_connections_.append(self.obj103)
   self.obj103.in_connections_.append(self.obj109)

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

   self.obj114=Agent(self)
   self.obj114.preAction( cobj0.LHS.CREATE )
   self.obj114.isGraphObjectVisual = True

   if(hasattr(self.obj114, '_setHierarchicalLink')):
     self.obj114._setHierarchicalLink(False)

   # price
   self.obj114.price.setNone()

   # name
   self.obj114.name.setValue('')
   self.obj114.name.setNone()

   self.obj114.GGLabel.setValue(1)
   self.obj114.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(100.0,20.0,self.obj114)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj114.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj114)
   self.obj114.postAction( cobj0.LHS.CREATE )

   self.obj115=Capabilitie(self)
   self.obj115.preAction( cobj0.LHS.CREATE )
   self.obj115.isGraphObjectVisual = True

   if(hasattr(self.obj115, '_setHierarchicalLink')):
     self.obj115._setHierarchicalLink(False)

   # name
   self.obj115.name.setValue('')
   self.obj115.name.setNone()

   self.obj115.GGLabel.setValue(3)
   self.obj115.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(340.0,40.0,self.obj115)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj115.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj115)
   self.obj115.postAction( cobj0.LHS.CREATE )

   self.obj116=Capabilitie(self)
   self.obj116.preAction( cobj0.LHS.CREATE )
   self.obj116.isGraphObjectVisual = True

   if(hasattr(self.obj116, '_setHierarchicalLink')):
     self.obj116._setHierarchicalLink(False)

   # name
   self.obj116.name.setValue('')
   self.obj116.name.setNone()

   self.obj116.GGLabel.setValue(4)
   self.obj116.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(140.0,160.0,self.obj116)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj116.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj116)
   self.obj116.postAction( cobj0.LHS.CREATE )

   self.obj117=Role(self)
   self.obj117.preAction( cobj0.LHS.CREATE )
   self.obj117.isGraphObjectVisual = True

   if(hasattr(self.obj117, '_setHierarchicalLink')):
     self.obj117._setHierarchicalLink(False)

   # name
   self.obj117.name.setValue('')
   self.obj117.name.setNone()

   self.obj117.GGLabel.setValue(2)
   self.obj117.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(300.0,140.0,self.obj117)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj117.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj117)
   self.obj117.postAction( cobj0.LHS.CREATE )

   self.obj118=posses(self)
   self.obj118.preAction( cobj0.LHS.CREATE )
   self.obj118.isGraphObjectVisual = True

   if(hasattr(self.obj118, '_setHierarchicalLink')):
     self.obj118._setHierarchicalLink(False)

   # rate
   self.obj118.rate.setNone()

   self.obj118.GGLabel.setValue(5)
   self.obj118.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(143.0,120.5,self.obj118)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj118.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj118)
   self.obj118.postAction( cobj0.LHS.CREATE )

   self.obj119=CapableOf(self)
   self.obj119.preAction( cobj0.LHS.CREATE )
   self.obj119.isGraphObjectVisual = True

   if(hasattr(self.obj119, '_setHierarchicalLink')):
     self.obj119._setHierarchicalLink(False)

   # rate
   self.obj119.rate.setNone()

   self.obj119.GGLabel.setValue(8)
   self.obj119.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(224.5,111.5,self.obj119)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj119.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj119)
   self.obj119.postAction( cobj0.LHS.CREATE )

   self.obj120=require(self)
   self.obj120.preAction( cobj0.LHS.CREATE )
   self.obj120.isGraphObjectVisual = True

   if(hasattr(self.obj120, '_setHierarchicalLink')):
     self.obj120._setHierarchicalLink(False)

   self.obj120.GGLabel.setValue(7)
   self.obj120.graphClass_= graph_require
   if self.genGraphics:
      new_obj = graph_require(242.5,192.5,self.obj120)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj120.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj120)
   self.obj120.postAction( cobj0.LHS.CREATE )

   self.obj121=require(self)
   self.obj121.preAction( cobj0.LHS.CREATE )
   self.obj121.isGraphObjectVisual = True

   if(hasattr(self.obj121, '_setHierarchicalLink')):
     self.obj121._setHierarchicalLink(False)

   self.obj121.GGLabel.setValue(9)
   self.obj121.graphClass_= graph_require
   if self.genGraphics:
      new_obj = graph_require(351.0,111.5,self.obj121)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj121.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj121)
   self.obj121.postAction( cobj0.LHS.CREATE )

   self.obj114.out_connections_.append(self.obj118)
   self.obj118.in_connections_.append(self.obj114)
   self.obj114.graphObject_.pendingConnections.append((self.obj114.graphObject_.tag, self.obj118.graphObject_.tag, [137.0, 82.0, 143.0, 120.5], 2, 0))
   self.obj114.out_connections_.append(self.obj119)
   self.obj119.in_connections_.append(self.obj114)
   self.obj114.graphObject_.pendingConnections.append((self.obj114.graphObject_.tag, self.obj119.graphObject_.tag, [125.0, 82.0, 224.5, 111.5], 0, True))
   self.obj117.out_connections_.append(self.obj120)
   self.obj120.in_connections_.append(self.obj117)
   self.obj117.graphObject_.pendingConnections.append((self.obj117.graphObject_.tag, self.obj120.graphObject_.tag, [324.0, 186.0, 242.5, 192.5], 0, True))
   self.obj117.out_connections_.append(self.obj121)
   self.obj121.in_connections_.append(self.obj117)
   self.obj117.graphObject_.pendingConnections.append((self.obj117.graphObject_.tag, self.obj121.graphObject_.tag, [331.0, 140.0, 351.0, 111.5], 0, True))
   self.obj118.out_connections_.append(self.obj116)
   self.obj116.in_connections_.append(self.obj118)
   self.obj118.graphObject_.pendingConnections.append((self.obj118.graphObject_.tag, self.obj116.graphObject_.tag, [161.0, 159.0, 143.0, 120.5], 0, True))
   self.obj119.out_connections_.append(self.obj117)
   self.obj117.in_connections_.append(self.obj119)
   self.obj119.graphObject_.pendingConnections.append((self.obj119.graphObject_.tag, self.obj117.graphObject_.tag, [324.0, 141.0, 224.5, 111.5], 0, True))
   self.obj120.out_connections_.append(self.obj116)
   self.obj116.in_connections_.append(self.obj120)
   self.obj120.graphObject_.pendingConnections.append((self.obj120.graphObject_.tag, self.obj116.graphObject_.tag, [161.0, 199.0, 242.5, 192.5], 0, True))
   self.obj121.out_connections_.append(self.obj115)
   self.obj115.in_connections_.append(self.obj121)
   self.obj121.graphObject_.pendingConnections.append((self.obj121.graphObject_.tag, self.obj115.graphObject_.tag, [371.0, 83.0, 351.0, 111.5], 0, True))

   cobj0.RHS = ASG_omacs(self)

   self.obj123=Agent(self)
   self.obj123.preAction( cobj0.RHS.CREATE )
   self.obj123.isGraphObjectVisual = True

   if(hasattr(self.obj123, '_setHierarchicalLink')):
     self.obj123._setHierarchicalLink(False)

   # price
   self.obj123.price.setNone()

   # name
   self.obj123.name.setValue('')
   self.obj123.name.setNone()

   self.obj123.GGLabel.setValue(1)
   self.obj123.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(100.0,20.0,self.obj123)
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

   self.obj124=Capabilitie(self)
   self.obj124.preAction( cobj0.RHS.CREATE )
   self.obj124.isGraphObjectVisual = True

   if(hasattr(self.obj124, '_setHierarchicalLink')):
     self.obj124._setHierarchicalLink(False)

   # name
   self.obj124.name.setValue('')
   self.obj124.name.setNone()

   self.obj124.GGLabel.setValue(3)
   self.obj124.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(340.0,40.0,self.obj124)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj124.graphObject_ = new_obj
   self.obj1240= AttrCalc()
   self.obj1240.Copy=ATOM3Boolean()
   self.obj1240.Copy.setValue(('Copy from LHS', 1))
   self.obj1240.Copy.config = 0
   self.obj1240.Specify=ATOM3Constraint()
   self.obj1240.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj124.GGset2Any['name']= self.obj1240

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj124)
   self.obj124.postAction( cobj0.RHS.CREATE )

   self.obj125=Capabilitie(self)
   self.obj125.preAction( cobj0.RHS.CREATE )
   self.obj125.isGraphObjectVisual = True

   if(hasattr(self.obj125, '_setHierarchicalLink')):
     self.obj125._setHierarchicalLink(False)

   # name
   self.obj125.name.setValue('')
   self.obj125.name.setNone()

   self.obj125.GGLabel.setValue(4)
   self.obj125.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(140.0,160.0,self.obj125)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj125.graphObject_ = new_obj
   self.obj1250= AttrCalc()
   self.obj1250.Copy=ATOM3Boolean()
   self.obj1250.Copy.setValue(('Copy from LHS', 1))
   self.obj1250.Copy.config = 0
   self.obj1250.Specify=ATOM3Constraint()
   self.obj1250.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj125.GGset2Any['name']= self.obj1250

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj125)
   self.obj125.postAction( cobj0.RHS.CREATE )

   self.obj126=Role(self)
   self.obj126.preAction( cobj0.RHS.CREATE )
   self.obj126.isGraphObjectVisual = True

   if(hasattr(self.obj126, '_setHierarchicalLink')):
     self.obj126._setHierarchicalLink(False)

   # name
   self.obj126.name.setValue('')
   self.obj126.name.setNone()

   self.obj126.GGLabel.setValue(2)
   self.obj126.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(300.0,140.0,self.obj126)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj126.graphObject_ = new_obj
   self.obj1260= AttrCalc()
   self.obj1260.Copy=ATOM3Boolean()
   self.obj1260.Copy.setValue(('Copy from LHS', 1))
   self.obj1260.Copy.config = 0
   self.obj1260.Specify=ATOM3Constraint()
   self.obj1260.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj126.GGset2Any['name']= self.obj1260

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj126)
   self.obj126.postAction( cobj0.RHS.CREATE )

   self.obj127=posses(self)
   self.obj127.preAction( cobj0.RHS.CREATE )
   self.obj127.isGraphObjectVisual = True

   if(hasattr(self.obj127, '_setHierarchicalLink')):
     self.obj127._setHierarchicalLink(False)

   # rate
   self.obj127.rate.setNone()

   self.obj127.GGLabel.setValue(5)
   self.obj127.graphClass_= graph_posses
   if self.genGraphics:
      new_obj = graph_posses(143.0,120.5,self.obj127)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj127.graphObject_ = new_obj
   self.obj1270= AttrCalc()
   self.obj1270.Copy=ATOM3Boolean()
   self.obj1270.Copy.setValue(('Copy from LHS', 1))
   self.obj1270.Copy.config = 0
   self.obj1270.Specify=ATOM3Constraint()
   self.obj1270.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj127.GGset2Any['rate']= self.obj1270

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj127)
   self.obj127.postAction( cobj0.RHS.CREATE )

   self.obj128=require(self)
   self.obj128.preAction( cobj0.RHS.CREATE )
   self.obj128.isGraphObjectVisual = True

   if(hasattr(self.obj128, '_setHierarchicalLink')):
     self.obj128._setHierarchicalLink(False)

   self.obj128.GGLabel.setValue(7)
   self.obj128.graphClass_= graph_require
   if self.genGraphics:
      new_obj = graph_require(242.5,192.5,self.obj128)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj128.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj128)
   self.obj128.postAction( cobj0.RHS.CREATE )

   self.obj129=require(self)
   self.obj129.preAction( cobj0.RHS.CREATE )
   self.obj129.isGraphObjectVisual = True

   if(hasattr(self.obj129, '_setHierarchicalLink')):
     self.obj129._setHierarchicalLink(False)

   self.obj129.GGLabel.setValue(9)
   self.obj129.graphClass_= graph_require
   if self.genGraphics:
      new_obj = graph_require(351.0,111.5,self.obj129)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj129.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj129)
   self.obj129.postAction( cobj0.RHS.CREATE )

   self.obj123.out_connections_.append(self.obj127)
   self.obj127.in_connections_.append(self.obj123)
   self.obj123.graphObject_.pendingConnections.append((self.obj123.graphObject_.tag, self.obj127.graphObject_.tag, [137.0, 82.0, 143.0, 120.5], 2, 0))
   self.obj126.out_connections_.append(self.obj128)
   self.obj128.in_connections_.append(self.obj126)
   self.obj126.graphObject_.pendingConnections.append((self.obj126.graphObject_.tag, self.obj128.graphObject_.tag, [331.0, 185.0, 242.5, 192.5], 2, 0))
   self.obj126.out_connections_.append(self.obj129)
   self.obj129.in_connections_.append(self.obj126)
   self.obj126.graphObject_.pendingConnections.append((self.obj126.graphObject_.tag, self.obj129.graphObject_.tag, [331.0, 140.0, 351.0, 111.5], 0, True))
   self.obj127.out_connections_.append(self.obj125)
   self.obj125.in_connections_.append(self.obj127)
   self.obj127.graphObject_.pendingConnections.append((self.obj127.graphObject_.tag, self.obj125.graphObject_.tag, [171.0, 163.0, 143.0, 120.5], 2, 0))
   self.obj128.out_connections_.append(self.obj125)
   self.obj125.in_connections_.append(self.obj128)
   self.obj128.graphObject_.pendingConnections.append((self.obj128.graphObject_.tag, self.obj125.graphObject_.tag, [171.0, 203.0, 242.5, 192.5], 2, 0))
   self.obj129.out_connections_.append(self.obj124)
   self.obj124.in_connections_.append(self.obj129)
   self.obj129.graphObject_.pendingConnections.append((self.obj129.graphObject_.tag, self.obj124.graphObject_.tag, [371.0, 83.0, 351.0, 111.5], 0, True))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'agent = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nrole  = self.getMatched(graphID, self.LHS.nodeWithLabel(2))\nc1 = self.getMatched(graphID, self.LHS.nodeWithLabel(3))\nc2 = self.getMatched(graphID, self.LHS.nodeWithLabel(4))\n\nreturn not ( hasattr(c1,  agent.name.getValue() ) and \nhasattr(c1,  role.name.getValue() ) and\nhasattr(c2,  agent.name.getValue() ) and  hasattr(c2, role.name.getValue() ) )\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'agent = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nc1 = self.getMatched(graphID, self.LHS.nodeWithLabel(4))\nc2 = self.getMatched(graphID, self.LHS.nodeWithLabel(3))\nrole = self.getMatched(graphID, self.LHS.nodeWithLabel(2))\n\nsetattr( c1 ,  agent.name.getValue() , True )\nsetattr( c1 ,  role.name.getValue() , True )\n\nsetattr( c2 ,  agent.name.getValue() , True )\nsetattr( c2 ,  role.name.getValue() , True )\nprint\' Eli : (\'+agent.name.getValue()+\',\'+c1.name.getValue()+\',\'+c2.name.getValue()+\',\'+role.name.getValue()+\')\'\n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('TransAgent2Raw', 20)
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

   self.obj134=Agent(self)
   self.obj134.preAction( cobj0.LHS.CREATE )
   self.obj134.isGraphObjectVisual = True

   if(hasattr(self.obj134, '_setHierarchicalLink')):
     self.obj134._setHierarchicalLink(False)

   # price
   self.obj134.price.setNone()

   # name
   self.obj134.name.setValue('')
   self.obj134.name.setNone()

   self.obj134.GGLabel.setValue(1)
   self.obj134.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(100.0,20.0,self.obj134)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj134.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj134)
   self.obj134.postAction( cobj0.LHS.CREATE )

   self.obj135=Role(self)
   self.obj135.preAction( cobj0.LHS.CREATE )
   self.obj135.isGraphObjectVisual = True

   if(hasattr(self.obj135, '_setHierarchicalLink')):
     self.obj135._setHierarchicalLink(False)

   # name
   self.obj135.name.setValue('')
   self.obj135.name.setNone()

   self.obj135.GGLabel.setValue(2)
   self.obj135.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(360.0,160.0,self.obj135)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj135.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj135)
   self.obj135.postAction( cobj0.LHS.CREATE )

   self.obj136=CapableOf(self)
   self.obj136.preAction( cobj0.LHS.CREATE )
   self.obj136.isGraphObjectVisual = True

   if(hasattr(self.obj136, '_setHierarchicalLink')):
     self.obj136._setHierarchicalLink(False)

   # rate
   self.obj136.rate.setNone()

   self.obj136.GGLabel.setValue(3)
   self.obj136.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(281.5,134.0,self.obj136)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj136.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj136)
   self.obj136.postAction( cobj0.LHS.CREATE )

   self.obj134.out_connections_.append(self.obj136)
   self.obj136.in_connections_.append(self.obj134)
   self.obj134.graphObject_.pendingConnections.append((self.obj134.graphObject_.tag, self.obj136.graphObject_.tag, [125.0, 82.0, 161.0, 153.0, 281.5, 134.0], 2, True))
   self.obj136.out_connections_.append(self.obj135)
   self.obj135.in_connections_.append(self.obj136)
   self.obj136.graphObject_.pendingConnections.append((self.obj136.graphObject_.tag, self.obj135.graphObject_.tag, [384.0, 161.0, 402.0, 115.0, 281.5, 134.0], 2, True))

   cobj0.RHS = ASG_omacs(self)
   cobj0.RHS.merge(ASG_pns(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj140=Agent(self)
   self.obj140.preAction( cobj0.RHS.CREATE )
   self.obj140.isGraphObjectVisual = True

   if(hasattr(self.obj140, '_setHierarchicalLink')):
     self.obj140._setHierarchicalLink(False)

   # price
   self.obj140.price.setNone()

   # name
   self.obj140.name.setValue('')
   self.obj140.name.setNone()

   self.obj140.GGLabel.setValue(1)
   self.obj140.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(100.0,20.0,self.obj140)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj140.graphObject_ = new_obj
   self.obj1400= AttrCalc()
   self.obj1400.Copy=ATOM3Boolean()
   self.obj1400.Copy.setValue(('Copy from LHS', 1))
   self.obj1400.Copy.config = 0
   self.obj1400.Specify=ATOM3Constraint()
   self.obj1400.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj140.GGset2Any['price']= self.obj1400
   self.obj1401= AttrCalc()
   self.obj1401.Copy=ATOM3Boolean()
   self.obj1401.Copy.setValue(('Copy from LHS', 1))
   self.obj1401.Copy.config = 0
   self.obj1401.Specify=ATOM3Constraint()
   self.obj1401.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj140.GGset2Any['name']= self.obj1401

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj140)
   self.obj140.postAction( cobj0.RHS.CREATE )

   self.obj141=Role(self)
   self.obj141.preAction( cobj0.RHS.CREATE )
   self.obj141.isGraphObjectVisual = True

   if(hasattr(self.obj141, '_setHierarchicalLink')):
     self.obj141._setHierarchicalLink(False)

   # name
   self.obj141.name.setValue('')
   self.obj141.name.setNone()

   self.obj141.GGLabel.setValue(2)
   self.obj141.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(360.0,160.0,self.obj141)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj141.graphObject_ = new_obj
   self.obj1410= AttrCalc()
   self.obj1410.Copy=ATOM3Boolean()
   self.obj1410.Copy.setValue(('Copy from LHS', 1))
   self.obj1410.Copy.config = 0
   self.obj1410.Specify=ATOM3Constraint()
   self.obj1410.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj141.GGset2Any['name']= self.obj1410

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj141)
   self.obj141.postAction( cobj0.RHS.CREATE )

   self.obj142=CapableOf(self)
   self.obj142.preAction( cobj0.RHS.CREATE )
   self.obj142.isGraphObjectVisual = True

   if(hasattr(self.obj142, '_setHierarchicalLink')):
     self.obj142._setHierarchicalLink(False)

   # rate
   self.obj142.rate.setValue(0.0)

   self.obj142.GGLabel.setValue(3)
   self.obj142.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(281.5,134.0,self.obj142)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj142.graphObject_ = new_obj
   self.obj1420= AttrCalc()
   self.obj1420.Copy=ATOM3Boolean()
   self.obj1420.Copy.setValue(('Copy from LHS', 1))
   self.obj1420.Copy.config = 0
   self.obj1420.Specify=ATOM3Constraint()
   self.obj1420.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj142.GGset2Any['rate']= self.obj1420

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj142)
   self.obj142.postAction( cobj0.RHS.CREATE )

   self.obj143=rawMaterial(self)
   self.obj143.preAction( cobj0.RHS.CREATE )
   self.obj143.isGraphObjectVisual = True

   if(hasattr(self.obj143, '_setHierarchicalLink')):
     self.obj143._setHierarchicalLink(False)

   # MaxFlow
   self.obj143.MaxFlow.setValue(999999)

   # price
   self.obj143.price.setValue(0)

   # Name
   self.obj143.Name.setValue('')
   self.obj143.Name.setNone()

   # ReqFlow
   self.obj143.ReqFlow.setValue(0)

   self.obj143.GGLabel.setValue(6)
   self.obj143.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(280.0,20.0,self.obj143)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj143.graphObject_ = new_obj
   self.obj1430= AttrCalc()
   self.obj1430.Copy=ATOM3Boolean()
   self.obj1430.Copy.setValue(('Copy from LHS', 1))
   self.obj1430.Copy.config = 0
   self.obj1430.Specify=ATOM3Constraint()
   self.obj1430.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj143.GGset2Any['MaxFlow']= self.obj1430
   self.obj1431= AttrCalc()
   self.obj1431.Copy=ATOM3Boolean()
   self.obj1431.Copy.setValue(('Copy from LHS', 1))
   self.obj1431.Copy.config = 0
   self.obj1431.Specify=ATOM3Constraint()
   self.obj1431.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj143.GGset2Any['price']= self.obj1431
   self.obj1432= AttrCalc()
   self.obj1432.Copy=ATOM3Boolean()
   self.obj1432.Copy.setValue(('Copy from LHS', 0))
   self.obj1432.Copy.config = 0
   self.obj1432.Specify=ATOM3Constraint()
   self.obj1432.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()\n\n\n\n'))
   self.obj143.GGset2Any['Name']= self.obj1432
   self.obj1433= AttrCalc()
   self.obj1433.Copy=ATOM3Boolean()
   self.obj1433.Copy.setValue(('Copy from LHS', 1))
   self.obj1433.Copy.config = 0
   self.obj1433.Specify=ATOM3Constraint()
   self.obj1433.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj143.GGset2Any['ReqFlow']= self.obj1433

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj143)
   self.obj143.postAction( cobj0.RHS.CREATE )

   self.obj144=GenericGraphEdge(self)
   self.obj144.preAction( cobj0.RHS.CREATE )
   self.obj144.isGraphObjectVisual = True

   if(hasattr(self.obj144, '_setHierarchicalLink')):
     self.obj144._setHierarchicalLink(False)

   self.obj144.GGLabel.setValue(7)
   self.obj144.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(220.5,79.0,self.obj144)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj144.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj144)
   self.obj144.postAction( cobj0.RHS.CREATE )

   self.obj140.out_connections_.append(self.obj142)
   self.obj142.in_connections_.append(self.obj140)
   self.obj140.graphObject_.pendingConnections.append((self.obj140.graphObject_.tag, self.obj142.graphObject_.tag, [137.0, 82.0, 281.5, 134.0], 2, 0))
   self.obj140.out_connections_.append(self.obj144)
   self.obj144.in_connections_.append(self.obj140)
   self.obj140.graphObject_.pendingConnections.append((self.obj140.graphObject_.tag, self.obj144.graphObject_.tag, [137.0, 82.0, 220.5, 79.0], 0, True))
   self.obj142.out_connections_.append(self.obj141)
   self.obj141.in_connections_.append(self.obj142)
   self.obj142.graphObject_.pendingConnections.append((self.obj142.graphObject_.tag, self.obj141.graphObject_.tag, [391.0, 160.0, 281.5, 134.0], 2, 0))
   self.obj144.out_connections_.append(self.obj143)
   self.obj143.in_connections_.append(self.obj144)
   self.obj144.graphObject_.pendingConnections.append((self.obj144.graphObject_.tag, self.obj143.graphObject_.tag, [304.0, 76.0, 220.5, 79.0], 0, True))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nreturn not hasattr(node, "Agent2Raw")\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'node = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) )\nnode.Agent2Raw = True \n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('TransLinkAR2OpUnit', 20)
   cobj0.Order=ATOM3Integer(7)
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

   self.obj149=Agent(self)
   self.obj149.preAction( cobj0.LHS.CREATE )
   self.obj149.isGraphObjectVisual = True

   if(hasattr(self.obj149, '_setHierarchicalLink')):
     self.obj149._setHierarchicalLink(False)

   # price
   self.obj149.price.setNone()

   # name
   self.obj149.name.setValue('')
   self.obj149.name.setNone()

   self.obj149.GGLabel.setValue(1)
   self.obj149.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(60.0,40.0,self.obj149)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj149.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj149)
   self.obj149.postAction( cobj0.LHS.CREATE )

   self.obj150=Role(self)
   self.obj150.preAction( cobj0.LHS.CREATE )
   self.obj150.isGraphObjectVisual = True

   if(hasattr(self.obj150, '_setHierarchicalLink')):
     self.obj150._setHierarchicalLink(False)

   # name
   self.obj150.name.setValue('')
   self.obj150.name.setNone()

   self.obj150.GGLabel.setValue(2)
   self.obj150.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(320.0,220.0,self.obj150)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj150.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj150)
   self.obj150.postAction( cobj0.LHS.CREATE )

   self.obj151=CapableOf(self)
   self.obj151.preAction( cobj0.LHS.CREATE )
   self.obj151.isGraphObjectVisual = True

   if(hasattr(self.obj151, '_setHierarchicalLink')):
     self.obj151._setHierarchicalLink(False)

   # rate
   self.obj151.rate.setNone()

   self.obj151.GGLabel.setValue(3)
   self.obj151.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(230.0,173.0,self.obj151)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj151.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj151)
   self.obj151.postAction( cobj0.LHS.CREATE )

   self.obj149.out_connections_.append(self.obj151)
   self.obj151.in_connections_.append(self.obj149)
   self.obj149.graphObject_.pendingConnections.append((self.obj149.graphObject_.tag, self.obj151.graphObject_.tag, [85.0, 102.0, 117.0, 188.0, 230.0, 173.0], 2, True))
   self.obj151.out_connections_.append(self.obj150)
   self.obj150.in_connections_.append(self.obj151)
   self.obj151.graphObject_.pendingConnections.append((self.obj151.graphObject_.tag, self.obj150.graphObject_.tag, [344.0, 221.0, 343.0, 158.0, 230.0, 173.0], 2, True))

   cobj0.RHS = ASG_omacs(self)
   cobj0.RHS.merge(ASG_pns(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj155=Agent(self)
   self.obj155.preAction( cobj0.RHS.CREATE )
   self.obj155.isGraphObjectVisual = True

   if(hasattr(self.obj155, '_setHierarchicalLink')):
     self.obj155._setHierarchicalLink(False)

   # price
   self.obj155.price.setNone()

   # name
   self.obj155.name.setValue('')
   self.obj155.name.setNone()

   self.obj155.GGLabel.setValue(1)
   self.obj155.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(60.0,40.0,self.obj155)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj155.graphObject_ = new_obj
   self.obj1550= AttrCalc()
   self.obj1550.Copy=ATOM3Boolean()
   self.obj1550.Copy.setValue(('Copy from LHS', 1))
   self.obj1550.Copy.config = 0
   self.obj1550.Specify=ATOM3Constraint()
   self.obj1550.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj155.GGset2Any['price']= self.obj1550
   self.obj1551= AttrCalc()
   self.obj1551.Copy=ATOM3Boolean()
   self.obj1551.Copy.setValue(('Copy from LHS', 1))
   self.obj1551.Copy.config = 0
   self.obj1551.Specify=ATOM3Constraint()
   self.obj1551.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj155.GGset2Any['name']= self.obj1551

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj155)
   self.obj155.postAction( cobj0.RHS.CREATE )

   self.obj156=Role(self)
   self.obj156.preAction( cobj0.RHS.CREATE )
   self.obj156.isGraphObjectVisual = True

   if(hasattr(self.obj156, '_setHierarchicalLink')):
     self.obj156._setHierarchicalLink(False)

   # name
   self.obj156.name.setValue('')
   self.obj156.name.setNone()

   self.obj156.GGLabel.setValue(2)
   self.obj156.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(320.0,220.0,self.obj156)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj156.graphObject_ = new_obj
   self.obj1560= AttrCalc()
   self.obj1560.Copy=ATOM3Boolean()
   self.obj1560.Copy.setValue(('Copy from LHS', 1))
   self.obj1560.Copy.config = 0
   self.obj1560.Specify=ATOM3Constraint()
   self.obj1560.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj156.GGset2Any['name']= self.obj1560

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj156)
   self.obj156.postAction( cobj0.RHS.CREATE )

   self.obj157=CapableOf(self)
   self.obj157.preAction( cobj0.RHS.CREATE )
   self.obj157.isGraphObjectVisual = True

   if(hasattr(self.obj157, '_setHierarchicalLink')):
     self.obj157._setHierarchicalLink(False)

   # rate
   self.obj157.rate.setNone()

   self.obj157.GGLabel.setValue(3)
   self.obj157.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(230.0,173.0,self.obj157)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj157.graphObject_ = new_obj
   self.obj1570= AttrCalc()
   self.obj1570.Copy=ATOM3Boolean()
   self.obj1570.Copy.setValue(('Copy from LHS', 1))
   self.obj1570.Copy.config = 0
   self.obj1570.Specify=ATOM3Constraint()
   self.obj1570.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj157.GGset2Any['rate']= self.obj1570

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj157)
   self.obj157.postAction( cobj0.RHS.CREATE )

   self.obj158=operatingUnit(self)
   self.obj158.preAction( cobj0.RHS.CREATE )
   self.obj158.isGraphObjectVisual = True

   if(hasattr(self.obj158, '_setHierarchicalLink')):
     self.obj158._setHierarchicalLink(False)

   # OperCostProp
   self.obj158.OperCostProp.setValue(0.0)

   # name
   self.obj158.name.setValue('')
   self.obj158.name.setNone()

   # OperCostFix
   self.obj158.OperCostFix.setValue(0.0)

   self.obj158.GGLabel.setValue(5)
   self.obj158.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(60.0,220.0,self.obj158)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj158.graphObject_ = new_obj
   self.obj1580= AttrCalc()
   self.obj1580.Copy=ATOM3Boolean()
   self.obj1580.Copy.setValue(('Copy from LHS', 1))
   self.obj1580.Copy.config = 0
   self.obj1580.Specify=ATOM3Constraint()
   self.obj1580.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj158.GGset2Any['OperCostProp']= self.obj1580
   self.obj1581= AttrCalc()
   self.obj1581.Copy=ATOM3Boolean()
   self.obj1581.Copy.setValue(('Copy from LHS', 0))
   self.obj1581.Copy.config = 0
   self.obj1581.Specify=ATOM3Constraint()
   self.obj1581.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()+\' \'+self.getMatched(graphID, self.LHS.nodeWithLabel(2)).name.getValue()\n\n\n\n'))
   self.obj158.GGset2Any['name']= self.obj1581
   self.obj1582= AttrCalc()
   self.obj1582.Copy=ATOM3Boolean()
   self.obj1582.Copy.setValue(('Copy from LHS', 1))
   self.obj1582.Copy.config = 0
   self.obj1582.Specify=ATOM3Constraint()
   self.obj1582.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj158.GGset2Any['OperCostFix']= self.obj1582

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj158)
   self.obj158.postAction( cobj0.RHS.CREATE )

   self.obj159=GenericGraphEdge(self)
   self.obj159.preAction( cobj0.RHS.CREATE )
   self.obj159.isGraphObjectVisual = True

   if(hasattr(self.obj159, '_setHierarchicalLink')):
     self.obj159._setHierarchicalLink(False)

   self.obj159.GGLabel.setValue(6)
   self.obj159.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(103.5,161.5,self.obj159)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj159.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj159)
   self.obj159.postAction( cobj0.RHS.CREATE )

   self.obj155.out_connections_.append(self.obj157)
   self.obj157.in_connections_.append(self.obj155)
   self.obj155.graphObject_.pendingConnections.append((self.obj155.graphObject_.tag, self.obj157.graphObject_.tag, [97.0, 102.0, 230.0, 173.0], 2, 0))
   self.obj155.out_connections_.append(self.obj159)
   self.obj159.in_connections_.append(self.obj155)
   self.obj155.graphObject_.pendingConnections.append((self.obj155.graphObject_.tag, self.obj159.graphObject_.tag, [97.0, 102.0, 103.5, 161.5], 0, True))
   self.obj157.out_connections_.append(self.obj156)
   self.obj156.in_connections_.append(self.obj157)
   self.obj157.graphObject_.pendingConnections.append((self.obj157.graphObject_.tag, self.obj156.graphObject_.tag, [351.0, 220.0, 230.0, 173.0], 2, 0))
   self.obj159.out_connections_.append(self.obj158)
   self.obj158.in_connections_.append(self.obj159)
   self.obj159.graphObject_.pendingConnections.append((self.obj159.graphObject_.tag, self.obj158.graphObject_.tag, [110.0, 221.0, 103.5, 161.5], 0, True))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nnode2 = self.getMatched(graphID, self.LHS.nodeWithLabel(2))\nprint node.name.getValue()+\' \'+node2.name.getValue()\n# remplaceed by  "LinkAR2OpUnit"\nreturn not(  hasattr(node,node2.name.getValue()+\'7\') and hasattr(node2, node.name.getValue()+\'7\') )\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'node = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) )\n\nnode2 = self.getMatched ( graphID , self.LHS.nodeWithLabel(2) )\nsetattr( node ,node2.name.getValue()+\'7\' ,True )\nsetattr( node2 ,node.name.getValue()+\'7\' ,True )\n\n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('TransGoal2Mat', 20)
   cobj0.Order=ATOM3Integer(9)
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

   self.obj165=Goal(self)
   self.obj165.preAction( cobj0.LHS.CREATE )
   self.obj165.isGraphObjectVisual = True

   if(hasattr(self.obj165, '_setHierarchicalLink')):
     self.obj165._setHierarchicalLink(False)

   # name
   self.obj165.name.setValue('')
   self.obj165.name.setNone()

   self.obj165.GGLabel.setValue(1)
   self.obj165.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(80.0,80.0,self.obj165)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj165.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj165)
   self.obj165.postAction( cobj0.LHS.CREATE )


   cobj0.RHS = ASG_pns(self)
   cobj0.RHS.merge(ASG_omacs(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj169=metarial(self)
   self.obj169.preAction( cobj0.RHS.CREATE )
   self.obj169.isGraphObjectVisual = True

   if(hasattr(self.obj169, '_setHierarchicalLink')):
     self.obj169._setHierarchicalLink(False)

   # MaxFlow
   self.obj169.MaxFlow.setValue(999999)

   # price
   self.obj169.price.setValue(0)

   # Name
   self.obj169.Name.setValue('')
   self.obj169.Name.setNone()

   # ReqFlow
   self.obj169.ReqFlow.setValue(0)

   self.obj169.GGLabel.setValue(2)
   self.obj169.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(300.0,60.0,self.obj169)
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
   self.obj169.GGset2Any['MaxFlow']= self.obj1690
   self.obj1691= AttrCalc()
   self.obj1691.Copy=ATOM3Boolean()
   self.obj1691.Copy.setValue(('Copy from LHS', 0))
   self.obj1691.Copy.config = 0
   self.obj1691.Specify=ATOM3Constraint()
   self.obj1691.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()\n'))
   self.obj169.GGset2Any['Name']= self.obj1691
   self.obj1692= AttrCalc()
   self.obj1692.Copy=ATOM3Boolean()
   self.obj1692.Copy.setValue(('Copy from LHS', 1))
   self.obj1692.Copy.config = 0
   self.obj1692.Specify=ATOM3Constraint()
   self.obj1692.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj169.GGset2Any['ReqFlow']= self.obj1692

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj169)
   self.obj169.postAction( cobj0.RHS.CREATE )

   self.obj170=Goal(self)
   self.obj170.preAction( cobj0.RHS.CREATE )
   self.obj170.isGraphObjectVisual = True

   if(hasattr(self.obj170, '_setHierarchicalLink')):
     self.obj170._setHierarchicalLink(False)

   # name
   self.obj170.name.setValue('')
   self.obj170.name.setNone()

   self.obj170.GGLabel.setValue(1)
   self.obj170.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(80.0,80.0,self.obj170)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj170.graphObject_ = new_obj
   self.obj1700= AttrCalc()
   self.obj1700.Copy=ATOM3Boolean()
   self.obj1700.Copy.setValue(('Copy from LHS', 1))
   self.obj1700.Copy.config = 0
   self.obj1700.Specify=ATOM3Constraint()
   self.obj1700.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj170.GGset2Any['name']= self.obj1700

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj170)
   self.obj170.postAction( cobj0.RHS.CREATE )

   self.obj171=GenericGraphEdge(self)
   self.obj171.preAction( cobj0.RHS.CREATE )
   self.obj171.isGraphObjectVisual = True

   if(hasattr(self.obj171, '_setHierarchicalLink')):
     self.obj171._setHierarchicalLink(False)

   self.obj171.GGLabel.setValue(4)
   self.obj171.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(209.5,91.5,self.obj171)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj171.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj171)
   self.obj171.postAction( cobj0.RHS.CREATE )

   self.obj170.out_connections_.append(self.obj171)
   self.obj171.in_connections_.append(self.obj170)
   self.obj170.graphObject_.pendingConnections.append((self.obj170.graphObject_.tag, self.obj171.graphObject_.tag, [113.0, 81.0, 209.5, 91.5], 0, True))
   self.obj171.out_connections_.append(self.obj169)
   self.obj169.in_connections_.append(self.obj171)
   self.obj171.graphObject_.pendingConnections.append((self.obj171.graphObject_.tag, self.obj169.graphObject_.tag, [306.0, 102.0, 209.5, 91.5], 0, True))

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

   self.obj178=rawMaterial(self)
   self.obj178.preAction( cobj0.LHS.CREATE )
   self.obj178.isGraphObjectVisual = True

   if(hasattr(self.obj178, '_setHierarchicalLink')):
     self.obj178._setHierarchicalLink(False)

   # MaxFlow
   self.obj178.MaxFlow.setValue(999999)

   # price
   self.obj178.price.setValue(0)

   # Name
   self.obj178.Name.setValue('')
   self.obj178.Name.setNone()

   # ReqFlow
   self.obj178.ReqFlow.setValue(0)

   self.obj178.GGLabel.setValue(3)
   self.obj178.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(220.0,20.0,self.obj178)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj178.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj178)
   self.obj178.postAction( cobj0.LHS.CREATE )

   self.obj179=operatingUnit(self)
   self.obj179.preAction( cobj0.LHS.CREATE )
   self.obj179.isGraphObjectVisual = True

   if(hasattr(self.obj179, '_setHierarchicalLink')):
     self.obj179._setHierarchicalLink(False)

   # OperCostProp
   self.obj179.OperCostProp.setValue(0.0)

   # name
   self.obj179.name.setValue('')
   self.obj179.name.setNone()

   # OperCostFix
   self.obj179.OperCostFix.setValue(0.0)

   self.obj179.GGLabel.setValue(2)
   self.obj179.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(260.0,160.0,self.obj179)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj179.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj179)
   self.obj179.postAction( cobj0.LHS.CREATE )

   self.obj180=Agent(self)
   self.obj180.preAction( cobj0.LHS.CREATE )
   self.obj180.isGraphObjectVisual = True

   if(hasattr(self.obj180, '_setHierarchicalLink')):
     self.obj180._setHierarchicalLink(False)

   # price
   self.obj180.price.setNone()

   # name
   self.obj180.name.setValue('')
   self.obj180.name.setNone()

   self.obj180.GGLabel.setValue(1)
   self.obj180.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(80.0,120.0,self.obj180)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj180.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj180)
   self.obj180.postAction( cobj0.LHS.CREATE )

   self.obj181=GenericGraphEdge(self)
   self.obj181.preAction( cobj0.LHS.CREATE )
   self.obj181.isGraphObjectVisual = True

   if(hasattr(self.obj181, '_setHierarchicalLink')):
     self.obj181._setHierarchicalLink(False)

   self.obj181.GGLabel.setValue(4)
   self.obj181.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(181.75,114.0,self.obj181)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj181.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj181)
   self.obj181.postAction( cobj0.LHS.CREATE )

   self.obj182=GenericGraphEdge(self)
   self.obj182.preAction( cobj0.LHS.CREATE )
   self.obj182.isGraphObjectVisual = True

   if(hasattr(self.obj182, '_setHierarchicalLink')):
     self.obj182._setHierarchicalLink(False)

   self.obj182.GGLabel.setValue(5)
   self.obj182.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(229.25,150.25,self.obj182)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj182.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj182)
   self.obj182.postAction( cobj0.LHS.CREATE )

   self.obj180.out_connections_.append(self.obj181)
   self.obj181.in_connections_.append(self.obj180)
   self.obj180.graphObject_.pendingConnections.append((self.obj180.graphObject_.tag, self.obj181.graphObject_.tag, [105.0, 182.0, 147.0, 140.5, 181.75, 114.0], 2, True))
   self.obj180.out_connections_.append(self.obj182)
   self.obj182.in_connections_.append(self.obj180)
   self.obj180.graphObject_.pendingConnections.append((self.obj180.graphObject_.tag, self.obj182.graphObject_.tag, [105.0, 182.0, 185.5, 153.0, 229.25, 150.25], 2, True))
   self.obj181.out_connections_.append(self.obj178)
   self.obj178.in_connections_.append(self.obj181)
   self.obj181.graphObject_.pendingConnections.append((self.obj181.graphObject_.tag, self.obj178.graphObject_.tag, [244.0, 76.0, 216.5, 87.5, 181.75, 114.0], 2, True))
   self.obj182.out_connections_.append(self.obj179)
   self.obj179.in_connections_.append(self.obj182)
   self.obj182.graphObject_.pendingConnections.append((self.obj182.graphObject_.tag, self.obj179.graphObject_.tag, [280.0, 171.0, 273.0, 147.5, 229.25, 150.25], 2, True))

   cobj0.RHS = ASG_pns(self)
   cobj0.RHS.merge(ASG_omacs(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj186=rawMaterial(self)
   self.obj186.preAction( cobj0.RHS.CREATE )
   self.obj186.isGraphObjectVisual = True

   if(hasattr(self.obj186, '_setHierarchicalLink')):
     self.obj186._setHierarchicalLink(False)

   # MaxFlow
   self.obj186.MaxFlow.setValue(999999)

   # price
   self.obj186.price.setValue(0)

   # Name
   self.obj186.Name.setValue('')
   self.obj186.Name.setNone()

   # ReqFlow
   self.obj186.ReqFlow.setValue(0)

   self.obj186.GGLabel.setValue(3)
   self.obj186.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(220.0,20.0,self.obj186)
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
   self.obj186.GGset2Any['MaxFlow']= self.obj1860
   self.obj1861= AttrCalc()
   self.obj1861.Copy=ATOM3Boolean()
   self.obj1861.Copy.setValue(('Copy from LHS', 1))
   self.obj1861.Copy.config = 0
   self.obj1861.Specify=ATOM3Constraint()
   self.obj1861.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj186.GGset2Any['Name']= self.obj1861
   self.obj1862= AttrCalc()
   self.obj1862.Copy=ATOM3Boolean()
   self.obj1862.Copy.setValue(('Copy from LHS', 1))
   self.obj1862.Copy.config = 0
   self.obj1862.Specify=ATOM3Constraint()
   self.obj1862.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj186.GGset2Any['ReqFlow']= self.obj1862

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj186)
   self.obj186.postAction( cobj0.RHS.CREATE )

   self.obj187=operatingUnit(self)
   self.obj187.preAction( cobj0.RHS.CREATE )
   self.obj187.isGraphObjectVisual = True

   if(hasattr(self.obj187, '_setHierarchicalLink')):
     self.obj187._setHierarchicalLink(False)

   # OperCostProp
   self.obj187.OperCostProp.setValue(0.0)

   # name
   self.obj187.name.setValue('')
   self.obj187.name.setNone()

   # OperCostFix
   self.obj187.OperCostFix.setValue(0.0)

   self.obj187.GGLabel.setValue(2)
   self.obj187.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(260.0,160.0,self.obj187)
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
   self.obj187.GGset2Any['OperCostProp']= self.obj1870
   self.obj1871= AttrCalc()
   self.obj1871.Copy=ATOM3Boolean()
   self.obj1871.Copy.setValue(('Copy from LHS', 1))
   self.obj1871.Copy.config = 0
   self.obj1871.Specify=ATOM3Constraint()
   self.obj1871.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj187.GGset2Any['name']= self.obj1871
   self.obj1872= AttrCalc()
   self.obj1872.Copy=ATOM3Boolean()
   self.obj1872.Copy.setValue(('Copy from LHS', 1))
   self.obj1872.Copy.config = 0
   self.obj1872.Specify=ATOM3Constraint()
   self.obj1872.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj187.GGset2Any['OperCostFix']= self.obj1872

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj187)
   self.obj187.postAction( cobj0.RHS.CREATE )

   self.obj188=fromRaw(self)
   self.obj188.preAction( cobj0.RHS.CREATE )
   self.obj188.isGraphObjectVisual = True

   if(hasattr(self.obj188, '_setHierarchicalLink')):
     self.obj188._setHierarchicalLink(False)

   # rate
   self.obj188.rate.setValue(1.0)

   self.obj188.GGLabel.setValue(7)
   self.obj188.graphClass_= graph_fromRaw
   if self.genGraphics:
      new_obj = graph_fromRaw(262.0,115.5,self.obj188)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj188.graphObject_ = new_obj
   self.obj1880= AttrCalc()
   self.obj1880.Copy=ATOM3Boolean()
   self.obj1880.Copy.setValue(('Copy from LHS', 0))
   self.obj1880.Copy.config = 0
   self.obj1880.Specify=ATOM3Constraint()
   self.obj1880.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj188.GGset2Any['rate']= self.obj1880

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj188)
   self.obj188.postAction( cobj0.RHS.CREATE )

   self.obj189=Agent(self)
   self.obj189.preAction( cobj0.RHS.CREATE )
   self.obj189.isGraphObjectVisual = True

   if(hasattr(self.obj189, '_setHierarchicalLink')):
     self.obj189._setHierarchicalLink(False)

   # price
   self.obj189.price.setNone()

   # name
   self.obj189.name.setValue('')
   self.obj189.name.setNone()

   self.obj189.GGLabel.setValue(1)
   self.obj189.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(80.0,120.0,self.obj189)
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
   self.obj189.GGset2Any['price']= self.obj1890
   self.obj1891= AttrCalc()
   self.obj1891.Copy=ATOM3Boolean()
   self.obj1891.Copy.setValue(('Copy from LHS', 1))
   self.obj1891.Copy.config = 0
   self.obj1891.Specify=ATOM3Constraint()
   self.obj1891.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj189.GGset2Any['name']= self.obj1891

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj189)
   self.obj189.postAction( cobj0.RHS.CREATE )

   self.obj190=GenericGraphEdge(self)
   self.obj190.preAction( cobj0.RHS.CREATE )
   self.obj190.isGraphObjectVisual = True

   if(hasattr(self.obj190, '_setHierarchicalLink')):
     self.obj190._setHierarchicalLink(False)

   self.obj190.GGLabel.setValue(4)
   self.obj190.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(181.75,114.0,self.obj190)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj190.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj190)
   self.obj190.postAction( cobj0.RHS.CREATE )

   self.obj191=GenericGraphEdge(self)
   self.obj191.preAction( cobj0.RHS.CREATE )
   self.obj191.isGraphObjectVisual = True

   if(hasattr(self.obj191, '_setHierarchicalLink')):
     self.obj191._setHierarchicalLink(False)

   self.obj191.GGLabel.setValue(5)
   self.obj191.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(229.25,150.25,self.obj191)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj191.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj191)
   self.obj191.postAction( cobj0.RHS.CREATE )

   self.obj186.out_connections_.append(self.obj188)
   self.obj188.in_connections_.append(self.obj186)
   self.obj186.graphObject_.pendingConnections.append((self.obj186.graphObject_.tag, self.obj188.graphObject_.tag, [244.0, 70.0, 262.0, 115.5], 0, True))
   self.obj188.out_connections_.append(self.obj187)
   self.obj187.in_connections_.append(self.obj188)
   self.obj188.graphObject_.pendingConnections.append((self.obj188.graphObject_.tag, self.obj187.graphObject_.tag, [280.0, 161.0, 262.0, 115.5], 0, True))
   self.obj189.out_connections_.append(self.obj190)
   self.obj190.in_connections_.append(self.obj189)
   self.obj189.graphObject_.pendingConnections.append((self.obj189.graphObject_.tag, self.obj190.graphObject_.tag, [117.0, 182.0, 181.75, 114.0], 2, 0))
   self.obj189.out_connections_.append(self.obj191)
   self.obj191.in_connections_.append(self.obj189)
   self.obj189.graphObject_.pendingConnections.append((self.obj189.graphObject_.tag, self.obj191.graphObject_.tag, [117.0, 182.0, 229.25, 150.25], 2, 0))
   self.obj190.out_connections_.append(self.obj186)
   self.obj186.in_connections_.append(self.obj190)
   self.obj190.graphObject_.pendingConnections.append((self.obj190.graphObject_.tag, self.obj186.graphObject_.tag, [244.0, 70.0, 181.75, 114.0], 2, 0))
   self.obj191.out_connections_.append(self.obj187)
   self.obj187.in_connections_.append(self.obj191)
   self.obj191.graphObject_.pendingConnections.append((self.obj191.graphObject_.tag, self.obj187.graphObject_.tag, [280.0, 161.0, 229.25, 150.25], 2, 0))

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

   self.obj197=product(self)
   self.obj197.preAction( cobj0.RHS.CREATE )
   self.obj197.isGraphObjectVisual = True

   if(hasattr(self.obj197, '_setHierarchicalLink')):
     self.obj197._setHierarchicalLink(False)

   # MaxFlow
   self.obj197.MaxFlow.setValue(999999)

   # price
   self.obj197.price.setValue(0)

   # Name
   self.obj197.Name.setValue('OAF')

   # ReqFlow
   self.obj197.ReqFlow.setValue(0)

   self.obj197.GGLabel.setValue(1)
   self.obj197.graphClass_= graph_product
   if self.genGraphics:
      new_obj = graph_product(100.0,80.0,self.obj197)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj197.graphObject_ = new_obj
   self.obj1970= AttrCalc()
   self.obj1970.Copy=ATOM3Boolean()
   self.obj1970.Copy.setValue(('Copy from LHS', 1))
   self.obj1970.Copy.config = 0
   self.obj1970.Specify=ATOM3Constraint()
   self.obj1970.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj197.GGset2Any['MaxFlow']= self.obj1970
   self.obj1971= AttrCalc()
   self.obj1971.Copy=ATOM3Boolean()
   self.obj1971.Copy.setValue(('Copy from LHS', 0))
   self.obj1971.Copy.config = 0
   self.obj1971.Specify=ATOM3Constraint()
   self.obj1971.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj197.GGset2Any['Name']= self.obj1971
   self.obj1972= AttrCalc()
   self.obj1972.Copy=ATOM3Boolean()
   self.obj1972.Copy.setValue(('Copy from LHS', 1))
   self.obj1972.Copy.config = 0
   self.obj1972.Specify=ATOM3Constraint()
   self.obj1972.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj197.GGset2Any['ReqFlow']= self.obj1972

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj197)
   self.obj197.postAction( cobj0.RHS.CREATE )


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

   self.obj204=product(self)
   self.obj204.preAction( cobj0.LHS.CREATE )
   self.obj204.isGraphObjectVisual = True

   if(hasattr(self.obj204, '_setHierarchicalLink')):
     self.obj204._setHierarchicalLink(False)

   # MaxFlow
   self.obj204.MaxFlow.setNone()

   # price
   self.obj204.price.setValue(0)

   # Name
   self.obj204.Name.setValue('')
   self.obj204.Name.setNone()

   # ReqFlow
   self.obj204.ReqFlow.setNone()

   self.obj204.GGLabel.setValue(5)
   self.obj204.graphClass_= graph_product
   if self.genGraphics:
      new_obj = graph_product(280.0,220.0,self.obj204)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj204.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj204)
   self.obj204.postAction( cobj0.LHS.CREATE )

   self.obj205=metarial(self)
   self.obj205.preAction( cobj0.LHS.CREATE )
   self.obj205.isGraphObjectVisual = True

   if(hasattr(self.obj205, '_setHierarchicalLink')):
     self.obj205._setHierarchicalLink(False)

   # MaxFlow
   self.obj205.MaxFlow.setNone()

   # price
   self.obj205.price.setValue(0)

   # Name
   self.obj205.Name.setValue('')
   self.obj205.Name.setNone()

   # ReqFlow
   self.obj205.ReqFlow.setNone()

   self.obj205.GGLabel.setValue(3)
   self.obj205.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(320.0,40.0,self.obj205)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj205.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj205)
   self.obj205.postAction( cobj0.LHS.CREATE )

   self.obj206=Goal(self)
   self.obj206.preAction( cobj0.LHS.CREATE )
   self.obj206.isGraphObjectVisual = True

   if(hasattr(self.obj206, '_setHierarchicalLink')):
     self.obj206._setHierarchicalLink(False)

   # name
   self.obj206.name.setValue('')
   self.obj206.name.setNone()

   self.obj206.GGLabel.setValue(2)
   self.obj206.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(180.0,60.0,self.obj206)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj206.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj206)
   self.obj206.postAction( cobj0.LHS.CREATE )

   self.obj207=GenericGraphEdge(self)
   self.obj207.preAction( cobj0.LHS.CREATE )
   self.obj207.isGraphObjectVisual = True

   if(hasattr(self.obj207, '_setHierarchicalLink')):
     self.obj207._setHierarchicalLink(False)

   self.obj207.GGLabel.setValue(4)
   self.obj207.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(264.5,71.5,self.obj207)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj207.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj207)
   self.obj207.postAction( cobj0.LHS.CREATE )

   self.obj206.out_connections_.append(self.obj207)
   self.obj207.in_connections_.append(self.obj206)
   self.obj206.graphObject_.pendingConnections.append((self.obj206.graphObject_.tag, self.obj207.graphObject_.tag, [203.0, 61.0, 264.5, 71.5], 0, True))
   self.obj207.out_connections_.append(self.obj205)
   self.obj205.in_connections_.append(self.obj207)
   self.obj207.graphObject_.pendingConnections.append((self.obj207.graphObject_.tag, self.obj205.graphObject_.tag, [326.0, 82.0, 264.5, 71.5], 0, True))

   cobj0.RHS = ASG_pns(self)
   cobj0.RHS.merge(ASG_omacs(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj211=product(self)
   self.obj211.preAction( cobj0.RHS.CREATE )
   self.obj211.isGraphObjectVisual = True

   if(hasattr(self.obj211, '_setHierarchicalLink')):
     self.obj211._setHierarchicalLink(False)

   # MaxFlow
   self.obj211.MaxFlow.setNone()

   # price
   self.obj211.price.setValue(0)

   # Name
   self.obj211.Name.setValue('')
   self.obj211.Name.setNone()

   # ReqFlow
   self.obj211.ReqFlow.setNone()

   self.obj211.GGLabel.setValue(5)
   self.obj211.graphClass_= graph_product
   if self.genGraphics:
      new_obj = graph_product(280.0,220.0,self.obj211)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj211.graphObject_ = new_obj
   self.obj2110= AttrCalc()
   self.obj2110.Copy=ATOM3Boolean()
   self.obj2110.Copy.setValue(('Copy from LHS', 1))
   self.obj2110.Copy.config = 0
   self.obj2110.Specify=ATOM3Constraint()
   self.obj2110.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj211.GGset2Any['MaxFlow']= self.obj2110
   self.obj2111= AttrCalc()
   self.obj2111.Copy=ATOM3Boolean()
   self.obj2111.Copy.setValue(('Copy from LHS', 1))
   self.obj2111.Copy.config = 0
   self.obj2111.Specify=ATOM3Constraint()
   self.obj2111.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj211.GGset2Any['Name']= self.obj2111
   self.obj2112= AttrCalc()
   self.obj2112.Copy=ATOM3Boolean()
   self.obj2112.Copy.setValue(('Copy from LHS', 1))
   self.obj2112.Copy.config = 0
   self.obj2112.Specify=ATOM3Constraint()
   self.obj2112.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj211.GGset2Any['ReqFlow']= self.obj2112

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj211)
   self.obj211.postAction( cobj0.RHS.CREATE )

   self.obj212=metarial(self)
   self.obj212.preAction( cobj0.RHS.CREATE )
   self.obj212.isGraphObjectVisual = True

   if(hasattr(self.obj212, '_setHierarchicalLink')):
     self.obj212._setHierarchicalLink(False)

   # MaxFlow
   self.obj212.MaxFlow.setNone()

   # price
   self.obj212.price.setValue(0)

   # Name
   self.obj212.Name.setValue('')
   self.obj212.Name.setNone()

   # ReqFlow
   self.obj212.ReqFlow.setNone()

   self.obj212.GGLabel.setValue(3)
   self.obj212.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(320.0,40.0,self.obj212)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj212.graphObject_ = new_obj
   self.obj2120= AttrCalc()
   self.obj2120.Copy=ATOM3Boolean()
   self.obj2120.Copy.setValue(('Copy from LHS', 1))
   self.obj2120.Copy.config = 0
   self.obj2120.Specify=ATOM3Constraint()
   self.obj2120.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj212.GGset2Any['MaxFlow']= self.obj2120
   self.obj2121= AttrCalc()
   self.obj2121.Copy=ATOM3Boolean()
   self.obj2121.Copy.setValue(('Copy from LHS', 1))
   self.obj2121.Copy.config = 0
   self.obj2121.Specify=ATOM3Constraint()
   self.obj2121.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj212.GGset2Any['Name']= self.obj2121
   self.obj2122= AttrCalc()
   self.obj2122.Copy=ATOM3Boolean()
   self.obj2122.Copy.setValue(('Copy from LHS', 1))
   self.obj2122.Copy.config = 0
   self.obj2122.Specify=ATOM3Constraint()
   self.obj2122.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj212.GGset2Any['ReqFlow']= self.obj2122

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj212)
   self.obj212.postAction( cobj0.RHS.CREATE )

   self.obj213=operatingUnit(self)
   self.obj213.preAction( cobj0.RHS.CREATE )
   self.obj213.isGraphObjectVisual = True

   if(hasattr(self.obj213, '_setHierarchicalLink')):
     self.obj213._setHierarchicalLink(False)

   # OperCostProp
   self.obj213.OperCostProp.setValue(1.0)

   # name
   self.obj213.name.setValue('')
   self.obj213.name.setNone()

   # OperCostFix
   self.obj213.OperCostFix.setValue(2.0)

   self.obj213.GGLabel.setValue(7)
   self.obj213.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(320.0,140.0,self.obj213)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj213.graphObject_ = new_obj
   self.obj2130= AttrCalc()
   self.obj2130.Copy=ATOM3Boolean()
   self.obj2130.Copy.setValue(('Copy from LHS', 0))
   self.obj2130.Copy.config = 0
   self.obj2130.Specify=ATOM3Constraint()
   self.obj2130.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj213.GGset2Any['OperCostProp']= self.obj2130
   self.obj2131= AttrCalc()
   self.obj2131.Copy=ATOM3Boolean()
   self.obj2131.Copy.setValue(('Copy from LHS', 0))
   self.obj2131.Copy.config = 0
   self.obj2131.Specify=ATOM3Constraint()
   self.obj2131.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(2)).name.getValue()+\' OAF\'\n'))
   self.obj213.GGset2Any['name']= self.obj2131
   self.obj2132= AttrCalc()
   self.obj2132.Copy=ATOM3Boolean()
   self.obj2132.Copy.setValue(('Copy from LHS', 0))
   self.obj2132.Copy.config = 0
   self.obj2132.Specify=ATOM3Constraint()
   self.obj2132.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj213.GGset2Any['OperCostFix']= self.obj2132

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj213)
   self.obj213.postAction( cobj0.RHS.CREATE )

   self.obj214=intoProduct(self)
   self.obj214.preAction( cobj0.RHS.CREATE )
   self.obj214.isGraphObjectVisual = True

   if(hasattr(self.obj214, '_setHierarchicalLink')):
     self.obj214._setHierarchicalLink(False)

   # rate
   self.obj214.rate.setValue(1.0)

   self.obj214.GGLabel.setValue(9)
   self.obj214.graphClass_= graph_intoProduct
   if self.genGraphics:
      new_obj = graph_intoProduct(322.0,179.0,self.obj214)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj214.graphObject_ = new_obj
   self.obj2140= AttrCalc()
   self.obj2140.Copy=ATOM3Boolean()
   self.obj2140.Copy.setValue(('Copy from LHS', 0))
   self.obj2140.Copy.config = 0
   self.obj2140.Specify=ATOM3Constraint()
   self.obj2140.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj214.GGset2Any['rate']= self.obj2140

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj214)
   self.obj214.postAction( cobj0.RHS.CREATE )

   self.obj215=fromMaterial(self)
   self.obj215.preAction( cobj0.RHS.CREATE )
   self.obj215.isGraphObjectVisual = True

   if(hasattr(self.obj215, '_setHierarchicalLink')):
     self.obj215._setHierarchicalLink(False)

   # rate
   self.obj215.rate.setValue(1.0)

   self.obj215.GGLabel.setValue(8)
   self.obj215.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(342.0,110.0,self.obj215)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj215.graphObject_ = new_obj
   self.obj2150= AttrCalc()
   self.obj2150.Copy=ATOM3Boolean()
   self.obj2150.Copy.setValue(('Copy from LHS', 0))
   self.obj2150.Copy.config = 0
   self.obj2150.Specify=ATOM3Constraint()
   self.obj2150.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj215.GGset2Any['rate']= self.obj2150

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj215)
   self.obj215.postAction( cobj0.RHS.CREATE )

   self.obj216=Goal(self)
   self.obj216.preAction( cobj0.RHS.CREATE )
   self.obj216.isGraphObjectVisual = True

   if(hasattr(self.obj216, '_setHierarchicalLink')):
     self.obj216._setHierarchicalLink(False)

   # name
   self.obj216.name.setValue('')
   self.obj216.name.setNone()

   self.obj216.GGLabel.setValue(2)
   self.obj216.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(180.0,60.0,self.obj216)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj216.graphObject_ = new_obj
   self.obj2160= AttrCalc()
   self.obj2160.Copy=ATOM3Boolean()
   self.obj2160.Copy.setValue(('Copy from LHS', 1))
   self.obj2160.Copy.config = 0
   self.obj2160.Specify=ATOM3Constraint()
   self.obj2160.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj216.GGset2Any['name']= self.obj2160

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj216)
   self.obj216.postAction( cobj0.RHS.CREATE )

   self.obj217=GenericGraphEdge(self)
   self.obj217.preAction( cobj0.RHS.CREATE )
   self.obj217.isGraphObjectVisual = True

   if(hasattr(self.obj217, '_setHierarchicalLink')):
     self.obj217._setHierarchicalLink(False)

   self.obj217.GGLabel.setValue(4)
   self.obj217.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(264.5,71.5,self.obj217)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj217.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj217)
   self.obj217.postAction( cobj0.RHS.CREATE )

   self.obj212.out_connections_.append(self.obj215)
   self.obj215.in_connections_.append(self.obj212)
   self.obj212.graphObject_.pendingConnections.append((self.obj212.graphObject_.tag, self.obj215.graphObject_.tag, [244.0, 89.0, 342.0, 110.0], 0, True))
   self.obj213.out_connections_.append(self.obj214)
   self.obj214.in_connections_.append(self.obj213)
   self.obj213.graphObject_.pendingConnections.append((self.obj213.graphObject_.tag, self.obj214.graphObject_.tag, [339.0, 158.0, 322.0, 179.0], 0, True))
   self.obj214.out_connections_.append(self.obj211)
   self.obj211.in_connections_.append(self.obj214)
   self.obj214.graphObject_.pendingConnections.append((self.obj214.graphObject_.tag, self.obj211.graphObject_.tag, [305.0, 220.0, 322.0, 179.0], 0, True))
   self.obj215.out_connections_.append(self.obj213)
   self.obj213.in_connections_.append(self.obj215)
   self.obj215.graphObject_.pendingConnections.append((self.obj215.graphObject_.tag, self.obj213.graphObject_.tag, [340.0, 151.0, 342.0, 110.0], 0, True))
   self.obj216.out_connections_.append(self.obj217)
   self.obj217.in_connections_.append(self.obj216)
   self.obj216.graphObject_.pendingConnections.append((self.obj216.graphObject_.tag, self.obj217.graphObject_.tag, [93.0, 61.0, 264.5, 71.5], 2, 0))
   self.obj217.out_connections_.append(self.obj212)
   self.obj212.in_connections_.append(self.obj217)
   self.obj217.graphObject_.pendingConnections.append((self.obj217.graphObject_.tag, self.obj212.graphObject_.tag, [226.0, 82.0, 264.5, 71.5], 2, 0))

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

   self.obj223=CapableOf(self)
   self.obj223.preAction( cobj0.LHS.CREATE )
   self.obj223.isGraphObjectVisual = True

   if(hasattr(self.obj223, '_setHierarchicalLink')):
     self.obj223._setHierarchicalLink(False)

   # rate
   self.obj223.rate.setNone()

   self.obj223.GGLabel.setValue(4)
   self.obj223.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(250.75,110.75,self.obj223)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj223.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj223)
   self.obj223.postAction( cobj0.LHS.CREATE )

   self.obj224=Goal(self)
   self.obj224.preAction( cobj0.LHS.CREATE )
   self.obj224.isGraphObjectVisual = True

   if(hasattr(self.obj224, '_setHierarchicalLink')):
     self.obj224._setHierarchicalLink(False)

   # name
   self.obj224.name.setValue('')
   self.obj224.name.setNone()

   self.obj224.GGLabel.setValue(3)
   self.obj224.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(100.0,240.0,self.obj224)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj224.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj224)
   self.obj224.postAction( cobj0.LHS.CREATE )

   self.obj225=Agent(self)
   self.obj225.preAction( cobj0.LHS.CREATE )
   self.obj225.isGraphObjectVisual = True

   if(hasattr(self.obj225, '_setHierarchicalLink')):
     self.obj225._setHierarchicalLink(False)

   # price
   self.obj225.price.setNone()

   # name
   self.obj225.name.setValue('')
   self.obj225.name.setNone()

   self.obj225.GGLabel.setValue(1)
   self.obj225.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(80.0,40.0,self.obj225)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj225.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj225)
   self.obj225.postAction( cobj0.LHS.CREATE )

   self.obj226=Role(self)
   self.obj226.preAction( cobj0.LHS.CREATE )
   self.obj226.isGraphObjectVisual = True

   if(hasattr(self.obj226, '_setHierarchicalLink')):
     self.obj226._setHierarchicalLink(False)

   # name
   self.obj226.name.setValue('')
   self.obj226.name.setNone()

   self.obj226.GGLabel.setValue(2)
   self.obj226.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(280.0,140.0,self.obj226)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj226.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj226)
   self.obj226.postAction( cobj0.LHS.CREATE )

   self.obj227=achieve(self)
   self.obj227.preAction( cobj0.LHS.CREATE )
   self.obj227.isGraphObjectVisual = True

   if(hasattr(self.obj227, '_setHierarchicalLink')):
     self.obj227._setHierarchicalLink(False)

   # rate
   self.obj227.rate.setNone()

   self.obj227.GGLabel.setValue(5)
   self.obj227.graphClass_= graph_achieve
   if self.genGraphics:
      new_obj = graph_achieve(258.5,259.0,self.obj227)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj227.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj227)
   self.obj227.postAction( cobj0.LHS.CREATE )

   self.obj223.out_connections_.append(self.obj226)
   self.obj226.in_connections_.append(self.obj223)
   self.obj223.graphObject_.pendingConnections.append((self.obj223.graphObject_.tag, self.obj226.graphObject_.tag, [304.0, 141.0, 300.5, 120.5, 250.75, 110.75], 2, True))
   self.obj225.out_connections_.append(self.obj223)
   self.obj223.in_connections_.append(self.obj225)
   self.obj225.graphObject_.pendingConnections.append((self.obj225.graphObject_.tag, self.obj223.graphObject_.tag, [105.0, 102.0, 201.0, 101.0, 250.75, 110.75], 2, True))
   self.obj226.out_connections_.append(self.obj227)
   self.obj227.in_connections_.append(self.obj226)
   self.obj226.graphObject_.pendingConnections.append((self.obj226.graphObject_.tag, self.obj227.graphObject_.tag, [304.0, 186.0, 303.5, 233.0, 258.5, 259.0], 2, True))
   self.obj227.out_connections_.append(self.obj224)
   self.obj224.in_connections_.append(self.obj227)
   self.obj227.graphObject_.pendingConnections.append((self.obj227.graphObject_.tag, self.obj224.graphObject_.tag, [124.0, 290.0, 213.5, 285.0, 258.5, 259.0], 2, True))

   cobj0.RHS = ASG_pns(self)
   cobj0.RHS.merge(ASG_omacs(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj231=metarial(self)
   self.obj231.preAction( cobj0.RHS.CREATE )
   self.obj231.isGraphObjectVisual = True

   if(hasattr(self.obj231, '_setHierarchicalLink')):
     self.obj231._setHierarchicalLink(False)

   # MaxFlow
   self.obj231.MaxFlow.setValue(999999)

   # price
   self.obj231.price.setValue(0)

   # Name
   self.obj231.Name.setValue('')
   self.obj231.Name.setNone()

   # ReqFlow
   self.obj231.ReqFlow.setValue(0)

   self.obj231.GGLabel.setValue(8)
   self.obj231.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(400.0,80.0,self.obj231)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj231.graphObject_ = new_obj
   self.obj2310= AttrCalc()
   self.obj2310.Copy=ATOM3Boolean()
   self.obj2310.Copy.setValue(('Copy from LHS', 1))
   self.obj2310.Copy.config = 0
   self.obj2310.Specify=ATOM3Constraint()
   self.obj2310.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj231.GGset2Any['MaxFlow']= self.obj2310
   self.obj2311= AttrCalc()
   self.obj2311.Copy=ATOM3Boolean()
   self.obj2311.Copy.setValue(('Copy from LHS', 0))
   self.obj2311.Copy.config = 0
   self.obj2311.Specify=ATOM3Constraint()
   self.obj2311.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()+\' \'+ self.getMatched(graphID, self.LHS.nodeWithLabel(2)).name.getValue()+\' \'+ self.getMatched(graphID, self.LHS.nodeWithLabel(3)).name.getValue()\n\n'))
   self.obj231.GGset2Any['Name']= self.obj2311
   self.obj2312= AttrCalc()
   self.obj2312.Copy=ATOM3Boolean()
   self.obj2312.Copy.setValue(('Copy from LHS', 1))
   self.obj2312.Copy.config = 0
   self.obj2312.Specify=ATOM3Constraint()
   self.obj2312.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj231.GGset2Any['ReqFlow']= self.obj2312

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj231)
   self.obj231.postAction( cobj0.RHS.CREATE )

   self.obj232=operatingUnit(self)
   self.obj232.preAction( cobj0.RHS.CREATE )
   self.obj232.isGraphObjectVisual = True

   if(hasattr(self.obj232, '_setHierarchicalLink')):
     self.obj232._setHierarchicalLink(False)

   # OperCostProp
   self.obj232.OperCostProp.setValue(0.0)

   # name
   self.obj232.name.setValue('')
   self.obj232.name.setNone()

   # OperCostFix
   self.obj232.OperCostFix.setValue(0.0)

   self.obj232.GGLabel.setValue(7)
   self.obj232.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(400.0,240.0,self.obj232)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj232.graphObject_ = new_obj
   self.obj2320= AttrCalc()
   self.obj2320.Copy=ATOM3Boolean()
   self.obj2320.Copy.setValue(('Copy from LHS', 0))
   self.obj2320.Copy.config = 0
   self.obj2320.Specify=ATOM3Constraint()
   self.obj2320.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(5)).rate.getValue()\n'))
   self.obj232.GGset2Any['OperCostProp']= self.obj2320
   self.obj2321= AttrCalc()
   self.obj2321.Copy=ATOM3Boolean()
   self.obj2321.Copy.setValue(('Copy from LHS', 0))
   self.obj2321.Copy.config = 0
   self.obj2321.Specify=ATOM3Constraint()
   self.obj2321.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()+\' \'+ self.getMatched(graphID, self.LHS.nodeWithLabel(2)).name.getValue()+\' \'+ self.getMatched(graphID, self.LHS.nodeWithLabel(3)).name.getValue()\n\n\n\n\n\n\n'))
   self.obj232.GGset2Any['name']= self.obj2321
   self.obj2322= AttrCalc()
   self.obj2322.Copy=ATOM3Boolean()
   self.obj2322.Copy.setValue(('Copy from LHS', 0))
   self.obj2322.Copy.config = 0
   self.obj2322.Specify=ATOM3Constraint()
   self.obj2322.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return 2.0\n'))
   self.obj232.GGset2Any['OperCostFix']= self.obj2322

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj232)
   self.obj232.postAction( cobj0.RHS.CREATE )

   self.obj233=fromMaterial(self)
   self.obj233.preAction( cobj0.RHS.CREATE )
   self.obj233.isGraphObjectVisual = True

   if(hasattr(self.obj233, '_setHierarchicalLink')):
     self.obj233._setHierarchicalLink(False)

   # rate
   self.obj233.rate.setValue(1.0)

   self.obj233.GGLabel.setValue(9)
   self.obj233.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(422.0,190.0,self.obj233)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj233.graphObject_ = new_obj
   self.obj2330= AttrCalc()
   self.obj2330.Copy=ATOM3Boolean()
   self.obj2330.Copy.setValue(('Copy from LHS', 0))
   self.obj2330.Copy.config = 0
   self.obj2330.Specify=ATOM3Constraint()
   self.obj2330.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj233.GGset2Any['rate']= self.obj2330

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj233)
   self.obj233.postAction( cobj0.RHS.CREATE )

   self.obj234=CapableOf(self)
   self.obj234.preAction( cobj0.RHS.CREATE )
   self.obj234.isGraphObjectVisual = True

   if(hasattr(self.obj234, '_setHierarchicalLink')):
     self.obj234._setHierarchicalLink(False)

   # rate
   self.obj234.rate.setNone()

   self.obj234.GGLabel.setValue(4)
   self.obj234.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(250.75,110.75,self.obj234)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj234.graphObject_ = new_obj
   self.obj2340= AttrCalc()
   self.obj2340.Copy=ATOM3Boolean()
   self.obj2340.Copy.setValue(('Copy from LHS', 1))
   self.obj2340.Copy.config = 0
   self.obj2340.Specify=ATOM3Constraint()
   self.obj2340.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj234.GGset2Any['rate']= self.obj2340

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj234)
   self.obj234.postAction( cobj0.RHS.CREATE )

   self.obj235=Goal(self)
   self.obj235.preAction( cobj0.RHS.CREATE )
   self.obj235.isGraphObjectVisual = True

   if(hasattr(self.obj235, '_setHierarchicalLink')):
     self.obj235._setHierarchicalLink(False)

   # name
   self.obj235.name.setValue('')
   self.obj235.name.setNone()

   self.obj235.GGLabel.setValue(3)
   self.obj235.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(100.0,240.0,self.obj235)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj235.graphObject_ = new_obj
   self.obj2350= AttrCalc()
   self.obj2350.Copy=ATOM3Boolean()
   self.obj2350.Copy.setValue(('Copy from LHS', 1))
   self.obj2350.Copy.config = 0
   self.obj2350.Specify=ATOM3Constraint()
   self.obj2350.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj235.GGset2Any['name']= self.obj2350

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj235)
   self.obj235.postAction( cobj0.RHS.CREATE )

   self.obj236=Agent(self)
   self.obj236.preAction( cobj0.RHS.CREATE )
   self.obj236.isGraphObjectVisual = True

   if(hasattr(self.obj236, '_setHierarchicalLink')):
     self.obj236._setHierarchicalLink(False)

   # price
   self.obj236.price.setNone()

   # name
   self.obj236.name.setValue('')
   self.obj236.name.setNone()

   self.obj236.GGLabel.setValue(1)
   self.obj236.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(80.0,40.0,self.obj236)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj236.graphObject_ = new_obj
   self.obj2360= AttrCalc()
   self.obj2360.Copy=ATOM3Boolean()
   self.obj2360.Copy.setValue(('Copy from LHS', 1))
   self.obj2360.Copy.config = 0
   self.obj2360.Specify=ATOM3Constraint()
   self.obj2360.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj236.GGset2Any['price']= self.obj2360
   self.obj2361= AttrCalc()
   self.obj2361.Copy=ATOM3Boolean()
   self.obj2361.Copy.setValue(('Copy from LHS', 1))
   self.obj2361.Copy.config = 0
   self.obj2361.Specify=ATOM3Constraint()
   self.obj2361.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj236.GGset2Any['name']= self.obj2361

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj236)
   self.obj236.postAction( cobj0.RHS.CREATE )

   self.obj237=Role(self)
   self.obj237.preAction( cobj0.RHS.CREATE )
   self.obj237.isGraphObjectVisual = True

   if(hasattr(self.obj237, '_setHierarchicalLink')):
     self.obj237._setHierarchicalLink(False)

   # name
   self.obj237.name.setValue('')
   self.obj237.name.setNone()

   self.obj237.GGLabel.setValue(2)
   self.obj237.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(280.0,140.0,self.obj237)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj237.graphObject_ = new_obj
   self.obj2370= AttrCalc()
   self.obj2370.Copy=ATOM3Boolean()
   self.obj2370.Copy.setValue(('Copy from LHS', 1))
   self.obj2370.Copy.config = 0
   self.obj2370.Specify=ATOM3Constraint()
   self.obj2370.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj237.GGset2Any['name']= self.obj2370

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj237)
   self.obj237.postAction( cobj0.RHS.CREATE )

   self.obj238=achieve(self)
   self.obj238.preAction( cobj0.RHS.CREATE )
   self.obj238.isGraphObjectVisual = True

   if(hasattr(self.obj238, '_setHierarchicalLink')):
     self.obj238._setHierarchicalLink(False)

   # rate
   self.obj238.rate.setNone()

   self.obj238.GGLabel.setValue(5)
   self.obj238.graphClass_= graph_achieve
   if self.genGraphics:
      new_obj = graph_achieve(258.5,259.0,self.obj238)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj238.graphObject_ = new_obj
   self.obj2380= AttrCalc()
   self.obj2380.Copy=ATOM3Boolean()
   self.obj2380.Copy.setValue(('Copy from LHS', 1))
   self.obj2380.Copy.config = 0
   self.obj2380.Specify=ATOM3Constraint()
   self.obj2380.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj238.GGset2Any['rate']= self.obj2380

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj238)
   self.obj238.postAction( cobj0.RHS.CREATE )

   self.obj239=GenericGraphEdge(self)
   self.obj239.preAction( cobj0.RHS.CREATE )
   self.obj239.isGraphObjectVisual = True

   if(hasattr(self.obj239, '_setHierarchicalLink')):
     self.obj239._setHierarchicalLink(False)

   self.obj239.GGLabel.setValue(10)
   self.obj239.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(358.5,131.0,self.obj239)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj239.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj239)
   self.obj239.postAction( cobj0.RHS.CREATE )

   self.obj231.out_connections_.append(self.obj233)
   self.obj233.in_connections_.append(self.obj231)
   self.obj231.graphObject_.pendingConnections.append((self.obj231.graphObject_.tag, self.obj233.graphObject_.tag, [424.0, 129.0, 422.0, 190.0], 0, True))
   self.obj233.out_connections_.append(self.obj232)
   self.obj232.in_connections_.append(self.obj233)
   self.obj233.graphObject_.pendingConnections.append((self.obj233.graphObject_.tag, self.obj232.graphObject_.tag, [420.0, 251.0, 422.0, 190.0], 0, True))
   self.obj234.out_connections_.append(self.obj237)
   self.obj237.in_connections_.append(self.obj234)
   self.obj234.graphObject_.pendingConnections.append((self.obj234.graphObject_.tag, self.obj237.graphObject_.tag, [311.0, 140.0, 250.75, 110.75], 2, 0))
   self.obj236.out_connections_.append(self.obj234)
   self.obj234.in_connections_.append(self.obj236)
   self.obj236.graphObject_.pendingConnections.append((self.obj236.graphObject_.tag, self.obj234.graphObject_.tag, [117.0, 102.0, 250.75, 110.75], 2, 0))
   self.obj237.out_connections_.append(self.obj238)
   self.obj238.in_connections_.append(self.obj237)
   self.obj237.graphObject_.pendingConnections.append((self.obj237.graphObject_.tag, self.obj238.graphObject_.tag, [311.0, 185.0, 258.5, 259.0], 2, 0))
   self.obj237.out_connections_.append(self.obj239)
   self.obj239.in_connections_.append(self.obj237)
   self.obj237.graphObject_.pendingConnections.append((self.obj237.graphObject_.tag, self.obj239.graphObject_.tag, [311.0, 140.0, 358.5, 131.0], 0, True))
   self.obj238.out_connections_.append(self.obj235)
   self.obj235.in_connections_.append(self.obj238)
   self.obj238.graphObject_.pendingConnections.append((self.obj238.graphObject_.tag, self.obj235.graphObject_.tag, [134.0, 290.0, 258.5, 259.0], 2, 0))
   self.obj239.out_connections_.append(self.obj231)
   self.obj231.in_connections_.append(self.obj239)
   self.obj239.graphObject_.pendingConnections.append((self.obj239.graphObject_.tag, self.obj231.graphObject_.tag, [406.0, 122.0, 358.5, 131.0], 0, True))

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

   self.obj246=metarial(self)
   self.obj246.preAction( cobj0.LHS.CREATE )
   self.obj246.isGraphObjectVisual = True

   if(hasattr(self.obj246, '_setHierarchicalLink')):
     self.obj246._setHierarchicalLink(False)

   # MaxFlow
   self.obj246.MaxFlow.setNone()

   # price
   self.obj246.price.setValue(0)

   # Name
   self.obj246.Name.setValue('')
   self.obj246.Name.setNone()

   # ReqFlow
   self.obj246.ReqFlow.setNone()

   self.obj246.GGLabel.setValue(4)
   self.obj246.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(240.0,20.0,self.obj246)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj246.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj246)
   self.obj246.postAction( cobj0.LHS.CREATE )

   self.obj247=metarial(self)
   self.obj247.preAction( cobj0.LHS.CREATE )
   self.obj247.isGraphObjectVisual = True

   if(hasattr(self.obj247, '_setHierarchicalLink')):
     self.obj247._setHierarchicalLink(False)

   # MaxFlow
   self.obj247.MaxFlow.setNone()

   # price
   self.obj247.price.setValue(0)

   # Name
   self.obj247.Name.setValue('')
   self.obj247.Name.setNone()

   # ReqFlow
   self.obj247.ReqFlow.setNone()

   self.obj247.GGLabel.setValue(6)
   self.obj247.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(240.0,240.0,self.obj247)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj247.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj247)
   self.obj247.postAction( cobj0.LHS.CREATE )

   self.obj248=operatingUnit(self)
   self.obj248.preAction( cobj0.LHS.CREATE )
   self.obj248.isGraphObjectVisual = True

   if(hasattr(self.obj248, '_setHierarchicalLink')):
     self.obj248._setHierarchicalLink(False)

   # OperCostProp
   self.obj248.OperCostProp.setNone()

   # name
   self.obj248.name.setValue('')
   self.obj248.name.setNone()

   # OperCostFix
   self.obj248.OperCostFix.setNone()

   self.obj248.GGLabel.setValue(5)
   self.obj248.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(240.0,140.0,self.obj248)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj248.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj248)
   self.obj248.postAction( cobj0.LHS.CREATE )

   self.obj249=fromMaterial(self)
   self.obj249.preAction( cobj0.LHS.CREATE )
   self.obj249.isGraphObjectVisual = True

   if(hasattr(self.obj249, '_setHierarchicalLink')):
     self.obj249._setHierarchicalLink(False)

   # rate
   self.obj249.rate.setNone()

   self.obj249.GGLabel.setValue(8)
   self.obj249.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(265.0,100.0,self.obj249)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj249.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj249)
   self.obj249.postAction( cobj0.LHS.CREATE )

   self.obj250=Goal(self)
   self.obj250.preAction( cobj0.LHS.CREATE )
   self.obj250.isGraphObjectVisual = True

   if(hasattr(self.obj250, '_setHierarchicalLink')):
     self.obj250._setHierarchicalLink(False)

   # name
   self.obj250.name.setValue('')
   self.obj250.name.setNone()

   self.obj250.GGLabel.setValue(2)
   self.obj250.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(60.0,220.0,self.obj250)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj250.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj250)
   self.obj250.postAction( cobj0.LHS.CREATE )

   self.obj251=Role(self)
   self.obj251.preAction( cobj0.LHS.CREATE )
   self.obj251.isGraphObjectVisual = True

   if(hasattr(self.obj251, '_setHierarchicalLink')):
     self.obj251._setHierarchicalLink(False)

   # name
   self.obj251.name.setValue('')
   self.obj251.name.setNone()

   self.obj251.GGLabel.setValue(1)
   self.obj251.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(60.0,40.0,self.obj251)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj251.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj251)
   self.obj251.postAction( cobj0.LHS.CREATE )

   self.obj252=achieve(self)
   self.obj252.preAction( cobj0.LHS.CREATE )
   self.obj252.isGraphObjectVisual = True

   if(hasattr(self.obj252, '_setHierarchicalLink')):
     self.obj252._setHierarchicalLink(False)

   # rate
   self.obj252.rate.setNone()

   self.obj252.GGLabel.setValue(3)
   self.obj252.graphClass_= graph_achieve
   if self.genGraphics:
      new_obj = graph_achieve(97.5,137.5,self.obj252)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj252.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj252)
   self.obj252.postAction( cobj0.LHS.CREATE )

   self.obj253=GenericGraphEdge(self)
   self.obj253.preAction( cobj0.LHS.CREATE )
   self.obj253.isGraphObjectVisual = True

   if(hasattr(self.obj253, '_setHierarchicalLink')):
     self.obj253._setHierarchicalLink(False)

   self.obj253.GGLabel.setValue(7)
   self.obj253.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(215.0,41.5,self.obj253)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj253.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj253)
   self.obj253.postAction( cobj0.LHS.CREATE )

   self.obj254=GenericGraphEdge(self)
   self.obj254.preAction( cobj0.LHS.CREATE )
   self.obj254.isGraphObjectVisual = True

   if(hasattr(self.obj254, '_setHierarchicalLink')):
     self.obj254._setHierarchicalLink(False)

   self.obj254.GGLabel.setValue(9)
   self.obj254.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(185.0,276.0,self.obj254)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj254.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj254)
   self.obj254.postAction( cobj0.LHS.CREATE )

   self.obj246.out_connections_.append(self.obj249)
   self.obj249.in_connections_.append(self.obj246)
   self.obj246.graphObject_.pendingConnections.append((self.obj246.graphObject_.tag, self.obj249.graphObject_.tag, [264.0, 69.0, 265.0, 100.0], 0, True))
   self.obj249.out_connections_.append(self.obj248)
   self.obj248.in_connections_.append(self.obj249)
   self.obj249.graphObject_.pendingConnections.append((self.obj249.graphObject_.tag, self.obj248.graphObject_.tag, [260.0, 151.0, 352.0, 90.0], 0, True))
   self.obj250.out_connections_.append(self.obj254)
   self.obj254.in_connections_.append(self.obj250)
   self.obj250.graphObject_.pendingConnections.append((self.obj250.graphObject_.tag, self.obj254.graphObject_.tag, [84.0, 270.0, 185.0, 276.0], 0, True))
   self.obj251.out_connections_.append(self.obj252)
   self.obj252.in_connections_.append(self.obj251)
   self.obj251.graphObject_.pendingConnections.append((self.obj251.graphObject_.tag, self.obj252.graphObject_.tag, [84.0, 86.0, 97.5, 137.5], 0, True))
   self.obj251.out_connections_.append(self.obj253)
   self.obj253.in_connections_.append(self.obj251)
   self.obj251.graphObject_.pendingConnections.append((self.obj251.graphObject_.tag, self.obj253.graphObject_.tag, [84.0, 41.0, 215.0, 41.5], 0, True))
   self.obj252.out_connections_.append(self.obj250)
   self.obj250.in_connections_.append(self.obj252)
   self.obj252.graphObject_.pendingConnections.append((self.obj252.graphObject_.tag, self.obj250.graphObject_.tag, [83.0, 221.0, 93.5, 143.5], 0, True))
   self.obj253.out_connections_.append(self.obj246)
   self.obj246.in_connections_.append(self.obj253)
   self.obj253.graphObject_.pendingConnections.append((self.obj253.graphObject_.tag, self.obj246.graphObject_.tag, [246.0, 62.0, 215.0, 41.5], 0, True))
   self.obj254.out_connections_.append(self.obj247)
   self.obj247.in_connections_.append(self.obj254)
   self.obj254.graphObject_.pendingConnections.append((self.obj254.graphObject_.tag, self.obj247.graphObject_.tag, [246.0, 282.0, 185.0, 276.0], 0, True))

   cobj0.RHS = ASG_pns(self)
   cobj0.RHS.merge(ASG_omacs(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj258=metarial(self)
   self.obj258.preAction( cobj0.RHS.CREATE )
   self.obj258.isGraphObjectVisual = True

   if(hasattr(self.obj258, '_setHierarchicalLink')):
     self.obj258._setHierarchicalLink(False)

   # MaxFlow
   self.obj258.MaxFlow.setNone()

   # price
   self.obj258.price.setValue(0)

   # Name
   self.obj258.Name.setValue('')
   self.obj258.Name.setNone()

   # ReqFlow
   self.obj258.ReqFlow.setNone()

   self.obj258.GGLabel.setValue(4)
   self.obj258.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(280.0,20.0,self.obj258)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj258.graphObject_ = new_obj
   self.obj2580= AttrCalc()
   self.obj2580.Copy=ATOM3Boolean()
   self.obj2580.Copy.setValue(('Copy from LHS', 1))
   self.obj2580.Copy.config = 0
   self.obj2580.Specify=ATOM3Constraint()
   self.obj2580.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj258.GGset2Any['MaxFlow']= self.obj2580
   self.obj2581= AttrCalc()
   self.obj2581.Copy=ATOM3Boolean()
   self.obj2581.Copy.setValue(('Copy from LHS', 1))
   self.obj2581.Copy.config = 0
   self.obj2581.Specify=ATOM3Constraint()
   self.obj2581.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj258.GGset2Any['Name']= self.obj2581
   self.obj2582= AttrCalc()
   self.obj2582.Copy=ATOM3Boolean()
   self.obj2582.Copy.setValue(('Copy from LHS', 1))
   self.obj2582.Copy.config = 0
   self.obj2582.Specify=ATOM3Constraint()
   self.obj2582.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj258.GGset2Any['ReqFlow']= self.obj2582

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj258)
   self.obj258.postAction( cobj0.RHS.CREATE )

   self.obj259=metarial(self)
   self.obj259.preAction( cobj0.RHS.CREATE )
   self.obj259.isGraphObjectVisual = True

   if(hasattr(self.obj259, '_setHierarchicalLink')):
     self.obj259._setHierarchicalLink(False)

   # MaxFlow
   self.obj259.MaxFlow.setNone()

   # price
   self.obj259.price.setValue(0)

   # Name
   self.obj259.Name.setValue('')
   self.obj259.Name.setNone()

   # ReqFlow
   self.obj259.ReqFlow.setNone()

   self.obj259.GGLabel.setValue(6)
   self.obj259.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(280.0,240.0,self.obj259)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj259.graphObject_ = new_obj
   self.obj2590= AttrCalc()
   self.obj2590.Copy=ATOM3Boolean()
   self.obj2590.Copy.setValue(('Copy from LHS', 1))
   self.obj2590.Copy.config = 0
   self.obj2590.Specify=ATOM3Constraint()
   self.obj2590.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj259.GGset2Any['MaxFlow']= self.obj2590
   self.obj2591= AttrCalc()
   self.obj2591.Copy=ATOM3Boolean()
   self.obj2591.Copy.setValue(('Copy from LHS', 1))
   self.obj2591.Copy.config = 0
   self.obj2591.Specify=ATOM3Constraint()
   self.obj2591.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj259.GGset2Any['Name']= self.obj2591
   self.obj2592= AttrCalc()
   self.obj2592.Copy=ATOM3Boolean()
   self.obj2592.Copy.setValue(('Copy from LHS', 1))
   self.obj2592.Copy.config = 0
   self.obj2592.Specify=ATOM3Constraint()
   self.obj2592.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj259.GGset2Any['ReqFlow']= self.obj2592

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj259)
   self.obj259.postAction( cobj0.RHS.CREATE )

   self.obj260=operatingUnit(self)
   self.obj260.preAction( cobj0.RHS.CREATE )
   self.obj260.isGraphObjectVisual = True

   if(hasattr(self.obj260, '_setHierarchicalLink')):
     self.obj260._setHierarchicalLink(False)

   # OperCostProp
   self.obj260.OperCostProp.setNone()

   # name
   self.obj260.name.setValue('')
   self.obj260.name.setNone()

   # OperCostFix
   self.obj260.OperCostFix.setNone()

   self.obj260.GGLabel.setValue(5)
   self.obj260.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(280.0,140.0,self.obj260)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj260.graphObject_ = new_obj
   self.obj2600= AttrCalc()
   self.obj2600.Copy=ATOM3Boolean()
   self.obj2600.Copy.setValue(('Copy from LHS', 1))
   self.obj2600.Copy.config = 0
   self.obj2600.Specify=ATOM3Constraint()
   self.obj2600.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj260.GGset2Any['OperCostProp']= self.obj2600
   self.obj2601= AttrCalc()
   self.obj2601.Copy=ATOM3Boolean()
   self.obj2601.Copy.setValue(('Copy from LHS', 1))
   self.obj2601.Copy.config = 0
   self.obj2601.Specify=ATOM3Constraint()
   self.obj2601.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj260.GGset2Any['name']= self.obj2601
   self.obj2602= AttrCalc()
   self.obj2602.Copy=ATOM3Boolean()
   self.obj2602.Copy.setValue(('Copy from LHS', 1))
   self.obj2602.Copy.config = 0
   self.obj2602.Specify=ATOM3Constraint()
   self.obj2602.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj260.GGset2Any['OperCostFix']= self.obj2602

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj260)
   self.obj260.postAction( cobj0.RHS.CREATE )

   self.obj261=intoMaterial(self)
   self.obj261.preAction( cobj0.RHS.CREATE )
   self.obj261.isGraphObjectVisual = True

   if(hasattr(self.obj261, '_setHierarchicalLink')):
     self.obj261._setHierarchicalLink(False)

   # rate
   self.obj261.rate.setValue(0.0)

   self.obj261.GGLabel.setValue(10)
   self.obj261.graphClass_= graph_intoMaterial
   if self.genGraphics:
      new_obj = graph_intoMaterial(315.25,202.5,self.obj261)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj261.graphObject_ = new_obj
   self.obj2610= AttrCalc()
   self.obj2610.Copy=ATOM3Boolean()
   self.obj2610.Copy.setValue(('Copy from LHS', 0))
   self.obj2610.Copy.config = 0
   self.obj2610.Specify=ATOM3Constraint()
   self.obj2610.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(3)).rate.getValue()\n\n\n\n\n\n\n\n\n\n'))
   self.obj261.GGset2Any['rate']= self.obj2610

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj261)
   self.obj261.postAction( cobj0.RHS.CREATE )

   self.obj262=fromMaterial(self)
   self.obj262.preAction( cobj0.RHS.CREATE )
   self.obj262.isGraphObjectVisual = True

   if(hasattr(self.obj262, '_setHierarchicalLink')):
     self.obj262._setHierarchicalLink(False)

   # rate
   self.obj262.rate.setNone()

   self.obj262.GGLabel.setValue(8)
   self.obj262.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(323.0,83.0,self.obj262)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj262.graphObject_ = new_obj
   self.obj2620= AttrCalc()
   self.obj2620.Copy=ATOM3Boolean()
   self.obj2620.Copy.setValue(('Copy from LHS', 1))
   self.obj2620.Copy.config = 0
   self.obj2620.Specify=ATOM3Constraint()
   self.obj2620.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj262.GGset2Any['rate']= self.obj2620

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj262)
   self.obj262.postAction( cobj0.RHS.CREATE )

   self.obj263=Goal(self)
   self.obj263.preAction( cobj0.RHS.CREATE )
   self.obj263.isGraphObjectVisual = True

   if(hasattr(self.obj263, '_setHierarchicalLink')):
     self.obj263._setHierarchicalLink(False)

   # name
   self.obj263.name.setValue('')
   self.obj263.name.setNone()

   self.obj263.GGLabel.setValue(2)
   self.obj263.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(60.0,220.0,self.obj263)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj263.graphObject_ = new_obj
   self.obj2630= AttrCalc()
   self.obj2630.Copy=ATOM3Boolean()
   self.obj2630.Copy.setValue(('Copy from LHS', 1))
   self.obj2630.Copy.config = 0
   self.obj2630.Specify=ATOM3Constraint()
   self.obj2630.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj263.GGset2Any['name']= self.obj2630

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj263)
   self.obj263.postAction( cobj0.RHS.CREATE )

   self.obj264=Role(self)
   self.obj264.preAction( cobj0.RHS.CREATE )
   self.obj264.isGraphObjectVisual = True

   if(hasattr(self.obj264, '_setHierarchicalLink')):
     self.obj264._setHierarchicalLink(False)

   # name
   self.obj264.name.setValue('')
   self.obj264.name.setNone()

   self.obj264.GGLabel.setValue(1)
   self.obj264.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(60.0,40.0,self.obj264)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj264.graphObject_ = new_obj
   self.obj2640= AttrCalc()
   self.obj2640.Copy=ATOM3Boolean()
   self.obj2640.Copy.setValue(('Copy from LHS', 1))
   self.obj2640.Copy.config = 0
   self.obj2640.Specify=ATOM3Constraint()
   self.obj2640.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj264.GGset2Any['name']= self.obj2640

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj264)
   self.obj264.postAction( cobj0.RHS.CREATE )

   self.obj265=achieve(self)
   self.obj265.preAction( cobj0.RHS.CREATE )
   self.obj265.isGraphObjectVisual = True

   if(hasattr(self.obj265, '_setHierarchicalLink')):
     self.obj265._setHierarchicalLink(False)

   # rate
   self.obj265.rate.setNone()

   self.obj265.GGLabel.setValue(3)
   self.obj265.graphClass_= graph_achieve
   if self.genGraphics:
      new_obj = graph_achieve(93.5,143.5,self.obj265)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj265.graphObject_ = new_obj
   self.obj2650= AttrCalc()
   self.obj2650.Copy=ATOM3Boolean()
   self.obj2650.Copy.setValue(('Copy from LHS', 1))
   self.obj2650.Copy.config = 0
   self.obj2650.Specify=ATOM3Constraint()
   self.obj2650.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj265.GGset2Any['rate']= self.obj2650

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj265)
   self.obj265.postAction( cobj0.RHS.CREATE )

   self.obj266=GenericGraphEdge(self)
   self.obj266.preAction( cobj0.RHS.CREATE )
   self.obj266.isGraphObjectVisual = True

   if(hasattr(self.obj266, '_setHierarchicalLink')):
     self.obj266._setHierarchicalLink(False)

   self.obj266.GGLabel.setValue(7)
   self.obj266.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(215.0,41.5,self.obj266)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj266.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj266)
   self.obj266.postAction( cobj0.RHS.CREATE )

   self.obj267=GenericGraphEdge(self)
   self.obj267.preAction( cobj0.RHS.CREATE )
   self.obj267.isGraphObjectVisual = True

   if(hasattr(self.obj267, '_setHierarchicalLink')):
     self.obj267._setHierarchicalLink(False)

   self.obj267.GGLabel.setValue(9)
   self.obj267.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(185.0,276.0,self.obj267)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj267.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj267)
   self.obj267.postAction( cobj0.RHS.CREATE )

   self.obj258.out_connections_.append(self.obj262)
   self.obj262.in_connections_.append(self.obj258)
   self.obj258.graphObject_.pendingConnections.append((self.obj258.graphObject_.tag, self.obj262.graphObject_.tag, [284.0, 69.0, 323.0, 83.0], 2, 0))
   self.obj260.out_connections_.append(self.obj261)
   self.obj261.in_connections_.append(self.obj260)
   self.obj260.graphObject_.pendingConnections.append((self.obj260.graphObject_.tag, self.obj261.graphObject_.tag, [333.0, 148.0, 332.0, 167.0, 371.25, 179.5], 2, True))
   self.obj261.out_connections_.append(self.obj259)
   self.obj259.in_connections_.append(self.obj261)
   self.obj261.graphObject_.pendingConnections.append((self.obj261.graphObject_.tag, self.obj259.graphObject_.tag, [326.0, 250.0, 354.5, 215.0, 371.25, 179.5], 2, True))
   self.obj262.out_connections_.append(self.obj260)
   self.obj260.in_connections_.append(self.obj262)
   self.obj262.graphObject_.pendingConnections.append((self.obj262.graphObject_.tag, self.obj260.graphObject_.tag, [333.0, 148.0, 352.0, 90.0], 2, 0))
   self.obj263.out_connections_.append(self.obj267)
   self.obj267.in_connections_.append(self.obj263)
   self.obj263.graphObject_.pendingConnections.append((self.obj263.graphObject_.tag, self.obj267.graphObject_.tag, [94.0, 270.0, 185.0, 276.0], 2, 0))
   self.obj264.out_connections_.append(self.obj265)
   self.obj265.in_connections_.append(self.obj264)
   self.obj264.graphObject_.pendingConnections.append((self.obj264.graphObject_.tag, self.obj265.graphObject_.tag, [91.0, 85.0, 93.5, 143.5], 2, 0))
   self.obj264.out_connections_.append(self.obj266)
   self.obj266.in_connections_.append(self.obj264)
   self.obj264.graphObject_.pendingConnections.append((self.obj264.graphObject_.tag, self.obj266.graphObject_.tag, [91.0, 40.0, 215.0, 41.5], 2, 0))
   self.obj265.out_connections_.append(self.obj263)
   self.obj263.in_connections_.append(self.obj265)
   self.obj265.graphObject_.pendingConnections.append((self.obj265.graphObject_.tag, self.obj263.graphObject_.tag, [93.0, 221.0, 93.5, 143.5], 2, 0))
   self.obj266.out_connections_.append(self.obj258)
   self.obj258.in_connections_.append(self.obj266)
   self.obj266.graphObject_.pendingConnections.append((self.obj266.graphObject_.tag, self.obj258.graphObject_.tag, [266.0, 62.0, 215.0, 41.5], 2, 0))
   self.obj267.out_connections_.append(self.obj259)
   self.obj259.in_connections_.append(self.obj267)
   self.obj267.graphObject_.pendingConnections.append((self.obj267.graphObject_.tag, self.obj259.graphObject_.tag, [286.0, 282.0, 185.0, 276.0], 2, 0))

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

   self.obj274=rawMaterial(self)
   self.obj274.preAction( cobj0.LHS.CREATE )
   self.obj274.isGraphObjectVisual = True

   if(hasattr(self.obj274, '_setHierarchicalLink')):
     self.obj274._setHierarchicalLink(False)

   # MaxFlow
   self.obj274.MaxFlow.setNone()

   # price
   self.obj274.price.setValue(0)

   # Name
   self.obj274.Name.setValue('')
   self.obj274.Name.setNone()

   # ReqFlow
   self.obj274.ReqFlow.setNone()

   self.obj274.GGLabel.setValue(6)
   self.obj274.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(240.0,0.0,self.obj274)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj274.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj274)
   self.obj274.postAction( cobj0.LHS.CREATE )

   self.obj275=metarial(self)
   self.obj275.preAction( cobj0.LHS.CREATE )
   self.obj275.isGraphObjectVisual = True

   if(hasattr(self.obj275, '_setHierarchicalLink')):
     self.obj275._setHierarchicalLink(False)

   # MaxFlow
   self.obj275.MaxFlow.setNone()

   # price
   self.obj275.price.setValue(0)

   # Name
   self.obj275.Name.setValue('')
   self.obj275.Name.setNone()

   # ReqFlow
   self.obj275.ReqFlow.setNone()

   self.obj275.GGLabel.setValue(11)
   self.obj275.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(260.0,200.0,self.obj275)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj275.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj275)
   self.obj275.postAction( cobj0.LHS.CREATE )

   self.obj276=operatingUnit(self)
   self.obj276.preAction( cobj0.LHS.CREATE )
   self.obj276.isGraphObjectVisual = True

   if(hasattr(self.obj276, '_setHierarchicalLink')):
     self.obj276._setHierarchicalLink(False)

   # OperCostProp
   self.obj276.OperCostProp.setNone()

   # name
   self.obj276.name.setValue('')
   self.obj276.name.setNone()

   # OperCostFix
   self.obj276.OperCostFix.setNone()

   self.obj276.GGLabel.setValue(7)
   self.obj276.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(280.0,100.0,self.obj276)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj276.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj276)
   self.obj276.postAction( cobj0.LHS.CREATE )

   self.obj277=operatingUnit(self)
   self.obj277.preAction( cobj0.LHS.CREATE )
   self.obj277.isGraphObjectVisual = True

   if(hasattr(self.obj277, '_setHierarchicalLink')):
     self.obj277._setHierarchicalLink(False)

   # OperCostProp
   self.obj277.OperCostProp.setNone()

   # name
   self.obj277.name.setValue('')
   self.obj277.name.setNone()

   # OperCostFix
   self.obj277.OperCostFix.setNone()

   self.obj277.GGLabel.setValue(12)
   self.obj277.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(360.0,260.0,self.obj277)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj277.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj277)
   self.obj277.postAction( cobj0.LHS.CREATE )

   self.obj278=fromRaw(self)
   self.obj278.preAction( cobj0.LHS.CREATE )
   self.obj278.isGraphObjectVisual = True

   if(hasattr(self.obj278, '_setHierarchicalLink')):
     self.obj278._setHierarchicalLink(False)

   # rate
   self.obj278.rate.setNone()

   self.obj278.GGLabel.setValue(8)
   self.obj278.graphClass_= graph_fromRaw
   if self.genGraphics:
      new_obj = graph_fromRaw(311.5,63.25,self.obj278)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj278.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj278)
   self.obj278.postAction( cobj0.LHS.CREATE )

   self.obj279=fromMaterial(self)
   self.obj279.preAction( cobj0.LHS.CREATE )
   self.obj279.isGraphObjectVisual = True

   if(hasattr(self.obj279, '_setHierarchicalLink')):
     self.obj279._setHierarchicalLink(False)

   # rate
   self.obj279.rate.setNone()

   self.obj279.GGLabel.setValue(14)
   self.obj279.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(379.5,235.25,self.obj279)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj279.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj279)
   self.obj279.postAction( cobj0.LHS.CREATE )

   self.obj280=CapableOf(self)
   self.obj280.preAction( cobj0.LHS.CREATE )
   self.obj280.isGraphObjectVisual = True

   if(hasattr(self.obj280, '_setHierarchicalLink')):
     self.obj280._setHierarchicalLink(False)

   # rate
   self.obj280.rate.setNone()

   self.obj280.GGLabel.setValue(3)
   self.obj280.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(84.5,131.5,self.obj280)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj280.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj280)
   self.obj280.postAction( cobj0.LHS.CREATE )

   self.obj281=Agent(self)
   self.obj281.preAction( cobj0.LHS.CREATE )
   self.obj281.isGraphObjectVisual = True

   if(hasattr(self.obj281, '_setHierarchicalLink')):
     self.obj281._setHierarchicalLink(False)

   # price
   self.obj281.price.setNone()

   # name
   self.obj281.name.setValue('')
   self.obj281.name.setNone()

   self.obj281.GGLabel.setValue(1)
   self.obj281.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(60.0,20.0,self.obj281)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj281.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj281)
   self.obj281.postAction( cobj0.LHS.CREATE )

   self.obj282=Role(self)
   self.obj282.preAction( cobj0.LHS.CREATE )
   self.obj282.isGraphObjectVisual = True

   if(hasattr(self.obj282, '_setHierarchicalLink')):
     self.obj282._setHierarchicalLink(False)

   # name
   self.obj282.name.setValue('')
   self.obj282.name.setNone()

   self.obj282.GGLabel.setValue(2)
   self.obj282.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(60.0,180.0,self.obj282)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj282.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj282)
   self.obj282.postAction( cobj0.LHS.CREATE )

   self.obj283=GenericGraphEdge(self)
   self.obj283.preAction( cobj0.LHS.CREATE )
   self.obj283.isGraphObjectVisual = True

   if(hasattr(self.obj283, '_setHierarchicalLink')):
     self.obj283._setHierarchicalLink(False)

   self.obj283.GGLabel.setValue(15)
   self.obj283.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(174.5,69.0,self.obj283)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj283.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj283)
   self.obj283.postAction( cobj0.LHS.CREATE )

   self.obj284=GenericGraphEdge(self)
   self.obj284.preAction( cobj0.LHS.CREATE )
   self.obj284.isGraphObjectVisual = True

   if(hasattr(self.obj284, '_setHierarchicalLink')):
     self.obj284._setHierarchicalLink(False)

   self.obj284.GGLabel.setValue(10)
   self.obj284.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(245.75,97.25,self.obj284)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj284.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj284)
   self.obj284.postAction( cobj0.LHS.CREATE )

   self.obj285=GenericGraphEdge(self)
   self.obj285.preAction( cobj0.LHS.CREATE )
   self.obj285.isGraphObjectVisual = True

   if(hasattr(self.obj285, '_setHierarchicalLink')):
     self.obj285._setHierarchicalLink(False)

   self.obj285.GGLabel.setValue(13)
   self.obj285.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(175.0,234.0,self.obj285)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj285.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj285)
   self.obj285.postAction( cobj0.LHS.CREATE )

   self.obj274.out_connections_.append(self.obj278)
   self.obj278.in_connections_.append(self.obj274)
   self.obj274.graphObject_.pendingConnections.append((self.obj274.graphObject_.tag, self.obj278.graphObject_.tag, [264.0, 56.0, 295.0, 49.5, 311.5, 63.25], 2, True))
   self.obj275.out_connections_.append(self.obj279)
   self.obj279.in_connections_.append(self.obj275)
   self.obj275.graphObject_.pendingConnections.append((self.obj275.graphObject_.tag, self.obj279.graphObject_.tag, [306.0, 210.0, 353.5, 220.0, 379.5, 235.25], 2, True))
   self.obj278.out_connections_.append(self.obj276)
   self.obj276.in_connections_.append(self.obj278)
   self.obj278.graphObject_.pendingConnections.append((self.obj278.graphObject_.tag, self.obj276.graphObject_.tag, [330.0, 111.0, 328.0, 77.0, 311.5, 63.25], 2, True))
   self.obj279.out_connections_.append(self.obj277)
   self.obj277.in_connections_.append(self.obj279)
   self.obj279.graphObject_.pendingConnections.append((self.obj279.graphObject_.tag, self.obj277.graphObject_.tag, [410.0, 271.0, 405.5, 250.5, 379.5, 235.25], 2, True))
   self.obj280.out_connections_.append(self.obj282)
   self.obj282.in_connections_.append(self.obj280)
   self.obj280.graphObject_.pendingConnections.append((self.obj280.graphObject_.tag, self.obj282.graphObject_.tag, [84.0, 181.0, 84.5, 131.5], 0, True))
   self.obj281.out_connections_.append(self.obj280)
   self.obj280.in_connections_.append(self.obj281)
   self.obj281.graphObject_.pendingConnections.append((self.obj281.graphObject_.tag, self.obj280.graphObject_.tag, [85.0, 82.0, 84.5, 131.5], 0, True))
   self.obj281.out_connections_.append(self.obj283)
   self.obj283.in_connections_.append(self.obj281)
   self.obj281.graphObject_.pendingConnections.append((self.obj281.graphObject_.tag, self.obj283.graphObject_.tag, [85.0, 82.0, 174.5, 69.0], 0, True))
   self.obj281.out_connections_.append(self.obj284)
   self.obj284.in_connections_.append(self.obj281)
   self.obj281.graphObject_.pendingConnections.append((self.obj281.graphObject_.tag, self.obj284.graphObject_.tag, [85.0, 82.0, 192.0, 90.0, 245.75, 97.25], 2, True))
   self.obj282.out_connections_.append(self.obj285)
   self.obj285.in_connections_.append(self.obj282)
   self.obj282.graphObject_.pendingConnections.append((self.obj282.graphObject_.tag, self.obj285.graphObject_.tag, [84.0, 226.0, 175.0, 234.0], 0, True))
   self.obj283.out_connections_.append(self.obj274)
   self.obj274.in_connections_.append(self.obj283)
   self.obj283.graphObject_.pendingConnections.append((self.obj283.graphObject_.tag, self.obj274.graphObject_.tag, [264.0, 56.0, 174.5, 69.0], 0, True))
   self.obj284.out_connections_.append(self.obj276)
   self.obj276.in_connections_.append(self.obj284)
   self.obj284.graphObject_.pendingConnections.append((self.obj284.graphObject_.tag, self.obj276.graphObject_.tag, [300.0, 111.0, 299.5, 104.5, 245.75, 97.25], 2, True))
   self.obj285.out_connections_.append(self.obj275)
   self.obj275.in_connections_.append(self.obj285)
   self.obj285.graphObject_.pendingConnections.append((self.obj285.graphObject_.tag, self.obj275.graphObject_.tag, [266.0, 242.0, 175.0, 234.0], 0, True))

   cobj0.RHS = ASG_pns(self)
   cobj0.RHS.merge(ASG_omacs(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj289=rawMaterial(self)
   self.obj289.preAction( cobj0.RHS.CREATE )
   self.obj289.isGraphObjectVisual = True

   if(hasattr(self.obj289, '_setHierarchicalLink')):
     self.obj289._setHierarchicalLink(False)

   # MaxFlow
   self.obj289.MaxFlow.setNone()

   # price
   self.obj289.price.setValue(0)

   # Name
   self.obj289.Name.setValue('')
   self.obj289.Name.setNone()

   # ReqFlow
   self.obj289.ReqFlow.setNone()

   self.obj289.GGLabel.setValue(6)
   self.obj289.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(240.0,0.0,self.obj289)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj289.graphObject_ = new_obj
   self.obj2890= AttrCalc()
   self.obj2890.Copy=ATOM3Boolean()
   self.obj2890.Copy.setValue(('Copy from LHS', 1))
   self.obj2890.Copy.config = 0
   self.obj2890.Specify=ATOM3Constraint()
   self.obj2890.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj289.GGset2Any['MaxFlow']= self.obj2890
   self.obj2891= AttrCalc()
   self.obj2891.Copy=ATOM3Boolean()
   self.obj2891.Copy.setValue(('Copy from LHS', 1))
   self.obj2891.Copy.config = 0
   self.obj2891.Specify=ATOM3Constraint()
   self.obj2891.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj289.GGset2Any['Name']= self.obj2891
   self.obj2892= AttrCalc()
   self.obj2892.Copy=ATOM3Boolean()
   self.obj2892.Copy.setValue(('Copy from LHS', 1))
   self.obj2892.Copy.config = 0
   self.obj2892.Specify=ATOM3Constraint()
   self.obj2892.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj289.GGset2Any['ReqFlow']= self.obj2892

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj289)
   self.obj289.postAction( cobj0.RHS.CREATE )

   self.obj290=metarial(self)
   self.obj290.preAction( cobj0.RHS.CREATE )
   self.obj290.isGraphObjectVisual = True

   if(hasattr(self.obj290, '_setHierarchicalLink')):
     self.obj290._setHierarchicalLink(False)

   # MaxFlow
   self.obj290.MaxFlow.setNone()

   # price
   self.obj290.price.setValue(0)

   # Name
   self.obj290.Name.setValue('')
   self.obj290.Name.setNone()

   # ReqFlow
   self.obj290.ReqFlow.setNone()

   self.obj290.GGLabel.setValue(11)
   self.obj290.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(260.0,200.0,self.obj290)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj290.graphObject_ = new_obj
   self.obj2900= AttrCalc()
   self.obj2900.Copy=ATOM3Boolean()
   self.obj2900.Copy.setValue(('Copy from LHS', 1))
   self.obj2900.Copy.config = 0
   self.obj2900.Specify=ATOM3Constraint()
   self.obj2900.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj290.GGset2Any['MaxFlow']= self.obj2900
   self.obj2901= AttrCalc()
   self.obj2901.Copy=ATOM3Boolean()
   self.obj2901.Copy.setValue(('Copy from LHS', 1))
   self.obj2901.Copy.config = 0
   self.obj2901.Specify=ATOM3Constraint()
   self.obj2901.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj290.GGset2Any['Name']= self.obj2901
   self.obj2902= AttrCalc()
   self.obj2902.Copy=ATOM3Boolean()
   self.obj2902.Copy.setValue(('Copy from LHS', 1))
   self.obj2902.Copy.config = 0
   self.obj2902.Specify=ATOM3Constraint()
   self.obj2902.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj290.GGset2Any['ReqFlow']= self.obj2902

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj290)
   self.obj290.postAction( cobj0.RHS.CREATE )

   self.obj291=operatingUnit(self)
   self.obj291.preAction( cobj0.RHS.CREATE )
   self.obj291.isGraphObjectVisual = True

   if(hasattr(self.obj291, '_setHierarchicalLink')):
     self.obj291._setHierarchicalLink(False)

   # OperCostProp
   self.obj291.OperCostProp.setNone()

   # name
   self.obj291.name.setValue('')
   self.obj291.name.setNone()

   # OperCostFix
   self.obj291.OperCostFix.setNone()

   self.obj291.GGLabel.setValue(7)
   self.obj291.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(280.0,100.0,self.obj291)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj291.graphObject_ = new_obj
   self.obj2910= AttrCalc()
   self.obj2910.Copy=ATOM3Boolean()
   self.obj2910.Copy.setValue(('Copy from LHS', 1))
   self.obj2910.Copy.config = 0
   self.obj2910.Specify=ATOM3Constraint()
   self.obj2910.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj291.GGset2Any['OperCostProp']= self.obj2910
   self.obj2911= AttrCalc()
   self.obj2911.Copy=ATOM3Boolean()
   self.obj2911.Copy.setValue(('Copy from LHS', 1))
   self.obj2911.Copy.config = 0
   self.obj2911.Specify=ATOM3Constraint()
   self.obj2911.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj291.GGset2Any['name']= self.obj2911
   self.obj2912= AttrCalc()
   self.obj2912.Copy=ATOM3Boolean()
   self.obj2912.Copy.setValue(('Copy from LHS', 1))
   self.obj2912.Copy.config = 0
   self.obj2912.Specify=ATOM3Constraint()
   self.obj2912.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj291.GGset2Any['OperCostFix']= self.obj2912

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj291)
   self.obj291.postAction( cobj0.RHS.CREATE )

   self.obj292=operatingUnit(self)
   self.obj292.preAction( cobj0.RHS.CREATE )
   self.obj292.isGraphObjectVisual = True

   if(hasattr(self.obj292, '_setHierarchicalLink')):
     self.obj292._setHierarchicalLink(False)

   # OperCostProp
   self.obj292.OperCostProp.setNone()

   # name
   self.obj292.name.setValue('')
   self.obj292.name.setNone()

   # OperCostFix
   self.obj292.OperCostFix.setNone()

   self.obj292.GGLabel.setValue(12)
   self.obj292.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(360.0,260.0,self.obj292)
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
   self.obj292.GGset2Any['OperCostProp']= self.obj2920
   self.obj2921= AttrCalc()
   self.obj2921.Copy=ATOM3Boolean()
   self.obj2921.Copy.setValue(('Copy from LHS', 1))
   self.obj2921.Copy.config = 0
   self.obj2921.Specify=ATOM3Constraint()
   self.obj2921.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj292.GGset2Any['name']= self.obj2921
   self.obj2922= AttrCalc()
   self.obj2922.Copy=ATOM3Boolean()
   self.obj2922.Copy.setValue(('Copy from LHS', 1))
   self.obj2922.Copy.config = 0
   self.obj2922.Specify=ATOM3Constraint()
   self.obj2922.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj292.GGset2Any['OperCostFix']= self.obj2922

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj292)
   self.obj292.postAction( cobj0.RHS.CREATE )

   self.obj293=fromRaw(self)
   self.obj293.preAction( cobj0.RHS.CREATE )
   self.obj293.isGraphObjectVisual = True

   if(hasattr(self.obj293, '_setHierarchicalLink')):
     self.obj293._setHierarchicalLink(False)

   # rate
   self.obj293.rate.setNone()

   self.obj293.GGLabel.setValue(8)
   self.obj293.graphClass_= graph_fromRaw
   if self.genGraphics:
      new_obj = graph_fromRaw(311.5,63.25,self.obj293)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj293.graphObject_ = new_obj
   self.obj2930= AttrCalc()
   self.obj2930.Copy=ATOM3Boolean()
   self.obj2930.Copy.setValue(('Copy from LHS', 1))
   self.obj2930.Copy.config = 0
   self.obj2930.Specify=ATOM3Constraint()
   self.obj2930.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj293.GGset2Any['rate']= self.obj2930

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj293)
   self.obj293.postAction( cobj0.RHS.CREATE )

   self.obj294=intoMaterial(self)
   self.obj294.preAction( cobj0.RHS.CREATE )
   self.obj294.isGraphObjectVisual = True

   if(hasattr(self.obj294, '_setHierarchicalLink')):
     self.obj294._setHierarchicalLink(False)

   # rate
   self.obj294.rate.setValue(0.0)

   self.obj294.GGLabel.setValue(17)
   self.obj294.graphClass_= graph_intoMaterial
   if self.genGraphics:
      new_obj = graph_intoMaterial(324.25,167.5,self.obj294)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj294.graphObject_ = new_obj
   self.obj2940= AttrCalc()
   self.obj2940.Copy=ATOM3Boolean()
   self.obj2940.Copy.setValue(('Copy from LHS', 0))
   self.obj2940.Copy.config = 0
   self.obj2940.Specify=ATOM3Constraint()
   self.obj2940.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'a = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) ).name.getValue()\nb = self.getMatched ( graphID , self.LHS.nodeWithLabel(2) ).name.getValue()\nreturn self.graphRewritingSystem.Dictag[ a ][b]\n\n'))
   self.obj294.GGset2Any['rate']= self.obj2940

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj294)
   self.obj294.postAction( cobj0.RHS.CREATE )

   self.obj295=fromMaterial(self)
   self.obj295.preAction( cobj0.RHS.CREATE )
   self.obj295.isGraphObjectVisual = True

   if(hasattr(self.obj295, '_setHierarchicalLink')):
     self.obj295._setHierarchicalLink(False)

   # rate
   self.obj295.rate.setNone()

   self.obj295.GGLabel.setValue(14)
   self.obj295.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(379.5,235.25,self.obj295)
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

   self.obj296=CapableOf(self)
   self.obj296.preAction( cobj0.RHS.CREATE )
   self.obj296.isGraphObjectVisual = True

   if(hasattr(self.obj296, '_setHierarchicalLink')):
     self.obj296._setHierarchicalLink(False)

   # rate
   self.obj296.rate.setNone()

   self.obj296.GGLabel.setValue(3)
   self.obj296.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(84.5,131.5,self.obj296)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj296.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj296)
   self.obj296.postAction( cobj0.RHS.CREATE )

   self.obj297=Agent(self)
   self.obj297.preAction( cobj0.RHS.CREATE )
   self.obj297.isGraphObjectVisual = True

   if(hasattr(self.obj297, '_setHierarchicalLink')):
     self.obj297._setHierarchicalLink(False)

   # price
   self.obj297.price.setNone()

   # name
   self.obj297.name.setValue('')
   self.obj297.name.setNone()

   self.obj297.GGLabel.setValue(1)
   self.obj297.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(60.0,20.0,self.obj297)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj297.graphObject_ = new_obj
   self.obj2970= AttrCalc()
   self.obj2970.Copy=ATOM3Boolean()
   self.obj2970.Copy.setValue(('Copy from LHS', 1))
   self.obj2970.Copy.config = 0
   self.obj2970.Specify=ATOM3Constraint()
   self.obj2970.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj297.GGset2Any['price']= self.obj2970
   self.obj2971= AttrCalc()
   self.obj2971.Copy=ATOM3Boolean()
   self.obj2971.Copy.setValue(('Copy from LHS', 1))
   self.obj2971.Copy.config = 0
   self.obj2971.Specify=ATOM3Constraint()
   self.obj2971.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj297.GGset2Any['name']= self.obj2971

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj297)
   self.obj297.postAction( cobj0.RHS.CREATE )

   self.obj298=Role(self)
   self.obj298.preAction( cobj0.RHS.CREATE )
   self.obj298.isGraphObjectVisual = True

   if(hasattr(self.obj298, '_setHierarchicalLink')):
     self.obj298._setHierarchicalLink(False)

   # name
   self.obj298.name.setValue('')
   self.obj298.name.setNone()

   self.obj298.GGLabel.setValue(2)
   self.obj298.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(60.0,180.0,self.obj298)
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
   self.obj298.GGset2Any['name']= self.obj2980

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj298)
   self.obj298.postAction( cobj0.RHS.CREATE )

   self.obj299=GenericGraphEdge(self)
   self.obj299.preAction( cobj0.RHS.CREATE )
   self.obj299.isGraphObjectVisual = True

   if(hasattr(self.obj299, '_setHierarchicalLink')):
     self.obj299._setHierarchicalLink(False)

   self.obj299.GGLabel.setValue(15)
   self.obj299.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(174.5,69.0,self.obj299)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj299.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj299)
   self.obj299.postAction( cobj0.RHS.CREATE )

   self.obj300=GenericGraphEdge(self)
   self.obj300.preAction( cobj0.RHS.CREATE )
   self.obj300.isGraphObjectVisual = True

   if(hasattr(self.obj300, '_setHierarchicalLink')):
     self.obj300._setHierarchicalLink(False)

   self.obj300.GGLabel.setValue(10)
   self.obj300.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(245.75,97.25,self.obj300)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj300.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj300)
   self.obj300.postAction( cobj0.RHS.CREATE )

   self.obj301=GenericGraphEdge(self)
   self.obj301.preAction( cobj0.RHS.CREATE )
   self.obj301.isGraphObjectVisual = True

   if(hasattr(self.obj301, '_setHierarchicalLink')):
     self.obj301._setHierarchicalLink(False)

   self.obj301.GGLabel.setValue(13)
   self.obj301.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(175.0,234.0,self.obj301)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj301.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj301)
   self.obj301.postAction( cobj0.RHS.CREATE )

   self.obj289.out_connections_.append(self.obj293)
   self.obj293.in_connections_.append(self.obj289)
   self.obj289.graphObject_.pendingConnections.append((self.obj289.graphObject_.tag, self.obj293.graphObject_.tag, [264.0, 50.0, 311.5, 63.25], 2, 0))
   self.obj290.out_connections_.append(self.obj295)
   self.obj295.in_connections_.append(self.obj290)
   self.obj290.graphObject_.pendingConnections.append((self.obj290.graphObject_.tag, self.obj295.graphObject_.tag, [306.0, 210.0, 379.5, 235.25], 2, 0))
   self.obj291.out_connections_.append(self.obj294)
   self.obj294.in_connections_.append(self.obj291)
   self.obj291.graphObject_.pendingConnections.append((self.obj291.graphObject_.tag, self.obj294.graphObject_.tag, [333.0, 108.0, 331.0, 142.0, 324.25, 167.5], 2, True))
   self.obj293.out_connections_.append(self.obj291)
   self.obj291.in_connections_.append(self.obj293)
   self.obj293.graphObject_.pendingConnections.append((self.obj293.graphObject_.tag, self.obj291.graphObject_.tag, [330.0, 101.0, 311.5, 63.25], 2, 0))
   self.obj294.out_connections_.append(self.obj290)
   self.obj290.in_connections_.append(self.obj294)
   self.obj294.graphObject_.pendingConnections.append((self.obj294.graphObject_.tag, self.obj290.graphObject_.tag, [306.0, 210.0, 317.5, 193.0, 324.25, 167.5], 2, True))
   self.obj295.out_connections_.append(self.obj292)
   self.obj292.in_connections_.append(self.obj295)
   self.obj295.graphObject_.pendingConnections.append((self.obj295.graphObject_.tag, self.obj292.graphObject_.tag, [413.0, 268.0, 379.5, 235.25], 2, 0))
   self.obj296.out_connections_.append(self.obj298)
   self.obj298.in_connections_.append(self.obj296)
   self.obj296.graphObject_.pendingConnections.append((self.obj296.graphObject_.tag, self.obj298.graphObject_.tag, [91.0, 180.0, 84.5, 131.5], 2, 0))
   self.obj297.out_connections_.append(self.obj296)
   self.obj296.in_connections_.append(self.obj297)
   self.obj297.graphObject_.pendingConnections.append((self.obj297.graphObject_.tag, self.obj296.graphObject_.tag, [97.0, 82.0, 84.5, 131.5], 2, 0))
   self.obj297.out_connections_.append(self.obj299)
   self.obj299.in_connections_.append(self.obj297)
   self.obj297.graphObject_.pendingConnections.append((self.obj297.graphObject_.tag, self.obj299.graphObject_.tag, [97.0, 82.0, 174.5, 69.0], 2, 0))
   self.obj297.out_connections_.append(self.obj300)
   self.obj300.in_connections_.append(self.obj297)
   self.obj297.graphObject_.pendingConnections.append((self.obj297.graphObject_.tag, self.obj300.graphObject_.tag, [97.0, 82.0, 245.75, 97.25], 2, 0))
   self.obj298.out_connections_.append(self.obj301)
   self.obj301.in_connections_.append(self.obj298)
   self.obj298.graphObject_.pendingConnections.append((self.obj298.graphObject_.tag, self.obj301.graphObject_.tag, [91.0, 225.0, 175.0, 234.0], 2, 0))
   self.obj299.out_connections_.append(self.obj289)
   self.obj289.in_connections_.append(self.obj299)
   self.obj299.graphObject_.pendingConnections.append((self.obj299.graphObject_.tag, self.obj289.graphObject_.tag, [264.0, 50.0, 174.5, 69.0], 2, 0))
   self.obj300.out_connections_.append(self.obj291)
   self.obj291.in_connections_.append(self.obj300)
   self.obj300.graphObject_.pendingConnections.append((self.obj300.graphObject_.tag, self.obj291.graphObject_.tag, [300.0, 101.0, 245.75, 97.25], 2, 0))
   self.obj301.out_connections_.append(self.obj290)
   self.obj290.in_connections_.append(self.obj301)
   self.obj301.graphObject_.pendingConnections.append((self.obj301.graphObject_.tag, self.obj290.graphObject_.tag, [266.0, 242.0, 175.0, 234.0], 2, 0))

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

   self.obj308=rawMaterial(self)
   self.obj308.preAction( cobj0.LHS.CREATE )
   self.obj308.isGraphObjectVisual = True

   if(hasattr(self.obj308, '_setHierarchicalLink')):
     self.obj308._setHierarchicalLink(False)

   # MaxFlow
   self.obj308.MaxFlow.setNone()

   # price
   self.obj308.price.setNone()

   # Name
   self.obj308.Name.setValue('')
   self.obj308.Name.setNone()

   # ReqFlow
   self.obj308.ReqFlow.setNone()

   self.obj308.GGLabel.setValue(1)
   self.obj308.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(280.0,60.0,self.obj308)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['Text Scale'] = 0.5
      new_obj.layConstraints['scale'] = [0.5, 0.5]
   else: new_obj = None
   self.obj308.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj308)
   self.obj308.postAction( cobj0.LHS.CREATE )

   self.obj309=Agent(self)
   self.obj309.preAction( cobj0.LHS.CREATE )
   self.obj309.isGraphObjectVisual = True

   if(hasattr(self.obj309, '_setHierarchicalLink')):
     self.obj309._setHierarchicalLink(False)

   # price
   self.obj309.price.setNone()

   # name
   self.obj309.name.setValue('')
   self.obj309.name.setNone()

   self.obj309.GGLabel.setValue(2)
   self.obj309.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(120.0,60.0,self.obj309)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['Text Scale'] = 0.5
      new_obj.layConstraints['scale'] = [0.5, 0.5]
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

   self.obj310.GGLabel.setValue(3)
   self.obj310.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(198.5,126.5,self.obj310)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj310.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj310)
   self.obj310.postAction( cobj0.LHS.CREATE )

   self.obj309.out_connections_.append(self.obj310)
   self.obj310.in_connections_.append(self.obj309)
   self.obj309.graphObject_.pendingConnections.append((self.obj309.graphObject_.tag, self.obj310.graphObject_.tag, [105.0, 89.5, 130.0, 127.0, 198.5, 126.5], 2, True))
   self.obj310.out_connections_.append(self.obj308)
   self.obj308.in_connections_.append(self.obj310)
   self.obj310.graphObject_.pendingConnections.append((self.obj310.graphObject_.tag, self.obj308.graphObject_.tag, [290.5, 89.5, 267.0, 126.0, 198.5, 126.5], 2, True))

   cobj0.RHS = ASG_pns(self)
   cobj0.RHS.merge(ASG_omacs(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj314=rawMaterial(self)
   self.obj314.preAction( cobj0.RHS.CREATE )
   self.obj314.isGraphObjectVisual = True

   if(hasattr(self.obj314, '_setHierarchicalLink')):
     self.obj314._setHierarchicalLink(False)

   # MaxFlow
   self.obj314.MaxFlow.setNone()

   # price
   self.obj314.price.setNone()

   # Name
   self.obj314.Name.setValue('')
   self.obj314.Name.setNone()

   # ReqFlow
   self.obj314.ReqFlow.setNone()

   self.obj314.GGLabel.setValue(1)
   self.obj314.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(280.0,60.0,self.obj314)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj314.graphObject_ = new_obj
   self.obj3140= AttrCalc()
   self.obj3140.Copy=ATOM3Boolean()
   self.obj3140.Copy.setValue(('Copy from LHS', 1))
   self.obj3140.Copy.config = 0
   self.obj3140.Specify=ATOM3Constraint()
   self.obj3140.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj314.GGset2Any['MaxFlow']= self.obj3140
   self.obj3141= AttrCalc()
   self.obj3141.Copy=ATOM3Boolean()
   self.obj3141.Copy.setValue(('Copy from LHS', 0))
   self.obj3141.Copy.config = 0
   self.obj3141.Specify=ATOM3Constraint()
   self.obj3141.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(2)).price.getValue()\n\n\n\n\n\n\n'))
   self.obj314.GGset2Any['price']= self.obj3141
   self.obj3142= AttrCalc()
   self.obj3142.Copy=ATOM3Boolean()
   self.obj3142.Copy.setValue(('Copy from LHS', 1))
   self.obj3142.Copy.config = 0
   self.obj3142.Specify=ATOM3Constraint()
   self.obj3142.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj314.GGset2Any['Name']= self.obj3142
   self.obj3143= AttrCalc()
   self.obj3143.Copy=ATOM3Boolean()
   self.obj3143.Copy.setValue(('Copy from LHS', 1))
   self.obj3143.Copy.config = 0
   self.obj3143.Specify=ATOM3Constraint()
   self.obj3143.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj314.GGset2Any['ReqFlow']= self.obj3143

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj314)
   self.obj314.postAction( cobj0.RHS.CREATE )

   self.obj315=Agent(self)
   self.obj315.preAction( cobj0.RHS.CREATE )
   self.obj315.isGraphObjectVisual = True

   if(hasattr(self.obj315, '_setHierarchicalLink')):
     self.obj315._setHierarchicalLink(False)

   # price
   self.obj315.price.setNone()

   # name
   self.obj315.name.setValue('')
   self.obj315.name.setNone()

   self.obj315.GGLabel.setValue(2)
   self.obj315.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(120.0,60.0,self.obj315)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj315.graphObject_ = new_obj
   self.obj3150= AttrCalc()
   self.obj3150.Copy=ATOM3Boolean()
   self.obj3150.Copy.setValue(('Copy from LHS', 1))
   self.obj3150.Copy.config = 0
   self.obj3150.Specify=ATOM3Constraint()
   self.obj3150.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj315.GGset2Any['price']= self.obj3150
   self.obj3151= AttrCalc()
   self.obj3151.Copy=ATOM3Boolean()
   self.obj3151.Copy.setValue(('Copy from LHS', 1))
   self.obj3151.Copy.config = 0
   self.obj3151.Specify=ATOM3Constraint()
   self.obj3151.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj315.GGset2Any['name']= self.obj3151

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj315)
   self.obj315.postAction( cobj0.RHS.CREATE )

   self.obj316=GenericGraphEdge(self)
   self.obj316.preAction( cobj0.RHS.CREATE )
   self.obj316.isGraphObjectVisual = True

   if(hasattr(self.obj316, '_setHierarchicalLink')):
     self.obj316._setHierarchicalLink(False)

   self.obj316.GGLabel.setValue(3)
   self.obj316.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(198.5,126.5,self.obj316)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj316.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj316)
   self.obj316.postAction( cobj0.RHS.CREATE )

   self.obj315.out_connections_.append(self.obj316)
   self.obj316.in_connections_.append(self.obj315)
   self.obj315.graphObject_.pendingConnections.append((self.obj315.graphObject_.tag, self.obj316.graphObject_.tag, [157.0, 122.0, 198.5, 126.5], 2, 0))
   self.obj316.out_connections_.append(self.obj314)
   self.obj314.in_connections_.append(self.obj316)
   self.obj316.graphObject_.pendingConnections.append((self.obj316.graphObject_.tag, self.obj314.graphObject_.tag, [304.0, 110.0, 198.5, 126.5], 2, 0))

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

   self.obj323=operatingUnit(self)
   self.obj323.preAction( cobj0.LHS.CREATE )
   self.obj323.isGraphObjectVisual = True

   if(hasattr(self.obj323, '_setHierarchicalLink')):
     self.obj323._setHierarchicalLink(False)

   # OperCostProp
   self.obj323.OperCostProp.setNone()

   # name
   self.obj323.name.setValue('')
   self.obj323.name.setNone()

   # OperCostFix
   self.obj323.OperCostFix.setNone()

   self.obj323.GGLabel.setValue(4)
   self.obj323.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(280.0,120.0,self.obj323)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj323.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj323)
   self.obj323.postAction( cobj0.LHS.CREATE )

   self.obj324=CapableOf(self)
   self.obj324.preAction( cobj0.LHS.CREATE )
   self.obj324.isGraphObjectVisual = True

   if(hasattr(self.obj324, '_setHierarchicalLink')):
     self.obj324._setHierarchicalLink(False)

   # rate
   self.obj324.rate.setNone()

   self.obj324.GGLabel.setValue(5)
   self.obj324.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(160.5,121.5,self.obj324)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj324.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj324)
   self.obj324.postAction( cobj0.LHS.CREATE )

   self.obj325=Agent(self)
   self.obj325.preAction( cobj0.LHS.CREATE )
   self.obj325.isGraphObjectVisual = True

   if(hasattr(self.obj325, '_setHierarchicalLink')):
     self.obj325._setHierarchicalLink(False)

   # price
   self.obj325.price.setNone()

   # name
   self.obj325.name.setValue('')
   self.obj325.name.setNone()

   self.obj325.GGLabel.setValue(1)
   self.obj325.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(120.0,40.0,self.obj325)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj325.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj325)
   self.obj325.postAction( cobj0.LHS.CREATE )

   self.obj326=Role(self)
   self.obj326.preAction( cobj0.LHS.CREATE )
   self.obj326.isGraphObjectVisual = True

   if(hasattr(self.obj326, '_setHierarchicalLink')):
     self.obj326._setHierarchicalLink(False)

   # name
   self.obj326.name.setValue('')
   self.obj326.name.setNone()

   self.obj326.GGLabel.setValue(2)
   self.obj326.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(140.0,140.0,self.obj326)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj326.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj326)
   self.obj326.postAction( cobj0.LHS.CREATE )

   self.obj327=GenericGraphEdge(self)
   self.obj327.preAction( cobj0.LHS.CREATE )
   self.obj327.isGraphObjectVisual = True

   if(hasattr(self.obj327, '_setHierarchicalLink')):
     self.obj327._setHierarchicalLink(False)

   self.obj327.GGLabel.setValue(3)
   self.obj327.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(264.75,85.25,self.obj327)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj327.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj327)
   self.obj327.postAction( cobj0.LHS.CREATE )

   self.obj324.out_connections_.append(self.obj326)
   self.obj326.in_connections_.append(self.obj324)
   self.obj324.graphObject_.pendingConnections.append((self.obj324.graphObject_.tag, self.obj326.graphObject_.tag, [164.0, 141.0, 160.5, 121.5], 0, True))
   self.obj325.out_connections_.append(self.obj327)
   self.obj327.in_connections_.append(self.obj325)
   self.obj325.graphObject_.pendingConnections.append((self.obj325.graphObject_.tag, self.obj327.graphObject_.tag, [145.0, 102.0, 226.0, 83.0, 264.75, 85.25], 2, True))
   self.obj325.out_connections_.append(self.obj324)
   self.obj324.in_connections_.append(self.obj325)
   self.obj325.graphObject_.pendingConnections.append((self.obj325.graphObject_.tag, self.obj324.graphObject_.tag, [157.0, 102.0, 160.5, 121.5], 0, True))
   self.obj327.out_connections_.append(self.obj323)
   self.obj323.in_connections_.append(self.obj327)
   self.obj327.graphObject_.pendingConnections.append((self.obj327.graphObject_.tag, self.obj323.graphObject_.tag, [300.0, 121.0, 264.75, 85.25], 2, 0))

   cobj0.RHS = ASG_pns(self)
   cobj0.RHS.merge(ASG_omacs(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj331=operatingUnit(self)
   self.obj331.preAction( cobj0.RHS.CREATE )
   self.obj331.isGraphObjectVisual = True

   if(hasattr(self.obj331, '_setHierarchicalLink')):
     self.obj331._setHierarchicalLink(False)

   # OperCostProp
   self.obj331.OperCostProp.setNone()

   # name
   self.obj331.name.setValue('')
   self.obj331.name.setNone()

   # OperCostFix
   self.obj331.OperCostFix.setNone()

   self.obj331.GGLabel.setValue(4)
   self.obj331.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(280.0,120.0,self.obj331)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj331.graphObject_ = new_obj
   self.obj3310= AttrCalc()
   self.obj3310.Copy=ATOM3Boolean()
   self.obj3310.Copy.setValue(('Copy from LHS', 0))
   self.obj3310.Copy.config = 0
   self.obj3310.Specify=ATOM3Constraint()
   self.obj3310.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'a = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) ).name.getValue()\nb = self.getMatched ( graphID , self.LHS.nodeWithLabel(2) ).name.getValue()\nreturn self.graphRewritingSystem.Dictag[ a ][b]\n\n'))
   self.obj331.GGset2Any['OperCostProp']= self.obj3310
   self.obj3311= AttrCalc()
   self.obj3311.Copy=ATOM3Boolean()
   self.obj3311.Copy.setValue(('Copy from LHS', 1))
   self.obj3311.Copy.config = 0
   self.obj3311.Specify=ATOM3Constraint()
   self.obj3311.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj331.GGset2Any['name']= self.obj3311
   self.obj3312= AttrCalc()
   self.obj3312.Copy=ATOM3Boolean()
   self.obj3312.Copy.setValue(('Copy from LHS', 0))
   self.obj3312.Copy.config = 0
   self.obj3312.Specify=ATOM3Constraint()
   self.obj3312.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj331.GGset2Any['OperCostFix']= self.obj3312

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj331)
   self.obj331.postAction( cobj0.RHS.CREATE )

   self.obj332=CapableOf(self)
   self.obj332.preAction( cobj0.RHS.CREATE )
   self.obj332.isGraphObjectVisual = True

   if(hasattr(self.obj332, '_setHierarchicalLink')):
     self.obj332._setHierarchicalLink(False)

   # rate
   self.obj332.rate.setNone()

   self.obj332.GGLabel.setValue(5)
   self.obj332.graphClass_= graph_CapableOf
   if self.genGraphics:
      new_obj = graph_CapableOf(160.5,121.5,self.obj332)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj332.graphObject_ = new_obj
   self.obj3320= AttrCalc()
   self.obj3320.Copy=ATOM3Boolean()
   self.obj3320.Copy.setValue(('Copy from LHS', 1))
   self.obj3320.Copy.config = 0
   self.obj3320.Specify=ATOM3Constraint()
   self.obj3320.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj332.GGset2Any['rate']= self.obj3320

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj332)
   self.obj332.postAction( cobj0.RHS.CREATE )

   self.obj333=Agent(self)
   self.obj333.preAction( cobj0.RHS.CREATE )
   self.obj333.isGraphObjectVisual = True

   if(hasattr(self.obj333, '_setHierarchicalLink')):
     self.obj333._setHierarchicalLink(False)

   # price
   self.obj333.price.setNone()

   # name
   self.obj333.name.setValue('')
   self.obj333.name.setNone()

   self.obj333.GGLabel.setValue(1)
   self.obj333.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(120.0,40.0,self.obj333)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj333.graphObject_ = new_obj
   self.obj3330= AttrCalc()
   self.obj3330.Copy=ATOM3Boolean()
   self.obj3330.Copy.setValue(('Copy from LHS', 1))
   self.obj3330.Copy.config = 0
   self.obj3330.Specify=ATOM3Constraint()
   self.obj3330.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj333.GGset2Any['price']= self.obj3330
   self.obj3331= AttrCalc()
   self.obj3331.Copy=ATOM3Boolean()
   self.obj3331.Copy.setValue(('Copy from LHS', 1))
   self.obj3331.Copy.config = 0
   self.obj3331.Specify=ATOM3Constraint()
   self.obj3331.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj333.GGset2Any['name']= self.obj3331

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj333)
   self.obj333.postAction( cobj0.RHS.CREATE )

   self.obj334=Role(self)
   self.obj334.preAction( cobj0.RHS.CREATE )
   self.obj334.isGraphObjectVisual = True

   if(hasattr(self.obj334, '_setHierarchicalLink')):
     self.obj334._setHierarchicalLink(False)

   # name
   self.obj334.name.setValue('')
   self.obj334.name.setNone()

   self.obj334.GGLabel.setValue(2)
   self.obj334.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(140.0,140.0,self.obj334)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj334.graphObject_ = new_obj
   self.obj3340= AttrCalc()
   self.obj3340.Copy=ATOM3Boolean()
   self.obj3340.Copy.setValue(('Copy from LHS', 1))
   self.obj3340.Copy.config = 0
   self.obj3340.Specify=ATOM3Constraint()
   self.obj3340.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj334.GGset2Any['name']= self.obj3340

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj334)
   self.obj334.postAction( cobj0.RHS.CREATE )

   self.obj335=GenericGraphEdge(self)
   self.obj335.preAction( cobj0.RHS.CREATE )
   self.obj335.isGraphObjectVisual = True

   if(hasattr(self.obj335, '_setHierarchicalLink')):
     self.obj335._setHierarchicalLink(False)

   self.obj335.GGLabel.setValue(3)
   self.obj335.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(264.75,85.25,self.obj335)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj335.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj335)
   self.obj335.postAction( cobj0.RHS.CREATE )

   self.obj332.out_connections_.append(self.obj334)
   self.obj334.in_connections_.append(self.obj332)
   self.obj332.graphObject_.pendingConnections.append((self.obj332.graphObject_.tag, self.obj334.graphObject_.tag, [171.0, 140.0, 160.5, 121.5], 2, 0))
   self.obj333.out_connections_.append(self.obj335)
   self.obj335.in_connections_.append(self.obj333)
   self.obj333.graphObject_.pendingConnections.append((self.obj333.graphObject_.tag, self.obj335.graphObject_.tag, [157.0, 102.0, 264.75, 85.25], 2, 0))
   self.obj333.out_connections_.append(self.obj332)
   self.obj332.in_connections_.append(self.obj333)
   self.obj333.graphObject_.pendingConnections.append((self.obj333.graphObject_.tag, self.obj332.graphObject_.tag, [157.0, 102.0, 160.5, 121.5], 2, 0))
   self.obj335.out_connections_.append(self.obj331)
   self.obj331.in_connections_.append(self.obj335)
   self.obj335.graphObject_.pendingConnections.append((self.obj335.graphObject_.tag, self.obj331.graphObject_.tag, [300.0, 121.0, 264.75, 85.25], 2, 0))

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

   self.obj342=metarial(self)
   self.obj342.preAction( cobj0.LHS.CREATE )
   self.obj342.isGraphObjectVisual = True

   if(hasattr(self.obj342, '_setHierarchicalLink')):
     self.obj342._setHierarchicalLink(False)

   # MaxFlow
   self.obj342.MaxFlow.setNone()

   # price
   self.obj342.price.setValue(0)

   # Name
   self.obj342.Name.setValue('')
   self.obj342.Name.setNone()

   # ReqFlow
   self.obj342.ReqFlow.setNone()

   self.obj342.GGLabel.setValue(1)
   self.obj342.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(280.0,60.0,self.obj342)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj342.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj342)
   self.obj342.postAction( cobj0.LHS.CREATE )

   self.obj343=Goal(self)
   self.obj343.preAction( cobj0.LHS.CREATE )
   self.obj343.isGraphObjectVisual = True

   if(hasattr(self.obj343, '_setHierarchicalLink')):
     self.obj343._setHierarchicalLink(False)

   # name
   self.obj343.name.setValue('')
   self.obj343.name.setNone()

   self.obj343.GGLabel.setValue(3)
   self.obj343.graphClass_= graph_Goal
   if self.genGraphics:
      new_obj = graph_Goal(100.0,60.0,self.obj343)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj343.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj343)
   self.obj343.postAction( cobj0.LHS.CREATE )

   self.obj344=GenericGraphEdge(self)
   self.obj344.preAction( cobj0.LHS.CREATE )
   self.obj344.isGraphObjectVisual = True

   if(hasattr(self.obj344, '_setHierarchicalLink')):
     self.obj344._setHierarchicalLink(False)

   self.obj344.GGLabel.setValue(4)
   self.obj344.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(205.0,106.0,self.obj344)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj344.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj344)
   self.obj344.postAction( cobj0.LHS.CREATE )

   self.obj343.out_connections_.append(self.obj344)
   self.obj344.in_connections_.append(self.obj343)
   self.obj343.graphObject_.pendingConnections.append((self.obj343.graphObject_.tag, self.obj344.graphObject_.tag, [124.0, 110.0, 205.0, 106.0], 0, True))
   self.obj344.out_connections_.append(self.obj342)
   self.obj342.in_connections_.append(self.obj344)
   self.obj344.graphObject_.pendingConnections.append((self.obj344.graphObject_.tag, self.obj342.graphObject_.tag, [286.0, 102.0, 205.0, 106.0], 0, True))

   cobj0.RHS = ASG_pns(self)

   self.obj346=metarial(self)
   self.obj346.preAction( cobj0.RHS.CREATE )
   self.obj346.isGraphObjectVisual = True

   if(hasattr(self.obj346, '_setHierarchicalLink')):
     self.obj346._setHierarchicalLink(False)

   # MaxFlow
   self.obj346.MaxFlow.setNone()

   # price
   self.obj346.price.setValue(0)

   # Name
   self.obj346.Name.setValue('')
   self.obj346.Name.setNone()

   # ReqFlow
   self.obj346.ReqFlow.setNone()

   self.obj346.GGLabel.setValue(1)
   self.obj346.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(180.0,40.0,self.obj346)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj346.graphObject_ = new_obj
   self.obj3460= AttrCalc()
   self.obj3460.Copy=ATOM3Boolean()
   self.obj3460.Copy.setValue(('Copy from LHS', 1))
   self.obj3460.Copy.config = 0
   self.obj3460.Specify=ATOM3Constraint()
   self.obj3460.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj346.GGset2Any['MaxFlow']= self.obj3460
   self.obj3461= AttrCalc()
   self.obj3461.Copy=ATOM3Boolean()
   self.obj3461.Copy.setValue(('Copy from LHS', 1))
   self.obj3461.Copy.config = 0
   self.obj3461.Specify=ATOM3Constraint()
   self.obj3461.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj346.GGset2Any['Name']= self.obj3461
   self.obj3462= AttrCalc()
   self.obj3462.Copy=ATOM3Boolean()
   self.obj3462.Copy.setValue(('Copy from LHS', 1))
   self.obj3462.Copy.config = 0
   self.obj3462.Specify=ATOM3Constraint()
   self.obj3462.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj346.GGset2Any['ReqFlow']= self.obj3462

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj346)
   self.obj346.postAction( cobj0.RHS.CREATE )


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

   self.obj353=rawMaterial(self)
   self.obj353.preAction( cobj0.LHS.CREATE )
   self.obj353.isGraphObjectVisual = True

   if(hasattr(self.obj353, '_setHierarchicalLink')):
     self.obj353._setHierarchicalLink(False)

   # MaxFlow
   self.obj353.MaxFlow.setNone()

   # price
   self.obj353.price.setNone()

   # Name
   self.obj353.Name.setValue('')
   self.obj353.Name.setNone()

   # ReqFlow
   self.obj353.ReqFlow.setNone()

   self.obj353.GGLabel.setValue(2)
   self.obj353.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(260.0,40.0,self.obj353)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj353.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj353)
   self.obj353.postAction( cobj0.LHS.CREATE )

   self.obj354=operatingUnit(self)
   self.obj354.preAction( cobj0.LHS.CREATE )
   self.obj354.isGraphObjectVisual = True

   if(hasattr(self.obj354, '_setHierarchicalLink')):
     self.obj354._setHierarchicalLink(False)

   # OperCostProp
   self.obj354.OperCostProp.setNone()

   # name
   self.obj354.name.setValue('')
   self.obj354.name.setNone()

   # OperCostFix
   self.obj354.OperCostFix.setNone()

   self.obj354.GGLabel.setValue(3)
   self.obj354.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(280.0,140.0,self.obj354)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj354.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj354)
   self.obj354.postAction( cobj0.LHS.CREATE )

   self.obj355=fromRaw(self)
   self.obj355.preAction( cobj0.LHS.CREATE )
   self.obj355.isGraphObjectVisual = True

   if(hasattr(self.obj355, '_setHierarchicalLink')):
     self.obj355._setHierarchicalLink(False)

   # rate
   self.obj355.rate.setNone()

   self.obj355.GGLabel.setValue(5)
   self.obj355.graphClass_= graph_fromRaw
   if self.genGraphics:
      new_obj = graph_fromRaw(292.0,123.5,self.obj355)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj355.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj355)
   self.obj355.postAction( cobj0.LHS.CREATE )

   self.obj356=Agent(self)
   self.obj356.preAction( cobj0.LHS.CREATE )
   self.obj356.isGraphObjectVisual = True

   if(hasattr(self.obj356, '_setHierarchicalLink')):
     self.obj356._setHierarchicalLink(False)

   # price
   self.obj356.price.setNone()

   # name
   self.obj356.name.setValue('')
   self.obj356.name.setNone()

   self.obj356.GGLabel.setValue(1)
   self.obj356.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(60.0,60.0,self.obj356)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj356.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj356)
   self.obj356.postAction( cobj0.LHS.CREATE )

   self.obj357=GenericGraphEdge(self)
   self.obj357.preAction( cobj0.LHS.CREATE )
   self.obj357.isGraphObjectVisual = True

   if(hasattr(self.obj357, '_setHierarchicalLink')):
     self.obj357._setHierarchicalLink(False)

   self.obj357.GGLabel.setValue(4)
   self.obj357.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(184.5,109.0,self.obj357)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj357.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj357)
   self.obj357.postAction( cobj0.LHS.CREATE )

   self.obj358=GenericGraphEdge(self)
   self.obj358.preAction( cobj0.LHS.CREATE )
   self.obj358.isGraphObjectVisual = True

   if(hasattr(self.obj358, '_setHierarchicalLink')):
     self.obj358._setHierarchicalLink(False)

   self.obj358.GGLabel.setValue(6)
   self.obj358.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(159.0,150.5,self.obj358)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj358.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj358)
   self.obj358.postAction( cobj0.LHS.CREATE )

   self.obj353.out_connections_.append(self.obj355)
   self.obj355.in_connections_.append(self.obj353)
   self.obj353.graphObject_.pendingConnections.append((self.obj353.graphObject_.tag, self.obj355.graphObject_.tag, [284.0, 96.0, 292.0, 123.5], 0, True))
   self.obj355.out_connections_.append(self.obj354)
   self.obj354.in_connections_.append(self.obj355)
   self.obj355.graphObject_.pendingConnections.append((self.obj355.graphObject_.tag, self.obj354.graphObject_.tag, [300.0, 151.0, 292.0, 123.5], 0, True))
   self.obj356.out_connections_.append(self.obj357)
   self.obj357.in_connections_.append(self.obj356)
   self.obj356.graphObject_.pendingConnections.append((self.obj356.graphObject_.tag, self.obj357.graphObject_.tag, [85.0, 122.0, 184.5, 109.0], 0, True))
   self.obj356.out_connections_.append(self.obj358)
   self.obj358.in_connections_.append(self.obj356)
   self.obj356.graphObject_.pendingConnections.append((self.obj356.graphObject_.tag, self.obj358.graphObject_.tag, [85.0, 122.0, 105.5, 141.5, 159.0, 150.5], 2, True))
   self.obj357.out_connections_.append(self.obj353)
   self.obj353.in_connections_.append(self.obj357)
   self.obj357.graphObject_.pendingConnections.append((self.obj357.graphObject_.tag, self.obj353.graphObject_.tag, [284.0, 96.0, 184.5, 109.0], 0, True))
   self.obj358.out_connections_.append(self.obj354)
   self.obj354.in_connections_.append(self.obj358)
   self.obj358.graphObject_.pendingConnections.append((self.obj358.graphObject_.tag, self.obj354.graphObject_.tag, [299.0, 158.0, 212.5, 159.5, 159.0, 150.5], 2, True))

   cobj0.RHS = ASG_pns(self)

   self.obj360=rawMaterial(self)
   self.obj360.preAction( cobj0.RHS.CREATE )
   self.obj360.isGraphObjectVisual = True

   if(hasattr(self.obj360, '_setHierarchicalLink')):
     self.obj360._setHierarchicalLink(False)

   # MaxFlow
   self.obj360.MaxFlow.setValue(999999)

   # price
   self.obj360.price.setValue(0)

   # Name
   self.obj360.Name.setValue('')
   self.obj360.Name.setNone()

   # ReqFlow
   self.obj360.ReqFlow.setValue(0)

   self.obj360.GGLabel.setValue(2)
   self.obj360.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(160.0,40.0,self.obj360)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['Text Scale'] = 1.0
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj360.graphObject_ = new_obj
   self.obj3600= AttrCalc()
   self.obj3600.Copy=ATOM3Boolean()
   self.obj3600.Copy.setValue(('Copy from LHS', 1))
   self.obj3600.Copy.config = 0
   self.obj3600.Specify=ATOM3Constraint()
   self.obj3600.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj360.GGset2Any['MaxFlow']= self.obj3600
   self.obj3601= AttrCalc()
   self.obj3601.Copy=ATOM3Boolean()
   self.obj3601.Copy.setValue(('Copy from LHS', 0))
   self.obj3601.Copy.config = 0
   self.obj3601.Specify=ATOM3Constraint()
   self.obj3601.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).price.getValue()\n'))
   self.obj360.GGset2Any['price']= self.obj3601
   self.obj3602= AttrCalc()
   self.obj3602.Copy=ATOM3Boolean()
   self.obj3602.Copy.setValue(('Copy from LHS', 1))
   self.obj3602.Copy.config = 0
   self.obj3602.Specify=ATOM3Constraint()
   self.obj3602.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj360.GGset2Any['Name']= self.obj3602
   self.obj3603= AttrCalc()
   self.obj3603.Copy=ATOM3Boolean()
   self.obj3603.Copy.setValue(('Copy from LHS', 1))
   self.obj3603.Copy.config = 0
   self.obj3603.Specify=ATOM3Constraint()
   self.obj3603.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj360.GGset2Any['ReqFlow']= self.obj3603

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj360)
   self.obj360.postAction( cobj0.RHS.CREATE )

   self.obj361=operatingUnit(self)
   self.obj361.preAction( cobj0.RHS.CREATE )
   self.obj361.isGraphObjectVisual = True

   if(hasattr(self.obj361, '_setHierarchicalLink')):
     self.obj361._setHierarchicalLink(False)

   # OperCostProp
   self.obj361.OperCostProp.setValue(0.0)

   # name
   self.obj361.name.setValue('')
   self.obj361.name.setNone()

   # OperCostFix
   self.obj361.OperCostFix.setValue(0.0)

   self.obj361.GGLabel.setValue(3)
   self.obj361.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(120.0,160.0,self.obj361)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj361.graphObject_ = new_obj
   self.obj3610= AttrCalc()
   self.obj3610.Copy=ATOM3Boolean()
   self.obj3610.Copy.setValue(('Copy from LHS', 1))
   self.obj3610.Copy.config = 0
   self.obj3610.Specify=ATOM3Constraint()
   self.obj3610.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj361.GGset2Any['OperCostProp']= self.obj3610
   self.obj3611= AttrCalc()
   self.obj3611.Copy=ATOM3Boolean()
   self.obj3611.Copy.setValue(('Copy from LHS', 1))
   self.obj3611.Copy.config = 0
   self.obj3611.Specify=ATOM3Constraint()
   self.obj3611.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj361.GGset2Any['name']= self.obj3611
   self.obj3612= AttrCalc()
   self.obj3612.Copy=ATOM3Boolean()
   self.obj3612.Copy.setValue(('Copy from LHS', 1))
   self.obj3612.Copy.config = 0
   self.obj3612.Specify=ATOM3Constraint()
   self.obj3612.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj361.GGset2Any['OperCostFix']= self.obj3612

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj361)
   self.obj361.postAction( cobj0.RHS.CREATE )

   self.obj362=fromRaw(self)
   self.obj362.preAction( cobj0.RHS.CREATE )
   self.obj362.isGraphObjectVisual = True

   if(hasattr(self.obj362, '_setHierarchicalLink')):
     self.obj362._setHierarchicalLink(False)

   # rate
   self.obj362.rate.setValue(0.0)

   self.obj362.GGLabel.setValue(5)
   self.obj362.graphClass_= graph_fromRaw
   if self.genGraphics:
      new_obj = graph_fromRaw(177.0,133.5,self.obj362)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj362.graphObject_ = new_obj
   self.obj3620= AttrCalc()
   self.obj3620.Copy=ATOM3Boolean()
   self.obj3620.Copy.setValue(('Copy from LHS', 1))
   self.obj3620.Copy.config = 0
   self.obj3620.Specify=ATOM3Constraint()
   self.obj3620.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj362.GGset2Any['rate']= self.obj3620

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj362)
   self.obj362.postAction( cobj0.RHS.CREATE )

   self.obj360.out_connections_.append(self.obj362)
   self.obj362.in_connections_.append(self.obj360)
   self.obj360.graphObject_.pendingConnections.append((self.obj360.graphObject_.tag, self.obj362.graphObject_.tag, [184.0, 96.0, 177.0, 133.5], 0, True))
   self.obj362.out_connections_.append(self.obj361)
   self.obj361.in_connections_.append(self.obj362)
   self.obj362.graphObject_.pendingConnections.append((self.obj362.graphObject_.tag, self.obj361.graphObject_.tag, [170.0, 171.0, 177.0, 133.5], 0, True))

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

   self.obj368=Capabilitie(self)
   self.obj368.preAction( cobj0.LHS.CREATE )
   self.obj368.isGraphObjectVisual = True

   if(hasattr(self.obj368, '_setHierarchicalLink')):
     self.obj368._setHierarchicalLink(False)

   # name
   self.obj368.name.setValue('')
   self.obj368.name.setNone()

   self.obj368.GGLabel.setValue(1)
   self.obj368.graphClass_= graph_Capabilitie
   if self.genGraphics:
      new_obj = graph_Capabilitie(220.0,80.0,self.obj368)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj368.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj368)
   self.obj368.postAction( cobj0.LHS.CREATE )


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

   self.obj376=metarial(self)
   self.obj376.preAction( cobj0.LHS.CREATE )
   self.obj376.isGraphObjectVisual = True

   if(hasattr(self.obj376, '_setHierarchicalLink')):
     self.obj376._setHierarchicalLink(False)

   # MaxFlow
   self.obj376.MaxFlow.setNone()

   # price
   self.obj376.price.setValue(0)

   # Name
   self.obj376.Name.setValue('')
   self.obj376.Name.setNone()

   # ReqFlow
   self.obj376.ReqFlow.setNone()

   self.obj376.GGLabel.setValue(2)
   self.obj376.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(280.0,40.0,self.obj376)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj376.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj376)
   self.obj376.postAction( cobj0.LHS.CREATE )

   self.obj377=operatingUnit(self)
   self.obj377.preAction( cobj0.LHS.CREATE )
   self.obj377.isGraphObjectVisual = True

   if(hasattr(self.obj377, '_setHierarchicalLink')):
     self.obj377._setHierarchicalLink(False)

   # OperCostProp
   self.obj377.OperCostProp.setNone()

   # name
   self.obj377.name.setValue('')
   self.obj377.name.setNone()

   # OperCostFix
   self.obj377.OperCostFix.setNone()

   self.obj377.GGLabel.setValue(3)
   self.obj377.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(300.0,140.0,self.obj377)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj377.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj377)
   self.obj377.postAction( cobj0.LHS.CREATE )

   self.obj378=fromMaterial(self)
   self.obj378.preAction( cobj0.LHS.CREATE )
   self.obj378.isGraphObjectVisual = True

   if(hasattr(self.obj378, '_setHierarchicalLink')):
     self.obj378._setHierarchicalLink(False)

   # rate
   self.obj378.rate.setNone()

   self.obj378.GGLabel.setValue(4)
   self.obj378.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(342.75,113.75,self.obj378)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj378.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj378)
   self.obj378.postAction( cobj0.LHS.CREATE )

   self.obj379=Role(self)
   self.obj379.preAction( cobj0.LHS.CREATE )
   self.obj379.isGraphObjectVisual = True

   if(hasattr(self.obj379, '_setHierarchicalLink')):
     self.obj379._setHierarchicalLink(False)

   # name
   self.obj379.name.setValue('')
   self.obj379.name.setNone()

   self.obj379.GGLabel.setValue(1)
   self.obj379.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(80.0,60.0,self.obj379)
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

   self.obj380.GGLabel.setValue(5)
   self.obj380.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(195.0,71.5,self.obj380)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj380.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj380)
   self.obj380.postAction( cobj0.LHS.CREATE )

   self.obj376.out_connections_.append(self.obj378)
   self.obj378.in_connections_.append(self.obj376)
   self.obj376.graphObject_.pendingConnections.append((self.obj376.graphObject_.tag, self.obj378.graphObject_.tag, [321.0, 82.0, 335.5, 96.5, 342.75, 113.75], 2, True))
   self.obj378.out_connections_.append(self.obj377)
   self.obj377.in_connections_.append(self.obj378)
   self.obj378.graphObject_.pendingConnections.append((self.obj378.graphObject_.tag, self.obj377.graphObject_.tag, [350.0, 151.0, 350.0, 131.0, 342.75, 113.75], 2, True))
   self.obj379.out_connections_.append(self.obj380)
   self.obj380.in_connections_.append(self.obj379)
   self.obj379.graphObject_.pendingConnections.append((self.obj379.graphObject_.tag, self.obj380.graphObject_.tag, [104.0, 61.0, 195.0, 71.5], 0, True))
   self.obj380.out_connections_.append(self.obj376)
   self.obj376.in_connections_.append(self.obj380)
   self.obj380.graphObject_.pendingConnections.append((self.obj380.graphObject_.tag, self.obj376.graphObject_.tag, [286.0, 82.0, 195.0, 71.5], 0, True))

   cobj0.RHS = ASG_pns(self)

   self.obj382=metarial(self)
   self.obj382.preAction( cobj0.RHS.CREATE )
   self.obj382.isGraphObjectVisual = True

   if(hasattr(self.obj382, '_setHierarchicalLink')):
     self.obj382._setHierarchicalLink(False)

   # MaxFlow
   self.obj382.MaxFlow.setValue(999999)

   # price
   self.obj382.price.setValue(0)

   # Name
   self.obj382.Name.setValue('')
   self.obj382.Name.setNone()

   # ReqFlow
   self.obj382.ReqFlow.setValue(0)

   self.obj382.GGLabel.setValue(2)
   self.obj382.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(160.0,40.0,self.obj382)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj382.graphObject_ = new_obj
   self.obj3820= AttrCalc()
   self.obj3820.Copy=ATOM3Boolean()
   self.obj3820.Copy.setValue(('Copy from LHS', 1))
   self.obj3820.Copy.config = 0
   self.obj3820.Specify=ATOM3Constraint()
   self.obj3820.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj382.GGset2Any['MaxFlow']= self.obj3820
   self.obj3821= AttrCalc()
   self.obj3821.Copy=ATOM3Boolean()
   self.obj3821.Copy.setValue(('Copy from LHS', 1))
   self.obj3821.Copy.config = 0
   self.obj3821.Specify=ATOM3Constraint()
   self.obj3821.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj382.GGset2Any['Name']= self.obj3821
   self.obj3822= AttrCalc()
   self.obj3822.Copy=ATOM3Boolean()
   self.obj3822.Copy.setValue(('Copy from LHS', 1))
   self.obj3822.Copy.config = 0
   self.obj3822.Specify=ATOM3Constraint()
   self.obj3822.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj382.GGset2Any['ReqFlow']= self.obj3822

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj382)
   self.obj382.postAction( cobj0.RHS.CREATE )

   self.obj383=operatingUnit(self)
   self.obj383.preAction( cobj0.RHS.CREATE )
   self.obj383.isGraphObjectVisual = True

   if(hasattr(self.obj383, '_setHierarchicalLink')):
     self.obj383._setHierarchicalLink(False)

   # OperCostProp
   self.obj383.OperCostProp.setValue(0.0)

   # name
   self.obj383.name.setValue('')
   self.obj383.name.setNone()

   # OperCostFix
   self.obj383.OperCostFix.setValue(0.0)

   self.obj383.GGLabel.setValue(3)
   self.obj383.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(200.0,140.0,self.obj383)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj383.graphObject_ = new_obj
   self.obj3830= AttrCalc()
   self.obj3830.Copy=ATOM3Boolean()
   self.obj3830.Copy.setValue(('Copy from LHS', 1))
   self.obj3830.Copy.config = 0
   self.obj3830.Specify=ATOM3Constraint()
   self.obj3830.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj383.GGset2Any['OperCostProp']= self.obj3830
   self.obj3831= AttrCalc()
   self.obj3831.Copy=ATOM3Boolean()
   self.obj3831.Copy.setValue(('Copy from LHS', 1))
   self.obj3831.Copy.config = 0
   self.obj3831.Specify=ATOM3Constraint()
   self.obj3831.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj383.GGset2Any['name']= self.obj3831
   self.obj3832= AttrCalc()
   self.obj3832.Copy=ATOM3Boolean()
   self.obj3832.Copy.setValue(('Copy from LHS', 1))
   self.obj3832.Copy.config = 0
   self.obj3832.Specify=ATOM3Constraint()
   self.obj3832.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj383.GGset2Any['OperCostFix']= self.obj3832

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj383)
   self.obj383.postAction( cobj0.RHS.CREATE )

   self.obj384=fromMaterial(self)
   self.obj384.preAction( cobj0.RHS.CREATE )
   self.obj384.isGraphObjectVisual = True

   if(hasattr(self.obj384, '_setHierarchicalLink')):
     self.obj384._setHierarchicalLink(False)

   # rate
   self.obj384.rate.setValue(0.0)

   self.obj384.GGLabel.setValue(4)
   self.obj384.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(238.75,106.25,self.obj384)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj384.graphObject_ = new_obj
   self.obj3840= AttrCalc()
   self.obj3840.Copy=ATOM3Boolean()
   self.obj3840.Copy.setValue(('Copy from LHS', 1))
   self.obj3840.Copy.config = 0
   self.obj3840.Specify=ATOM3Constraint()
   self.obj3840.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj384.GGset2Any['rate']= self.obj3840

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj384)
   self.obj384.postAction( cobj0.RHS.CREATE )

   self.obj382.out_connections_.append(self.obj384)
   self.obj384.in_connections_.append(self.obj382)
   self.obj382.graphObject_.pendingConnections.append((self.obj382.graphObject_.tag, self.obj384.graphObject_.tag, [201.0, 82.0, 226.5, 89.0, 238.75, 106.25], 2, True))
   self.obj384.out_connections_.append(self.obj383)
   self.obj383.in_connections_.append(self.obj384)
   self.obj384.graphObject_.pendingConnections.append((self.obj384.graphObject_.tag, self.obj383.graphObject_.tag, [250.0, 151.0, 251.0, 123.5, 238.75, 106.25], 2, True))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.graphRewritingSystem.finalStat > 20 \n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   lcobj0.append(cobj0)
   self.EditingGraphGrammar.Rules.setValue(lcobj0)
   self.EditingGraphGrammar.InitialAction=ATOM3Constraint()
   self.EditingGraphGrammar.InitialAction.setValue(('constraint', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'print \'Version 1Hahaha \'\nself.rewritingSystem.finalStat = 0\nself.rewritingSystem.Dictag = {}\nself.rewritingSystem.Dictro = {}\nAgentDict = {}\nAgentDict2 = {}\nRoleDict = {} \nRoleDict2 = {} \nPosses  = {}\nAchiev = {}\natom3i = self.rewritingSystem.parent\nfor nodeType in atom3i.ASGroot.listNodes.keys():\n   for node in atom3i.ASGroot.listNodes[nodeType]:\n       if node.__class__.__name__ == \'Agent\' : \n           nodeName = node.name.getValue()\n           AgentDict[nodeName]={} \n           AgentDict2[nodeName]=[]\n           for link in node.out_connections_ : \n               if hasattr(link,\'rate\') :\n                   for nodes in link.out_connections_ :\n\n                      AgentDict[nodeName][nodes.name.getValue()]=link.rate.getValue()\n                      AgentDict2[nodeName].append(nodes.name.getValue())\n           #AgentDict[nodeName]= AgentDict[nodeName]/ len(node.out_connections_)\n       elif node.__class__.__name__ == \'Role\' :\n           nodeName = node.name.getValue()\n           RoleDict[nodeName]={} \n           RoleDict2[nodeName]=[]\n           lisst = RoleDict[nodeName]\n           for link in node.out_connections_ : \n               for nodes in link.out_connections_ :\n                   if hasattr(link,\'rate\'):        RoleDict[nodeName][nodes.name.getValue()]=link.rate.getValue()\n                   else :  RoleDict2[nodeName].append(nodes.name.getValue())\n\n                         #lisst.append( {nodes.name.getValue():link.rate.getValue()} ) \n           #RoleDict[nodeName] = lisst  \n\nprint \'[DicAG]Agent Dict for his Value  : \'+str(AgentDict)\nprint \'Agent dict 2 \'+str(AgentDict2)\nprint \'Role Dict for his Value  : \'+str(RoleDict)\nprint \'Role Dict2 for his Value  : \'+str(RoleDict2)\n # all these line new \nfor key , val in AgentDict2.items() :\n   val.sort()\nfor key , val in RoleDict2.items() :\n   val.sort()\nfor key , val in AgentDict2.items() :\n    for key2 , val2 in RoleDict2.items() :\n        v = \'\'.join(val)\n        v2 = \'\'.join(val2)\n        if  v2 in v : \n           s = 0\n           #print str(key) +\' Can Play \'+str(key2)\n           for i in val2 : \n               #if type(AgentDict[key]).__name__ != \'float\':\n               #print \'  \'+str(i)   \n               s+=AgentDict[key][i] \n           AgentDict[key][key2] = s/len(val2)\n           Posses[str(key)+\' \'+str(key2)]=s*len(val2) #Just Equation for the cost of OpUnit\n           print key + \' :\'+key2+\' Can Achiev \'+str(RoleDict[key2])\n\n           #print \'AgentDict : \'+str(AgentDict)	 \nfor key , val in AgentDict2.items() :\n     print str(key) +\' Rate \'+str( AgentDict[key] )		\n \nprint Posses\nself.rewritingSystem.Dictag = AgentDict\nself.rewritingSystem.Dictro = RoleDict\n##\n\n'))
   self.EditingGraphGrammar.FinalAction=ATOM3Constraint()
   self.EditingGraphGrammar.FinalAction.setValue(('const', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))


