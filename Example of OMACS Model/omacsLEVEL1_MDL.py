"""
__omacsMODEL1_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: sam
Modified: Fri Feb 17 12:23:34 2017
_________________________________________________________________________
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

def omacsMODEL1_MDL(self, rootNode, omacssRootNode=None):

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


    self.obj1822=Agent(self)
    self.obj1822.isGraphObjectVisual = True

    if(hasattr(self.obj1822, '_setHierarchicalLink')):
      self.obj1822._setHierarchicalLink(False)

    # price
    self.obj1822.price.setValue(0)

    # name
    self.obj1822.name.setValue('A1')

    self.obj1822.graphClass_= graph_Agent
    if self.genGraphics:
       new_obj = graph_Agent(180.0,80.0,self.obj1822)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Agent", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1822.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1822)
    self.globalAndLocalPostcondition(self.obj1822, rootNode)
    self.obj1822.postAction( rootNode.CREATE )

    self.obj1823=Agent(self)
    self.obj1823.isGraphObjectVisual = True

    if(hasattr(self.obj1823, '_setHierarchicalLink')):
      self.obj1823._setHierarchicalLink(False)

    # price
    self.obj1823.price.setValue(0)

    # name
    self.obj1823.name.setValue('A2')

    self.obj1823.graphClass_= graph_Agent
    if self.genGraphics:
       new_obj = graph_Agent(320.0,60.0,self.obj1823)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Agent", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1823.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1823)
    self.globalAndLocalPostcondition(self.obj1823, rootNode)
    self.obj1823.postAction( rootNode.CREATE )

    self.obj1824=Agent(self)
    self.obj1824.isGraphObjectVisual = True

    if(hasattr(self.obj1824, '_setHierarchicalLink')):
      self.obj1824._setHierarchicalLink(False)

    # price
    self.obj1824.price.setValue(0)

    # name
    self.obj1824.name.setValue('A3')

    self.obj1824.graphClass_= graph_Agent
    if self.genGraphics:
       new_obj = graph_Agent(440.0,80.0,self.obj1824)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Agent", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1824.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1824)
    self.globalAndLocalPostcondition(self.obj1824, rootNode)
    self.obj1824.postAction( rootNode.CREATE )

    self.obj1825=Capabilitie(self)
    self.obj1825.isGraphObjectVisual = True

    if(hasattr(self.obj1825, '_setHierarchicalLink')):
      self.obj1825._setHierarchicalLink(False)

    # name
    self.obj1825.name.setValue('C1')

    self.obj1825.graphClass_= graph_Capabilitie
    if self.genGraphics:
       new_obj = graph_Capabilitie(200.0,220.0,self.obj1825)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Capabilitie", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1825.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1825)
    self.globalAndLocalPostcondition(self.obj1825, rootNode)
    self.obj1825.postAction( rootNode.CREATE )

    self.obj1826=Capabilitie(self)
    self.obj1826.isGraphObjectVisual = True

    if(hasattr(self.obj1826, '_setHierarchicalLink')):
      self.obj1826._setHierarchicalLink(False)

    # name
    self.obj1826.name.setValue('C2')

    self.obj1826.graphClass_= graph_Capabilitie
    if self.genGraphics:
       new_obj = graph_Capabilitie(360.0,220.0,self.obj1826)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Capabilitie", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1826.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1826)
    self.globalAndLocalPostcondition(self.obj1826, rootNode)
    self.obj1826.postAction( rootNode.CREATE )

    self.obj1827=Capabilitie(self)
    self.obj1827.isGraphObjectVisual = True

    if(hasattr(self.obj1827, '_setHierarchicalLink')):
      self.obj1827._setHierarchicalLink(False)

    # name
    self.obj1827.name.setValue('C3')

    self.obj1827.graphClass_= graph_Capabilitie
    if self.genGraphics:
       new_obj = graph_Capabilitie(480.0,220.0,self.obj1827)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Capabilitie", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1827.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1827)
    self.globalAndLocalPostcondition(self.obj1827, rootNode)
    self.obj1827.postAction( rootNode.CREATE )

    self.obj1838=Role(self)
    self.obj1838.isGraphObjectVisual = True

    if(hasattr(self.obj1838, '_setHierarchicalLink')):
      self.obj1838._setHierarchicalLink(False)

    # name
    self.obj1838.name.setValue('R1')

    self.obj1838.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(240.0,340.0,self.obj1838)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1838.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1838)
    self.globalAndLocalPostcondition(self.obj1838, rootNode)
    self.obj1838.postAction( rootNode.CREATE )

    self.obj1839=Role(self)
    self.obj1839.isGraphObjectVisual = True

    if(hasattr(self.obj1839, '_setHierarchicalLink')):
      self.obj1839._setHierarchicalLink(False)

    # name
    self.obj1839.name.setValue('R2')

    self.obj1839.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(420.0,340.0,self.obj1839)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1839.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1839)
    self.globalAndLocalPostcondition(self.obj1839, rootNode)
    self.obj1839.postAction( rootNode.CREATE )

    self.obj1844=Goal(self)
    self.obj1844.isGraphObjectVisual = True

    if(hasattr(self.obj1844, '_setHierarchicalLink')):
      self.obj1844._setHierarchicalLink(False)

    # name
    self.obj1844.name.setValue('G1')

    self.obj1844.graphClass_= graph_Goal
    if self.genGraphics:
       new_obj = graph_Goal(240.0,480.0,self.obj1844)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Goal", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1844.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1844)
    self.globalAndLocalPostcondition(self.obj1844, rootNode)
    self.obj1844.postAction( rootNode.CREATE )

    self.obj1845=Goal(self)
    self.obj1845.isGraphObjectVisual = True

    if(hasattr(self.obj1845, '_setHierarchicalLink')):
      self.obj1845._setHierarchicalLink(False)

    # name
    self.obj1845.name.setValue('G2')

    self.obj1845.graphClass_= graph_Goal
    if self.genGraphics:
       new_obj = graph_Goal(420.0,500.0,self.obj1845)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Goal", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1845.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1845)
    self.globalAndLocalPostcondition(self.obj1845, rootNode)
    self.obj1845.postAction( rootNode.CREATE )

    self.obj1828=posses(self)
    self.obj1828.isGraphObjectVisual = True

    if(hasattr(self.obj1828, '_setHierarchicalLink')):
      self.obj1828._setHierarchicalLink(False)

    # rate
    self.obj1828.rate.setValue(3.3)

    self.obj1828.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(483.0,180.5,self.obj1828)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1828.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1828)
    self.globalAndLocalPostcondition(self.obj1828, rootNode)
    self.obj1828.postAction( rootNode.CREATE )

    self.obj1829=posses(self)
    self.obj1829.isGraphObjectVisual = True

    if(hasattr(self.obj1829, '_setHierarchicalLink')):
      self.obj1829._setHierarchicalLink(False)

    # rate
    self.obj1829.rate.setValue(2.3)

    self.obj1829.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(433.5,169.75,self.obj1829)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1829.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1829)
    self.globalAndLocalPostcondition(self.obj1829, rootNode)
    self.obj1829.postAction( rootNode.CREATE )

    self.obj1830=posses(self)
    self.obj1830.isGraphObjectVisual = True

    if(hasattr(self.obj1830, '_setHierarchicalLink')):
      self.obj1830._setHierarchicalLink(False)

    # rate
    self.obj1830.rate.setValue(2.2)

    self.obj1830.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(363.0,170.5,self.obj1830)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1830.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1830)
    self.globalAndLocalPostcondition(self.obj1830, rootNode)
    self.obj1830.postAction( rootNode.CREATE )

    self.obj1831=posses(self)
    self.obj1831.isGraphObjectVisual = True

    if(hasattr(self.obj1831, '_setHierarchicalLink')):
      self.obj1831._setHierarchicalLink(False)

    # rate
    self.obj1831.rate.setValue(2.1)

    self.obj1831.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(282.0,206.5,self.obj1831)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1831.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1831)
    self.globalAndLocalPostcondition(self.obj1831, rootNode)
    self.obj1831.postAction( rootNode.CREATE )

    self.obj1832=posses(self)
    self.obj1832.isGraphObjectVisual = True

    if(hasattr(self.obj1832, '_setHierarchicalLink')):
      self.obj1832._setHierarchicalLink(False)

    # rate
    self.obj1832.rate.setValue(1.1)

    self.obj1832.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(213.0,180.5,self.obj1832)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1832.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1832)
    self.globalAndLocalPostcondition(self.obj1832, rootNode)
    self.obj1832.postAction( rootNode.CREATE )

    self.obj1833=posses(self)
    self.obj1833.isGraphObjectVisual = True

    if(hasattr(self.obj1833, '_setHierarchicalLink')):
      self.obj1833._setHierarchicalLink(False)

    # rate
    self.obj1833.rate.setValue(1.2)

    self.obj1833.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(255.0,136.5,self.obj1833)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1833.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1833)
    self.globalAndLocalPostcondition(self.obj1833, rootNode)
    self.obj1833.postAction( rootNode.CREATE )

    self.obj1846=achieve(self)
    self.obj1846.isGraphObjectVisual = True

    if(hasattr(self.obj1846, '_setHierarchicalLink')):
      self.obj1846._setHierarchicalLink(False)

    # rate
    self.obj1846.rate.setValue(2.2)

    self.obj1846.graphClass_= graph_achieve
    if self.genGraphics:
       new_obj = graph_achieve(433.5,463.5,self.obj1846)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("achieve", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1846.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1846)
    self.globalAndLocalPostcondition(self.obj1846, rootNode)
    self.obj1846.postAction( rootNode.CREATE )

    self.obj1847=achieve(self)
    self.obj1847.isGraphObjectVisual = True

    if(hasattr(self.obj1847, '_setHierarchicalLink')):
      self.obj1847._setHierarchicalLink(False)

    # rate
    self.obj1847.rate.setValue(1.1)

    self.obj1847.graphClass_= graph_achieve
    if self.genGraphics:
       new_obj = graph_achieve(253.5,453.5,self.obj1847)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("achieve", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1847.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1847)
    self.globalAndLocalPostcondition(self.obj1847, rootNode)
    self.obj1847.postAction( rootNode.CREATE )

    self.obj1840=requir(self)
    self.obj1840.isGraphObjectVisual = True

    if(hasattr(self.obj1840, '_setHierarchicalLink')):
      self.obj1840._setHierarchicalLink(False)

    self.obj1840.graphClass_= graph_requir
    if self.genGraphics:
       new_obj = graph_requir(232.5,320.0,self.obj1840)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("requir", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1840.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1840)
    self.globalAndLocalPostcondition(self.obj1840, rootNode)
    self.obj1840.postAction( rootNode.CREATE )

    self.obj1841=requir(self)
    self.obj1841.isGraphObjectVisual = True

    if(hasattr(self.obj1841, '_setHierarchicalLink')):
      self.obj1841._setHierarchicalLink(False)

    self.obj1841.graphClass_= graph_requir
    if self.genGraphics:
       new_obj = graph_requir(312.5,320.0,self.obj1841)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("requir", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1841.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1841)
    self.globalAndLocalPostcondition(self.obj1841, rootNode)
    self.obj1841.postAction( rootNode.CREATE )

    self.obj1842=requir(self)
    self.obj1842.isGraphObjectVisual = True

    if(hasattr(self.obj1842, '_setHierarchicalLink')):
      self.obj1842._setHierarchicalLink(False)

    self.obj1842.graphClass_= graph_requir
    if self.genGraphics:
       new_obj = graph_requir(400.5,308.0,self.obj1842)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("requir", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1842.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1842)
    self.globalAndLocalPostcondition(self.obj1842, rootNode)
    self.obj1842.postAction( rootNode.CREATE )

    self.obj1843=requir(self)
    self.obj1843.isGraphObjectVisual = True

    if(hasattr(self.obj1843, '_setHierarchicalLink')):
      self.obj1843._setHierarchicalLink(False)

    self.obj1843.graphClass_= graph_requir
    if self.genGraphics:
       new_obj = graph_requir(472.5,320.0,self.obj1843)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("requir", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1843.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1843)
    self.globalAndLocalPostcondition(self.obj1843, rootNode)
    self.obj1843.postAction( rootNode.CREATE )

    # Connections for obj1822 (graphObject_: Obj918) named A1
    self.drawConnections(
(self.obj1822,self.obj1832,[205.0, 142.0, 213.0, 180.5],"true", 2),
(self.obj1822,self.obj1833,[205.0, 142.0, 255.0, 136.5],"true", 2) )
    # Connections for obj1823 (graphObject_: Obj919) named A2
    self.drawConnections(
(self.obj1823,self.obj1829,[345.0, 122.0, 394.5, 145.5, 433.5, 169.75],"true", 3),
(self.obj1823,self.obj1830,[345.0, 122.0, 363.0, 170.5],"true", 2),
(self.obj1823,self.obj1831,[345.0, 122.0, 282.0, 206.5],"true", 2) )
    # Connections for obj1824 (graphObject_: Obj920) named A3
    self.drawConnections(
(self.obj1824,self.obj1828,[465.0, 142.0, 483.0, 180.5],"true", 2) )
    # Connections for obj1825 (graphObject_: Obj921) named C1
    self.drawConnections(
 )
    # Connections for obj1826 (graphObject_: Obj922) named C2
    self.drawConnections(
 )
    # Connections for obj1827 (graphObject_: Obj923) named C3
    self.drawConnections(
 )
    # Connections for obj1838 (graphObject_: Obj936) named R1
    self.drawConnections(
(self.obj1838,self.obj1840,[264.0, 341.0, 232.5, 320.0],"true", 2),
(self.obj1838,self.obj1841,[264.0, 341.0, 312.5, 320.0],"true", 2),
(self.obj1838,self.obj1847,[264.0, 386.0, 253.5, 453.5],"true", 2) )
    # Connections for obj1839 (graphObject_: Obj937) named R2
    self.drawConnections(
(self.obj1839,self.obj1842,[444.0, 341.0, 400.5, 308.0],"true", 2),
(self.obj1839,self.obj1843,[444.0, 341.0, 472.5, 320.0],"true", 2),
(self.obj1839,self.obj1846,[444.0, 386.0, 433.5, 463.5],"true", 2) )
    # Connections for obj1844 (graphObject_: Obj942) named G1
    self.drawConnections(
 )
    # Connections for obj1845 (graphObject_: Obj943) named G2
    self.drawConnections(
 )
    # Connections for obj1828 (graphObject_: Obj924) of type posses
    self.drawConnections(
(self.obj1828,self.obj1827,[483.0, 180.5, 501.0, 219.0],"true", 2) )
    # Connections for obj1829 (graphObject_: Obj926) of type posses
    self.drawConnections(
(self.obj1829,self.obj1827,[433.5, 169.75, 472.5, 194.0, 501.0, 219.0],"true", 3) )
    # Connections for obj1830 (graphObject_: Obj928) of type posses
    self.drawConnections(
(self.obj1830,self.obj1826,[363.0, 170.5, 381.0, 219.0],"true", 2) )
    # Connections for obj1831 (graphObject_: Obj930) of type posses
    self.drawConnections(
(self.obj1831,self.obj1825,[282.0, 206.5, 221.0, 219.0],"true", 2) )
    # Connections for obj1832 (graphObject_: Obj932) of type posses
    self.drawConnections(
(self.obj1832,self.obj1825,[213.0, 180.5, 221.0, 219.0],"true", 2) )
    # Connections for obj1833 (graphObject_: Obj934) of type posses
    self.drawConnections(
(self.obj1833,self.obj1826,[255.0, 136.5, 381.0, 219.0],"true", 2) )
    # Connections for obj1846 (graphObject_: Obj944) of type achieve
    self.drawConnections(
(self.obj1846,self.obj1845,[433.5, 463.5, 443.0, 501.0],"true", 2) )
    # Connections for obj1847 (graphObject_: Obj946) of type achieve
    self.drawConnections(
(self.obj1847,self.obj1844,[253.5, 453.5, 263.0, 481.0],"true", 2) )
    # Connections for obj1840 (graphObject_: Obj938) of type requir
    self.drawConnections(
(self.obj1840,self.obj1825,[232.5, 320.0, 221.0, 259.0],"true", 2) )
    # Connections for obj1841 (graphObject_: Obj939) of type requir
    self.drawConnections(
(self.obj1841,self.obj1826,[312.5, 320.0, 381.0, 259.0],"true", 2) )
    # Connections for obj1842 (graphObject_: Obj940) of type requir
    self.drawConnections(
(self.obj1842,self.obj1826,[400.5, 308.0, 381.0, 259.0],"true", 2) )
    # Connections for obj1843 (graphObject_: Obj941) of type requir
    self.drawConnections(
(self.obj1843,self.obj1827,[472.5, 320.0, 501.0, 259.0],"true", 2) )

newfunction = omacsMODEL1_MDL

loadedMMName = 'omacss_META'

atom3version = '0.3'
