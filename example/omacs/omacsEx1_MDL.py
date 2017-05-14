"""
__omacsEx1_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: sam
Modified: Fri May 12 17:09:41 2017
______________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from Agent import *
from Capabilitie import *
from Role import *
from Goal import *
from posses import *
from achieve import *
from require import *
from graph_posses import *
from graph_achieve import *
from graph_require import *
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

def omacsEx1_MDL(self, rootNode, omacsRootNode=None):

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


    self.obj70=Agent(self)
    self.obj70.isGraphObjectVisual = True

    if(hasattr(self.obj70, '_setHierarchicalLink')):
      self.obj70._setHierarchicalLink(False)

    # price
    self.obj70.price.setValue(5)

    # name
    self.obj70.name.setValue('A1')

    self.obj70.graphClass_= graph_Agent
    if self.genGraphics:
       new_obj = graph_Agent(66.8963808433,6.41503697948,self.obj70)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Agent", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.92
       new_obj.layConstraints['scale'] = [0.5, 0.5]
    else: new_obj = None
    self.obj70.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj70)
    self.globalAndLocalPostcondition(self.obj70, rootNode)
    self.obj70.postAction( rootNode.CREATE )

    self.obj72=Capabilitie(self)
    self.obj72.isGraphObjectVisual = True

    if(hasattr(self.obj72, '_setHierarchicalLink')):
      self.obj72._setHierarchicalLink(False)

    # name
    self.obj72.name.setValue('C1')

    self.obj72.graphClass_= graph_Capabilitie
    if self.genGraphics:
       new_obj = graph_Capabilitie(0.0,138.077162131,self.obj72)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Capabilitie", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.92
       new_obj.layConstraints['scale'] = [0.5, 0.5]
    else: new_obj = None
    self.obj72.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj72)
    self.globalAndLocalPostcondition(self.obj72, rootNode)
    self.obj72.postAction( rootNode.CREATE )

    self.obj73=Capabilitie(self)
    self.obj73.isGraphObjectVisual = True

    if(hasattr(self.obj73, '_setHierarchicalLink')):
      self.obj73._setHierarchicalLink(False)

    # name
    self.obj73.name.setValue('C2')

    self.obj73.graphClass_= graph_Capabilitie
    if self.genGraphics:
       new_obj = graph_Capabilitie(173.872398929,138.915067181,self.obj73)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Capabilitie", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.92
       new_obj.layConstraints['scale'] = [0.5, 0.5]
    else: new_obj = None
    self.obj73.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj73)
    self.globalAndLocalPostcondition(self.obj73, rootNode)
    self.obj73.postAction( rootNode.CREATE )

    self.obj74=Capabilitie(self)
    self.obj74.isGraphObjectVisual = True

    if(hasattr(self.obj74, '_setHierarchicalLink')):
      self.obj74._setHierarchicalLink(False)

    # name
    self.obj74.name.setValue('C3')

    self.obj74.graphClass_= graph_Capabilitie
    if self.genGraphics:
       new_obj = graph_Capabilitie(368.483618626,117.785128873,self.obj74)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Capabilitie", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.92
       new_obj.layConstraints['scale'] = [0.5, 0.5]
    else: new_obj = None
    self.obj74.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj74)
    self.globalAndLocalPostcondition(self.obj74, rootNode)
    self.obj74.postAction( rootNode.CREATE )

    self.obj75=Role(self)
    self.obj75.isGraphObjectVisual = True

    if(hasattr(self.obj75, '_setHierarchicalLink')):
      self.obj75._setHierarchicalLink(False)

    # name
    self.obj75.name.setValue('R1')

    self.obj75.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(104.578380568,273.079999986,self.obj75)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.92
       new_obj.layConstraints['scale'] = [0.5, 0.5]
    else: new_obj = None
    self.obj75.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj75)
    self.globalAndLocalPostcondition(self.obj75, rootNode)
    self.obj75.postAction( rootNode.CREATE )

    self.obj76=Role(self)
    self.obj76.isGraphObjectVisual = True

    if(hasattr(self.obj76, '_setHierarchicalLink')):
      self.obj76._setHierarchicalLink(False)

    # name
    self.obj76.name.setValue('R2')

    self.obj76.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(283.382705292,244.348766903,self.obj76)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.92
       new_obj.layConstraints['scale'] = [0.5, 0.5]
    else: new_obj = None
    self.obj76.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj76)
    self.globalAndLocalPostcondition(self.obj76, rootNode)
    self.obj76.postAction( rootNode.CREATE )

    self.obj77=Goal(self)
    self.obj77.isGraphObjectVisual = True

    if(hasattr(self.obj77, '_setHierarchicalLink')):
      self.obj77._setHierarchicalLink(False)

    # name
    self.obj77.name.setValue('G1')

    self.obj77.graphClass_= graph_Goal
    if self.genGraphics:
       new_obj = graph_Goal(4.01727460844,388.881233861,self.obj77)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Goal", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.92
       new_obj.layConstraints['scale'] = [0.5, 0.5]
    else: new_obj = None
    self.obj77.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj77)
    self.globalAndLocalPostcondition(self.obj77, rootNode)
    self.obj77.postAction( rootNode.CREATE )

    self.obj78=Goal(self)
    self.obj78.isGraphObjectVisual = True

    if(hasattr(self.obj78, '_setHierarchicalLink')):
      self.obj78._setHierarchicalLink(False)

    # name
    self.obj78.name.setValue('G2')

    self.obj78.graphClass_= graph_Goal
    if self.genGraphics:
       new_obj = graph_Goal(283.482036653,382.072046503,self.obj78)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Goal", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.92
       new_obj.layConstraints['scale'] = [0.5, 0.5]
    else: new_obj = None
    self.obj78.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj78)
    self.globalAndLocalPostcondition(self.obj78, rootNode)
    self.obj78.postAction( rootNode.CREATE )

    self.obj79=posses(self)
    self.obj79.isGraphObjectVisual = True

    if(hasattr(self.obj79, '_setHierarchicalLink')):
      self.obj79._setHierarchicalLink(False)

    # rate
    self.obj79.rate.setValue(0.2)

    self.obj79.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(64.5081639099,100.058863313,self.obj79)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.92
       new_obj.layConstraints['scale'] = [0.5, 0.5]
    else: new_obj = None
    self.obj79.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj79)
    self.globalAndLocalPostcondition(self.obj79, rootNode)
    self.obj79.postAction( rootNode.CREATE )

    self.obj80=posses(self)
    self.obj80.isGraphObjectVisual = True

    if(hasattr(self.obj80, '_setHierarchicalLink')):
      self.obj80._setHierarchicalLink(False)

    # rate
    self.obj80.rate.setValue(0.8)

    self.obj80.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(150.290138757,87.9296918105,self.obj80)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.92
       new_obj.layConstraints['scale'] = [0.5, 0.5]
    else: new_obj = None
    self.obj80.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj80)
    self.globalAndLocalPostcondition(self.obj80, rootNode)
    self.obj80.postAction( rootNode.CREATE )

    self.obj84=achieve(self)
    self.obj84.isGraphObjectVisual = True

    if(hasattr(self.obj84, '_setHierarchicalLink')):
      self.obj84._setHierarchicalLink(False)

    # rate
    self.obj84.rate.setValue(0.11)

    self.obj84.graphClass_= graph_achieve
    if self.genGraphics:
       new_obj = graph_achieve(84.8262697098,362.145172582,self.obj84)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("achieve", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.92
       new_obj.layConstraints['scale'] = [0.5, 0.5]
    else: new_obj = None
    self.obj84.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj84)
    self.globalAndLocalPostcondition(self.obj84, rootNode)
    self.obj84.postAction( rootNode.CREATE )

    self.obj85=achieve(self)
    self.obj85.isGraphObjectVisual = True

    if(hasattr(self.obj85, '_setHierarchicalLink')):
      self.obj85._setHierarchicalLink(False)

    # rate
    self.obj85.rate.setValue(0.22)

    self.obj85.graphClass_= graph_achieve
    if self.genGraphics:
       new_obj = graph_achieve(317.182310383,337.057717493,self.obj85)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("achieve", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.92
       new_obj.layConstraints['scale'] = [0.5, 0.5]
    else: new_obj = None
    self.obj85.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj85)
    self.globalAndLocalPostcondition(self.obj85, rootNode)
    self.obj85.postAction( rootNode.CREATE )

    self.obj86=achieve(self)
    self.obj86.isGraphObjectVisual = True

    if(hasattr(self.obj86, '_setHierarchicalLink')):
      self.obj86._setHierarchicalLink(False)

    # rate
    self.obj86.rate.setValue(0.12)

    self.obj86.graphClass_= graph_achieve
    if self.genGraphics:
       new_obj = graph_achieve(222.137563265,342.387775475,self.obj86)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("achieve", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj86.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj86)
    self.globalAndLocalPostcondition(self.obj86, rootNode)
    self.obj86.postAction( rootNode.CREATE )

    self.obj88=require(self)
    self.obj88.isGraphObjectVisual = True

    if(hasattr(self.obj88, '_setHierarchicalLink')):
      self.obj88._setHierarchicalLink(False)

    self.obj88.graphClass_= graph_require
    if self.genGraphics:
       new_obj = graph_require(340.414318872,195.904654541,self.obj88)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("require", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj88.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj88)
    self.globalAndLocalPostcondition(self.obj88, rootNode)
    self.obj88.postAction( rootNode.CREATE )

    self.obj89=require(self)
    self.obj89.isGraphObjectVisual = True

    if(hasattr(self.obj89, '_setHierarchicalLink')):
      self.obj89._setHierarchicalLink(False)

    self.obj89.graphClass_= graph_require
    if self.genGraphics:
       new_obj = graph_require(244.92103503,220.28528088,self.obj89)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("require", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj89.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj89)
    self.globalAndLocalPostcondition(self.obj89, rootNode)
    self.obj89.postAction( rootNode.CREATE )

    self.obj90=require(self)
    self.obj90.isGraphObjectVisual = True

    if(hasattr(self.obj90, '_setHierarchicalLink')):
      self.obj90._setHierarchicalLink(False)

    self.obj90.graphClass_= graph_require
    if self.genGraphics:
       new_obj = graph_require(153.01081005,221.905331689,self.obj90)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("require", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj90.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj90)
    self.globalAndLocalPostcondition(self.obj90, rootNode)
    self.obj90.postAction( rootNode.CREATE )

    self.obj91=require(self)
    self.obj91.isGraphObjectVisual = True

    if(hasattr(self.obj91, '_setHierarchicalLink')):
      self.obj91._setHierarchicalLink(False)

    self.obj91.graphClass_= graph_require
    if self.genGraphics:
       new_obj = graph_require(67.381555298,233.108740168,self.obj91)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("require", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj91.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj91)
    self.globalAndLocalPostcondition(self.obj91, rootNode)
    self.obj91.postAction( rootNode.CREATE )

    # Connections for obj70 (graphObject_: Obj58) named A1
    self.drawConnections(
(self.obj70,self.obj79,[91.3963808432991, 41.91503697947731, 82.10725912074903, 73.76833202511551, 64.50816390992425, 100.05886331303657],"true", 3),
(self.obj70,self.obj80,[91.3963808432991, 41.91503697947731, 124.42113423544087, 61.42968426010813, 150.29013875682384, 87.92969181051987],"true", 3) )
    # Connections for obj72 (graphObject_: Obj60) named C1
    self.drawConnections(
 )
    # Connections for obj73 (graphObject_: Obj61) named C2
    self.drawConnections(
 )
    # Connections for obj74 (graphObject_: Obj62) named C3
    self.drawConnections(
 )
    # Connections for obj75 (graphObject_: Obj63) named R1
    self.drawConnections(
(self.obj75,self.obj90,[128.5783805680038, 285.70499998567504, 136.43730545936495, 251.3528148901846, 153.01081004957175, 221.9053316890469],"true", 3),
(self.obj75,self.obj91,[128.5783805680038, 285.70499998567504, 94.27615044002344, 262.7656996317734, 67.38155529802249, 233.10874016814495],"true", 3),
(self.obj75,self.obj84,[128.5783805680038, 308.20499998567504, 110.09154619972537, 338.85111411300124, 84.82626970983395, 362.1451725819457],"true", 3),
(self.obj75,self.obj86,[128.5783805680038, 308.20499998567504, 177.53664924416333, 320.79601384542224, 222.13756326537128, 342.3877754747146],"true", 3) )
    # Connections for obj76 (graphObject_: Obj64) named R2
    self.drawConnections(
(self.obj76,self.obj88,[307.3827052922357, 256.9737669028152, 319.8890905381401, 223.4518140486341, 340.414318871705, 195.90465454112874],"true", 3),
(self.obj76,self.obj89,[307.3827052922357, 256.9737669028152, 273.0486116211594, 242.54995581082727, 244.92103503030822, 220.28528088040454],"true", 3),
(self.obj76,self.obj85,[307.3827052922357, 279.4737669028152, 317.2824775426448, 308.2831475934922, 317.1823103827948, 337.0577174934995],"true", 3) )
    # Connections for obj77 (graphObject_: Obj65) named G1
    self.drawConnections(
 )
    # Connections for obj78 (graphObject_: Obj66) named G2
    self.drawConnections(
 )
    # Connections for obj79 (graphObject_: Obj67) of type posses
    self.drawConnections(
(self.obj79,self.obj72,[64.50816390992425, 100.05886331303657, 46.90906869909948, 126.34939460095762, 21.0, 147.07716213116151],"true", 3) )
    # Connections for obj80 (graphObject_: Obj69) of type posses
    self.drawConnections(
(self.obj80,self.obj73,[150.29013875682384, 87.92969181051987, 176.15914327820678, 114.42969936093161, 194.87239892883093, 147.91506718112427],"true", 3) )
    # Connections for obj84 (graphObject_: Obj77) of type achieve
    self.drawConnections(
(self.obj84,self.obj77,[84.82626970983395, 362.1451725819457, 59.56099321994252, 385.43923105089016, 27.517274608438115, 401.38123386145287],"true", 3) )
    # Connections for obj85 (graphObject_: Obj79) of type achieve
    self.drawConnections(
(self.obj85,self.obj78,[317.1823103827948, 337.0577174934995, 317.0821432229448, 365.8322873935069, 306.9820366528357, 394.57204650284456],"true", 3) )
    # Connections for obj86 (graphObject_: Obj81) of type achieve
    self.drawConnections(
(self.obj86,self.obj78,[222.13756326537128, 342.3877754747146, 266.73847728657927, 363.97953710400697, 306.9820366528357, 394.57204650284456],"true", 3) )
    # Connections for obj88 (graphObject_: Obj85) of type require
    self.drawConnections(
(self.obj88,self.obj74,[340.414318871705, 195.90465454112874, 360.9395472052699, 168.3574950336234, 389.4836186264952, 146.78512887279376],"true", 3) )
    # Connections for obj89 (graphObject_: Obj86) of type require
    self.drawConnections(
(self.obj89,self.obj73,[244.92103503030822, 220.28528088040454, 216.79345843945703, 198.02060594998179, 194.87239892883093, 167.91506718112427],"true", 3) )
    # Connections for obj90 (graphObject_: Obj87) of type require
    self.drawConnections(
(self.obj90,self.obj73,[153.01081004957175, 221.9053316890469, 169.58431463977854, 192.45784848790922, 194.87239892883093, 167.91506718112427],"true", 3) )
    # Connections for obj91 (graphObject_: Obj88) of type require
    self.drawConnections(
(self.obj91,self.obj72,[67.38155529802249, 233.10874016814495, 40.486960156021546, 203.45178070451655, 21.0, 167.07716213116151],"true", 3) )

newfunction = omacsEx1_MDL

loadedMMName = 'omacs_META'

atom3version = '0.3'
