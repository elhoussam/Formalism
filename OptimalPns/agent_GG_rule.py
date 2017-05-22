# _ agent_GG_rule.py ____________________________________________________________________________
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
class agent_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 1)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_pns(parent)

      self.obj91=rawMaterial(parent)
      self.obj91.preAction( self.LHS.CREATE )
      self.obj91.isGraphObjectVisual = True

      if(hasattr(self.obj91, '_setHierarchicalLink')):
        self.obj91._setHierarchicalLink(False)

      # MaxFlow
      self.obj91.MaxFlow.setNone()

      # price
      self.obj91.price.setNone()

      # Name
      self.obj91.Name.setValue('')
      self.obj91.Name.setNone()

      # ReqFlow
      self.obj91.ReqFlow.setNone()

      self.obj91.GGLabel.setValue(1)
      self.obj91.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(60.0,20.0,self.obj91)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj91.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj91)
      self.obj91.postAction( self.LHS.CREATE )

      self.obj92=metarial(parent)
      self.obj92.preAction( self.LHS.CREATE )
      self.obj92.isGraphObjectVisual = True

      if(hasattr(self.obj92, '_setHierarchicalLink')):
        self.obj92._setHierarchicalLink(False)

      # MaxFlow
      self.obj92.MaxFlow.setNone()

      # price
      self.obj92.price.setNone()

      # Name
      self.obj92.Name.setValue('')
      self.obj92.Name.setNone()

      # ReqFlow
      self.obj92.ReqFlow.setNone()

      self.obj92.GGLabel.setValue(4)
      self.obj92.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(360.0,160.0,self.obj92)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj92.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj92)
      self.obj92.postAction( self.LHS.CREATE )

      self.obj93=operatingUnit(parent)
      self.obj93.preAction( self.LHS.CREATE )
      self.obj93.isGraphObjectVisual = True

      if(hasattr(self.obj93, '_setHierarchicalLink')):
        self.obj93._setHierarchicalLink(False)

      # OperCostProp
      self.obj93.OperCostProp.setNone()

      # name
      self.obj93.name.setValue('')
      self.obj93.name.setNone()

      # OperCostFix
      self.obj93.OperCostFix.setNone()

      self.obj93.GGLabel.setValue(2)
      self.obj93.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(160.0,100.0,self.obj93)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj93.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj93)
      self.obj93.postAction( self.LHS.CREATE )

      self.obj94=fromRaw(parent)
      self.obj94.preAction( self.LHS.CREATE )
      self.obj94.isGraphObjectVisual = True

      if(hasattr(self.obj94, '_setHierarchicalLink')):
        self.obj94._setHierarchicalLink(False)

      # rate
      self.obj94.rate.setNone()

      self.obj94.GGLabel.setValue(3)
      self.obj94.graphClass_= graph_fromRaw
      if parent.genGraphics:
         new_obj = graph_fromRaw(135.5,78.0,self.obj94)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj94.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj94)
      self.obj94.postAction( self.LHS.CREATE )

      self.obj95=intoMaterial(parent)
      self.obj95.preAction( self.LHS.CREATE )
      self.obj95.isGraphObjectVisual = True

      if(hasattr(self.obj95, '_setHierarchicalLink')):
        self.obj95._setHierarchicalLink(False)

      # rate
      self.obj95.rate.setNone()

      self.obj95.GGLabel.setValue(5)
      self.obj95.graphClass_= graph_intoMaterial
      if parent.genGraphics:
         new_obj = graph_intoMaterial(291.5,140.5,self.obj95)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj95.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj95)
      self.obj95.postAction( self.LHS.CREATE )

      self.obj91.out_connections_.append(self.obj94)
      self.obj94.in_connections_.append(self.obj91)
      self.obj91.graphObject_.pendingConnections.append((self.obj91.graphObject_.tag, self.obj94.graphObject_.tag, [84.0, 76.0, 84.0, 118.0, 135.5, 78.0], 2, True))
      self.obj93.out_connections_.append(self.obj95)
      self.obj95.in_connections_.append(self.obj93)
      self.obj93.graphObject_.pendingConnections.append((self.obj93.graphObject_.tag, self.obj95.graphObject_.tag, [213.0, 118.0, 212.0, 177.0, 291.5, 140.5], 2, True))
      self.obj94.out_connections_.append(self.obj93)
      self.obj93.in_connections_.append(self.obj94)
      self.obj94.graphObject_.pendingConnections.append((self.obj94.graphObject_.tag, self.obj93.graphObject_.tag, [180.0, 111.0, 187.0, 38.0, 135.5, 78.0], 2, True))
      self.obj95.out_connections_.append(self.obj92)
      self.obj92.in_connections_.append(self.obj95)
      self.obj95.graphObject_.pendingConnections.append((self.obj95.graphObject_.tag, self.obj92.graphObject_.tag, [386.0, 158.0, 371.0, 104.0, 291.5, 140.5], 2, True))

      self.RHS = ASG_pns(parent)

      self.obj97=rawMaterial(parent)
      self.obj97.preAction( self.RHS.CREATE )
      self.obj97.isGraphObjectVisual = True

      if(hasattr(self.obj97, '_setHierarchicalLink')):
        self.obj97._setHierarchicalLink(False)

      # MaxFlow
      self.obj97.MaxFlow.setNone()

      # price
      self.obj97.price.setNone()

      # Name
      self.obj97.Name.setValue('')
      self.obj97.Name.setNone()

      # ReqFlow
      self.obj97.ReqFlow.setNone()

      self.obj97.GGLabel.setValue(1)
      self.obj97.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(60.0,20.0,self.obj97)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj97.graphObject_ = new_obj
      self.obj970= AttrCalc()
      self.obj970.Copy=ATOM3Boolean()
      self.obj970.Copy.setValue(('Copy from LHS', 1))
      self.obj970.Copy.config = 0
      self.obj970.Specify=ATOM3Constraint()
      self.obj970.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj97.GGset2Any['MaxFlow']= self.obj970
      self.obj971= AttrCalc()
      self.obj971.Copy=ATOM3Boolean()
      self.obj971.Copy.setValue(('Copy from LHS', 1))
      self.obj971.Copy.config = 0
      self.obj971.Specify=ATOM3Constraint()
      self.obj971.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj97.GGset2Any['price']= self.obj971
      self.obj972= AttrCalc()
      self.obj972.Copy=ATOM3Boolean()
      self.obj972.Copy.setValue(('Copy from LHS', 1))
      self.obj972.Copy.config = 0
      self.obj972.Specify=ATOM3Constraint()
      self.obj972.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj97.GGset2Any['Name']= self.obj972
      self.obj973= AttrCalc()
      self.obj973.Copy=ATOM3Boolean()
      self.obj973.Copy.setValue(('Copy from LHS', 1))
      self.obj973.Copy.config = 0
      self.obj973.Specify=ATOM3Constraint()
      self.obj973.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj97.GGset2Any['ReqFlow']= self.obj973

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj97)
      self.obj97.postAction( self.RHS.CREATE )

      self.obj98=metarial(parent)
      self.obj98.preAction( self.RHS.CREATE )
      self.obj98.isGraphObjectVisual = True

      if(hasattr(self.obj98, '_setHierarchicalLink')):
        self.obj98._setHierarchicalLink(False)

      # MaxFlow
      self.obj98.MaxFlow.setNone()

      # price
      self.obj98.price.setNone()

      # Name
      self.obj98.Name.setValue('')
      self.obj98.Name.setNone()

      # ReqFlow
      self.obj98.ReqFlow.setNone()

      self.obj98.GGLabel.setValue(4)
      self.obj98.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(360.0,160.0,self.obj98)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj98.graphObject_ = new_obj
      self.obj980= AttrCalc()
      self.obj980.Copy=ATOM3Boolean()
      self.obj980.Copy.setValue(('Copy from LHS', 1))
      self.obj980.Copy.config = 0
      self.obj980.Specify=ATOM3Constraint()
      self.obj980.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj98.GGset2Any['MaxFlow']= self.obj980
      self.obj981= AttrCalc()
      self.obj981.Copy=ATOM3Boolean()
      self.obj981.Copy.setValue(('Copy from LHS', 1))
      self.obj981.Copy.config = 0
      self.obj981.Specify=ATOM3Constraint()
      self.obj981.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj98.GGset2Any['price']= self.obj981
      self.obj982= AttrCalc()
      self.obj982.Copy=ATOM3Boolean()
      self.obj982.Copy.setValue(('Copy from LHS', 1))
      self.obj982.Copy.config = 0
      self.obj982.Specify=ATOM3Constraint()
      self.obj982.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj98.GGset2Any['Name']= self.obj982
      self.obj983= AttrCalc()
      self.obj983.Copy=ATOM3Boolean()
      self.obj983.Copy.setValue(('Copy from LHS', 1))
      self.obj983.Copy.config = 0
      self.obj983.Specify=ATOM3Constraint()
      self.obj983.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj98.GGset2Any['ReqFlow']= self.obj983

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj98)
      self.obj98.postAction( self.RHS.CREATE )

      self.obj99=operatingUnit(parent)
      self.obj99.preAction( self.RHS.CREATE )
      self.obj99.isGraphObjectVisual = True

      if(hasattr(self.obj99, '_setHierarchicalLink')):
        self.obj99._setHierarchicalLink(False)

      # OperCostProp
      self.obj99.OperCostProp.setNone()

      # name
      self.obj99.name.setValue('')
      self.obj99.name.setNone()

      # OperCostFix
      self.obj99.OperCostFix.setNone()

      self.obj99.GGLabel.setValue(2)
      self.obj99.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(160.0,100.0,self.obj99)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj99.graphObject_ = new_obj
      self.obj990= AttrCalc()
      self.obj990.Copy=ATOM3Boolean()
      self.obj990.Copy.setValue(('Copy from LHS', 1))
      self.obj990.Copy.config = 0
      self.obj990.Specify=ATOM3Constraint()
      self.obj990.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj99.GGset2Any['OperCostProp']= self.obj990
      self.obj991= AttrCalc()
      self.obj991.Copy=ATOM3Boolean()
      self.obj991.Copy.setValue(('Copy from LHS', 1))
      self.obj991.Copy.config = 0
      self.obj991.Specify=ATOM3Constraint()
      self.obj991.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj99.GGset2Any['name']= self.obj991
      self.obj992= AttrCalc()
      self.obj992.Copy=ATOM3Boolean()
      self.obj992.Copy.setValue(('Copy from LHS', 1))
      self.obj992.Copy.config = 0
      self.obj992.Specify=ATOM3Constraint()
      self.obj992.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj99.GGset2Any['OperCostFix']= self.obj992

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj99)
      self.obj99.postAction( self.RHS.CREATE )

      self.obj100=fromRaw(parent)
      self.obj100.preAction( self.RHS.CREATE )
      self.obj100.isGraphObjectVisual = True

      if(hasattr(self.obj100, '_setHierarchicalLink')):
        self.obj100._setHierarchicalLink(False)

      # rate
      self.obj100.rate.setNone()

      self.obj100.GGLabel.setValue(3)
      self.obj100.graphClass_= graph_fromRaw
      if parent.genGraphics:
         new_obj = graph_fromRaw(135.5,78.0,self.obj100)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj100.graphObject_ = new_obj
      self.obj1000= AttrCalc()
      self.obj1000.Copy=ATOM3Boolean()
      self.obj1000.Copy.setValue(('Copy from LHS', 1))
      self.obj1000.Copy.config = 0
      self.obj1000.Specify=ATOM3Constraint()
      self.obj1000.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj100.GGset2Any['rate']= self.obj1000

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj100)
      self.obj100.postAction( self.RHS.CREATE )

      self.obj101=intoMaterial(parent)
      self.obj101.preAction( self.RHS.CREATE )
      self.obj101.isGraphObjectVisual = True

      if(hasattr(self.obj101, '_setHierarchicalLink')):
        self.obj101._setHierarchicalLink(False)

      # rate
      self.obj101.rate.setNone()

      self.obj101.GGLabel.setValue(5)
      self.obj101.graphClass_= graph_intoMaterial
      if parent.genGraphics:
         new_obj = graph_intoMaterial(291.5,140.5,self.obj101)
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
      self.obj101.GGset2Any['rate']= self.obj1010

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj101)
      self.obj101.postAction( self.RHS.CREATE )

      self.obj97.out_connections_.append(self.obj100)
      self.obj100.in_connections_.append(self.obj97)
      self.obj97.graphObject_.pendingConnections.append((self.obj97.graphObject_.tag, self.obj100.graphObject_.tag, [84.0, 70.0, 135.5, 78.0], 2, 0))
      self.obj99.out_connections_.append(self.obj101)
      self.obj101.in_connections_.append(self.obj99)
      self.obj99.graphObject_.pendingConnections.append((self.obj99.graphObject_.tag, self.obj101.graphObject_.tag, [213.0, 108.0, 291.5, 140.5], 2, 0))
      self.obj100.out_connections_.append(self.obj99)
      self.obj99.in_connections_.append(self.obj100)
      self.obj100.graphObject_.pendingConnections.append((self.obj100.graphObject_.tag, self.obj99.graphObject_.tag, [210.0, 101.0, 135.5, 78.0], 2, 0))
      self.obj101.out_connections_.append(self.obj98)
      self.obj98.in_connections_.append(self.obj101)
      self.obj101.graphObject_.pendingConnections.append((self.obj101.graphObject_.tag, self.obj98.graphObject_.tag, [370.0, 165.0, 291.5, 140.5], 2, 0))

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
      
      

