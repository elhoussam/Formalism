# _ VisitMat_GG_rule.py ____________________________________________________________________________
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
class VisitMat_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 2)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_pns(parent)

      self.obj933=metarial(parent)
      self.obj933.preAction( self.LHS.CREATE )
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
      if parent.genGraphics:
         new_obj = graph_metarial(140.0,60.0,self.obj933)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj933.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj933)
      self.obj933.postAction( self.LHS.CREATE )


      self.RHS = ASG_pns(parent)

      self.obj935=metarial(parent)
      self.obj935.preAction( self.RHS.CREATE )
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
      if parent.genGraphics:
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

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj935)
      self.obj935.postAction( self.RHS.CREATE )


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
      newMaterial(  Pns2Xml_GG_exec.materials , nodeName , node.ID , 1 , x , y ,  node.price.getValue() , node.ReqFlow.getValue() ,node.MaxFlow.getValue()  )
      #,beginID = 0 , endID = 0, rate = 0 
      print node.Name.getValue()+' : '+str(node.ID)
      
      

