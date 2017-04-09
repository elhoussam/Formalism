# _ VisitProduct_GG_rule.py ____________________________________________________________________________
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
class VisitProduct_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 3)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_pns(parent)

      self.obj940=product(parent)
      self.obj940.preAction( self.LHS.CREATE )
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
      if parent.genGraphics:
         new_obj = graph_product(200.0,60.0,self.obj940)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj940.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj940)
      self.obj940.postAction( self.LHS.CREATE )


      self.RHS = ASG_pns(parent)

      self.obj942=product(parent)
      self.obj942.preAction( self.RHS.CREATE )
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
      if parent.genGraphics:
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

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj942)
      self.obj942.postAction( self.RHS.CREATE )


   def condition(self, graphID, isograph, atom3i):
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      return not hasattr(node, "ID")
      

   def action(self, graphID, isograph, atom3i):
      # code action of rule 
      # Import Function && Variables
      from MyFunction import *
      import Pns2Xml_GG_exec 
      Pns2Xml_GG_exec.iD = Pns2Xml_GG_exec.iD + 1 
      print 'global iD : '+str(Pns2Xml_GG_exec.iD)
      #Add Node 
      node = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) )
      node.ID =   Pns2Xml_GG_exec.iD
      nodeName = node.Name.getValue() # name of the node 'Agent'
      x = int (node.graphObject_.x * 3)           
      y = int(node.graphObject_.y * 3)
      #newNode(  Pns2Xml_GG_exec.materials , nodeName , node.ID , 0 , x , y ,price=node.price.getValue()  )
      newMaterial(  Pns2Xml_GG_exec.materials , nodeName , node.ID , 2 , x , y ,  node.price.getValue() , node.ReqFlow.getValue() ,node.MaxFlow.getValue()  )
      #,beginID = 0 , endID = 0, rate = 0 
      print node.Name.getValue()+' : '+str(node.ID)
      
      

