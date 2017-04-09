from GraphGrammarEdit import *
from GGruleEdit import *

def savedTrans(self):
   self.EditingGraphGrammar= GraphGrammarEdit(None, self)
   self.EditingGraphGrammar.Name=ATOM3String('Pns2Xml', 20)
   self.EditingGraphGrammar.Rules=ATOM3List([ 1, 1, 1, 0],GGruleEdit,None, self)
   lcobj0=[]
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('VisitRaw', 20)
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

   self.obj926=rawMaterial(self)
   self.obj926.preAction( cobj0.LHS.CREATE )
   self.obj926.isGraphObjectVisual = True

   if(hasattr(self.obj926, '_setHierarchicalLink')):
     self.obj926._setHierarchicalLink(False)

   # MaxFlow
   self.obj926.MaxFlow.setNone()

   # price
   self.obj926.price.setNone()

   # Name
   self.obj926.Name.setValue('')
   self.obj926.Name.setNone()

   # ReqFlow
   self.obj926.ReqFlow.setNone()

   self.obj926.GGLabel.setValue(1)
   self.obj926.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(160.0,40.0,self.obj926)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj926.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj926)
   self.obj926.postAction( cobj0.LHS.CREATE )


   cobj0.RHS = ASG_pns(self)

   self.obj928=rawMaterial(self)
   self.obj928.preAction( cobj0.RHS.CREATE )
   self.obj928.isGraphObjectVisual = True

   if(hasattr(self.obj928, '_setHierarchicalLink')):
     self.obj928._setHierarchicalLink(False)

   # MaxFlow
   self.obj928.MaxFlow.setNone()

   # price
   self.obj928.price.setNone()

   # Name
   self.obj928.Name.setValue('')
   self.obj928.Name.setNone()

   # ReqFlow
   self.obj928.ReqFlow.setNone()

   self.obj928.GGLabel.setValue(1)
   self.obj928.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(160.0,40.0,self.obj928)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj928.graphObject_ = new_obj
   self.obj9280= AttrCalc()
   self.obj9280.Copy=ATOM3Boolean()
   self.obj9280.Copy.setValue(('Copy from LHS', 1))
   self.obj9280.Copy.config = 0
   self.obj9280.Specify=ATOM3Constraint()
   self.obj9280.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj928.GGset2Any['MaxFlow']= self.obj9280
   self.obj9281= AttrCalc()
   self.obj9281.Copy=ATOM3Boolean()
   self.obj9281.Copy.setValue(('Copy from LHS', 1))
   self.obj9281.Copy.config = 0
   self.obj9281.Specify=ATOM3Constraint()
   self.obj9281.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj928.GGset2Any['price']= self.obj9281
   self.obj9282= AttrCalc()
   self.obj9282.Copy=ATOM3Boolean()
   self.obj9282.Copy.setValue(('Copy from LHS', 1))
   self.obj9282.Copy.config = 0
   self.obj9282.Specify=ATOM3Constraint()
   self.obj9282.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj928.GGset2Any['Name']= self.obj9282
   self.obj9283= AttrCalc()
   self.obj9283.Copy=ATOM3Boolean()
   self.obj9283.Copy.setValue(('Copy from LHS', 1))
   self.obj9283.Copy.config = 0
   self.obj9283.Specify=ATOM3Constraint()
   self.obj9283.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj928.GGset2Any['ReqFlow']= self.obj9283

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj928)
   self.obj928.postAction( cobj0.RHS.CREATE )


   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nreturn not hasattr(node, "ID")\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# code action of rule \n# Import Function && Variables\nfrom MyFunction import *\nimport Pns2Xml_GG_exec \nPns2Xml_GG_exec.iD = Pns2Xml_GG_exec.iD + 1 \nprint \'global iD : \'+str(Pns2Xml_GG_exec.iD)\n#Add Node \nnode = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) )\nnode.ID =   Pns2Xml_GG_exec.iD\nnodeName = node.Name.getValue() # name of the node \'Agent\'\nx = int (node.graphObject_.x * 3)           \ny = int(node.graphObject_.y * 3)\n#newNode(  Pns2Xml_GG_exec.materials , nodeName , node.ID , 0 , x , y ,price=node.price.getValue()  )\nnewMaterial(  Pns2Xml_GG_exec.materials , nodeName , node.ID , 0 , x , y ,  node.price.getValue() , node.ReqFlow.getValue() ,node.MaxFlow.getValue()  )\n#,beginID = 0 , endID = 0, rate = 0 \nprint node.Name.getValue()+\' : \'+str(node.ID)\n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('VisitMat', 20)
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

   self.obj933=metarial(self)
   self.obj933.preAction( cobj0.LHS.CREATE )
   self.obj933.isGraphObjectVisual = True

   if(hasattr(self.obj933, '_setHierarchicalLink')):
     self.obj933._setHierarchicalLink(False)

   # MaxFlow
   self.obj933.MaxFlow.setNone()

   # price
   self.obj933.price.setNone()

   # Name
   self.obj933.Name.setValue('')
   self.obj933.Name.setNone()

   # ReqFlow
   self.obj933.ReqFlow.setNone()

   self.obj933.GGLabel.setValue(1)
   self.obj933.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(140.0,60.0,self.obj933)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj933.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj933)
   self.obj933.postAction( cobj0.LHS.CREATE )


   cobj0.RHS = ASG_pns(self)

   self.obj935=metarial(self)
   self.obj935.preAction( cobj0.RHS.CREATE )
   self.obj935.isGraphObjectVisual = True

   if(hasattr(self.obj935, '_setHierarchicalLink')):
     self.obj935._setHierarchicalLink(False)

   # MaxFlow
   self.obj935.MaxFlow.setNone()

   # price
   self.obj935.price.setNone()

   # Name
   self.obj935.Name.setValue('')
   self.obj935.Name.setNone()

   # ReqFlow
   self.obj935.ReqFlow.setNone()

   self.obj935.GGLabel.setValue(1)
   self.obj935.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(140.0,60.0,self.obj935)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj935.graphObject_ = new_obj
   self.obj9350= AttrCalc()
   self.obj9350.Copy=ATOM3Boolean()
   self.obj9350.Copy.setValue(('Copy from LHS', 1))
   self.obj9350.Copy.config = 0
   self.obj9350.Specify=ATOM3Constraint()
   self.obj9350.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj935.GGset2Any['MaxFlow']= self.obj9350
   self.obj9351= AttrCalc()
   self.obj9351.Copy=ATOM3Boolean()
   self.obj9351.Copy.setValue(('Copy from LHS', 1))
   self.obj9351.Copy.config = 0
   self.obj9351.Specify=ATOM3Constraint()
   self.obj9351.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj935.GGset2Any['price']= self.obj9351
   self.obj9352= AttrCalc()
   self.obj9352.Copy=ATOM3Boolean()
   self.obj9352.Copy.setValue(('Copy from LHS', 1))
   self.obj9352.Copy.config = 0
   self.obj9352.Specify=ATOM3Constraint()
   self.obj9352.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj935.GGset2Any['Name']= self.obj9352
   self.obj9353= AttrCalc()
   self.obj9353.Copy=ATOM3Boolean()
   self.obj9353.Copy.setValue(('Copy from LHS', 1))
   self.obj9353.Copy.config = 0
   self.obj9353.Specify=ATOM3Constraint()
   self.obj9353.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj935.GGset2Any['ReqFlow']= self.obj9353

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj935)
   self.obj935.postAction( cobj0.RHS.CREATE )


   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nreturn not hasattr(node, "ID")\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# code action of rule \n# Import Function && Variables\nfrom MyFunction import *\nimport Pns2Xml_GG_exec \nPns2Xml_GG_exec.iD = Pns2Xml_GG_exec.iD + 1 \nprint \'global iD : \'+str(Pns2Xml_GG_exec.iD)\n#Add Node \nnode = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) )\nnode.ID =   Pns2Xml_GG_exec.iD\nnodeName = node.Name.getValue() # name of the node \'Agent\'\nx = int (node.graphObject_.x * 3)           \ny = int(node.graphObject_.y * 3)\n#newNode(  Pns2Xml_GG_exec.materials , nodeName , node.ID , 0 , x , y ,price=node.price.getValue()  )\nnewMaterial(  Pns2Xml_GG_exec.materials , nodeName , node.ID , 1 , x , y ,  node.price.getValue() , node.ReqFlow.getValue() ,node.MaxFlow.getValue()  )\n#,beginID = 0 , endID = 0, rate = 0 \nprint node.Name.getValue()+\' : \'+str(node.ID)\n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('VisitProduct', 20)
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

   self.obj940=product(self)
   self.obj940.preAction( cobj0.LHS.CREATE )
   self.obj940.isGraphObjectVisual = True

   if(hasattr(self.obj940, '_setHierarchicalLink')):
     self.obj940._setHierarchicalLink(False)

   # MaxFlow
   self.obj940.MaxFlow.setNone()

   # price
   self.obj940.price.setNone()

   # Name
   self.obj940.Name.setValue('')
   self.obj940.Name.setNone()

   # ReqFlow
   self.obj940.ReqFlow.setNone()

   self.obj940.GGLabel.setValue(1)
   self.obj940.graphClass_= graph_product
   if self.genGraphics:
      new_obj = graph_product(200.0,60.0,self.obj940)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj940.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj940)
   self.obj940.postAction( cobj0.LHS.CREATE )


   cobj0.RHS = ASG_pns(self)

   self.obj942=product(self)
   self.obj942.preAction( cobj0.RHS.CREATE )
   self.obj942.isGraphObjectVisual = True

   if(hasattr(self.obj942, '_setHierarchicalLink')):
     self.obj942._setHierarchicalLink(False)

   # MaxFlow
   self.obj942.MaxFlow.setNone()

   # price
   self.obj942.price.setNone()

   # Name
   self.obj942.Name.setValue('')
   self.obj942.Name.setNone()

   # ReqFlow
   self.obj942.ReqFlow.setNone()

   self.obj942.GGLabel.setValue(1)
   self.obj942.graphClass_= graph_product
   if self.genGraphics:
      new_obj = graph_product(200.0,60.0,self.obj942)
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
   self.obj942.GGset2Any['MaxFlow']= self.obj9420
   self.obj9421= AttrCalc()
   self.obj9421.Copy=ATOM3Boolean()
   self.obj9421.Copy.setValue(('Copy from LHS', 1))
   self.obj9421.Copy.config = 0
   self.obj9421.Specify=ATOM3Constraint()
   self.obj9421.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj942.GGset2Any['price']= self.obj9421
   self.obj9422= AttrCalc()
   self.obj9422.Copy=ATOM3Boolean()
   self.obj9422.Copy.setValue(('Copy from LHS', 1))
   self.obj9422.Copy.config = 0
   self.obj9422.Specify=ATOM3Constraint()
   self.obj9422.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj942.GGset2Any['Name']= self.obj9422
   self.obj9423= AttrCalc()
   self.obj9423.Copy=ATOM3Boolean()
   self.obj9423.Copy.setValue(('Copy from LHS', 1))
   self.obj9423.Copy.config = 0
   self.obj9423.Specify=ATOM3Constraint()
   self.obj9423.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj942.GGset2Any['ReqFlow']= self.obj9423

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj942)
   self.obj942.postAction( cobj0.RHS.CREATE )


   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nreturn not hasattr(node, "ID")\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# code action of rule \n# Import Function && Variables\nfrom MyFunction import *\nimport Pns2Xml_GG_exec \nPns2Xml_GG_exec.iD = Pns2Xml_GG_exec.iD + 1 \nprint \'global iD : \'+str(Pns2Xml_GG_exec.iD)\n#Add Node \nnode = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) )\nnode.ID =   Pns2Xml_GG_exec.iD\nnodeName = node.Name.getValue() # name of the node \'Agent\'\nx = int (node.graphObject_.x * 3)           \ny = int(node.graphObject_.y * 3)\n#newNode(  Pns2Xml_GG_exec.materials , nodeName , node.ID , 0 , x , y ,price=node.price.getValue()  )\nnewMaterial(  Pns2Xml_GG_exec.materials , nodeName , node.ID , 2 , x , y ,  node.price.getValue() , node.ReqFlow.getValue() ,node.MaxFlow.getValue()  )\n#,beginID = 0 , endID = 0, rate = 0 \nprint node.Name.getValue()+\' : \'+str(node.ID)\n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('VisitOpUnit', 20)
   cobj0.Order=ATOM3Integer(4)
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

   self.obj947=operatingUnit(self)
   self.obj947.preAction( cobj0.LHS.CREATE )
   self.obj947.isGraphObjectVisual = True

   if(hasattr(self.obj947, '_setHierarchicalLink')):
     self.obj947._setHierarchicalLink(False)

   # OperCostProp
   self.obj947.OperCostProp.setNone()

   # name
   self.obj947.name.setValue('')
   self.obj947.name.setNone()

   # OperCostFix
   self.obj947.OperCostFix.setNone()

   self.obj947.GGLabel.setValue(1)
   self.obj947.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(200.0,40.0,self.obj947)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj947.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj947)
   self.obj947.postAction( cobj0.LHS.CREATE )


   cobj0.RHS = ASG_pns(self)

   self.obj949=operatingUnit(self)
   self.obj949.preAction( cobj0.RHS.CREATE )
   self.obj949.isGraphObjectVisual = True

   if(hasattr(self.obj949, '_setHierarchicalLink')):
     self.obj949._setHierarchicalLink(False)

   # OperCostProp
   self.obj949.OperCostProp.setNone()

   # name
   self.obj949.name.setValue('')
   self.obj949.name.setNone()

   # OperCostFix
   self.obj949.OperCostFix.setNone()

   self.obj949.GGLabel.setValue(1)
   self.obj949.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(200.0,60.0,self.obj949)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj949.graphObject_ = new_obj
   self.obj9490= AttrCalc()
   self.obj9490.Copy=ATOM3Boolean()
   self.obj9490.Copy.setValue(('Copy from LHS', 1))
   self.obj9490.Copy.config = 0
   self.obj9490.Specify=ATOM3Constraint()
   self.obj9490.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj949.GGset2Any['OperCostProp']= self.obj9490
   self.obj9491= AttrCalc()
   self.obj9491.Copy=ATOM3Boolean()
   self.obj9491.Copy.setValue(('Copy from LHS', 1))
   self.obj9491.Copy.config = 0
   self.obj9491.Specify=ATOM3Constraint()
   self.obj9491.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj949.GGset2Any['name']= self.obj9491
   self.obj9492= AttrCalc()
   self.obj9492.Copy=ATOM3Boolean()
   self.obj9492.Copy.setValue(('Copy from LHS', 1))
   self.obj9492.Copy.config = 0
   self.obj9492.Specify=ATOM3Constraint()
   self.obj9492.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj949.GGset2Any['OperCostFix']= self.obj9492

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj949)
   self.obj949.postAction( cobj0.RHS.CREATE )


   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nreturn not hasattr(node, "ID")\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# code action of rule \n# Import Function && Variables\nfrom MyFunction import *\nimport Pns2Xml_GG_exec \nPns2Xml_GG_exec.iD = Pns2Xml_GG_exec.iD + 1 \nprint \'global iD : \'+str(Pns2Xml_GG_exec.iD)\n#Add Node \nnode = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) )\nnode.ID =   Pns2Xml_GG_exec.iD\nnodeName = node.name.getValue() # name of the node \'Agent\'\nx = int (node.graphObject_.x * 3)           \ny = int(node.graphObject_.y * 3)\n#newNode(  Pns2Xml_GG_exec.materials , nodeName , node.ID , 0 , x , y ,price=node.price.getValue()  ) opunits\nnewOpUnit(  Pns2Xml_GG_exec.opunits , nodeName , node.ID  , x , y , node.OperCostProp.getValue() ,node.OperCostFix.getValue()  )\n#,beginID = 0 , endID = 0, rate = 0 \nprint nodeName+\' : \'+str(node.ID)\n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('Visit1EdgeRAW', 20)
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

   self.obj954=rawMaterial(self)
   self.obj954.preAction( cobj0.LHS.CREATE )
   self.obj954.isGraphObjectVisual = True

   if(hasattr(self.obj954, '_setHierarchicalLink')):
     self.obj954._setHierarchicalLink(False)

   # MaxFlow
   self.obj954.MaxFlow.setNone()

   # price
   self.obj954.price.setNone()

   # Name
   self.obj954.Name.setValue('')
   self.obj954.Name.setNone()

   # ReqFlow
   self.obj954.ReqFlow.setNone()

   self.obj954.GGLabel.setValue(1)
   self.obj954.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(200.0,20.0,self.obj954)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj954.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj954)
   self.obj954.postAction( cobj0.LHS.CREATE )

   self.obj955=operatingUnit(self)
   self.obj955.preAction( cobj0.LHS.CREATE )
   self.obj955.isGraphObjectVisual = True

   if(hasattr(self.obj955, '_setHierarchicalLink')):
     self.obj955._setHierarchicalLink(False)

   # OperCostProp
   self.obj955.OperCostProp.setNone()

   # name
   self.obj955.name.setValue('')
   self.obj955.name.setNone()

   # OperCostFix
   self.obj955.OperCostFix.setNone()

   self.obj955.GGLabel.setValue(2)
   self.obj955.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(200.0,160.0,self.obj955)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj955.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj955)
   self.obj955.postAction( cobj0.LHS.CREATE )

   self.obj956=fromRaw(self)
   self.obj956.preAction( cobj0.LHS.CREATE )
   self.obj956.isGraphObjectVisual = True

   if(hasattr(self.obj956, '_setHierarchicalLink')):
     self.obj956._setHierarchicalLink(False)

   # rate
   self.obj956.rate.setNone()

   self.obj956.GGLabel.setValue(3)
   self.obj956.graphClass_= graph_fromRaw
   if self.genGraphics:
      new_obj = graph_fromRaw(222.0,123.5,self.obj956)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj956.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj956)
   self.obj956.postAction( cobj0.LHS.CREATE )

   self.obj954.out_connections_.append(self.obj956)
   self.obj956.in_connections_.append(self.obj954)
   self.obj954.graphObject_.pendingConnections.append((self.obj954.graphObject_.tag, self.obj956.graphObject_.tag, [224.0, 76.0, 222.0, 123.5], 0, True))
   self.obj956.out_connections_.append(self.obj955)
   self.obj955.in_connections_.append(self.obj956)
   self.obj956.graphObject_.pendingConnections.append((self.obj956.graphObject_.tag, self.obj955.graphObject_.tag, [220.0, 171.0, 222.0, 123.5], 0, True))

   cobj0.RHS = ASG_pns(self)

   self.obj958=rawMaterial(self)
   self.obj958.preAction( cobj0.RHS.CREATE )
   self.obj958.isGraphObjectVisual = True

   if(hasattr(self.obj958, '_setHierarchicalLink')):
     self.obj958._setHierarchicalLink(False)

   # MaxFlow
   self.obj958.MaxFlow.setNone()

   # price
   self.obj958.price.setNone()

   # Name
   self.obj958.Name.setValue('')
   self.obj958.Name.setNone()

   # ReqFlow
   self.obj958.ReqFlow.setNone()

   self.obj958.GGLabel.setValue(1)
   self.obj958.graphClass_= graph_rawMaterial
   if self.genGraphics:
      new_obj = graph_rawMaterial(200.0,20.0,self.obj958)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj958.graphObject_ = new_obj
   self.obj9580= AttrCalc()
   self.obj9580.Copy=ATOM3Boolean()
   self.obj9580.Copy.setValue(('Copy from LHS', 1))
   self.obj9580.Copy.config = 0
   self.obj9580.Specify=ATOM3Constraint()
   self.obj9580.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj958.GGset2Any['MaxFlow']= self.obj9580
   self.obj9581= AttrCalc()
   self.obj9581.Copy=ATOM3Boolean()
   self.obj9581.Copy.setValue(('Copy from LHS', 1))
   self.obj9581.Copy.config = 0
   self.obj9581.Specify=ATOM3Constraint()
   self.obj9581.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj958.GGset2Any['price']= self.obj9581
   self.obj9582= AttrCalc()
   self.obj9582.Copy=ATOM3Boolean()
   self.obj9582.Copy.setValue(('Copy from LHS', 1))
   self.obj9582.Copy.config = 0
   self.obj9582.Specify=ATOM3Constraint()
   self.obj9582.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj958.GGset2Any['Name']= self.obj9582
   self.obj9583= AttrCalc()
   self.obj9583.Copy=ATOM3Boolean()
   self.obj9583.Copy.setValue(('Copy from LHS', 1))
   self.obj9583.Copy.config = 0
   self.obj9583.Specify=ATOM3Constraint()
   self.obj9583.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj958.GGset2Any['ReqFlow']= self.obj9583

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj958)
   self.obj958.postAction( cobj0.RHS.CREATE )

   self.obj959=operatingUnit(self)
   self.obj959.preAction( cobj0.RHS.CREATE )
   self.obj959.isGraphObjectVisual = True

   if(hasattr(self.obj959, '_setHierarchicalLink')):
     self.obj959._setHierarchicalLink(False)

   # OperCostProp
   self.obj959.OperCostProp.setNone()

   # name
   self.obj959.name.setValue('')
   self.obj959.name.setNone()

   # OperCostFix
   self.obj959.OperCostFix.setNone()

   self.obj959.GGLabel.setValue(2)
   self.obj959.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(200.0,160.0,self.obj959)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj959.graphObject_ = new_obj
   self.obj9590= AttrCalc()
   self.obj9590.Copy=ATOM3Boolean()
   self.obj9590.Copy.setValue(('Copy from LHS', 1))
   self.obj9590.Copy.config = 0
   self.obj9590.Specify=ATOM3Constraint()
   self.obj9590.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj959.GGset2Any['OperCostProp']= self.obj9590
   self.obj9591= AttrCalc()
   self.obj9591.Copy=ATOM3Boolean()
   self.obj9591.Copy.setValue(('Copy from LHS', 1))
   self.obj9591.Copy.config = 0
   self.obj9591.Specify=ATOM3Constraint()
   self.obj9591.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj959.GGset2Any['name']= self.obj9591
   self.obj9592= AttrCalc()
   self.obj9592.Copy=ATOM3Boolean()
   self.obj9592.Copy.setValue(('Copy from LHS', 1))
   self.obj9592.Copy.config = 0
   self.obj9592.Specify=ATOM3Constraint()
   self.obj9592.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj959.GGset2Any['OperCostFix']= self.obj9592

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj959)
   self.obj959.postAction( cobj0.RHS.CREATE )

   self.obj960=fromRaw(self)
   self.obj960.preAction( cobj0.RHS.CREATE )
   self.obj960.isGraphObjectVisual = True

   if(hasattr(self.obj960, '_setHierarchicalLink')):
     self.obj960._setHierarchicalLink(False)

   # rate
   self.obj960.rate.setNone()

   self.obj960.GGLabel.setValue(3)
   self.obj960.graphClass_= graph_fromRaw
   if self.genGraphics:
      new_obj = graph_fromRaw(222.0,123.5,self.obj960)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj960.graphObject_ = new_obj
   self.obj9600= AttrCalc()
   self.obj9600.Copy=ATOM3Boolean()
   self.obj9600.Copy.setValue(('Copy from LHS', 1))
   self.obj9600.Copy.config = 0
   self.obj9600.Specify=ATOM3Constraint()
   self.obj9600.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj960.GGset2Any['rate']= self.obj9600

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj960)
   self.obj960.postAction( cobj0.RHS.CREATE )

   self.obj958.out_connections_.append(self.obj960)
   self.obj960.in_connections_.append(self.obj958)
   self.obj958.graphObject_.pendingConnections.append((self.obj958.graphObject_.tag, self.obj960.graphObject_.tag, [224.0, 70.0, 222.0, 123.5], 2, 0))
   self.obj960.out_connections_.append(self.obj959)
   self.obj959.in_connections_.append(self.obj960)
   self.obj960.graphObject_.pendingConnections.append((self.obj960.graphObject_.tag, self.obj959.graphObject_.tag, [250.0, 161.0, 222.0, 123.5], 2, 0))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'node = self.getMatched(graphID, self.LHS.nodeWithLabel(3))\nreturn not hasattr(node, "ID")\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# code action of rule \nfrom MyFunction import *\nimport Pns2Xml_GG_exec \nPns2Xml_GG_exec.iD = Pns2Xml_GG_exec.iD + 1 \nprint \'global iD : \'+str(Pns2Xml_GG_exec.iD)\n\nnode = self.getMatched ( graphID , self.LHS.nodeWithLabel(3) )\nnode.ID =   Pns2Xml_GG_exec.iD\n#nodeName = node.name.getValue() # name of the node \'Agent\'\nnodeRate = node.rate.getValue()\nx = int (node.graphObject_.x * 3)           \ny = int(node.graphObject_.y * 3)\n\nbID = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) ).ID \neID = self.getMatched ( graphID , self.LHS.nodeWithLabel(2) ).ID \nnewEdges(  Pns2Xml_GG_exec.edges , nodeRate , node.ID  , x ,  y ,   bID , eID )\n#,beginID = 0 , endID = 0, rate = 0 \nprint str(node.rate.getValue())+\' : \'+str(node.ID)\n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('Visit2EdgeFINAL', 20)
   cobj0.Order=ATOM3Integer(6)
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

   self.obj965=product(self)
   self.obj965.preAction( cobj0.LHS.CREATE )
   self.obj965.isGraphObjectVisual = True

   if(hasattr(self.obj965, '_setHierarchicalLink')):
     self.obj965._setHierarchicalLink(False)

   # MaxFlow
   self.obj965.MaxFlow.setNone()

   # price
   self.obj965.price.setNone()

   # Name
   self.obj965.Name.setValue('')
   self.obj965.Name.setNone()

   # ReqFlow
   self.obj965.ReqFlow.setNone()

   self.obj965.GGLabel.setValue(2)
   self.obj965.graphClass_= graph_product
   if self.genGraphics:
      new_obj = graph_product(220.0,140.0,self.obj965)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj965.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj965)
   self.obj965.postAction( cobj0.LHS.CREATE )

   self.obj966=operatingUnit(self)
   self.obj966.preAction( cobj0.LHS.CREATE )
   self.obj966.isGraphObjectVisual = True

   if(hasattr(self.obj966, '_setHierarchicalLink')):
     self.obj966._setHierarchicalLink(False)

   # OperCostProp
   self.obj966.OperCostProp.setNone()

   # name
   self.obj966.name.setValue('')
   self.obj966.name.setNone()

   # OperCostFix
   self.obj966.OperCostFix.setNone()

   self.obj966.GGLabel.setValue(1)
   self.obj966.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(180.0,20.0,self.obj966)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj966.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj966)
   self.obj966.postAction( cobj0.LHS.CREATE )

   self.obj967=intoProduct(self)
   self.obj967.preAction( cobj0.LHS.CREATE )
   self.obj967.isGraphObjectVisual = True

   if(hasattr(self.obj967, '_setHierarchicalLink')):
     self.obj967._setHierarchicalLink(False)

   # rate
   self.obj967.rate.setNone()

   self.obj967.GGLabel.setValue(3)
   self.obj967.graphClass_= graph_intoProduct
   if self.genGraphics:
      new_obj = graph_intoProduct(239.0,89.0,self.obj967)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj967.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj967)
   self.obj967.postAction( cobj0.LHS.CREATE )

   self.obj966.out_connections_.append(self.obj967)
   self.obj967.in_connections_.append(self.obj966)
   self.obj966.graphObject_.pendingConnections.append((self.obj966.graphObject_.tag, self.obj967.graphObject_.tag, [233.0, 38.0, 239.0, 89.0], 0, True))
   self.obj967.out_connections_.append(self.obj965)
   self.obj965.in_connections_.append(self.obj967)
   self.obj967.graphObject_.pendingConnections.append((self.obj967.graphObject_.tag, self.obj965.graphObject_.tag, [245.0, 140.0, 239.0, 89.0], 0, True))

   cobj0.RHS = ASG_pns(self)

   self.obj969=product(self)
   self.obj969.preAction( cobj0.RHS.CREATE )
   self.obj969.isGraphObjectVisual = True

   if(hasattr(self.obj969, '_setHierarchicalLink')):
     self.obj969._setHierarchicalLink(False)

   # MaxFlow
   self.obj969.MaxFlow.setNone()

   # price
   self.obj969.price.setNone()

   # Name
   self.obj969.Name.setValue('')
   self.obj969.Name.setNone()

   # ReqFlow
   self.obj969.ReqFlow.setNone()

   self.obj969.GGLabel.setValue(2)
   self.obj969.graphClass_= graph_product
   if self.genGraphics:
      new_obj = graph_product(220.0,140.0,self.obj969)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj969.graphObject_ = new_obj
   self.obj9690= AttrCalc()
   self.obj9690.Copy=ATOM3Boolean()
   self.obj9690.Copy.setValue(('Copy from LHS', 1))
   self.obj9690.Copy.config = 0
   self.obj9690.Specify=ATOM3Constraint()
   self.obj9690.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj969.GGset2Any['MaxFlow']= self.obj9690
   self.obj9691= AttrCalc()
   self.obj9691.Copy=ATOM3Boolean()
   self.obj9691.Copy.setValue(('Copy from LHS', 1))
   self.obj9691.Copy.config = 0
   self.obj9691.Specify=ATOM3Constraint()
   self.obj9691.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj969.GGset2Any['price']= self.obj9691
   self.obj9692= AttrCalc()
   self.obj9692.Copy=ATOM3Boolean()
   self.obj9692.Copy.setValue(('Copy from LHS', 1))
   self.obj9692.Copy.config = 0
   self.obj9692.Specify=ATOM3Constraint()
   self.obj9692.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj969.GGset2Any['Name']= self.obj9692
   self.obj9693= AttrCalc()
   self.obj9693.Copy=ATOM3Boolean()
   self.obj9693.Copy.setValue(('Copy from LHS', 1))
   self.obj9693.Copy.config = 0
   self.obj9693.Specify=ATOM3Constraint()
   self.obj9693.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj969.GGset2Any['ReqFlow']= self.obj9693

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj969)
   self.obj969.postAction( cobj0.RHS.CREATE )

   self.obj970=operatingUnit(self)
   self.obj970.preAction( cobj0.RHS.CREATE )
   self.obj970.isGraphObjectVisual = True

   if(hasattr(self.obj970, '_setHierarchicalLink')):
     self.obj970._setHierarchicalLink(False)

   # OperCostProp
   self.obj970.OperCostProp.setNone()

   # name
   self.obj970.name.setValue('')
   self.obj970.name.setNone()

   # OperCostFix
   self.obj970.OperCostFix.setNone()

   self.obj970.GGLabel.setValue(1)
   self.obj970.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(180.0,20.0,self.obj970)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj970.graphObject_ = new_obj
   self.obj9700= AttrCalc()
   self.obj9700.Copy=ATOM3Boolean()
   self.obj9700.Copy.setValue(('Copy from LHS', 1))
   self.obj9700.Copy.config = 0
   self.obj9700.Specify=ATOM3Constraint()
   self.obj9700.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj970.GGset2Any['OperCostProp']= self.obj9700
   self.obj9701= AttrCalc()
   self.obj9701.Copy=ATOM3Boolean()
   self.obj9701.Copy.setValue(('Copy from LHS', 1))
   self.obj9701.Copy.config = 0
   self.obj9701.Specify=ATOM3Constraint()
   self.obj9701.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj970.GGset2Any['name']= self.obj9701
   self.obj9702= AttrCalc()
   self.obj9702.Copy=ATOM3Boolean()
   self.obj9702.Copy.setValue(('Copy from LHS', 1))
   self.obj9702.Copy.config = 0
   self.obj9702.Specify=ATOM3Constraint()
   self.obj9702.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj970.GGset2Any['OperCostFix']= self.obj9702

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj970)
   self.obj970.postAction( cobj0.RHS.CREATE )

   self.obj971=intoProduct(self)
   self.obj971.preAction( cobj0.RHS.CREATE )
   self.obj971.isGraphObjectVisual = True

   if(hasattr(self.obj971, '_setHierarchicalLink')):
     self.obj971._setHierarchicalLink(False)

   # rate
   self.obj971.rate.setNone()

   self.obj971.GGLabel.setValue(3)
   self.obj971.graphClass_= graph_intoProduct
   if self.genGraphics:
      new_obj = graph_intoProduct(239.0,89.0,self.obj971)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj971.graphObject_ = new_obj
   self.obj9710= AttrCalc()
   self.obj9710.Copy=ATOM3Boolean()
   self.obj9710.Copy.setValue(('Copy from LHS', 1))
   self.obj9710.Copy.config = 0
   self.obj9710.Specify=ATOM3Constraint()
   self.obj9710.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj971.GGset2Any['rate']= self.obj9710

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj971)
   self.obj971.postAction( cobj0.RHS.CREATE )

   self.obj970.out_connections_.append(self.obj971)
   self.obj971.in_connections_.append(self.obj970)
   self.obj970.graphObject_.pendingConnections.append((self.obj970.graphObject_.tag, self.obj971.graphObject_.tag, [233.0, 28.0, 239.0, 89.0], 2, 0))
   self.obj971.out_connections_.append(self.obj969)
   self.obj969.in_connections_.append(self.obj971)
   self.obj971.graphObject_.pendingConnections.append((self.obj971.graphObject_.tag, self.obj969.graphObject_.tag, [245.0, 140.0, 239.0, 89.0], 2, 0))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'node = self.getMatched(graphID, self.LHS.nodeWithLabel(3))\nreturn not hasattr(node, "ID")\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# code action of rule \nfrom MyFunction import *\nimport Pns2Xml_GG_exec \nPns2Xml_GG_exec.iD = Pns2Xml_GG_exec.iD + 1 \nprint \'global iD : \'+str(Pns2Xml_GG_exec.iD)\n\nnode = self.getMatched ( graphID , self.LHS.nodeWithLabel(3) )\nnode.ID =   Pns2Xml_GG_exec.iD\n#nodeName = node.name.getValue() # name of the node \'Agent\'\nnodeRate = node.rate.getValue()\nx = int (node.graphObject_.x * 3)           \ny = int(node.graphObject_.y * 3)\n\nbID = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) ).ID \neID = self.getMatched ( graphID , self.LHS.nodeWithLabel(2) ).ID \nnewEdges(Pns2Xml_GG_exec.edges , nodeRate , node.ID ,  x ,  y ,  bID ,  eID )\n#,beginID = 0 , endID = 0, rate = 0 \nprint str(node.rate.getValue())+\' : \'+str(node.ID)\n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('Visit3EdgeMat', 20)
   cobj0.Order=ATOM3Integer(7)
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

   self.obj976=metarial(self)
   self.obj976.preAction( cobj0.LHS.CREATE )
   self.obj976.isGraphObjectVisual = True

   if(hasattr(self.obj976, '_setHierarchicalLink')):
     self.obj976._setHierarchicalLink(False)

   # MaxFlow
   self.obj976.MaxFlow.setNone()

   # price
   self.obj976.price.setNone()

   # Name
   self.obj976.Name.setValue('')
   self.obj976.Name.setNone()

   # ReqFlow
   self.obj976.ReqFlow.setNone()

   self.obj976.GGLabel.setValue(1)
   self.obj976.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(200.0,20.0,self.obj976)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj976.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj976)
   self.obj976.postAction( cobj0.LHS.CREATE )

   self.obj977=operatingUnit(self)
   self.obj977.preAction( cobj0.LHS.CREATE )
   self.obj977.isGraphObjectVisual = True

   if(hasattr(self.obj977, '_setHierarchicalLink')):
     self.obj977._setHierarchicalLink(False)

   # OperCostProp
   self.obj977.OperCostProp.setNone()

   # name
   self.obj977.name.setValue('')
   self.obj977.name.setNone()

   # OperCostFix
   self.obj977.OperCostFix.setNone()

   self.obj977.GGLabel.setValue(2)
   self.obj977.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(220.0,160.0,self.obj977)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj977.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj977)
   self.obj977.postAction( cobj0.LHS.CREATE )

   self.obj978=fromMaterial(self)
   self.obj978.preAction( cobj0.LHS.CREATE )
   self.obj978.isGraphObjectVisual = True

   if(hasattr(self.obj978, '_setHierarchicalLink')):
     self.obj978._setHierarchicalLink(False)

   # rate
   self.obj978.rate.setNone()

   self.obj978.GGLabel.setValue(3)
   self.obj978.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(232.0,120.0,self.obj978)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj978.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj978)
   self.obj978.postAction( cobj0.LHS.CREATE )

   self.obj976.out_connections_.append(self.obj978)
   self.obj978.in_connections_.append(self.obj976)
   self.obj976.graphObject_.pendingConnections.append((self.obj976.graphObject_.tag, self.obj978.graphObject_.tag, [224.0, 69.0, 232.0, 120.0], 0, True))
   self.obj978.out_connections_.append(self.obj977)
   self.obj977.in_connections_.append(self.obj978)
   self.obj978.graphObject_.pendingConnections.append((self.obj978.graphObject_.tag, self.obj977.graphObject_.tag, [240.0, 171.0, 232.0, 120.0], 0, True))

   cobj0.RHS = ASG_pns(self)

   self.obj980=metarial(self)
   self.obj980.preAction( cobj0.RHS.CREATE )
   self.obj980.isGraphObjectVisual = True

   if(hasattr(self.obj980, '_setHierarchicalLink')):
     self.obj980._setHierarchicalLink(False)

   # MaxFlow
   self.obj980.MaxFlow.setNone()

   # price
   self.obj980.price.setNone()

   # Name
   self.obj980.Name.setValue('')
   self.obj980.Name.setNone()

   # ReqFlow
   self.obj980.ReqFlow.setNone()

   self.obj980.GGLabel.setValue(1)
   self.obj980.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(200.0,20.0,self.obj980)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj980.graphObject_ = new_obj
   self.obj9800= AttrCalc()
   self.obj9800.Copy=ATOM3Boolean()
   self.obj9800.Copy.setValue(('Copy from LHS', 1))
   self.obj9800.Copy.config = 0
   self.obj9800.Specify=ATOM3Constraint()
   self.obj9800.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj980.GGset2Any['MaxFlow']= self.obj9800
   self.obj9801= AttrCalc()
   self.obj9801.Copy=ATOM3Boolean()
   self.obj9801.Copy.setValue(('Copy from LHS', 1))
   self.obj9801.Copy.config = 0
   self.obj9801.Specify=ATOM3Constraint()
   self.obj9801.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj980.GGset2Any['price']= self.obj9801
   self.obj9802= AttrCalc()
   self.obj9802.Copy=ATOM3Boolean()
   self.obj9802.Copy.setValue(('Copy from LHS', 1))
   self.obj9802.Copy.config = 0
   self.obj9802.Specify=ATOM3Constraint()
   self.obj9802.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj980.GGset2Any['Name']= self.obj9802
   self.obj9803= AttrCalc()
   self.obj9803.Copy=ATOM3Boolean()
   self.obj9803.Copy.setValue(('Copy from LHS', 1))
   self.obj9803.Copy.config = 0
   self.obj9803.Specify=ATOM3Constraint()
   self.obj9803.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj980.GGset2Any['ReqFlow']= self.obj9803

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj980)
   self.obj980.postAction( cobj0.RHS.CREATE )

   self.obj981=operatingUnit(self)
   self.obj981.preAction( cobj0.RHS.CREATE )
   self.obj981.isGraphObjectVisual = True

   if(hasattr(self.obj981, '_setHierarchicalLink')):
     self.obj981._setHierarchicalLink(False)

   # OperCostProp
   self.obj981.OperCostProp.setNone()

   # name
   self.obj981.name.setValue('')
   self.obj981.name.setNone()

   # OperCostFix
   self.obj981.OperCostFix.setNone()

   self.obj981.GGLabel.setValue(2)
   self.obj981.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(220.0,160.0,self.obj981)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj981.graphObject_ = new_obj
   self.obj9810= AttrCalc()
   self.obj9810.Copy=ATOM3Boolean()
   self.obj9810.Copy.setValue(('Copy from LHS', 1))
   self.obj9810.Copy.config = 0
   self.obj9810.Specify=ATOM3Constraint()
   self.obj9810.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj981.GGset2Any['OperCostProp']= self.obj9810
   self.obj9811= AttrCalc()
   self.obj9811.Copy=ATOM3Boolean()
   self.obj9811.Copy.setValue(('Copy from LHS', 1))
   self.obj9811.Copy.config = 0
   self.obj9811.Specify=ATOM3Constraint()
   self.obj9811.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj981.GGset2Any['name']= self.obj9811
   self.obj9812= AttrCalc()
   self.obj9812.Copy=ATOM3Boolean()
   self.obj9812.Copy.setValue(('Copy from LHS', 1))
   self.obj9812.Copy.config = 0
   self.obj9812.Specify=ATOM3Constraint()
   self.obj9812.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj981.GGset2Any['OperCostFix']= self.obj9812

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj981)
   self.obj981.postAction( cobj0.RHS.CREATE )

   self.obj982=fromMaterial(self)
   self.obj982.preAction( cobj0.RHS.CREATE )
   self.obj982.isGraphObjectVisual = True

   if(hasattr(self.obj982, '_setHierarchicalLink')):
     self.obj982._setHierarchicalLink(False)

   # rate
   self.obj982.rate.setNone()

   self.obj982.GGLabel.setValue(3)
   self.obj982.graphClass_= graph_fromMaterial
   if self.genGraphics:
      new_obj = graph_fromMaterial(232.0,120.0,self.obj982)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj982.graphObject_ = new_obj
   self.obj9820= AttrCalc()
   self.obj9820.Copy=ATOM3Boolean()
   self.obj9820.Copy.setValue(('Copy from LHS', 1))
   self.obj9820.Copy.config = 0
   self.obj9820.Specify=ATOM3Constraint()
   self.obj9820.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj982.GGset2Any['rate']= self.obj9820

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj982)
   self.obj982.postAction( cobj0.RHS.CREATE )

   self.obj980.out_connections_.append(self.obj982)
   self.obj982.in_connections_.append(self.obj980)
   self.obj980.graphObject_.pendingConnections.append((self.obj980.graphObject_.tag, self.obj982.graphObject_.tag, [224.0, 69.0, 232.0, 120.0], 2, 0))
   self.obj982.out_connections_.append(self.obj981)
   self.obj981.in_connections_.append(self.obj982)
   self.obj982.graphObject_.pendingConnections.append((self.obj982.graphObject_.tag, self.obj981.graphObject_.tag, [270.0, 161.0, 232.0, 120.0], 2, 0))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'node = self.getMatched(graphID, self.LHS.nodeWithLabel(3))\nreturn not hasattr(node, "ID")\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# code action of rule \nfrom MyFunction import *\nimport Pns2Xml_GG_exec \nPns2Xml_GG_exec.iD = Pns2Xml_GG_exec.iD + 1 \nprint \'global iD : \'+str(Pns2Xml_GG_exec.iD)\n\nnode = self.getMatched ( graphID , self.LHS.nodeWithLabel(3) )\nnode.ID =   Pns2Xml_GG_exec.iD\n#nodeName = node.name.getValue() # name of the node \'Agent\'\nnodeRate = node.rate.getValue()\nx = int (node.graphObject_.x * 3)           \ny = int(node.graphObject_.y * 3)\n\nbID = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) ).ID \neID = self.getMatched ( graphID , self.LHS.nodeWithLabel(2) ).ID \nnewEdges(Pns2Xml_GG_exec.edges , nodeRate , node.ID ,  x ,  y ,  bID ,  eID )\n#,beginID = 0 , endID = 0, rate = 0 \nprint str(node.rate.getValue())+\' : \'+str(node.ID)\n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('Visit4EdgeMat', 20)
   cobj0.Order=ATOM3Integer(8)
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

   self.obj987=metarial(self)
   self.obj987.preAction( cobj0.LHS.CREATE )
   self.obj987.isGraphObjectVisual = True

   if(hasattr(self.obj987, '_setHierarchicalLink')):
     self.obj987._setHierarchicalLink(False)

   # MaxFlow
   self.obj987.MaxFlow.setNone()

   # price
   self.obj987.price.setNone()

   # Name
   self.obj987.Name.setValue('')
   self.obj987.Name.setNone()

   # ReqFlow
   self.obj987.ReqFlow.setNone()

   self.obj987.GGLabel.setValue(2)
   self.obj987.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(240.0,140.0,self.obj987)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj987.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj987)
   self.obj987.postAction( cobj0.LHS.CREATE )

   self.obj988=operatingUnit(self)
   self.obj988.preAction( cobj0.LHS.CREATE )
   self.obj988.isGraphObjectVisual = True

   if(hasattr(self.obj988, '_setHierarchicalLink')):
     self.obj988._setHierarchicalLink(False)

   # OperCostProp
   self.obj988.OperCostProp.setNone()

   # name
   self.obj988.name.setValue('')
   self.obj988.name.setNone()

   # OperCostFix
   self.obj988.OperCostFix.setNone()

   self.obj988.GGLabel.setValue(1)
   self.obj988.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(220.0,20.0,self.obj988)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj988.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj988)
   self.obj988.postAction( cobj0.LHS.CREATE )

   self.obj989=intoMaterial(self)
   self.obj989.preAction( cobj0.LHS.CREATE )
   self.obj989.isGraphObjectVisual = True

   if(hasattr(self.obj989, '_setHierarchicalLink')):
     self.obj989._setHierarchicalLink(False)

   # rate
   self.obj989.rate.setNone()

   self.obj989.GGLabel.setValue(3)
   self.obj989.graphClass_= graph_intoMaterial
   if self.genGraphics:
      new_obj = graph_intoMaterial(269.5,88.0,self.obj989)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj989.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj989)
   self.obj989.postAction( cobj0.LHS.CREATE )

   self.obj988.out_connections_.append(self.obj989)
   self.obj989.in_connections_.append(self.obj988)
   self.obj988.graphObject_.pendingConnections.append((self.obj988.graphObject_.tag, self.obj989.graphObject_.tag, [273.0, 38.0, 269.5, 88.0], 0, True))
   self.obj989.out_connections_.append(self.obj987)
   self.obj987.in_connections_.append(self.obj989)
   self.obj989.graphObject_.pendingConnections.append((self.obj989.graphObject_.tag, self.obj987.graphObject_.tag, [266.0, 138.0, 269.5, 88.0], 0, True))

   cobj0.RHS = ASG_pns(self)

   self.obj991=metarial(self)
   self.obj991.preAction( cobj0.RHS.CREATE )
   self.obj991.isGraphObjectVisual = True

   if(hasattr(self.obj991, '_setHierarchicalLink')):
     self.obj991._setHierarchicalLink(False)

   # MaxFlow
   self.obj991.MaxFlow.setNone()

   # price
   self.obj991.price.setNone()

   # Name
   self.obj991.Name.setValue('')
   self.obj991.Name.setNone()

   # ReqFlow
   self.obj991.ReqFlow.setNone()

   self.obj991.GGLabel.setValue(2)
   self.obj991.graphClass_= graph_metarial
   if self.genGraphics:
      new_obj = graph_metarial(240.0,140.0,self.obj991)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj991.graphObject_ = new_obj
   self.obj9910= AttrCalc()
   self.obj9910.Copy=ATOM3Boolean()
   self.obj9910.Copy.setValue(('Copy from LHS', 1))
   self.obj9910.Copy.config = 0
   self.obj9910.Specify=ATOM3Constraint()
   self.obj9910.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj991.GGset2Any['MaxFlow']= self.obj9910
   self.obj9911= AttrCalc()
   self.obj9911.Copy=ATOM3Boolean()
   self.obj9911.Copy.setValue(('Copy from LHS', 1))
   self.obj9911.Copy.config = 0
   self.obj9911.Specify=ATOM3Constraint()
   self.obj9911.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj991.GGset2Any['price']= self.obj9911
   self.obj9912= AttrCalc()
   self.obj9912.Copy=ATOM3Boolean()
   self.obj9912.Copy.setValue(('Copy from LHS', 1))
   self.obj9912.Copy.config = 0
   self.obj9912.Specify=ATOM3Constraint()
   self.obj9912.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj991.GGset2Any['Name']= self.obj9912
   self.obj9913= AttrCalc()
   self.obj9913.Copy=ATOM3Boolean()
   self.obj9913.Copy.setValue(('Copy from LHS', 1))
   self.obj9913.Copy.config = 0
   self.obj9913.Specify=ATOM3Constraint()
   self.obj9913.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj991.GGset2Any['ReqFlow']= self.obj9913

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj991)
   self.obj991.postAction( cobj0.RHS.CREATE )

   self.obj992=operatingUnit(self)
   self.obj992.preAction( cobj0.RHS.CREATE )
   self.obj992.isGraphObjectVisual = True

   if(hasattr(self.obj992, '_setHierarchicalLink')):
     self.obj992._setHierarchicalLink(False)

   # OperCostProp
   self.obj992.OperCostProp.setNone()

   # name
   self.obj992.name.setValue('')
   self.obj992.name.setNone()

   # OperCostFix
   self.obj992.OperCostFix.setNone()

   self.obj992.GGLabel.setValue(1)
   self.obj992.graphClass_= graph_operatingUnit
   if self.genGraphics:
      new_obj = graph_operatingUnit(220.0,20.0,self.obj992)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj992.graphObject_ = new_obj
   self.obj9920= AttrCalc()
   self.obj9920.Copy=ATOM3Boolean()
   self.obj9920.Copy.setValue(('Copy from LHS', 1))
   self.obj9920.Copy.config = 0
   self.obj9920.Specify=ATOM3Constraint()
   self.obj9920.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj992.GGset2Any['OperCostProp']= self.obj9920
   self.obj9921= AttrCalc()
   self.obj9921.Copy=ATOM3Boolean()
   self.obj9921.Copy.setValue(('Copy from LHS', 1))
   self.obj9921.Copy.config = 0
   self.obj9921.Specify=ATOM3Constraint()
   self.obj9921.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj992.GGset2Any['name']= self.obj9921
   self.obj9922= AttrCalc()
   self.obj9922.Copy=ATOM3Boolean()
   self.obj9922.Copy.setValue(('Copy from LHS', 1))
   self.obj9922.Copy.config = 0
   self.obj9922.Specify=ATOM3Constraint()
   self.obj9922.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj992.GGset2Any['OperCostFix']= self.obj9922

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj992)
   self.obj992.postAction( cobj0.RHS.CREATE )

   self.obj993=intoMaterial(self)
   self.obj993.preAction( cobj0.RHS.CREATE )
   self.obj993.isGraphObjectVisual = True

   if(hasattr(self.obj993, '_setHierarchicalLink')):
     self.obj993._setHierarchicalLink(False)

   # rate
   self.obj993.rate.setNone()

   self.obj993.GGLabel.setValue(3)
   self.obj993.graphClass_= graph_intoMaterial
   if self.genGraphics:
      new_obj = graph_intoMaterial(269.5,88.0,self.obj993)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj993.graphObject_ = new_obj
   self.obj9930= AttrCalc()
   self.obj9930.Copy=ATOM3Boolean()
   self.obj9930.Copy.setValue(('Copy from LHS', 1))
   self.obj9930.Copy.config = 0
   self.obj9930.Specify=ATOM3Constraint()
   self.obj9930.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj993.GGset2Any['rate']= self.obj9930

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj993)
   self.obj993.postAction( cobj0.RHS.CREATE )

   self.obj992.out_connections_.append(self.obj993)
   self.obj993.in_connections_.append(self.obj992)
   self.obj992.graphObject_.pendingConnections.append((self.obj992.graphObject_.tag, self.obj993.graphObject_.tag, [273.0, 28.0, 269.5, 88.0], 2, 0))
   self.obj993.out_connections_.append(self.obj991)
   self.obj991.in_connections_.append(self.obj993)
   self.obj993.graphObject_.pendingConnections.append((self.obj993.graphObject_.tag, self.obj991.graphObject_.tag, [286.0, 150.0, 269.5, 88.0], 2, 0))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'node = self.getMatched(graphID, self.LHS.nodeWithLabel(3))\nreturn not hasattr(node, "ID")\n\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n\n# code action of rule \nfrom MyFunction import *\nimport Pns2Xml_GG_exec \nPns2Xml_GG_exec.iD = Pns2Xml_GG_exec.iD + 1 \nprint \'global iD : \'+str(Pns2Xml_GG_exec.iD)\n\nnode = self.getMatched ( graphID , self.LHS.nodeWithLabel(3) )\nnode.ID =   Pns2Xml_GG_exec.iD\n#nodeName = node.name.getValue() # name of the node \'Agent\'\nnodeRate = node.rate.getValue()\nx = int (node.graphObject_.x * 3)           \ny = int(node.graphObject_.y * 3)\n\nbID = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) ).ID \neID = self.getMatched ( graphID , self.LHS.nodeWithLabel(2) ).ID \nnewEdges(Pns2Xml_GG_exec.edges , nodeRate , node.ID ,  x ,  y ,  bID ,  eID )\n#,beginID = 0 , endID = 0, rate = 0 \nprint str(node.rate.getValue())+\' : \'+str(node.ID)\n\n'))
   lcobj0.append(cobj0)
   self.EditingGraphGrammar.Rules.setValue(lcobj0)
   self.EditingGraphGrammar.InitialAction=ATOM3Constraint()
   self.EditingGraphGrammar.InitialAction.setValue(('constraint', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'global iD\niD = 1\nglobal ET\nimport xml.etree.cElementTree as ET\n# main Nodes\nglobal pgraph \npgraph = ET.Element("PGraph")\nglobal materials\nmaterials = ET.SubElement(pgraph, "Materials")\nglobal edges\nedges = ET.SubElement(pgraph, "Edges")\nglobal opunits\nopunits = ET.SubElement(pgraph, "OperatingUnits") \n\n'))
   self.EditingGraphGrammar.FinalAction=ATOM3Constraint()
   self.EditingGraphGrammar.FinalAction.setValue(('constraint', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'import Pns2Xml_GG_exec\nimport time \nimport os\n\nprint \'Start Final Action \'\nname  = str(os.getcwd())+\'/pns\'+str(int(time.time()))+\'.pgsx\'\nprint name\ntree = Pns2Xml_GG_exec.ET.ElementTree( Pns2Xml_GG_exec.pgraph )\ntree.write(name,xml_declaration=True,encoding="utf-8",method ="xml")\n\nprint \'End Final Action \'\n\n'))


