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

      self.obj595=Role(parent)
      self.obj595.preAction( self.LHS.CREATE )
      self.obj595.isGraphObjectVisual = True

      if(hasattr(self.obj595, '_setHierarchicalLink')):
        self.obj595._setHierarchicalLink(False)

      # name
      self.obj595.name.setValue('')
      self.obj595.name.setNone()

      self.obj595.GGLabel.setValue(2)
      self.obj595.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(40.0,40.0,self.obj595)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj595.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj595)
      self.obj595.postAction( self.LHS.CREATE )

      self.obj596=Goal(parent)
      self.obj596.preAction( self.LHS.CREATE )
      self.obj596.isGraphObjectVisual = True

      if(hasattr(self.obj596, '_setHierarchicalLink')):
        self.obj596._setHierarchicalLink(False)

      # name
      self.obj596.name.setValue('')
      self.obj596.name.setNone()

      self.obj596.GGLabel.setValue(1)
      self.obj596.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(300.0,160.0,self.obj596)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj596.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj596)
      self.obj596.postAction( self.LHS.CREATE )

      self.obj597=achieve(parent)
      self.obj597.preAction( self.LHS.CREATE )
      self.obj597.isGraphObjectVisual = True

      if(hasattr(self.obj597, '_setHierarchicalLink')):
        self.obj597._setHierarchicalLink(False)

      # rate
      self.obj597.rate.setNone()

      self.obj597.GGLabel.setValue(3)
      self.obj597.graphClass_= graph_achieve
      if parent.genGraphics:
         new_obj = graph_achieve(171.25,141.25,self.obj597)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj597.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj597)
      self.obj597.postAction( self.LHS.CREATE )

      self.obj595.out_connections_.append(self.obj597)
      self.obj597.in_connections_.append(self.obj595)
      self.obj595.graphObject_.pendingConnections.append((self.obj595.graphObject_.tag, self.obj597.graphObject_.tag, [64.0, 86.0, 106.5, 122.5, 171.25, 141.25], 2, True))
      self.obj597.out_connections_.append(self.obj596)
      self.obj596.in_connections_.append(self.obj597)
      self.obj597.graphObject_.pendingConnections.append((self.obj597.graphObject_.tag, self.obj596.graphObject_.tag, [323.0, 161.0, 236.0, 160.0, 171.25, 141.25], 2, True))

      self.RHS = ASG_omacs(parent)

      self.obj599=Role(parent)
      self.obj599.preAction( self.RHS.CREATE )
      self.obj599.isGraphObjectVisual = True

      if(hasattr(self.obj599, '_setHierarchicalLink')):
        self.obj599._setHierarchicalLink(False)

      # name
      self.obj599.name.setValue('')
      self.obj599.name.setNone()

      self.obj599.GGLabel.setValue(2)
      self.obj599.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(40.0,40.0,self.obj599)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj599.graphObject_ = new_obj
      self.obj5990= AttrCalc()
      self.obj5990.Copy=ATOM3Boolean()
      self.obj5990.Copy.setValue(('Copy from LHS', 1))
      self.obj5990.Copy.config = 0
      self.obj5990.Specify=ATOM3Constraint()
      self.obj5990.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj599.GGset2Any['name']= self.obj5990

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj599)
      self.obj599.postAction( self.RHS.CREATE )

      self.obj600=Goal(parent)
      self.obj600.preAction( self.RHS.CREATE )
      self.obj600.isGraphObjectVisual = True

      if(hasattr(self.obj600, '_setHierarchicalLink')):
        self.obj600._setHierarchicalLink(False)

      # name
      self.obj600.name.setValue('')
      self.obj600.name.setNone()

      self.obj600.GGLabel.setValue(1)
      self.obj600.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(300.0,160.0,self.obj600)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj600.graphObject_ = new_obj
      self.obj6000= AttrCalc()
      self.obj6000.Copy=ATOM3Boolean()
      self.obj6000.Copy.setValue(('Copy from LHS', 1))
      self.obj6000.Copy.config = 0
      self.obj6000.Specify=ATOM3Constraint()
      self.obj6000.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj600.GGset2Any['name']= self.obj6000

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj600)
      self.obj600.postAction( self.RHS.CREATE )

      self.obj601=achieve(parent)
      self.obj601.preAction( self.RHS.CREATE )
      self.obj601.isGraphObjectVisual = True

      if(hasattr(self.obj601, '_setHierarchicalLink')):
        self.obj601._setHierarchicalLink(False)

      # rate
      self.obj601.rate.setNone()

      self.obj601.GGLabel.setValue(3)
      self.obj601.graphClass_= graph_achieve
      if parent.genGraphics:
         new_obj = graph_achieve(171.25,141.25,self.obj601)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj601.graphObject_ = new_obj
      self.obj6010= AttrCalc()
      self.obj6010.Copy=ATOM3Boolean()
      self.obj6010.Copy.setValue(('Copy from LHS', 1))
      self.obj6010.Copy.config = 0
      self.obj6010.Specify=ATOM3Constraint()
      self.obj6010.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj601.GGset2Any['rate']= self.obj6010

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj601)
      self.obj601.postAction( self.RHS.CREATE )

      self.obj599.out_connections_.append(self.obj601)
      self.obj601.in_connections_.append(self.obj599)
      self.obj599.graphObject_.pendingConnections.append((self.obj599.graphObject_.tag, self.obj601.graphObject_.tag, [71.0, 85.0, 171.25, 141.25], 2, 0))
      self.obj601.out_connections_.append(self.obj600)
      self.obj600.in_connections_.append(self.obj601)
      self.obj601.graphObject_.pendingConnections.append((self.obj601.graphObject_.tag, self.obj600.graphObject_.tag, [333.0, 161.0, 171.25, 141.25], 2, 0))

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
      
      

