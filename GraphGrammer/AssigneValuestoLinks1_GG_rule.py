# _ AssigneValuestoLinks1_GG_rule.py ____________________________________________________________________________
# File generated automatically by ATOM3. Graph Grammar Rule
# ___________________________________________________________________________________________
from GGrule import *
from CapableOf import *
from GenericGraphEdge import *
from Goal import *
from ASG_omacss import *
from intoProduct import *
from operatingUnit import *
from metarial import *
from rawMaterial import *
from Agent import *
from fromMaterial import *
from Capabilitie import *
from Role import *
from requir import *
from fromRaw import *
from ASG_pns2 import *
from intoMaterial import *
from ASG_GenericGraph import *
from product import *
from GenericGraphNode import *
from achieve import *
from posses import *
class AssigneValuestoLinks1_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 22)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_omacss(parent)
      self.LHS.merge(ASG_pns2(parent))
      self.LHS.merge(ASG_GenericGraph(parent))

      self.obj371=Agent(parent)
      self.obj371.preAction( self.LHS.CREATE )
      self.obj371.isGraphObjectVisual = True

      if(hasattr(self.obj371, '_setHierarchicalLink')):
        self.obj371._setHierarchicalLink(False)

      # price
      self.obj371.price.setNone()

      # name
      self.obj371.name.setValue('')
      self.obj371.name.setNone()

      self.obj371.GGLabel.setValue(1)
      self.obj371.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(100.0,20.0,self.obj371)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj371.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj371)
      self.obj371.postAction( self.LHS.CREATE )

      self.obj372=Role(parent)
      self.obj372.preAction( self.LHS.CREATE )
      self.obj372.isGraphObjectVisual = True

      if(hasattr(self.obj372, '_setHierarchicalLink')):
        self.obj372._setHierarchicalLink(False)

      # name
      self.obj372.name.setValue('')
      self.obj372.name.setNone()

      self.obj372.GGLabel.setValue(2)
      self.obj372.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(60.0,160.0,self.obj372)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj372.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj372)
      self.obj372.postAction( self.LHS.CREATE )

      self.obj373=rawMaterial(parent)
      self.obj373.preAction( self.LHS.CREATE )
      self.obj373.isGraphObjectVisual = True

      if(hasattr(self.obj373, '_setHierarchicalLink')):
        self.obj373._setHierarchicalLink(False)

      # Name
      self.obj373.Name.setValue('')
      self.obj373.Name.setNone()

      self.obj373.GGLabel.setValue(3)
      self.obj373.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(240.0,20.0,self.obj373)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj373.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj373)
      self.obj373.postAction( self.LHS.CREATE )

      self.obj374=operatingUnit(parent)
      self.obj374.preAction( self.LHS.CREATE )
      self.obj374.isGraphObjectVisual = True

      if(hasattr(self.obj374, '_setHierarchicalLink')):
        self.obj374._setHierarchicalLink(False)

      # name
      self.obj374.name.setValue('')
      self.obj374.name.setNone()

      self.obj374.GGLabel.setValue(4)
      self.obj374.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(260.0,100.0,self.obj374)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj374.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj374)
      self.obj374.postAction( self.LHS.CREATE )

      self.obj375=operatingUnit(parent)
      self.obj375.preAction( self.LHS.CREATE )
      self.obj375.isGraphObjectVisual = True

      if(hasattr(self.obj375, '_setHierarchicalLink')):
        self.obj375._setHierarchicalLink(False)

      # name
      self.obj375.name.setValue('')
      self.obj375.name.setNone()

      self.obj375.GGLabel.setValue(9)
      self.obj375.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(220.0,260.0,self.obj375)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj375.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj375)
      self.obj375.postAction( self.LHS.CREATE )

      self.obj376=metarial(parent)
      self.obj376.preAction( self.LHS.CREATE )
      self.obj376.isGraphObjectVisual = True

      if(hasattr(self.obj376, '_setHierarchicalLink')):
        self.obj376._setHierarchicalLink(False)

      # Name
      self.obj376.Name.setValue('')
      self.obj376.Name.setNone()

      self.obj376.GGLabel.setValue(7)
      self.obj376.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(240.0,160.0,self.obj376)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj376.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj376)
      self.obj376.postAction( self.LHS.CREATE )

      self.obj377=fromMaterial(parent)
      self.obj377.preAction( self.LHS.CREATE )
      self.obj377.isGraphObjectVisual = True

      if(hasattr(self.obj377, '_setHierarchicalLink')):
        self.obj377._setHierarchicalLink(False)

      # rate
      self.obj377.rate.setNone()

      self.obj377.GGLabel.setValue(10)
      self.obj377.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(262.663551402,238.736842105,self.obj377)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj377.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj377)
      self.obj377.postAction( self.LHS.CREATE )

      self.obj378=fromRaw(parent)
      self.obj378.preAction( self.LHS.CREATE )
      self.obj378.isGraphObjectVisual = True

      if(hasattr(self.obj378, '_setHierarchicalLink')):
        self.obj378._setHierarchicalLink(False)

      # rate
      self.obj378.rate.setNone()

      self.obj378.GGLabel.setValue(5)
      self.obj378.graphClass_= graph_fromRaw
      if parent.genGraphics:
         new_obj = graph_fromRaw(268.785046729,90.7105263158,self.obj378)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj378.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj378)
      self.obj378.postAction( self.LHS.CREATE )

      self.obj379=intoMaterial(parent)
      self.obj379.preAction( self.LHS.CREATE )
      self.obj379.isGraphObjectVisual = True

      if(hasattr(self.obj379, '_setHierarchicalLink')):
        self.obj379._setHierarchicalLink(False)

      # rate
      self.obj379.rate.setNone()

      self.obj379.GGLabel.setValue(11)
      self.obj379.graphClass_= graph_intoMaterial
      if parent.genGraphics:
         new_obj = graph_intoMaterial(271.093457944,138.263157895,self.obj379)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj379.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj379)
      self.obj379.postAction( self.LHS.CREATE )

      self.obj380=GenericGraphEdge(parent)
      self.obj380.preAction( self.LHS.CREATE )
      self.obj380.isGraphObjectVisual = True

      if(hasattr(self.obj380, '_setHierarchicalLink')):
        self.obj380._setHierarchicalLink(False)

      self.obj380.GGLabel.setValue(6)
      self.obj380.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(194.5,77.5,self.obj380)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj380.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj380)
      self.obj380.postAction( self.LHS.CREATE )

      self.obj381=GenericGraphEdge(parent)
      self.obj381.preAction( self.LHS.CREATE )
      self.obj381.isGraphObjectVisual = True

      if(hasattr(self.obj381, '_setHierarchicalLink')):
        self.obj381._setHierarchicalLink(False)

      self.obj381.GGLabel.setValue(8)
      self.obj381.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(168.0,163.0,self.obj381)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj381.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj381)
      self.obj381.postAction( self.LHS.CREATE )

      self.obj382=GenericGraphEdge(parent)
      self.obj382.preAction( self.LHS.CREATE )
      self.obj382.isGraphObjectVisual = True

      if(hasattr(self.obj382, '_setHierarchicalLink')):
        self.obj382._setHierarchicalLink(False)

      self.obj382.GGLabel.setValue(12)
      self.obj382.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(205.785046729,95.2105263158,self.obj382)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj382.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj382)
      self.obj382.postAction( self.LHS.CREATE )

      self.obj371.out_connections_.append(self.obj380)
      self.obj380.in_connections_.append(self.obj371)
      self.obj371.graphObject_.pendingConnections.append((self.obj371.graphObject_.tag, self.obj380.graphObject_.tag, [125.0, 82.0, 194.5, 77.5], 0, True))
      self.obj371.out_connections_.append(self.obj382)
      self.obj382.in_connections_.append(self.obj371)
      self.obj371.graphObject_.pendingConnections.append((self.obj371.graphObject_.tag, self.obj382.graphObject_.tag, [137.0, 82.0, 205.78504672897196, 95.21052631578948], 0, True))
      self.obj372.out_connections_.append(self.obj381)
      self.obj381.in_connections_.append(self.obj372)
      self.obj372.graphObject_.pendingConnections.append((self.obj372.graphObject_.tag, self.obj381.graphObject_.tag, [84.0, 161.0, 168.0, 163.0], 0, True))
      self.obj373.out_connections_.append(self.obj378)
      self.obj378.in_connections_.append(self.obj373)
      self.obj373.graphObject_.pendingConnections.append((self.obj373.graphObject_.tag, self.obj378.graphObject_.tag, [264.0, 73.0, 268.78504672897196, 90.71052631578948], 0, True))
      self.obj374.out_connections_.append(self.obj379)
      self.obj379.in_connections_.append(self.obj374)
      self.obj374.graphObject_.pendingConnections.append((self.obj374.graphObject_.tag, self.obj379.graphObject_.tag, [275.1869158878505, 115.5263157894737, 271.0934579439253, 138.26315789473685], 0, True))
      self.obj376.out_connections_.append(self.obj377)
      self.obj377.in_connections_.append(self.obj376)
      self.obj376.graphObject_.pendingConnections.append((self.obj376.graphObject_.tag, self.obj377.graphObject_.tag, [264.0, 210.0, 262.6635514018692, 238.73684210526315], 0, True))
      self.obj377.out_connections_.append(self.obj375)
      self.obj375.in_connections_.append(self.obj377)
      self.obj377.graphObject_.pendingConnections.append((self.obj377.graphObject_.tag, self.obj375.graphObject_.tag, [261.32710280373834, 267.4736842105263, 262.6635514018692, 238.73684210526315], 0, True))
      self.obj378.out_connections_.append(self.obj374)
      self.obj374.in_connections_.append(self.obj378)
      self.obj378.graphObject_.pendingConnections.append((self.obj378.graphObject_.tag, self.obj374.graphObject_.tag, [273.5700934579439, 108.42105263157895, 268.78504672897196, 90.71052631578948], 0, True))
      self.obj379.out_connections_.append(self.obj376)
      self.obj376.in_connections_.append(self.obj379)
      self.obj379.graphObject_.pendingConnections.append((self.obj379.graphObject_.tag, self.obj376.graphObject_.tag, [267.0, 161.0, 271.0934579439253, 138.26315789473685], 0, True))
      self.obj380.out_connections_.append(self.obj373)
      self.obj373.in_connections_.append(self.obj380)
      self.obj380.graphObject_.pendingConnections.append((self.obj380.graphObject_.tag, self.obj373.graphObject_.tag, [264.0, 73.0, 194.5, 77.5], 0, True))
      self.obj381.out_connections_.append(self.obj376)
      self.obj376.in_connections_.append(self.obj381)
      self.obj381.graphObject_.pendingConnections.append((self.obj381.graphObject_.tag, self.obj376.graphObject_.tag, [252.0, 165.0, 168.0, 163.0], 0, True))
      self.obj382.out_connections_.append(self.obj374)
      self.obj374.in_connections_.append(self.obj382)
      self.obj382.graphObject_.pendingConnections.append((self.obj382.graphObject_.tag, self.obj374.graphObject_.tag, [274.5700934579439, 108.42105263157895, 205.78504672897196, 95.21052631578948], 0, True))

      self.RHS = ASG_omacss(parent)
      self.RHS.merge(ASG_pns2(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj386=Agent(parent)
      self.obj386.preAction( self.RHS.CREATE )
      self.obj386.isGraphObjectVisual = True

      if(hasattr(self.obj386, '_setHierarchicalLink')):
        self.obj386._setHierarchicalLink(False)

      # price
      self.obj386.price.setValue(0)

      # name
      self.obj386.name.setValue('')
      self.obj386.name.setNone()

      self.obj386.GGLabel.setValue(1)
      self.obj386.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(40.0,40.0,self.obj386)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj386.graphObject_ = new_obj
      self.obj3860= AttrCalc()
      self.obj3860.Copy=ATOM3Boolean()
      self.obj3860.Copy.setValue(('Copy from LHS', 1))
      self.obj3860.Copy.config = 0
      self.obj3860.Specify=ATOM3Constraint()
      self.obj3860.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj386.GGset2Any['price']= self.obj3860
      self.obj3861= AttrCalc()
      self.obj3861.Copy=ATOM3Boolean()
      self.obj3861.Copy.setValue(('Copy from LHS', 1))
      self.obj3861.Copy.config = 0
      self.obj3861.Specify=ATOM3Constraint()
      self.obj3861.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj386.GGset2Any['name']= self.obj3861

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj386)
      self.obj386.postAction( self.RHS.CREATE )

      self.obj387=Role(parent)
      self.obj387.preAction( self.RHS.CREATE )
      self.obj387.isGraphObjectVisual = True

      if(hasattr(self.obj387, '_setHierarchicalLink')):
        self.obj387._setHierarchicalLink(False)

      # name
      self.obj387.name.setValue('')
      self.obj387.name.setNone()

      self.obj387.GGLabel.setValue(2)
      self.obj387.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(20.0,180.0,self.obj387)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj387.graphObject_ = new_obj
      self.obj3870= AttrCalc()
      self.obj3870.Copy=ATOM3Boolean()
      self.obj3870.Copy.setValue(('Copy from LHS', 1))
      self.obj3870.Copy.config = 0
      self.obj3870.Specify=ATOM3Constraint()
      self.obj3870.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj387.GGset2Any['name']= self.obj3870

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj387)
      self.obj387.postAction( self.RHS.CREATE )

      self.obj388=rawMaterial(parent)
      self.obj388.preAction( self.RHS.CREATE )
      self.obj388.isGraphObjectVisual = True

      if(hasattr(self.obj388, '_setHierarchicalLink')):
        self.obj388._setHierarchicalLink(False)

      # Name
      self.obj388.Name.setValue('')
      self.obj388.Name.setNone()

      self.obj388.GGLabel.setValue(3)
      self.obj388.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(200.0,20.0,self.obj388)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj388.graphObject_ = new_obj
      self.obj3880= AttrCalc()
      self.obj3880.Copy=ATOM3Boolean()
      self.obj3880.Copy.setValue(('Copy from LHS', 1))
      self.obj3880.Copy.config = 0
      self.obj3880.Specify=ATOM3Constraint()
      self.obj3880.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj388.GGset2Any['Name']= self.obj3880

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj388)
      self.obj388.postAction( self.RHS.CREATE )

      self.obj389=operatingUnit(parent)
      self.obj389.preAction( self.RHS.CREATE )
      self.obj389.isGraphObjectVisual = True

      if(hasattr(self.obj389, '_setHierarchicalLink')):
        self.obj389._setHierarchicalLink(False)

      # name
      self.obj389.name.setValue('')
      self.obj389.name.setNone()

      self.obj389.GGLabel.setValue(4)
      self.obj389.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(200.0,100.0,self.obj389)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj389.graphObject_ = new_obj
      self.obj3890= AttrCalc()
      self.obj3890.Copy=ATOM3Boolean()
      self.obj3890.Copy.setValue(('Copy from LHS', 1))
      self.obj3890.Copy.config = 0
      self.obj3890.Specify=ATOM3Constraint()
      self.obj3890.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj389.GGset2Any['name']= self.obj3890

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj389)
      self.obj389.postAction( self.RHS.CREATE )

      self.obj390=operatingUnit(parent)
      self.obj390.preAction( self.RHS.CREATE )
      self.obj390.isGraphObjectVisual = True

      if(hasattr(self.obj390, '_setHierarchicalLink')):
        self.obj390._setHierarchicalLink(False)

      # name
      self.obj390.name.setValue('')
      self.obj390.name.setNone()

      self.obj390.GGLabel.setValue(9)
      self.obj390.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(220.0,260.0,self.obj390)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj390.graphObject_ = new_obj
      self.obj3900= AttrCalc()
      self.obj3900.Copy=ATOM3Boolean()
      self.obj3900.Copy.setValue(('Copy from LHS', 1))
      self.obj3900.Copy.config = 0
      self.obj3900.Specify=ATOM3Constraint()
      self.obj3900.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj390.GGset2Any['name']= self.obj3900

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj390)
      self.obj390.postAction( self.RHS.CREATE )

      self.obj391=metarial(parent)
      self.obj391.preAction( self.RHS.CREATE )
      self.obj391.isGraphObjectVisual = True

      if(hasattr(self.obj391, '_setHierarchicalLink')):
        self.obj391._setHierarchicalLink(False)

      # Name
      self.obj391.Name.setValue('')
      self.obj391.Name.setNone()

      self.obj391.GGLabel.setValue(7)
      self.obj391.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(200.0,180.0,self.obj391)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj391.graphObject_ = new_obj
      self.obj3910= AttrCalc()
      self.obj3910.Copy=ATOM3Boolean()
      self.obj3910.Copy.setValue(('Copy from LHS', 1))
      self.obj3910.Copy.config = 0
      self.obj3910.Specify=ATOM3Constraint()
      self.obj3910.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj391.GGset2Any['Name']= self.obj3910

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj391)
      self.obj391.postAction( self.RHS.CREATE )

      self.obj392=fromMaterial(parent)
      self.obj392.preAction( self.RHS.CREATE )
      self.obj392.isGraphObjectVisual = True

      if(hasattr(self.obj392, '_setHierarchicalLink')):
        self.obj392._setHierarchicalLink(False)

      # rate
      self.obj392.rate.setValue(0.0)

      self.obj392.GGLabel.setValue(10)
      self.obj392.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(228.785046729,249.210526316,self.obj392)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj392.graphObject_ = new_obj
      self.obj3920= AttrCalc()
      self.obj3920.Copy=ATOM3Boolean()
      self.obj3920.Copy.setValue(('Copy from LHS', 1))
      self.obj3920.Copy.config = 0
      self.obj3920.Specify=ATOM3Constraint()
      self.obj3920.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj392.GGset2Any['rate']= self.obj3920

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj392)
      self.obj392.postAction( self.RHS.CREATE )

      self.obj393=fromRaw(parent)
      self.obj393.preAction( self.RHS.CREATE )
      self.obj393.isGraphObjectVisual = True

      if(hasattr(self.obj393, '_setHierarchicalLink')):
        self.obj393._setHierarchicalLink(False)

      # rate
      self.obj393.rate.setValue(0.0)

      self.obj393.GGLabel.setValue(5)
      self.obj393.graphClass_= graph_fromRaw
      if parent.genGraphics:
         new_obj = graph_fromRaw(218.785046729,90.7105263158,self.obj393)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj393.graphObject_ = new_obj
      self.obj3930= AttrCalc()
      self.obj3930.Copy=ATOM3Boolean()
      self.obj3930.Copy.setValue(('Copy from LHS', 1))
      self.obj3930.Copy.config = 0
      self.obj3930.Specify=ATOM3Constraint()
      self.obj3930.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj393.GGset2Any['rate']= self.obj3930

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj393)
      self.obj393.postAction( self.RHS.CREATE )

      self.obj394=intoMaterial(parent)
      self.obj394.preAction( self.RHS.CREATE )
      self.obj394.isGraphObjectVisual = True

      if(hasattr(self.obj394, '_setHierarchicalLink')):
        self.obj394._setHierarchicalLink(False)

      # rate
      self.obj394.rate.setValue(0.0)

      self.obj394.GGLabel.setValue(11)
      self.obj394.graphClass_= graph_intoMaterial
      if parent.genGraphics:
         new_obj = graph_intoMaterial(220.593457944,148.263157895,self.obj394)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj394.graphObject_ = new_obj
      self.obj3940= AttrCalc()
      self.obj3940.Copy=ATOM3Boolean()
      self.obj3940.Copy.setValue(('Copy from LHS', 0))
      self.obj3940.Copy.config = 0
      self.obj3940.Specify=ATOM3Constraint()
      self.obj3940.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.graphRewritingSystem.Dictag[ self.getMatched ( graphID , self.LHS.nodeWithLabel(1) ).name.getValue() ]\n\n\n\n\n\n\n\n\n\n'))
      self.obj394.GGset2Any['rate']= self.obj3940

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj394)
      self.obj394.postAction( self.RHS.CREATE )

      self.obj395=GenericGraphEdge(parent)
      self.obj395.preAction( self.RHS.CREATE )
      self.obj395.isGraphObjectVisual = True

      if(hasattr(self.obj395, '_setHierarchicalLink')):
        self.obj395._setHierarchicalLink(False)

      self.obj395.GGLabel.setValue(6)
      self.obj395.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(144.5,87.5,self.obj395)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj395.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj395)
      self.obj395.postAction( self.RHS.CREATE )

      self.obj396=GenericGraphEdge(parent)
      self.obj396.preAction( self.RHS.CREATE )
      self.obj396.isGraphObjectVisual = True

      if(hasattr(self.obj396, '_setHierarchicalLink')):
        self.obj396._setHierarchicalLink(False)

      self.obj396.GGLabel.setValue(8)
      self.obj396.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(128.0,183.0,self.obj396)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj396.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj396)
      self.obj396.postAction( self.RHS.CREATE )

      self.obj397=GenericGraphEdge(parent)
      self.obj397.preAction( self.RHS.CREATE )
      self.obj397.isGraphObjectVisual = True

      if(hasattr(self.obj397, '_setHierarchicalLink')):
        self.obj397._setHierarchicalLink(False)

      self.obj397.GGLabel.setValue(12)
      self.obj397.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(145.785046729,105.210526316,self.obj397)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj397.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj397)
      self.obj397.postAction( self.RHS.CREATE )

      self.obj386.out_connections_.append(self.obj395)
      self.obj395.in_connections_.append(self.obj386)
      self.obj386.graphObject_.pendingConnections.append((self.obj386.graphObject_.tag, self.obj395.graphObject_.tag, [65.0, 102.0, 144.5, 87.5], 0, True))
      self.obj386.out_connections_.append(self.obj397)
      self.obj397.in_connections_.append(self.obj386)
      self.obj386.graphObject_.pendingConnections.append((self.obj386.graphObject_.tag, self.obj397.graphObject_.tag, [77.0, 102.0, 145.78504672897196, 105.21052631578948], 0, True))
      self.obj387.out_connections_.append(self.obj396)
      self.obj396.in_connections_.append(self.obj387)
      self.obj387.graphObject_.pendingConnections.append((self.obj387.graphObject_.tag, self.obj396.graphObject_.tag, [44.0, 181.0, 128.0, 183.0], 0, True))
      self.obj388.out_connections_.append(self.obj393)
      self.obj393.in_connections_.append(self.obj388)
      self.obj388.graphObject_.pendingConnections.append((self.obj388.graphObject_.tag, self.obj393.graphObject_.tag, [224.0, 73.0, 218.78504672897196, 90.71052631578948], 0, True))
      self.obj389.out_connections_.append(self.obj394)
      self.obj394.in_connections_.append(self.obj389)
      self.obj389.graphObject_.pendingConnections.append((self.obj389.graphObject_.tag, self.obj394.graphObject_.tag, [214.1869158878505, 115.5263157894737, 220.59345794392524, 148.26315789473685], 0, True))
      self.obj391.out_connections_.append(self.obj392)
      self.obj392.in_connections_.append(self.obj391)
      self.obj391.graphObject_.pendingConnections.append((self.obj391.graphObject_.tag, self.obj392.graphObject_.tag, [224.0, 230.0, 228.78504672897196, 249.21052631578948], 0, True))
      self.obj392.out_connections_.append(self.obj390)
      self.obj390.in_connections_.append(self.obj392)
      self.obj392.graphObject_.pendingConnections.append((self.obj392.graphObject_.tag, self.obj390.graphObject_.tag, [233.57009345794393, 268.42105263157896, 228.78504672897196, 249.21052631578948], 0, True))
      self.obj393.out_connections_.append(self.obj389)
      self.obj389.in_connections_.append(self.obj393)
      self.obj393.graphObject_.pendingConnections.append((self.obj393.graphObject_.tag, self.obj389.graphObject_.tag, [213.57009345794393, 108.42105263157895, 218.78504672897196, 90.71052631578948], 0, True))
      self.obj394.out_connections_.append(self.obj391)
      self.obj391.in_connections_.append(self.obj394)
      self.obj394.graphObject_.pendingConnections.append((self.obj394.graphObject_.tag, self.obj391.graphObject_.tag, [227.0, 181.0, 220.59345794392524, 148.26315789473685], 0, True))
      self.obj395.out_connections_.append(self.obj388)
      self.obj388.in_connections_.append(self.obj395)
      self.obj395.graphObject_.pendingConnections.append((self.obj395.graphObject_.tag, self.obj388.graphObject_.tag, [224.0, 73.0, 144.5, 87.5], 0, True))
      self.obj396.out_connections_.append(self.obj391)
      self.obj391.in_connections_.append(self.obj396)
      self.obj396.graphObject_.pendingConnections.append((self.obj396.graphObject_.tag, self.obj391.graphObject_.tag, [212.0, 185.0, 128.0, 183.0], 0, True))
      self.obj397.out_connections_.append(self.obj389)
      self.obj389.in_connections_.append(self.obj397)
      self.obj397.graphObject_.pendingConnections.append((self.obj397.graphObject_.tag, self.obj389.graphObject_.tag, [214.57009345794393, 108.42105263157895, 145.78504672897196, 105.21052631578948], 0, True))

   def condition(self, graphID, isograph, atom3i):
      print 'Rule 22 :'
      print str(self.graphRewritingSystem.Dictag[ self.getMatched ( graphID , self.LHS.nodeWithLabel(1) ).name.getValue() ]) +' for '+ self.getMatched ( graphID , self.LHS.nodeWithLabel(1) ).name.getValue()
      
      no4 = self.getMatched(graphID, self.LHS.nodeWithLabel(4))
      no7 = self.getMatched(graphID, self.LHS.nodeWithLabel(7))
      return not( hasattr(no4, "assign1Rule") and hasattr(no7, "assign1Rule") )
      
      

   def action(self, graphID, isograph, atom3i):
      nod4 = self.getMatched(graphID, self.LHS.nodeWithLabel(4))
      nod7 = self.getMatched(graphID, self.LHS.nodeWithLabel(7))
      nod4.assign1Rule = True 
      nod7.assign1Rule = True 
      
      

