# _ CollectInf1_GG_rule.py ____________________________________________________________________________
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
class CollectInf1_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 4)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_omacs(parent)

      self.obj567=Agent(parent)
      self.obj567.preAction( self.LHS.CREATE )
      self.obj567.isGraphObjectVisual = True

      if(hasattr(self.obj567, '_setHierarchicalLink')):
        self.obj567._setHierarchicalLink(False)

      # price
      self.obj567.price.setNone()

      # name
      self.obj567.name.setValue('')
      self.obj567.name.setNone()

      self.obj567.GGLabel.setValue(1)
      self.obj567.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(20.0,20.0,self.obj567)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj567.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj567)
      self.obj567.postAction( self.LHS.CREATE )

      self.obj568=Capabilitie(parent)
      self.obj568.preAction( self.LHS.CREATE )
      self.obj568.isGraphObjectVisual = True

      if(hasattr(self.obj568, '_setHierarchicalLink')):
        self.obj568._setHierarchicalLink(False)

      # name
      self.obj568.name.setValue('')
      self.obj568.name.setNone()

      self.obj568.GGLabel.setValue(3)
      self.obj568.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(140.0,160.0,self.obj568)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj568.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj568)
      self.obj568.postAction( self.LHS.CREATE )

      self.obj569=Role(parent)
      self.obj569.preAction( self.LHS.CREATE )
      self.obj569.isGraphObjectVisual = True

      if(hasattr(self.obj569, '_setHierarchicalLink')):
        self.obj569._setHierarchicalLink(False)

      # name
      self.obj569.name.setValue('')
      self.obj569.name.setNone()

      self.obj569.GGLabel.setValue(2)
      self.obj569.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(380.0,180.0,self.obj569)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj569.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj569)
      self.obj569.postAction( self.LHS.CREATE )

      self.obj570=posses(parent)
      self.obj570.preAction( self.LHS.CREATE )
      self.obj570.isGraphObjectVisual = True

      if(hasattr(self.obj570, '_setHierarchicalLink')):
        self.obj570._setHierarchicalLink(False)

      # rate
      self.obj570.rate.setNone()

      self.obj570.GGLabel.setValue(4)
      self.obj570.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(78.5,145.75,self.obj570)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj570.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj570)
      self.obj570.postAction( self.LHS.CREATE )

      self.obj571=CapableOf(parent)
      self.obj571.preAction( self.LHS.CREATE )
      self.obj571.isGraphObjectVisual = True

      if(hasattr(self.obj571, '_setHierarchicalLink')):
        self.obj571._setHierarchicalLink(False)

      # rate
      self.obj571.rate.setNone()

      self.obj571.GGLabel.setValue(6)
      self.obj571.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(295.25,111.25,self.obj571)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj571.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj571)
      self.obj571.postAction( self.LHS.CREATE )

      self.obj572=require(parent)
      self.obj572.preAction( self.LHS.CREATE )
      self.obj572.isGraphObjectVisual = True

      if(hasattr(self.obj572, '_setHierarchicalLink')):
        self.obj572._setHierarchicalLink(False)

      self.obj572.GGLabel.setValue(5)
      self.obj572.graphClass_= graph_require
      if parent.genGraphics:
         new_obj = graph_require(291.0,171.5,self.obj572)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj572.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj572)
      self.obj572.postAction( self.LHS.CREATE )

      self.obj567.out_connections_.append(self.obj570)
      self.obj570.in_connections_.append(self.obj567)
      self.obj567.graphObject_.pendingConnections.append((self.obj567.graphObject_.tag, self.obj570.graphObject_.tag, [45.0, 82.0, 49.5, 126.5, 78.5, 145.75], 2, True))
      self.obj567.out_connections_.append(self.obj571)
      self.obj571.in_connections_.append(self.obj567)
      self.obj567.graphObject_.pendingConnections.append((self.obj567.graphObject_.tag, self.obj571.graphObject_.tag, [45.0, 82.0, 205.5, 86.5, 295.25, 111.25], 2, True))
      self.obj569.out_connections_.append(self.obj572)
      self.obj572.in_connections_.append(self.obj569)
      self.obj569.graphObject_.pendingConnections.append((self.obj569.graphObject_.tag, self.obj572.graphObject_.tag, [404.0, 181.0, 374.0, 146.0, 291.0, 171.5], 2, True))
      self.obj570.out_connections_.append(self.obj568)
      self.obj568.in_connections_.append(self.obj570)
      self.obj570.graphObject_.pendingConnections.append((self.obj570.graphObject_.tag, self.obj568.graphObject_.tag, [161.0, 159.0, 107.5, 165.0, 78.5, 145.75], 2, True))
      self.obj571.out_connections_.append(self.obj569)
      self.obj569.in_connections_.append(self.obj571)
      self.obj571.graphObject_.pendingConnections.append((self.obj571.graphObject_.tag, self.obj569.graphObject_.tag, [404.0, 181.0, 385.0, 136.0, 295.25, 111.25], 2, True))
      self.obj572.out_connections_.append(self.obj568)
      self.obj568.in_connections_.append(self.obj572)
      self.obj572.graphObject_.pendingConnections.append((self.obj572.graphObject_.tag, self.obj568.graphObject_.tag, [161.0, 199.0, 208.0, 197.0, 291.0, 171.5], 2, True))

      self.RHS = ASG_omacs(parent)

      self.obj574=Agent(parent)
      self.obj574.preAction( self.RHS.CREATE )
      self.obj574.isGraphObjectVisual = True

      if(hasattr(self.obj574, '_setHierarchicalLink')):
        self.obj574._setHierarchicalLink(False)

      # price
      self.obj574.price.setNone()

      # name
      self.obj574.name.setValue('')
      self.obj574.name.setNone()

      self.obj574.GGLabel.setValue(1)
      self.obj574.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(20.0,20.0,self.obj574)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj574.graphObject_ = new_obj
      self.obj5740= AttrCalc()
      self.obj5740.Copy=ATOM3Boolean()
      self.obj5740.Copy.setValue(('Copy from LHS', 1))
      self.obj5740.Copy.config = 0
      self.obj5740.Specify=ATOM3Constraint()
      self.obj5740.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj574.GGset2Any['price']= self.obj5740
      self.obj5741= AttrCalc()
      self.obj5741.Copy=ATOM3Boolean()
      self.obj5741.Copy.setValue(('Copy from LHS', 1))
      self.obj5741.Copy.config = 0
      self.obj5741.Specify=ATOM3Constraint()
      self.obj5741.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj574.GGset2Any['name']= self.obj5741

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj574)
      self.obj574.postAction( self.RHS.CREATE )

      self.obj575=Capabilitie(parent)
      self.obj575.preAction( self.RHS.CREATE )
      self.obj575.isGraphObjectVisual = True

      if(hasattr(self.obj575, '_setHierarchicalLink')):
        self.obj575._setHierarchicalLink(False)

      # name
      self.obj575.name.setValue('')
      self.obj575.name.setNone()

      self.obj575.GGLabel.setValue(3)
      self.obj575.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(140.0,160.0,self.obj575)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj575.graphObject_ = new_obj
      self.obj5750= AttrCalc()
      self.obj5750.Copy=ATOM3Boolean()
      self.obj5750.Copy.setValue(('Copy from LHS', 1))
      self.obj5750.Copy.config = 0
      self.obj5750.Specify=ATOM3Constraint()
      self.obj5750.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj575.GGset2Any['name']= self.obj5750

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj575)
      self.obj575.postAction( self.RHS.CREATE )

      self.obj576=Role(parent)
      self.obj576.preAction( self.RHS.CREATE )
      self.obj576.isGraphObjectVisual = True

      if(hasattr(self.obj576, '_setHierarchicalLink')):
        self.obj576._setHierarchicalLink(False)

      # name
      self.obj576.name.setValue('')
      self.obj576.name.setNone()

      self.obj576.GGLabel.setValue(2)
      self.obj576.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(380.0,180.0,self.obj576)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj576.graphObject_ = new_obj
      self.obj5760= AttrCalc()
      self.obj5760.Copy=ATOM3Boolean()
      self.obj5760.Copy.setValue(('Copy from LHS', 1))
      self.obj5760.Copy.config = 0
      self.obj5760.Specify=ATOM3Constraint()
      self.obj5760.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj576.GGset2Any['name']= self.obj5760

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj576)
      self.obj576.postAction( self.RHS.CREATE )

      self.obj577=posses(parent)
      self.obj577.preAction( self.RHS.CREATE )
      self.obj577.isGraphObjectVisual = True

      if(hasattr(self.obj577, '_setHierarchicalLink')):
        self.obj577._setHierarchicalLink(False)

      # rate
      self.obj577.rate.setNone()

      self.obj577.GGLabel.setValue(4)
      self.obj577.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(78.5,145.75,self.obj577)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj577.graphObject_ = new_obj
      self.obj5770= AttrCalc()
      self.obj5770.Copy=ATOM3Boolean()
      self.obj5770.Copy.setValue(('Copy from LHS', 1))
      self.obj5770.Copy.config = 0
      self.obj5770.Specify=ATOM3Constraint()
      self.obj5770.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj577.GGset2Any['rate']= self.obj5770

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj577)
      self.obj577.postAction( self.RHS.CREATE )

      self.obj578=CapableOf(parent)
      self.obj578.preAction( self.RHS.CREATE )
      self.obj578.isGraphObjectVisual = True

      if(hasattr(self.obj578, '_setHierarchicalLink')):
        self.obj578._setHierarchicalLink(False)

      # rate
      self.obj578.rate.setNone()

      self.obj578.GGLabel.setValue(6)
      self.obj578.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(295.25,111.25,self.obj578)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj578.graphObject_ = new_obj
      self.obj5780= AttrCalc()
      self.obj5780.Copy=ATOM3Boolean()
      self.obj5780.Copy.setValue(('Copy from LHS', 1))
      self.obj5780.Copy.config = 0
      self.obj5780.Specify=ATOM3Constraint()
      self.obj5780.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj578.GGset2Any['rate']= self.obj5780

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj578)
      self.obj578.postAction( self.RHS.CREATE )

      self.obj579=require(parent)
      self.obj579.preAction( self.RHS.CREATE )
      self.obj579.isGraphObjectVisual = True

      if(hasattr(self.obj579, '_setHierarchicalLink')):
        self.obj579._setHierarchicalLink(False)

      self.obj579.GGLabel.setValue(5)
      self.obj579.graphClass_= graph_require
      if parent.genGraphics:
         new_obj = graph_require(291.0,171.5,self.obj579)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj579.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj579)
      self.obj579.postAction( self.RHS.CREATE )

      self.obj574.out_connections_.append(self.obj577)
      self.obj577.in_connections_.append(self.obj574)
      self.obj574.graphObject_.pendingConnections.append((self.obj574.graphObject_.tag, self.obj577.graphObject_.tag, [57.0, 82.0, 78.5, 145.75], 2, 0))
      self.obj574.out_connections_.append(self.obj578)
      self.obj578.in_connections_.append(self.obj574)
      self.obj574.graphObject_.pendingConnections.append((self.obj574.graphObject_.tag, self.obj578.graphObject_.tag, [57.0, 82.0, 295.25, 111.25], 2, 0))
      self.obj576.out_connections_.append(self.obj579)
      self.obj579.in_connections_.append(self.obj576)
      self.obj576.graphObject_.pendingConnections.append((self.obj576.graphObject_.tag, self.obj579.graphObject_.tag, [411.0, 180.0, 291.0, 171.5], 2, 0))
      self.obj577.out_connections_.append(self.obj575)
      self.obj575.in_connections_.append(self.obj577)
      self.obj577.graphObject_.pendingConnections.append((self.obj577.graphObject_.tag, self.obj575.graphObject_.tag, [171.0, 163.0, 78.5, 145.75], 2, 0))
      self.obj578.out_connections_.append(self.obj576)
      self.obj576.in_connections_.append(self.obj578)
      self.obj578.graphObject_.pendingConnections.append((self.obj578.graphObject_.tag, self.obj576.graphObject_.tag, [411.0, 180.0, 295.25, 111.25], 2, 0))
      self.obj579.out_connections_.append(self.obj575)
      self.obj575.in_connections_.append(self.obj579)
      self.obj579.graphObject_.pendingConnections.append((self.obj579.graphObject_.tag, self.obj575.graphObject_.tag, [171.0, 163.0, 291.0, 171.5], 2, 0))

   def condition(self, graphID, isograph, atom3i):
      agent = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      role  = self.getMatched(graphID, self.LHS.nodeWithLabel(2))
      link = self.getMatched(graphID, self.LHS.nodeWithLabel(5)) 
      
      return not ( hasattr(link,  "rule1"+agent.name.getValue()+role.name.getValue() ))
      
      

   def action(self, graphID, isograph, atom3i):
      linkk = self.getMatched(graphID, self.LHS.nodeWithLabel(5)) 
      c1 = self.getMatched(graphID, self.LHS.nodeWithLabel(3)) 
      a = self.getMatched(graphID, self.LHS.nodeWithLabel(1)) 
      r = self.getMatched(graphID, self.LHS.nodeWithLabel(2)) 
      link = self.getMatched(graphID, self.LHS.nodeWithLabel(4))
      
      setattr( linkk ,  "rule1"+a.name.getValue()+r.name.getValue() , True )
      
      print "Collect 1 "+a.name.getValue()+" "+r.name.getValue()+" "+str(link.rate.getValue())+c1.name.getValue()
      if not ( "nb"+r.name.getValue() in  self.graphRewritingSystem.Dictag[a.name.getValue()].keys() ):
       self.graphRewritingSystem.Dictag[a.name.getValue()]["nb"+r.name.getValue()]=0
      
      self.graphRewritingSystem.Dictag[a.name.getValue()]["nb"+r.name.getValue()] += 1
      self.graphRewritingSystem.Dictag[a.name.getValue()][r.name.getValue()] += link.rate.getValue()
      self.graphRewritingSystem.Dictag[a.name.getValue()][c1.name.getValue()] = link.rate.getValue()
      print "Collect inf 1 "+str( self.graphRewritingSystem.Dictag )
      
      

