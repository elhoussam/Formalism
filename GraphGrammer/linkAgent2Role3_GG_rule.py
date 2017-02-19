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

      self.obj177=Agent(parent)
      self.obj177.preAction( self.LHS.CREATE )
      self.obj177.isGraphObjectVisual = True

      if(hasattr(self.obj177, '_setHierarchicalLink')):
        self.obj177._setHierarchicalLink(False)

      # price
      self.obj177.price.setValue(0)

      # name
      self.obj177.name.setValue('')
      self.obj177.name.setNone()

      self.obj177.GGLabel.setValue(1)
      self.obj177.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(40.0,40.0,self.obj177)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj177.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj177)
      self.obj177.postAction( self.LHS.CREATE )

      self.obj178=Capabilitie(parent)
      self.obj178.preAction( self.LHS.CREATE )
      self.obj178.isGraphObjectVisual = True

      if(hasattr(self.obj178, '_setHierarchicalLink')):
        self.obj178._setHierarchicalLink(False)

      # name
      self.obj178.name.setValue('')
      self.obj178.name.setNone()

      self.obj178.GGLabel.setValue(3)
      self.obj178.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(300.0,20.0,self.obj178)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj178.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj178)
      self.obj178.postAction( self.LHS.CREATE )

      self.obj179=Capabilitie(parent)
      self.obj179.preAction( self.LHS.CREATE )
      self.obj179.isGraphObjectVisual = True

      if(hasattr(self.obj179, '_setHierarchicalLink')):
        self.obj179._setHierarchicalLink(False)

      # name
      self.obj179.name.setValue('')
      self.obj179.name.setNone()

      self.obj179.GGLabel.setValue(4)
      self.obj179.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(100.0,160.0,self.obj179)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj179.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj179)
      self.obj179.postAction( self.LHS.CREATE )

      self.obj180=Role(parent)
      self.obj180.preAction( self.LHS.CREATE )
      self.obj180.isGraphObjectVisual = True

      if(hasattr(self.obj180, '_setHierarchicalLink')):
        self.obj180._setHierarchicalLink(False)

      # name
      self.obj180.name.setValue('')
      self.obj180.name.setNone()

      self.obj180.GGLabel.setValue(2)
      self.obj180.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(300.0,120.0,self.obj180)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj180.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj180)
      self.obj180.postAction( self.LHS.CREATE )

      self.obj181=posses(parent)
      self.obj181.preAction( self.LHS.CREATE )
      self.obj181.isGraphObjectVisual = True

      if(hasattr(self.obj181, '_setHierarchicalLink')):
        self.obj181._setHierarchicalLink(False)

      # rate
      self.obj181.rate.setNone()

      self.obj181.GGLabel.setValue(5)
      self.obj181.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(93.0,130.5,self.obj181)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj181.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj181)
      self.obj181.postAction( self.LHS.CREATE )

      self.obj182=CapableOf(parent)
      self.obj182.preAction( self.LHS.CREATE )
      self.obj182.isGraphObjectVisual = True

      if(hasattr(self.obj182, '_setHierarchicalLink')):
        self.obj182._setHierarchicalLink(False)

      self.obj182.GGLabel.setValue(6)
      self.obj182.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(194.5,111.5,self.obj182)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj182.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj182)
      self.obj182.postAction( self.LHS.CREATE )

      self.obj183=requir(parent)
      self.obj183.preAction( self.LHS.CREATE )
      self.obj183.isGraphObjectVisual = True

      if(hasattr(self.obj183, '_setHierarchicalLink')):
        self.obj183._setHierarchicalLink(False)

      self.obj183.GGLabel.setValue(7)
      self.obj183.graphClass_= graph_requir
      if parent.genGraphics:
         new_obj = graph_requir(222.5,162.5,self.obj183)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj183.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj183)
      self.obj183.postAction( self.LHS.CREATE )

      self.obj184=requir(parent)
      self.obj184.preAction( self.LHS.CREATE )
      self.obj184.isGraphObjectVisual = True

      if(hasattr(self.obj184, '_setHierarchicalLink')):
        self.obj184._setHierarchicalLink(False)

      self.obj184.GGLabel.setValue(8)
      self.obj184.graphClass_= graph_requir
      if parent.genGraphics:
         new_obj = graph_requir(322.5,90.0,self.obj184)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj184.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj184)
      self.obj184.postAction( self.LHS.CREATE )

      self.obj177.out_connections_.append(self.obj181)
      self.obj181.in_connections_.append(self.obj177)
      self.obj177.graphObject_.pendingConnections.append((self.obj177.graphObject_.tag, self.obj181.graphObject_.tag, [77.0, 102.0, 93.0, 130.5], 2, 0))
      self.obj177.out_connections_.append(self.obj182)
      self.obj182.in_connections_.append(self.obj177)
      self.obj177.graphObject_.pendingConnections.append((self.obj177.graphObject_.tag, self.obj182.graphObject_.tag, [65.0, 102.0, 194.5, 111.5], 0, True))
      self.obj180.out_connections_.append(self.obj183)
      self.obj183.in_connections_.append(self.obj180)
      self.obj180.graphObject_.pendingConnections.append((self.obj180.graphObject_.tag, self.obj183.graphObject_.tag, [324.0, 166.0, 222.5, 162.5], 0, True))
      self.obj180.out_connections_.append(self.obj184)
      self.obj184.in_connections_.append(self.obj180)
      self.obj180.graphObject_.pendingConnections.append((self.obj180.graphObject_.tag, self.obj184.graphObject_.tag, [324.0, 121.0, 322.5, 90.0], 0, True))
      self.obj181.out_connections_.append(self.obj179)
      self.obj179.in_connections_.append(self.obj181)
      self.obj181.graphObject_.pendingConnections.append((self.obj181.graphObject_.tag, self.obj179.graphObject_.tag, [121.0, 159.0, 93.0, 130.5], 0, True))
      self.obj182.out_connections_.append(self.obj180)
      self.obj180.in_connections_.append(self.obj182)
      self.obj182.graphObject_.pendingConnections.append((self.obj182.graphObject_.tag, self.obj180.graphObject_.tag, [331.0, 120.0, 194.5, 111.5], 2, 0))
      self.obj183.out_connections_.append(self.obj179)
      self.obj179.in_connections_.append(self.obj183)
      self.obj183.graphObject_.pendingConnections.append((self.obj183.graphObject_.tag, self.obj179.graphObject_.tag, [121.0, 159.0, 222.5, 162.5], 0, True))
      self.obj184.out_connections_.append(self.obj178)
      self.obj178.in_connections_.append(self.obj184)
      self.obj184.graphObject_.pendingConnections.append((self.obj184.graphObject_.tag, self.obj178.graphObject_.tag, [321.0, 59.0, 322.5, 90.0], 0, True))

      self.RHS = ASG_omacss(parent)

      self.obj186=Agent(parent)
      self.obj186.preAction( self.RHS.CREATE )
      self.obj186.isGraphObjectVisual = True

      if(hasattr(self.obj186, '_setHierarchicalLink')):
        self.obj186._setHierarchicalLink(False)

      # price
      self.obj186.price.setValue(0)

      # name
      self.obj186.name.setValue('')
      self.obj186.name.setNone()

      self.obj186.GGLabel.setValue(1)
      self.obj186.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(40.0,40.0,self.obj186)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj186.graphObject_ = new_obj
      self.obj1860= AttrCalc()
      self.obj1860.Copy=ATOM3Boolean()
      self.obj1860.Copy.setValue(('Copy from LHS', 1))
      self.obj1860.Copy.config = 0
      self.obj1860.Specify=ATOM3Constraint()
      self.obj1860.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj186.GGset2Any['price']= self.obj1860
      self.obj1861= AttrCalc()
      self.obj1861.Copy=ATOM3Boolean()
      self.obj1861.Copy.setValue(('Copy from LHS', 1))
      self.obj1861.Copy.config = 0
      self.obj1861.Specify=ATOM3Constraint()
      self.obj1861.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj186.GGset2Any['name']= self.obj1861

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj186)
      self.obj186.postAction( self.RHS.CREATE )

      self.obj187=Capabilitie(parent)
      self.obj187.preAction( self.RHS.CREATE )
      self.obj187.isGraphObjectVisual = True

      if(hasattr(self.obj187, '_setHierarchicalLink')):
        self.obj187._setHierarchicalLink(False)

      # name
      self.obj187.name.setValue('')
      self.obj187.name.setNone()

      self.obj187.GGLabel.setValue(3)
      self.obj187.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(300.0,20.0,self.obj187)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj187.graphObject_ = new_obj
      self.obj1870= AttrCalc()
      self.obj1870.Copy=ATOM3Boolean()
      self.obj1870.Copy.setValue(('Copy from LHS', 1))
      self.obj1870.Copy.config = 0
      self.obj1870.Specify=ATOM3Constraint()
      self.obj1870.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj187.GGset2Any['name']= self.obj1870

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj187)
      self.obj187.postAction( self.RHS.CREATE )

      self.obj188=Capabilitie(parent)
      self.obj188.preAction( self.RHS.CREATE )
      self.obj188.isGraphObjectVisual = True

      if(hasattr(self.obj188, '_setHierarchicalLink')):
        self.obj188._setHierarchicalLink(False)

      # name
      self.obj188.name.setValue('')
      self.obj188.name.setNone()

      self.obj188.GGLabel.setValue(4)
      self.obj188.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(100.0,160.0,self.obj188)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj188.graphObject_ = new_obj
      self.obj1880= AttrCalc()
      self.obj1880.Copy=ATOM3Boolean()
      self.obj1880.Copy.setValue(('Copy from LHS', 1))
      self.obj1880.Copy.config = 0
      self.obj1880.Specify=ATOM3Constraint()
      self.obj1880.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj188.GGset2Any['name']= self.obj1880

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj188)
      self.obj188.postAction( self.RHS.CREATE )

      self.obj189=Role(parent)
      self.obj189.preAction( self.RHS.CREATE )
      self.obj189.isGraphObjectVisual = True

      if(hasattr(self.obj189, '_setHierarchicalLink')):
        self.obj189._setHierarchicalLink(False)

      # name
      self.obj189.name.setValue('')
      self.obj189.name.setNone()

      self.obj189.GGLabel.setValue(2)
      self.obj189.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(300.0,120.0,self.obj189)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj189.graphObject_ = new_obj
      self.obj1890= AttrCalc()
      self.obj1890.Copy=ATOM3Boolean()
      self.obj1890.Copy.setValue(('Copy from LHS', 1))
      self.obj1890.Copy.config = 0
      self.obj1890.Specify=ATOM3Constraint()
      self.obj1890.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj189.GGset2Any['name']= self.obj1890

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj189)
      self.obj189.postAction( self.RHS.CREATE )

      self.obj190=posses(parent)
      self.obj190.preAction( self.RHS.CREATE )
      self.obj190.isGraphObjectVisual = True

      if(hasattr(self.obj190, '_setHierarchicalLink')):
        self.obj190._setHierarchicalLink(False)

      # rate
      self.obj190.rate.setValue(0.0)

      self.obj190.GGLabel.setValue(5)
      self.obj190.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(93.0,130.5,self.obj190)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj190.graphObject_ = new_obj
      self.obj1900= AttrCalc()
      self.obj1900.Copy=ATOM3Boolean()
      self.obj1900.Copy.setValue(('Copy from LHS', 1))
      self.obj1900.Copy.config = 0
      self.obj1900.Specify=ATOM3Constraint()
      self.obj1900.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj190.GGset2Any['rate']= self.obj1900

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj190)
      self.obj190.postAction( self.RHS.CREATE )

      self.obj191=requir(parent)
      self.obj191.preAction( self.RHS.CREATE )
      self.obj191.isGraphObjectVisual = True

      if(hasattr(self.obj191, '_setHierarchicalLink')):
        self.obj191._setHierarchicalLink(False)

      self.obj191.GGLabel.setValue(7)
      self.obj191.graphClass_= graph_requir
      if parent.genGraphics:
         new_obj = graph_requir(222.5,162.5,self.obj191)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj191.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj191)
      self.obj191.postAction( self.RHS.CREATE )

      self.obj192=requir(parent)
      self.obj192.preAction( self.RHS.CREATE )
      self.obj192.isGraphObjectVisual = True

      if(hasattr(self.obj192, '_setHierarchicalLink')):
        self.obj192._setHierarchicalLink(False)

      self.obj192.GGLabel.setValue(8)
      self.obj192.graphClass_= graph_requir
      if parent.genGraphics:
         new_obj = graph_requir(322.5,90.0,self.obj192)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj192.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj192)
      self.obj192.postAction( self.RHS.CREATE )

      self.obj186.out_connections_.append(self.obj190)
      self.obj190.in_connections_.append(self.obj186)
      self.obj186.graphObject_.pendingConnections.append((self.obj186.graphObject_.tag, self.obj190.graphObject_.tag, [77.0, 102.0, 93.0, 130.5], 2, 0))
      self.obj189.out_connections_.append(self.obj191)
      self.obj191.in_connections_.append(self.obj189)
      self.obj189.graphObject_.pendingConnections.append((self.obj189.graphObject_.tag, self.obj191.graphObject_.tag, [331.0, 165.0, 222.5, 162.5], 2, 0))
      self.obj189.out_connections_.append(self.obj192)
      self.obj192.in_connections_.append(self.obj189)
      self.obj189.graphObject_.pendingConnections.append((self.obj189.graphObject_.tag, self.obj192.graphObject_.tag, [331.0, 120.0, 322.5, 90.0], 2, 0))
      self.obj190.out_connections_.append(self.obj188)
      self.obj188.in_connections_.append(self.obj190)
      self.obj190.graphObject_.pendingConnections.append((self.obj190.graphObject_.tag, self.obj188.graphObject_.tag, [131.0, 163.0, 93.0, 130.5], 2, 0))
      self.obj191.out_connections_.append(self.obj188)
      self.obj188.in_connections_.append(self.obj191)
      self.obj191.graphObject_.pendingConnections.append((self.obj191.graphObject_.tag, self.obj188.graphObject_.tag, [131.0, 163.0, 222.5, 162.5], 2, 0))
      self.obj192.out_connections_.append(self.obj187)
      self.obj187.in_connections_.append(self.obj192)
      self.obj192.graphObject_.pendingConnections.append((self.obj192.graphObject_.tag, self.obj187.graphObject_.tag, [331.0, 63.0, 322.5, 90.0], 2, 0))

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
      
      

