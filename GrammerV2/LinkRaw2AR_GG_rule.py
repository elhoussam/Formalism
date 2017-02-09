# _ LinkRaw2AR_GG_rule.py ____________________________________________________________________________
# File generated automatically by ATOM3. Graph Grammar Rule
# ___________________________________________________________________________________________
from GGrule import *
from Capabilitie import *
from rawMaterial import *
from GenericGraphEdge import *
from Goal import *
from intoProduct import *
from operatingUnit import *
from metarial import *
from GenericGraphNode import *
from product import *
from Agent import *
from fromMaterial import *
from CapableOf import *
from Role import *
from fromRaw import *
from ASG_pns2 import *
from intoMaterial import *
from ASG_GenericGraph import *
from ASG_omacs import *
from require import *
from achieve import *
from posses import *
class LinkRaw2AR_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 8)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_pns2(parent)
      self.LHS.merge(ASG_omacs(parent))
      self.LHS.merge(ASG_GenericGraph(parent))

      self.obj289=rawMaterial(parent)
      self.obj289.preAction( self.LHS.CREATE )
      self.obj289.isGraphObjectVisual = True

      if(hasattr(self.obj289, '_setHierarchicalLink')):
        self.obj289._setHierarchicalLink(False)

      # Name
      self.obj289.Name.setValue('')
      self.obj289.Name.setNone()

      self.obj289.GGLabel.setValue(1)
      self.obj289.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(280.0,60.0,self.obj289)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj289.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj289)
      self.obj289.postAction( self.LHS.CREATE )

      self.obj291=operatingUnit(parent)
      self.obj291.preAction( self.LHS.CREATE )
      self.obj291.isGraphObjectVisual = True

      if(hasattr(self.obj291, '_setHierarchicalLink')):
        self.obj291._setHierarchicalLink(False)

      self.obj291.GGLabel.setValue(3)
      self.obj291.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(280.0,240.0,self.obj291)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj291.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj291)
      self.obj291.postAction( self.LHS.CREATE )

      self.obj304=Agent(parent)
      self.obj304.preAction( self.LHS.CREATE )
      self.obj304.isGraphObjectVisual = True

      if(hasattr(self.obj304, '_setHierarchicalLink')):
        self.obj304._setHierarchicalLink(False)

      # price
      self.obj304.price.setValue(0)

      # name
      self.obj304.name.setValue('')
      self.obj304.name.setNone()

      self.obj304.GGLabel.setValue(5)
      self.obj304.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(20.0,120.0,self.obj304)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj304.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj304)
      self.obj304.postAction( self.LHS.CREATE )

      self.obj309=GenericGraphEdge(parent)
      self.obj309.preAction( self.LHS.CREATE )
      self.obj309.isGraphObjectVisual = True

      if(hasattr(self.obj309, '_setHierarchicalLink')):
        self.obj309._setHierarchicalLink(False)

      self.obj309.GGLabel.setValue(6)
      self.obj309.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(264.0,158.75,self.obj309)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj309.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj309)
      self.obj309.postAction( self.LHS.CREATE )

      self.obj310=GenericGraphEdge(parent)
      self.obj310.preAction( self.LHS.CREATE )
      self.obj310.isGraphObjectVisual = True

      if(hasattr(self.obj310, '_setHierarchicalLink')):
        self.obj310._setHierarchicalLink(False)

      self.obj310.GGLabel.setValue(7)
      self.obj310.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(262.75,206.25,self.obj310)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj310.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj310)
      self.obj310.postAction( self.LHS.CREATE )

      self.obj304.out_connections_.append(self.obj309)
      self.obj309.in_connections_.append(self.obj304)
      self.obj304.graphObject_.pendingConnections.append((self.obj304.graphObject_.tag, self.obj309.graphObject_.tag, [52.0, 206.0, 201.0, 182.0, 264.0, 158.75], 2, True))
      self.obj304.out_connections_.append(self.obj310)
      self.obj310.in_connections_.append(self.obj304)
      self.obj304.graphObject_.pendingConnections.append((self.obj304.graphObject_.tag, self.obj310.graphObject_.tag, [52.0, 206.0, 189.0, 197.5, 262.75, 206.25], 2, True))
      self.obj309.out_connections_.append(self.obj289)
      self.obj289.in_connections_.append(self.obj309)
      self.obj309.graphObject_.pendingConnections.append((self.obj309.graphObject_.tag, self.obj289.graphObject_.tag, [304.0, 113.0, 327.0, 135.5, 264.0, 158.75], 2, True))
      self.obj310.out_connections_.append(self.obj291)
      self.obj291.in_connections_.append(self.obj310)
      self.obj310.graphObject_.pendingConnections.append((self.obj310.graphObject_.tag, self.obj291.graphObject_.tag, [347.0, 241.0, 336.5, 215.0, 262.75, 206.25], 2, True))

      self.RHS = ASG_pns2(parent)
      self.RHS.merge(ASG_omacs(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj292=rawMaterial(parent)
      self.obj292.preAction( self.RHS.CREATE )
      self.obj292.isGraphObjectVisual = True

      if(hasattr(self.obj292, '_setHierarchicalLink')):
        self.obj292._setHierarchicalLink(False)

      # Name
      self.obj292.Name.setValue('')
      self.obj292.Name.setNone()

      self.obj292.GGLabel.setValue(1)
      self.obj292.graphClass_= graph_rawMaterial
      if parent.genGraphics:
         new_obj = graph_rawMaterial(260.0,60.0,self.obj292)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj292.graphObject_ = new_obj
      self.obj2920= AttrCalc()
      self.obj2920.Copy=ATOM3Boolean()
      self.obj2920.Copy.setValue(('Copy from LHS', 1))
      self.obj2920.Copy.config = 0
      self.obj2920.Specify=ATOM3Constraint()
      self.obj2920.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj292.GGset2Any['Name']= self.obj2920

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj292)
      self.obj292.postAction( self.RHS.CREATE )

      self.obj294=operatingUnit(parent)
      self.obj294.preAction( self.RHS.CREATE )
      self.obj294.isGraphObjectVisual = True

      if(hasattr(self.obj294, '_setHierarchicalLink')):
        self.obj294._setHierarchicalLink(False)

      self.obj294.GGLabel.setValue(3)
      self.obj294.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(280.0,240.0,self.obj294)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj294.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj294)
      self.obj294.postAction( self.RHS.CREATE )

      self.obj295=fromRaw(parent)
      self.obj295.preAction( self.RHS.CREATE )
      self.obj295.isGraphObjectVisual = True

      if(hasattr(self.obj295, '_setHierarchicalLink')):
        self.obj295._setHierarchicalLink(False)

      # rate
      self.obj295.rate.setValue(0.0)

      self.obj295.GGLabel.setValue(4)
      self.obj295.graphClass_= graph_fromRaw
      if parent.genGraphics:
         new_obj = graph_fromRaw(293.0,178.0,self.obj295)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj295.graphObject_ = new_obj
      self.obj2950= AttrCalc()
      self.obj2950.Copy=ATOM3Boolean()
      self.obj2950.Copy.setValue(('Copy from LHS', 1))
      self.obj2950.Copy.config = 0
      self.obj2950.Specify=ATOM3Constraint()
      self.obj2950.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj295.GGset2Any['rate']= self.obj2950

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj295)
      self.obj295.postAction( self.RHS.CREATE )

      self.obj319=Agent(parent)
      self.obj319.preAction( self.RHS.CREATE )
      self.obj319.isGraphObjectVisual = True

      if(hasattr(self.obj319, '_setHierarchicalLink')):
        self.obj319._setHierarchicalLink(False)

      # price
      self.obj319.price.setValue(0)

      # name
      self.obj319.name.setValue('')
      self.obj319.name.setNone()

      self.obj319.GGLabel.setValue(5)
      self.obj319.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(20.0,120.0,self.obj319)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj319.graphObject_ = new_obj
      self.obj3190= AttrCalc()
      self.obj3190.Copy=ATOM3Boolean()
      self.obj3190.Copy.setValue(('Copy from LHS', 1))
      self.obj3190.Copy.config = 0
      self.obj3190.Specify=ATOM3Constraint()
      self.obj3190.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj319.GGset2Any['price']= self.obj3190
      self.obj3191= AttrCalc()
      self.obj3191.Copy=ATOM3Boolean()
      self.obj3191.Copy.setValue(('Copy from LHS', 1))
      self.obj3191.Copy.config = 0
      self.obj3191.Specify=ATOM3Constraint()
      self.obj3191.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj319.GGset2Any['name']= self.obj3191

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj319)
      self.obj319.postAction( self.RHS.CREATE )

      self.obj324=GenericGraphEdge(parent)
      self.obj324.preAction( self.RHS.CREATE )
      self.obj324.isGraphObjectVisual = True

      if(hasattr(self.obj324, '_setHierarchicalLink')):
        self.obj324._setHierarchicalLink(False)

      self.obj324.GGLabel.setValue(6)
      self.obj324.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(205.5,156.75,self.obj324)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj324.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj324)
      self.obj324.postAction( self.RHS.CREATE )

      self.obj325=GenericGraphEdge(parent)
      self.obj325.preAction( self.RHS.CREATE )
      self.obj325.isGraphObjectVisual = True

      if(hasattr(self.obj325, '_setHierarchicalLink')):
        self.obj325._setHierarchicalLink(False)

      self.obj325.GGLabel.setValue(7)
      self.obj325.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(215.0,206.75,self.obj325)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj325.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj325)
      self.obj325.postAction( self.RHS.CREATE )

      self.obj292.out_connections_.append(self.obj295)
      self.obj295.in_connections_.append(self.obj292)
      self.obj292.graphObject_.pendingConnections.append((self.obj292.graphObject_.tag, self.obj295.graphObject_.tag, [284.0, 113.0, 293.0, 178.0], 0, True))
      self.obj295.out_connections_.append(self.obj294)
      self.obj294.in_connections_.append(self.obj295)
      self.obj295.graphObject_.pendingConnections.append((self.obj295.graphObject_.tag, self.obj294.graphObject_.tag, [302.0, 243.0, 293.0, 178.0], 0, True))
      self.obj319.out_connections_.append(self.obj324)
      self.obj324.in_connections_.append(self.obj319)
      self.obj319.graphObject_.pendingConnections.append((self.obj319.graphObject_.tag, self.obj324.graphObject_.tag, [52.0, 206.0, 147.5, 180.0, 205.5, 156.75], 2, True))
      self.obj319.out_connections_.append(self.obj325)
      self.obj325.in_connections_.append(self.obj319)
      self.obj319.graphObject_.pendingConnections.append((self.obj319.graphObject_.tag, self.obj325.graphObject_.tag, [52.0, 206.0, 152.5, 197.5, 215.0, 206.75], 2, True))
      self.obj324.out_connections_.append(self.obj292)
      self.obj292.in_connections_.append(self.obj324)
      self.obj324.graphObject_.pendingConnections.append((self.obj324.graphObject_.tag, self.obj292.graphObject_.tag, [284.0, 113.0, 263.5, 133.5, 205.5, 156.75], 2, True))
      self.obj325.out_connections_.append(self.obj294)
      self.obj294.in_connections_.append(self.obj325)
      self.obj325.graphObject_.pendingConnections.append((self.obj325.graphObject_.tag, self.obj294.graphObject_.tag, [302.0, 243.0, 277.5, 216.0, 215.0, 206.75], 2, True))

   def condition(self, graphID, isograph, atom3i):
      # code condition of rule
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(3))
      return not hasattr(node, "LinkRaw2AR")
      
      
      
      

   def action(self, graphID, isograph, atom3i):
      # code action of rule
      node = self.getMatched ( graphID , self.LHS.nodeWithLabel(3) )
      node.LinkRaw2AR = True
      
      

