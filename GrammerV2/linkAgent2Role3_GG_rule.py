# _ linkAgent2Role3_GG_rule.py ____________________________________________________________________________
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
class linkAgent2Role3_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 3)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_omacss(parent)

      self.obj974=Agent(parent)
      self.obj974.preAction( self.LHS.CREATE )
      self.obj974.isGraphObjectVisual = True

      if(hasattr(self.obj974, '_setHierarchicalLink')):
        self.obj974._setHierarchicalLink(False)

      # price
      self.obj974.price.setValue(0)

      # name
      self.obj974.name.setValue('')
      self.obj974.name.setNone()

      self.obj974.GGLabel.setValue(1)
      self.obj974.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(40.0,40.0,self.obj974)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj974.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj974)
      self.obj974.postAction( self.LHS.CREATE )

      self.obj975=Capabilitie(parent)
      self.obj975.preAction( self.LHS.CREATE )
      self.obj975.isGraphObjectVisual = True

      if(hasattr(self.obj975, '_setHierarchicalLink')):
        self.obj975._setHierarchicalLink(False)

      # name
      self.obj975.name.setValue('')
      self.obj975.name.setNone()

      self.obj975.GGLabel.setValue(3)
      self.obj975.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(300.0,20.0,self.obj975)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj975.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj975)
      self.obj975.postAction( self.LHS.CREATE )

      self.obj976=Capabilitie(parent)
      self.obj976.preAction( self.LHS.CREATE )
      self.obj976.isGraphObjectVisual = True

      if(hasattr(self.obj976, '_setHierarchicalLink')):
        self.obj976._setHierarchicalLink(False)

      # name
      self.obj976.name.setValue('')
      self.obj976.name.setNone()

      self.obj976.GGLabel.setValue(4)
      self.obj976.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(100.0,160.0,self.obj976)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj976.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj976)
      self.obj976.postAction( self.LHS.CREATE )

      self.obj977=Role(parent)
      self.obj977.preAction( self.LHS.CREATE )
      self.obj977.isGraphObjectVisual = True

      if(hasattr(self.obj977, '_setHierarchicalLink')):
        self.obj977._setHierarchicalLink(False)

      # name
      self.obj977.name.setValue('')
      self.obj977.name.setNone()

      self.obj977.GGLabel.setValue(2)
      self.obj977.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(300.0,120.0,self.obj977)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj977.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj977)
      self.obj977.postAction( self.LHS.CREATE )

      self.obj978=posses(parent)
      self.obj978.preAction( self.LHS.CREATE )
      self.obj978.isGraphObjectVisual = True

      if(hasattr(self.obj978, '_setHierarchicalLink')):
        self.obj978._setHierarchicalLink(False)

      # rate
      self.obj978.rate.setValue(0.0)

      self.obj978.GGLabel.setValue(5)
      self.obj978.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(93.0,130.5,self.obj978)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj978.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj978)
      self.obj978.postAction( self.LHS.CREATE )

      self.obj979=CapableOf(parent)
      self.obj979.preAction( self.LHS.CREATE )
      self.obj979.isGraphObjectVisual = True

      if(hasattr(self.obj979, '_setHierarchicalLink')):
        self.obj979._setHierarchicalLink(False)

      self.obj979.GGLabel.setValue(6)
      self.obj979.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(194.5,111.5,self.obj979)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj979.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj979)
      self.obj979.postAction( self.LHS.CREATE )

      self.obj980=requir(parent)
      self.obj980.preAction( self.LHS.CREATE )
      self.obj980.isGraphObjectVisual = True

      if(hasattr(self.obj980, '_setHierarchicalLink')):
        self.obj980._setHierarchicalLink(False)

      self.obj980.GGLabel.setValue(7)
      self.obj980.graphClass_= graph_requir
      if parent.genGraphics:
         new_obj = graph_requir(222.5,162.5,self.obj980)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj980.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj980)
      self.obj980.postAction( self.LHS.CREATE )

      self.obj981=requir(parent)
      self.obj981.preAction( self.LHS.CREATE )
      self.obj981.isGraphObjectVisual = True

      if(hasattr(self.obj981, '_setHierarchicalLink')):
        self.obj981._setHierarchicalLink(False)

      self.obj981.GGLabel.setValue(8)
      self.obj981.graphClass_= graph_requir
      if parent.genGraphics:
         new_obj = graph_requir(322.5,90.0,self.obj981)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj981.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj981)
      self.obj981.postAction( self.LHS.CREATE )

      self.obj974.out_connections_.append(self.obj978)
      self.obj978.in_connections_.append(self.obj974)
      self.obj974.graphObject_.pendingConnections.append((self.obj974.graphObject_.tag, self.obj978.graphObject_.tag, [77.0, 102.0, 93.0, 130.5], 2, 0))
      self.obj974.out_connections_.append(self.obj979)
      self.obj979.in_connections_.append(self.obj974)
      self.obj974.graphObject_.pendingConnections.append((self.obj974.graphObject_.tag, self.obj979.graphObject_.tag, [65.0, 102.0, 194.5, 111.5], 0, True))
      self.obj977.out_connections_.append(self.obj980)
      self.obj980.in_connections_.append(self.obj977)
      self.obj977.graphObject_.pendingConnections.append((self.obj977.graphObject_.tag, self.obj980.graphObject_.tag, [324.0, 166.0, 222.5, 162.5], 0, True))
      self.obj977.out_connections_.append(self.obj981)
      self.obj981.in_connections_.append(self.obj977)
      self.obj977.graphObject_.pendingConnections.append((self.obj977.graphObject_.tag, self.obj981.graphObject_.tag, [324.0, 121.0, 322.5, 90.0], 0, True))
      self.obj978.out_connections_.append(self.obj976)
      self.obj976.in_connections_.append(self.obj978)
      self.obj978.graphObject_.pendingConnections.append((self.obj978.graphObject_.tag, self.obj976.graphObject_.tag, [121.0, 159.0, 93.0, 130.5], 0, True))
      self.obj979.out_connections_.append(self.obj977)
      self.obj977.in_connections_.append(self.obj979)
      self.obj979.graphObject_.pendingConnections.append((self.obj979.graphObject_.tag, self.obj977.graphObject_.tag, [331.0, 120.0, 194.5, 111.5], 2, 0))
      self.obj980.out_connections_.append(self.obj976)
      self.obj976.in_connections_.append(self.obj980)
      self.obj980.graphObject_.pendingConnections.append((self.obj980.graphObject_.tag, self.obj976.graphObject_.tag, [121.0, 159.0, 222.5, 162.5], 0, True))
      self.obj981.out_connections_.append(self.obj975)
      self.obj975.in_connections_.append(self.obj981)
      self.obj981.graphObject_.pendingConnections.append((self.obj981.graphObject_.tag, self.obj975.graphObject_.tag, [321.0, 59.0, 322.5, 90.0], 0, True))

      self.RHS = ASG_omacss(parent)

      self.obj983=Agent(parent)
      self.obj983.preAction( self.RHS.CREATE )
      self.obj983.isGraphObjectVisual = True

      if(hasattr(self.obj983, '_setHierarchicalLink')):
        self.obj983._setHierarchicalLink(False)

      # price
      self.obj983.price.setValue(0)

      # name
      self.obj983.name.setValue('')
      self.obj983.name.setNone()

      self.obj983.GGLabel.setValue(1)
      self.obj983.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(40.0,40.0,self.obj983)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj983.graphObject_ = new_obj
      self.obj9830= AttrCalc()
      self.obj9830.Copy=ATOM3Boolean()
      self.obj9830.Copy.setValue(('Copy from LHS', 1))
      self.obj9830.Copy.config = 0
      self.obj9830.Specify=ATOM3Constraint()
      self.obj9830.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj983.GGset2Any['price']= self.obj9830
      self.obj9831= AttrCalc()
      self.obj9831.Copy=ATOM3Boolean()
      self.obj9831.Copy.setValue(('Copy from LHS', 1))
      self.obj9831.Copy.config = 0
      self.obj9831.Specify=ATOM3Constraint()
      self.obj9831.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj983.GGset2Any['name']= self.obj9831

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj983)
      self.obj983.postAction( self.RHS.CREATE )

      self.obj984=Capabilitie(parent)
      self.obj984.preAction( self.RHS.CREATE )
      self.obj984.isGraphObjectVisual = True

      if(hasattr(self.obj984, '_setHierarchicalLink')):
        self.obj984._setHierarchicalLink(False)

      # name
      self.obj984.name.setValue('')
      self.obj984.name.setNone()

      self.obj984.GGLabel.setValue(3)
      self.obj984.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(300.0,20.0,self.obj984)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj984.graphObject_ = new_obj
      self.obj9840= AttrCalc()
      self.obj9840.Copy=ATOM3Boolean()
      self.obj9840.Copy.setValue(('Copy from LHS', 1))
      self.obj9840.Copy.config = 0
      self.obj9840.Specify=ATOM3Constraint()
      self.obj9840.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj984.GGset2Any['name']= self.obj9840

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj984)
      self.obj984.postAction( self.RHS.CREATE )

      self.obj985=Capabilitie(parent)
      self.obj985.preAction( self.RHS.CREATE )
      self.obj985.isGraphObjectVisual = True

      if(hasattr(self.obj985, '_setHierarchicalLink')):
        self.obj985._setHierarchicalLink(False)

      # name
      self.obj985.name.setValue('')
      self.obj985.name.setNone()

      self.obj985.GGLabel.setValue(4)
      self.obj985.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(100.0,160.0,self.obj985)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj985.graphObject_ = new_obj
      self.obj9850= AttrCalc()
      self.obj9850.Copy=ATOM3Boolean()
      self.obj9850.Copy.setValue(('Copy from LHS', 1))
      self.obj9850.Copy.config = 0
      self.obj9850.Specify=ATOM3Constraint()
      self.obj9850.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj985.GGset2Any['name']= self.obj9850

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj985)
      self.obj985.postAction( self.RHS.CREATE )

      self.obj986=Role(parent)
      self.obj986.preAction( self.RHS.CREATE )
      self.obj986.isGraphObjectVisual = True

      if(hasattr(self.obj986, '_setHierarchicalLink')):
        self.obj986._setHierarchicalLink(False)

      # name
      self.obj986.name.setValue('')
      self.obj986.name.setNone()

      self.obj986.GGLabel.setValue(2)
      self.obj986.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(300.0,120.0,self.obj986)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj986.graphObject_ = new_obj
      self.obj9860= AttrCalc()
      self.obj9860.Copy=ATOM3Boolean()
      self.obj9860.Copy.setValue(('Copy from LHS', 1))
      self.obj9860.Copy.config = 0
      self.obj9860.Specify=ATOM3Constraint()
      self.obj9860.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj986.GGset2Any['name']= self.obj9860

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj986)
      self.obj986.postAction( self.RHS.CREATE )

      self.obj987=posses(parent)
      self.obj987.preAction( self.RHS.CREATE )
      self.obj987.isGraphObjectVisual = True

      if(hasattr(self.obj987, '_setHierarchicalLink')):
        self.obj987._setHierarchicalLink(False)

      # rate
      self.obj987.rate.setValue(0.0)

      self.obj987.GGLabel.setValue(5)
      self.obj987.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(93.0,130.5,self.obj987)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj987.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj987)
      self.obj987.postAction( self.RHS.CREATE )

      self.obj988=requir(parent)
      self.obj988.preAction( self.RHS.CREATE )
      self.obj988.isGraphObjectVisual = True

      if(hasattr(self.obj988, '_setHierarchicalLink')):
        self.obj988._setHierarchicalLink(False)

      self.obj988.GGLabel.setValue(7)
      self.obj988.graphClass_= graph_requir
      if parent.genGraphics:
         new_obj = graph_requir(222.5,162.5,self.obj988)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj988.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj988)
      self.obj988.postAction( self.RHS.CREATE )

      self.obj989=requir(parent)
      self.obj989.preAction( self.RHS.CREATE )
      self.obj989.isGraphObjectVisual = True

      if(hasattr(self.obj989, '_setHierarchicalLink')):
        self.obj989._setHierarchicalLink(False)

      self.obj989.GGLabel.setValue(8)
      self.obj989.graphClass_= graph_requir
      if parent.genGraphics:
         new_obj = graph_requir(322.5,90.0,self.obj989)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj989.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj989)
      self.obj989.postAction( self.RHS.CREATE )

      self.obj983.out_connections_.append(self.obj987)
      self.obj987.in_connections_.append(self.obj983)
      self.obj983.graphObject_.pendingConnections.append((self.obj983.graphObject_.tag, self.obj987.graphObject_.tag, [77.0, 102.0, 93.0, 130.5], 2, 0))
      self.obj986.out_connections_.append(self.obj988)
      self.obj988.in_connections_.append(self.obj986)
      self.obj986.graphObject_.pendingConnections.append((self.obj986.graphObject_.tag, self.obj988.graphObject_.tag, [331.0, 165.0, 222.5, 162.5], 2, 0))
      self.obj986.out_connections_.append(self.obj989)
      self.obj989.in_connections_.append(self.obj986)
      self.obj986.graphObject_.pendingConnections.append((self.obj986.graphObject_.tag, self.obj989.graphObject_.tag, [331.0, 120.0, 322.5, 90.0], 2, 0))
      self.obj987.out_connections_.append(self.obj985)
      self.obj985.in_connections_.append(self.obj987)
      self.obj987.graphObject_.pendingConnections.append((self.obj987.graphObject_.tag, self.obj985.graphObject_.tag, [131.0, 163.0, 93.0, 130.5], 2, 0))
      self.obj988.out_connections_.append(self.obj985)
      self.obj985.in_connections_.append(self.obj988)
      self.obj988.graphObject_.pendingConnections.append((self.obj988.graphObject_.tag, self.obj985.graphObject_.tag, [131.0, 163.0, 222.5, 162.5], 2, 0))
      self.obj989.out_connections_.append(self.obj984)
      self.obj984.in_connections_.append(self.obj989)
      self.obj989.graphObject_.pendingConnections.append((self.obj989.graphObject_.tag, self.obj984.graphObject_.tag, [331.0, 63.0, 322.5, 90.0], 2, 0))

   def condition(self, graphID, isograph, atom3i):
      agent = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      role  = self.getMatched(graphID, self.LHS.nodeWithLabel(2))
      c1 = self.getMatched(graphID, self.LHS.nodeWithLabel(3))
      c2 = self.getMatched(graphID, self.LHS.nodeWithLabel(4))
      
      return not ( hasattr(c1,  agent.name.getValue() ) and 
      hasattr(c1,  role.name.getValue() ) and
      hasattr(c2,  agent.name.getValue() ) and  hasattr(c2, role.name.getValue() ) )
      
      

   def action(self, graphID, isograph, atom3i):
      agent = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      c1 = self.getMatched(graphID, self.LHS.nodeWithLabel(4))
      c2 = self.getMatched(graphID, self.LHS.nodeWithLabel(3))
      role = self.getMatched(graphID, self.LHS.nodeWithLabel(2))
      
      setattr( c1 ,  agent.name.getValue() , True )
      setattr( c1 ,  role.name.getValue() , True )
      
      setattr( c2 ,  agent.name.getValue() , True )
      setattr( c2 ,  role.name.getValue() , True )
      print' Eli : ('+agent.name.getValue()+','+c1.name.getValue()+','+c2.name.getValue()+','+role.name.getValue()+')'
      
      

