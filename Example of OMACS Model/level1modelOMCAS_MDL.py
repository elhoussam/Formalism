"""
__level1modelOMCAS_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: sam
Modified: Sat Feb 18 19:53:59 2017
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

def level1modelOMCAS_MDL(self, rootNode, omacssRootNode=None):

    # --- Generating attributes code for ASG omacss ---
    if( omacssRootNode ): 
        # author
        omacssRootNode.author.setValue('Houssam Sam')

        # description
        omacssRootNode.description.setValue('\n')
        omacssRootNode.description.setHeight(15)

        # name
        omacssRootNode.name.setValue('modelOMACS1')
    # --- ASG attributes over ---


    self.obj3836=Agent(self)
    self.obj3836.isGraphObjectVisual = True

    if(hasattr(self.obj3836, '_setHierarchicalLink')):
      self.obj3836._setHierarchicalLink(False)

    # price
    self.obj3836.price.setValue(0)

    # name
    self.obj3836.name.setValue('a1')

    self.obj3836.graphClass_= graph_Agent
    if self.genGraphics:
       new_obj = graph_Agent(160.0,60.0,self.obj3836)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Agent", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj3836.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3836)
    self.globalAndLocalPostcondition(self.obj3836, rootNode)
    self.obj3836.postAction( rootNode.CREATE )

    self.obj3837=Agent(self)
    self.obj3837.isGraphObjectVisual = True

    if(hasattr(self.obj3837, '_setHierarchicalLink')):
      self.obj3837._setHierarchicalLink(False)

    # price
    self.obj3837.price.setValue(0)

    # name
    self.obj3837.name.setValue('a2')

    self.obj3837.graphClass_= graph_Agent
    if self.genGraphics:
       new_obj = graph_Agent(300.0,80.0,self.obj3837)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Agent", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj3837.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3837)
    self.globalAndLocalPostcondition(self.obj3837, rootNode)
    self.obj3837.postAction( rootNode.CREATE )

    self.obj3838=Agent(self)
    self.obj3838.isGraphObjectVisual = True

    if(hasattr(self.obj3838, '_setHierarchicalLink')):
      self.obj3838._setHierarchicalLink(False)

    # price
    self.obj3838.price.setValue(0)

    # name
    self.obj3838.name.setValue('a3')

    self.obj3838.graphClass_= graph_Agent
    if self.genGraphics:
       new_obj = graph_Agent(440.0,60.0,self.obj3838)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Agent", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj3838.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3838)
    self.globalAndLocalPostcondition(self.obj3838, rootNode)
    self.obj3838.postAction( rootNode.CREATE )

    self.obj3839=Capabilitie(self)
    self.obj3839.isGraphObjectVisual = True

    if(hasattr(self.obj3839, '_setHierarchicalLink')):
      self.obj3839._setHierarchicalLink(False)

    # name
    self.obj3839.name.setValue('c1')

    self.obj3839.graphClass_= graph_Capabilitie
    if self.genGraphics:
       new_obj = graph_Capabilitie(180.0,220.0,self.obj3839)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Capabilitie", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj3839.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3839)
    self.globalAndLocalPostcondition(self.obj3839, rootNode)
    self.obj3839.postAction( rootNode.CREATE )

    self.obj3840=Capabilitie(self)
    self.obj3840.isGraphObjectVisual = True

    if(hasattr(self.obj3840, '_setHierarchicalLink')):
      self.obj3840._setHierarchicalLink(False)

    # name
    self.obj3840.name.setValue('c2')

    self.obj3840.graphClass_= graph_Capabilitie
    if self.genGraphics:
       new_obj = graph_Capabilitie(300.0,220.0,self.obj3840)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Capabilitie", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj3840.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3840)
    self.globalAndLocalPostcondition(self.obj3840, rootNode)
    self.obj3840.postAction( rootNode.CREATE )

    self.obj3841=Capabilitie(self)
    self.obj3841.isGraphObjectVisual = True

    if(hasattr(self.obj3841, '_setHierarchicalLink')):
      self.obj3841._setHierarchicalLink(False)

    # name
    self.obj3841.name.setValue('c3')

    self.obj3841.graphClass_= graph_Capabilitie
    if self.genGraphics:
       new_obj = graph_Capabilitie(440.0,240.0,self.obj3841)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Capabilitie", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj3841.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3841)
    self.globalAndLocalPostcondition(self.obj3841, rootNode)
    self.obj3841.postAction( rootNode.CREATE )

    self.obj3842=Role(self)
    self.obj3842.isGraphObjectVisual = True

    if(hasattr(self.obj3842, '_setHierarchicalLink')):
      self.obj3842._setHierarchicalLink(False)

    # name
    self.obj3842.name.setValue('R1')

    self.obj3842.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(220.0,340.0,self.obj3842)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj3842.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3842)
    self.globalAndLocalPostcondition(self.obj3842, rootNode)
    self.obj3842.postAction( rootNode.CREATE )

    self.obj3843=Role(self)
    self.obj3843.isGraphObjectVisual = True

    if(hasattr(self.obj3843, '_setHierarchicalLink')):
      self.obj3843._setHierarchicalLink(False)

    # name
    self.obj3843.name.setValue('R2')

    self.obj3843.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(400.0,340.0,self.obj3843)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj3843.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3843)
    self.globalAndLocalPostcondition(self.obj3843, rootNode)
    self.obj3843.postAction( rootNode.CREATE )

    self.obj3844=Goal(self)
    self.obj3844.isGraphObjectVisual = True

    if(hasattr(self.obj3844, '_setHierarchicalLink')):
      self.obj3844._setHierarchicalLink(False)

    # name
    self.obj3844.name.setValue('G1')

    self.obj3844.graphClass_= graph_Goal
    if self.genGraphics:
       new_obj = graph_Goal(240.0,480.0,self.obj3844)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Goal", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj3844.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3844)
    self.globalAndLocalPostcondition(self.obj3844, rootNode)
    self.obj3844.postAction( rootNode.CREATE )

    self.obj3845=Goal(self)
    self.obj3845.isGraphObjectVisual = True

    if(hasattr(self.obj3845, '_setHierarchicalLink')):
      self.obj3845._setHierarchicalLink(False)

    # name
    self.obj3845.name.setValue('G2')

    self.obj3845.graphClass_= graph_Goal
    if self.genGraphics:
       new_obj = graph_Goal(420.0,480.0,self.obj3845)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Goal", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj3845.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3845)
    self.globalAndLocalPostcondition(self.obj3845, rootNode)
    self.obj3845.postAction( rootNode.CREATE )

    self.obj3866=posses(self)
    self.obj3866.isGraphObjectVisual = True

    if(hasattr(self.obj3866, '_setHierarchicalLink')):
      self.obj3866._setHierarchicalLink(False)

    # rate
    self.obj3866.rate.setValue(1.1)

    self.obj3866.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(193.0,170.5,self.obj3866)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj3866.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3866)
    self.globalAndLocalPostcondition(self.obj3866, rootNode)
    self.obj3866.postAction( rootNode.CREATE )

    self.obj3867=posses(self)
    self.obj3867.isGraphObjectVisual = True

    if(hasattr(self.obj3867, '_setHierarchicalLink')):
      self.obj3867._setHierarchicalLink(False)

    # rate
    self.obj3867.rate.setValue(1.2)

    self.obj3867.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(253.0,170.5,self.obj3867)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj3867.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3867)
    self.globalAndLocalPostcondition(self.obj3867, rootNode)
    self.obj3867.postAction( rootNode.CREATE )

    self.obj3872=posses(self)
    self.obj3872.isGraphObjectVisual = True

    if(hasattr(self.obj3872, '_setHierarchicalLink')):
      self.obj3872._setHierarchicalLink(False)

    # rate
    self.obj3872.rate.setValue(2.1)

    self.obj3872.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(250.0,144.5,self.obj3872)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj3872.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3872)
    self.globalAndLocalPostcondition(self.obj3872, rootNode)
    self.obj3872.postAction( rootNode.CREATE )

    self.obj3873=posses(self)
    self.obj3873.isGraphObjectVisual = True

    if(hasattr(self.obj3873, '_setHierarchicalLink')):
      self.obj3873._setHierarchicalLink(False)

    # rate
    self.obj3873.rate.setValue(2.2)

    self.obj3873.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(323.0,180.5,self.obj3873)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj3873.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3873)
    self.globalAndLocalPostcondition(self.obj3873, rootNode)
    self.obj3873.postAction( rootNode.CREATE )

    self.obj3874=posses(self)
    self.obj3874.isGraphObjectVisual = True

    if(hasattr(self.obj3874, '_setHierarchicalLink')):
      self.obj3874._setHierarchicalLink(False)

    # rate
    self.obj3874.rate.setValue(2.3)

    self.obj3874.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(402.5,208.75,self.obj3874)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj3874.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3874)
    self.globalAndLocalPostcondition(self.obj3874, rootNode)
    self.obj3874.postAction( rootNode.CREATE )

    self.obj3881=posses(self)
    self.obj3881.isGraphObjectVisual = True

    if(hasattr(self.obj3881, '_setHierarchicalLink')):
      self.obj3881._setHierarchicalLink(False)

    # rate
    self.obj3881.rate.setValue(3.2)

    self.obj3881.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(394.5,152.25,self.obj3881)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj3881.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3881)
    self.globalAndLocalPostcondition(self.obj3881, rootNode)
    self.obj3881.postAction( rootNode.CREATE )

    self.obj3882=posses(self)
    self.obj3882.isGraphObjectVisual = True

    if(hasattr(self.obj3882, '_setHierarchicalLink')):
      self.obj3882._setHierarchicalLink(False)

    # rate
    self.obj3882.rate.setValue(3.3)

    self.obj3882.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(453.0,210.5,self.obj3882)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj3882.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3882)
    self.globalAndLocalPostcondition(self.obj3882, rootNode)
    self.obj3882.postAction( rootNode.CREATE )

    self.obj3893=achieve(self)
    self.obj3893.isGraphObjectVisual = True

    if(hasattr(self.obj3893, '_setHierarchicalLink')):
      self.obj3893._setHierarchicalLink(False)

    # rate
    self.obj3893.rate.setValue(1.1)

    self.obj3893.graphClass_= graph_achieve
    if self.genGraphics:
       new_obj = graph_achieve(253.5,433.5,self.obj3893)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("achieve", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj3893.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3893)
    self.globalAndLocalPostcondition(self.obj3893, rootNode)
    self.obj3893.postAction( rootNode.CREATE )

    self.obj3894=achieve(self)
    self.obj3894.isGraphObjectVisual = True

    if(hasattr(self.obj3894, '_setHierarchicalLink')):
      self.obj3894._setHierarchicalLink(False)

    # rate
    self.obj3894.rate.setValue(1.2)

    self.obj3894.graphClass_= graph_achieve
    if self.genGraphics:
       new_obj = graph_achieve(347.25,464.25,self.obj3894)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("achieve", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj3894.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3894)
    self.globalAndLocalPostcondition(self.obj3894, rootNode)
    self.obj3894.postAction( rootNode.CREATE )

    self.obj3895=achieve(self)
    self.obj3895.isGraphObjectVisual = True

    if(hasattr(self.obj3895, '_setHierarchicalLink')):
      self.obj3895._setHierarchicalLink(False)

    # rate
    self.obj3895.rate.setValue(2.2)

    self.obj3895.graphClass_= graph_achieve
    if self.genGraphics:
       new_obj = graph_achieve(433.5,433.5,self.obj3895)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("achieve", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj3895.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3895)
    self.globalAndLocalPostcondition(self.obj3895, rootNode)
    self.obj3895.postAction( rootNode.CREATE )

    self.obj3887=requir(self)
    self.obj3887.isGraphObjectVisual = True

    if(hasattr(self.obj3887, '_setHierarchicalLink')):
      self.obj3887._setHierarchicalLink(False)

    self.obj3887.graphClass_= graph_requir
    if self.genGraphics:
       new_obj = graph_requir(222.5,300.0,self.obj3887)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("requir", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj3887.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3887)
    self.globalAndLocalPostcondition(self.obj3887, rootNode)
    self.obj3887.postAction( rootNode.CREATE )

    self.obj3888=requir(self)
    self.obj3888.isGraphObjectVisual = True

    if(hasattr(self.obj3888, '_setHierarchicalLink')):
      self.obj3888._setHierarchicalLink(False)

    self.obj3888.graphClass_= graph_requir
    if self.genGraphics:
       new_obj = graph_requir(282.5,300.0,self.obj3888)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("requir", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj3888.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3888)
    self.globalAndLocalPostcondition(self.obj3888, rootNode)
    self.obj3888.postAction( rootNode.CREATE )

    self.obj3889=requir(self)
    self.obj3889.isGraphObjectVisual = True

    if(hasattr(self.obj3889, '_setHierarchicalLink')):
      self.obj3889._setHierarchicalLink(False)

    self.obj3889.graphClass_= graph_requir
    if self.genGraphics:
       new_obj = graph_requir(372.5,300.0,self.obj3889)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("requir", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj3889.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3889)
    self.globalAndLocalPostcondition(self.obj3889, rootNode)
    self.obj3889.postAction( rootNode.CREATE )

    self.obj3892=requir(self)
    self.obj3892.isGraphObjectVisual = True

    if(hasattr(self.obj3892, '_setHierarchicalLink')):
      self.obj3892._setHierarchicalLink(False)

    self.obj3892.graphClass_= graph_requir
    if self.genGraphics:
       new_obj = graph_requir(442.5,310.0,self.obj3892)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("requir", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj3892.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3892)
    self.globalAndLocalPostcondition(self.obj3892, rootNode)
    self.obj3892.postAction( rootNode.CREATE )

    # Connections for obj3836 (graphObject_: Obj1822) named a1
    self.drawConnections(
(self.obj3836,self.obj3866,[185.0, 122.0, 193.0, 170.5],"true", 2),
(self.obj3836,self.obj3867,[185.0, 122.0, 253.0, 170.5],"true", 2) )
    # Connections for obj3837 (graphObject_: Obj1823) named a2
    self.drawConnections(
(self.obj3837,self.obj3872,[325.0, 142.0, 250.0, 144.5],"true", 2),
(self.obj3837,self.obj3873,[325.0, 142.0, 323.0, 180.5],"true", 2),
(self.obj3837,self.obj3874,[325.0, 142.0, 368.5, 184.5, 402.5, 208.75],"true", 3) )
    # Connections for obj3838 (graphObject_: Obj1824) named a3
    self.drawConnections(
(self.obj3838,self.obj3881,[465.0, 122.0, 425.5, 143.0, 394.5, 152.25],"true", 3),
(self.obj3838,self.obj3882,[465.0, 122.0, 453.0, 210.5],"true", 2) )
    # Connections for obj3839 (graphObject_: Obj1825) named c1
    self.drawConnections(
 )
    # Connections for obj3840 (graphObject_: Obj1826) named c2
    self.drawConnections(
 )
    # Connections for obj3841 (graphObject_: Obj1827) named c3
    self.drawConnections(
 )
    # Connections for obj3842 (graphObject_: Obj1828) named R1
    self.drawConnections(
(self.obj3842,self.obj3887,[244.0, 341.0, 222.5, 300.0],"true", 2),
(self.obj3842,self.obj3888,[244.0, 341.0, 282.5, 300.0],"true", 2),
(self.obj3842,self.obj3893,[244.0, 386.0, 253.5, 433.5],"true", 2),
(self.obj3842,self.obj3894,[244.0, 386.0, 297.5, 440.5, 347.25, 464.25],"true", 3) )
    # Connections for obj3843 (graphObject_: Obj1829) named R2
    self.drawConnections(
(self.obj3843,self.obj3889,[424.0, 341.0, 372.5, 300.0],"true", 2),
(self.obj3843,self.obj3892,[424.0, 341.0, 442.5, 310.0],"true", 2),
(self.obj3843,self.obj3895,[424.0, 386.0, 433.5, 433.5],"true", 2) )
    # Connections for obj3844 (graphObject_: Obj1830) named G1
    self.drawConnections(
 )
    # Connections for obj3845 (graphObject_: Obj1831) named G2
    self.drawConnections(
 )
    # Connections for obj3866 (graphObject_: Obj1832) of type posses
    self.drawConnections(
(self.obj3866,self.obj3839,[193.0, 170.5, 201.0, 219.0],"true", 2) )
    # Connections for obj3867 (graphObject_: Obj1834) of type posses
    self.drawConnections(
(self.obj3867,self.obj3840,[253.0, 170.5, 321.0, 219.0],"true", 2) )
    # Connections for obj3872 (graphObject_: Obj1836) of type posses
    self.drawConnections(
(self.obj3872,self.obj3839,[250.0, 144.5, 201.0, 219.0],"true", 2) )
    # Connections for obj3873 (graphObject_: Obj1838) of type posses
    self.drawConnections(
(self.obj3873,self.obj3840,[323.0, 180.5, 321.0, 219.0],"true", 2) )
    # Connections for obj3874 (graphObject_: Obj1840) of type posses
    self.drawConnections(
(self.obj3874,self.obj3841,[402.5, 208.75, 436.5, 233.0, 461.0, 239.0],"true", 3) )
    # Connections for obj3881 (graphObject_: Obj1842) of type posses
    self.drawConnections(
(self.obj3881,self.obj3840,[394.5, 152.25, 363.5, 161.5, 321.0, 219.0],"true", 3) )
    # Connections for obj3882 (graphObject_: Obj1844) of type posses
    self.drawConnections(
(self.obj3882,self.obj3841,[453.0, 210.5, 461.0, 239.0],"true", 2) )
    # Connections for obj3893 (graphObject_: Obj1850) of type achieve
    self.drawConnections(
(self.obj3893,self.obj3844,[253.5, 433.5, 263.0, 481.0],"true", 2) )
    # Connections for obj3894 (graphObject_: Obj1852) of type achieve
    self.drawConnections(
(self.obj3894,self.obj3845,[347.25, 464.25, 397.0, 488.0, 443.0, 481.0],"true", 3) )
    # Connections for obj3895 (graphObject_: Obj1854) of type achieve
    self.drawConnections(
(self.obj3895,self.obj3845,[433.5, 433.5, 443.0, 481.0],"true", 2) )
    # Connections for obj3887 (graphObject_: Obj1846) of type requir
    self.drawConnections(
(self.obj3887,self.obj3839,[222.5, 300.0, 201.0, 259.0],"true", 2) )
    # Connections for obj3888 (graphObject_: Obj1847) of type requir
    self.drawConnections(
(self.obj3888,self.obj3840,[282.5, 300.0, 321.0, 259.0],"true", 2) )
    # Connections for obj3889 (graphObject_: Obj1848) of type requir
    self.drawConnections(
(self.obj3889,self.obj3840,[372.5, 300.0, 321.0, 259.0],"true", 2) )
    # Connections for obj3892 (graphObject_: Obj1849) of type requir
    self.drawConnections(
(self.obj3892,self.obj3841,[442.5, 310.0, 461.0, 279.0],"true", 2) )

newfunction = level1modelOMCAS_MDL

loadedMMName = 'omacss_META'

atom3version = '0.3'
