from GraphGrammarEdit import *
from GGruleEdit import *

def savedTrans(self):
   self.EditingGraphGrammar= GraphGrammarEdit(None, self)
   self.EditingGraphGrammar.Name=ATOM3String('omacsGG', 20)
   self.EditingGraphGrammar.Rules=ATOM3List([ 1, 1, 1, 0],GGruleEdit,None, self)
   lcobj0=[]
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('Agent_RawM', 20)
   cobj0.Order=ATOM3Integer(1)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

   from Goal import *
   from ASG_omacs2 import *
   from Agent import *
   from Role import *
   from CapableToPlay import *
   from Achieve import *
   from from_init import *
   from Transition import *
   from Init_Stat import *
   from ASG_pns import *
   from into_inter import *
   from into_final import *
   from from_inter import *
   from GenericGraphEdge import *
   from Final_Stat import *
   from ASG_GenericGraph import *
   from Inter_Stat import *
   from GenericGraphNode import *

   cobj0.LHS = ASG_omacs2(self)

   self.obj128=Agent(self)
   self.obj128.preAction( cobj0.LHS.CREATE )
   self.obj128.isGraphObjectVisual = True

   if(hasattr(self.obj128, '_setHierarchicalLink')):
     self.obj128._setHierarchicalLink(False)

   # Price
   self.obj128.Price.setValue(0)

   # Name
   self.obj128.Name.setValue('')
   self.obj128.Name.setNone()

   # possesC
   self.obj128.possesC.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   self.obj128.possesC.setValue(lcobj2)

   self.obj128.GGLabel.setValue(1)
   self.obj128.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(180.0,20.0,self.obj128)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj128.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj128)
   self.obj128.postAction( cobj0.LHS.CREATE )

   self.obj129=Role(self)
   self.obj129.preAction( cobj0.LHS.CREATE )
   self.obj129.isGraphObjectVisual = True

   if(hasattr(self.obj129, '_setHierarchicalLink')):
     self.obj129._setHierarchicalLink(False)

   # requireC
   self.obj129.requireC.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   self.obj129.requireC.setValue(lcobj2)

   # Name
   self.obj129.Name.setValue('')
   self.obj129.Name.setNone()

   self.obj129.GGLabel.setValue(2)
   self.obj129.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(120.0,180.0,self.obj129)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj129.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj129)
   self.obj129.postAction( cobj0.LHS.CREATE )

   self.obj130=Role(self)
   self.obj130.preAction( cobj0.LHS.CREATE )
   self.obj130.isGraphObjectVisual = True

   if(hasattr(self.obj130, '_setHierarchicalLink')):
     self.obj130._setHierarchicalLink(False)

   # requireC
   self.obj130.requireC.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   self.obj130.requireC.setValue(lcobj2)

   # Name
   self.obj130.Name.setValue('')
   self.obj130.Name.setNone()

   self.obj130.GGLabel.setValue(3)
   self.obj130.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(300.0,180.0,self.obj130)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj130.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj130)
   self.obj130.postAction( cobj0.LHS.CREATE )

   self.obj131=CapableToPlay(self)
   self.obj131.preAction( cobj0.LHS.CREATE )
   self.obj131.isGraphObjectVisual = True

   if(hasattr(self.obj131, '_setHierarchicalLink')):
     self.obj131._setHierarchicalLink(False)

   self.obj131.GGLabel.setValue(4)
   self.obj131.graphClass_= graph_CapableToPlay
   if self.genGraphics:
      new_obj = graph_CapableToPlay(174.0,130.5,self.obj131)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj131.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj131)
   self.obj131.postAction( cobj0.LHS.CREATE )

   self.obj132=CapableToPlay(self)
   self.obj132.preAction( cobj0.LHS.CREATE )
   self.obj132.isGraphObjectVisual = True

   if(hasattr(self.obj132, '_setHierarchicalLink')):
     self.obj132._setHierarchicalLink(False)

   self.obj132.GGLabel.setValue(5)
   self.obj132.graphClass_= graph_CapableToPlay
   if self.genGraphics:
      new_obj = graph_CapableToPlay(284.0,131.5,self.obj132)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj132.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj132)
   self.obj132.postAction( cobj0.LHS.CREATE )

   self.obj128.out_connections_.append(self.obj131)
   self.obj131.in_connections_.append(self.obj128)
   self.obj128.graphObject_.pendingConnections.append((self.obj128.graphObject_.tag, self.obj131.graphObject_.tag, [193.0, 81.0, 174.0, 130.5], 0, True))
   self.obj128.out_connections_.append(self.obj132)
   self.obj132.in_connections_.append(self.obj128)
   self.obj128.graphObject_.pendingConnections.append((self.obj128.graphObject_.tag, self.obj132.graphObject_.tag, [233.0, 83.0, 284.0, 131.5], 0, True))
   self.obj131.out_connections_.append(self.obj129)
   self.obj129.in_connections_.append(self.obj131)
   self.obj131.graphObject_.pendingConnections.append((self.obj131.graphObject_.tag, self.obj129.graphObject_.tag, [155.0, 180.0, 174.0, 130.5], 0, True))
   self.obj132.out_connections_.append(self.obj130)
   self.obj130.in_connections_.append(self.obj132)
   self.obj132.graphObject_.pendingConnections.append((self.obj132.graphObject_.tag, self.obj130.graphObject_.tag, [335.0, 180.0, 284.0, 131.5], 0, True))

   cobj0.RHS = ASG_omacs2(self)
   cobj0.RHS.merge(ASG_pns(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj128=Agent(self)
   self.obj128.preAction( cobj0.RHS.CREATE )
   self.obj128.isGraphObjectVisual = True

   if(hasattr(self.obj128, '_setHierarchicalLink')):
     self.obj128._setHierarchicalLink(False)

   # Price
   self.obj128.Price.setValue(0)

   # Name
   self.obj128.Name.setValue('')
   self.obj128.Name.setNone()

   # possesC
   self.obj128.possesC.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   self.obj128.possesC.setValue(lcobj2)

   self.obj128.GGLabel.setValue(1)
   self.obj128.graphClass_= graph_Agent
   if self.genGraphics:
      new_obj = graph_Agent(180.0,20.0,self.obj128)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj128.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj128)
   self.obj128.postAction( cobj0.RHS.CREATE )

   self.obj129=Role(self)
   self.obj129.preAction( cobj0.RHS.CREATE )
   self.obj129.isGraphObjectVisual = True

   if(hasattr(self.obj129, '_setHierarchicalLink')):
     self.obj129._setHierarchicalLink(False)

   # requireC
   self.obj129.requireC.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   self.obj129.requireC.setValue(lcobj2)

   # Name
   self.obj129.Name.setValue('')
   self.obj129.Name.setNone()

   self.obj129.GGLabel.setValue(2)
   self.obj129.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(120.0,180.0,self.obj129)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj129.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj129)
   self.obj129.postAction( cobj0.RHS.CREATE )

   self.obj130=Role(self)
   self.obj130.preAction( cobj0.RHS.CREATE )
   self.obj130.isGraphObjectVisual = True

   if(hasattr(self.obj130, '_setHierarchicalLink')):
     self.obj130._setHierarchicalLink(False)

   # requireC
   self.obj130.requireC.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   self.obj130.requireC.setValue(lcobj2)

   # Name
   self.obj130.Name.setValue('')
   self.obj130.Name.setNone()

   self.obj130.GGLabel.setValue(3)
   self.obj130.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(300.0,180.0,self.obj130)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj130.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj130)
   self.obj130.postAction( cobj0.RHS.CREATE )

   self.obj131=CapableToPlay(self)
   self.obj131.preAction( cobj0.RHS.CREATE )
   self.obj131.isGraphObjectVisual = True

   if(hasattr(self.obj131, '_setHierarchicalLink')):
     self.obj131._setHierarchicalLink(False)

   self.obj131.GGLabel.setValue(4)
   self.obj131.graphClass_= graph_CapableToPlay
   if self.genGraphics:
      new_obj = graph_CapableToPlay(174.0,130.5,self.obj131)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj131.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj131)
   self.obj131.postAction( cobj0.RHS.CREATE )

   self.obj132=CapableToPlay(self)
   self.obj132.preAction( cobj0.RHS.CREATE )
   self.obj132.isGraphObjectVisual = True

   if(hasattr(self.obj132, '_setHierarchicalLink')):
     self.obj132._setHierarchicalLink(False)

   self.obj132.GGLabel.setValue(5)
   self.obj132.graphClass_= graph_CapableToPlay
   if self.genGraphics:
      new_obj = graph_CapableToPlay(284.0,131.5,self.obj132)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj132.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj132)
   self.obj132.postAction( cobj0.RHS.CREATE )

   self.obj146=Init_Stat(self)
   self.obj146.preAction( cobj0.RHS.CREATE )
   self.obj146.isGraphObjectVisual = True

   if(hasattr(self.obj146, '_setHierarchicalLink')):
     self.obj146._setHierarchicalLink(False)

   # Name
   self.obj146.Name.setValue('')
   self.obj146.Name.setNone()

   self.obj146.GGLabel.setValue(7)
   self.obj146.graphClass_= graph_Init_Stat
   if self.genGraphics:
      new_obj = graph_Init_Stat(380.0,20.0,self.obj146)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj146.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj146)
   self.obj146.postAction( cobj0.RHS.CREATE )

   self.obj151=GenericGraphEdge(self)
   self.obj151.preAction( cobj0.RHS.CREATE )
   self.obj151.isGraphObjectVisual = True

   if(hasattr(self.obj151, '_setHierarchicalLink')):
     self.obj151._setHierarchicalLink(False)

   self.obj151.GGLabel.setValue(8)
   self.obj151.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(320.0,74.5,self.obj151)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj151.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj151)
   self.obj151.postAction( cobj0.RHS.CREATE )

   self.obj128.out_connections_.append(self.obj131)
   self.obj131.in_connections_.append(self.obj128)
   self.obj128.graphObject_.pendingConnections.append((self.obj128.graphObject_.tag, self.obj131.graphObject_.tag, [195.0, 81.0, 174.0, 130.5], 2, 0))
   self.obj128.out_connections_.append(self.obj132)
   self.obj132.in_connections_.append(self.obj128)
   self.obj128.graphObject_.pendingConnections.append((self.obj128.graphObject_.tag, self.obj132.graphObject_.tag, [235.0, 83.0, 284.0, 131.5], 2, 0))
   self.obj128.out_connections_.append(self.obj151)
   self.obj151.in_connections_.append(self.obj128)
   self.obj128.graphObject_.pendingConnections.append((self.obj128.graphObject_.tag, self.obj151.graphObject_.tag, [235.0, 83.0, 320.0, 74.5], 0, True))
   self.obj131.out_connections_.append(self.obj129)
   self.obj129.in_connections_.append(self.obj131)
   self.obj131.graphObject_.pendingConnections.append((self.obj131.graphObject_.tag, self.obj129.graphObject_.tag, [157.0, 180.0, 174.0, 130.5], 2, 0))
   self.obj132.out_connections_.append(self.obj130)
   self.obj130.in_connections_.append(self.obj132)
   self.obj132.graphObject_.pendingConnections.append((self.obj132.graphObject_.tag, self.obj130.graphObject_.tag, [337.0, 180.0, 284.0, 131.5], 2, 0))
   self.obj151.out_connections_.append(self.obj146)
   self.obj146.in_connections_.append(self.obj151)
   self.obj151.graphObject_.pendingConnections.append((self.obj151.graphObject_.tag, self.obj146.graphObject_.tag, [405.0, 66.0, 320.0, 74.5], 0, True))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return 1\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   lcobj0.append(cobj0)
   self.EditingGraphGrammar.Rules.setValue(lcobj0)
   self.EditingGraphGrammar.InitialAction=ATOM3Constraint()
   self.EditingGraphGrammar.InitialAction.setValue(('constraint', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.EditingGraphGrammar.FinalAction=ATOM3Constraint()
   self.EditingGraphGrammar.FinalAction.setValue(('const', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))


