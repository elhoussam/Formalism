"""
__omacsMODELsimple_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: sam
Modified: Fri Feb 17 14:40:01 2017
______________________________________________________________________________
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
from operatingUnit import *
from metarial import *
from fromMaterial import *
from intoMaterial import *
from graph_posses import *
from graph_operatingUnit import *
from graph_achieve import *
from graph_Goal import *
from graph_Agent import *
from graph_Capabilitie import *
from graph_intoMaterial import *
from graph_metarial import *
from graph_requir import *
from graph_fromMaterial import *
from graph_Role import *
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

def omacsMODELsimple_MDL(self, rootNode, omacssRootNode=None, pns2RootNode=None):

    # --- Generating attributes code for ASG omacss ---
    if( omacssRootNode ): 
        # author
        omacssRootNode.author.setValue('houssam')

        # description
        omacssRootNode.description.setValue('\n')
        omacssRootNode.description.setHeight(15)

        # name
        omacssRootNode.name.setValue('SMA')
    # --- ASG attributes over ---


    # --- Generating attributes code for ASG pns2 ---
    if( pns2RootNode ): 
        # author
        pns2RootNode.author.setValue('Annonymous')

        # description
        pns2RootNode.description.setValue('\n')
        pns2RootNode.description.setHeight(15)

        # name
        pns2RootNode.name.setValue('')
        pns2RootNode.name.setNone()
    # --- ASG attributes over ---


    self.obj24=Agent(self)
    self.obj24.isGraphObjectVisual = True

    if(hasattr(self.obj24, '_setHierarchicalLink')):
      self.obj24._setHierarchicalLink(False)

    # price
    self.obj24.price.setValue(0)

    # name
    self.obj24.name.setValue('a')

    self.obj24.graphClass_= graph_Agent
    if self.genGraphics:
       new_obj = graph_Agent(280.0,40.0,self.obj24)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Agent", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj24.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj24)
    self.globalAndLocalPostcondition(self.obj24, rootNode)
    self.obj24.postAction( rootNode.CREATE )

    self.obj25=Capabilitie(self)
    self.obj25.isGraphObjectVisual = True

    if(hasattr(self.obj25, '_setHierarchicalLink')):
      self.obj25._setHierarchicalLink(False)

    # name
    self.obj25.name.setValue('c')

    self.obj25.graphClass_= graph_Capabilitie
    if self.genGraphics:
       new_obj = graph_Capabilitie(280.0,180.0,self.obj25)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Capabilitie", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj25.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj25)
    self.globalAndLocalPostcondition(self.obj25, rootNode)
    self.obj25.postAction( rootNode.CREATE )

    self.obj26=Role(self)
    self.obj26.isGraphObjectVisual = True

    if(hasattr(self.obj26, '_setHierarchicalLink')):
      self.obj26._setHierarchicalLink(False)

    # name
    self.obj26.name.setValue('r')

    self.obj26.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(280.0,280.0,self.obj26)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj26.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj26)
    self.globalAndLocalPostcondition(self.obj26, rootNode)
    self.obj26.postAction( rootNode.CREATE )

    self.obj27=Goal(self)
    self.obj27.isGraphObjectVisual = True

    if(hasattr(self.obj27, '_setHierarchicalLink')):
      self.obj27._setHierarchicalLink(False)

    # name
    self.obj27.name.setValue('g')

    self.obj27.graphClass_= graph_Goal
    if self.genGraphics:
       new_obj = graph_Goal(300.0,400.0,self.obj27)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Goal", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj27.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj27)
    self.globalAndLocalPostcondition(self.obj27, rootNode)
    self.obj27.postAction( rootNode.CREATE )

    self.obj28=posses(self)
    self.obj28.isGraphObjectVisual = True

    if(hasattr(self.obj28, '_setHierarchicalLink')):
      self.obj28._setHierarchicalLink(False)

    # rate
    self.obj28.rate.setValue(0.0)

    self.obj28.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(303.0,140.5,self.obj28)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj28.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj28)
    self.globalAndLocalPostcondition(self.obj28, rootNode)
    self.obj28.postAction( rootNode.CREATE )

    self.obj29=achieve(self)
    self.obj29.isGraphObjectVisual = True

    if(hasattr(self.obj29, '_setHierarchicalLink')):
      self.obj29._setHierarchicalLink(False)

    # rate
    self.obj29.rate.setValue(0.0)

    self.obj29.graphClass_= graph_achieve
    if self.genGraphics:
       new_obj = graph_achieve(313.5,363.5,self.obj29)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("achieve", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj29.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj29)
    self.globalAndLocalPostcondition(self.obj29, rootNode)
    self.obj29.postAction( rootNode.CREATE )

    self.obj30=requir(self)
    self.obj30.isGraphObjectVisual = True

    if(hasattr(self.obj30, '_setHierarchicalLink')):
      self.obj30._setHierarchicalLink(False)

    self.obj30.graphClass_= graph_requir
    if self.genGraphics:
       new_obj = graph_requir(302.5,250.0,self.obj30)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("requir", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj30.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj30)
    self.globalAndLocalPostcondition(self.obj30, rootNode)
    self.obj30.postAction( rootNode.CREATE )

    self.obj40=operatingUnit(self)
    self.obj40.isGraphObjectVisual = True

    if(hasattr(self.obj40, '_setHierarchicalLink')):
      self.obj40._setHierarchicalLink(False)

    # name
    self.obj40.name.setValue('')
    self.obj40.name.setNone()

    self.obj40.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(640.0,100.0,self.obj40)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj40.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj40)
    self.globalAndLocalPostcondition(self.obj40, rootNode)
    self.obj40.postAction( rootNode.CREATE )

    self.obj39=metarial(self)
    self.obj39.isGraphObjectVisual = True

    if(hasattr(self.obj39, '_setHierarchicalLink')):
      self.obj39._setHierarchicalLink(False)

    # Name
    self.obj39.Name.setValue('')
    self.obj39.Name.setNone()

    self.obj39.graphClass_= graph_metarial
    if self.genGraphics:
       new_obj = graph_metarial(680.0,80.0,self.obj39)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("metarial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj39.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj39)
    self.globalAndLocalPostcondition(self.obj39, rootNode)
    self.obj39.postAction( rootNode.CREATE )

    self.obj42=fromMaterial(self)
    self.obj42.isGraphObjectVisual = True

    if(hasattr(self.obj42, '_setHierarchicalLink')):
      self.obj42._setHierarchicalLink(False)

    # rate
    self.obj42.rate.setValue(0.0)

    self.obj42.graphClass_= graph_fromMaterial
    if self.genGraphics:
       new_obj = graph_fromMaterial(706.448598131,151.5,self.obj42)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj42.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42)
    self.globalAndLocalPostcondition(self.obj42, rootNode)
    self.obj42.postAction( rootNode.CREATE )

    self.obj41=intoMaterial(self)
    self.obj41.isGraphObjectVisual = True

    if(hasattr(self.obj41, '_setHierarchicalLink')):
      self.obj41._setHierarchicalLink(False)

    # rate
    self.obj41.rate.setValue(0.0)

    self.obj41.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(661.0,43.0,self.obj41)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj41.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj41)
    self.globalAndLocalPostcondition(self.obj41, rootNode)
    self.obj41.postAction( rootNode.CREATE )

    # Connections for obj24 (graphObject_: Obj0) named a
    self.drawConnections(
(self.obj24,self.obj28,[305.0, 102.0, 303.0, 140.5],"true", 2) )
    # Connections for obj25 (graphObject_: Obj1) named c
    self.drawConnections(
 )
    # Connections for obj26 (graphObject_: Obj2) named r
    self.drawConnections(
(self.obj26,self.obj30,[304.0, 281.0, 302.5, 250.0],"true", 2),
(self.obj26,self.obj29,[304.0, 326.0, 313.5, 363.5],"true", 2) )
    # Connections for obj27 (graphObject_: Obj3) named g
    self.drawConnections(
 )
    # Connections for obj28 (graphObject_: Obj4) of type posses
    self.drawConnections(
(self.obj28,self.obj25,[303.0, 140.5, 301.0, 179.0],"true", 2) )
    # Connections for obj29 (graphObject_: Obj6) of type achieve
    self.drawConnections(
(self.obj29,self.obj27,[313.5, 363.5, 323.0, 401.0],"true", 2) )
    # Connections for obj30 (graphObject_: Obj8) of type requir
    self.drawConnections(
(self.obj30,self.obj25,[302.5, 250.0, 301.0, 219.0],"true", 2) )
    # Connections for obj40 (graphObject_: Obj10) named 
    self.drawConnections(
(self.obj40,self.obj41,[653.5700934579439, 108.42105263157895, 618.0, 43.0, 661.0, 43.0],"true", 3) )
    # Connections for obj39 (graphObject_: Obj9) of type metarial
    self.drawConnections(
(self.obj39,self.obj42,[704.0, 130.0, 711.5, 155.0, 706.4485981308411, 151.5],"true", 3) )
    # Connections for obj42 (graphObject_: Obj13) of type fromMaterial
    self.drawConnections(
(self.obj42,self.obj40,[706.4485981308411, 151.5, 701.3971962616822, 148.0, 683.7943925233645, 116.0],"true", 3) )
    # Connections for obj41 (graphObject_: Obj11) of type intoMaterial
    self.drawConnections(
(self.obj41,self.obj39,[661.0, 43.0, 704.0, 43.0, 707.0, 81.0],"true", 3) )

newfunction = omacsMODELsimple_MDL

loadedMMName = ['omacss_META', 'pns2_META']

atom3version = '0.3'
