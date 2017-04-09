# _ VisitOpUnit_GG_rule.py ____________________________________________________________________________
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
class VisitOpUnit_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 4)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_pns(parent)

      self.obj947=operatingUnit(parent)
      self.obj947.preAction( self.LHS.CREATE )
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
      if parent.genGraphics:
         new_obj = graph_operatingUnit(200.0,40.0,self.obj947)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj947.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj947)
      self.obj947.postAction( self.LHS.CREATE )


      self.RHS = ASG_pns(parent)

      self.obj949=operatingUnit(parent)
      self.obj949.preAction( self.RHS.CREATE )
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
      if parent.genGraphics:
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

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj949)
      self.obj949.postAction( self.RHS.CREATE )


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
      nodeName = node.name.getValue() # name of the node 'Agent'
      x = int (node.graphObject_.x * 3)           
      y = int(node.graphObject_.y * 3)
      #newNode(  Pns2Xml_GG_exec.materials , nodeName , node.ID , 0 , x , y ,price=node.price.getValue()  ) opunits
      newOpUnit(  Pns2Xml_GG_exec.opunits , nodeName , node.ID  , x , y , node.OperCostProp.getValue() ,node.OperCostFix.getValue()  )
      #,beginID = 0 , endID = 0, rate = 0 
      print nodeName+' : '+str(node.ID)
      
      

