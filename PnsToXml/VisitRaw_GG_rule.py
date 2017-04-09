# _ VisitRaw_GG_rule.py ____________________________________________________________________________
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
class VisitRaw_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 1)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_pns(parent)

      self.obj926=rawMaterial(parent)
      self.obj926.preAction( self.LHS.CREATE )
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
      if parent.genGraphics:
         new_obj = graph_rawMaterial(160.0,40.0,self.obj926)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj926.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj926)
      self.obj926.postAction( self.LHS.CREATE )


      self.RHS = ASG_pns(parent)

      self.obj928=rawMaterial(parent)
      self.obj928.preAction( self.RHS.CREATE )
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
      if parent.genGraphics:
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

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj928)
      self.obj928.postAction( self.RHS.CREATE )


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
      newMaterial(  Pns2Xml_GG_exec.materials , nodeName , node.ID , 0 , x , y ,  node.price.getValue() , node.ReqFlow.getValue() ,node.MaxFlow.getValue()  )
      #,beginID = 0 , endID = 0, rate = 0 
      print node.Name.getValue()+' : '+str(node.ID)
      
      

