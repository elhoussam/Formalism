# _ CollectInf3_GG_rule.py ____________________________________________________________________________
# File generated automatically by ATOM3. Graph Grammar Rule
# ___________________________________________________________________________________________
from GGrule import *
from CapableOf import *
from Goal import *
from require import *
from Agent import *
from Capabilitie import *
from Role import *
from ASG_omacs import *
from achieve import *
from posses import *
class CollectInf3_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 6)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_omacs(parent)

      self.obj1596=Role(parent)
      self.obj1596.preAction( self.LHS.CREATE )
      self.obj1596.isGraphObjectVisual = True

      if(hasattr(self.obj1596, '_setHierarchicalLink')):
        self.obj1596._setHierarchicalLink(False)

      # name
      self.obj1596.name.setValue('')
      self.obj1596.name.setNone()

      self.obj1596.GGLabel.setValue(2)
      self.obj1596.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(40.0,40.0,self.obj1596)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1596.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1596)
      self.obj1596.postAction( self.LHS.CREATE )

      self.obj1597=Goal(parent)
      self.obj1597.preAction( self.LHS.CREATE )
      self.obj1597.isGraphObjectVisual = True

      if(hasattr(self.obj1597, '_setHierarchicalLink')):
        self.obj1597._setHierarchicalLink(False)

      # name
      self.obj1597.name.setValue('')
      self.obj1597.name.setNone()

      self.obj1597.GGLabel.setValue(1)
      self.obj1597.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(300.0,160.0,self.obj1597)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1597.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1597)
      self.obj1597.postAction( self.LHS.CREATE )

      self.obj1598=achieve(parent)
      self.obj1598.preAction( self.LHS.CREATE )
      self.obj1598.isGraphObjectVisual = True

      if(hasattr(self.obj1598, '_setHierarchicalLink')):
        self.obj1598._setHierarchicalLink(False)

      # rate
      self.obj1598.rate.setNone()

      self.obj1598.GGLabel.setValue(3)
      self.obj1598.graphClass_= graph_achieve
      if parent.genGraphics:
         new_obj = graph_achieve(171.25,141.25,self.obj1598)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1598.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1598)
      self.obj1598.postAction( self.LHS.CREATE )

      self.obj1596.out_connections_.append(self.obj1598)
      self.obj1598.in_connections_.append(self.obj1596)
      self.obj1596.graphObject_.pendingConnections.append((self.obj1596.graphObject_.tag, self.obj1598.graphObject_.tag, [64.0, 86.0, 106.5, 122.5, 171.25, 141.25], 2, True))
      self.obj1598.out_connections_.append(self.obj1597)
      self.obj1597.in_connections_.append(self.obj1598)
      self.obj1598.graphObject_.pendingConnections.append((self.obj1598.graphObject_.tag, self.obj1597.graphObject_.tag, [323.0, 161.0, 236.0, 160.0, 171.25, 141.25], 2, True))

      self.RHS = ASG_omacs(parent)

      self.obj1600=Role(parent)
      self.obj1600.preAction( self.RHS.CREATE )
      self.obj1600.isGraphObjectVisual = True

      if(hasattr(self.obj1600, '_setHierarchicalLink')):
        self.obj1600._setHierarchicalLink(False)

      # name
      self.obj1600.name.setValue('')
      self.obj1600.name.setNone()

      self.obj1600.GGLabel.setValue(2)
      self.obj1600.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(40.0,40.0,self.obj1600)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1600.graphObject_ = new_obj
      self.obj16000= AttrCalc()
      self.obj16000.Copy=ATOM3Boolean()
      self.obj16000.Copy.setValue(('Copy from LHS', 1))
      self.obj16000.Copy.config = 0
      self.obj16000.Specify=ATOM3Constraint()
      self.obj16000.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1600.GGset2Any['name']= self.obj16000

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1600)
      self.obj1600.postAction( self.RHS.CREATE )

      self.obj1601=Goal(parent)
      self.obj1601.preAction( self.RHS.CREATE )
      self.obj1601.isGraphObjectVisual = True

      if(hasattr(self.obj1601, '_setHierarchicalLink')):
        self.obj1601._setHierarchicalLink(False)

      # name
      self.obj1601.name.setValue('')
      self.obj1601.name.setNone()

      self.obj1601.GGLabel.setValue(1)
      self.obj1601.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(300.0,160.0,self.obj1601)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1601.graphObject_ = new_obj
      self.obj16010= AttrCalc()
      self.obj16010.Copy=ATOM3Boolean()
      self.obj16010.Copy.setValue(('Copy from LHS', 1))
      self.obj16010.Copy.config = 0
      self.obj16010.Specify=ATOM3Constraint()
      self.obj16010.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1601.GGset2Any['name']= self.obj16010

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1601)
      self.obj1601.postAction( self.RHS.CREATE )

      self.obj1602=achieve(parent)
      self.obj1602.preAction( self.RHS.CREATE )
      self.obj1602.isGraphObjectVisual = True

      if(hasattr(self.obj1602, '_setHierarchicalLink')):
        self.obj1602._setHierarchicalLink(False)

      # rate
      self.obj1602.rate.setNone()

      self.obj1602.GGLabel.setValue(3)
      self.obj1602.graphClass_= graph_achieve
      if parent.genGraphics:
         new_obj = graph_achieve(171.25,141.25,self.obj1602)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1602.graphObject_ = new_obj
      self.obj16020= AttrCalc()
      self.obj16020.Copy=ATOM3Boolean()
      self.obj16020.Copy.setValue(('Copy from LHS', 1))
      self.obj16020.Copy.config = 0
      self.obj16020.Specify=ATOM3Constraint()
      self.obj16020.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1602.GGset2Any['rate']= self.obj16020

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1602)
      self.obj1602.postAction( self.RHS.CREATE )

      self.obj1600.out_connections_.append(self.obj1602)
      self.obj1602.in_connections_.append(self.obj1600)
      self.obj1600.graphObject_.pendingConnections.append((self.obj1600.graphObject_.tag, self.obj1602.graphObject_.tag, [71.0, 85.0, 171.25, 141.25], 2, 0))
      self.obj1602.out_connections_.append(self.obj1601)
      self.obj1601.in_connections_.append(self.obj1602)
      self.obj1602.graphObject_.pendingConnections.append((self.obj1602.graphObject_.tag, self.obj1601.graphObject_.tag, [333.0, 161.0, 171.25, 141.25], 2, 0))

   def condition(self, graphID, isograph, atom3i):
      
      g = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      r  = self.getMatched(graphID, self.LHS.nodeWithLabel(2))
      link  = self.getMatched(graphID, self.LHS.nodeWithLabel(3))
      
      return not ( hasattr(link,  "rule2"+g.name.getValue()+r.name.getValue() ))
      
      

   def action(self, graphID, isograph, atom3i):
      g = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      r  = self.getMatched(graphID, self.LHS.nodeWithLabel(2))
      link  = self.getMatched(graphID, self.LHS.nodeWithLabel(3))
      
      setattr( link ,  "rule2"+g.name.getValue()+r.name.getValue() , True )
      
      print "Collect 3 "+g.name.getValue()+" "+r.name.getValue()+" "+str(link.rate.getValue() )
      if not (r.name.getValue() in self.graphRewritingSystem.Dictro.keys() ) :
       self.graphRewritingSystem.Dictro[r.name.getValue()] = {}
      self.graphRewritingSystem.Dictro[r.name.getValue()][g.name.getValue()] = link.rate.getValue()
      
      print "Collect inf 3 DictRole "+str( self.graphRewritingSystem.Dictro )
      
      

