# _ CreateMat_ARG_GG_rule.py ____________________________________________________________________________
# File generated automatically by ATOM3. Graph Grammar Rule
# ___________________________________________________________________________________________
from GGrule import *
from Capabilitie import *
from rawMaterial import *
from Goal import *
from ASG_pns import *
from operatingUnit import *
from metarial import *
from product import *
from Agent import *
from fromMaterial import *
from CapableOf import *
from intoProduct import *
from Role import *
from fromRaw import *
from intoMaterial import *
from ASG_omacs import *
from require import *
from achieve import *
from posses import *
from GenericGraphEdge import *
from GenericGraphNode import *
from ASG_GenericGraph import *
class CreateMat_ARG_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 17)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_pns(parent)
      self.LHS.merge(ASG_omacs(parent))

      self.obj223=CapableOf(parent)
      self.obj223.preAction( self.LHS.CREATE )
      self.obj223.isGraphObjectVisual = True

      if(hasattr(self.obj223, '_setHierarchicalLink')):
        self.obj223._setHierarchicalLink(False)

      # rate
      self.obj223.rate.setNone()

      self.obj223.GGLabel.setValue(4)
      self.obj223.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(250.75,110.75,self.obj223)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj223.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj223)
      self.obj223.postAction( self.LHS.CREATE )

      self.obj224=Goal(parent)
      self.obj224.preAction( self.LHS.CREATE )
      self.obj224.isGraphObjectVisual = True

      if(hasattr(self.obj224, '_setHierarchicalLink')):
        self.obj224._setHierarchicalLink(False)

      # name
      self.obj224.name.setValue('')
      self.obj224.name.setNone()

      self.obj224.GGLabel.setValue(3)
      self.obj224.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(100.0,240.0,self.obj224)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj224.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj224)
      self.obj224.postAction( self.LHS.CREATE )

      self.obj225=Agent(parent)
      self.obj225.preAction( self.LHS.CREATE )
      self.obj225.isGraphObjectVisual = True

      if(hasattr(self.obj225, '_setHierarchicalLink')):
        self.obj225._setHierarchicalLink(False)

      # price
      self.obj225.price.setNone()

      # name
      self.obj225.name.setValue('')
      self.obj225.name.setNone()

      self.obj225.GGLabel.setValue(1)
      self.obj225.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(80.0,40.0,self.obj225)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj225.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj225)
      self.obj225.postAction( self.LHS.CREATE )

      self.obj226=Role(parent)
      self.obj226.preAction( self.LHS.CREATE )
      self.obj226.isGraphObjectVisual = True

      if(hasattr(self.obj226, '_setHierarchicalLink')):
        self.obj226._setHierarchicalLink(False)

      # name
      self.obj226.name.setValue('')
      self.obj226.name.setNone()

      self.obj226.GGLabel.setValue(2)
      self.obj226.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(280.0,140.0,self.obj226)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj226.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj226)
      self.obj226.postAction( self.LHS.CREATE )

      self.obj227=achieve(parent)
      self.obj227.preAction( self.LHS.CREATE )
      self.obj227.isGraphObjectVisual = True

      if(hasattr(self.obj227, '_setHierarchicalLink')):
        self.obj227._setHierarchicalLink(False)

      # rate
      self.obj227.rate.setNone()

      self.obj227.GGLabel.setValue(5)
      self.obj227.graphClass_= graph_achieve
      if parent.genGraphics:
         new_obj = graph_achieve(258.5,259.0,self.obj227)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj227.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj227)
      self.obj227.postAction( self.LHS.CREATE )

      self.obj223.out_connections_.append(self.obj226)
      self.obj226.in_connections_.append(self.obj223)
      self.obj223.graphObject_.pendingConnections.append((self.obj223.graphObject_.tag, self.obj226.graphObject_.tag, [304.0, 141.0, 300.5, 120.5, 250.75, 110.75], 2, True))
      self.obj225.out_connections_.append(self.obj223)
      self.obj223.in_connections_.append(self.obj225)
      self.obj225.graphObject_.pendingConnections.append((self.obj225.graphObject_.tag, self.obj223.graphObject_.tag, [105.0, 102.0, 201.0, 101.0, 250.75, 110.75], 2, True))
      self.obj226.out_connections_.append(self.obj227)
      self.obj227.in_connections_.append(self.obj226)
      self.obj226.graphObject_.pendingConnections.append((self.obj226.graphObject_.tag, self.obj227.graphObject_.tag, [304.0, 186.0, 303.5, 233.0, 258.5, 259.0], 2, True))
      self.obj227.out_connections_.append(self.obj224)
      self.obj224.in_connections_.append(self.obj227)
      self.obj227.graphObject_.pendingConnections.append((self.obj227.graphObject_.tag, self.obj224.graphObject_.tag, [124.0, 290.0, 213.5, 285.0, 258.5, 259.0], 2, True))

      self.RHS = ASG_pns(parent)
      self.RHS.merge(ASG_omacs(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj231=metarial(parent)
      self.obj231.preAction( self.RHS.CREATE )
      self.obj231.isGraphObjectVisual = True

      if(hasattr(self.obj231, '_setHierarchicalLink')):
        self.obj231._setHierarchicalLink(False)

      # MaxFlow
      self.obj231.MaxFlow.setValue(999999)

      # price
      self.obj231.price.setValue(0)

      # Name
      self.obj231.Name.setValue('')
      self.obj231.Name.setNone()

      # ReqFlow
      self.obj231.ReqFlow.setValue(0)

      self.obj231.GGLabel.setValue(8)
      self.obj231.graphClass_= graph_metarial
      if parent.genGraphics:
         new_obj = graph_metarial(400.0,80.0,self.obj231)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj231.graphObject_ = new_obj
      self.obj2310= AttrCalc()
      self.obj2310.Copy=ATOM3Boolean()
      self.obj2310.Copy.setValue(('Copy from LHS', 1))
      self.obj2310.Copy.config = 0
      self.obj2310.Specify=ATOM3Constraint()
      self.obj2310.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj231.GGset2Any['MaxFlow']= self.obj2310
      self.obj2311= AttrCalc()
      self.obj2311.Copy=ATOM3Boolean()
      self.obj2311.Copy.setValue(('Copy from LHS', 0))
      self.obj2311.Copy.config = 0
      self.obj2311.Specify=ATOM3Constraint()
      self.obj2311.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()+\' \'+ self.getMatched(graphID, self.LHS.nodeWithLabel(2)).name.getValue()+\' \'+ self.getMatched(graphID, self.LHS.nodeWithLabel(3)).name.getValue()\n\n'))
      self.obj231.GGset2Any['Name']= self.obj2311
      self.obj2312= AttrCalc()
      self.obj2312.Copy=ATOM3Boolean()
      self.obj2312.Copy.setValue(('Copy from LHS', 1))
      self.obj2312.Copy.config = 0
      self.obj2312.Specify=ATOM3Constraint()
      self.obj2312.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj231.GGset2Any['ReqFlow']= self.obj2312

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj231)
      self.obj231.postAction( self.RHS.CREATE )

      self.obj232=operatingUnit(parent)
      self.obj232.preAction( self.RHS.CREATE )
      self.obj232.isGraphObjectVisual = True

      if(hasattr(self.obj232, '_setHierarchicalLink')):
        self.obj232._setHierarchicalLink(False)

      # OperCostProp
      self.obj232.OperCostProp.setValue(0.0)

      # name
      self.obj232.name.setValue('')
      self.obj232.name.setNone()

      # OperCostFix
      self.obj232.OperCostFix.setValue(0.0)

      self.obj232.GGLabel.setValue(7)
      self.obj232.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(400.0,240.0,self.obj232)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj232.graphObject_ = new_obj
      self.obj2320= AttrCalc()
      self.obj2320.Copy=ATOM3Boolean()
      self.obj2320.Copy.setValue(('Copy from LHS', 0))
      self.obj2320.Copy.config = 0
      self.obj2320.Specify=ATOM3Constraint()
      self.obj2320.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(5)).rate.getValue()\n'))
      self.obj232.GGset2Any['OperCostProp']= self.obj2320
      self.obj2321= AttrCalc()
      self.obj2321.Copy=ATOM3Boolean()
      self.obj2321.Copy.setValue(('Copy from LHS', 0))
      self.obj2321.Copy.config = 0
      self.obj2321.Specify=ATOM3Constraint()
      self.obj2321.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()+\' \'+ self.getMatched(graphID, self.LHS.nodeWithLabel(2)).name.getValue()+\' \'+ self.getMatched(graphID, self.LHS.nodeWithLabel(3)).name.getValue()\n\n\n\n\n\n\n'))
      self.obj232.GGset2Any['name']= self.obj2321
      self.obj2322= AttrCalc()
      self.obj2322.Copy=ATOM3Boolean()
      self.obj2322.Copy.setValue(('Copy from LHS', 0))
      self.obj2322.Copy.config = 0
      self.obj2322.Specify=ATOM3Constraint()
      self.obj2322.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return 2.0\n'))
      self.obj232.GGset2Any['OperCostFix']= self.obj2322

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj232)
      self.obj232.postAction( self.RHS.CREATE )

      self.obj233=fromMaterial(parent)
      self.obj233.preAction( self.RHS.CREATE )
      self.obj233.isGraphObjectVisual = True

      if(hasattr(self.obj233, '_setHierarchicalLink')):
        self.obj233._setHierarchicalLink(False)

      # rate
      self.obj233.rate.setValue(1.0)

      self.obj233.GGLabel.setValue(9)
      self.obj233.graphClass_= graph_fromMaterial
      if parent.genGraphics:
         new_obj = graph_fromMaterial(422.0,190.0,self.obj233)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj233.graphObject_ = new_obj
      self.obj2330= AttrCalc()
      self.obj2330.Copy=ATOM3Boolean()
      self.obj2330.Copy.setValue(('Copy from LHS', 0))
      self.obj2330.Copy.config = 0
      self.obj2330.Specify=ATOM3Constraint()
      self.obj2330.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj233.GGset2Any['rate']= self.obj2330

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj233)
      self.obj233.postAction( self.RHS.CREATE )

      self.obj234=CapableOf(parent)
      self.obj234.preAction( self.RHS.CREATE )
      self.obj234.isGraphObjectVisual = True

      if(hasattr(self.obj234, '_setHierarchicalLink')):
        self.obj234._setHierarchicalLink(False)

      # rate
      self.obj234.rate.setNone()

      self.obj234.GGLabel.setValue(4)
      self.obj234.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(250.75,110.75,self.obj234)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj234.graphObject_ = new_obj
      self.obj2340= AttrCalc()
      self.obj2340.Copy=ATOM3Boolean()
      self.obj2340.Copy.setValue(('Copy from LHS', 1))
      self.obj2340.Copy.config = 0
      self.obj2340.Specify=ATOM3Constraint()
      self.obj2340.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj234.GGset2Any['rate']= self.obj2340

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj234)
      self.obj234.postAction( self.RHS.CREATE )

      self.obj235=Goal(parent)
      self.obj235.preAction( self.RHS.CREATE )
      self.obj235.isGraphObjectVisual = True

      if(hasattr(self.obj235, '_setHierarchicalLink')):
        self.obj235._setHierarchicalLink(False)

      # name
      self.obj235.name.setValue('')
      self.obj235.name.setNone()

      self.obj235.GGLabel.setValue(3)
      self.obj235.graphClass_= graph_Goal
      if parent.genGraphics:
         new_obj = graph_Goal(100.0,240.0,self.obj235)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj235.graphObject_ = new_obj
      self.obj2350= AttrCalc()
      self.obj2350.Copy=ATOM3Boolean()
      self.obj2350.Copy.setValue(('Copy from LHS', 1))
      self.obj2350.Copy.config = 0
      self.obj2350.Specify=ATOM3Constraint()
      self.obj2350.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj235.GGset2Any['name']= self.obj2350

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj235)
      self.obj235.postAction( self.RHS.CREATE )

      self.obj236=Agent(parent)
      self.obj236.preAction( self.RHS.CREATE )
      self.obj236.isGraphObjectVisual = True

      if(hasattr(self.obj236, '_setHierarchicalLink')):
        self.obj236._setHierarchicalLink(False)

      # price
      self.obj236.price.setNone()

      # name
      self.obj236.name.setValue('')
      self.obj236.name.setNone()

      self.obj236.GGLabel.setValue(1)
      self.obj236.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(80.0,40.0,self.obj236)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj236.graphObject_ = new_obj
      self.obj2360= AttrCalc()
      self.obj2360.Copy=ATOM3Boolean()
      self.obj2360.Copy.setValue(('Copy from LHS', 1))
      self.obj2360.Copy.config = 0
      self.obj2360.Specify=ATOM3Constraint()
      self.obj2360.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj236.GGset2Any['price']= self.obj2360
      self.obj2361= AttrCalc()
      self.obj2361.Copy=ATOM3Boolean()
      self.obj2361.Copy.setValue(('Copy from LHS', 1))
      self.obj2361.Copy.config = 0
      self.obj2361.Specify=ATOM3Constraint()
      self.obj2361.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj236.GGset2Any['name']= self.obj2361

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj236)
      self.obj236.postAction( self.RHS.CREATE )

      self.obj237=Role(parent)
      self.obj237.preAction( self.RHS.CREATE )
      self.obj237.isGraphObjectVisual = True

      if(hasattr(self.obj237, '_setHierarchicalLink')):
        self.obj237._setHierarchicalLink(False)

      # name
      self.obj237.name.setValue('')
      self.obj237.name.setNone()

      self.obj237.GGLabel.setValue(2)
      self.obj237.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(280.0,140.0,self.obj237)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj237.graphObject_ = new_obj
      self.obj2370= AttrCalc()
      self.obj2370.Copy=ATOM3Boolean()
      self.obj2370.Copy.setValue(('Copy from LHS', 1))
      self.obj2370.Copy.config = 0
      self.obj2370.Specify=ATOM3Constraint()
      self.obj2370.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj237.GGset2Any['name']= self.obj2370

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj237)
      self.obj237.postAction( self.RHS.CREATE )

      self.obj238=achieve(parent)
      self.obj238.preAction( self.RHS.CREATE )
      self.obj238.isGraphObjectVisual = True

      if(hasattr(self.obj238, '_setHierarchicalLink')):
        self.obj238._setHierarchicalLink(False)

      # rate
      self.obj238.rate.setNone()

      self.obj238.GGLabel.setValue(5)
      self.obj238.graphClass_= graph_achieve
      if parent.genGraphics:
         new_obj = graph_achieve(258.5,259.0,self.obj238)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj238.graphObject_ = new_obj
      self.obj2380= AttrCalc()
      self.obj2380.Copy=ATOM3Boolean()
      self.obj2380.Copy.setValue(('Copy from LHS', 1))
      self.obj2380.Copy.config = 0
      self.obj2380.Specify=ATOM3Constraint()
      self.obj2380.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj238.GGset2Any['rate']= self.obj2380

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj238)
      self.obj238.postAction( self.RHS.CREATE )

      self.obj239=GenericGraphEdge(parent)
      self.obj239.preAction( self.RHS.CREATE )
      self.obj239.isGraphObjectVisual = True

      if(hasattr(self.obj239, '_setHierarchicalLink')):
        self.obj239._setHierarchicalLink(False)

      self.obj239.GGLabel.setValue(10)
      self.obj239.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(358.5,131.0,self.obj239)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj239.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj239)
      self.obj239.postAction( self.RHS.CREATE )

      self.obj231.out_connections_.append(self.obj233)
      self.obj233.in_connections_.append(self.obj231)
      self.obj231.graphObject_.pendingConnections.append((self.obj231.graphObject_.tag, self.obj233.graphObject_.tag, [424.0, 129.0, 422.0, 190.0], 0, True))
      self.obj233.out_connections_.append(self.obj232)
      self.obj232.in_connections_.append(self.obj233)
      self.obj233.graphObject_.pendingConnections.append((self.obj233.graphObject_.tag, self.obj232.graphObject_.tag, [420.0, 251.0, 422.0, 190.0], 0, True))
      self.obj234.out_connections_.append(self.obj237)
      self.obj237.in_connections_.append(self.obj234)
      self.obj234.graphObject_.pendingConnections.append((self.obj234.graphObject_.tag, self.obj237.graphObject_.tag, [311.0, 140.0, 250.75, 110.75], 2, 0))
      self.obj236.out_connections_.append(self.obj234)
      self.obj234.in_connections_.append(self.obj236)
      self.obj236.graphObject_.pendingConnections.append((self.obj236.graphObject_.tag, self.obj234.graphObject_.tag, [117.0, 102.0, 250.75, 110.75], 2, 0))
      self.obj237.out_connections_.append(self.obj238)
      self.obj238.in_connections_.append(self.obj237)
      self.obj237.graphObject_.pendingConnections.append((self.obj237.graphObject_.tag, self.obj238.graphObject_.tag, [311.0, 185.0, 258.5, 259.0], 2, 0))
      self.obj237.out_connections_.append(self.obj239)
      self.obj239.in_connections_.append(self.obj237)
      self.obj237.graphObject_.pendingConnections.append((self.obj237.graphObject_.tag, self.obj239.graphObject_.tag, [311.0, 140.0, 358.5, 131.0], 0, True))
      self.obj238.out_connections_.append(self.obj235)
      self.obj235.in_connections_.append(self.obj238)
      self.obj238.graphObject_.pendingConnections.append((self.obj238.graphObject_.tag, self.obj235.graphObject_.tag, [134.0, 290.0, 258.5, 259.0], 2, 0))
      self.obj239.out_connections_.append(self.obj231)
      self.obj231.in_connections_.append(self.obj239)
      self.obj239.graphObject_.pendingConnections.append((self.obj239.graphObject_.tag, self.obj231.graphObject_.tag, [406.0, 122.0, 358.5, 131.0], 0, True))

   def condition(self, graphID, isograph, atom3i):
      print '======> GenAux1 Condition'
      a = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      aN = a.name.getValue()
      #print a.name.getValue()+' has att AUX : '+str( hasattr(a, "AUX") )
      r = self.getMatched(graphID, self.LHS.nodeWithLabel(2))
      Rn = r.name.getValue()
      g = self.getMatched(graphID, self.LHS.nodeWithLabel(3))
      Gn = g.name.getValue()
      # add list to the Agent Node
      if not hasattr(a,'markedNode') : 
      	a.markedNode = []
      	print 'add List to '+aN
      
      print 'CHeck if '+aN+'Have'
      for ele in a.markedNode : 
          if ele == (Rn,Gn) : return False
      return True
      #        print 'Check if '+aN+'Have '
      #        for ele in a.markedNode : 
      #            if ele == (Rn,Gn) : return False 
      #        return True
      
      

   def action(self, graphID, isograph, atom3i):
      print '======> GenAux1 ACtion'
      a = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      aN = a.name.getValue()
      #print a.name.getValue()+' has att AUX : '+str( hasattr(a, "AUX") )
      r = self.getMatched(graphID, self.LHS.nodeWithLabel(2))
      Rn = r.name.getValue()
      g = self.getMatched(graphID, self.LHS.nodeWithLabel(3))
      Gn = g.name.getValue()
      # add ele list to the Agent Node
      print 'Add Ele into list of '+aN
      a.markedNode.append( (Rn,Gn) )
      print 'List of MarkedNode'
      for ele in a.markedNode : 
      	print ele
      

