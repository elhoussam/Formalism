# _ CreateMat_ARG_GG_rule.py ____________________________________________________________________________
# File generated automatically by ATOM3. Graph Grammar Rule
# ___________________________________________________________________________________________
from GGrule import *
from CapableOf import *
from Goal import *
from ASG_omacss import *
from Agent import *
from Capabilitie import *
from Role import *
from requir import *
from achieve import *
from posses import *
from GenericGraphEdge import *
from intoProduct import *
from operatingUnit import *
from metarial import *
from rawMaterial import *
from fromMaterial import *
from fromRaw import *
from ASG_pns2 import *
from intoMaterial import *
from ASG_GenericGraph import *
from product import *
from GenericGraphNode import *
class CreateMat_ARG_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 17)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_omacss(parent)

      self.obj1083=Agent(parent)
      self.obj1083.preAction( self.LHS.CREATE )
      self.obj1083.isGraphObjectVisual = True

      if(hasattr(self.obj1083, '_setHierarchicalLink')):
        self.obj1083._setHierarchicalLink(False)

      # price
      self.obj1083.price.setValue(0)

      # name
      self.obj1083.name.setValue('')
      self.obj1083.name.setNone()

      self.obj1083.GGLabel.setValue(1)
      self.obj1083.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(80.0,20.0,self.obj1083)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1083.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1083)
      self.obj1083.postAction( self.LHS.CREATE )

      self.obj1084=Role(parent)
      self.obj1084.preAction( self.LHS.CREATE )
      self.obj1084.isGraphObjectVisual = True

      if(hasattr(self.obj1084, '_setHierarchicalLink')):
        self.obj1084._setHierarchicalLink(False)

      # name
      self.obj1084.name.setValue('')
      self.obj1084.name.setNone()

      self.obj1084.GGLabel.setValue(2)
      self.obj1084.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(200.0,100.0,self.obj1084)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1084.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1084)
      self.obj1084.postAction( self.LHS.CREATE )

      self.obj1085=Goal(parent)
      self.obj1085.preAction( self.LHS.CREATE )
      self.obj1085.isGraphObjectVisual = True

      if(hasattr(self.obj1085, '_setHierarchicalLink')):
        self.obj1085._setHierarchicalLink(False)

      # name
      self.obj1085.name.setValue('')
      self.obj1085.name.setNone()

      self.obj1085.GGLabel.setValue(3)
      self.obj1085.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(100.0,180.0,self.obj1085)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1085.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1085)
      self.obj1085.postAction( self.LHS.CREATE )

      self.obj1086=CapableOf(parent)
      self.obj1086.preAction( self.LHS.CREATE )
      self.obj1086.isGraphObjectVisual = True

      if(hasattr(self.obj1086, '_setHierarchicalLink')):
        self.obj1086._setHierarchicalLink(False)

      self.obj1086.GGLabel.setValue(4)
      self.obj1086.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(164.5,91.5,self.obj1086)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1086.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1086)
      self.obj1086.postAction( self.LHS.CREATE )

      self.obj1087=achieve(parent)
      self.obj1087.preAction( self.LHS.CREATE )
      self.obj1087.isGraphObjectVisual = True

      if(hasattr(self.obj1087, '_setHierarchicalLink')):
        self.obj1087._setHierarchicalLink(False)

      # rate
      self.obj1087.rate.setValue(0.0)

      self.obj1087.GGLabel.setValue(5)
      self.obj1087.graphClass_= graph_achieve
      if parent.genGraphics:
         new_obj = graph_achieve(173.5,163.5,self.obj1087)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1087.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1087)
      self.obj1087.postAction( self.LHS.CREATE )

      self.obj1083.out_connections_.append(self.obj1086)
      self.obj1086.in_connections_.append(self.obj1083)
      self.obj1083.graphObject_.pendingConnections.append((self.obj1083.graphObject_.tag, self.obj1086.graphObject_.tag, [105.0, 82.0, 164.5, 91.5], 0, True))
      self.obj1084.out_connections_.append(self.obj1087)
      self.obj1087.in_connections_.append(self.obj1084)
      self.obj1084.graphObject_.pendingConnections.append((self.obj1084.graphObject_.tag, self.obj1087.graphObject_.tag, [224.0, 146.0, 173.5, 163.5], 0, True))
      self.obj1086.out_connections_.append(self.obj1084)
      self.obj1084.in_connections_.append(self.obj1086)
      self.obj1086.graphObject_.pendingConnections.append((self.obj1086.graphObject_.tag, self.obj1084.graphObject_.tag, [224.0, 101.0, 164.5, 91.5], 0, True))
      self.obj1087.out_connections_.append(self.obj1085)
      self.obj1085.in_connections_.append(self.obj1087)
      self.obj1087.graphObject_.pendingConnections.append((self.obj1087.graphObject_.tag, self.obj1085.graphObject_.tag, [123.0, 181.0, 173.5, 163.5], 0, True))

      self.RHS = ASG_omacss(parent)
      self.RHS.merge(ASG_pns2(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj1091=Agent(parent)
      self.obj1091.preAction( self.RHS.CREATE )
      self.obj1091.isGraphObjectVisual = True

      if(hasattr(self.obj1091, '_setHierarchicalLink')):
        self.obj1091._setHierarchicalLink(False)

      # price
      self.obj1091.price.setValue(0)

      # name
      self.obj1091.name.setValue('')
      self.obj1091.name.setNone()

      self.obj1091.GGLabel.setValue(1)
      self.obj1091.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(80.0,20.0,self.obj1091)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1091.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1091)
      self.obj1091.postAction( self.RHS.CREATE )

      self.obj1092=Role(parent)
      self.obj1092.preAction( self.RHS.CREATE )
      self.obj1092.isGraphObjectVisual = True

      if(hasattr(self.obj1092, '_setHierarchicalLink')):
        self.obj1092._setHierarchicalLink(False)

      # name
      self.obj1092.name.setValue('')
      self.obj1092.name.setNone()

      self.obj1092.GGLabel.setValue(2)
      self.obj1092.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(200.0,100.0,self.obj1092)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1092.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1092)
      self.obj1092.postAction( self.RHS.CREATE )

      self.obj1093=Goal(parent)
      self.obj1093.preAction( self.RHS.CREATE )
      self.obj1093.isGraphObjectVisual = True

      if(hasattr(self.obj1093, '_setHierarchicalLink')):
        self.obj1093._setHierarchicalLink(False)

      # name
      self.obj1093.name.setValue('')
      self.obj1093.name.setNone()

      self.obj1093.GGLabel.setValue(3)
      self.obj1093.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(100.0,180.0,self.obj1093)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1093.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1093)
      self.obj1093.postAction( self.RHS.CREATE )

      self.obj1094=CapableOf(parent)
      self.obj1094.preAction( self.RHS.CREATE )
      self.obj1094.isGraphObjectVisual = True

      if(hasattr(self.obj1094, '_setHierarchicalLink')):
        self.obj1094._setHierarchicalLink(False)

      self.obj1094.GGLabel.setValue(4)
      self.obj1094.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(164.5,91.5,self.obj1094)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1094.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1094)
      self.obj1094.postAction( self.RHS.CREATE )

      self.obj1095=achieve(parent)
      self.obj1095.preAction( self.RHS.CREATE )
      self.obj1095.isGraphObjectVisual = True

      if(hasattr(self.obj1095, '_setHierarchicalLink')):
        self.obj1095._setHierarchicalLink(False)

      # rate
      self.obj1095.rate.setValue(0.0)

      self.obj1095.GGLabel.setValue(5)
      self.obj1095.graphClass_= graph_achieve
      if parent.genGraphics:
         new_obj = graph_achieve(173.5,163.5,self.obj1095)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1095.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1095)
      self.obj1095.postAction( self.RHS.CREATE )

      self.obj1096=operatingUnit(parent)
      self.obj1096.preAction( self.RHS.CREATE )
      self.obj1096.isGraphObjectVisual = True

      if(hasattr(self.obj1096, '_setHierarchicalLink')):
        self.obj1096._setHierarchicalLink(False)

      # name
      self.obj1096.name.setValue('')
      self.obj1096.name.setNone()

      self.obj1096.GGLabel.setValue(7)
      self.obj1096.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(320.0,140.0,self.obj1096)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1096.graphObject_ = new_obj
      self.obj10960= AttrCalc()
      self.obj10960.Copy=ATOM3Boolean()
      self.obj10960.Copy.setValue(('Copy from LHS', 0))
      self.obj10960.Copy.config = 0
      self.obj10960.Specify=ATOM3Constraint()
      self.obj10960.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()+\' \'+ self.getMatched(graphID, self.LHS.nodeWithLabel(2)).name.getValue()+\' \'+ self.getMatched(graphID, self.LHS.nodeWithLabel(3)).name.getValue()\n'))
      self.obj1096.GGset2Any['name']= self.obj10960

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1096)
      self.obj1096.postAction( self.RHS.CREATE )

      self.obj1097=metarial(parent)
      self.obj1097.preAction( self.RHS.CREATE )
      self.obj1097.isGraphObjectVisual = True

      if(hasattr(self.obj1097, '_setHierarchicalLink')):
        self.obj1097._setHierarchicalLink(False)

      # Name
      self.obj1097.Name.setValue('')
      self.obj1097.Name.setNone()

      self.obj1097.GGLabel.setValue(8)
      self.obj1097.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(320.0,40.0,self.obj1097)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1097.graphObject_ = new_obj
      self.obj10970= AttrCalc()
      self.obj10970.Copy=ATOM3Boolean()
      self.obj10970.Copy.setValue(('Copy from LHS', 0))
      self.obj10970.Copy.config = 0
      self.obj10970.Specify=ATOM3Constraint()
      self.obj10970.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()+\' \'+ self.getMatched(graphID, self.LHS.nodeWithLabel(2)).name.getValue()+\' \'+ self.getMatched(graphID, self.LHS.nodeWithLabel(3)).name.getValue()\n'))
      self.obj1097.GGset2Any['Name']= self.obj10970

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1097)
      self.obj1097.postAction( self.RHS.CREATE )

      self.obj1098=fromMaterial(parent)
      self.obj1098.preAction( self.RHS.CREATE )
      self.obj1098.isGraphObjectVisual = True

      if(hasattr(self.obj1098, '_setHierarchicalLink')):
        self.obj1098._setHierarchicalLink(False)

      # rate
      self.obj1098.rate.setValue(1.0)

      self.obj1098.GGLabel.setValue(9)
      self.obj1098.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(338.785046729,119.210526316,self.obj1098)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1098.graphObject_ = new_obj
      self.obj10980= AttrCalc()
      self.obj10980.Copy=ATOM3Boolean()
      self.obj10980.Copy.setValue(('Copy from LHS', 0))
      self.obj10980.Copy.config = 0
      self.obj10980.Specify=ATOM3Constraint()
      self.obj10980.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1098.GGset2Any['rate']= self.obj10980

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1098)
      self.obj1098.postAction( self.RHS.CREATE )

      self.obj1099=GenericGraphEdge(parent)
      self.obj1099.preAction( self.RHS.CREATE )
      self.obj1099.isGraphObjectVisual = True

      if(hasattr(self.obj1099, '_setHierarchicalLink')):
        self.obj1099._setHierarchicalLink(False)

      self.obj1099.GGLabel.setValue(10)
      self.obj1099.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(280.5,92.0,self.obj1099)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1099.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1099)
      self.obj1099.postAction( self.RHS.CREATE )

      self.obj1091.out_connections_.append(self.obj1094)
      self.obj1094.in_connections_.append(self.obj1091)
      self.obj1091.graphObject_.pendingConnections.append((self.obj1091.graphObject_.tag, self.obj1094.graphObject_.tag, [117.0, 82.0, 164.5, 91.5], 2, 0))
      self.obj1092.out_connections_.append(self.obj1095)
      self.obj1095.in_connections_.append(self.obj1092)
      self.obj1092.graphObject_.pendingConnections.append((self.obj1092.graphObject_.tag, self.obj1095.graphObject_.tag, [231.0, 145.0, 173.5, 163.5], 2, 0))
      self.obj1092.out_connections_.append(self.obj1099)
      self.obj1099.in_connections_.append(self.obj1092)
      self.obj1092.graphObject_.pendingConnections.append((self.obj1092.graphObject_.tag, self.obj1099.graphObject_.tag, [231.0, 100.0, 280.5, 92.0], 0, True))
      self.obj1094.out_connections_.append(self.obj1092)
      self.obj1092.in_connections_.append(self.obj1094)
      self.obj1094.graphObject_.pendingConnections.append((self.obj1094.graphObject_.tag, self.obj1092.graphObject_.tag, [231.0, 100.0, 164.5, 91.5], 2, 0))
      self.obj1095.out_connections_.append(self.obj1093)
      self.obj1093.in_connections_.append(self.obj1095)
      self.obj1095.graphObject_.pendingConnections.append((self.obj1095.graphObject_.tag, self.obj1093.graphObject_.tag, [133.0, 181.0, 173.5, 163.5], 2, 0))
      self.obj1097.out_connections_.append(self.obj1098)
      self.obj1098.in_connections_.append(self.obj1097)
      self.obj1097.graphObject_.pendingConnections.append((self.obj1097.graphObject_.tag, self.obj1098.graphObject_.tag, [344.0, 90.0, 338.78504672897196, 119.21052631578948], 0, True))
      self.obj1098.out_connections_.append(self.obj1096)
      self.obj1096.in_connections_.append(self.obj1098)
      self.obj1098.graphObject_.pendingConnections.append((self.obj1098.graphObject_.tag, self.obj1096.graphObject_.tag, [333.5700934579439, 148.42105263157896, 338.78504672897196, 119.21052631578948], 0, True))
      self.obj1099.out_connections_.append(self.obj1097)
      self.obj1097.in_connections_.append(self.obj1099)
      self.obj1099.graphObject_.pendingConnections.append((self.obj1099.graphObject_.tag, self.obj1097.graphObject_.tag, [330.0, 84.0, 280.5, 92.0], 0, True))

   def condition(self, graphID, isograph, atom3i):
      print '======> GenAux1 Condition'
      a = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      aN = a.name.getValue()
      #print a.name.getValue()+' has att AUX : '+str( hasattr(a, "AUX") )
      r = self.getMatched(graphID, self.LHS.nodeWithLabel(2))
      Rn = r.name.getValue()
      g = self.getMatched(graphID, self.LHS.nodeWithLabel(3))
      Gn = g.name.getValue()
      # add list to the Agent Node
      if not hasattr(a,'markedNode') : 
      	a.markedNode = []
      	print 'add List to '+aN
      
      print 'CHeck if '+aN+'Have'
      for ele in a.markedNode : 
          if ele == (Rn,Gn) : return False
      return True
      #        print 'Check if '+aN+'Have '
      #        for ele in a.markedNode : 
      #            if ele == (Rn,Gn) : return False 
      #        return True
      
      

   def action(self, graphID, isograph, atom3i):
      print '======> GenAux1 ACtion'
      a = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      aN = a.name.getValue()
      #print a.name.getValue()+' has att AUX : '+str( hasattr(a, "AUX") )
      r = self.getMatched(graphID, self.LHS.nodeWithLabel(2))
      Rn = r.name.getValue()
      g = self.getMatched(graphID, self.LHS.nodeWithLabel(3))
      Gn = g.name.getValue()
      # add ele list to the Agent Node
      print 'Add Ele into list of '+aN
      a.markedNode.append( (Rn,Gn) )
      print 'List of MarkedNode'
      for ele in a.markedNode : 
      	print ele
      
      

