# _ ComputeSol_GG_rule.py ____________________________________________________________________________
# File generated automatically by ATOM3. Graph Grammar Rule
# ___________________________________________________________________________________________
from GGrule import *
from rawMaterial import *
from ASG_pns import *
from operatingUnit import *
from metarial import *
from product import *
from fromMaterial import *
from intoProduct import *
from fromRaw import *
from intoMaterial import *
class ComputeSol_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 1)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_pns(parent)

      self.obj107=rawMaterial(parent)
      self.obj107.preAction( self.LHS.CREATE )
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
      if parent.genGraphics:
         new_obj = graph_rawMaterial(60.0,20.0,self.obj107)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj107.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj107)
      self.obj107.postAction( self.LHS.CREATE )

      self.obj108=metarial(parent)
      self.obj108.preAction( self.LHS.CREATE )
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
      if parent.genGraphics:
         new_obj = graph_metarial(360.0,160.0,self.obj108)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj108.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj108)
      self.obj108.postAction( self.LHS.CREATE )

      self.obj109=operatingUnit(parent)
      self.obj109.preAction( self.LHS.CREATE )
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
      if parent.genGraphics:
         new_obj = graph_operatingUnit(180.0,120.0,self.obj109)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj109.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj109)
      self.obj109.postAction( self.LHS.CREATE )

      self.obj110=fromRaw(parent)
      self.obj110.preAction( self.LHS.CREATE )
      self.obj110.isGraphObjectVisual = True

      if(hasattr(self.obj110, '_setHierarchicalLink')):
        self.obj110._setHierarchicalLink(False)

      # rate
      self.obj110.rate.setNone()

      self.obj110.GGLabel.setValue(3)
      self.obj110.graphClass_= graph_fromRaw
      if parent.genGraphics:
         new_obj = graph_fromRaw(135.5,78.0,self.obj110)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj110.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj110)
      self.obj110.postAction( self.LHS.CREATE )

      self.obj111=intoMaterial(parent)
      self.obj111.preAction( self.LHS.CREATE )
      self.obj111.isGraphObjectVisual = True

      if(hasattr(self.obj111, '_setHierarchicalLink')):
        self.obj111._setHierarchicalLink(False)

      # rate
      self.obj111.rate.setNone()

      self.obj111.GGLabel.setValue(5)
      self.obj111.graphClass_= graph_intoMaterial
      if parent.genGraphics:
         new_obj = graph_intoMaterial(291.5,140.5,self.obj111)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj111.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj111)
      self.obj111.postAction( self.LHS.CREATE )

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

      self.RHS = ASG_pns(parent)

      self.obj113=rawMaterial(parent)
      self.obj113.preAction( self.RHS.CREATE )
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
      if parent.genGraphics:
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

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj113)
      self.obj113.postAction( self.RHS.CREATE )

      self.obj114=metarial(parent)
      self.obj114.preAction( self.RHS.CREATE )
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
      if parent.genGraphics:
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

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj114)
      self.obj114.postAction( self.RHS.CREATE )

      self.obj115=operatingUnit(parent)
      self.obj115.preAction( self.RHS.CREATE )
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
      if parent.genGraphics:
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

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj115)
      self.obj115.postAction( self.RHS.CREATE )

      self.obj116=fromRaw(parent)
      self.obj116.preAction( self.RHS.CREATE )
      self.obj116.isGraphObjectVisual = True

      if(hasattr(self.obj116, '_setHierarchicalLink')):
        self.obj116._setHierarchicalLink(False)

      # rate
      self.obj116.rate.setNone()

      self.obj116.GGLabel.setValue(3)
      self.obj116.graphClass_= graph_fromRaw
      if parent.genGraphics:
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

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj116)
      self.obj116.postAction( self.RHS.CREATE )

      self.obj117=intoMaterial(parent)
      self.obj117.preAction( self.RHS.CREATE )
      self.obj117.isGraphObjectVisual = True

      if(hasattr(self.obj117, '_setHierarchicalLink')):
        self.obj117._setHierarchicalLink(False)

      # rate
      self.obj117.rate.setNone()

      self.obj117.GGLabel.setValue(5)
      self.obj117.graphClass_= graph_intoMaterial
      if parent.genGraphics:
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

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj117)
      self.obj117.postAction( self.RHS.CREATE )

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

   def condition(self, graphID, isograph, atom3i):
      agent = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      mat = self.getMatched(graphID, self.LHS.nodeWithLabel(4))
      op = self.getMatched(graphID, self.LHS.nodeWithLabel(2))
      return not ( hasattr(agent,"done") and hasattr(op,"done") and hasattr(mat,"done") )
      
      

   def action(self, graphID, isograph, atom3i):
      import OptimalPNS_GG_exec 
      agent = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      agent.done = 1 
      op = self.getMatched(graphID, self.LHS.nodeWithLabel(2))
      op.done = 1
      mat = self.getMatched(graphID, self.LHS.nodeWithLabel(4))
      mat.done = 1
      
      if not ( op.name.getValue() in  OptimalPNS_GG_exec.Agentdict.keys() ):
       OptimalPNS_GG_exec.Agentdict[ op.name.getValue() ]=0
      OptimalPNS_GG_exec.Agentdict[ op.name.getValue() ] += 1
      if not ( op.name.getValue() in  OptimalPNS_GG_exec.Agentnode.keys() ):
       OptimalPNS_GG_exec.Agentnode[ op.name.getValue()]=[]
      OptimalPNS_GG_exec.Agentnode[op.name.getValue()].append(OptimalPNS_GG_exec.ind)
      OptimalPNS_GG_exec.dictWord[OptimalPNS_GG_exec.ind]=mat.Name.getValue()
      OptimalPNS_GG_exec.ind+=1
      
      

