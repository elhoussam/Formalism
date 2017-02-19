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

      self.obj154=Agent(parent)
      self.obj154.preAction( self.LHS.CREATE )
      self.obj154.isGraphObjectVisual = True

      if(hasattr(self.obj154, '_setHierarchicalLink')):
        self.obj154._setHierarchicalLink(False)

      # price
      self.obj154.price.setValue(0)

      # name
      self.obj154.name.setValue('')
      self.obj154.name.setNone()

      self.obj154.GGLabel.setValue(1)
      self.obj154.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(60.0,20.0,self.obj154)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj154.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj154)
      self.obj154.postAction( self.LHS.CREATE )

      self.obj155=Capabilitie(parent)
      self.obj155.preAction( self.LHS.CREATE )
      self.obj155.isGraphObjectVisual = True

      if(hasattr(self.obj155, '_setHierarchicalLink')):
        self.obj155._setHierarchicalLink(False)

      # name
      self.obj155.name.setValue('')
      self.obj155.name.setNone()

      self.obj155.GGLabel.setValue(2)
      self.obj155.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(80.0,160.0,self.obj155)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj155.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj155)
      self.obj155.postAction( self.LHS.CREATE )

      self.obj156=Capabilitie(parent)
      self.obj156.preAction( self.LHS.CREATE )
      self.obj156.isGraphObjectVisual = True

      if(hasattr(self.obj156, '_setHierarchicalLink')):
        self.obj156._setHierarchicalLink(False)

      # name
      self.obj156.name.setValue('')
      self.obj156.name.setNone()

      self.obj156.GGLabel.setValue(3)
      self.obj156.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(260.0,20.0,self.obj156)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj156.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj156)
      self.obj156.postAction( self.LHS.CREATE )

      self.obj157=Role(parent)
      self.obj157.preAction( self.LHS.CREATE )
      self.obj157.isGraphObjectVisual = True

      if(hasattr(self.obj157, '_setHierarchicalLink')):
        self.obj157._setHierarchicalLink(False)

      # name
      self.obj157.name.setValue('')
      self.obj157.name.setNone()

      self.obj157.GGLabel.setValue(4)
      self.obj157.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(280.0,140.0,self.obj157)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj157.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj157)
      self.obj157.postAction( self.LHS.CREATE )

      self.obj158=posses(parent)
      self.obj158.preAction( self.LHS.CREATE )
      self.obj158.isGraphObjectVisual = True

      if(hasattr(self.obj158, '_setHierarchicalLink')):
        self.obj158._setHierarchicalLink(False)

      # rate
      self.obj158.rate.setNone()

      self.obj158.GGLabel.setValue(5)
      self.obj158.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(183.0,70.5,self.obj158)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj158.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj158)
      self.obj158.postAction( self.LHS.CREATE )

      self.obj159=posses(parent)
      self.obj159.preAction( self.LHS.CREATE )
      self.obj159.isGraphObjectVisual = True

      if(hasattr(self.obj159, '_setHierarchicalLink')):
        self.obj159._setHierarchicalLink(False)

      # rate
      self.obj159.rate.setNone()

      self.obj159.GGLabel.setValue(6)
      self.obj159.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(93.0,120.5,self.obj159)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj159.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj159)
      self.obj159.postAction( self.LHS.CREATE )

      self.obj160=CapableOf(parent)
      self.obj160.preAction( self.LHS.CREATE )
      self.obj160.isGraphObjectVisual = True

      if(hasattr(self.obj160, '_setHierarchicalLink')):
        self.obj160._setHierarchicalLink(False)

      self.obj160.GGLabel.setValue(9)
      self.obj160.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(194.5,111.5,self.obj160)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj160.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj160)
      self.obj160.postAction( self.LHS.CREATE )

      self.obj161=requir(parent)
      self.obj161.preAction( self.LHS.CREATE )
      self.obj161.isGraphObjectVisual = True

      if(hasattr(self.obj161, '_setHierarchicalLink')):
        self.obj161._setHierarchicalLink(False)

      self.obj161.GGLabel.setValue(7)
      self.obj161.graphClass_= graph_requir
      if parent.genGraphics:
         new_obj = graph_requir(202.5,192.5,self.obj161)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj161.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj161)
      self.obj161.postAction( self.LHS.CREATE )

      self.obj162=requir(parent)
      self.obj162.preAction( self.LHS.CREATE )
      self.obj162.isGraphObjectVisual = True

      if(hasattr(self.obj162, '_setHierarchicalLink')):
        self.obj162._setHierarchicalLink(False)

      self.obj162.GGLabel.setValue(8)
      self.obj162.graphClass_= graph_requir
      if parent.genGraphics:
         new_obj = graph_requir(292.5,100.0,self.obj162)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj162.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj162)
      self.obj162.postAction( self.LHS.CREATE )

      self.obj154.out_connections_.append(self.obj158)
      self.obj158.in_connections_.append(self.obj154)
      self.obj154.graphObject_.pendingConnections.append((self.obj154.graphObject_.tag, self.obj158.graphObject_.tag, [85.0, 82.0, 183.0, 70.5], 0, True))
      self.obj154.out_connections_.append(self.obj159)
      self.obj159.in_connections_.append(self.obj154)
      self.obj154.graphObject_.pendingConnections.append((self.obj154.graphObject_.tag, self.obj159.graphObject_.tag, [85.0, 82.0, 93.0, 120.5], 0, True))
      self.obj154.out_connections_.append(self.obj160)
      self.obj160.in_connections_.append(self.obj154)
      self.obj154.graphObject_.pendingConnections.append((self.obj154.graphObject_.tag, self.obj160.graphObject_.tag, [85.0, 82.0, 194.5, 111.5], 0, True))
      self.obj157.out_connections_.append(self.obj161)
      self.obj161.in_connections_.append(self.obj157)
      self.obj157.graphObject_.pendingConnections.append((self.obj157.graphObject_.tag, self.obj161.graphObject_.tag, [304.0, 186.0, 202.5, 192.5], 0, True))
      self.obj157.out_connections_.append(self.obj162)
      self.obj162.in_connections_.append(self.obj157)
      self.obj157.graphObject_.pendingConnections.append((self.obj157.graphObject_.tag, self.obj162.graphObject_.tag, [304.0, 141.0, 292.5, 100.0], 0, True))
      self.obj158.out_connections_.append(self.obj156)
      self.obj156.in_connections_.append(self.obj158)
      self.obj158.graphObject_.pendingConnections.append((self.obj158.graphObject_.tag, self.obj156.graphObject_.tag, [281.0, 59.0, 183.0, 70.5], 0, True))
      self.obj159.out_connections_.append(self.obj155)
      self.obj155.in_connections_.append(self.obj159)
      self.obj159.graphObject_.pendingConnections.append((self.obj159.graphObject_.tag, self.obj155.graphObject_.tag, [101.0, 159.0, 93.0, 120.5], 0, True))
      self.obj160.out_connections_.append(self.obj157)
      self.obj157.in_connections_.append(self.obj160)
      self.obj160.graphObject_.pendingConnections.append((self.obj160.graphObject_.tag, self.obj157.graphObject_.tag, [311.0, 140.0, 194.5, 111.5], 2, 0))
      self.obj161.out_connections_.append(self.obj155)
      self.obj155.in_connections_.append(self.obj161)
      self.obj161.graphObject_.pendingConnections.append((self.obj161.graphObject_.tag, self.obj155.graphObject_.tag, [101.0, 199.0, 202.5, 192.5], 0, True))
      self.obj162.out_connections_.append(self.obj156)
      self.obj156.in_connections_.append(self.obj162)
      self.obj162.graphObject_.pendingConnections.append((self.obj162.graphObject_.tag, self.obj156.graphObject_.tag, [281.0, 59.0, 292.5, 100.0], 0, True))

      self.RHS = ASG_omacss(parent)

      self.obj164=Agent(parent)
      self.obj164.preAction( self.RHS.CREATE )
      self.obj164.isGraphObjectVisual = True

      if(hasattr(self.obj164, '_setHierarchicalLink')):
        self.obj164._setHierarchicalLink(False)

      # price
      self.obj164.price.setValue(0)

      # name
      self.obj164.name.setValue('')
      self.obj164.name.setNone()

      self.obj164.GGLabel.setValue(1)
      self.obj164.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(60.0,20.0,self.obj164)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj164.graphObject_ = new_obj
      self.obj1640= AttrCalc()
      self.obj1640.Copy=ATOM3Boolean()
      self.obj1640.Copy.setValue(('Copy from LHS', 1))
      self.obj1640.Copy.config = 0
      self.obj1640.Specify=ATOM3Constraint()
      self.obj1640.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj164.GGset2Any['price']= self.obj1640
      self.obj1641= AttrCalc()
      self.obj1641.Copy=ATOM3Boolean()
      self.obj1641.Copy.setValue(('Copy from LHS', 1))
      self.obj1641.Copy.config = 0
      self.obj1641.Specify=ATOM3Constraint()
      self.obj1641.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj164.GGset2Any['name']= self.obj1641

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj164)
      self.obj164.postAction( self.RHS.CREATE )

      self.obj165=Capabilitie(parent)
      self.obj165.preAction( self.RHS.CREATE )
      self.obj165.isGraphObjectVisual = True

      if(hasattr(self.obj165, '_setHierarchicalLink')):
        self.obj165._setHierarchicalLink(False)

      # name
      self.obj165.name.setValue('')
      self.obj165.name.setNone()

      self.obj165.GGLabel.setValue(2)
      self.obj165.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(80.0,160.0,self.obj165)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj165.graphObject_ = new_obj
      self.obj1650= AttrCalc()
      self.obj1650.Copy=ATOM3Boolean()
      self.obj1650.Copy.setValue(('Copy from LHS', 1))
      self.obj1650.Copy.config = 0
      self.obj1650.Specify=ATOM3Constraint()
      self.obj1650.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj165.GGset2Any['name']= self.obj1650

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj165)
      self.obj165.postAction( self.RHS.CREATE )

      self.obj166=Capabilitie(parent)
      self.obj166.preAction( self.RHS.CREATE )
      self.obj166.isGraphObjectVisual = True

      if(hasattr(self.obj166, '_setHierarchicalLink')):
        self.obj166._setHierarchicalLink(False)

      # name
      self.obj166.name.setValue('')
      self.obj166.name.setNone()

      self.obj166.GGLabel.setValue(3)
      self.obj166.graphClass_= graph_Capabilitie
      if parent.genGraphics:
         new_obj = graph_Capabilitie(260.0,20.0,self.obj166)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj166.graphObject_ = new_obj
      self.obj1660= AttrCalc()
      self.obj1660.Copy=ATOM3Boolean()
      self.obj1660.Copy.setValue(('Copy from LHS', 1))
      self.obj1660.Copy.config = 0
      self.obj1660.Specify=ATOM3Constraint()
      self.obj1660.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj166.GGset2Any['name']= self.obj1660

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj166)
      self.obj166.postAction( self.RHS.CREATE )

      self.obj167=Role(parent)
      self.obj167.preAction( self.RHS.CREATE )
      self.obj167.isGraphObjectVisual = True

      if(hasattr(self.obj167, '_setHierarchicalLink')):
        self.obj167._setHierarchicalLink(False)

      # name
      self.obj167.name.setValue('')
      self.obj167.name.setNone()

      self.obj167.GGLabel.setValue(4)
      self.obj167.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(280.0,140.0,self.obj167)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj167.graphObject_ = new_obj
      self.obj1670= AttrCalc()
      self.obj1670.Copy=ATOM3Boolean()
      self.obj1670.Copy.setValue(('Copy from LHS', 1))
      self.obj1670.Copy.config = 0
      self.obj1670.Specify=ATOM3Constraint()
      self.obj1670.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj167.GGset2Any['name']= self.obj1670

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj167)
      self.obj167.postAction( self.RHS.CREATE )

      self.obj168=posses(parent)
      self.obj168.preAction( self.RHS.CREATE )
      self.obj168.isGraphObjectVisual = True

      if(hasattr(self.obj168, '_setHierarchicalLink')):
        self.obj168._setHierarchicalLink(False)

      # rate
      self.obj168.rate.setValue(0.0)

      self.obj168.GGLabel.setValue(5)
      self.obj168.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(183.0,70.5,self.obj168)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj168.graphObject_ = new_obj
      self.obj1680= AttrCalc()
      self.obj1680.Copy=ATOM3Boolean()
      self.obj1680.Copy.setValue(('Copy from LHS', 1))
      self.obj1680.Copy.config = 0
      self.obj1680.Specify=ATOM3Constraint()
      self.obj1680.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj168.GGset2Any['rate']= self.obj1680

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj168)
      self.obj168.postAction( self.RHS.CREATE )

      self.obj169=posses(parent)
      self.obj169.preAction( self.RHS.CREATE )
      self.obj169.isGraphObjectVisual = True

      if(hasattr(self.obj169, '_setHierarchicalLink')):
        self.obj169._setHierarchicalLink(False)

      # rate
      self.obj169.rate.setValue(0.0)

      self.obj169.GGLabel.setValue(6)
      self.obj169.graphClass_= graph_posses
      if parent.genGraphics:
         new_obj = graph_posses(93.0,120.5,self.obj169)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj169.graphObject_ = new_obj
      self.obj1690= AttrCalc()
      self.obj1690.Copy=ATOM3Boolean()
      self.obj1690.Copy.setValue(('Copy from LHS', 1))
      self.obj1690.Copy.config = 0
      self.obj1690.Specify=ATOM3Constraint()
      self.obj1690.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj169.GGset2Any['rate']= self.obj1690

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj169)
      self.obj169.postAction( self.RHS.CREATE )

      self.obj170=CapableOf(parent)
      self.obj170.preAction( self.RHS.CREATE )
      self.obj170.isGraphObjectVisual = True

      if(hasattr(self.obj170, '_setHierarchicalLink')):
        self.obj170._setHierarchicalLink(False)

      self.obj170.GGLabel.setValue(9)
      self.obj170.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(194.5,111.5,self.obj170)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj170.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj170)
      self.obj170.postAction( self.RHS.CREATE )

      self.obj171=requir(parent)
      self.obj171.preAction( self.RHS.CREATE )
      self.obj171.isGraphObjectVisual = True

      if(hasattr(self.obj171, '_setHierarchicalLink')):
        self.obj171._setHierarchicalLink(False)

      self.obj171.GGLabel.setValue(7)
      self.obj171.graphClass_= graph_requir
      if parent.genGraphics:
         new_obj = graph_requir(202.5,192.5,self.obj171)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj171.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj171)
      self.obj171.postAction( self.RHS.CREATE )

      self.obj172=requir(parent)
      self.obj172.preAction( self.RHS.CREATE )
      self.obj172.isGraphObjectVisual = True

      if(hasattr(self.obj172, '_setHierarchicalLink')):
        self.obj172._setHierarchicalLink(False)

      self.obj172.GGLabel.setValue(8)
      self.obj172.graphClass_= graph_requir
      if parent.genGraphics:
         new_obj = graph_requir(292.5,100.0,self.obj172)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj172.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj172)
      self.obj172.postAction( self.RHS.CREATE )

      self.obj164.out_connections_.append(self.obj168)
      self.obj168.in_connections_.append(self.obj164)
      self.obj164.graphObject_.pendingConnections.append((self.obj164.graphObject_.tag, self.obj168.graphObject_.tag, [97.0, 82.0, 183.0, 70.5], 2, 0))
      self.obj164.out_connections_.append(self.obj169)
      self.obj169.in_connections_.append(self.obj164)
      self.obj164.graphObject_.pendingConnections.append((self.obj164.graphObject_.tag, self.obj169.graphObject_.tag, [97.0, 82.0, 93.0, 120.5], 2, 0))
      self.obj164.out_connections_.append(self.obj170)
      self.obj170.in_connections_.append(self.obj164)
      self.obj164.graphObject_.pendingConnections.append((self.obj164.graphObject_.tag, self.obj170.graphObject_.tag, [97.0, 82.0, 194.5, 111.5], 2, 0))
      self.obj167.out_connections_.append(self.obj171)
      self.obj171.in_connections_.append(self.obj167)
      self.obj167.graphObject_.pendingConnections.append((self.obj167.graphObject_.tag, self.obj171.graphObject_.tag, [311.0, 185.0, 202.5, 192.5], 2, 0))
      self.obj167.out_connections_.append(self.obj172)
      self.obj172.in_connections_.append(self.obj167)
      self.obj167.graphObject_.pendingConnections.append((self.obj167.graphObject_.tag, self.obj172.graphObject_.tag, [311.0, 140.0, 292.5, 100.0], 2, 0))
      self.obj168.out_connections_.append(self.obj166)
      self.obj166.in_connections_.append(self.obj168)
      self.obj168.graphObject_.pendingConnections.append((self.obj168.graphObject_.tag, self.obj166.graphObject_.tag, [291.0, 63.0, 183.0, 70.5], 2, 0))
      self.obj169.out_connections_.append(self.obj165)
      self.obj165.in_connections_.append(self.obj169)
      self.obj169.graphObject_.pendingConnections.append((self.obj169.graphObject_.tag, self.obj165.graphObject_.tag, [111.0, 163.0, 93.0, 120.5], 2, 0))
      self.obj170.out_connections_.append(self.obj167)
      self.obj167.in_connections_.append(self.obj170)
      self.obj170.graphObject_.pendingConnections.append((self.obj170.graphObject_.tag, self.obj167.graphObject_.tag, [311.0, 140.0, 194.5, 111.5], 2, 0))
      self.obj171.out_connections_.append(self.obj165)
      self.obj165.in_connections_.append(self.obj171)
      self.obj171.graphObject_.pendingConnections.append((self.obj171.graphObject_.tag, self.obj165.graphObject_.tag, [111.0, 203.0, 202.5, 192.5], 2, 0))
      self.obj172.out_connections_.append(self.obj166)
      self.obj166.in_connections_.append(self.obj172)
      self.obj172.graphObject_.pendingConnections.append((self.obj172.graphObject_.tag, self.obj166.graphObject_.tag, [291.0, 63.0, 292.5, 100.0], 2, 0))

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
      
      

