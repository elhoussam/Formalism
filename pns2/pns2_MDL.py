"""
__pns2_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: sam
Modified: Fri Feb 17 12:40:28 2017
__________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from Agent import *
from Capabilitie import *
from Role import *
from Goal import *
from posses import *
from achieve import *
from requir import *
from graph_posses import *
from graph_achieve import *
from graph_Goal import *
from graph_Role import *
from graph_Capabilitie import *
from graph_requir import *
from graph_Agent import *
from ATOM3Enum import *
from ATOM3String import *
from ATOM3BottomType import *
from ATOM3Constraint import *
from ATOM3Attribute import *
from ATOM3Float import *
from ATOM3List import *
from ATOM3Link import *
from ATOM3Connection import *
from ATOM3Boolean import *
from ATOM3Appearance import *
from ATOM3Text import *
from ATOM3Action import *
from ATOM3Integer import *
from ATOM3Port import *
from ATOM3MSEnum import *

def pns2_MDL(self, rootNode, omacssRootNode=None):

    # --- Generating attributes code for ASG omacss ---
    if( omacssRootNode ): 
        # author
        omacssRootNode.author.setValue('Annonymous')

        # description
        omacssRootNode.description.setValue('\n')
        omacssRootNode.description.setHeight(15)

        # name
        omacssRootNode.name.setValue('')
        omacssRootNode.name.setNone()
    # --- ASG attributes over ---


    self.obj51=Agent(self)
    self.obj51.isGraphObjectVisual = True

    if(hasattr(self.obj51, '_setHierarchicalLink')):
      self.obj51._setHierarchicalLink(False)

    # price
    self.obj51.price.setValue(0)

    # name
    self.obj51.name.setValue('A1')

    self.obj51.graphClass_= graph_Agent
    if self.genGraphics:
       new_obj = graph_Agent(220.0,80.0,self.obj51)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Agent", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj51.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj51)
    self.globalAndLocalPostcondition(self.obj51, rootNode)
    self.obj51.postAction( rootNode.CREATE )

    self.obj52=Agent(self)
    self.obj52.isGraphObjectVisual = True

    if(hasattr(self.obj52, '_setHierarchicalLink')):
      self.obj52._setHierarchicalLink(False)

    # price
    self.obj52.price.setValue(0)

    # name
    self.obj52.name.setValue('A2')

    self.obj52.graphClass_= graph_Agent
    if self.genGraphics:
       new_obj = graph_Agent(340.0,40.0,self.obj52)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Agent", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj52.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52)
    self.globalAndLocalPostcondition(self.obj52, rootNode)
    self.obj52.postAction( rootNode.CREATE )

    self.obj53=Agent(self)
    self.obj53.isGraphObjectVisual = True

    if(hasattr(self.obj53, '_setHierarchicalLink')):
      self.obj53._setHierarchicalLink(False)

    # price
    self.obj53.price.setValue(0)

    # name
    self.obj53.name.setValue('A3')

    self.obj53.graphClass_= graph_Agent
    if self.genGraphics:
       new_obj = graph_Agent(440.0,80.0,self.obj53)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Agent", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj53.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj53)
    self.globalAndLocalPostcondition(self.obj53, rootNode)
    self.obj53.postAction( rootNode.CREATE )

    self.obj54=Capabilitie(self)
    self.obj54.isGraphObjectVisual = True

    if(hasattr(self.obj54, '_setHierarchicalLink')):
      self.obj54._setHierarchicalLink(False)

    # name
    self.obj54.name.setValue('C1')

    self.obj54.graphClass_= graph_Capabilitie
    if self.genGraphics:
       new_obj = graph_Capabilitie(220.0,200.0,self.obj54)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Capabilitie", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj54.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj54)
    self.globalAndLocalPostcondition(self.obj54, rootNode)
    self.obj54.postAction( rootNode.CREATE )

    self.obj55=Capabilitie(self)
    self.obj55.isGraphObjectVisual = True

    if(hasattr(self.obj55, '_setHierarchicalLink')):
      self.obj55._setHierarchicalLink(False)

    # name
    self.obj55.name.setValue('C2')

    self.obj55.graphClass_= graph_Capabilitie
    if self.genGraphics:
       new_obj = graph_Capabilitie(320.0,220.0,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Capabilitie", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj55.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)
    self.obj55.postAction( rootNode.CREATE )

    self.obj56=Capabilitie(self)
    self.obj56.isGraphObjectVisual = True

    if(hasattr(self.obj56, '_setHierarchicalLink')):
      self.obj56._setHierarchicalLink(False)

    # name
    self.obj56.name.setValue('C3')

    self.obj56.graphClass_= graph_Capabilitie
    if self.genGraphics:
       new_obj = graph_Capabilitie(440.0,200.0,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Capabilitie", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj56.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)
    self.obj56.postAction( rootNode.CREATE )

    self.obj63=Role(self)
    self.obj63.isGraphObjectVisual = True

    if(hasattr(self.obj63, '_setHierarchicalLink')):
      self.obj63._setHierarchicalLink(False)

    # name
    self.obj63.name.setValue('R2')

    self.obj63.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(340.0,360.0,self.obj63)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63)
    self.globalAndLocalPostcondition(self.obj63, rootNode)
    self.obj63.postAction( rootNode.CREATE )

    self.obj66=Role(self)
    self.obj66.isGraphObjectVisual = True

    if(hasattr(self.obj66, '_setHierarchicalLink')):
      self.obj66._setHierarchicalLink(False)

    # name
    self.obj66.name.setValue('R1')

    self.obj66.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(240.0,340.0,self.obj66)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj66.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj66)
    self.globalAndLocalPostcondition(self.obj66, rootNode)
    self.obj66.postAction( rootNode.CREATE )

    self.obj69=Goal(self)
    self.obj69.isGraphObjectVisual = True

    if(hasattr(self.obj69, '_setHierarchicalLink')):
      self.obj69._setHierarchicalLink(False)

    # name
    self.obj69.name.setValue('G1')

    self.obj69.graphClass_= graph_Goal
    if self.genGraphics:
       new_obj = graph_Goal(120.0,380.0,self.obj69)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Goal", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj69.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj69)
    self.globalAndLocalPostcondition(self.obj69, rootNode)
    self.obj69.postAction( rootNode.CREATE )

    self.obj70=Goal(self)
    self.obj70.isGraphObjectVisual = True

    if(hasattr(self.obj70, '_setHierarchicalLink')):
      self.obj70._setHierarchicalLink(False)

    # name
    self.obj70.name.setValue('G2')

    self.obj70.graphClass_= graph_Goal
    if self.genGraphics:
       new_obj = graph_Goal(460.0,400.0,self.obj70)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Goal", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj70.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj70)
    self.globalAndLocalPostcondition(self.obj70, rootNode)
    self.obj70.postAction( rootNode.CREATE )

    self.obj57=posses(self)
    self.obj57.isGraphObjectVisual = True

    if(hasattr(self.obj57, '_setHierarchicalLink')):
      self.obj57._setHierarchicalLink(False)

    # rate
    self.obj57.rate.setValue(0.0)

    self.obj57.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(243.0,170.5,self.obj57)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj57.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj57)
    self.globalAndLocalPostcondition(self.obj57, rootNode)
    self.obj57.postAction( rootNode.CREATE )

    self.obj58=posses(self)
    self.obj58.isGraphObjectVisual = True

    if(hasattr(self.obj58, '_setHierarchicalLink')):
      self.obj58._setHierarchicalLink(False)

    # rate
    self.obj58.rate.setValue(0.0)

    self.obj58.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(293.0,180.5,self.obj58)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj58.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj58)
    self.globalAndLocalPostcondition(self.obj58, rootNode)
    self.obj58.postAction( rootNode.CREATE )

    self.obj59=posses(self)
    self.obj59.isGraphObjectVisual = True

    if(hasattr(self.obj59, '_setHierarchicalLink')):
      self.obj59._setHierarchicalLink(False)

    # rate
    self.obj59.rate.setValue(0.0)

    self.obj59.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(298.0,144.25,self.obj59)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj59.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj59)
    self.globalAndLocalPostcondition(self.obj59, rootNode)
    self.obj59.postAction( rootNode.CREATE )

    self.obj60=posses(self)
    self.obj60.isGraphObjectVisual = True

    if(hasattr(self.obj60, '_setHierarchicalLink')):
      self.obj60._setHierarchicalLink(False)

    # rate
    self.obj60.rate.setValue(0.0)

    self.obj60.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(353.0,160.5,self.obj60)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj60.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj60)
    self.globalAndLocalPostcondition(self.obj60, rootNode)
    self.obj60.postAction( rootNode.CREATE )

    self.obj61=posses(self)
    self.obj61.isGraphObjectVisual = True

    if(hasattr(self.obj61, '_setHierarchicalLink')):
      self.obj61._setHierarchicalLink(False)

    # rate
    self.obj61.rate.setValue(0.0)

    self.obj61.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(413.0,150.5,self.obj61)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj61.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj61)
    self.globalAndLocalPostcondition(self.obj61, rootNode)
    self.obj61.postAction( rootNode.CREATE )

    self.obj62=posses(self)
    self.obj62.isGraphObjectVisual = True

    if(hasattr(self.obj62, '_setHierarchicalLink')):
      self.obj62._setHierarchicalLink(False)

    # rate
    self.obj62.rate.setValue(0.0)

    self.obj62.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(463.0,170.5,self.obj62)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj62.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj62)
    self.globalAndLocalPostcondition(self.obj62, rootNode)
    self.obj62.postAction( rootNode.CREATE )

    self.obj71=achieve(self)
    self.obj71.isGraphObjectVisual = True

    if(hasattr(self.obj71, '_setHierarchicalLink')):
      self.obj71._setHierarchicalLink(False)

    # rate
    self.obj71.rate.setValue(0.0)

    self.obj71.graphClass_= graph_achieve
    if self.genGraphics:
       new_obj = graph_achieve(423.5,403.5,self.obj71)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("achieve", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj71.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj71)
    self.globalAndLocalPostcondition(self.obj71, rootNode)
    self.obj71.postAction( rootNode.CREATE )

    self.obj72=achieve(self)
    self.obj72.isGraphObjectVisual = True

    if(hasattr(self.obj72, '_setHierarchicalLink')):
      self.obj72._setHierarchicalLink(False)

    # rate
    self.obj72.rate.setValue(0.0)

    self.obj72.graphClass_= graph_achieve
    if self.genGraphics:
       new_obj = graph_achieve(203.5,383.5,self.obj72)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("achieve", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj72.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj72)
    self.globalAndLocalPostcondition(self.obj72, rootNode)
    self.obj72.postAction( rootNode.CREATE )

    self.obj64=requir(self)
    self.obj64.isGraphObjectVisual = True

    if(hasattr(self.obj64, '_setHierarchicalLink')):
      self.obj64._setHierarchicalLink(False)

    self.obj64.graphClass_= graph_requir
    if self.genGraphics:
       new_obj = graph_requir(352.5,310.0,self.obj64)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("requir", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj64.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj64)
    self.globalAndLocalPostcondition(self.obj64, rootNode)
    self.obj64.postAction( rootNode.CREATE )

    self.obj65=requir(self)
    self.obj65.isGraphObjectVisual = True

    if(hasattr(self.obj65, '_setHierarchicalLink')):
      self.obj65._setHierarchicalLink(False)

    self.obj65.graphClass_= graph_requir
    if self.genGraphics:
       new_obj = graph_requir(412.5,300.0,self.obj65)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("requir", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj65.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj65)
    self.globalAndLocalPostcondition(self.obj65, rootNode)
    self.obj65.postAction( rootNode.CREATE )

    self.obj67=requir(self)
    self.obj67.isGraphObjectVisual = True

    if(hasattr(self.obj67, '_setHierarchicalLink')):
      self.obj67._setHierarchicalLink(False)

    self.obj67.graphClass_= graph_requir
    if self.genGraphics:
       new_obj = graph_requir(302.5,300.0,self.obj67)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("requir", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj67.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj67)
    self.globalAndLocalPostcondition(self.obj67, rootNode)
    self.obj67.postAction( rootNode.CREATE )

    self.obj68=requir(self)
    self.obj68.isGraphObjectVisual = True

    if(hasattr(self.obj68, '_setHierarchicalLink')):
      self.obj68._setHierarchicalLink(False)

    self.obj68.graphClass_= graph_requir
    if self.genGraphics:
       new_obj = graph_requir(252.5,290.0,self.obj68)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("requir", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj68.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj68)
    self.globalAndLocalPostcondition(self.obj68, rootNode)
    self.obj68.postAction( rootNode.CREATE )

    # Connections for obj51 (graphObject_: Obj12) named A1
    self.drawConnections(
(self.obj51,self.obj57,[245.0, 142.0, 243.0, 170.5],"true", 2),
(self.obj51,self.obj58,[245.0, 142.0, 293.0, 180.5],"true", 2) )
    # Connections for obj52 (graphObject_: Obj13) named A2
    self.drawConnections(
(self.obj52,self.obj59,[365.0, 102.0, 329.0, 120.0, 298.0, 144.25],"true", 3),
(self.obj52,self.obj60,[365.0, 102.0, 353.0, 160.5],"true", 2),
(self.obj52,self.obj61,[365.0, 102.0, 413.0, 150.5],"true", 2) )
    # Connections for obj53 (graphObject_: Obj14) named A3
    self.drawConnections(
(self.obj53,self.obj62,[465.0, 142.0, 463.0, 170.5],"true", 2) )
    # Connections for obj54 (graphObject_: Obj15) named C1
    self.drawConnections(
 )
    # Connections for obj55 (graphObject_: Obj16) named C2
    self.drawConnections(
 )
    # Connections for obj56 (graphObject_: Obj17) named C3
    self.drawConnections(
 )
    # Connections for obj63 (graphObject_: Obj30) named R2
    self.drawConnections(
(self.obj63,self.obj64,[364.0, 361.0, 352.5, 310.0],"true", 2),
(self.obj63,self.obj65,[364.0, 361.0, 412.5, 300.0],"true", 2),
(self.obj63,self.obj71,[364.0, 406.0, 423.5, 403.5],"true", 2) )
    # Connections for obj66 (graphObject_: Obj33) named R1
    self.drawConnections(
(self.obj66,self.obj67,[264.0, 341.0, 302.5, 300.0],"true", 2),
(self.obj66,self.obj68,[264.0, 341.0, 252.5, 290.0],"true", 2),
(self.obj66,self.obj72,[264.0, 386.0, 203.5, 383.5],"true", 2) )
    # Connections for obj69 (graphObject_: Obj36) named G1
    self.drawConnections(
 )
    # Connections for obj70 (graphObject_: Obj37) named G2
    self.drawConnections(
 )
    # Connections for obj57 (graphObject_: Obj18) of type posses
    self.drawConnections(
(self.obj57,self.obj54,[243.0, 170.5, 241.0, 199.0],"true", 2) )
    # Connections for obj58 (graphObject_: Obj20) of type posses
    self.drawConnections(
(self.obj58,self.obj55,[293.0, 180.5, 341.0, 219.0],"true", 2) )
    # Connections for obj59 (graphObject_: Obj22) of type posses
    self.drawConnections(
(self.obj59,self.obj54,[298.0, 144.25, 267.0, 168.5, 241.0, 199.0],"true", 3) )
    # Connections for obj60 (graphObject_: Obj24) of type posses
    self.drawConnections(
(self.obj60,self.obj55,[353.0, 160.5, 341.0, 219.0],"true", 2) )
    # Connections for obj61 (graphObject_: Obj26) of type posses
    self.drawConnections(
(self.obj61,self.obj56,[413.0, 150.5, 461.0, 199.0],"true", 2) )
    # Connections for obj62 (graphObject_: Obj28) of type posses
    self.drawConnections(
(self.obj62,self.obj56,[463.0, 170.5, 461.0, 199.0],"true", 2) )
    # Connections for obj71 (graphObject_: Obj38) of type achieve
    self.drawConnections(
(self.obj71,self.obj70,[423.5, 403.5, 483.0, 401.0],"true", 2) )
    # Connections for obj72 (graphObject_: Obj40) of type achieve
    self.drawConnections(
(self.obj72,self.obj69,[203.5, 383.5, 143.0, 381.0],"true", 2) )
    # Connections for obj64 (graphObject_: Obj31) of type requir
    self.drawConnections(
(self.obj64,self.obj55,[352.5, 310.0, 341.0, 259.0],"true", 2) )
    # Connections for obj65 (graphObject_: Obj32) of type requir
    self.drawConnections(
(self.obj65,self.obj56,[412.5, 300.0, 461.0, 239.0],"true", 2) )
    # Connections for obj67 (graphObject_: Obj34) of type requir
    self.drawConnections(
(self.obj67,self.obj55,[302.5, 300.0, 341.0, 259.0],"true", 2) )
    # Connections for obj68 (graphObject_: Obj35) of type requir
    self.drawConnections(
(self.obj68,self.obj54,[252.5, 290.0, 241.0, 239.0],"true", 2) )

newfunction = pns2_MDL

loadedMMName = 'omacss_META'

atom3version = '0.3'
