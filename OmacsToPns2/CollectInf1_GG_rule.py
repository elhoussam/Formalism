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

      self.obj1568=Agent(parent)
      self.obj1568.preAction( self.LHS.CREATE )
      self.obj1568.isGraphObjectVisual = True

      if(hasattr(self.obj1568, '_setHierarchicalLink')):
        self.obj1568._setHierarchicalLink(False)

      # price
      self.obj1568.price.setNone()

      # name
      self.obj1568.name.setValue('')
      self.obj1568.name.setNone()

      self.obj1568.GGLabel.setValue(1)
      self.obj1568.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(20.0,20.0,self.obj1568)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1568.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1568)
      self.obj1568.postAction( self.LHS.CREATE )

      self.obj1569=Capabilitie(parent)
      self.obj1569.preAction( self.LHS.CREATE )
      self.obj1569.isGraphObjectVisual = True

      if(hasattr(self.obj1569, '_setHierarchicalLink')):
        self.obj1569._setHierarchicalLink(False)

      # name
      self.obj1569.name.setValue('')
      self.obj1569.name.setNone()

      self.obj1569.GGLabel.setValue(3)
      self.obj1569.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(140.0,160.0,self.obj1569)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1569.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1569)
      self.obj1569.postAction( self.LHS.CREATE )

      self.obj1570=Role(parent)
      self.obj1570.preAction( self.LHS.CREATE )
      self.obj1570.isGraphObjectVisual = True

      if(hasattr(self.obj1570, '_setHierarchicalLink')):
        self.obj1570._setHierarchicalLink(False)

      # name
      self.obj1570.name.setValue('')
      self.obj1570.name.setNone()

      self.obj1570.GGLabel.setValue(2)
      self.obj1570.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(380.0,180.0,self.obj1570)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1570.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1570)
      self.obj1570.postAction( self.LHS.CREATE )

      self.obj1571=posses(parent)
      self.obj1571.preAction( self.LHS.CREATE )
      self.obj1571.isGraphObjectVisual = True

      if(hasattr(self.obj1571, '_setHierarchicalLink')):
        self.obj1571._setHierarchicalLink(False)

      # rate
      self.obj1571.rate.setNone()

      self.obj1571.GGLabel.setValue(4)
      self.obj1571.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(78.5,145.75,self.obj1571)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1571.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1571)
      self.obj1571.postAction( self.LHS.CREATE )

      self.obj1572=CapableOf(parent)
      self.obj1572.preAction( self.LHS.CREATE )
      self.obj1572.isGraphObjectVisual = True

      if(hasattr(self.obj1572, '_setHierarchicalLink')):
        self.obj1572._setHierarchicalLink(False)

      # rate
      self.obj1572.rate.setNone()

      self.obj1572.GGLabel.setValue(6)
      self.obj1572.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(295.25,111.25,self.obj1572)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1572.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1572)
      self.obj1572.postAction( self.LHS.CREATE )

      self.obj1573=require(parent)
      self.obj1573.preAction( self.LHS.CREATE )
      self.obj1573.isGraphObjectVisual = True

      if(hasattr(self.obj1573, '_setHierarchicalLink')):
        self.obj1573._setHierarchicalLink(False)

      self.obj1573.GGLabel.setValue(5)
      self.obj1573.graphClass_= graph_require
      if parent.genGraphics:
         new_obj = graph_require(291.0,171.5,self.obj1573)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1573.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1573)
      self.obj1573.postAction( self.LHS.CREATE )

      self.obj1568.out_connections_.append(self.obj1571)
      self.obj1571.in_connections_.append(self.obj1568)
      self.obj1568.graphObject_.pendingConnections.append((self.obj1568.graphObject_.tag, self.obj1571.graphObject_.tag, [45.0, 82.0, 49.5, 126.5, 78.5, 145.75], 2, True))
      self.obj1568.out_connections_.append(self.obj1572)
      self.obj1572.in_connections_.append(self.obj1568)
      self.obj1568.graphObject_.pendingConnections.append((self.obj1568.graphObject_.tag, self.obj1572.graphObject_.tag, [45.0, 82.0, 205.5, 86.5, 295.25, 111.25], 2, True))
      self.obj1570.out_connections_.append(self.obj1573)
      self.obj1573.in_connections_.append(self.obj1570)
      self.obj1570.graphObject_.pendingConnections.append((self.obj1570.graphObject_.tag, self.obj1573.graphObject_.tag, [404.0, 181.0, 374.0, 146.0, 291.0, 171.5], 2, True))
      self.obj1571.out_connections_.append(self.obj1569)
      self.obj1569.in_connections_.append(self.obj1571)
      self.obj1571.graphObject_.pendingConnections.append((self.obj1571.graphObject_.tag, self.obj1569.graphObject_.tag, [161.0, 159.0, 107.5, 165.0, 78.5, 145.75], 2, True))
      self.obj1572.out_connections_.append(self.obj1570)
      self.obj1570.in_connections_.append(self.obj1572)
      self.obj1572.graphObject_.pendingConnections.append((self.obj1572.graphObject_.tag, self.obj1570.graphObject_.tag, [404.0, 181.0, 385.0, 136.0, 295.25, 111.25], 2, True))
      self.obj1573.out_connections_.append(self.obj1569)
      self.obj1569.in_connections_.append(self.obj1573)
      self.obj1573.graphObject_.pendingConnections.append((self.obj1573.graphObject_.tag, self.obj1569.graphObject_.tag, [161.0, 199.0, 208.0, 197.0, 291.0, 171.5], 2, True))

      self.RHS = ASG_omacs(parent)

      self.obj1575=Agent(parent)
      self.obj1575.preAction( self.RHS.CREATE )
      self.obj1575.isGraphObjectVisual = True

      if(hasattr(self.obj1575, '_setHierarchicalLink')):
        self.obj1575._setHierarchicalLink(False)

      # price
      self.obj1575.price.setNone()

      # name
      self.obj1575.name.setValue('')
      self.obj1575.name.setNone()

      self.obj1575.GGLabel.setValue(1)
      self.obj1575.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(20.0,20.0,self.obj1575)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1575.graphObject_ = new_obj
      self.obj15750= AttrCalc()
      self.obj15750.Copy=ATOM3Boolean()
      self.obj15750.Copy.setValue(('Copy from LHS', 1))
      self.obj15750.Copy.config = 0
      self.obj15750.Specify=ATOM3Constraint()
      self.obj15750.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1575.GGset2Any['price']= self.obj15750
      self.obj15751= AttrCalc()
      self.obj15751.Copy=ATOM3Boolean()
      self.obj15751.Copy.setValue(('Copy from LHS', 1))
      self.obj15751.Copy.config = 0
      self.obj15751.Specify=ATOM3Constraint()
      self.obj15751.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1575.GGset2Any['name']= self.obj15751

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1575)
      self.obj1575.postAction( self.RHS.CREATE )

      self.obj1576=Capabilitie(parent)
      self.obj1576.preAction( self.RHS.CREATE )
      self.obj1576.isGraphObjectVisual = True

      if(hasattr(self.obj1576, '_setHierarchicalLink')):
        self.obj1576._setHierarchicalLink(False)

      # name
      self.obj1576.name.setValue('')
      self.obj1576.name.setNone()

      self.obj1576.GGLabel.setValue(3)
      self.obj1576.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(140.0,160.0,self.obj1576)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1576.graphObject_ = new_obj
      self.obj15760= AttrCalc()
      self.obj15760.Copy=ATOM3Boolean()
      self.obj15760.Copy.setValue(('Copy from LHS', 1))
      self.obj15760.Copy.config = 0
      self.obj15760.Specify=ATOM3Constraint()
      self.obj15760.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1576.GGset2Any['name']= self.obj15760

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1576)
      self.obj1576.postAction( self.RHS.CREATE )

      self.obj1577=Role(parent)
      self.obj1577.preAction( self.RHS.CREATE )
      self.obj1577.isGraphObjectVisual = True

      if(hasattr(self.obj1577, '_setHierarchicalLink')):
        self.obj1577._setHierarchicalLink(False)

      # name
      self.obj1577.name.setValue('')
      self.obj1577.name.setNone()

      self.obj1577.GGLabel.setValue(2)
      self.obj1577.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(380.0,180.0,self.obj1577)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1577.graphObject_ = new_obj
      self.obj15770= AttrCalc()
      self.obj15770.Copy=ATOM3Boolean()
      self.obj15770.Copy.setValue(('Copy from LHS', 1))
      self.obj15770.Copy.config = 0
      self.obj15770.Specify=ATOM3Constraint()
      self.obj15770.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1577.GGset2Any['name']= self.obj15770

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1577)
      self.obj1577.postAction( self.RHS.CREATE )

      self.obj1578=posses(parent)
      self.obj1578.preAction( self.RHS.CREATE )
      self.obj1578.isGraphObjectVisual = True

      if(hasattr(self.obj1578, '_setHierarchicalLink')):
        self.obj1578._setHierarchicalLink(False)

      # rate
      self.obj1578.rate.setNone()

      self.obj1578.GGLabel.setValue(4)
      self.obj1578.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(78.5,145.75,self.obj1578)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1578.graphObject_ = new_obj
      self.obj15780= AttrCalc()
      self.obj15780.Copy=ATOM3Boolean()
      self.obj15780.Copy.setValue(('Copy from LHS', 1))
      self.obj15780.Copy.config = 0
      self.obj15780.Specify=ATOM3Constraint()
      self.obj15780.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1578.GGset2Any['rate']= self.obj15780

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1578)
      self.obj1578.postAction( self.RHS.CREATE )

      self.obj1579=CapableOf(parent)
      self.obj1579.preAction( self.RHS.CREATE )
      self.obj1579.isGraphObjectVisual = True

      if(hasattr(self.obj1579, '_setHierarchicalLink')):
        self.obj1579._setHierarchicalLink(False)

      # rate
      self.obj1579.rate.setNone()

      self.obj1579.GGLabel.setValue(6)
      self.obj1579.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(295.25,111.25,self.obj1579)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1579.graphObject_ = new_obj
      self.obj15790= AttrCalc()
      self.obj15790.Copy=ATOM3Boolean()
      self.obj15790.Copy.setValue(('Copy from LHS', 1))
      self.obj15790.Copy.config = 0
      self.obj15790.Specify=ATOM3Constraint()
      self.obj15790.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1579.GGset2Any['rate']= self.obj15790

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1579)
      self.obj1579.postAction( self.RHS.CREATE )

      self.obj1580=require(parent)
      self.obj1580.preAction( self.RHS.CREATE )
      self.obj1580.isGraphObjectVisual = True

      if(hasattr(self.obj1580, '_setHierarchicalLink')):
        self.obj1580._setHierarchicalLink(False)

      self.obj1580.GGLabel.setValue(5)
      self.obj1580.graphClass_= graph_require
      if parent.genGraphics:
         new_obj = graph_require(291.0,171.5,self.obj1580)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1580.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1580)
      self.obj1580.postAction( self.RHS.CREATE )

      self.obj1575.out_connections_.append(self.obj1578)
      self.obj1578.in_connections_.append(self.obj1575)
      self.obj1575.graphObject_.pendingConnections.append((self.obj1575.graphObject_.tag, self.obj1578.graphObject_.tag, [57.0, 82.0, 78.5, 145.75], 2, 0))
      self.obj1575.out_connections_.append(self.obj1579)
      self.obj1579.in_connections_.append(self.obj1575)
      self.obj1575.graphObject_.pendingConnections.append((self.obj1575.graphObject_.tag, self.obj1579.graphObject_.tag, [57.0, 82.0, 295.25, 111.25], 2, 0))
      self.obj1577.out_connections_.append(self.obj1580)
      self.obj1580.in_connections_.append(self.obj1577)
      self.obj1577.graphObject_.pendingConnections.append((self.obj1577.graphObject_.tag, self.obj1580.graphObject_.tag, [411.0, 180.0, 291.0, 171.5], 2, 0))
      self.obj1578.out_connections_.append(self.obj1576)
      self.obj1576.in_connections_.append(self.obj1578)
      self.obj1578.graphObject_.pendingConnections.append((self.obj1578.graphObject_.tag, self.obj1576.graphObject_.tag, [171.0, 163.0, 78.5, 145.75], 2, 0))
      self.obj1579.out_connections_.append(self.obj1577)
      self.obj1577.in_connections_.append(self.obj1579)
      self.obj1579.graphObject_.pendingConnections.append((self.obj1579.graphObject_.tag, self.obj1577.graphObject_.tag, [411.0, 180.0, 295.25, 111.25], 2, 0))
      self.obj1580.out_connections_.append(self.obj1576)
      self.obj1576.in_connections_.append(self.obj1580)
      self.obj1580.graphObject_.pendingConnections.append((self.obj1580.graphObject_.tag, self.obj1576.graphObject_.tag, [171.0, 163.0, 291.0, 171.5], 2, 0))

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
      
      

