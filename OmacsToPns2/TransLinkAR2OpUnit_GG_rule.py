# _ TransLinkAR2OpUnit_GG_rule.py ____________________________________________________________________________
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
from GenericGraphEdge import *
from ASG_pns import *
from metarial import *
from GenericGraphNode import *
from rawMaterial import *
from fromMaterial import *
from intoProduct import *
from fromRaw import *
from ASG_GenericGraph import *
from intoMaterial import *
from product import *
from operatingUnit import *
class TransLinkAR2OpUnit_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 10)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_omacs(parent)

      self.obj621=Agent(parent)
      self.obj621.preAction( self.LHS.CREATE )
      self.obj621.isGraphObjectVisual = True

      if(hasattr(self.obj621, '_setHierarchicalLink')):
        self.obj621._setHierarchicalLink(False)

      # price
      self.obj621.price.setNone()

      # name
      self.obj621.name.setValue('')
      self.obj621.name.setNone()

      self.obj621.GGLabel.setValue(1)
      self.obj621.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(60.0,40.0,self.obj621)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj621.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj621)
      self.obj621.postAction( self.LHS.CREATE )

      self.obj622=Role(parent)
      self.obj622.preAction( self.LHS.CREATE )
      self.obj622.isGraphObjectVisual = True

      if(hasattr(self.obj622, '_setHierarchicalLink')):
        self.obj622._setHierarchicalLink(False)

      # name
      self.obj622.name.setValue('')
      self.obj622.name.setNone()

      self.obj622.GGLabel.setValue(2)
      self.obj622.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(320.0,220.0,self.obj622)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj622.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj622)
      self.obj622.postAction( self.LHS.CREATE )

      self.obj623=CapableOf(parent)
      self.obj623.preAction( self.LHS.CREATE )
      self.obj623.isGraphObjectVisual = True

      if(hasattr(self.obj623, '_setHierarchicalLink')):
        self.obj623._setHierarchicalLink(False)

      # rate
      self.obj623.rate.setNone()

      self.obj623.GGLabel.setValue(3)
      self.obj623.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(230.0,173.0,self.obj623)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj623.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj623)
      self.obj623.postAction( self.LHS.CREATE )

      self.obj621.out_connections_.append(self.obj623)
      self.obj623.in_connections_.append(self.obj621)
      self.obj621.graphObject_.pendingConnections.append((self.obj621.graphObject_.tag, self.obj623.graphObject_.tag, [85.0, 102.0, 117.0, 188.0, 230.0, 173.0], 2, True))
      self.obj623.out_connections_.append(self.obj622)
      self.obj622.in_connections_.append(self.obj623)
      self.obj623.graphObject_.pendingConnections.append((self.obj623.graphObject_.tag, self.obj622.graphObject_.tag, [344.0, 221.0, 343.0, 158.0, 230.0, 173.0], 2, True))

      self.RHS = ASG_omacs(parent)
      self.RHS.merge(ASG_pns(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj627=Agent(parent)
      self.obj627.preAction( self.RHS.CREATE )
      self.obj627.isGraphObjectVisual = True

      if(hasattr(self.obj627, '_setHierarchicalLink')):
        self.obj627._setHierarchicalLink(False)

      # price
      self.obj627.price.setNone()

      # name
      self.obj627.name.setValue('')
      self.obj627.name.setNone()

      self.obj627.GGLabel.setValue(1)
      self.obj627.graphClass_= graph_Agent
      if parent.genGraphics:
         new_obj = graph_Agent(60.0,40.0,self.obj627)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj627.graphObject_ = new_obj
      self.obj6270= AttrCalc()
      self.obj6270.Copy=ATOM3Boolean()
      self.obj6270.Copy.setValue(('Copy from LHS', 1))
      self.obj6270.Copy.config = 0
      self.obj6270.Specify=ATOM3Constraint()
      self.obj6270.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj627.GGset2Any['price']= self.obj6270
      self.obj6271= AttrCalc()
      self.obj6271.Copy=ATOM3Boolean()
      self.obj6271.Copy.setValue(('Copy from LHS', 1))
      self.obj6271.Copy.config = 0
      self.obj6271.Specify=ATOM3Constraint()
      self.obj6271.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj627.GGset2Any['name']= self.obj6271

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj627)
      self.obj627.postAction( self.RHS.CREATE )

      self.obj628=Role(parent)
      self.obj628.preAction( self.RHS.CREATE )
      self.obj628.isGraphObjectVisual = True

      if(hasattr(self.obj628, '_setHierarchicalLink')):
        self.obj628._setHierarchicalLink(False)

      # name
      self.obj628.name.setValue('')
      self.obj628.name.setNone()

      self.obj628.GGLabel.setValue(2)
      self.obj628.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(320.0,220.0,self.obj628)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj628.graphObject_ = new_obj
      self.obj6280= AttrCalc()
      self.obj6280.Copy=ATOM3Boolean()
      self.obj6280.Copy.setValue(('Copy from LHS', 1))
      self.obj6280.Copy.config = 0
      self.obj6280.Specify=ATOM3Constraint()
      self.obj6280.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj628.GGset2Any['name']= self.obj6280

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj628)
      self.obj628.postAction( self.RHS.CREATE )

      self.obj629=CapableOf(parent)
      self.obj629.preAction( self.RHS.CREATE )
      self.obj629.isGraphObjectVisual = True

      if(hasattr(self.obj629, '_setHierarchicalLink')):
        self.obj629._setHierarchicalLink(False)

      # rate
      self.obj629.rate.setNone()

      self.obj629.GGLabel.setValue(3)
      self.obj629.graphClass_= graph_CapableOf
      if parent.genGraphics:
         new_obj = graph_CapableOf(230.0,173.0,self.obj629)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj629.graphObject_ = new_obj
      self.obj6290= AttrCalc()
      self.obj6290.Copy=ATOM3Boolean()
      self.obj6290.Copy.setValue(('Copy from LHS', 1))
      self.obj6290.Copy.config = 0
      self.obj6290.Specify=ATOM3Constraint()
      self.obj6290.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj629.GGset2Any['rate']= self.obj6290

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj629)
      self.obj629.postAction( self.RHS.CREATE )

      self.obj630=operatingUnit(parent)
      self.obj630.preAction( self.RHS.CREATE )
      self.obj630.isGraphObjectVisual = True

      if(hasattr(self.obj630, '_setHierarchicalLink')):
        self.obj630._setHierarchicalLink(False)

      # OperCostProp
      self.obj630.OperCostProp.setValue(0.0)

      # name
      self.obj630.name.setValue('')
      self.obj630.name.setNone()

      # OperCostFix
      self.obj630.OperCostFix.setValue(0.0)

      self.obj630.GGLabel.setValue(5)
      self.obj630.graphClass_= graph_operatingUnit
      if parent.genGraphics:
         new_obj = graph_operatingUnit(60.0,220.0,self.obj630)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj630.graphObject_ = new_obj
      self.obj6300= AttrCalc()
      self.obj6300.Copy=ATOM3Boolean()
      self.obj6300.Copy.setValue(('Copy from LHS', 1))
      self.obj6300.Copy.config = 0
      self.obj6300.Specify=ATOM3Constraint()
      self.obj6300.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj630.GGset2Any['OperCostProp']= self.obj6300
      self.obj6301= AttrCalc()
      self.obj6301.Copy=ATOM3Boolean()
      self.obj6301.Copy.setValue(('Copy from LHS', 0))
      self.obj6301.Copy.config = 0
      self.obj6301.Specify=ATOM3Constraint()
      self.obj6301.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).name.getValue()+\' \'+self.getMatched(graphID, self.LHS.nodeWithLabel(2)).name.getValue()\n\n\n\n'))
      self.obj630.GGset2Any['name']= self.obj6301
      self.obj6302= AttrCalc()
      self.obj6302.Copy=ATOM3Boolean()
      self.obj6302.Copy.setValue(('Copy from LHS', 1))
      self.obj6302.Copy.config = 0
      self.obj6302.Specify=ATOM3Constraint()
      self.obj6302.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj630.GGset2Any['OperCostFix']= self.obj6302

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj630)
      self.obj630.postAction( self.RHS.CREATE )

      self.obj631=GenericGraphEdge(parent)
      self.obj631.preAction( self.RHS.CREATE )
      self.obj631.isGraphObjectVisual = True

      if(hasattr(self.obj631, '_setHierarchicalLink')):
        self.obj631._setHierarchicalLink(False)

      self.obj631.GGLabel.setValue(6)
      self.obj631.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(103.5,161.5,self.obj631)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj631.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj631)
      self.obj631.postAction( self.RHS.CREATE )

      self.obj627.out_connections_.append(self.obj629)
      self.obj629.in_connections_.append(self.obj627)
      self.obj627.graphObject_.pendingConnections.append((self.obj627.graphObject_.tag, self.obj629.graphObject_.tag, [97.0, 102.0, 230.0, 173.0], 2, 0))
      self.obj627.out_connections_.append(self.obj631)
      self.obj631.in_connections_.append(self.obj627)
      self.obj627.graphObject_.pendingConnections.append((self.obj627.graphObject_.tag, self.obj631.graphObject_.tag, [97.0, 102.0, 103.5, 161.5], 0, True))
      self.obj629.out_connections_.append(self.obj628)
      self.obj628.in_connections_.append(self.obj629)
      self.obj629.graphObject_.pendingConnections.append((self.obj629.graphObject_.tag, self.obj628.graphObject_.tag, [351.0, 220.0, 230.0, 173.0], 2, 0))
      self.obj631.out_connections_.append(self.obj630)
      self.obj630.in_connections_.append(self.obj631)
      self.obj631.graphObject_.pendingConnections.append((self.obj631.graphObject_.tag, self.obj630.graphObject_.tag, [110.0, 221.0, 103.5, 161.5], 0, True))

   def condition(self, graphID, isograph, atom3i):
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      node2 = self.getMatched(graphID, self.LHS.nodeWithLabel(2))
      print node.name.getValue()+' '+node2.name.getValue()
      # remplaceed by  "LinkAR2OpUnit"
      return not(  hasattr(node,node2.name.getValue()+'7') and hasattr(node2, node.name.getValue()+'7') )
      
      

   def action(self, graphID, isograph, atom3i):
      node = self.getMatched ( graphID , self.LHS.nodeWithLabel(1) )
      
      node2 = self.getMatched ( graphID , self.LHS.nodeWithLabel(2) )
      setattr( node ,node2.name.getValue()+'7' ,True )
      setattr( node2 ,node.name.getValue()+'7' ,True )
      
      
      

