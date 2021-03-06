"""
__pnsEx1_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: sam
Modified: Sat May 13 07:48:25 2017
____________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from rawMaterial import *
from operatingUnit import *
from metarial import *
from product import *
from fromMaterial import *
from intoProduct import *
from fromRaw import *
from intoMaterial import *
from graph_intoProduct import *
from graph_rawMaterial import *
from graph_operatingUnit import *
from graph_product import *
from graph_intoMaterial import *
from graph_metarial import *
from graph_fromRaw import *
from graph_fromMaterial import *
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

def pnsEx1_MDL(self, rootNode, pnsRootNode=None):

    # --- Generating attributes code for ASG pns ---
    if( pnsRootNode ): 
        # author
        pnsRootNode.author.setValue('Annonymous')

        # description
        pnsRootNode.description.setValue('\n')
        pnsRootNode.description.setHeight(15)

        # name
        pnsRootNode.name.setValue('')
        pnsRootNode.name.setNone()
    # --- ASG attributes over ---


    self.obj1028=rawMaterial(self)
    self.obj1028.isGraphObjectVisual = True

    if(hasattr(self.obj1028, '_setHierarchicalLink')):
      self.obj1028._setHierarchicalLink(False)

    # MaxFlow
    self.obj1028.MaxFlow.setValue(999999)

    # price
    self.obj1028.price.setValue(5)

    # Name
    self.obj1028.Name.setValue('A1')

    # ReqFlow
    self.obj1028.ReqFlow.setValue(0)

    self.obj1028.graphClass_= graph_rawMaterial
    if self.genGraphics:
       new_obj = graph_rawMaterial(206,0,self.obj1028)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rawMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1028.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1028)
    self.globalAndLocalPostcondition(self.obj1028, rootNode)
    self.obj1028.postAction( rootNode.CREATE )

    self.obj1029=operatingUnit(self)
    self.obj1029.isGraphObjectVisual = True

    if(hasattr(self.obj1029, '_setHierarchicalLink')):
      self.obj1029._setHierarchicalLink(False)

    # OperCostProp
    self.obj1029.OperCostProp.setValue(0.5)

    # name
    self.obj1029.name.setValue('A1 R1')

    # OperCostFix
    self.obj1029.OperCostFix.setValue(0.0)

    self.obj1029.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(206,108,self.obj1029)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1029.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1029)
    self.globalAndLocalPostcondition(self.obj1029, rootNode)
    self.obj1029.postAction( rootNode.CREATE )

    self.obj1030=operatingUnit(self)
    self.obj1030.isGraphObjectVisual = True

    if(hasattr(self.obj1030, '_setHierarchicalLink')):
      self.obj1030._setHierarchicalLink(False)

    # OperCostProp
    self.obj1030.OperCostProp.setValue(1.0)

    # name
    self.obj1030.name.setValue('G1 OAF')

    # OperCostFix
    self.obj1030.OperCostFix.setValue(2.0)

    self.obj1030.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(0,450,self.obj1030)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1030.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1030)
    self.globalAndLocalPostcondition(self.obj1030, rootNode)
    self.obj1030.postAction( rootNode.CREATE )

    self.obj1031=operatingUnit(self)
    self.obj1031.isGraphObjectVisual = True

    if(hasattr(self.obj1031, '_setHierarchicalLink')):
      self.obj1031._setHierarchicalLink(False)

    # OperCostProp
    self.obj1031.OperCostProp.setValue(1.0)

    # name
    self.obj1031.name.setValue('G2 OAF')

    # OperCostFix
    self.obj1031.OperCostFix.setValue(2.0)

    self.obj1031.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(206,450,self.obj1031)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1031.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1031)
    self.globalAndLocalPostcondition(self.obj1031, rootNode)
    self.obj1031.postAction( rootNode.CREATE )

    self.obj1032=operatingUnit(self)
    self.obj1032.isGraphObjectVisual = True

    if(hasattr(self.obj1032, '_setHierarchicalLink')):
      self.obj1032._setHierarchicalLink(False)

    # OperCostProp
    self.obj1032.OperCostProp.setValue(0.11)

    # name
    self.obj1032.name.setValue('A1 R1 G1')

    # OperCostFix
    self.obj1032.OperCostFix.setValue(2.0)

    self.obj1032.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(0,279,self.obj1032)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1032.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1032)
    self.globalAndLocalPostcondition(self.obj1032, rootNode)
    self.obj1032.postAction( rootNode.CREATE )

    self.obj1033=operatingUnit(self)
    self.obj1033.isGraphObjectVisual = True

    if(hasattr(self.obj1033, '_setHierarchicalLink')):
      self.obj1033._setHierarchicalLink(False)

    # OperCostProp
    self.obj1033.OperCostProp.setValue(0.12)

    # name
    self.obj1033.name.setValue('A1 R1 G2')

    # OperCostFix
    self.obj1033.OperCostFix.setValue(2.0)

    self.obj1033.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(206,279,self.obj1033)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1033.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1033)
    self.globalAndLocalPostcondition(self.obj1033, rootNode)
    self.obj1033.postAction( rootNode.CREATE )

    self.obj1034=metarial(self)
    self.obj1034.isGraphObjectVisual = True

    if(hasattr(self.obj1034, '_setHierarchicalLink')):
      self.obj1034._setHierarchicalLink(False)

    # MaxFlow
    self.obj1034.MaxFlow.setValue(999999)

    # price
    self.obj1034.price.setValue(0)

    # Name
    self.obj1034.Name.setValue('G1')

    # ReqFlow
    self.obj1034.ReqFlow.setValue(0)

    self.obj1034.graphClass_= graph_metarial
    if self.genGraphics:
       new_obj = graph_metarial(0,350,self.obj1034)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("metarial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1034.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1034)
    self.globalAndLocalPostcondition(self.obj1034, rootNode)
    self.obj1034.postAction( rootNode.CREATE )

    self.obj1035=metarial(self)
    self.obj1035.isGraphObjectVisual = True

    if(hasattr(self.obj1035, '_setHierarchicalLink')):
      self.obj1035._setHierarchicalLink(False)

    # MaxFlow
    self.obj1035.MaxFlow.setValue(999999)

    # price
    self.obj1035.price.setValue(0)

    # Name
    self.obj1035.Name.setValue('G2')

    # ReqFlow
    self.obj1035.ReqFlow.setValue(0)

    self.obj1035.graphClass_= graph_metarial
    if self.genGraphics:
       new_obj = graph_metarial(206,350,self.obj1035)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("metarial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1035.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1035)
    self.globalAndLocalPostcondition(self.obj1035, rootNode)
    self.obj1035.postAction( rootNode.CREATE )

    self.obj1036=metarial(self)
    self.obj1036.isGraphObjectVisual = True

    if(hasattr(self.obj1036, '_setHierarchicalLink')):
      self.obj1036._setHierarchicalLink(False)

    # MaxFlow
    self.obj1036.MaxFlow.setValue(999999)

    # price
    self.obj1036.price.setValue(0)

    # Name
    self.obj1036.Name.setValue('A1 R1 G1')

    # ReqFlow
    self.obj1036.ReqFlow.setValue(0)

    self.obj1036.graphClass_= graph_metarial
    if self.genGraphics:
       new_obj = graph_metarial(0,179,self.obj1036)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("metarial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1036.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1036)
    self.globalAndLocalPostcondition(self.obj1036, rootNode)
    self.obj1036.postAction( rootNode.CREATE )

    self.obj1037=metarial(self)
    self.obj1037.isGraphObjectVisual = True

    if(hasattr(self.obj1037, '_setHierarchicalLink')):
      self.obj1037._setHierarchicalLink(False)

    # MaxFlow
    self.obj1037.MaxFlow.setValue(999999)

    # price
    self.obj1037.price.setValue(0)

    # Name
    self.obj1037.Name.setValue('A1 R1 G2')

    # ReqFlow
    self.obj1037.ReqFlow.setValue(0)

    self.obj1037.graphClass_= graph_metarial
    if self.genGraphics:
       new_obj = graph_metarial(206,179,self.obj1037)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("metarial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1037.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1037)
    self.globalAndLocalPostcondition(self.obj1037, rootNode)
    self.obj1037.postAction( rootNode.CREATE )

    self.obj1038=product(self)
    self.obj1038.isGraphObjectVisual = True

    if(hasattr(self.obj1038, '_setHierarchicalLink')):
      self.obj1038._setHierarchicalLink(False)

    # MaxFlow
    self.obj1038.MaxFlow.setValue(999999)

    # price
    self.obj1038.price.setValue(0)

    # Name
    self.obj1038.Name.setValue('OAF')

    # ReqFlow
    self.obj1038.ReqFlow.setValue(0)

    self.obj1038.graphClass_= graph_product
    if self.genGraphics:
       new_obj = graph_product(206,521,self.obj1038)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("product", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1038.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1038)
    self.globalAndLocalPostcondition(self.obj1038, rootNode)
    self.obj1038.postAction( rootNode.CREATE )

    self.obj1039=fromMaterial(self)
    self.obj1039.isGraphObjectVisual = True

    if(hasattr(self.obj1039, '_setHierarchicalLink')):
      self.obj1039._setHierarchicalLink(False)

    # rate
    self.obj1039.rate.setValue(1.0)

    self.obj1039.graphClass_= graph_fromMaterial
    if self.genGraphics:
       new_obj = graph_fromMaterial(32.005065672,430.467211341,self.obj1039)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1039.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1039)
    self.globalAndLocalPostcondition(self.obj1039, rootNode)
    self.obj1039.postAction( rootNode.CREATE )

    self.obj1040=fromMaterial(self)
    self.obj1040.isGraphObjectVisual = True

    if(hasattr(self.obj1040, '_setHierarchicalLink')):
      self.obj1040._setHierarchicalLink(False)

    # rate
    self.obj1040.rate.setValue(1.0)

    self.obj1040.graphClass_= graph_fromMaterial
    if self.genGraphics:
       new_obj = graph_fromMaterial(238.207284862,430.669455243,self.obj1040)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1040.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1040)
    self.globalAndLocalPostcondition(self.obj1040, rootNode)
    self.obj1040.postAction( rootNode.CREATE )

    self.obj1041=fromMaterial(self)
    self.obj1041.isGraphObjectVisual = True

    if(hasattr(self.obj1041, '_setHierarchicalLink')):
      self.obj1041._setHierarchicalLink(False)

    # rate
    self.obj1041.rate.setValue(1.0)

    self.obj1041.graphClass_= graph_fromMaterial
    if self.genGraphics:
       new_obj = graph_fromMaterial(51.4550432196,256.476547823,self.obj1041)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1041.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1041)
    self.globalAndLocalPostcondition(self.obj1041, rootNode)
    self.obj1041.postAction( rootNode.CREATE )

    self.obj1042=fromMaterial(self)
    self.obj1042.isGraphObjectVisual = True

    if(hasattr(self.obj1042, '_setHierarchicalLink')):
      self.obj1042._setHierarchicalLink(False)

    # rate
    self.obj1042.rate.setValue(1.0)

    self.obj1042.graphClass_= graph_fromMaterial
    if self.genGraphics:
       new_obj = graph_fromMaterial(257.45504322,256.476547823,self.obj1042)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1042.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1042)
    self.globalAndLocalPostcondition(self.obj1042, rootNode)
    self.obj1042.postAction( rootNode.CREATE )

    self.obj1043=intoProduct(self)
    self.obj1043.isGraphObjectVisual = True

    if(hasattr(self.obj1043, '_setHierarchicalLink')):
      self.obj1043._setHierarchicalLink(False)

    # rate
    self.obj1043.rate.setValue(1.0)

    self.obj1043.graphClass_= graph_intoProduct
    if self.genGraphics:
       new_obj = graph_intoProduct(144.868478175,484.858273262,self.obj1043)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoProduct", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1043.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1043)
    self.globalAndLocalPostcondition(self.obj1043, rootNode)
    self.obj1043.postAction( rootNode.CREATE )

    self.obj1044=intoProduct(self)
    self.obj1044.isGraphObjectVisual = True

    if(hasattr(self.obj1044, '_setHierarchicalLink')):
      self.obj1044._setHierarchicalLink(False)

    # rate
    self.obj1044.rate.setValue(1.0)

    self.obj1044.graphClass_= graph_intoProduct
    if self.genGraphics:
       new_obj = graph_intoProduct(238.187112626,493.499100791,self.obj1044)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoProduct", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1044.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1044)
    self.globalAndLocalPostcondition(self.obj1044, rootNode)
    self.obj1044.postAction( rootNode.CREATE )

    self.obj1045=fromRaw(self)
    self.obj1045.isGraphObjectVisual = True

    if(hasattr(self.obj1045, '_setHierarchicalLink')):
      self.obj1045._setHierarchicalLink(False)

    # rate
    self.obj1045.rate.setValue(1.0)

    self.obj1045.graphClass_= graph_fromRaw
    if self.genGraphics:
       new_obj = graph_fromRaw(237.772666213,87.9637186904,self.obj1045)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromRaw", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1045.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1045)
    self.globalAndLocalPostcondition(self.obj1045, rootNode)
    self.obj1045.postAction( rootNode.CREATE )

    self.obj1046=intoMaterial(self)
    self.obj1046.isGraphObjectVisual = True

    if(hasattr(self.obj1046, '_setHierarchicalLink')):
      self.obj1046._setHierarchicalLink(False)

    # rate
    self.obj1046.rate.setValue(0.11)

    self.obj1046.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(32.4226168069,321.008573698,self.obj1046)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1046.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1046)
    self.globalAndLocalPostcondition(self.obj1046, rootNode)
    self.obj1046.postAction( rootNode.CREATE )

    self.obj1047=intoMaterial(self)
    self.obj1047.isGraphObjectVisual = True

    if(hasattr(self.obj1047, '_setHierarchicalLink')):
      self.obj1047._setHierarchicalLink(False)

    # rate
    self.obj1047.rate.setValue(0.12)

    self.obj1047.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(238.390600655,321.222839546,self.obj1047)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1047.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1047)
    self.globalAndLocalPostcondition(self.obj1047, rootNode)
    self.obj1047.postAction( rootNode.CREATE )

    self.obj1048=intoMaterial(self)
    self.obj1048.isGraphObjectVisual = True

    if(hasattr(self.obj1048, '_setHierarchicalLink')):
      self.obj1048._setHierarchicalLink(False)

    # rate
    self.obj1048.rate.setValue(0.5)

    self.obj1048.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(143.686831985,166.822062776,self.obj1048)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1048.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1048)
    self.globalAndLocalPostcondition(self.obj1048, rootNode)
    self.obj1048.postAction( rootNode.CREATE )

    self.obj1049=intoMaterial(self)
    self.obj1049.isGraphObjectVisual = True

    if(hasattr(self.obj1049, '_setHierarchicalLink')):
      self.obj1049._setHierarchicalLink(False)

    # rate
    self.obj1049.rate.setValue(0.5)

    self.obj1049.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(242.68883419,148.342483174,self.obj1049)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1049.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1049)
    self.globalAndLocalPostcondition(self.obj1049, rootNode)
    self.obj1049.postAction( rootNode.CREATE )

    # Connections for obj1028 (graphObject_: Obj713) of type rawMaterial
    self.drawConnections(
(self.obj1028,self.obj1045,[229.7927616866, 55.830073958000014, 238.77266621273276, 72.21371869016248, 237.77266621258278, 87.96371869041248],"true", 3) )
    # Connections for obj1029 (graphObject_: Obj714) named A1 R1
    self.drawConnections(
(self.obj1029,self.obj1048,[224.792761686, 125.830073959, 185.99042726423008, 151.00958126939372, 143.68683198473008, 166.82206277614372],"true", 3),
(self.obj1029,self.obj1049,[224.792761686, 125.830073959, 238.49242946992584, 135.53000166744766, 242.68883419042584, 148.34248317419767],"true", 3) )
    # Connections for obj1030 (graphObject_: Obj715) named G1 OAF
    self.drawConnections(
(self.obj1030,self.obj1043,[53.0172746084, 467.88123386200004, 100.37279682732834, 471.57858172741805, 144.86847817522835, 484.85827326191804],"true", 3) )
    # Connections for obj1031 (graphObject_: Obj716) named G2 OAF
    self.drawConnections(
(self.obj1031,self.obj1044,[225.482036654, 468.072046504, 236.80762178979543, 480.2671124172909, 238.18711262629543, 493.49910079129086],"true", 3) )
    # Connections for obj1032 (graphObject_: Obj717) named A1 R1 G1
    self.drawConnections(
(self.obj1032,self.obj1046,[19.0, 297.0, 30.663979502928797, 308.3179567678522, 32.422616806928794, 321.00857369835217],"true", 3) )
    # Connections for obj1033 (graphObject_: Obj718) named A1 R1 G2
    self.drawConnections(
(self.obj1033,self.obj1047,[225.0, 297.0, 236.6495823288382, 308.4368162949629, 238.39060065533818, 321.2228395464629],"true", 3) )
    # Connections for obj1034 (graphObject_: Obj719) of type metarial
    self.drawConnections(
(self.obj1034,self.obj1039,[24.034549215999988, 398.7624677220001, 33.009384323918454, 414.9375198057641, 32.00506567201846, 430.4672113407641],"true", 3) )
    # Connections for obj1035 (graphObject_: Obj720) of type metarial
    self.drawConnections(
(self.obj1035,self.obj1040,[229.964073306, 399.14409300600005, 239.07779402486605, 415.18746686842474, 238.20728486186607, 430.6694552429247],"true", 3) )
    # Connections for obj1036 (graphObject_: Obj721) of type metarial
    self.drawConnections(
(self.obj1036,self.obj1041,[33.578380568, 228.07999998599996, 47.34963836160739, 240.9965478196302, 51.45504321960739, 256.4765478231302],"true", 3) )
    # Connections for obj1037 (graphObject_: Obj722) of type metarial
    self.drawConnections(
(self.obj1037,self.obj1042,[239.578380568, 228.07999998600008, 253.34963836160736, 240.99654781963028, 257.4550432196074, 256.47654782313026],"true", 3) )
    # Connections for obj1038 (graphObject_: Obj723) of type product
    self.drawConnections(
 )
    # Connections for obj1039 (graphObject_: Obj724) of type fromMaterial
    self.drawConnections(
(self.obj1039,self.obj1030,[32.00506567201846, 430.4672113407641, 31.00074702011846, 445.9969028757641, 20.0172746084, 460.88123386200004],"true", 3) )
    # Connections for obj1040 (graphObject_: Obj726) of type fromMaterial
    self.drawConnections(
(self.obj1040,self.obj1031,[238.20728486186607, 430.6694552429247, 237.3367756988661, 446.15144361742466, 226.482036654, 461.072046504],"true", 3) )
    # Connections for obj1041 (graphObject_: Obj728) of type fromMaterial
    self.drawConnections(
(self.obj1041,self.obj1032,[51.45504321960739, 256.4765478231302, 55.56044807760739, 271.95654782663024, 50.0, 290.0],"true", 3) )
    # Connections for obj1042 (graphObject_: Obj730) of type fromMaterial
    self.drawConnections(
(self.obj1042,self.obj1033,[257.4550432196074, 256.47654782313026, 261.5604480776074, 271.95654782663024, 256.0, 290.0],"true", 3) )
    # Connections for obj1043 (graphObject_: Obj732) of type intoProduct
    self.drawConnections(
(self.obj1043,self.obj1038,[144.86847817522835, 484.85827326191804, 189.3641595231283, 498.13796479641803, 231.0, 521.0],"true", 3) )
    # Connections for obj1044 (graphObject_: Obj734) of type intoProduct
    self.drawConnections(
(self.obj1044,self.obj1038,[238.18711262629543, 493.49910079129086, 239.56660346279543, 506.7310891652908, 231.0, 521.0],"true", 3) )
    # Connections for obj1045 (graphObject_: Obj736) of type fromRaw
    self.drawConnections(
(self.obj1045,self.obj1029,[237.77266621258278, 87.96371869041248, 236.7726662124328, 103.71371869066247, 225.792761686, 118.830073959],"true", 3) )
    # Connections for obj1046 (graphObject_: Obj738) of type intoMaterial
    self.drawConnections(
(self.obj1046,self.obj1034,[32.422616806928794, 321.00857369835217, 34.18125411092879, 333.69919062885214, 26.034549215999988, 347.762467722],"true", 3) )
    # Connections for obj1047 (graphObject_: Obj740) of type intoMaterial
    self.drawConnections(
(self.obj1047,self.obj1035,[238.39060065533818, 321.2228395464629, 240.13161898183816, 334.00886279796293, 231.964073306, 348.14409300600005],"true", 3) )
    # Connections for obj1048 (graphObject_: Obj742) of type intoMaterial
    self.drawConnections(
(self.obj1048,self.obj1036,[143.68683198473008, 166.82206277614372, 101.38323670523008, 182.63454428289373, 55.57838056800006, 189.07999998599996],"true", 3) )
    # Connections for obj1049 (graphObject_: Obj744) of type intoMaterial
    self.drawConnections(
(self.obj1049,self.obj1037,[242.68883419042584, 148.34248317419767, 246.88523891092584, 161.15496468094767, 241.578380568, 177.07999998600002],"true", 3) )

newfunction = pnsEx1_MDL

loadedMMName = 'pns_META'

atom3version = '0.3'
