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

      self.obj584=Agent(parent)
      self.obj584.preAction( self.LHS.CREATE )
      self.obj584.isGraphObjectVisual = True

      if(hasattr(self.obj584, '_setHierarchicalLink')):
        self.obj584._setHierarchicalLink(False)

      # price
      self.obj584.price.setNone()

      # name
      self.obj584.name.setValue('')
      self.obj584.name.setNone()

      self.obj584.GGLabel.setValue(1)
      self.obj584.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(40.0,20.0,self.obj584)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj584.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj584)
      self.obj584.postAction( self.LHS.CREATE )

      self.obj585=Role(parent)
      self.obj585.preAction( self.LHS.CREATE )
      self.obj585.isGraphObjectVisual = True

      if(hasattr(self.obj585, '_setHierarchicalLink')):
        self.obj585._setHierarchicalLink(False)

      # name
      self.obj585.name.setValue('')
      self.obj585.name.setNone()

      self.obj585.GGLabel.setValue(2)
      self.obj585.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(360.0,160.0,self.obj585)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj585.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj585)
      self.obj585.postAction( self.LHS.CREATE )

      self.obj586=CapableOf(parent)
      self.obj586.preAction( self.LHS.CREATE )
      self.obj586.isGraphObjectVisual = True

      if(hasattr(self.obj586, '_setHierarchicalLink')):
        self.obj586._setHierarchicalLink(False)

      # rate
      self.obj586.rate.setNone()

      self.obj586.GGLabel.setValue(3)
      self.obj586.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(220.0,114.5,self.obj586)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj586.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj586)
      self.obj586.postAction( self.LHS.CREATE )

      self.obj584.out_connections_.append(self.obj586)
      self.obj586.in_connections_.append(self.obj584)
      self.obj584.graphObject_.pendingConnections.append((self.obj584.graphObject_.tag, self.obj586.graphObject_.tag, [65.0, 82.0, 84.0, 138.0, 220.0, 114.5], 2, True))
      self.obj586.out_connections_.append(self.obj585)
      self.obj585.in_connections_.append(self.obj586)
      self.obj586.graphObject_.pendingConnections.append((self.obj586.graphObject_.tag, self.obj585.graphObject_.tag, [384.0, 161.0, 356.0, 91.0, 220.0, 114.5], 2, True))

      self.RHS = ASG_omacs(parent)

      self.obj588=Agent(parent)
      self.obj588.preAction( self.RHS.CREATE )
      self.obj588.isGraphObjectVisual = True

      if(hasattr(self.obj588, '_setHierarchicalLink')):
        self.obj588._setHierarchicalLink(False)

      # price
      self.obj588.price.setNone()

      # name
      self.obj588.name.setValue('')
      self.obj588.name.setNone()

      self.obj588.GGLabel.setValue(1)
      self.obj588.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(40.0,20.0,self.obj588)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj588.graphObject_ = new_obj
      self.obj5880= AttrCalc()
      self.obj5880.Copy=ATOM3Boolean()
      self.obj5880.Copy.setValue(('Copy from LHS', 1))
      self.obj5880.Copy.config = 0
      self.obj5880.Specify=ATOM3Constraint()
      self.obj5880.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj588.GGset2Any['price']= self.obj5880
      self.obj5881= AttrCalc()
      self.obj5881.Copy=ATOM3Boolean()
      self.obj5881.Copy.setValue(('Copy from LHS', 1))
      self.obj5881.Copy.config = 0
      self.obj5881.Specify=ATOM3Constraint()
      self.obj5881.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj588.GGset2Any['name']= self.obj5881

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj588)
      self.obj588.postAction( self.RHS.CREATE )

      self.obj589=Role(parent)
      self.obj589.preAction( self.RHS.CREATE )
      self.obj589.isGraphObjectVisual = True

      if(hasattr(self.obj589, '_setHierarchicalLink')):
        self.obj589._setHierarchicalLink(False)

      # name
      self.obj589.name.setValue('')
      self.obj589.name.setNone()

      self.obj589.GGLabel.setValue(2)
      self.obj589.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(360.0,160.0,self.obj589)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj589.graphObject_ = new_obj
      self.obj5890= AttrCalc()
      self.obj5890.Copy=ATOM3Boolean()
      self.obj5890.Copy.setValue(('Copy from LHS', 1))
      self.obj5890.Copy.config = 0
      self.obj5890.Specify=ATOM3Constraint()
      self.obj5890.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj589.GGset2Any['name']= self.obj5890

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj589)
      self.obj589.postAction( self.RHS.CREATE )

      self.obj590=CapableOf(parent)
      self.obj590.preAction( self.RHS.CREATE )
      self.obj590.isGraphObjectVisual = True

      if(hasattr(self.obj590, '_setHierarchicalLink')):
        self.obj590._setHierarchicalLink(False)

      # rate
      self.obj590.rate.setNone()

      self.obj590.GGLabel.setValue(3)
      self.obj590.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(220.0,114.5,self.obj590)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj590.graphObject_ = new_obj
      self.obj5900= AttrCalc()
      self.obj5900.Copy=ATOM3Boolean()
      self.obj5900.Copy.setValue(('Copy from LHS', 1))
      self.obj5900.Copy.config = 0
      self.obj5900.Specify=ATOM3Constraint()
      self.obj5900.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj590.GGset2Any['rate']= self.obj5900

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj590)
      self.obj590.postAction( self.RHS.CREATE )

      self.obj588.out_connections_.append(self.obj590)
      self.obj590.in_connections_.append(self.obj588)
      self.obj588.graphObject_.pendingConnections.append((self.obj588.graphObject_.tag, self.obj590.graphObject_.tag, [77.0, 82.0, 220.0, 114.5], 2, 0))
      self.obj590.out_connections_.append(self.obj589)
      self.obj589.in_connections_.append(self.obj590)
      self.obj590.graphObject_.pendingConnections.append((self.obj590.graphObject_.tag, self.obj589.graphObject_.tag, [391.0, 160.0, 220.0, 114.5], 2, 0))

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
      
      

