# _ Visit3EdgeMat_GG_rule.py ____________________________________________________________________________
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
class Visit3EdgeMat_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 7)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_pns(parent)

      self.obj976=metarial(parent)
      self.obj976.preAction( self.LHS.CREATE )
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
      if parent.genGraphics:
         new_obj = graph_metarial(200.0,20.0,self.obj976)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj976.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj976)
      self.obj976.postAction( self.LHS.CREATE )

      self.obj977=operatingUnit(parent)
      self.obj977.preAction( self.LHS.CREATE )
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
      if parent.genGraphics:
         new_obj = graph_operatingUnit(220.0,160.0,self.obj977)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj977.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj977)
      self.obj977.postAction( self.LHS.CREATE )

      self.obj978=fromMaterial(parent)
      self.obj978.preAction( self.LHS.CREATE )
      self.obj978.isGraphObjectVisual = True

      if(hasattr(self.obj978, '_setHierarchicalLink')):
        self.obj978._setHierarchicalLink(False)

      # rate
      self.obj978.rate.setNone()

      self.obj978.GGLabel.setValue(3)
      self.obj978.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(232.0,120.0,self.obj978)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj978.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj978)
      self.obj978.postAction( self.LHS.CREATE )

      self.obj976.out_connections_.append(self.obj978)
      self.obj978.in_connections_.append(self.obj976)
      self.obj976.graphObject_.pendingConnections.append((self.obj976.graphObject_.tag, self.obj978.graphObject_.tag, [224.0, 69.0, 232.0, 120.0], 0, True))
      self.obj978.out_connections_.append(self.obj977)
      self.obj977.in_connections_.append(self.obj978)
      self.obj978.graphObject_.pendingConnections.append((self.obj978.graphObject_.tag, self.obj977.graphObject_.tag, [240.0, 171.0, 232.0, 120.0], 0, True))

      self.RHS = ASG_pns(parent)

      self.obj980=metarial(parent)
      self.obj980.preAction( self.RHS.CREATE )
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
      if parent.genGraphics:
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

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj980)
      self.obj980.postAction( self.RHS.CREATE )

      self.obj981=operatingUnit(parent)
      self.obj981.preAction( self.RHS.CREATE )
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
      if parent.genGraphics:
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

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj981)
      self.obj981.postAction( self.RHS.CREATE )

      self.obj982=fromMaterial(parent)
      self.obj982.preAction( self.RHS.CREATE )
      self.obj982.isGraphObjectVisual = True

      if(hasattr(self.obj982, '_setHierarchicalLink')):
        self.obj982._setHierarchicalLink(False)

      # rate
      self.obj982.rate.setNone()

      self.obj982.GGLabel.setValue(3)
      self.obj982.graphClass_= graph_fromMaterial
      if parent.genGraphics:
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

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj982)
      self.obj982.postAction( self.RHS.CREATE )

      self.obj980.out_connections_.append(self.obj982)
      self.obj982.in_connections_.append(self.obj980)
      self.obj980.graphObject_.pendingConnections.append((self.obj980.graphObject_.tag, self.obj982.graphObject_.tag, [224.0, 69.0, 232.0, 120.0], 2, 0))
      self.obj982.out_connections_.append(self.obj981)
      self.obj981.in_connections_.append(self.obj982)
      self.obj982.graphObject_.pendingConnections.append((self.obj982.graphObject_.tag, self.obj981.graphObject_.tag, [270.0, 161.0, 232.0, 120.0], 2, 0))

   def condition(self, graphID, isograph, atom3i):
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(3))
      return not hasattr(node, "ID")
      

   def action(self, graphID, isograph, atom3i):
      # code action of rule 
      from MyFunction import *
      import Pns2Xml_GG_exec 
      Pns2Xml_GG_exec.iD = Pns2Xml_GG_exec.iD + 1 
      print 'global iD : '+str(Pns2Xml_GG_exec.iD)
      
      node = self.getMatched ( graphID , self.LHS.nodeWithLabel(3) )
      node.ID =   Pns2Xml_GG_exec.iD
      #nodeName = node.name.getValue() # name of the node 'Agent'
      nodeRate = node.rate.getValue()
      x = int (node.graphObject_.x * 3)           
      y = int(node.graphObject_.y * 3)
      
      bID = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) ).ID 
      eID = self.getMatched ( graphID , self.LHS.nodeWithLabel(2) ).ID 
      newEdges(Pns2Xml_GG_exec.edges , nodeRate , node.ID ,  x ,  y ,  bID ,  eID )
      #,beginID = 0 , endID = 0, rate = 0 
      print str(node.rate.getValue())+' : '+str(node.ID)
      
      

