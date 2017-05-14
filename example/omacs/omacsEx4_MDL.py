"""
__omacsEx4_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: sam
Modified: Sat May 13 07:32:21 2017
______________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from Goal import *
from require import *
from Agent import *
from Capabilitie import *
from Role import *
from achieve import *
from posses import *
from graph_posses import *
from graph_require import *
from graph_achieve import *
from graph_Goal import *
from graph_Role import *
from graph_Capabilitie import *
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

def omacsEx4_MDL(self, rootNode, omacsRootNode=None):

    # --- Generating attributes code for ASG omacs ---
    if( omacsRootNode ): 
        # author
        omacsRootNode.author.setValue('Annonymous')

        # description
        omacsRootNode.description.setValue('\n')
        omacsRootNode.description.setHeight(15)

        # name
        omacsRootNode.name.setValue('')
        omacsRootNode.name.setNone()
    # --- ASG attributes over ---


    self.obj149=Goal(self)
    self.obj149.isGraphObjectVisual = True

    if(hasattr(self.obj149, '_setHierarchicalLink')):
      self.obj149._setHierarchicalLink(False)

    # name
    self.obj149.name.setValue('G1')

    self.obj149.graphClass_= graph_Goal
    if self.genGraphics:
       new_obj = graph_Goal(19.0,505.0,self.obj149)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Goal", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj149.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj149)
    self.globalAndLocalPostcondition(self.obj149, rootNode)
    self.obj149.postAction( rootNode.CREATE )

    self.obj150=Goal(self)
    self.obj150.isGraphObjectVisual = True

    if(hasattr(self.obj150, '_setHierarchicalLink')):
      self.obj150._setHierarchicalLink(False)

    # name
    self.obj150.name.setValue('G2')

    self.obj150.graphClass_= graph_Goal
    if self.genGraphics:
       new_obj = graph_Goal(199.0,505.0,self.obj150)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Goal", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj150.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj150)
    self.globalAndLocalPostcondition(self.obj150, rootNode)
    self.obj150.postAction( rootNode.CREATE )

    self.obj151=Goal(self)
    self.obj151.isGraphObjectVisual = True

    if(hasattr(self.obj151, '_setHierarchicalLink')):
      self.obj151._setHierarchicalLink(False)

    # name
    self.obj151.name.setValue('G3')

    self.obj151.graphClass_= graph_Goal
    if self.genGraphics:
       new_obj = graph_Goal(339.0,505.0,self.obj151)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Goal", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj151.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj151)
    self.globalAndLocalPostcondition(self.obj151, rootNode)
    self.obj151.postAction( rootNode.CREATE )

    self.obj152=Goal(self)
    self.obj152.isGraphObjectVisual = True

    if(hasattr(self.obj152, '_setHierarchicalLink')):
      self.obj152._setHierarchicalLink(False)

    # name
    self.obj152.name.setValue('G4')

    self.obj152.graphClass_= graph_Goal
    if self.genGraphics:
       new_obj = graph_Goal(479.0,505.0,self.obj152)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Goal", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj152.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj152)
    self.globalAndLocalPostcondition(self.obj152, rootNode)
    self.obj152.postAction( rootNode.CREATE )

    self.obj171=require(self)
    self.obj171.isGraphObjectVisual = True

    if(hasattr(self.obj171, '_setHierarchicalLink')):
      self.obj171._setHierarchicalLink(False)

    self.obj171.graphClass_= graph_require
    if self.genGraphics:
       new_obj = graph_require(135.75,317.5,self.obj171)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("require", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj171.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj171)
    self.globalAndLocalPostcondition(self.obj171, rootNode)
    self.obj171.postAction( rootNode.CREATE )

    self.obj172=require(self)
    self.obj172.isGraphObjectVisual = True

    if(hasattr(self.obj172, '_setHierarchicalLink')):
      self.obj172._setHierarchicalLink(False)

    self.obj172.graphClass_= graph_require
    if self.genGraphics:
       new_obj = graph_require(226.25,312.5,self.obj172)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("require", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj172.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj172)
    self.globalAndLocalPostcondition(self.obj172, rootNode)
    self.obj172.postAction( rootNode.CREATE )

    self.obj173=require(self)
    self.obj173.isGraphObjectVisual = True

    if(hasattr(self.obj173, '_setHierarchicalLink')):
      self.obj173._setHierarchicalLink(False)

    self.obj173.graphClass_= graph_require
    if self.genGraphics:
       new_obj = graph_require(309.25,323.0,self.obj173)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("require", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj173.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj173)
    self.globalAndLocalPostcondition(self.obj173, rootNode)
    self.obj173.postAction( rootNode.CREATE )

    self.obj174=require(self)
    self.obj174.isGraphObjectVisual = True

    if(hasattr(self.obj174, '_setHierarchicalLink')):
      self.obj174._setHierarchicalLink(False)

    self.obj174.graphClass_= graph_require
    if self.genGraphics:
       new_obj = graph_require(444.5,297.0,self.obj174)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("require", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj174.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj174)
    self.globalAndLocalPostcondition(self.obj174, rootNode)
    self.obj174.postAction( rootNode.CREATE )

    self.obj175=require(self)
    self.obj175.isGraphObjectVisual = True

    if(hasattr(self.obj175, '_setHierarchicalLink')):
      self.obj175._setHierarchicalLink(False)

    self.obj175.graphClass_= graph_require
    if self.genGraphics:
       new_obj = graph_require(370.75,323.5,self.obj175)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("require", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj175.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj175)
    self.globalAndLocalPostcondition(self.obj175, rootNode)
    self.obj175.postAction( rootNode.CREATE )

    self.obj176=require(self)
    self.obj176.isGraphObjectVisual = True

    if(hasattr(self.obj176, '_setHierarchicalLink')):
      self.obj176._setHierarchicalLink(False)

    self.obj176.graphClass_= graph_require
    if self.genGraphics:
       new_obj = graph_require(324.25,326.5,self.obj176)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("require", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj176.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj176)
    self.globalAndLocalPostcondition(self.obj176, rootNode)
    self.obj176.postAction( rootNode.CREATE )

    self.obj140=Agent(self)
    self.obj140.isGraphObjectVisual = True

    if(hasattr(self.obj140, '_setHierarchicalLink')):
      self.obj140._setHierarchicalLink(False)

    # price
    self.obj140.price.setValue(85)

    # name
    self.obj140.name.setValue('A1')

    self.obj140.graphClass_= graph_Agent
    if self.genGraphics:
       new_obj = graph_Agent(53.0,9.0,self.obj140)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Agent", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj140.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj140)
    self.globalAndLocalPostcondition(self.obj140, rootNode)
    self.obj140.postAction( rootNode.CREATE )

    self.obj141=Agent(self)
    self.obj141.isGraphObjectVisual = True

    if(hasattr(self.obj141, '_setHierarchicalLink')):
      self.obj141._setHierarchicalLink(False)

    # price
    self.obj141.price.setValue(90)

    # name
    self.obj141.name.setValue('A2')

    self.obj141.graphClass_= graph_Agent
    if self.genGraphics:
       new_obj = graph_Agent(253.0,9.0,self.obj141)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Agent", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj141.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj141)
    self.globalAndLocalPostcondition(self.obj141, rootNode)
    self.obj141.postAction( rootNode.CREATE )

    self.obj142=Agent(self)
    self.obj142.isGraphObjectVisual = True

    if(hasattr(self.obj142, '_setHierarchicalLink')):
      self.obj142._setHierarchicalLink(False)

    # price
    self.obj142.price.setValue(95)

    # name
    self.obj142.name.setValue('A3')

    self.obj142.graphClass_= graph_Agent
    if self.genGraphics:
       new_obj = graph_Agent(453.0,9.0,self.obj142)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Agent", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj142.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj142)
    self.globalAndLocalPostcondition(self.obj142, rootNode)
    self.obj142.postAction( rootNode.CREATE )

    self.obj143=Capabilitie(self)
    self.obj143.isGraphObjectVisual = True

    if(hasattr(self.obj143, '_setHierarchicalLink')):
      self.obj143._setHierarchicalLink(False)

    # name
    self.obj143.name.setValue('C1')

    self.obj143.graphClass_= graph_Capabilitie
    if self.genGraphics:
       new_obj = graph_Capabilitie(104.0,202.0,self.obj143)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Capabilitie", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.2
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj143.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj143)
    self.globalAndLocalPostcondition(self.obj143, rootNode)
    self.obj143.postAction( rootNode.CREATE )

    self.obj144=Capabilitie(self)
    self.obj144.isGraphObjectVisual = True

    if(hasattr(self.obj144, '_setHierarchicalLink')):
      self.obj144._setHierarchicalLink(False)

    # name
    self.obj144.name.setValue('C2')

    self.obj144.graphClass_= graph_Capabilitie
    if self.genGraphics:
       new_obj = graph_Capabilitie(204.0,202.0,self.obj144)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Capabilitie", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj144.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj144)
    self.globalAndLocalPostcondition(self.obj144, rootNode)
    self.obj144.postAction( rootNode.CREATE )

    self.obj145=Capabilitie(self)
    self.obj145.isGraphObjectVisual = True

    if(hasattr(self.obj145, '_setHierarchicalLink')):
      self.obj145._setHierarchicalLink(False)

    # name
    self.obj145.name.setValue('C3')

    self.obj145.graphClass_= graph_Capabilitie
    if self.genGraphics:
       new_obj = graph_Capabilitie(324.0,202.0,self.obj145)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Capabilitie", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj145.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj145)
    self.globalAndLocalPostcondition(self.obj145, rootNode)
    self.obj145.postAction( rootNode.CREATE )

    self.obj146=Capabilitie(self)
    self.obj146.isGraphObjectVisual = True

    if(hasattr(self.obj146, '_setHierarchicalLink')):
      self.obj146._setHierarchicalLink(False)

    # name
    self.obj146.name.setValue('C4')

    self.obj146.graphClass_= graph_Capabilitie
    if self.genGraphics:
       new_obj = graph_Capabilitie(424.0,202.0,self.obj146)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Capabilitie", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj146.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj146)
    self.globalAndLocalPostcondition(self.obj146, rootNode)
    self.obj146.postAction( rootNode.CREATE )

    self.obj147=Role(self)
    self.obj147.isGraphObjectVisual = True

    if(hasattr(self.obj147, '_setHierarchicalLink')):
      self.obj147._setHierarchicalLink(False)

    # name
    self.obj147.name.setValue('R1')

    self.obj147.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(160.0,352.0,self.obj147)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj147.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj147)
    self.globalAndLocalPostcondition(self.obj147, rootNode)
    self.obj147.postAction( rootNode.CREATE )

    self.obj148=Role(self)
    self.obj148.isGraphObjectVisual = True

    if(hasattr(self.obj148, '_setHierarchicalLink')):
      self.obj148._setHierarchicalLink(False)

    # name
    self.obj148.name.setValue('R2')

    self.obj148.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(420.0,352.0,self.obj148)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj148.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj148)
    self.globalAndLocalPostcondition(self.obj148, rootNode)
    self.obj148.postAction( rootNode.CREATE )

    self.obj163=achieve(self)
    self.obj163.isGraphObjectVisual = True

    if(hasattr(self.obj163, '_setHierarchicalLink')):
      self.obj163._setHierarchicalLink(False)

    # rate
    self.obj163.rate.setValue(0.2)

    self.obj163.graphClass_= graph_achieve
    if self.genGraphics:
       new_obj = graph_achieve(59.5,430.0,self.obj163)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("achieve", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj163.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj163)
    self.globalAndLocalPostcondition(self.obj163, rootNode)
    self.obj163.postAction( rootNode.CREATE )

    self.obj164=achieve(self)
    self.obj164.isGraphObjectVisual = True

    if(hasattr(self.obj164, '_setHierarchicalLink')):
      self.obj164._setHierarchicalLink(False)

    # rate
    self.obj164.rate.setValue(0.8)

    self.obj164.graphClass_= graph_achieve
    if self.genGraphics:
       new_obj = graph_achieve(338.0,410.5,self.obj164)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("achieve", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj164.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj164)
    self.globalAndLocalPostcondition(self.obj164, rootNode)
    self.obj164.postAction( rootNode.CREATE )

    self.obj165=achieve(self)
    self.obj165.isGraphObjectVisual = True

    if(hasattr(self.obj165, '_setHierarchicalLink')):
      self.obj165._setHierarchicalLink(False)

    # rate
    self.obj165.rate.setValue(0.6)

    self.obj165.graphClass_= graph_achieve
    if self.genGraphics:
       new_obj = graph_achieve(294.0,455.0,self.obj165)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("achieve", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj165.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj165)
    self.globalAndLocalPostcondition(self.obj165, rootNode)
    self.obj165.postAction( rootNode.CREATE )

    self.obj166=achieve(self)
    self.obj166.isGraphObjectVisual = True

    if(hasattr(self.obj166, '_setHierarchicalLink')):
      self.obj166._setHierarchicalLink(False)

    # rate
    self.obj166.rate.setValue(0.4)

    self.obj166.graphClass_= graph_achieve
    if self.genGraphics:
       new_obj = graph_achieve(204.5,447.5,self.obj166)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("achieve", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj166.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj166)
    self.globalAndLocalPostcondition(self.obj166, rootNode)
    self.obj166.postAction( rootNode.CREATE )

    self.obj167=achieve(self)
    self.obj167.isGraphObjectVisual = True

    if(hasattr(self.obj167, '_setHierarchicalLink')):
      self.obj167._setHierarchicalLink(False)

    # rate
    self.obj167.rate.setValue(0.1)

    self.obj167.graphClass_= graph_achieve
    if self.genGraphics:
       new_obj = graph_achieve(497.5,416.0,self.obj167)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("achieve", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj167.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj167)
    self.globalAndLocalPostcondition(self.obj167, rootNode)
    self.obj167.postAction( rootNode.CREATE )

    self.obj168=achieve(self)
    self.obj168.isGraphObjectVisual = True

    if(hasattr(self.obj168, '_setHierarchicalLink')):
      self.obj168._setHierarchicalLink(False)

    # rate
    self.obj168.rate.setValue(0.4)

    self.obj168.graphClass_= graph_achieve
    if self.genGraphics:
       new_obj = graph_achieve(395.0,434.0,self.obj168)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("achieve", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj168.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj168)
    self.globalAndLocalPostcondition(self.obj168, rootNode)
    self.obj168.postAction( rootNode.CREATE )

    self.obj169=achieve(self)
    self.obj169.isGraphObjectVisual = True

    if(hasattr(self.obj169, '_setHierarchicalLink')):
      self.obj169._setHierarchicalLink(False)

    # rate
    self.obj169.rate.setValue(0.7)

    self.obj169.graphClass_= graph_achieve
    if self.genGraphics:
       new_obj = graph_achieve(284.5,420.0,self.obj169)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("achieve", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj169.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj169)
    self.globalAndLocalPostcondition(self.obj169, rootNode)
    self.obj169.postAction( rootNode.CREATE )

    self.obj170=achieve(self)
    self.obj170.isGraphObjectVisual = True

    if(hasattr(self.obj170, '_setHierarchicalLink')):
      self.obj170._setHierarchicalLink(False)

    # rate
    self.obj170.rate.setValue(1.0)

    self.obj170.graphClass_= graph_achieve
    if self.genGraphics:
       new_obj = graph_achieve(98.0,455.0,self.obj170)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("achieve", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj170.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj170)
    self.globalAndLocalPostcondition(self.obj170, rootNode)
    self.obj170.postAction( rootNode.CREATE )

    self.obj153=posses(self)
    self.obj153.isGraphObjectVisual = True

    if(hasattr(self.obj153, '_setHierarchicalLink')):
      self.obj153._setHierarchicalLink(False)

    # rate
    self.obj153.rate.setValue(0.3)

    self.obj153.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(90.75,176.0,self.obj153)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj153.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj153)
    self.globalAndLocalPostcondition(self.obj153, rootNode)
    self.obj153.postAction( rootNode.CREATE )

    self.obj154=posses(self)
    self.obj154.isGraphObjectVisual = True

    if(hasattr(self.obj154, '_setHierarchicalLink')):
      self.obj154._setHierarchicalLink(False)

    # rate
    self.obj154.rate.setValue(0.5)

    self.obj154.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(124.25,136.0,self.obj154)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.94
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj154.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj154)
    self.globalAndLocalPostcondition(self.obj154, rootNode)
    self.obj154.postAction( rootNode.CREATE )

    self.obj155=posses(self)
    self.obj155.isGraphObjectVisual = True

    if(hasattr(self.obj155, '_setHierarchicalLink')):
      self.obj155._setHierarchicalLink(False)

    # rate
    self.obj155.rate.setValue(0.5)

    self.obj155.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(246.75,164.5,self.obj155)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj155.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj155)
    self.globalAndLocalPostcondition(self.obj155, rootNode)
    self.obj155.postAction( rootNode.CREATE )

    self.obj156=posses(self)
    self.obj156.isGraphObjectVisual = True

    if(hasattr(self.obj156, '_setHierarchicalLink')):
      self.obj156._setHierarchicalLink(False)

    # rate
    self.obj156.rate.setValue(0.3)

    self.obj156.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(309.25,133.0,self.obj156)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj156.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj156)
    self.globalAndLocalPostcondition(self.obj156, rootNode)
    self.obj156.postAction( rootNode.CREATE )

    self.obj157=posses(self)
    self.obj157.isGraphObjectVisual = True

    if(hasattr(self.obj157, '_setHierarchicalLink')):
      self.obj157._setHierarchicalLink(False)

    # rate
    self.obj157.rate.setValue(0.2)

    self.obj157.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(474.75,126.0,self.obj157)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj157.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj157)
    self.globalAndLocalPostcondition(self.obj157, rootNode)
    self.obj157.postAction( rootNode.CREATE )

    self.obj158=posses(self)
    self.obj158.isGraphObjectVisual = True

    if(hasattr(self.obj158, '_setHierarchicalLink')):
      self.obj158._setHierarchicalLink(False)

    # rate
    self.obj158.rate.setValue(0.7)

    self.obj158.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(376.25,109.0,self.obj158)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj158.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj158)
    self.globalAndLocalPostcondition(self.obj158, rootNode)
    self.obj158.postAction( rootNode.CREATE )

    self.obj159=posses(self)
    self.obj159.isGraphObjectVisual = True

    if(hasattr(self.obj159, '_setHierarchicalLink')):
      self.obj159._setHierarchicalLink(False)

    # rate
    self.obj159.rate.setValue(0.5)

    self.obj159.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(273.5,68.0,self.obj159)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj159.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj159)
    self.globalAndLocalPostcondition(self.obj159, rootNode)
    self.obj159.postAction( rootNode.CREATE )

    self.obj160=posses(self)
    self.obj160.isGraphObjectVisual = True

    if(hasattr(self.obj160, '_setHierarchicalLink')):
      self.obj160._setHierarchicalLink(False)

    # rate
    self.obj160.rate.setValue(0.7)

    self.obj160.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(223.5,108.0,self.obj160)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.16
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj160.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj160)
    self.globalAndLocalPostcondition(self.obj160, rootNode)
    self.obj160.postAction( rootNode.CREATE )

    self.obj161=posses(self)
    self.obj161.isGraphObjectVisual = True

    if(hasattr(self.obj161, '_setHierarchicalLink')):
      self.obj161._setHierarchicalLink(False)

    # rate
    self.obj161.rate.setValue(0.9)

    self.obj161.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(416.25,95.5,self.obj161)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj161.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj161)
    self.globalAndLocalPostcondition(self.obj161, rootNode)
    self.obj161.postAction( rootNode.CREATE )

    self.obj162=posses(self)
    self.obj162.isGraphObjectVisual = True

    if(hasattr(self.obj162, '_setHierarchicalLink')):
      self.obj162._setHierarchicalLink(False)

    # rate
    self.obj162.rate.setValue(0.4)

    self.obj162.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(323.5,94.0,self.obj162)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.93
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj162.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj162)
    self.globalAndLocalPostcondition(self.obj162, rootNode)
    self.obj162.postAction( rootNode.CREATE )

    # Connections for obj149 (graphObject_: Obj177) named G1
    self.drawConnections(
 )
    # Connections for obj150 (graphObject_: Obj178) named G2
    self.drawConnections(
 )
    # Connections for obj151 (graphObject_: Obj179) named G3
    self.drawConnections(
 )
    # Connections for obj152 (graphObject_: Obj180) named G4
    self.drawConnections(
 )
    # Connections for obj171 (graphObject_: Obj217) of type require
    self.drawConnections(
(self.obj171,self.obj143,[135.75, 317.5, 121.0, 289.5, 125.0, 241.0],"true", 3) )
    # Connections for obj172 (graphObject_: Obj218) of type require
    self.drawConnections(
(self.obj172,self.obj144,[226.25, 312.5, 236.5, 284.5, 225.0, 241.0],"true", 3) )
    # Connections for obj173 (graphObject_: Obj219) of type require
    self.drawConnections(
(self.obj173,self.obj145,[309.25, 323.0, 349.5, 295.0, 345.0, 241.0],"true", 3) )
    # Connections for obj174 (graphObject_: Obj220) of type require
    self.drawConnections(
(self.obj174,self.obj146,[444.5, 297.0, 445.0, 241.0],"true", 2) )
    # Connections for obj175 (graphObject_: Obj221) of type require
    self.drawConnections(
(self.obj175,self.obj145,[370.75, 323.5, 346.0, 295.5, 345.0, 241.0],"true", 3) )
    # Connections for obj176 (graphObject_: Obj222) of type require
    self.drawConnections(
(self.obj176,self.obj144,[324.25, 326.5, 269.5, 298.5, 225.0, 241.0],"true", 3) )
    # Connections for obj140 (graphObject_: Obj168) named A1
    self.drawConnections(
(self.obj140,self.obj153,[78.0, 71.0, 79.0, 143.5, 90.75, 176.0],"true", 3),
(self.obj140,self.obj154,[78.0, 71.0, 87.5, 103.5, 124.25, 136.0],"true", 3),
(self.obj140,self.obj155,[78.0, 71.0, 180.0, 132.0, 246.75, 164.5],"true", 3),
(self.obj140,self.obj156,[78.0, 71.0, 217.5, 100.5, 309.25, 133.0],"true", 3) )
    # Connections for obj141 (graphObject_: Obj169) named A2
    self.drawConnections(
(self.obj141,self.obj158,[278.0, 71.0, 334.5, 76.5, 376.25, 109.0],"true", 3),
(self.obj141,self.obj159,[278.0, 71.0, 273.5, 68.0],"true", 2),
(self.obj141,self.obj160,[278.0, 71.0, 236.0, 75.0, 223.5, 108.0],"true", 3) )
    # Connections for obj142 (graphObject_: Obj170) named A3
    self.drawConnections(
(self.obj142,self.obj157,[478.0, 71.0, 483.0, 93.5, 474.75, 126.0],"true", 3),
(self.obj142,self.obj161,[478.0, 71.0, 449.5, 63.0, 416.25, 95.5],"true", 3),
(self.obj142,self.obj162,[478.0, 71.0, 344.0, 86.0, 323.5, 94.0],"true", 3) )
    # Connections for obj143 (graphObject_: Obj171) named C1
    self.drawConnections(
 )
    # Connections for obj144 (graphObject_: Obj172) named C2
    self.drawConnections(
 )
    # Connections for obj145 (graphObject_: Obj173) named C3
    self.drawConnections(
 )
    # Connections for obj146 (graphObject_: Obj174) named C4
    self.drawConnections(
 )
    # Connections for obj147 (graphObject_: Obj175) named R1
    self.drawConnections(
(self.obj147,self.obj171,[184.0, 353.0, 150.5, 345.5, 135.75, 317.5],"true", 3),
(self.obj147,self.obj172,[184.0, 353.0, 216.0, 340.5, 226.25, 312.5],"true", 3),
(self.obj147,self.obj173,[184.0, 353.0, 269.0, 351.0, 309.25, 323.0],"true", 3),
(self.obj147,self.obj163,[184.0, 398.0, 95.0, 403.0, 59.5, 430.0],"true", 3),
(self.obj147,self.obj164,[184.0, 398.0, 258.5, 383.5, 338.0, 410.5],"true", 3),
(self.obj147,self.obj165,[184.0, 398.0, 249.5, 428.0, 294.0, 455.0],"true", 3),
(self.obj147,self.obj166,[184.0, 398.0, 195.0, 420.5, 204.5, 447.5],"true", 3) )
    # Connections for obj148 (graphObject_: Obj176) named R2
    self.drawConnections(
(self.obj148,self.obj174,[444.0, 353.0, 444.5, 297.0],"true", 2),
(self.obj148,self.obj175,[444.0, 353.0, 395.5, 351.5, 370.75, 323.5],"true", 3),
(self.obj148,self.obj176,[444.0, 353.0, 379.0, 354.5, 324.25, 326.5],"true", 3),
(self.obj148,self.obj167,[444.0, 398.0, 483.0, 389.0, 497.5, 416.0],"true", 3),
(self.obj148,self.obj168,[444.0, 398.0, 415.5, 407.0, 395.0, 434.0],"true", 3),
(self.obj148,self.obj169,[444.0, 398.0, 340.0, 393.0, 284.5, 420.0],"true", 3),
(self.obj148,self.obj170,[444.0, 398.0, 193.0, 391.0, 98.0, 455.0],"true", 3) )
    # Connections for obj163 (graphObject_: Obj201) of type achieve
    self.drawConnections(
(self.obj163,self.obj149,[59.5, 430.0, 24.0, 457.0, 42.0, 506.0],"true", 3) )
    # Connections for obj164 (graphObject_: Obj203) of type achieve
    self.drawConnections(
(self.obj164,self.obj152,[338.0, 410.5, 417.5, 437.5, 502.0, 506.0],"true", 3) )
    # Connections for obj165 (graphObject_: Obj205) of type achieve
    self.drawConnections(
(self.obj165,self.obj151,[294.0, 455.0, 338.5, 482.0, 362.0, 506.0],"true", 3) )
    # Connections for obj166 (graphObject_: Obj207) of type achieve
    self.drawConnections(
(self.obj166,self.obj150,[204.5, 447.5, 214.0, 474.5, 222.0, 506.0],"true", 3) )
    # Connections for obj167 (graphObject_: Obj209) of type achieve
    self.drawConnections(
(self.obj167,self.obj152,[497.5, 416.0, 512.0, 443.0, 502.0, 506.0],"true", 3) )
    # Connections for obj168 (graphObject_: Obj211) of type achieve
    self.drawConnections(
(self.obj168,self.obj151,[395.0, 434.0, 374.5, 461.0, 362.0, 506.0],"true", 3) )
    # Connections for obj169 (graphObject_: Obj213) of type achieve
    self.drawConnections(
(self.obj169,self.obj150,[284.5, 420.0, 229.0, 447.0, 222.0, 506.0],"true", 3) )
    # Connections for obj170 (graphObject_: Obj215) of type achieve
    self.drawConnections(
(self.obj170,self.obj149,[98.0, 455.0, 42.0, 506.0],"true", 2) )
    # Connections for obj153 (graphObject_: Obj181) of type posses
    self.drawConnections(
(self.obj153,self.obj143,[90.75, 176.0, 102.5, 208.5, 125.0, 201.0],"true", 3) )
    # Connections for obj154 (graphObject_: Obj183) of type posses
    self.drawConnections(
(self.obj154,self.obj144,[124.25, 136.0, 161.0, 168.5, 225.0, 201.0],"true", 3) )
    # Connections for obj155 (graphObject_: Obj185) of type posses
    self.drawConnections(
(self.obj155,self.obj145,[246.75, 164.5, 313.5, 197.0, 345.0, 201.0],"true", 3) )
    # Connections for obj156 (graphObject_: Obj187) of type posses
    self.drawConnections(
(self.obj156,self.obj146,[309.25, 133.0, 401.0, 165.5, 445.0, 201.0],"true", 3) )
    # Connections for obj157 (graphObject_: Obj189) of type posses
    self.drawConnections(
(self.obj157,self.obj146,[474.75, 126.0, 466.5, 158.5, 445.0, 201.0],"true", 3) )
    # Connections for obj158 (graphObject_: Obj191) of type posses
    self.drawConnections(
(self.obj158,self.obj146,[376.25, 109.0, 418.0, 141.5, 445.0, 201.0],"true", 3) )
    # Connections for obj159 (graphObject_: Obj193) of type posses
    self.drawConnections(
(self.obj159,self.obj145,[273.5, 68.0, 345.0, 201.0],"true", 2) )
    # Connections for obj160 (graphObject_: Obj195) of type posses
    self.drawConnections(
(self.obj160,self.obj144,[223.5, 108.0, 225.0, 201.0],"true", 2) )
    # Connections for obj161 (graphObject_: Obj197) of type posses
    self.drawConnections(
(self.obj161,self.obj145,[416.25, 95.5, 383.0, 128.0, 345.0, 201.0],"true", 3) )
    # Connections for obj162 (graphObject_: Obj199) of type posses
    self.drawConnections(
(self.obj162,self.obj144,[323.5, 94.0, 284.0, 119.0, 225.0, 201.0],"true", 3) )

newfunction = omacsEx4_MDL

loadedMMName = 'omacs_META'

atom3version = '0.3'
