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

      self.obj286=Agent(parent)
      self.obj286.preAction( self.LHS.CREATE )
      self.obj286.isGraphObjectVisual = True

      if(hasattr(self.obj286, '_setHierarchicalLink')):
        self.obj286._setHierarchicalLink(False)

      # price
      self.obj286.price.setValue(0)

      # name
      self.obj286.name.setValue('')
      self.obj286.name.setNone()

      self.obj286.GGLabel.setValue(1)
      self.obj286.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(80.0,20.0,self.obj286)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj286.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj286)
      self.obj286.postAction( self.LHS.CREATE )

      self.obj287=Role(parent)
      self.obj287.preAction( self.LHS.CREATE )
      self.obj287.isGraphObjectVisual = True

      if(hasattr(self.obj287, '_setHierarchicalLink')):
        self.obj287._setHierarchicalLink(False)

      # name
      self.obj287.name.setValue('')
      self.obj287.name.setNone()

      self.obj287.GGLabel.setValue(2)
      self.obj287.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(200.0,100.0,self.obj287)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj287.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj287)
      self.obj287.postAction( self.LHS.CREATE )

      self.obj288=Goal(parent)
      self.obj288.preAction( self.LHS.CREATE )
      self.obj288.isGraphObjectVisual = True

      if(hasattr(self.obj288, '_setHierarchicalLink')):
        self.obj288._setHierarchicalLink(False)

      # name
      self.obj288.name.setValue('')
      self.obj288.name.setNone()

      self.obj288.GGLabel.setValue(3)
      self.obj288.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(100.0,180.0,self.obj288)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj288.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj288)
      self.obj288.postAction( self.LHS.CREATE )

      self.obj289=CapableOf(parent)
      self.obj289.preAction( self.LHS.CREATE )
      self.obj289.isGraphObjectVisual = True

      if(hasattr(self.obj289, '_setHierarchicalLink')):
        self.obj289._setHierarchicalLink(False)

      self.obj289.GGLabel.setValue(4)
      self.obj289.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(164.5,91.5,self.obj289)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj289.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj289)
      self.obj289.postAction( self.LHS.CREATE )

      self.obj290=achieve(parent)
      self.obj290.preAction( self.LHS.CREATE )
      self.obj290.isGraphObjectVisual = True

      if(hasattr(self.obj290, '_setHierarchicalLink')):
        self.obj290._setHierarchicalLink(False)

      # rate
      self.obj290.rate.setNone()

      self.obj290.GGLabel.setValue(5)
      self.obj290.graphClass_= graph_achieve
      if parent.genGraphics:
         new_obj = graph_achieve(173.5,163.5,self.obj290)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj290.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj290)
      self.obj290.postAction( self.LHS.CREATE )

      self.obj286.out_connections_.append(self.obj289)
      self.obj289.in_connections_.append(self.obj286)
      self.obj286.graphObject_.pendingConnections.append((self.obj286.graphObject_.tag, self.obj289.graphObject_.tag, [105.0, 82.0, 164.5, 91.5], 0, True))
      self.obj287.out_connections_.append(self.obj290)
      self.obj290.in_connections_.append(self.obj287)
      self.obj287.graphObject_.pendingConnections.append((self.obj287.graphObject_.tag, self.obj290.graphObject_.tag, [224.0, 146.0, 173.5, 163.5], 0, True))
      self.obj289.out_connections_.append(self.obj287)
      self.obj287.in_connections_.append(self.obj289)
      self.obj289.graphObject_.pendingConnections.append((self.obj289.graphObject_.tag, self.obj287.graphObject_.tag, [224.0, 101.0, 164.5, 91.5], 0, True))
      self.obj290.out_connections_.append(self.obj288)
      self.obj288.in_connections_.append(self.obj290)
      self.obj290.graphObject_.pendingConnections.append((self.obj290.graphObject_.tag, self.obj288.graphObject_.tag, [123.0, 181.0, 173.5, 163.5], 0, True))

      self.RHS = ASG_omacss(parent)
      self.RHS.merge(ASG_pns2(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj294=Agent(parent)
      self.obj294.preAction( self.RHS.CREATE )
      self.obj294.isGraphObjectVisual = True

      if(hasattr(self.obj294, '_setHierarchicalLink')):
        self.obj294._setHierarchicalLink(False)

      # price
      self.obj294.price.setValue(0)

      # name
      self.obj294.name.setValue('')
      self.obj294.name.setNone()

      self.obj294.GGLabel.setValue(1)
      self.obj294.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(80.0,20.0,self.obj294)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj294.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj294)
      self.obj294.postAction( self.RHS.CREATE )

      self.obj295=Role(parent)
      self.obj295.preAction( self.RHS.CREATE )
      self.obj295.isGraphObjectVisual = True

      if(hasattr(self.obj295, '_setHierarchicalLink')):
        self.obj295._setHierarchicalLink(False)

      # name
      self.obj295.name.setValue('')
      self.obj295.name.setNone()

      self.obj295.GGLabel.setValue(2)
      self.obj295.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(200.0,100.0,self.obj295)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj295.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj295)
      self.obj295.postAction( self.RHS.CREATE )

      self.obj296=Goal(parent)
      self.obj296.preAction( self.RHS.CREATE )
      self.obj296.isGraphObjectVisual = True

      if(hasattr(self.obj296, '_setHierarchicalLink')):
        self.obj296._setHierarchicalLink(False)

      # name
      self.obj296.name.setValue('')
      self.obj296.name.setNone()

      self.obj296.GGLabel.setValue(3)
      self.obj296.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(100.0,180.0,self.obj296)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj296.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj296)
      self.obj296.postAction( self.RHS.CREATE )

      self.obj297=CapableOf(parent)
      self.obj297.preAction( self.RHS.CREATE )
      self.obj297.isGraphObjectVisual = True

      if(hasattr(self.obj297, '_setHierarchicalLink')):
        self.obj297._setHierarchicalLink(False)

      self.obj297.GGLabel.setValue(4)
      self.obj297.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(164.5,91.5,self.obj297)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj297.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj297)
      self.obj297.postAction( self.RHS.CREATE )

      self.obj298=achieve(parent)
      self.obj298.preAction( self.RHS.CREATE )
      self.obj298.isGraphObjectVisual = True

      if(hasattr(self.obj298, '_setHierarchicalLink')):
        self.obj298._setHierarchicalLink(False)

      # rate
      self.obj298.rate.setValue(0.0)

      self.obj298.GGLabel.setValue(5)
      self.obj298.graphClass_= graph_achieve
      if parent.genGraphics:
         new_obj = graph_achieve(173.5,163.5,self.obj298)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj298.graphObject_ = new_obj
      self.obj2980= AttrCalc()
      self.obj2980.Copy=ATOM3Boolean()
      self.obj2980.Copy.setValue(('Copy from LHS', 1))
      self.obj2980.Copy.config = 0
      self.obj2980.Specify=ATOM3Constraint()
      self.obj2980.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj298.GGset2Any['rate']= self.obj2980

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj298)
      self.obj298.postAction( self.RHS.CREATE )

      self.obj299=operatingUnit(parent)
      self.obj299.preAction( self.RHS.CREATE )
      self.obj299.isGraphObjectVisual = True

      if(hasattr(self.obj299, '_setHierarchicalLink')):
        self.obj299._setHierarchicalLink(False)

      # name
      self.obj299.name.setValue('')
      self.obj299.name.setNone()

      self.obj299.GGLabel.setValue(7)
      self.obj299.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(320.0,140.0,self.obj299)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj299.graphObject_ = new_obj
      self.obj2990= AttrCalc()
      self.obj2990.Copy=ATOM3Boolean()
      self.obj2990.Copy.setValue(('Copy from LHS', 0))
      self.obj2990.Copy.config = 0
      self.obj2990.Specify=ATOM3Constraint()
      self.obj2990.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()+\' \'+ self.getMatched(graphID, self.LHS.nodeWithLabel(2)).name.getValue()+\' \'+ self.getMatched(graphID, self.LHS.nodeWithLabel(3)).name.getValue()\n'))
      self.obj299.GGset2Any['name']= self.obj2990

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj299)
      self.obj299.postAction( self.RHS.CREATE )

      self.obj300=metarial(parent)
      self.obj300.preAction( self.RHS.CREATE )
      self.obj300.isGraphObjectVisual = True

      if(hasattr(self.obj300, '_setHierarchicalLink')):
        self.obj300._setHierarchicalLink(False)

      # Name
      self.obj300.Name.setValue('')
      self.obj300.Name.setNone()

      self.obj300.GGLabel.setValue(8)
      self.obj300.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(320.0,40.0,self.obj300)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj300.graphObject_ = new_obj
      self.obj3000= AttrCalc()
      self.obj3000.Copy=ATOM3Boolean()
      self.obj3000.Copy.setValue(('Copy from LHS', 0))
      self.obj3000.Copy.config = 0
      self.obj3000.Specify=ATOM3Constraint()
      self.obj3000.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()+\' \'+ self.getMatched(graphID, self.LHS.nodeWithLabel(2)).name.getValue()+\' \'+ self.getMatched(graphID, self.LHS.nodeWithLabel(3)).name.getValue()\n'))
      self.obj300.GGset2Any['Name']= self.obj3000

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj300)
      self.obj300.postAction( self.RHS.CREATE )

      self.obj301=fromMaterial(parent)
      self.obj301.preAction( self.RHS.CREATE )
      self.obj301.isGraphObjectVisual = True

      if(hasattr(self.obj301, '_setHierarchicalLink')):
        self.obj301._setHierarchicalLink(False)

      # rate
      self.obj301.rate.setValue(1.0)

      self.obj301.GGLabel.setValue(9)
      self.obj301.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(338.785046729,119.210526316,self.obj301)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj301.graphObject_ = new_obj
      self.obj3010= AttrCalc()
      self.obj3010.Copy=ATOM3Boolean()
      self.obj3010.Copy.setValue(('Copy from LHS', 0))
      self.obj3010.Copy.config = 0
      self.obj3010.Specify=ATOM3Constraint()
      self.obj3010.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj301.GGset2Any['rate']= self.obj3010

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj301)
      self.obj301.postAction( self.RHS.CREATE )

      self.obj302=GenericGraphEdge(parent)
      self.obj302.preAction( self.RHS.CREATE )
      self.obj302.isGraphObjectVisual = True

      if(hasattr(self.obj302, '_setHierarchicalLink')):
        self.obj302._setHierarchicalLink(False)

      self.obj302.GGLabel.setValue(10)
      self.obj302.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(280.5,92.0,self.obj302)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj302.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj302)
      self.obj302.postAction( self.RHS.CREATE )

      self.obj294.out_connections_.append(self.obj297)
      self.obj297.in_connections_.append(self.obj294)
      self.obj294.graphObject_.pendingConnections.append((self.obj294.graphObject_.tag, self.obj297.graphObject_.tag, [117.0, 82.0, 164.5, 91.5], 2, 0))
      self.obj295.out_connections_.append(self.obj298)
      self.obj298.in_connections_.append(self.obj295)
      self.obj295.graphObject_.pendingConnections.append((self.obj295.graphObject_.tag, self.obj298.graphObject_.tag, [231.0, 145.0, 173.5, 163.5], 2, 0))
      self.obj295.out_connections_.append(self.obj302)
      self.obj302.in_connections_.append(self.obj295)
      self.obj295.graphObject_.pendingConnections.append((self.obj295.graphObject_.tag, self.obj302.graphObject_.tag, [231.0, 100.0, 280.5, 92.0], 0, True))
      self.obj297.out_connections_.append(self.obj295)
      self.obj295.in_connections_.append(self.obj297)
      self.obj297.graphObject_.pendingConnections.append((self.obj297.graphObject_.tag, self.obj295.graphObject_.tag, [231.0, 100.0, 164.5, 91.5], 2, 0))
      self.obj298.out_connections_.append(self.obj296)
      self.obj296.in_connections_.append(self.obj298)
      self.obj298.graphObject_.pendingConnections.append((self.obj298.graphObject_.tag, self.obj296.graphObject_.tag, [133.0, 181.0, 173.5, 163.5], 2, 0))
      self.obj300.out_connections_.append(self.obj301)
      self.obj301.in_connections_.append(self.obj300)
      self.obj300.graphObject_.pendingConnections.append((self.obj300.graphObject_.tag, self.obj301.graphObject_.tag, [344.0, 90.0, 338.78504672897196, 119.21052631578948], 0, True))
      self.obj301.out_connections_.append(self.obj299)
      self.obj299.in_connections_.append(self.obj301)
      self.obj301.graphObject_.pendingConnections.append((self.obj301.graphObject_.tag, self.obj299.graphObject_.tag, [333.5700934579439, 148.42105263157896, 338.78504672897196, 119.21052631578948], 0, True))
      self.obj302.out_connections_.append(self.obj300)
      self.obj300.in_connections_.append(self.obj302)
      self.obj302.graphObject_.pendingConnections.append((self.obj302.graphObject_.tag, self.obj300.graphObject_.tag, [330.0, 84.0, 280.5, 92.0], 0, True))

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
      
      

