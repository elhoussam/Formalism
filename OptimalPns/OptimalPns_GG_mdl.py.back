from GraphGrammarEdit import *
from GGruleEdit import *

def savedTrans(self):
   self.EditingGraphGrammar= GraphGrammarEdit(None, self)
   self.EditingGraphGrammar.Name=ATOM3String('OptimalPNS', 20)
   self.EditingGraphGrammar.Rules=ATOM3List([ 1, 1, 1, 0],GGruleEdit,None, self)
   lcobj0=[]
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('ComputeSol', 20)
   cobj0.Order=ATOM3Integer(1)
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

   self.obj107=rawMaterial(self)
   self.obj107.preAction( cobj0.LHS.CREATE )
   self.obj107.isGraphObjectVisual = True

   if(hasattr(self.obj107, '_setHierarchicalLink')):
     self.obj107._setHierarchicalLink(False)

   # MaxFlow
   self.obj107.MaxFlow.setNone()

   # price
   self.obj107.price.setNone()

   # Name
   self.obj107.Name.setValue('')
   self.obj107.Name.setNone()

   # ReqFlow
   self.obj107.ReqFlow.setNone()

   self.obj107.GGLabel.setValue(1)
   self.obj107.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(60.0,20.0,self.obj107)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj107.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj107)
   self.obj107.postAction( cobj0.LHS.CREATE )

   self.obj108=metarial(self)
   self.obj108.preAction( cobj0.LHS.CREATE )
   self.obj108.isGraphObjectVisual = True

   if(hasattr(self.obj108, '_setHierarchicalLink')):
     self.obj108._setHierarchicalLink(False)

   # MaxFlow
   self.obj108.MaxFlow.setNone()

   # price
   self.obj108.price.setNone()

   # Name
   self.obj108.Name.setValue('')
   self.obj108.Name.setNone()

   # ReqFlow
   self.obj108.ReqFlow.setNone()

   self.obj108.GGLabel.setValue(4)
   self.obj108.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(360.0,160.0,self.obj108)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj108.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj108)
   self.obj108.postAction( cobj0.LHS.CREATE )

   self.obj109=operatingUnit(self)
   self.obj109.preAction( cobj0.LHS.CREATE )
   self.obj109.isGraphObjectVisual = True

   if(hasattr(self.obj109, '_setHierarchicalLink')):
     self.obj109._setHierarchicalLink(False)

   # OperCostProp
   self.obj109.OperCostProp.setNone()

   # name
   self.obj109.name.setValue('')
   self.obj109.name.setNone()

   # OperCostFix
   self.obj109.OperCostFix.setNone()

   self.obj109.GGLabel.setValue(2)
   self.obj109.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(180.0,120.0,self.obj109)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj109.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj109)
   self.obj109.postAction( cobj0.LHS.CREATE )

   self.obj110=fromRaw(self)
   self.obj110.preAction( cobj0.LHS.CREATE )
   self.obj110.isGraphObjectVisual = True

   if(hasattr(self.obj110, '_setHierarchicalLink')):
     self.obj110._setHierarchicalLink(False)

   # rate
   self.obj110.rate.setNone()

   self.obj110.GGLabel.setValue(3)
   self.obj110.graphClass_= graph_fromRaw
   if self.genGraphics:
      new_obj = graph_fromRaw(135.5,78.0,self.obj110)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj110.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj110)
   self.obj110.postAction( cobj0.LHS.CREATE )

   self.obj111=intoMaterial(self)
   self.obj111.preAction( cobj0.LHS.CREATE )
   self.obj111.isGraphObjectVisual = True

   if(hasattr(self.obj111, '_setHierarchicalLink')):
     self.obj111._setHierarchicalLink(False)

   # rate
   self.obj111.rate.setNone()

   self.obj111.GGLabel.setValue(5)
   self.obj111.graphClass_= graph_intoMaterial
   if self.genGraphics:
      new_obj = graph_intoMaterial(291.5,140.5,self.obj111)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj111.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj111)
   self.obj111.postAction( cobj0.LHS.CREATE )

   self.obj107.out_connections_.append(self.obj110)
   self.obj110.in_connections_.append(self.obj107)
   self.obj107.graphObject_.pendingConnections.append((self.obj107.graphObject_.tag, self.obj110.graphObject_.tag, [84.0, 76.0, 84.0, 118.0, 135.5, 78.0], 2, True))
   self.obj109.out_connections_.append(self.obj111)
   self.obj111.in_connections_.append(self.obj109)
   self.obj109.graphObject_.pendingConnections.append((self.obj109.graphObject_.tag, self.obj111.graphObject_.tag, [233.0, 138.0, 212.0, 177.0, 291.5, 140.5], 2, True))
   self.obj110.out_connections_.append(self.obj109)
   self.obj109.in_connections_.append(self.obj110)
   self.obj110.graphObject_.pendingConnections.append((self.obj110.graphObject_.tag, self.obj109.graphObject_.tag, [200.0, 131.0, 187.0, 38.0, 135.5, 78.0], 2, True))
   self.obj111.out_connections_.append(self.obj108)
   self.obj108.in_connections_.append(self.obj111)
   self.obj111.graphObject_.pendingConnections.append((self.obj111.graphObject_.tag, self.obj108.graphObject_.tag, [386.0, 158.0, 371.0, 104.0, 291.5, 140.5], 2, True))

   cobj0.RHS = ASG_pns(self)

   self.obj113=rawMaterial(self)
   self.obj113.preAction( cobj0.RHS.CREATE )
   self.obj113.isGraphObjectVisual = True

   if(hasattr(self.obj113, '_setHierarchicalLink')):
     self.obj113._setHierarchicalLink(False)

   # MaxFlow
   self.obj113.MaxFlow.setNone()

   # price
   self.obj113.price.setNone()

   # Name
   self.obj113.Name.setValue('')
   self.obj113.Name.setNone()

   # ReqFlow
   self.obj113.ReqFlow.setNone()

   self.obj113.GGLabel.setValue(1)
   self.obj113.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(60.0,20.0,self.obj113)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj113.graphObject_ = new_obj
   self.obj1130= AttrCalc()
   self.obj1130.Copy=ATOM3Boolean()
   self.obj1130.Copy.setValue(('Copy from LHS', 1))
   self.obj1130.Copy.config = 0
   self.obj1130.Specify=ATOM3Constraint()
   self.obj1130.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj113.GGset2Any['MaxFlow']= self.obj1130
   self.obj1131= AttrCalc()
   self.obj1131.Copy=ATOM3Boolean()
   self.obj1131.Copy.setValue(('Copy from LHS', 1))
   self.obj1131.Copy.config = 0
   self.obj1131.Specify=ATOM3Constraint()
   self.obj1131.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj113.GGset2Any['price']= self.obj1131
   self.obj1132= AttrCalc()
   self.obj1132.Copy=ATOM3Boolean()
   self.obj1132.Copy.setValue(('Copy from LHS', 1))
   self.obj1132.Copy.config = 0
   self.obj1132.Specify=ATOM3Constraint()
   self.obj1132.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj113.GGset2Any['Name']= self.obj1132
   self.obj1133= AttrCalc()
   self.obj1133.Copy=ATOM3Boolean()
   self.obj1133.Copy.setValue(('Copy from LHS', 1))
   self.obj1133.Copy.config = 0
   self.obj1133.Specify=ATOM3Constraint()
   self.obj1133.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj113.GGset2Any['ReqFlow']= self.obj1133

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj113)
   self.obj113.postAction( cobj0.RHS.CREATE )

   self.obj114=metarial(self)
   self.obj114.preAction( cobj0.RHS.CREATE )
   self.obj114.isGraphObjectVisual = True

   if(hasattr(self.obj114, '_setHierarchicalLink')):
     self.obj114._setHierarchicalLink(False)

   # MaxFlow
   self.obj114.MaxFlow.setNone()

   # price
   self.obj114.price.setNone()

   # Name
   self.obj114.Name.setValue('')
   self.obj114.Name.setNone()

   # ReqFlow
   self.obj114.ReqFlow.setNone()

   self.obj114.GGLabel.setValue(4)
   self.obj114.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(360.0,160.0,self.obj114)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj114.graphObject_ = new_obj
   self.obj1140= AttrCalc()
   self.obj1140.Copy=ATOM3Boolean()
   self.obj1140.Copy.setValue(('Copy from LHS', 1))
   self.obj1140.Copy.config = 0
   self.obj1140.Specify=ATOM3Constraint()
   self.obj1140.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj114.GGset2Any['MaxFlow']= self.obj1140
   self.obj1141= AttrCalc()
   self.obj1141.Copy=ATOM3Boolean()
   self.obj1141.Copy.setValue(('Copy from LHS', 1))
   self.obj1141.Copy.config = 0
   self.obj1141.Specify=ATOM3Constraint()
   self.obj1141.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj114.GGset2Any['price']= self.obj1141
   self.obj1142= AttrCalc()
   self.obj1142.Copy=ATOM3Boolean()
   self.obj1142.Copy.setValue(('Copy from LHS', 1))
   self.obj1142.Copy.config = 0
   self.obj1142.Specify=ATOM3Constraint()
   self.obj1142.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj114.GGset2Any['Name']= self.obj1142
   self.obj1143= AttrCalc()
   self.obj1143.Copy=ATOM3Boolean()
   self.obj1143.Copy.setValue(('Copy from LHS', 1))
   self.obj1143.Copy.config = 0
   self.obj1143.Specify=ATOM3Constraint()
   self.obj1143.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj114.GGset2Any['ReqFlow']= self.obj1143

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj114)
   self.obj114.postAction( cobj0.RHS.CREATE )

   self.obj115=operatingUnit(self)
   self.obj115.preAction( cobj0.RHS.CREATE )
   self.obj115.isGraphObjectVisual = True

   if(hasattr(self.obj115, '_setHierarchicalLink')):
     self.obj115._setHierarchicalLink(False)

   # OperCostProp
   self.obj115.OperCostProp.setNone()

   # name
   self.obj115.name.setValue('')
   self.obj115.name.setNone()

   # OperCostFix
   self.obj115.OperCostFix.setNone()

   self.obj115.GGLabel.setValue(2)
   self.obj115.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(160.0,100.0,self.obj115)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj115.graphObject_ = new_obj
   self.obj1150= AttrCalc()
   self.obj1150.Copy=ATOM3Boolean()
   self.obj1150.Copy.setValue(('Copy from LHS', 1))
   self.obj1150.Copy.config = 0
   self.obj1150.Specify=ATOM3Constraint()
   self.obj1150.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj115.GGset2Any['OperCostProp']= self.obj1150
   self.obj1151= AttrCalc()
   self.obj1151.Copy=ATOM3Boolean()
   self.obj1151.Copy.setValue(('Copy from LHS', 1))
   self.obj1151.Copy.config = 0
   self.obj1151.Specify=ATOM3Constraint()
   self.obj1151.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj115.GGset2Any['name']= self.obj1151
   self.obj1152= AttrCalc()
   self.obj1152.Copy=ATOM3Boolean()
   self.obj1152.Copy.setValue(('Copy from LHS', 1))
   self.obj1152.Copy.config = 0
   self.obj1152.Specify=ATOM3Constraint()
   self.obj1152.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj115.GGset2Any['OperCostFix']= self.obj1152

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj115)
   self.obj115.postAction( cobj0.RHS.CREATE )

   self.obj116=fromRaw(self)
   self.obj116.preAction( cobj0.RHS.CREATE )
   self.obj116.isGraphObjectVisual = True

   if(hasattr(self.obj116, '_setHierarchicalLink')):
     self.obj116._setHierarchicalLink(False)

   # rate
   self.obj116.rate.setNone()

   self.obj116.GGLabel.setValue(3)
   self.obj116.graphClass_= graph_fromRaw
   if self.genGraphics:
      new_obj = graph_fromRaw(135.5,78.0,self.obj116)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj116.graphObject_ = new_obj
   self.obj1160= AttrCalc()
   self.obj1160.Copy=ATOM3Boolean()
   self.obj1160.Copy.setValue(('Copy from LHS', 1))
   self.obj1160.Copy.config = 0
   self.obj1160.Specify=ATOM3Constraint()
   self.obj1160.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj116.GGset2Any['rate']= self.obj1160

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj116)
   self.obj116.postAction( cobj0.RHS.CREATE )

   self.obj117=intoMaterial(self)
   self.obj117.preAction( cobj0.RHS.CREATE )
   self.obj117.isGraphObjectVisual = True

   if(hasattr(self.obj117, '_setHierarchicalLink')):
     self.obj117._setHierarchicalLink(False)

   # rate
   self.obj117.rate.setNone()

   self.obj117.GGLabel.setValue(5)
   self.obj117.graphClass_= graph_intoMaterial
   if self.genGraphics:
      new_obj = graph_intoMaterial(291.5,140.5,self.obj117)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj117.graphObject_ = new_obj
   self.obj1170= AttrCalc()
   self.obj1170.Copy=ATOM3Boolean()
   self.obj1170.Copy.setValue(('Copy from LHS', 1))
   self.obj1170.Copy.config = 0
   self.obj1170.Specify=ATOM3Constraint()
   self.obj1170.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj117.GGset2Any['rate']= self.obj1170

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj117)
   self.obj117.postAction( cobj0.RHS.CREATE )

   self.obj113.out_connections_.append(self.obj116)
   self.obj116.in_connections_.append(self.obj113)
   self.obj113.graphObject_.pendingConnections.append((self.obj113.graphObject_.tag, self.obj116.graphObject_.tag, [84.0, 70.0, 135.5, 78.0], 2, 0))
   self.obj115.out_connections_.append(self.obj117)
   self.obj117.in_connections_.append(self.obj115)
   self.obj115.graphObject_.pendingConnections.append((self.obj115.graphObject_.tag, self.obj117.graphObject_.tag, [213.0, 108.0, 291.5, 140.5], 2, 0))
   self.obj116.out_connections_.append(self.obj115)
   self.obj115.in_connections_.append(self.obj116)
   self.obj116.graphObject_.pendingConnections.append((self.obj116.graphObject_.tag, self.obj115.graphObject_.tag, [210.0, 101.0, 135.5, 78.0], 2, 0))
   self.obj117.out_connections_.append(self.obj114)
   self.obj114.in_connections_.append(self.obj117)
   self.obj117.graphObject_.pendingConnections.append((self.obj117.graphObject_.tag, self.obj114.graphObject_.tag, [370.0, 165.0, 291.5, 140.5], 2, 0))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'agent = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nmat = self.getMatched(graphID, self.LHS.nodeWithLabel(4))\nop = self.getMatched(graphID, self.LHS.nodeWithLabel(2))\nreturn not ( hasattr(agent,"done") and hasattr(op,"done") and hasattr(mat,"done") )\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'import OptimalPNS_GG_exec \nagent = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nagent.done = 1 \nop = self.getMatched(graphID, self.LHS.nodeWithLabel(2))\nop.done = 1\nmat = self.getMatched(graphID, self.LHS.nodeWithLabel(4))\nmat.done = 1\n\nif not ( op.name.getValue() in  OptimalPNS_GG_exec.Agentdict.keys() ):\n OptimalPNS_GG_exec.Agentdict[ op.name.getValue() ]=0\nOptimalPNS_GG_exec.Agentdict[ op.name.getValue() ] += 1\nif not ( op.name.getValue() in  OptimalPNS_GG_exec.Agentnode.keys() ):\n OptimalPNS_GG_exec.Agentnode[ op.name.getValue()]=[]\nOptimalPNS_GG_exec.Agentnode[op.name.getValue()].append(OptimalPNS_GG_exec.ind)\nOptimalPNS_GG_exec.dictWord[OptimalPNS_GG_exec.ind]=mat.Name.getValue()\nOptimalPNS_GG_exec.ind+=1\n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('SeparateClasses', 20)
   cobj0.Order=ATOM3Integer(2)
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


   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.graphRewritingSystem.finalStat == 0\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# import needed packages\nimport OptimalPNS_GG_exec \nimport itertools\n# print our data Struct\nprint OptimalPNS_GG_exec.Agentdict\nprint OptimalPNS_GG_exec.Agentnode\nprint OptimalPNS_GG_exec.dictWord\nlocalcounter = 1\n# start extract information from data Struct\nfor key in OptimalPNS_GG_exec.Agentdict.keys() : \n listStuf = OptimalPNS_GG_exec.Agentnode[key]\n print key\n for L in range(1, len(listStuf)+1):\n  for subset in itertools.combinations(listStuf, L):\n   print(subset)\n   list2 = [] #list( subset )\n   for T in subset :\n    list2.append( OptimalPNS_GG_exec.dictWord[T] ) # remplate all keys with corresp node name\n   print str(localcounter)+":"+str(list2)\n   localcounter+=1 \nself.graphRewritingSystem.finalStat = 1 \n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('MarkOpUnit1', 20)
   cobj0.Order=ATOM3Integer(3)
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

   self.obj127=rawMaterial(self)
   self.obj127.preAction( cobj0.LHS.CREATE )
   self.obj127.isGraphObjectVisual = True

   if(hasattr(self.obj127, '_setHierarchicalLink')):
     self.obj127._setHierarchicalLink(False)

   # MaxFlow
   self.obj127.MaxFlow.setNone()

   # price
   self.obj127.price.setNone()

   # Name
   self.obj127.Name.setValue('')
   self.obj127.Name.setNone()

   # ReqFlow
   self.obj127.ReqFlow.setNone()

   self.obj127.GGLabel.setValue(1)
   self.obj127.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(40.0,20.0,self.obj127)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj127.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj127)
   self.obj127.postAction( cobj0.LHS.CREATE )

   self.obj128=metarial(self)
   self.obj128.preAction( cobj0.LHS.CREATE )
   self.obj128.isGraphObjectVisual = True

   if(hasattr(self.obj128, '_setHierarchicalLink')):
     self.obj128._setHierarchicalLink(False)

   # MaxFlow
   self.obj128.MaxFlow.setNone()

   # price
   self.obj128.price.setNone()

   # Name
   self.obj128.Name.setValue('')
   self.obj128.Name.setNone()

   # ReqFlow
   self.obj128.ReqFlow.setNone()

   self.obj128.GGLabel.setValue(3)
   self.obj128.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(360.0,140.0,self.obj128)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj128.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj128)
   self.obj128.postAction( cobj0.LHS.CREATE )

   self.obj129=operatingUnit(self)
   self.obj129.preAction( cobj0.LHS.CREATE )
   self.obj129.isGraphObjectVisual = True

   if(hasattr(self.obj129, '_setHierarchicalLink')):
     self.obj129._setHierarchicalLink(False)

   # OperCostProp
   self.obj129.OperCostProp.setNone()

   # name
   self.obj129.name.setValue('')
   self.obj129.name.setNone()

   # OperCostFix
   self.obj129.OperCostFix.setNone()

   self.obj129.GGLabel.setValue(2)
   self.obj129.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(180.0,100.0,self.obj129)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj129.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj129)
   self.obj129.postAction( cobj0.LHS.CREATE )

   self.obj130=fromRaw(self)
   self.obj130.preAction( cobj0.LHS.CREATE )
   self.obj130.isGraphObjectVisual = True

   if(hasattr(self.obj130, '_setHierarchicalLink')):
     self.obj130._setHierarchicalLink(False)

   # rate
   self.obj130.rate.setNone()

   self.obj130.GGLabel.setValue(4)
   self.obj130.graphClass_= graph_fromRaw
   if self.genGraphics:
      new_obj = graph_fromRaw(183.0,77.75,self.obj130)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj130.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj130)
   self.obj130.postAction( cobj0.LHS.CREATE )

   self.obj131=intoMaterial(self)
   self.obj131.preAction( cobj0.LHS.CREATE )
   self.obj131.isGraphObjectVisual = True

   if(hasattr(self.obj131, '_setHierarchicalLink')):
     self.obj131._setHierarchicalLink(False)

   # rate
   self.obj131.rate.setNone()

   self.obj131.GGLabel.setValue(5)
   self.obj131.graphClass_= graph_intoMaterial
   if self.genGraphics:
      new_obj = graph_intoMaterial(258.75,158.0,self.obj131)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj131.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj131)
   self.obj131.postAction( cobj0.LHS.CREATE )

   self.obj127.out_connections_.append(self.obj130)
   self.obj130.in_connections_.append(self.obj127)
   self.obj127.graphObject_.pendingConnections.append((self.obj127.graphObject_.tag, self.obj130.graphObject_.tag, [64.0, 76.0, 144.0, 69.0, 183.0, 77.75], 2, True))
   self.obj129.out_connections_.append(self.obj131)
   self.obj131.in_connections_.append(self.obj129)
   self.obj129.graphObject_.pendingConnections.append((self.obj129.graphObject_.tag, self.obj131.graphObject_.tag, [199.0, 118.0, 222.0, 142.0, 258.75, 158.0], 2, True))
   self.obj130.out_connections_.append(self.obj129)
   self.obj129.in_connections_.append(self.obj130)
   self.obj130.graphObject_.pendingConnections.append((self.obj130.graphObject_.tag, self.obj129.graphObject_.tag, [200.0, 111.0, 222.0, 86.5, 183.0, 77.75], 2, True))
   self.obj131.out_connections_.append(self.obj128)
   self.obj128.in_connections_.append(self.obj131)
   self.obj131.graphObject_.pendingConnections.append((self.obj131.graphObject_.tag, self.obj128.graphObject_.tag, [366.0, 182.0, 295.5, 174.0, 258.75, 158.0], 2, True))

   cobj0.RHS = ASG_pns(self)

   self.obj133=rawMaterial(self)
   self.obj133.preAction( cobj0.RHS.CREATE )
   self.obj133.isGraphObjectVisual = True

   if(hasattr(self.obj133, '_setHierarchicalLink')):
     self.obj133._setHierarchicalLink(False)

   # MaxFlow
   self.obj133.MaxFlow.setNone()

   # price
   self.obj133.price.setNone()

   # Name
   self.obj133.Name.setValue('')
   self.obj133.Name.setNone()

   # ReqFlow
   self.obj133.ReqFlow.setNone()

   self.obj133.GGLabel.setValue(1)
   self.obj133.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(40.0,20.0,self.obj133)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj133.graphObject_ = new_obj
   self.obj1330= AttrCalc()
   self.obj1330.Copy=ATOM3Boolean()
   self.obj1330.Copy.setValue(('Copy from LHS', 1))
   self.obj1330.Copy.config = 0
   self.obj1330.Specify=ATOM3Constraint()
   self.obj1330.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj133.GGset2Any['MaxFlow']= self.obj1330
   self.obj1331= AttrCalc()
   self.obj1331.Copy=ATOM3Boolean()
   self.obj1331.Copy.setValue(('Copy from LHS', 1))
   self.obj1331.Copy.config = 0
   self.obj1331.Specify=ATOM3Constraint()
   self.obj1331.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj133.GGset2Any['price']= self.obj1331
   self.obj1332= AttrCalc()
   self.obj1332.Copy=ATOM3Boolean()
   self.obj1332.Copy.setValue(('Copy from LHS', 1))
   self.obj1332.Copy.config = 0
   self.obj1332.Specify=ATOM3Constraint()
   self.obj1332.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj133.GGset2Any['Name']= self.obj1332
   self.obj1333= AttrCalc()
   self.obj1333.Copy=ATOM3Boolean()
   self.obj1333.Copy.setValue(('Copy from LHS', 1))
   self.obj1333.Copy.config = 0
   self.obj1333.Specify=ATOM3Constraint()
   self.obj1333.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj133.GGset2Any['ReqFlow']= self.obj1333

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj133)
   self.obj133.postAction( cobj0.RHS.CREATE )

   self.obj134=metarial(self)
   self.obj134.preAction( cobj0.RHS.CREATE )
   self.obj134.isGraphObjectVisual = True

   if(hasattr(self.obj134, '_setHierarchicalLink')):
     self.obj134._setHierarchicalLink(False)

   # MaxFlow
   self.obj134.MaxFlow.setNone()

   # price
   self.obj134.price.setNone()

   # Name
   self.obj134.Name.setValue('')
   self.obj134.Name.setNone()

   # ReqFlow
   self.obj134.ReqFlow.setNone()

   self.obj134.GGLabel.setValue(3)
   self.obj134.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(360.0,140.0,self.obj134)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj134.graphObject_ = new_obj
   self.obj1340= AttrCalc()
   self.obj1340.Copy=ATOM3Boolean()
   self.obj1340.Copy.setValue(('Copy from LHS', 1))
   self.obj1340.Copy.config = 0
   self.obj1340.Specify=ATOM3Constraint()
   self.obj1340.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj134.GGset2Any['MaxFlow']= self.obj1340
   self.obj1341= AttrCalc()
   self.obj1341.Copy=ATOM3Boolean()
   self.obj1341.Copy.setValue(('Copy from LHS', 1))
   self.obj1341.Copy.config = 0
   self.obj1341.Specify=ATOM3Constraint()
   self.obj1341.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj134.GGset2Any['price']= self.obj1341
   self.obj1342= AttrCalc()
   self.obj1342.Copy=ATOM3Boolean()
   self.obj1342.Copy.setValue(('Copy from LHS', 1))
   self.obj1342.Copy.config = 0
   self.obj1342.Specify=ATOM3Constraint()
   self.obj1342.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj134.GGset2Any['Name']= self.obj1342
   self.obj1343= AttrCalc()
   self.obj1343.Copy=ATOM3Boolean()
   self.obj1343.Copy.setValue(('Copy from LHS', 1))
   self.obj1343.Copy.config = 0
   self.obj1343.Specify=ATOM3Constraint()
   self.obj1343.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj134.GGset2Any['ReqFlow']= self.obj1343

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj134)
   self.obj134.postAction( cobj0.RHS.CREATE )

   self.obj135=operatingUnit(self)
   self.obj135.preAction( cobj0.RHS.CREATE )
   self.obj135.isGraphObjectVisual = True

   if(hasattr(self.obj135, '_setHierarchicalLink')):
     self.obj135._setHierarchicalLink(False)

   # OperCostProp
   self.obj135.OperCostProp.setNone()

   # name
   self.obj135.name.setValue('')
   self.obj135.name.setNone()

   # OperCostFix
   self.obj135.OperCostFix.setNone()

   self.obj135.GGLabel.setValue(2)
   self.obj135.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(180.0,100.0,self.obj135)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj135.graphObject_ = new_obj
   self.obj1350= AttrCalc()
   self.obj1350.Copy=ATOM3Boolean()
   self.obj1350.Copy.setValue(('Copy from LHS', 1))
   self.obj1350.Copy.config = 0
   self.obj1350.Specify=ATOM3Constraint()
   self.obj1350.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj135.GGset2Any['OperCostProp']= self.obj1350
   self.obj1351= AttrCalc()
   self.obj1351.Copy=ATOM3Boolean()
   self.obj1351.Copy.setValue(('Copy from LHS', 1))
   self.obj1351.Copy.config = 0
   self.obj1351.Specify=ATOM3Constraint()
   self.obj1351.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj135.GGset2Any['name']= self.obj1351
   self.obj1352= AttrCalc()
   self.obj1352.Copy=ATOM3Boolean()
   self.obj1352.Copy.setValue(('Copy from LHS', 1))
   self.obj1352.Copy.config = 0
   self.obj1352.Specify=ATOM3Constraint()
   self.obj1352.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj135.GGset2Any['OperCostFix']= self.obj1352

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj135)
   self.obj135.postAction( cobj0.RHS.CREATE )

   self.obj136=fromRaw(self)
   self.obj136.preAction( cobj0.RHS.CREATE )
   self.obj136.isGraphObjectVisual = True

   if(hasattr(self.obj136, '_setHierarchicalLink')):
     self.obj136._setHierarchicalLink(False)

   # rate
   self.obj136.rate.setNone()

   self.obj136.GGLabel.setValue(4)
   self.obj136.graphClass_= graph_fromRaw
   if self.genGraphics:
      new_obj = graph_fromRaw(183.0,77.75,self.obj136)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj136.graphObject_ = new_obj
   self.obj1360= AttrCalc()
   self.obj1360.Copy=ATOM3Boolean()
   self.obj1360.Copy.setValue(('Copy from LHS', 1))
   self.obj1360.Copy.config = 0
   self.obj1360.Specify=ATOM3Constraint()
   self.obj1360.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj136.GGset2Any['rate']= self.obj1360

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj136)
   self.obj136.postAction( cobj0.RHS.CREATE )

   self.obj137=intoMaterial(self)
   self.obj137.preAction( cobj0.RHS.CREATE )
   self.obj137.isGraphObjectVisual = True

   if(hasattr(self.obj137, '_setHierarchicalLink')):
     self.obj137._setHierarchicalLink(False)

   # rate
   self.obj137.rate.setNone()

   self.obj137.GGLabel.setValue(5)
   self.obj137.graphClass_= graph_intoMaterial
   if self.genGraphics:
      new_obj = graph_intoMaterial(258.75,158.0,self.obj137)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj137.graphObject_ = new_obj
   self.obj1370= AttrCalc()
   self.obj1370.Copy=ATOM3Boolean()
   self.obj1370.Copy.setValue(('Copy from LHS', 1))
   self.obj1370.Copy.config = 0
   self.obj1370.Specify=ATOM3Constraint()
   self.obj1370.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj137.GGset2Any['rate']= self.obj1370

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj137)
   self.obj137.postAction( cobj0.RHS.CREATE )

   self.obj133.out_connections_.append(self.obj136)
   self.obj136.in_connections_.append(self.obj133)
   self.obj133.graphObject_.pendingConnections.append((self.obj133.graphObject_.tag, self.obj136.graphObject_.tag, [64.0, 70.0, 183.0, 77.75], 2, 0))
   self.obj135.out_connections_.append(self.obj137)
   self.obj137.in_connections_.append(self.obj135)
   self.obj135.graphObject_.pendingConnections.append((self.obj135.graphObject_.tag, self.obj137.graphObject_.tag, [233.0, 108.0, 258.75, 158.0], 2, 0))
   self.obj136.out_connections_.append(self.obj135)
   self.obj135.in_connections_.append(self.obj136)
   self.obj136.graphObject_.pendingConnections.append((self.obj136.graphObject_.tag, self.obj135.graphObject_.tag, [230.0, 101.0, 183.0, 77.75], 2, 0))
   self.obj137.out_connections_.append(self.obj134)
   self.obj134.in_connections_.append(self.obj137)
   self.obj137.graphObject_.pendingConnections.append((self.obj137.graphObject_.tag, self.obj134.graphObject_.tag, [366.0, 182.0, 258.75, 158.0], 2, 0))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'opUnit = self.getMatched(graphID, self.LHS.nodeWithLabel(2)) \nreturn not ( hasattr(opUnit,"rat") )\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'input = self.getMatched(graphID, self.LHS.nodeWithLabel(4))\noutput = self.getMatched(graphID, self.LHS.nodeWithLabel(5))\n\nop = self.getMatched(graphID, self.LHS.nodeWithLabel(2))\nop.rat = input.rate.getValue()/output.rate.getValue()\nprint op.name.getValue()+":"+str(op.rat)\n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('MarkOpUnit2', 20)
   cobj0.Order=ATOM3Integer(5)
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

   self.obj142=metarial(self)
   self.obj142.preAction( cobj0.LHS.CREATE )
   self.obj142.isGraphObjectVisual = True

   if(hasattr(self.obj142, '_setHierarchicalLink')):
     self.obj142._setHierarchicalLink(False)

   # MaxFlow
   self.obj142.MaxFlow.setNone()

   # price
   self.obj142.price.setNone()

   # Name
   self.obj142.Name.setValue('')
   self.obj142.Name.setNone()

   # ReqFlow
   self.obj142.ReqFlow.setNone()

   self.obj142.GGLabel.setValue(1)
   self.obj142.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(40.0,40.0,self.obj142)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj142.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj142)
   self.obj142.postAction( cobj0.LHS.CREATE )

   self.obj143=metarial(self)
   self.obj143.preAction( cobj0.LHS.CREATE )
   self.obj143.isGraphObjectVisual = True

   if(hasattr(self.obj143, '_setHierarchicalLink')):
     self.obj143._setHierarchicalLink(False)

   # MaxFlow
   self.obj143.MaxFlow.setNone()

   # price
   self.obj143.price.setNone()

   # Name
   self.obj143.Name.setValue('')
   self.obj143.Name.setNone()

   # ReqFlow
   self.obj143.ReqFlow.setNone()

   self.obj143.GGLabel.setValue(3)
   self.obj143.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(360.0,160.0,self.obj143)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj143.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj143)
   self.obj143.postAction( cobj0.LHS.CREATE )

   self.obj144=operatingUnit(self)
   self.obj144.preAction( cobj0.LHS.CREATE )
   self.obj144.isGraphObjectVisual = True

   if(hasattr(self.obj144, '_setHierarchicalLink')):
     self.obj144._setHierarchicalLink(False)

   # OperCostProp
   self.obj144.OperCostProp.setNone()

   # name
   self.obj144.name.setValue('')
   self.obj144.name.setNone()

   # OperCostFix
   self.obj144.OperCostFix.setNone()

   self.obj144.GGLabel.setValue(2)
   self.obj144.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(180.0,100.0,self.obj144)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj144.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj144)
   self.obj144.postAction( cobj0.LHS.CREATE )

   self.obj145=intoMaterial(self)
   self.obj145.preAction( cobj0.LHS.CREATE )
   self.obj145.isGraphObjectVisual = True

   if(hasattr(self.obj145, '_setHierarchicalLink')):
     self.obj145._setHierarchicalLink(False)

   # rate
   self.obj145.rate.setNone()

   self.obj145.GGLabel.setValue(5)
   self.obj145.graphClass_= graph_intoMaterial
   if self.genGraphics:
      new_obj = graph_intoMaterial(248.75,168.5,self.obj145)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj145.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj145)
   self.obj145.postAction( cobj0.LHS.CREATE )

   self.obj146=fromMaterial(self)
   self.obj146.preAction( cobj0.LHS.CREATE )
   self.obj146.isGraphObjectVisual = True

   if(hasattr(self.obj146, '_setHierarchicalLink')):
     self.obj146._setHierarchicalLink(False)

   # rate
   self.obj146.rate.setNone()

   self.obj146.GGLabel.setValue(4)
   self.obj146.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(175.0,68.75,self.obj146)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj146.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj146)
   self.obj146.postAction( cobj0.LHS.CREATE )

   self.obj142.out_connections_.append(self.obj146)
   self.obj146.in_connections_.append(self.obj142)
   self.obj142.graphObject_.pendingConnections.append((self.obj142.graphObject_.tag, self.obj146.graphObject_.tag, [86.0, 50.0, 146.5, 53.5, 175.0, 68.75], 2, True))
   self.obj144.out_connections_.append(self.obj145)
   self.obj145.in_connections_.append(self.obj144)
   self.obj144.graphObject_.pendingConnections.append((self.obj144.graphObject_.tag, self.obj145.graphObject_.tag, [199.0, 118.0, 207.0, 147.5, 248.75, 168.5], 2, True))
   self.obj145.out_connections_.append(self.obj143)
   self.obj143.in_connections_.append(self.obj145)
   self.obj145.graphObject_.pendingConnections.append((self.obj145.graphObject_.tag, self.obj143.graphObject_.tag, [366.0, 202.0, 290.5, 189.5, 248.75, 168.5], 2, True))
   self.obj146.out_connections_.append(self.obj144)
   self.obj144.in_connections_.append(self.obj146)
   self.obj146.graphObject_.pendingConnections.append((self.obj146.graphObject_.tag, self.obj144.graphObject_.tag, [200.0, 111.0, 203.5, 84.0, 175.0, 68.75], 2, True))

   cobj0.RHS = ASG_pns(self)

   self.obj148=metarial(self)
   self.obj148.preAction( cobj0.RHS.CREATE )
   self.obj148.isGraphObjectVisual = True

   if(hasattr(self.obj148, '_setHierarchicalLink')):
     self.obj148._setHierarchicalLink(False)

   # MaxFlow
   self.obj148.MaxFlow.setNone()

   # price
   self.obj148.price.setNone()

   # Name
   self.obj148.Name.setValue('')
   self.obj148.Name.setNone()

   # ReqFlow
   self.obj148.ReqFlow.setNone()

   self.obj148.GGLabel.setValue(1)
   self.obj148.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(40.0,40.0,self.obj148)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj148.graphObject_ = new_obj
   self.obj1480= AttrCalc()
   self.obj1480.Copy=ATOM3Boolean()
   self.obj1480.Copy.setValue(('Copy from LHS', 1))
   self.obj1480.Copy.config = 0
   self.obj1480.Specify=ATOM3Constraint()
   self.obj1480.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj148.GGset2Any['MaxFlow']= self.obj1480
   self.obj1481= AttrCalc()
   self.obj1481.Copy=ATOM3Boolean()
   self.obj1481.Copy.setValue(('Copy from LHS', 1))
   self.obj1481.Copy.config = 0
   self.obj1481.Specify=ATOM3Constraint()
   self.obj1481.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj148.GGset2Any['price']= self.obj1481
   self.obj1482= AttrCalc()
   self.obj1482.Copy=ATOM3Boolean()
   self.obj1482.Copy.setValue(('Copy from LHS', 1))
   self.obj1482.Copy.config = 0
   self.obj1482.Specify=ATOM3Constraint()
   self.obj1482.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj148.GGset2Any['Name']= self.obj1482
   self.obj1483= AttrCalc()
   self.obj1483.Copy=ATOM3Boolean()
   self.obj1483.Copy.setValue(('Copy from LHS', 1))
   self.obj1483.Copy.config = 0
   self.obj1483.Specify=ATOM3Constraint()
   self.obj1483.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj148.GGset2Any['ReqFlow']= self.obj1483

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj148)
   self.obj148.postAction( cobj0.RHS.CREATE )

   self.obj149=metarial(self)
   self.obj149.preAction( cobj0.RHS.CREATE )
   self.obj149.isGraphObjectVisual = True

   if(hasattr(self.obj149, '_setHierarchicalLink')):
     self.obj149._setHierarchicalLink(False)

   # MaxFlow
   self.obj149.MaxFlow.setNone()

   # price
   self.obj149.price.setNone()

   # Name
   self.obj149.Name.setValue('')
   self.obj149.Name.setNone()

   # ReqFlow
   self.obj149.ReqFlow.setNone()

   self.obj149.GGLabel.setValue(3)
   self.obj149.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(360.0,160.0,self.obj149)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj149.graphObject_ = new_obj
   self.obj1490= AttrCalc()
   self.obj1490.Copy=ATOM3Boolean()
   self.obj1490.Copy.setValue(('Copy from LHS', 1))
   self.obj1490.Copy.config = 0
   self.obj1490.Specify=ATOM3Constraint()
   self.obj1490.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj149.GGset2Any['MaxFlow']= self.obj1490
   self.obj1491= AttrCalc()
   self.obj1491.Copy=ATOM3Boolean()
   self.obj1491.Copy.setValue(('Copy from LHS', 1))
   self.obj1491.Copy.config = 0
   self.obj1491.Specify=ATOM3Constraint()
   self.obj1491.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj149.GGset2Any['price']= self.obj1491
   self.obj1492= AttrCalc()
   self.obj1492.Copy=ATOM3Boolean()
   self.obj1492.Copy.setValue(('Copy from LHS', 1))
   self.obj1492.Copy.config = 0
   self.obj1492.Specify=ATOM3Constraint()
   self.obj1492.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj149.GGset2Any['Name']= self.obj1492
   self.obj1493= AttrCalc()
   self.obj1493.Copy=ATOM3Boolean()
   self.obj1493.Copy.setValue(('Copy from LHS', 1))
   self.obj1493.Copy.config = 0
   self.obj1493.Specify=ATOM3Constraint()
   self.obj1493.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj149.GGset2Any['ReqFlow']= self.obj1493

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj149)
   self.obj149.postAction( cobj0.RHS.CREATE )

   self.obj150=operatingUnit(self)
   self.obj150.preAction( cobj0.RHS.CREATE )
   self.obj150.isGraphObjectVisual = True

   if(hasattr(self.obj150, '_setHierarchicalLink')):
     self.obj150._setHierarchicalLink(False)

   # OperCostProp
   self.obj150.OperCostProp.setNone()

   # name
   self.obj150.name.setValue('')
   self.obj150.name.setNone()

   # OperCostFix
   self.obj150.OperCostFix.setNone()

   self.obj150.GGLabel.setValue(2)
   self.obj150.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(180.0,100.0,self.obj150)
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
   self.obj150.GGset2Any['OperCostProp']= self.obj1500
   self.obj1501= AttrCalc()
   self.obj1501.Copy=ATOM3Boolean()
   self.obj1501.Copy.setValue(('Copy from LHS', 1))
   self.obj1501.Copy.config = 0
   self.obj1501.Specify=ATOM3Constraint()
   self.obj1501.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj150.GGset2Any['name']= self.obj1501
   self.obj1502= AttrCalc()
   self.obj1502.Copy=ATOM3Boolean()
   self.obj1502.Copy.setValue(('Copy from LHS', 1))
   self.obj1502.Copy.config = 0
   self.obj1502.Specify=ATOM3Constraint()
   self.obj1502.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj150.GGset2Any['OperCostFix']= self.obj1502

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj150)
   self.obj150.postAction( cobj0.RHS.CREATE )

   self.obj151=intoMaterial(self)
   self.obj151.preAction( cobj0.RHS.CREATE )
   self.obj151.isGraphObjectVisual = True

   if(hasattr(self.obj151, '_setHierarchicalLink')):
     self.obj151._setHierarchicalLink(False)

   # rate
   self.obj151.rate.setNone()

   self.obj151.GGLabel.setValue(5)
   self.obj151.graphClass_= graph_intoMaterial
   if self.genGraphics:
      new_obj = graph_intoMaterial(210.75,161.5,self.obj151)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['Text Scale'] = 0.68
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj151.graphObject_ = new_obj
   self.obj1510= AttrCalc()
   self.obj1510.Copy=ATOM3Boolean()
   self.obj1510.Copy.setValue(('Copy from LHS', 1))
   self.obj1510.Copy.config = 0
   self.obj1510.Specify=ATOM3Constraint()
   self.obj1510.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj151.GGset2Any['rate']= self.obj1510

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj151)
   self.obj151.postAction( cobj0.RHS.CREATE )

   self.obj152=fromMaterial(self)
   self.obj152.preAction( cobj0.RHS.CREATE )
   self.obj152.isGraphObjectVisual = True

   if(hasattr(self.obj152, '_setHierarchicalLink')):
     self.obj152._setHierarchicalLink(False)

   # rate
   self.obj152.rate.setNone()

   self.obj152.GGLabel.setValue(4)
   self.obj152.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(175.0,68.75,self.obj152)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj152.graphObject_ = new_obj
   self.obj1520= AttrCalc()
   self.obj1520.Copy=ATOM3Boolean()
   self.obj1520.Copy.setValue(('Copy from LHS', 1))
   self.obj1520.Copy.config = 0
   self.obj1520.Specify=ATOM3Constraint()
   self.obj1520.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj152.GGset2Any['rate']= self.obj1520

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj152)
   self.obj152.postAction( cobj0.RHS.CREATE )

   self.obj148.out_connections_.append(self.obj152)
   self.obj152.in_connections_.append(self.obj148)
   self.obj148.graphObject_.pendingConnections.append((self.obj148.graphObject_.tag, self.obj152.graphObject_.tag, [86.0, 50.0, 175.0, 68.75], 2, 0))
   self.obj150.out_connections_.append(self.obj151)
   self.obj151.in_connections_.append(self.obj150)
   self.obj150.graphObject_.pendingConnections.append((self.obj150.graphObject_.tag, self.obj151.graphObject_.tag, [233.0, 108.0, 210.75, 161.5], 2, 0))
   self.obj151.out_connections_.append(self.obj149)
   self.obj149.in_connections_.append(self.obj151)
   self.obj151.graphObject_.pendingConnections.append((self.obj151.graphObject_.tag, self.obj149.graphObject_.tag, [370.0, 165.0, 248.75, 168.5], 2, 0))
   self.obj152.out_connections_.append(self.obj150)
   self.obj150.in_connections_.append(self.obj152)
   self.obj152.graphObject_.pendingConnections.append((self.obj152.graphObject_.tag, self.obj150.graphObject_.tag, [230.0, 101.0, 175.0, 68.75], 2, 0))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'opUnit = self.getMatched(graphID, self.LHS.nodeWithLabel(2)) \nreturn not ( hasattr(opUnit,"rat") )\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'input = self.getMatched(graphID, self.LHS.nodeWithLabel(4))\noutput = self.getMatched(graphID, self.LHS.nodeWithLabel(5))\n\nop = self.getMatched(graphID, self.LHS.nodeWithLabel(2))\nop.rat = input.rate.getValue()/output.rate.getValue()\nprint op.name.getValue()+":"+str(op.rat)\n\n'))
   lcobj0.append(cobj0)
   self.EditingGraphGrammar.Rules.setValue(lcobj0)
   self.EditingGraphGrammar.InitialAction=ATOM3Constraint()
   self.EditingGraphGrammar.InitialAction.setValue(('constraint', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'self.rewritingSystem.finalStat = 0\nglobal nSolution \nnSolution = 0\nglobal Agentdict\nglobal Agentnode\nglobal dictWord\nglobal SolutionClasses\nglobal ind\nind = 0\nSolutionClasses ={}\ndictWord={}\nAgentdict = {}\nAgentnode = {}\n\n'))
   self.EditingGraphGrammar.FinalAction=ATOM3Constraint()
   self.EditingGraphGrammar.FinalAction.setValue(('constraint', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# import needed packages\nimport OptimalPNS_GG_exec \nimport math \n# print our data Struct\nprint OptimalPNS_GG_exec.Agentdict \ntotalSolution = 0 \n# start extract information from data Struct\nfor key in OptimalPNS_GG_exec.Agentdict.keys() :\n totalSolution += math.pow(2, OptimalPNS_GG_exec.Agentdict[key] ) -1\nprint "Finish "+str( totalSolution ) \n\n'))


