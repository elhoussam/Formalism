# _ Visit1EdgeRAW_GG_rule.py ____________________________________________________________________________
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
class Visit1EdgeRAW_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 5)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_pns(parent)

      self.obj954=rawMaterial(parent)
      self.obj954.preAction( self.LHS.CREATE )
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
      if parent.genGraphics:
         new_obj = graph_rawMaterial(200.0,20.0,self.obj954)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj954.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj954)
      self.obj954.postAction( self.LHS.CREATE )

      self.obj955=operatingUnit(parent)
      self.obj955.preAction( self.LHS.CREATE )
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
      if parent.genGraphics:
         new_obj = graph_operatingUnit(200.0,160.0,self.obj955)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj955.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj955)
      self.obj955.postAction( self.LHS.CREATE )

      self.obj956=fromRaw(parent)
      self.obj956.preAction( self.LHS.CREATE )
      self.obj956.isGraphObjectVisual = True

      if(hasattr(self.obj956, '_setHierarchicalLink')):
        self.obj956._setHierarchicalLink(False)

      # rate
      self.obj956.rate.setNone()

      self.obj956.GGLabel.setValue(3)
      self.obj956.graphClass_= graph_fromRaw
      if parent.genGraphics:
         new_obj = graph_fromRaw(222.0,123.5,self.obj956)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj956.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj956)
      self.obj956.postAction( self.LHS.CREATE )

      self.obj954.out_connections_.append(self.obj956)
      self.obj956.in_connections_.append(self.obj954)
      self.obj954.graphObject_.pendingConnections.append((self.obj954.graphObject_.tag, self.obj956.graphObject_.tag, [224.0, 76.0, 222.0, 123.5], 0, True))
      self.obj956.out_connections_.append(self.obj955)
      self.obj955.in_connections_.append(self.obj956)
      self.obj956.graphObject_.pendingConnections.append((self.obj956.graphObject_.tag, self.obj955.graphObject_.tag, [220.0, 171.0, 222.0, 123.5], 0, True))

      self.RHS = ASG_pns(parent)

      self.obj958=rawMaterial(parent)
      self.obj958.preAction( self.RHS.CREATE )
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
      if parent.genGraphics:
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

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj958)
      self.obj958.postAction( self.RHS.CREATE )

      self.obj959=operatingUnit(parent)
      self.obj959.preAction( self.RHS.CREATE )
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
      if parent.genGraphics:
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

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj959)
      self.obj959.postAction( self.RHS.CREATE )

      self.obj960=fromRaw(parent)
      self.obj960.preAction( self.RHS.CREATE )
      self.obj960.isGraphObjectVisual = True

      if(hasattr(self.obj960, '_setHierarchicalLink')):
        self.obj960._setHierarchicalLink(False)

      # rate
      self.obj960.rate.setNone()

      self.obj960.GGLabel.setValue(3)
      self.obj960.graphClass_= graph_fromRaw
      if parent.genGraphics:
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

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj960)
      self.obj960.postAction( self.RHS.CREATE )

      self.obj958.out_connections_.append(self.obj960)
      self.obj960.in_connections_.append(self.obj958)
      self.obj958.graphObject_.pendingConnections.append((self.obj958.graphObject_.tag, self.obj960.graphObject_.tag, [224.0, 70.0, 222.0, 123.5], 2, 0))
      self.obj960.out_connections_.append(self.obj959)
      self.obj959.in_connections_.append(self.obj960)
      self.obj960.graphObject_.pendingConnections.append((self.obj960.graphObject_.tag, self.obj959.graphObject_.tag, [250.0, 161.0, 222.0, 123.5], 2, 0))

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
      newEdges(  Pns2Xml_GG_exec.edges , nodeRate , node.ID  , x ,  y ,   bID , eID )
      #,beginID = 0 , endID = 0, rate = 0 
      print str(node.rate.getValue())+' : '+str(node.ID)
      
      

