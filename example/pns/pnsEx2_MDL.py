"""
__pnsEx2_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: sam
Modified: Sat May 13 08:00:57 2017
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

def pnsEx2_MDL(self, rootNode, pnsRootNode=None):

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


    self.obj2050=rawMaterial(self)
    self.obj2050.isGraphObjectVisual = True

    if(hasattr(self.obj2050, '_setHierarchicalLink')):
      self.obj2050._setHierarchicalLink(False)

    # MaxFlow
    self.obj2050.MaxFlow.setValue(999999)

    # price
    self.obj2050.price.setValue(5)

    # Name
    self.obj2050.Name.setValue('A1')

    # ReqFlow
    self.obj2050.ReqFlow.setValue(0)

    self.obj2050.graphClass_= graph_rawMaterial
    if self.genGraphics:
       new_obj = graph_rawMaterial(412,0,self.obj2050)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rawMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2050.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2050)
    self.globalAndLocalPostcondition(self.obj2050, rootNode)
    self.obj2050.postAction( rootNode.CREATE )

    self.obj2051=rawMaterial(self)
    self.obj2051.isGraphObjectVisual = True

    if(hasattr(self.obj2051, '_setHierarchicalLink')):
      self.obj2051._setHierarchicalLink(False)

    # MaxFlow
    self.obj2051.MaxFlow.setValue(999999)

    # price
    self.obj2051.price.setValue(5)

    # Name
    self.obj2051.Name.setValue('A2')

    # ReqFlow
    self.obj2051.ReqFlow.setValue(0)

    self.obj2051.graphClass_= graph_rawMaterial
    if self.genGraphics:
       new_obj = graph_rawMaterial(0,0,self.obj2051)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rawMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2051.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2051)
    self.globalAndLocalPostcondition(self.obj2051, rootNode)
    self.obj2051.postAction( rootNode.CREATE )

    self.obj2052=operatingUnit(self)
    self.obj2052.isGraphObjectVisual = True

    if(hasattr(self.obj2052, '_setHierarchicalLink')):
      self.obj2052._setHierarchicalLink(False)

    # OperCostProp
    self.obj2052.OperCostProp.setValue(0.5)

    # name
    self.obj2052.name.setValue('A1 R1')

    # OperCostFix
    self.obj2052.OperCostFix.setValue(0.0)

    self.obj2052.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(412,108,self.obj2052)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2052.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2052)
    self.globalAndLocalPostcondition(self.obj2052, rootNode)
    self.obj2052.postAction( rootNode.CREATE )

    self.obj2053=operatingUnit(self)
    self.obj2053.isGraphObjectVisual = True

    if(hasattr(self.obj2053, '_setHierarchicalLink')):
      self.obj2053._setHierarchicalLink(False)

    # OperCostProp
    self.obj2053.OperCostProp.setValue(0.25)

    # name
    self.obj2053.name.setValue('A2 R2')

    # OperCostFix
    self.obj2053.OperCostFix.setValue(0.0)

    self.obj2053.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(0,108,self.obj2053)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2053.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2053)
    self.globalAndLocalPostcondition(self.obj2053, rootNode)
    self.obj2053.postAction( rootNode.CREATE )

    self.obj2054=operatingUnit(self)
    self.obj2054.isGraphObjectVisual = True

    if(hasattr(self.obj2054, '_setHierarchicalLink')):
      self.obj2054._setHierarchicalLink(False)

    # OperCostProp
    self.obj2054.OperCostProp.setValue(1.0)

    # name
    self.obj2054.name.setValue('G1 OAF')

    # OperCostFix
    self.obj2054.OperCostFix.setValue(2.0)

    self.obj2054.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(412,450,self.obj2054)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2054.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2054)
    self.globalAndLocalPostcondition(self.obj2054, rootNode)
    self.obj2054.postAction( rootNode.CREATE )

    self.obj2055=operatingUnit(self)
    self.obj2055.isGraphObjectVisual = True

    if(hasattr(self.obj2055, '_setHierarchicalLink')):
      self.obj2055._setHierarchicalLink(False)

    # OperCostProp
    self.obj2055.OperCostProp.setValue(1.0)

    # name
    self.obj2055.name.setValue('G2 OAF')

    # OperCostFix
    self.obj2055.OperCostFix.setValue(2.0)

    self.obj2055.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(206,450,self.obj2055)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2055.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2055)
    self.globalAndLocalPostcondition(self.obj2055, rootNode)
    self.obj2055.postAction( rootNode.CREATE )

    self.obj2056=operatingUnit(self)
    self.obj2056.isGraphObjectVisual = True

    if(hasattr(self.obj2056, '_setHierarchicalLink')):
      self.obj2056._setHierarchicalLink(False)

    # OperCostProp
    self.obj2056.OperCostProp.setValue(0.11)

    # name
    self.obj2056.name.setValue('A1 R1 G1')

    # OperCostFix
    self.obj2056.OperCostFix.setValue(2.0)

    self.obj2056.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(412,279,self.obj2056)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2056.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2056)
    self.globalAndLocalPostcondition(self.obj2056, rootNode)
    self.obj2056.postAction( rootNode.CREATE )

    self.obj2057=operatingUnit(self)
    self.obj2057.isGraphObjectVisual = True

    if(hasattr(self.obj2057, '_setHierarchicalLink')):
      self.obj2057._setHierarchicalLink(False)

    # OperCostProp
    self.obj2057.OperCostProp.setValue(0.12)

    # name
    self.obj2057.name.setValue('A1 R1 G2')

    # OperCostFix
    self.obj2057.OperCostFix.setValue(2.0)

    self.obj2057.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(206,279,self.obj2057)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2057.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2057)
    self.globalAndLocalPostcondition(self.obj2057, rootNode)
    self.obj2057.postAction( rootNode.CREATE )

    self.obj2058=operatingUnit(self)
    self.obj2058.isGraphObjectVisual = True

    if(hasattr(self.obj2058, '_setHierarchicalLink')):
      self.obj2058._setHierarchicalLink(False)

    # OperCostProp
    self.obj2058.OperCostProp.setValue(0.22)

    # name
    self.obj2058.name.setValue('A2 R2 G2')

    # OperCostFix
    self.obj2058.OperCostFix.setValue(2.0)

    self.obj2058.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(0,279,self.obj2058)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2058.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2058)
    self.globalAndLocalPostcondition(self.obj2058, rootNode)
    self.obj2058.postAction( rootNode.CREATE )

    self.obj2059=metarial(self)
    self.obj2059.isGraphObjectVisual = True

    if(hasattr(self.obj2059, '_setHierarchicalLink')):
      self.obj2059._setHierarchicalLink(False)

    # MaxFlow
    self.obj2059.MaxFlow.setValue(999999)

    # price
    self.obj2059.price.setValue(0)

    # Name
    self.obj2059.Name.setValue('G1')

    # ReqFlow
    self.obj2059.ReqFlow.setValue(0)

    self.obj2059.graphClass_= graph_metarial
    if self.genGraphics:
       new_obj = graph_metarial(412,350,self.obj2059)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("metarial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2059.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2059)
    self.globalAndLocalPostcondition(self.obj2059, rootNode)
    self.obj2059.postAction( rootNode.CREATE )

    self.obj2060=metarial(self)
    self.obj2060.isGraphObjectVisual = True

    if(hasattr(self.obj2060, '_setHierarchicalLink')):
      self.obj2060._setHierarchicalLink(False)

    # MaxFlow
    self.obj2060.MaxFlow.setValue(999999)

    # price
    self.obj2060.price.setValue(0)

    # Name
    self.obj2060.Name.setValue('G2')

    # ReqFlow
    self.obj2060.ReqFlow.setValue(0)

    self.obj2060.graphClass_= graph_metarial
    if self.genGraphics:
       new_obj = graph_metarial(206,350,self.obj2060)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("metarial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2060.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2060)
    self.globalAndLocalPostcondition(self.obj2060, rootNode)
    self.obj2060.postAction( rootNode.CREATE )

    self.obj2061=metarial(self)
    self.obj2061.isGraphObjectVisual = True

    if(hasattr(self.obj2061, '_setHierarchicalLink')):
      self.obj2061._setHierarchicalLink(False)

    # MaxFlow
    self.obj2061.MaxFlow.setValue(999999)

    # price
    self.obj2061.price.setValue(0)

    # Name
    self.obj2061.Name.setValue('A1 R1 G1')

    # ReqFlow
    self.obj2061.ReqFlow.setValue(0)

    self.obj2061.graphClass_= graph_metarial
    if self.genGraphics:
       new_obj = graph_metarial(412,179,self.obj2061)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("metarial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2061.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2061)
    self.globalAndLocalPostcondition(self.obj2061, rootNode)
    self.obj2061.postAction( rootNode.CREATE )

    self.obj2062=metarial(self)
    self.obj2062.isGraphObjectVisual = True

    if(hasattr(self.obj2062, '_setHierarchicalLink')):
      self.obj2062._setHierarchicalLink(False)

    # MaxFlow
    self.obj2062.MaxFlow.setValue(999999)

    # price
    self.obj2062.price.setValue(0)

    # Name
    self.obj2062.Name.setValue('A1 R1 G2')

    # ReqFlow
    self.obj2062.ReqFlow.setValue(0)

    self.obj2062.graphClass_= graph_metarial
    if self.genGraphics:
       new_obj = graph_metarial(206,179,self.obj2062)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("metarial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2062.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2062)
    self.globalAndLocalPostcondition(self.obj2062, rootNode)
    self.obj2062.postAction( rootNode.CREATE )

    self.obj2063=metarial(self)
    self.obj2063.isGraphObjectVisual = True

    if(hasattr(self.obj2063, '_setHierarchicalLink')):
      self.obj2063._setHierarchicalLink(False)

    # MaxFlow
    self.obj2063.MaxFlow.setValue(999999)

    # price
    self.obj2063.price.setValue(0)

    # Name
    self.obj2063.Name.setValue('A2 R2 G2')

    # ReqFlow
    self.obj2063.ReqFlow.setValue(0)

    self.obj2063.graphClass_= graph_metarial
    if self.genGraphics:
       new_obj = graph_metarial(0,179,self.obj2063)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("metarial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2063.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2063)
    self.globalAndLocalPostcondition(self.obj2063, rootNode)
    self.obj2063.postAction( rootNode.CREATE )

    self.obj2064=product(self)
    self.obj2064.isGraphObjectVisual = True

    if(hasattr(self.obj2064, '_setHierarchicalLink')):
      self.obj2064._setHierarchicalLink(False)

    # MaxFlow
    self.obj2064.MaxFlow.setValue(999999)

    # price
    self.obj2064.price.setValue(0)

    # Name
    self.obj2064.Name.setValue('OAF')

    # ReqFlow
    self.obj2064.ReqFlow.setValue(0)

    self.obj2064.graphClass_= graph_product
    if self.genGraphics:
       new_obj = graph_product(412,521,self.obj2064)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("product", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2064.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2064)
    self.globalAndLocalPostcondition(self.obj2064, rootNode)
    self.obj2064.postAction( rootNode.CREATE )

    self.obj2065=fromMaterial(self)
    self.obj2065.isGraphObjectVisual = True

    if(hasattr(self.obj2065, '_setHierarchicalLink')):
      self.obj2065._setHierarchicalLink(False)

    # rate
    self.obj2065.rate.setValue(1.0)

    self.obj2065.graphClass_= graph_fromMaterial
    if self.genGraphics:
       new_obj = graph_fromMaterial(443.97925309,430.64382278,self.obj2065)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2065.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2065)
    self.globalAndLocalPostcondition(self.obj2065, rootNode)
    self.obj2065.postAction( rootNode.CREATE )

    self.obj2066=fromMaterial(self)
    self.obj2066.isGraphObjectVisual = True

    if(hasattr(self.obj2066, '_setHierarchicalLink')):
      self.obj2066._setHierarchicalLink(False)

    # rate
    self.obj2066.rate.setValue(1.0)

    self.obj2066.graphClass_= graph_fromMaterial
    if self.genGraphics:
       new_obj = graph_fromMaterial(237.97925309,430.64382278,self.obj2066)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2066.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2066)
    self.globalAndLocalPostcondition(self.obj2066, rootNode)
    self.obj2066.postAction( rootNode.CREATE )

    self.obj2067=fromMaterial(self)
    self.obj2067.isGraphObjectVisual = True

    if(hasattr(self.obj2067, '_setHierarchicalLink')):
      self.obj2067._setHierarchicalLink(False)

    # rate
    self.obj2067.rate.setValue(1.0)

    self.obj2067.graphClass_= graph_fromMaterial
    if self.genGraphics:
       new_obj = graph_fromMaterial(463.682773237,256.50121981,self.obj2067)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2067.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2067)
    self.globalAndLocalPostcondition(self.obj2067, rootNode)
    self.obj2067.postAction( rootNode.CREATE )

    self.obj2068=fromMaterial(self)
    self.obj2068.isGraphObjectVisual = True

    if(hasattr(self.obj2068, '_setHierarchicalLink')):
      self.obj2068._setHierarchicalLink(False)

    # rate
    self.obj2068.rate.setValue(1.0)

    self.obj2068.graphClass_= graph_fromMaterial
    if self.genGraphics:
       new_obj = graph_fromMaterial(257.682773237,256.50121981,self.obj2068)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2068.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2068)
    self.globalAndLocalPostcondition(self.obj2068, rootNode)
    self.obj2068.postAction( rootNode.CREATE )

    self.obj2069=fromMaterial(self)
    self.obj2069.isGraphObjectVisual = True

    if(hasattr(self.obj2069, '_setHierarchicalLink')):
      self.obj2069._setHierarchicalLink(False)

    # rate
    self.obj2069.rate.setValue(1.0)

    self.obj2069.graphClass_= graph_fromMaterial
    if self.genGraphics:
       new_obj = graph_fromMaterial(51.6827732371,256.50121981,self.obj2069)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2069.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2069)
    self.globalAndLocalPostcondition(self.obj2069, rootNode)
    self.obj2069.postAction( rootNode.CREATE )

    self.obj2070=intoProduct(self)
    self.obj2070.isGraphObjectVisual = True

    if(hasattr(self.obj2070, '_setHierarchicalLink')):
      self.obj2070._setHierarchicalLink(False)

    # rate
    self.obj2070.rate.setValue(1.0)

    self.obj2070.graphClass_= graph_intoProduct
    if self.genGraphics:
       new_obj = graph_intoProduct(443.936529683,493.375109847,self.obj2070)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoProduct", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2070.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2070)
    self.globalAndLocalPostcondition(self.obj2070, rootNode)
    self.obj2070.postAction( rootNode.CREATE )

    self.obj2071=intoProduct(self)
    self.obj2071.isGraphObjectVisual = True

    if(hasattr(self.obj2071, '_setHierarchicalLink')):
      self.obj2071._setHierarchicalLink(False)

    # rate
    self.obj2071.rate.setValue(1.0)

    self.obj2071.graphClass_= graph_intoProduct
    if self.genGraphics:
       new_obj = graph_intoProduct(350.853713603,484.915829787,self.obj2071)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoProduct", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2071.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2071)
    self.globalAndLocalPostcondition(self.obj2071, rootNode)
    self.obj2071.postAction( rootNode.CREATE )

    self.obj2072=fromRaw(self)
    self.obj2072.isGraphObjectVisual = True

    if(hasattr(self.obj2072, '_setHierarchicalLink')):
      self.obj2072._setHierarchicalLink(False)

    # rate
    self.obj2072.rate.setValue(1.0)

    self.obj2072.graphClass_= graph_fromRaw
    if self.genGraphics:
       new_obj = graph_fromRaw(443.979904526,88.1336447318,self.obj2072)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromRaw", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2072.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2072)
    self.globalAndLocalPostcondition(self.obj2072, rootNode)
    self.obj2072.postAction( rootNode.CREATE )

    self.obj2073=fromRaw(self)
    self.obj2073.isGraphObjectVisual = True

    if(hasattr(self.obj2073, '_setHierarchicalLink')):
      self.obj2073._setHierarchicalLink(False)

    # rate
    self.obj2073.rate.setValue(1.0)

    self.obj2073.graphClass_= graph_fromRaw
    if self.genGraphics:
       new_obj = graph_fromRaw(31.9799045263,88.1336447318,self.obj2073)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromRaw", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2073.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2073)
    self.globalAndLocalPostcondition(self.obj2073, rootNode)
    self.obj2073.postAction( rootNode.CREATE )

    self.obj2074=intoMaterial(self)
    self.obj2074.isGraphObjectVisual = True

    if(hasattr(self.obj2074, '_setHierarchicalLink')):
      self.obj2074._setHierarchicalLink(False)

    # rate
    self.obj2074.rate.setValue(0.11)

    self.obj2074.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(444.407115796,321.140199793,self.obj2074)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2074.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2074)
    self.globalAndLocalPostcondition(self.obj2074, rootNode)
    self.obj2074.postAction( rootNode.CREATE )

    self.obj2075=intoMaterial(self)
    self.obj2075.isGraphObjectVisual = True

    if(hasattr(self.obj2075, '_setHierarchicalLink')):
      self.obj2075._setHierarchicalLink(False)

    # rate
    self.obj2075.rate.setValue(0.12)

    self.obj2075.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(238.407115796,321.140199793,self.obj2075)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2075.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2075)
    self.globalAndLocalPostcondition(self.obj2075, rootNode)
    self.obj2075.postAction( rootNode.CREATE )

    self.obj2076=intoMaterial(self)
    self.obj2076.isGraphObjectVisual = True

    if(hasattr(self.obj2076, '_setHierarchicalLink')):
      self.obj2076._setHierarchicalLink(False)

    # rate
    self.obj2076.rate.setValue(0.22)

    self.obj2076.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(137.852377142,316.57866424,self.obj2076)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2076.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2076)
    self.globalAndLocalPostcondition(self.obj2076, rootNode)
    self.obj2076.postAction( rootNode.CREATE )

    self.obj2077=intoMaterial(self)
    self.obj2077.isGraphObjectVisual = True

    if(hasattr(self.obj2077, '_setHierarchicalLink')):
      self.obj2077._setHierarchicalLink(False)

    # rate
    self.obj2077.rate.setValue(0.5)

    self.obj2077.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(448.986832981,148.33772234,self.obj2077)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2077.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2077)
    self.globalAndLocalPostcondition(self.obj2077, rootNode)
    self.obj2077.postAction( rootNode.CREATE )

    self.obj2078=intoMaterial(self)
    self.obj2078.isGraphObjectVisual = True

    if(hasattr(self.obj2078, '_setHierarchicalLink')):
      self.obj2078._setHierarchicalLink(False)

    # rate
    self.obj2078.rate.setValue(0.5)

    self.obj2078.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(349.992999454,166.870109648,self.obj2078)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2078.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2078)
    self.globalAndLocalPostcondition(self.obj2078, rootNode)
    self.obj2078.postAction( rootNode.CREATE )

    self.obj2079=intoMaterial(self)
    self.obj2079.isGraphObjectVisual = True

    if(hasattr(self.obj2079, '_setHierarchicalLink')):
      self.obj2079._setHierarchicalLink(False)

    # rate
    self.obj2079.rate.setValue(0.25)

    self.obj2079.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(36.9868329805,148.33772234,self.obj2079)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2079.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2079)
    self.globalAndLocalPostcondition(self.obj2079, rootNode)
    self.obj2079.postAction( rootNode.CREATE )

    # Connections for obj2050 (graphObject_: Obj1645) of type rawMaterial
    self.drawConnections(
(self.obj2050,self.obj2072,[436.0, 56.0, 444.9799045262882, 72.38364473182781, 443.9799045262882, 88.13364473182781],"true", 3) )
    # Connections for obj2051 (graphObject_: Obj1646) of type rawMaterial
    self.drawConnections(
(self.obj2051,self.obj2073,[24.0, 56.0, 32.97990452628816, 72.38364473182781, 31.97990452628816, 88.13364473182781],"true", 3) )
    # Connections for obj2052 (graphObject_: Obj1647) named A1 R1
    self.drawConnections(
(self.obj2052,self.obj2077,[431.0, 126.0, 444.73683298050514, 135.58772233983163, 448.98683298050514, 148.33772233983163],"true", 3),
(self.obj2052,self.obj2078,[431.0, 126.0, 392.2429994544884, 151.1201096477546, 349.9929994544884, 166.8701096477546],"true", 3) )
    # Connections for obj2053 (graphObject_: Obj1648) named A2 R2
    self.drawConnections(
(self.obj2053,self.obj2079,[19.0, 126.0, 32.73683298050514, 135.58772233983163, 36.98683298050514, 148.33772233983163],"true", 3) )
    # Connections for obj2054 (graphObject_: Obj1649) named G1 OAF
    self.drawConnections(
(self.obj2054,self.obj2070,[431.0, 468.0, 442.43652968314956, 480.12510984719063, 443.93652968314956, 493.37510984719063],"true", 3) )
    # Connections for obj2055 (graphObject_: Obj1650) named G2 OAF
    self.drawConnections(
(self.obj2055,self.obj2071,[259.0, 468.0, 306.353713602772, 471.6658297869167, 350.853713602772, 484.9158297869167],"true", 3) )
    # Connections for obj2056 (graphObject_: Obj1651) named A1 R1 G1
    self.drawConnections(
(self.obj2056,self.obj2074,[431.0, 297.0, 442.6571157960441, 308.39019979269983, 444.4071157960441, 321.14019979269983],"true", 3) )
    # Connections for obj2057 (graphObject_: Obj1652) named A1 R1 G2
    self.drawConnections(
(self.obj2057,self.obj2075,[225.0, 297.0, 236.65711579604408, 308.39019979269983, 238.40711579604408, 321.14019979269983],"true", 3) )
    # Connections for obj2058 (graphObject_: Obj1653) named A2 R2 G2
    self.drawConnections(
(self.obj2058,self.obj2076,[53.0, 297.0, 97.10237714155916, 302.078664240101, 137.85237714155915, 316.578664240101],"true", 3) )
    # Connections for obj2059 (graphObject_: Obj1654) of type metarial
    self.drawConnections(
(self.obj2059,self.obj2065,[436.0, 399.0, 444.97925308968456, 415.14382277997964, 443.97925308968456, 430.64382277997964],"true", 3) )
    # Connections for obj2060 (graphObject_: Obj1655) of type metarial
    self.drawConnections(
(self.obj2060,self.obj2066,[230.0, 399.0, 238.9792530896846, 415.14382277997964, 237.9792530896846, 430.64382277997964],"true", 3) )
    # Connections for obj2061 (graphObject_: Obj1656) of type metarial
    self.drawConnections(
(self.obj2061,self.obj2067,[446.0, 228.0, 459.68277323709356, 241.0012198097823, 463.68277323709356, 256.5012198097823],"true", 3) )
    # Connections for obj2062 (graphObject_: Obj1657) of type metarial
    self.drawConnections(
(self.obj2062,self.obj2068,[240.0, 228.0, 253.68277323709358, 241.0012198097823, 257.68277323709356, 256.5012198097823],"true", 3) )
    # Connections for obj2063 (graphObject_: Obj1658) of type metarial
    self.drawConnections(
(self.obj2063,self.obj2069,[34.0, 228.0, 47.68277323709358, 241.0012198097823, 51.68277323709358, 256.5012198097823],"true", 3) )
    # Connections for obj2064 (graphObject_: Obj1659) of type product
    self.drawConnections(
 )
    # Connections for obj2065 (graphObject_: Obj1660) of type fromMaterial
    self.drawConnections(
(self.obj2065,self.obj2054,[443.97925308968456, 430.64382277997964, 442.97925308968456, 446.14382277997964, 432.0, 461.0],"true", 3) )
    # Connections for obj2066 (graphObject_: Obj1662) of type fromMaterial
    self.drawConnections(
(self.obj2066,self.obj2055,[237.9792530896846, 430.64382277997964, 236.9792530896846, 446.14382277997964, 226.0, 461.0],"true", 3) )
    # Connections for obj2067 (graphObject_: Obj1664) of type fromMaterial
    self.drawConnections(
(self.obj2067,self.obj2056,[463.68277323709356, 256.5012198097823, 467.68277323709356, 272.0012198097823, 462.0, 290.0],"true", 3) )
    # Connections for obj2068 (graphObject_: Obj1666) of type fromMaterial
    self.drawConnections(
(self.obj2068,self.obj2057,[257.68277323709356, 256.5012198097823, 261.68277323709356, 272.0012198097823, 256.0, 290.0],"true", 3) )
    # Connections for obj2069 (graphObject_: Obj1668) of type fromMaterial
    self.drawConnections(
(self.obj2069,self.obj2058,[51.68277323709358, 256.5012198097823, 55.68277323709358, 272.0012198097823, 50.0, 290.0],"true", 3) )
    # Connections for obj2070 (graphObject_: Obj1670) of type intoProduct
    self.drawConnections(
(self.obj2070,self.obj2064,[443.93652968314956, 493.37510984719063, 445.43652968314956, 506.62510984719063, 437.0, 521.0],"true", 3) )
    # Connections for obj2071 (graphObject_: Obj1672) of type intoProduct
    self.drawConnections(
(self.obj2071,self.obj2064,[350.853713602772, 484.9158297869167, 395.353713602772, 498.1658297869167, 437.0, 521.0],"true", 3) )
    # Connections for obj2072 (graphObject_: Obj1674) of type fromRaw
    self.drawConnections(
(self.obj2072,self.obj2052,[443.9799045262882, 88.13364473182781, 442.9799045262882, 103.88364473182781, 432.0, 119.0],"true", 3) )
    # Connections for obj2073 (graphObject_: Obj1676) of type fromRaw
    self.drawConnections(
(self.obj2073,self.obj2053,[31.97990452628816, 88.13364473182781, 30.97990452628816, 103.88364473182781, 20.0, 119.0],"true", 3) )
    # Connections for obj2074 (graphObject_: Obj1678) of type intoMaterial
    self.drawConnections(
(self.obj2074,self.obj2059,[444.4071157960441, 321.14019979269983, 446.1571157960441, 333.89019979269983, 438.0, 348.0],"true", 3) )
    # Connections for obj2075 (graphObject_: Obj1680) of type intoMaterial
    self.drawConnections(
(self.obj2075,self.obj2060,[238.40711579604408, 321.14019979269983, 240.15711579604408, 333.89019979269983, 232.0, 348.0],"true", 3) )
    # Connections for obj2076 (graphObject_: Obj1682) of type intoMaterial
    self.drawConnections(
(self.obj2076,self.obj2060,[137.85237714155915, 316.578664240101, 178.60237714155915, 331.078664240101, 216.0, 355.0],"true", 3) )
    # Connections for obj2077 (graphObject_: Obj1684) of type intoMaterial
    self.drawConnections(
(self.obj2077,self.obj2061,[448.98683298050514, 148.33772233983163, 453.23683298050514, 161.08772233983163, 448.0, 177.0],"true", 3) )
    # Connections for obj2078 (graphObject_: Obj1686) of type intoMaterial
    self.drawConnections(
(self.obj2078,self.obj2062,[349.9929994544884, 166.8701096477546, 307.7429994544884, 182.6201096477546, 262.0, 189.0],"true", 3) )
    # Connections for obj2079 (graphObject_: Obj1688) of type intoMaterial
    self.drawConnections(
(self.obj2079,self.obj2063,[36.98683298050514, 148.33772233983163, 41.23683298050514, 161.08772233983163, 36.0, 177.0],"true", 3) )

newfunction = pnsEx2_MDL

loadedMMName = 'pns_META'

atom3version = '0.3'
