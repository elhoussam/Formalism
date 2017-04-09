# _ Visit2EdgeFINAL_GG_rule.py ____________________________________________________________________________
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
class Visit2EdgeFINAL_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 6)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_pns(parent)

      self.obj965=product(parent)
      self.obj965.preAction( self.LHS.CREATE )
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
      if parent.genGraphics:
         new_obj = graph_product(220.0,140.0,self.obj965)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj965.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj965)
      self.obj965.postAction( self.LHS.CREATE )

      self.obj966=operatingUnit(parent)
      self.obj966.preAction( self.LHS.CREATE )
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
      if parent.genGraphics:
         new_obj = graph_operatingUnit(180.0,20.0,self.obj966)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj966.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj966)
      self.obj966.postAction( self.LHS.CREATE )

      self.obj967=intoProduct(parent)
      self.obj967.preAction( self.LHS.CREATE )
      self.obj967.isGraphObjectVisual = True

      if(hasattr(self.obj967, '_setHierarchicalLink')):
        self.obj967._setHierarchicalLink(False)

      # rate
      self.obj967.rate.setNone()

      self.obj967.GGLabel.setValue(3)
      self.obj967.graphClass_= graph_intoProduct
      if parent.genGraphics:
         new_obj = graph_intoProduct(239.0,89.0,self.obj967)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj967.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj967)
      self.obj967.postAction( self.LHS.CREATE )

      self.obj966.out_connections_.append(self.obj967)
      self.obj967.in_connections_.append(self.obj966)
      self.obj966.graphObject_.pendingConnections.append((self.obj966.graphObject_.tag, self.obj967.graphObject_.tag, [233.0, 38.0, 239.0, 89.0], 0, True))
      self.obj967.out_connections_.append(self.obj965)
      self.obj965.in_connections_.append(self.obj967)
      self.obj967.graphObject_.pendingConnections.append((self.obj967.graphObject_.tag, self.obj965.graphObject_.tag, [245.0, 140.0, 239.0, 89.0], 0, True))

      self.RHS = ASG_pns(parent)

      self.obj969=product(parent)
      self.obj969.preAction( self.RHS.CREATE )
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
      if parent.genGraphics:
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

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj969)
      self.obj969.postAction( self.RHS.CREATE )

      self.obj970=operatingUnit(parent)
      self.obj970.preAction( self.RHS.CREATE )
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
      if parent.genGraphics:
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

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj970)
      self.obj970.postAction( self.RHS.CREATE )

      self.obj971=intoProduct(parent)
      self.obj971.preAction( self.RHS.CREATE )
      self.obj971.isGraphObjectVisual = True

      if(hasattr(self.obj971, '_setHierarchicalLink')):
        self.obj971._setHierarchicalLink(False)

      # rate
      self.obj971.rate.setNone()

      self.obj971.GGLabel.setValue(3)
      self.obj971.graphClass_= graph_intoProduct
      if parent.genGraphics:
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

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj971)
      self.obj971.postAction( self.RHS.CREATE )

      self.obj970.out_connections_.append(self.obj971)
      self.obj971.in_connections_.append(self.obj970)
      self.obj970.graphObject_.pendingConnections.append((self.obj970.graphObject_.tag, self.obj971.graphObject_.tag, [233.0, 28.0, 239.0, 89.0], 2, 0))
      self.obj971.out_connections_.append(self.obj969)
      self.obj969.in_connections_.append(self.obj971)
      self.obj971.graphObject_.pendingConnections.append((self.obj971.graphObject_.tag, self.obj969.graphObject_.tag, [245.0, 140.0, 239.0, 89.0], 2, 0))

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
      
      

