# _ CollectInf2_GG_rule.py ____________________________________________________________________________
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
class CollectInf2_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 5)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_omacs(parent)

      self.obj1585=Agent(parent)
      self.obj1585.preAction( self.LHS.CREATE )
      self.obj1585.isGraphObjectVisual = True

      if(hasattr(self.obj1585, '_setHierarchicalLink')):
        self.obj1585._setHierarchicalLink(False)

      # price
      self.obj1585.price.setNone()

      # name
      self.obj1585.name.setValue('')
      self.obj1585.name.setNone()

      self.obj1585.GGLabel.setValue(1)
      self.obj1585.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(40.0,20.0,self.obj1585)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1585.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1585)
      self.obj1585.postAction( self.LHS.CREATE )

      self.obj1586=Role(parent)
      self.obj1586.preAction( self.LHS.CREATE )
      self.obj1586.isGraphObjectVisual = True

      if(hasattr(self.obj1586, '_setHierarchicalLink')):
        self.obj1586._setHierarchicalLink(False)

      # name
      self.obj1586.name.setValue('')
      self.obj1586.name.setNone()

      self.obj1586.GGLabel.setValue(2)
      self.obj1586.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(360.0,160.0,self.obj1586)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1586.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1586)
      self.obj1586.postAction( self.LHS.CREATE )

      self.obj1587=CapableOf(parent)
      self.obj1587.preAction( self.LHS.CREATE )
      self.obj1587.isGraphObjectVisual = True

      if(hasattr(self.obj1587, '_setHierarchicalLink')):
        self.obj1587._setHierarchicalLink(False)

      # rate
      self.obj1587.rate.setNone()

      self.obj1587.GGLabel.setValue(3)
      self.obj1587.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(220.0,114.5,self.obj1587)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1587.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1587)
      self.obj1587.postAction( self.LHS.CREATE )

      self.obj1585.out_connections_.append(self.obj1587)
      self.obj1587.in_connections_.append(self.obj1585)
      self.obj1585.graphObject_.pendingConnections.append((self.obj1585.graphObject_.tag, self.obj1587.graphObject_.tag, [65.0, 82.0, 84.0, 138.0, 220.0, 114.5], 2, True))
      self.obj1587.out_connections_.append(self.obj1586)
      self.obj1586.in_connections_.append(self.obj1587)
      self.obj1587.graphObject_.pendingConnections.append((self.obj1587.graphObject_.tag, self.obj1586.graphObject_.tag, [384.0, 161.0, 356.0, 91.0, 220.0, 114.5], 2, True))

      self.RHS = ASG_omacs(parent)

      self.obj1589=Agent(parent)
      self.obj1589.preAction( self.RHS.CREATE )
      self.obj1589.isGraphObjectVisual = True

      if(hasattr(self.obj1589, '_setHierarchicalLink')):
        self.obj1589._setHierarchicalLink(False)

      # price
      self.obj1589.price.setNone()

      # name
      self.obj1589.name.setValue('')
      self.obj1589.name.setNone()

      self.obj1589.GGLabel.setValue(1)
      self.obj1589.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(40.0,20.0,self.obj1589)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1589.graphObject_ = new_obj
      self.obj15890= AttrCalc()
      self.obj15890.Copy=ATOM3Boolean()
      self.obj15890.Copy.setValue(('Copy from LHS', 1))
      self.obj15890.Copy.config = 0
      self.obj15890.Specify=ATOM3Constraint()
      self.obj15890.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1589.GGset2Any['price']= self.obj15890
      self.obj15891= AttrCalc()
      self.obj15891.Copy=ATOM3Boolean()
      self.obj15891.Copy.setValue(('Copy from LHS', 1))
      self.obj15891.Copy.config = 0
      self.obj15891.Specify=ATOM3Constraint()
      self.obj15891.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1589.GGset2Any['name']= self.obj15891

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1589)
      self.obj1589.postAction( self.RHS.CREATE )

      self.obj1590=Role(parent)
      self.obj1590.preAction( self.RHS.CREATE )
      self.obj1590.isGraphObjectVisual = True

      if(hasattr(self.obj1590, '_setHierarchicalLink')):
        self.obj1590._setHierarchicalLink(False)

      # name
      self.obj1590.name.setValue('')
      self.obj1590.name.setNone()

      self.obj1590.GGLabel.setValue(2)
      self.obj1590.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(360.0,160.0,self.obj1590)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1590.graphObject_ = new_obj
      self.obj15900= AttrCalc()
      self.obj15900.Copy=ATOM3Boolean()
      self.obj15900.Copy.setValue(('Copy from LHS', 1))
      self.obj15900.Copy.config = 0
      self.obj15900.Specify=ATOM3Constraint()
      self.obj15900.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1590.GGset2Any['name']= self.obj15900

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1590)
      self.obj1590.postAction( self.RHS.CREATE )

      self.obj1591=CapableOf(parent)
      self.obj1591.preAction( self.RHS.CREATE )
      self.obj1591.isGraphObjectVisual = True

      if(hasattr(self.obj1591, '_setHierarchicalLink')):
        self.obj1591._setHierarchicalLink(False)

      # rate
      self.obj1591.rate.setNone()

      self.obj1591.GGLabel.setValue(3)
      self.obj1591.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(220.0,114.5,self.obj1591)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1591.graphObject_ = new_obj
      self.obj15910= AttrCalc()
      self.obj15910.Copy=ATOM3Boolean()
      self.obj15910.Copy.setValue(('Copy from LHS', 1))
      self.obj15910.Copy.config = 0
      self.obj15910.Specify=ATOM3Constraint()
      self.obj15910.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1591.GGset2Any['rate']= self.obj15910

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1591)
      self.obj1591.postAction( self.RHS.CREATE )

      self.obj1589.out_connections_.append(self.obj1591)
      self.obj1591.in_connections_.append(self.obj1589)
      self.obj1589.graphObject_.pendingConnections.append((self.obj1589.graphObject_.tag, self.obj1591.graphObject_.tag, [77.0, 82.0, 220.0, 114.5], 2, 0))
      self.obj1591.out_connections_.append(self.obj1590)
      self.obj1590.in_connections_.append(self.obj1591)
      self.obj1591.graphObject_.pendingConnections.append((self.obj1591.graphObject_.tag, self.obj1590.graphObject_.tag, [391.0, 160.0, 220.0, 114.5], 2, 0))

   def condition(self, graphID, isograph, atom3i):
      link = self.getMatched(graphID, self.LHS.nodeWithLabel(3))
      return not ( hasattr(link,"done") )
      
      

   def action(self, graphID, isograph, atom3i):
      a = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      r = self.getMatched(graphID, self.LHS.nodeWithLabel(2))
      link = self.getMatched(graphID, self.LHS.nodeWithLabel(3))
      
      link.done = True 
      
      
      print "Collect 2 "+a.name.getValue()+" "+r.name.getValue()+" "+str(link.rate.getValue())
      
      self.graphRewritingSystem.Dictag[a.name.getValue()][r.name.getValue()] /=  self.graphRewritingSystem.Dictag[a.name.getValue()]["nb"+r.name.getValue()]
      round( self.graphRewritingSystem.Dictag[a.name.getValue()][r.name.getValue()] ,3)
      print "Collect 2  : "+str(  self.graphRewritingSystem.Dictag )
      
      

