# _ linkAgent2Role2_GG_rule.py ____________________________________________________________________________
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
class linkAgent2Role2_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 2)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_omacss(parent)

      self.obj951=Agent(parent)
      self.obj951.preAction( self.LHS.CREATE )
      self.obj951.isGraphObjectVisual = True

      if(hasattr(self.obj951, '_setHierarchicalLink')):
        self.obj951._setHierarchicalLink(False)

      # price
      self.obj951.price.setValue(0)

      # name
      self.obj951.name.setValue('')
      self.obj951.name.setNone()

      self.obj951.GGLabel.setValue(1)
      self.obj951.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(60.0,20.0,self.obj951)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj951.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj951)
      self.obj951.postAction( self.LHS.CREATE )

      self.obj952=Capabilitie(parent)
      self.obj952.preAction( self.LHS.CREATE )
      self.obj952.isGraphObjectVisual = True

      if(hasattr(self.obj952, '_setHierarchicalLink')):
        self.obj952._setHierarchicalLink(False)

      # name
      self.obj952.name.setValue('')
      self.obj952.name.setNone()

      self.obj952.GGLabel.setValue(2)
      self.obj952.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(80.0,160.0,self.obj952)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj952.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj952)
      self.obj952.postAction( self.LHS.CREATE )

      self.obj953=Capabilitie(parent)
      self.obj953.preAction( self.LHS.CREATE )
      self.obj953.isGraphObjectVisual = True

      if(hasattr(self.obj953, '_setHierarchicalLink')):
        self.obj953._setHierarchicalLink(False)

      # name
      self.obj953.name.setValue('')
      self.obj953.name.setNone()

      self.obj953.GGLabel.setValue(3)
      self.obj953.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(260.0,20.0,self.obj953)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj953.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj953)
      self.obj953.postAction( self.LHS.CREATE )

      self.obj954=Role(parent)
      self.obj954.preAction( self.LHS.CREATE )
      self.obj954.isGraphObjectVisual = True

      if(hasattr(self.obj954, '_setHierarchicalLink')):
        self.obj954._setHierarchicalLink(False)

      # name
      self.obj954.name.setValue('')
      self.obj954.name.setNone()

      self.obj954.GGLabel.setValue(4)
      self.obj954.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(280.0,140.0,self.obj954)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj954.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj954)
      self.obj954.postAction( self.LHS.CREATE )

      self.obj955=posses(parent)
      self.obj955.preAction( self.LHS.CREATE )
      self.obj955.isGraphObjectVisual = True

      if(hasattr(self.obj955, '_setHierarchicalLink')):
        self.obj955._setHierarchicalLink(False)

      # rate
      self.obj955.rate.setValue(0.0)

      self.obj955.GGLabel.setValue(5)
      self.obj955.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(183.0,70.5,self.obj955)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj955.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj955)
      self.obj955.postAction( self.LHS.CREATE )

      self.obj956=posses(parent)
      self.obj956.preAction( self.LHS.CREATE )
      self.obj956.isGraphObjectVisual = True

      if(hasattr(self.obj956, '_setHierarchicalLink')):
        self.obj956._setHierarchicalLink(False)

      # rate
      self.obj956.rate.setValue(0.0)

      self.obj956.GGLabel.setValue(6)
      self.obj956.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(93.0,120.5,self.obj956)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj956.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj956)
      self.obj956.postAction( self.LHS.CREATE )

      self.obj957=CapableOf(parent)
      self.obj957.preAction( self.LHS.CREATE )
      self.obj957.isGraphObjectVisual = True

      if(hasattr(self.obj957, '_setHierarchicalLink')):
        self.obj957._setHierarchicalLink(False)

      self.obj957.GGLabel.setValue(9)
      self.obj957.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(194.5,111.5,self.obj957)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj957.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj957)
      self.obj957.postAction( self.LHS.CREATE )

      self.obj958=requir(parent)
      self.obj958.preAction( self.LHS.CREATE )
      self.obj958.isGraphObjectVisual = True

      if(hasattr(self.obj958, '_setHierarchicalLink')):
        self.obj958._setHierarchicalLink(False)

      self.obj958.GGLabel.setValue(7)
      self.obj958.graphClass_= graph_requir
      if parent.genGraphics:
         new_obj = graph_requir(202.5,192.5,self.obj958)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj958.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj958)
      self.obj958.postAction( self.LHS.CREATE )

      self.obj959=requir(parent)
      self.obj959.preAction( self.LHS.CREATE )
      self.obj959.isGraphObjectVisual = True

      if(hasattr(self.obj959, '_setHierarchicalLink')):
        self.obj959._setHierarchicalLink(False)

      self.obj959.GGLabel.setValue(8)
      self.obj959.graphClass_= graph_requir
      if parent.genGraphics:
         new_obj = graph_requir(292.5,100.0,self.obj959)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj959.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj959)
      self.obj959.postAction( self.LHS.CREATE )

      self.obj951.out_connections_.append(self.obj955)
      self.obj955.in_connections_.append(self.obj951)
      self.obj951.graphObject_.pendingConnections.append((self.obj951.graphObject_.tag, self.obj955.graphObject_.tag, [85.0, 82.0, 183.0, 70.5], 0, True))
      self.obj951.out_connections_.append(self.obj956)
      self.obj956.in_connections_.append(self.obj951)
      self.obj951.graphObject_.pendingConnections.append((self.obj951.graphObject_.tag, self.obj956.graphObject_.tag, [85.0, 82.0, 93.0, 120.5], 0, True))
      self.obj951.out_connections_.append(self.obj957)
      self.obj957.in_connections_.append(self.obj951)
      self.obj951.graphObject_.pendingConnections.append((self.obj951.graphObject_.tag, self.obj957.graphObject_.tag, [85.0, 82.0, 194.5, 111.5], 0, True))
      self.obj954.out_connections_.append(self.obj958)
      self.obj958.in_connections_.append(self.obj954)
      self.obj954.graphObject_.pendingConnections.append((self.obj954.graphObject_.tag, self.obj958.graphObject_.tag, [304.0, 186.0, 202.5, 192.5], 0, True))
      self.obj954.out_connections_.append(self.obj959)
      self.obj959.in_connections_.append(self.obj954)
      self.obj954.graphObject_.pendingConnections.append((self.obj954.graphObject_.tag, self.obj959.graphObject_.tag, [304.0, 141.0, 292.5, 100.0], 0, True))
      self.obj955.out_connections_.append(self.obj953)
      self.obj953.in_connections_.append(self.obj955)
      self.obj955.graphObject_.pendingConnections.append((self.obj955.graphObject_.tag, self.obj953.graphObject_.tag, [281.0, 59.0, 183.0, 70.5], 0, True))
      self.obj956.out_connections_.append(self.obj952)
      self.obj952.in_connections_.append(self.obj956)
      self.obj956.graphObject_.pendingConnections.append((self.obj956.graphObject_.tag, self.obj952.graphObject_.tag, [101.0, 159.0, 93.0, 120.5], 0, True))
      self.obj957.out_connections_.append(self.obj954)
      self.obj954.in_connections_.append(self.obj957)
      self.obj957.graphObject_.pendingConnections.append((self.obj957.graphObject_.tag, self.obj954.graphObject_.tag, [311.0, 140.0, 194.5, 111.5], 2, 0))
      self.obj958.out_connections_.append(self.obj952)
      self.obj952.in_connections_.append(self.obj958)
      self.obj958.graphObject_.pendingConnections.append((self.obj958.graphObject_.tag, self.obj952.graphObject_.tag, [101.0, 199.0, 202.5, 192.5], 0, True))
      self.obj959.out_connections_.append(self.obj953)
      self.obj953.in_connections_.append(self.obj959)
      self.obj959.graphObject_.pendingConnections.append((self.obj959.graphObject_.tag, self.obj953.graphObject_.tag, [281.0, 59.0, 292.5, 100.0], 0, True))

      self.RHS = ASG_omacss(parent)

      self.obj961=Agent(parent)
      self.obj961.preAction( self.RHS.CREATE )
      self.obj961.isGraphObjectVisual = True

      if(hasattr(self.obj961, '_setHierarchicalLink')):
        self.obj961._setHierarchicalLink(False)

      # price
      self.obj961.price.setValue(0)

      # name
      self.obj961.name.setValue('')
      self.obj961.name.setNone()

      self.obj961.GGLabel.setValue(1)
      self.obj961.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(60.0,20.0,self.obj961)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj961.graphObject_ = new_obj
      self.obj9610= AttrCalc()
      self.obj9610.Copy=ATOM3Boolean()
      self.obj9610.Copy.setValue(('Copy from LHS', 1))
      self.obj9610.Copy.config = 0
      self.obj9610.Specify=ATOM3Constraint()
      self.obj9610.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj961.GGset2Any['price']= self.obj9610
      self.obj9611= AttrCalc()
      self.obj9611.Copy=ATOM3Boolean()
      self.obj9611.Copy.setValue(('Copy from LHS', 1))
      self.obj9611.Copy.config = 0
      self.obj9611.Specify=ATOM3Constraint()
      self.obj9611.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj961.GGset2Any['name']= self.obj9611

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj961)
      self.obj961.postAction( self.RHS.CREATE )

      self.obj962=Capabilitie(parent)
      self.obj962.preAction( self.RHS.CREATE )
      self.obj962.isGraphObjectVisual = True

      if(hasattr(self.obj962, '_setHierarchicalLink')):
        self.obj962._setHierarchicalLink(False)

      # name
      self.obj962.name.setValue('')
      self.obj962.name.setNone()

      self.obj962.GGLabel.setValue(2)
      self.obj962.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(80.0,160.0,self.obj962)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj962.graphObject_ = new_obj
      self.obj9620= AttrCalc()
      self.obj9620.Copy=ATOM3Boolean()
      self.obj9620.Copy.setValue(('Copy from LHS', 1))
      self.obj9620.Copy.config = 0
      self.obj9620.Specify=ATOM3Constraint()
      self.obj9620.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj962.GGset2Any['name']= self.obj9620

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj962)
      self.obj962.postAction( self.RHS.CREATE )

      self.obj963=Capabilitie(parent)
      self.obj963.preAction( self.RHS.CREATE )
      self.obj963.isGraphObjectVisual = True

      if(hasattr(self.obj963, '_setHierarchicalLink')):
        self.obj963._setHierarchicalLink(False)

      # name
      self.obj963.name.setValue('')
      self.obj963.name.setNone()

      self.obj963.GGLabel.setValue(3)
      self.obj963.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(260.0,20.0,self.obj963)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj963.graphObject_ = new_obj
      self.obj9630= AttrCalc()
      self.obj9630.Copy=ATOM3Boolean()
      self.obj9630.Copy.setValue(('Copy from LHS', 1))
      self.obj9630.Copy.config = 0
      self.obj9630.Specify=ATOM3Constraint()
      self.obj9630.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj963.GGset2Any['name']= self.obj9630

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj963)
      self.obj963.postAction( self.RHS.CREATE )

      self.obj964=Role(parent)
      self.obj964.preAction( self.RHS.CREATE )
      self.obj964.isGraphObjectVisual = True

      if(hasattr(self.obj964, '_setHierarchicalLink')):
        self.obj964._setHierarchicalLink(False)

      # name
      self.obj964.name.setValue('')
      self.obj964.name.setNone()

      self.obj964.GGLabel.setValue(4)
      self.obj964.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(280.0,140.0,self.obj964)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj964.graphObject_ = new_obj
      self.obj9640= AttrCalc()
      self.obj9640.Copy=ATOM3Boolean()
      self.obj9640.Copy.setValue(('Copy from LHS', 1))
      self.obj9640.Copy.config = 0
      self.obj9640.Specify=ATOM3Constraint()
      self.obj9640.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj964.GGset2Any['name']= self.obj9640

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj964)
      self.obj964.postAction( self.RHS.CREATE )

      self.obj965=posses(parent)
      self.obj965.preAction( self.RHS.CREATE )
      self.obj965.isGraphObjectVisual = True

      if(hasattr(self.obj965, '_setHierarchicalLink')):
        self.obj965._setHierarchicalLink(False)

      # rate
      self.obj965.rate.setValue(0.0)

      self.obj965.GGLabel.setValue(5)
      self.obj965.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(183.0,70.5,self.obj965)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj965.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj965)
      self.obj965.postAction( self.RHS.CREATE )

      self.obj966=posses(parent)
      self.obj966.preAction( self.RHS.CREATE )
      self.obj966.isGraphObjectVisual = True

      if(hasattr(self.obj966, '_setHierarchicalLink')):
        self.obj966._setHierarchicalLink(False)

      # rate
      self.obj966.rate.setValue(0.0)

      self.obj966.GGLabel.setValue(6)
      self.obj966.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(93.0,120.5,self.obj966)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj966.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj966)
      self.obj966.postAction( self.RHS.CREATE )

      self.obj967=CapableOf(parent)
      self.obj967.preAction( self.RHS.CREATE )
      self.obj967.isGraphObjectVisual = True

      if(hasattr(self.obj967, '_setHierarchicalLink')):
        self.obj967._setHierarchicalLink(False)

      self.obj967.GGLabel.setValue(9)
      self.obj967.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(194.5,111.5,self.obj967)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj967.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj967)
      self.obj967.postAction( self.RHS.CREATE )

      self.obj968=requir(parent)
      self.obj968.preAction( self.RHS.CREATE )
      self.obj968.isGraphObjectVisual = True

      if(hasattr(self.obj968, '_setHierarchicalLink')):
        self.obj968._setHierarchicalLink(False)

      self.obj968.GGLabel.setValue(7)
      self.obj968.graphClass_= graph_requir
      if parent.genGraphics:
         new_obj = graph_requir(202.5,192.5,self.obj968)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj968.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj968)
      self.obj968.postAction( self.RHS.CREATE )

      self.obj969=requir(parent)
      self.obj969.preAction( self.RHS.CREATE )
      self.obj969.isGraphObjectVisual = True

      if(hasattr(self.obj969, '_setHierarchicalLink')):
        self.obj969._setHierarchicalLink(False)

      self.obj969.GGLabel.setValue(8)
      self.obj969.graphClass_= graph_requir
      if parent.genGraphics:
         new_obj = graph_requir(292.5,100.0,self.obj969)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj969.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj969)
      self.obj969.postAction( self.RHS.CREATE )

      self.obj961.out_connections_.append(self.obj965)
      self.obj965.in_connections_.append(self.obj961)
      self.obj961.graphObject_.pendingConnections.append((self.obj961.graphObject_.tag, self.obj965.graphObject_.tag, [97.0, 82.0, 183.0, 70.5], 2, 0))
      self.obj961.out_connections_.append(self.obj966)
      self.obj966.in_connections_.append(self.obj961)
      self.obj961.graphObject_.pendingConnections.append((self.obj961.graphObject_.tag, self.obj966.graphObject_.tag, [97.0, 82.0, 93.0, 120.5], 2, 0))
      self.obj961.out_connections_.append(self.obj967)
      self.obj967.in_connections_.append(self.obj961)
      self.obj961.graphObject_.pendingConnections.append((self.obj961.graphObject_.tag, self.obj967.graphObject_.tag, [97.0, 82.0, 194.5, 111.5], 2, 0))
      self.obj964.out_connections_.append(self.obj968)
      self.obj968.in_connections_.append(self.obj964)
      self.obj964.graphObject_.pendingConnections.append((self.obj964.graphObject_.tag, self.obj968.graphObject_.tag, [311.0, 185.0, 202.5, 192.5], 2, 0))
      self.obj964.out_connections_.append(self.obj969)
      self.obj969.in_connections_.append(self.obj964)
      self.obj964.graphObject_.pendingConnections.append((self.obj964.graphObject_.tag, self.obj969.graphObject_.tag, [311.0, 140.0, 292.5, 100.0], 2, 0))
      self.obj965.out_connections_.append(self.obj963)
      self.obj963.in_connections_.append(self.obj965)
      self.obj965.graphObject_.pendingConnections.append((self.obj965.graphObject_.tag, self.obj963.graphObject_.tag, [291.0, 63.0, 183.0, 70.5], 2, 0))
      self.obj966.out_connections_.append(self.obj962)
      self.obj962.in_connections_.append(self.obj966)
      self.obj966.graphObject_.pendingConnections.append((self.obj966.graphObject_.tag, self.obj962.graphObject_.tag, [111.0, 163.0, 93.0, 120.5], 2, 0))
      self.obj967.out_connections_.append(self.obj964)
      self.obj964.in_connections_.append(self.obj967)
      self.obj967.graphObject_.pendingConnections.append((self.obj967.graphObject_.tag, self.obj964.graphObject_.tag, [311.0, 140.0, 194.5, 111.5], 2, 0))
      self.obj968.out_connections_.append(self.obj962)
      self.obj962.in_connections_.append(self.obj968)
      self.obj968.graphObject_.pendingConnections.append((self.obj968.graphObject_.tag, self.obj962.graphObject_.tag, [111.0, 203.0, 202.5, 192.5], 2, 0))
      self.obj969.out_connections_.append(self.obj963)
      self.obj963.in_connections_.append(self.obj969)
      self.obj969.graphObject_.pendingConnections.append((self.obj969.graphObject_.tag, self.obj963.graphObject_.tag, [291.0, 63.0, 292.5, 100.0], 2, 0))

   def condition(self, graphID, isograph, atom3i):
      
      agent = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      c1 = self.getMatched(graphID, self.LHS.nodeWithLabel(2))
      c2 = self.getMatched(graphID, self.LHS.nodeWithLabel(3))
      role = self.getMatched(graphID, self.LHS.nodeWithLabel(4))
      
      return not ( hasattr(c1, agent.name.getValue() ) and 
      hasattr(c1, role.name.getValue() ) and
      hasattr(c2, agent.name.getValue() ) and  hasattr(c2,  role.name.getValue()  ) )
      
      

   def action(self, graphID, isograph, atom3i):
      agent = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      c1 = self.getMatched(graphID, self.LHS.nodeWithLabel(2))
      c2 = self.getMatched(graphID, self.LHS.nodeWithLabel(3))
      role = self.getMatched(graphID, self.LHS.nodeWithLabel(4))
      
      setattr( c1 ,  agent.name.getValue() , True )
      setattr( c1 ,  role.name.getValue() , True )
      
      setattr( c2 ,  agent.name.getValue() , True )
      setattr( c2 ,  role.name.getValue() , True )
      print' Mark :('+agent.name.getValue()+','+c1.name.getValue()+','+c2.name.getValue()+','+role.name.getValue()+')'
      
      

