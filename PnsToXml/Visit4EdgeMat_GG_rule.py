# _ Visit4EdgeMat_GG_rule.py ____________________________________________________________________________
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
class Visit4EdgeMat_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 8)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_pns(parent)

      self.obj987=metarial(parent)
      self.obj987.preAction( self.LHS.CREATE )
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
      if parent.genGraphics:
         new_obj = graph_metarial(240.0,140.0,self.obj987)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj987.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj987)
      self.obj987.postAction( self.LHS.CREATE )

      self.obj988=operatingUnit(parent)
      self.obj988.preAction( self.LHS.CREATE )
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
      if parent.genGraphics:
         new_obj = graph_operatingUnit(220.0,20.0,self.obj988)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj988.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj988)
      self.obj988.postAction( self.LHS.CREATE )

      self.obj989=intoMaterial(parent)
      self.obj989.preAction( self.LHS.CREATE )
      self.obj989.isGraphObjectVisual = True

      if(hasattr(self.obj989, '_setHierarchicalLink')):
        self.obj989._setHierarchicalLink(False)

      # rate
      self.obj989.rate.setNone()

      self.obj989.GGLabel.setValue(3)
      self.obj989.graphClass_= graph_intoMaterial
      if parent.genGraphics:
         new_obj = graph_intoMaterial(269.5,88.0,self.obj989)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj989.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj989)
      self.obj989.postAction( self.LHS.CREATE )

      self.obj988.out_connections_.append(self.obj989)
      self.obj989.in_connections_.append(self.obj988)
      self.obj988.graphObject_.pendingConnections.append((self.obj988.graphObject_.tag, self.obj989.graphObject_.tag, [273.0, 38.0, 269.5, 88.0], 0, True))
      self.obj989.out_connections_.append(self.obj987)
      self.obj987.in_connections_.append(self.obj989)
      self.obj989.graphObject_.pendingConnections.append((self.obj989.graphObject_.tag, self.obj987.graphObject_.tag, [266.0, 138.0, 269.5, 88.0], 0, True))

      self.RHS = ASG_pns(parent)

      self.obj991=metarial(parent)
      self.obj991.preAction( self.RHS.CREATE )
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
      if parent.genGraphics:
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

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj991)
      self.obj991.postAction( self.RHS.CREATE )

      self.obj992=operatingUnit(parent)
      self.obj992.preAction( self.RHS.CREATE )
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
      if parent.genGraphics:
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

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj992)
      self.obj992.postAction( self.RHS.CREATE )

      self.obj993=intoMaterial(parent)
      self.obj993.preAction( self.RHS.CREATE )
      self.obj993.isGraphObjectVisual = True

      if(hasattr(self.obj993, '_setHierarchicalLink')):
        self.obj993._setHierarchicalLink(False)

      # rate
      self.obj993.rate.setNone()

      self.obj993.GGLabel.setValue(3)
      self.obj993.graphClass_= graph_intoMaterial
      if parent.genGraphics:
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

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj993)
      self.obj993.postAction( self.RHS.CREATE )

      self.obj992.out_connections_.append(self.obj993)
      self.obj993.in_connections_.append(self.obj992)
      self.obj992.graphObject_.pendingConnections.append((self.obj992.graphObject_.tag, self.obj993.graphObject_.tag, [273.0, 28.0, 269.5, 88.0], 2, 0))
      self.obj993.out_connections_.append(self.obj991)
      self.obj991.in_connections_.append(self.obj993)
      self.obj993.graphObject_.pendingConnections.append((self.obj993.graphObject_.tag, self.obj991.graphObject_.tag, [286.0, 150.0, 269.5, 88.0], 2, 0))

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
      
      

