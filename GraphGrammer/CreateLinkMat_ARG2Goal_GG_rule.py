# _ CreateLinkMat_ARG2Goal_GG_rule.py ____________________________________________________________________________
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
class CreateLinkMat_ARG2Goal_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 19)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_omacss(parent)
      self.LHS.merge(ASG_pns2(parent))
      self.LHS.merge(ASG_GenericGraph(parent))

      self.obj309=Role(parent)
      self.obj309.preAction( self.LHS.CREATE )
      self.obj309.isGraphObjectVisual = True

      if(hasattr(self.obj309, '_setHierarchicalLink')):
        self.obj309._setHierarchicalLink(False)

      # name
      self.obj309.name.setValue('')
      self.obj309.name.setNone()

      self.obj309.GGLabel.setValue(1)
      self.obj309.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(80.0,20.0,self.obj309)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj309.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj309)
      self.obj309.postAction( self.LHS.CREATE )

      self.obj310=Goal(parent)
      self.obj310.preAction( self.LHS.CREATE )
      self.obj310.isGraphObjectVisual = True

      if(hasattr(self.obj310, '_setHierarchicalLink')):
        self.obj310._setHierarchicalLink(False)

      # name
      self.obj310.name.setValue('')
      self.obj310.name.setNone()

      self.obj310.GGLabel.setValue(2)
      self.obj310.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(100.0,180.0,self.obj310)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj310.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj310)
      self.obj310.postAction( self.LHS.CREATE )

      self.obj311=achieve(parent)
      self.obj311.preAction( self.LHS.CREATE )
      self.obj311.isGraphObjectVisual = True

      if(hasattr(self.obj311, '_setHierarchicalLink')):
        self.obj311._setHierarchicalLink(False)

      # rate
      self.obj311.rate.setNone()

      self.obj311.GGLabel.setValue(3)
      self.obj311.graphClass_= graph_achieve
      if parent.genGraphics:
         new_obj = graph_achieve(113.5,123.5,self.obj311)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj311.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj311)
      self.obj311.postAction( self.LHS.CREATE )

      self.obj312=operatingUnit(parent)
      self.obj312.preAction( self.LHS.CREATE )
      self.obj312.isGraphObjectVisual = True

      if(hasattr(self.obj312, '_setHierarchicalLink')):
        self.obj312._setHierarchicalLink(False)

      # name
      self.obj312.name.setValue('')
      self.obj312.name.setNone()

      self.obj312.GGLabel.setValue(5)
      self.obj312.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(280.0,100.0,self.obj312)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj312.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj312)
      self.obj312.postAction( self.LHS.CREATE )

      self.obj313=metarial(parent)
      self.obj313.preAction( self.LHS.CREATE )
      self.obj313.isGraphObjectVisual = True

      if(hasattr(self.obj313, '_setHierarchicalLink')):
        self.obj313._setHierarchicalLink(False)

      # Name
      self.obj313.Name.setValue('')
      self.obj313.Name.setNone()

      self.obj313.GGLabel.setValue(4)
      self.obj313.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(280.0,20.0,self.obj313)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj313.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj313)
      self.obj313.postAction( self.LHS.CREATE )

      self.obj314=metarial(parent)
      self.obj314.preAction( self.LHS.CREATE )
      self.obj314.isGraphObjectVisual = True

      if(hasattr(self.obj314, '_setHierarchicalLink')):
        self.obj314._setHierarchicalLink(False)

      # Name
      self.obj314.Name.setValue('')
      self.obj314.Name.setNone()

      self.obj314.GGLabel.setValue(6)
      self.obj314.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(320.0,220.0,self.obj314)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj314.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj314)
      self.obj314.postAction( self.LHS.CREATE )

      self.obj315=fromMaterial(parent)
      self.obj315.preAction( self.LHS.CREATE )
      self.obj315.isGraphObjectVisual = True

      if(hasattr(self.obj315, '_setHierarchicalLink')):
        self.obj315._setHierarchicalLink(False)

      # rate
      self.obj315.rate.setNone()

      self.obj315.GGLabel.setValue(8)
      self.obj315.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(298.785046729,89.2105263158,self.obj315)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj315.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj315)
      self.obj315.postAction( self.LHS.CREATE )

      self.obj316=GenericGraphEdge(parent)
      self.obj316.preAction( self.LHS.CREATE )
      self.obj316.isGraphObjectVisual = True

      if(hasattr(self.obj316, '_setHierarchicalLink')):
        self.obj316._setHierarchicalLink(False)

      self.obj316.GGLabel.setValue(7)
      self.obj316.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(198.0,23.0,self.obj316)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj316.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj316)
      self.obj316.postAction( self.LHS.CREATE )

      self.obj317=GenericGraphEdge(parent)
      self.obj317.preAction( self.LHS.CREATE )
      self.obj317.isGraphObjectVisual = True

      if(hasattr(self.obj317, '_setHierarchicalLink')):
        self.obj317._setHierarchicalLink(False)

      self.obj317.GGLabel.setValue(9)
      self.obj317.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(228.0,227.5,self.obj317)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj317.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj317)
      self.obj317.postAction( self.LHS.CREATE )

      self.obj309.out_connections_.append(self.obj311)
      self.obj311.in_connections_.append(self.obj309)
      self.obj309.graphObject_.pendingConnections.append((self.obj309.graphObject_.tag, self.obj311.graphObject_.tag, [104.0, 66.0, 113.5, 123.5], 0, True))
      self.obj309.out_connections_.append(self.obj316)
      self.obj316.in_connections_.append(self.obj309)
      self.obj309.graphObject_.pendingConnections.append((self.obj309.graphObject_.tag, self.obj316.graphObject_.tag, [104.0, 21.0, 198.0, 23.0], 0, True))
      self.obj310.out_connections_.append(self.obj317)
      self.obj317.in_connections_.append(self.obj310)
      self.obj310.graphObject_.pendingConnections.append((self.obj310.graphObject_.tag, self.obj317.graphObject_.tag, [124.0, 230.0, 228.0, 227.5], 0, True))
      self.obj311.out_connections_.append(self.obj310)
      self.obj310.in_connections_.append(self.obj311)
      self.obj311.graphObject_.pendingConnections.append((self.obj311.graphObject_.tag, self.obj310.graphObject_.tag, [123.0, 181.0, 113.5, 123.5], 0, True))
      self.obj313.out_connections_.append(self.obj315)
      self.obj315.in_connections_.append(self.obj313)
      self.obj313.graphObject_.pendingConnections.append((self.obj313.graphObject_.tag, self.obj315.graphObject_.tag, [304.0, 70.0, 298.78504672897196, 89.21052631578948], 0, True))
      self.obj315.out_connections_.append(self.obj312)
      self.obj312.in_connections_.append(self.obj315)
      self.obj315.graphObject_.pendingConnections.append((self.obj315.graphObject_.tag, self.obj312.graphObject_.tag, [293.5700934579439, 108.42105263157895, 298.78504672897196, 89.21052631578948], 0, True))
      self.obj316.out_connections_.append(self.obj313)
      self.obj313.in_connections_.append(self.obj316)
      self.obj316.graphObject_.pendingConnections.append((self.obj316.graphObject_.tag, self.obj313.graphObject_.tag, [292.0, 25.0, 198.0, 23.0], 0, True))
      self.obj317.out_connections_.append(self.obj314)
      self.obj314.in_connections_.append(self.obj317)
      self.obj317.graphObject_.pendingConnections.append((self.obj317.graphObject_.tag, self.obj314.graphObject_.tag, [332.0, 225.0, 228.0, 227.5], 0, True))

      self.RHS = ASG_omacss(parent)
      self.RHS.merge(ASG_pns2(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj321=Role(parent)
      self.obj321.preAction( self.RHS.CREATE )
      self.obj321.isGraphObjectVisual = True

      if(hasattr(self.obj321, '_setHierarchicalLink')):
        self.obj321._setHierarchicalLink(False)

      # name
      self.obj321.name.setValue('')
      self.obj321.name.setNone()

      self.obj321.GGLabel.setValue(1)
      self.obj321.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(100.0,40.0,self.obj321)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj321.graphObject_ = new_obj
      self.obj3210= AttrCalc()
      self.obj3210.Copy=ATOM3Boolean()
      self.obj3210.Copy.setValue(('Copy from LHS', 1))
      self.obj3210.Copy.config = 0
      self.obj3210.Specify=ATOM3Constraint()
      self.obj3210.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj321.GGset2Any['name']= self.obj3210

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj321)
      self.obj321.postAction( self.RHS.CREATE )

      self.obj322=Goal(parent)
      self.obj322.preAction( self.RHS.CREATE )
      self.obj322.isGraphObjectVisual = True

      if(hasattr(self.obj322, '_setHierarchicalLink')):
        self.obj322._setHierarchicalLink(False)

      # name
      self.obj322.name.setValue('')
      self.obj322.name.setNone()

      self.obj322.GGLabel.setValue(2)
      self.obj322.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(120.0,160.0,self.obj322)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj322.graphObject_ = new_obj
      self.obj3220= AttrCalc()
      self.obj3220.Copy=ATOM3Boolean()
      self.obj3220.Copy.setValue(('Copy from LHS', 1))
      self.obj3220.Copy.config = 0
      self.obj3220.Specify=ATOM3Constraint()
      self.obj3220.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj322.GGset2Any['name']= self.obj3220

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj322)
      self.obj322.postAction( self.RHS.CREATE )

      self.obj323=achieve(parent)
      self.obj323.preAction( self.RHS.CREATE )
      self.obj323.isGraphObjectVisual = True

      if(hasattr(self.obj323, '_setHierarchicalLink')):
        self.obj323._setHierarchicalLink(False)

      # rate
      self.obj323.rate.setValue(0.0)

      self.obj323.GGLabel.setValue(3)
      self.obj323.graphClass_= graph_achieve
      if parent.genGraphics:
         new_obj = graph_achieve(133.5,123.5,self.obj323)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj323.graphObject_ = new_obj
      self.obj3230= AttrCalc()
      self.obj3230.Copy=ATOM3Boolean()
      self.obj3230.Copy.setValue(('Copy from LHS', 1))
      self.obj3230.Copy.config = 0
      self.obj3230.Specify=ATOM3Constraint()
      self.obj3230.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj323.GGset2Any['rate']= self.obj3230

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj323)
      self.obj323.postAction( self.RHS.CREATE )

      self.obj324=operatingUnit(parent)
      self.obj324.preAction( self.RHS.CREATE )
      self.obj324.isGraphObjectVisual = True

      if(hasattr(self.obj324, '_setHierarchicalLink')):
        self.obj324._setHierarchicalLink(False)

      # name
      self.obj324.name.setValue('')
      self.obj324.name.setNone()

      self.obj324.GGLabel.setValue(5)
      self.obj324.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(280.0,120.0,self.obj324)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj324.graphObject_ = new_obj
      self.obj3240= AttrCalc()
      self.obj3240.Copy=ATOM3Boolean()
      self.obj3240.Copy.setValue(('Copy from LHS', 1))
      self.obj3240.Copy.config = 0
      self.obj3240.Specify=ATOM3Constraint()
      self.obj3240.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj324.GGset2Any['name']= self.obj3240

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj324)
      self.obj324.postAction( self.RHS.CREATE )

      self.obj325=metarial(parent)
      self.obj325.preAction( self.RHS.CREATE )
      self.obj325.isGraphObjectVisual = True

      if(hasattr(self.obj325, '_setHierarchicalLink')):
        self.obj325._setHierarchicalLink(False)

      # Name
      self.obj325.Name.setValue('')
      self.obj325.Name.setNone()

      self.obj325.GGLabel.setValue(4)
      self.obj325.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(280.0,40.0,self.obj325)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj325.graphObject_ = new_obj
      self.obj3250= AttrCalc()
      self.obj3250.Copy=ATOM3Boolean()
      self.obj3250.Copy.setValue(('Copy from LHS', 1))
      self.obj3250.Copy.config = 0
      self.obj3250.Specify=ATOM3Constraint()
      self.obj3250.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj325.GGset2Any['Name']= self.obj3250

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj325)
      self.obj325.postAction( self.RHS.CREATE )

      self.obj326=metarial(parent)
      self.obj326.preAction( self.RHS.CREATE )
      self.obj326.isGraphObjectVisual = True

      if(hasattr(self.obj326, '_setHierarchicalLink')):
        self.obj326._setHierarchicalLink(False)

      # Name
      self.obj326.Name.setValue('')
      self.obj326.Name.setNone()

      self.obj326.GGLabel.setValue(6)
      self.obj326.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(280.0,200.0,self.obj326)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj326.graphObject_ = new_obj
      self.obj3260= AttrCalc()
      self.obj3260.Copy=ATOM3Boolean()
      self.obj3260.Copy.setValue(('Copy from LHS', 1))
      self.obj3260.Copy.config = 0
      self.obj3260.Specify=ATOM3Constraint()
      self.obj3260.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj326.GGset2Any['Name']= self.obj3260

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj326)
      self.obj326.postAction( self.RHS.CREATE )

      self.obj327=fromMaterial(parent)
      self.obj327.preAction( self.RHS.CREATE )
      self.obj327.isGraphObjectVisual = True

      if(hasattr(self.obj327, '_setHierarchicalLink')):
        self.obj327._setHierarchicalLink(False)

      # rate
      self.obj327.rate.setValue(0.0)

      self.obj327.GGLabel.setValue(8)
      self.obj327.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(298.785046729,109.210526316,self.obj327)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj327.graphObject_ = new_obj
      self.obj3270= AttrCalc()
      self.obj3270.Copy=ATOM3Boolean()
      self.obj3270.Copy.setValue(('Copy from LHS', 1))
      self.obj3270.Copy.config = 0
      self.obj3270.Specify=ATOM3Constraint()
      self.obj3270.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj327.GGset2Any['rate']= self.obj3270

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj327)
      self.obj327.postAction( self.RHS.CREATE )

      self.obj328=intoMaterial(parent)
      self.obj328.preAction( self.RHS.CREATE )
      self.obj328.isGraphObjectVisual = True

      if(hasattr(self.obj328, '_setHierarchicalLink')):
        self.obj328._setHierarchicalLink(False)

      # rate
      self.obj328.rate.setValue(0.0)

      self.obj328.GGLabel.setValue(10)
      self.obj328.graphClass_= graph_intoMaterial
      if parent.genGraphics:
         new_obj = graph_intoMaterial(301.093457944,168.263157895,self.obj328)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj328.graphObject_ = new_obj
      self.obj3280= AttrCalc()
      self.obj3280.Copy=ATOM3Boolean()
      self.obj3280.Copy.setValue(('Copy from LHS', 0))
      self.obj3280.Copy.config = 0
      self.obj3280.Specify=ATOM3Constraint()
      self.obj3280.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(3)).rate.getValue()\n\n\n\n'))
      self.obj328.GGset2Any['rate']= self.obj3280

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj328)
      self.obj328.postAction( self.RHS.CREATE )

      self.obj329=GenericGraphEdge(parent)
      self.obj329.preAction( self.RHS.CREATE )
      self.obj329.isGraphObjectVisual = True

      if(hasattr(self.obj329, '_setHierarchicalLink')):
        self.obj329._setHierarchicalLink(False)

      self.obj329.GGLabel.setValue(7)
      self.obj329.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(208.0,43.0,self.obj329)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj329.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj329)
      self.obj329.postAction( self.RHS.CREATE )

      self.obj330=GenericGraphEdge(parent)
      self.obj330.preAction( self.RHS.CREATE )
      self.obj330.isGraphObjectVisual = True

      if(hasattr(self.obj330, '_setHierarchicalLink')):
        self.obj330._setHierarchicalLink(False)

      self.obj330.GGLabel.setValue(9)
      self.obj330.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(223.0,207.5,self.obj330)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj330.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj330)
      self.obj330.postAction( self.RHS.CREATE )

      self.obj321.out_connections_.append(self.obj323)
      self.obj323.in_connections_.append(self.obj321)
      self.obj321.graphObject_.pendingConnections.append((self.obj321.graphObject_.tag, self.obj323.graphObject_.tag, [124.0, 86.0, 133.5, 123.5], 0, True))
      self.obj321.out_connections_.append(self.obj329)
      self.obj329.in_connections_.append(self.obj321)
      self.obj321.graphObject_.pendingConnections.append((self.obj321.graphObject_.tag, self.obj329.graphObject_.tag, [124.0, 41.0, 208.0, 43.0], 0, True))
      self.obj322.out_connections_.append(self.obj330)
      self.obj330.in_connections_.append(self.obj322)
      self.obj322.graphObject_.pendingConnections.append((self.obj322.graphObject_.tag, self.obj330.graphObject_.tag, [154.0, 210.0, 223.0, 207.5], 0, True))
      self.obj323.out_connections_.append(self.obj322)
      self.obj322.in_connections_.append(self.obj323)
      self.obj323.graphObject_.pendingConnections.append((self.obj323.graphObject_.tag, self.obj322.graphObject_.tag, [143.0, 161.0, 133.5, 123.5], 0, True))
      self.obj324.out_connections_.append(self.obj328)
      self.obj328.in_connections_.append(self.obj324)
      self.obj324.graphObject_.pendingConnections.append((self.obj324.graphObject_.tag, self.obj328.graphObject_.tag, [295.1869158878505, 135.5263157894737, 301.0934579439253, 168.26315789473685], 0, True))
      self.obj325.out_connections_.append(self.obj327)
      self.obj327.in_connections_.append(self.obj325)
      self.obj325.graphObject_.pendingConnections.append((self.obj325.graphObject_.tag, self.obj327.graphObject_.tag, [304.0, 90.0, 298.78504672897196, 109.21052631578948], 0, True))
      self.obj327.out_connections_.append(self.obj324)
      self.obj324.in_connections_.append(self.obj327)
      self.obj327.graphObject_.pendingConnections.append((self.obj327.graphObject_.tag, self.obj324.graphObject_.tag, [293.5700934579439, 128.42105263157896, 298.78504672897196, 109.21052631578948], 0, True))
      self.obj328.out_connections_.append(self.obj326)
      self.obj326.in_connections_.append(self.obj328)
      self.obj328.graphObject_.pendingConnections.append((self.obj328.graphObject_.tag, self.obj326.graphObject_.tag, [307.0, 201.0, 301.0934579439253, 168.26315789473685], 0, True))
      self.obj329.out_connections_.append(self.obj325)
      self.obj325.in_connections_.append(self.obj329)
      self.obj329.graphObject_.pendingConnections.append((self.obj329.graphObject_.tag, self.obj325.graphObject_.tag, [292.0, 45.0, 208.0, 43.0], 0, True))
      self.obj330.out_connections_.append(self.obj326)
      self.obj326.in_connections_.append(self.obj330)
      self.obj330.graphObject_.pendingConnections.append((self.obj330.graphObject_.tag, self.obj326.graphObject_.tag, [292.0, 205.0, 223.0, 207.5], 2, 0))

   def condition(self, graphID, isograph, atom3i):
      print '======> Link Aux Condition'# _ Agent2Raw_GG_rule.py _
      aRg = self.getMatched ( graphID , self.LHS.nodeWithLabel(4) )
      nameARG = aRg.Name.getValue()
      g = self.getMatched ( graphID , self.LHS.nodeWithLabel(6) )
      # test if nameARG  end with name of Goal 
      print  nameARG +' END WITH '+g.Name.getValue()
      print nameARG.endswith( g.Name.getValue() )
      if nameARG.endswith( g.Name.getValue() ) and not hasattr(aRg,'LinkAux'): 
       return True
      else : 
       return False
      
      

   def action(self, graphID, isograph, atom3i):
      print '======> Link Aux Action'
      aRg = self.getMatched ( graphID , self.LHS.nodeWithLabel(4) )
      aRg.LinkAux = True 
      
      

