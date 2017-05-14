"""
__pnsEx4_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: sam
Modified: Sat May 13 07:35:07 2017
____________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from rawMaterial import *
from product import *
from metarial import *
from operatingUnit import *
from fromRaw import *
from intoMaterial import *
from intoProduct import *
from fromMaterial import *
from graph_intoProduct import *
from graph_rawMaterial import *
from graph_operatingUnit import *
from graph_intoMaterial import *
from graph_metarial import *
from graph_fromRaw import *
from graph_product import *
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

def pnsEx4_MDL(self, rootNode, pnsRootNode=None):

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


    self.obj636=rawMaterial(self)
    self.obj636.isGraphObjectVisual = True

    if(hasattr(self.obj636, '_setHierarchicalLink')):
      self.obj636._setHierarchicalLink(False)

    # MaxFlow
    self.obj636.MaxFlow.setValue(999999)

    # price
    self.obj636.price.setValue(85)

    # Name
    self.obj636.Name.setValue('A1')

    # ReqFlow
    self.obj636.ReqFlow.setValue(0)

    self.obj636.graphClass_= graph_rawMaterial
    if self.genGraphics:
       new_obj = graph_rawMaterial(2472,0,self.obj636)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rawMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj636.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj636)
    self.globalAndLocalPostcondition(self.obj636, rootNode)
    self.obj636.postAction( rootNode.CREATE )

    self.obj637=rawMaterial(self)
    self.obj637.isGraphObjectVisual = True

    if(hasattr(self.obj637, '_setHierarchicalLink')):
      self.obj637._setHierarchicalLink(False)

    # MaxFlow
    self.obj637.MaxFlow.setValue(999999)

    # price
    self.obj637.price.setValue(90)

    # Name
    self.obj637.Name.setValue('A2')

    # ReqFlow
    self.obj637.ReqFlow.setValue(0)

    self.obj637.graphClass_= graph_rawMaterial
    if self.genGraphics:
       new_obj = graph_rawMaterial(1236,0,self.obj637)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rawMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj637.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj637)
    self.globalAndLocalPostcondition(self.obj637, rootNode)
    self.obj637.postAction( rootNode.CREATE )

    self.obj638=rawMaterial(self)
    self.obj638.isGraphObjectVisual = True

    if(hasattr(self.obj638, '_setHierarchicalLink')):
      self.obj638._setHierarchicalLink(False)

    # MaxFlow
    self.obj638.MaxFlow.setValue(999999)

    # price
    self.obj638.price.setValue(95)

    # Name
    self.obj638.Name.setValue('A3')

    # ReqFlow
    self.obj638.ReqFlow.setValue(0)

    self.obj638.graphClass_= graph_rawMaterial
    if self.genGraphics:
       new_obj = graph_rawMaterial(412,0,self.obj638)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rawMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj638.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj638)
    self.globalAndLocalPostcondition(self.obj638, rootNode)
    self.obj638.postAction( rootNode.CREATE )

    self.obj639=product(self)
    self.obj639.isGraphObjectVisual = True

    if(hasattr(self.obj639, '_setHierarchicalLink')):
      self.obj639._setHierarchicalLink(False)

    # MaxFlow
    self.obj639.MaxFlow.setValue(999999)

    # price
    self.obj639.price.setValue(0)

    # Name
    self.obj639.Name.setValue('OAF')

    # ReqFlow
    self.obj639.ReqFlow.setValue(0)

    self.obj639.graphClass_= graph_product
    if self.genGraphics:
       new_obj = graph_product(1648,521,self.obj639)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("product", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj639.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj639)
    self.globalAndLocalPostcondition(self.obj639, rootNode)
    self.obj639.postAction( rootNode.CREATE )

    self.obj640=metarial(self)
    self.obj640.isGraphObjectVisual = True

    if(hasattr(self.obj640, '_setHierarchicalLink')):
      self.obj640._setHierarchicalLink(False)

    # MaxFlow
    self.obj640.MaxFlow.setValue(999999)

    # price
    self.obj640.price.setValue(0)

    # Name
    self.obj640.Name.setValue('G1')

    # ReqFlow
    self.obj640.ReqFlow.setValue(0)

    self.obj640.graphClass_= graph_metarial
    if self.genGraphics:
       new_obj = graph_metarial(1648,350,self.obj640)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("metarial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj640.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj640)
    self.globalAndLocalPostcondition(self.obj640, rootNode)
    self.obj640.postAction( rootNode.CREATE )

    self.obj641=metarial(self)
    self.obj641.isGraphObjectVisual = True

    if(hasattr(self.obj641, '_setHierarchicalLink')):
      self.obj641._setHierarchicalLink(False)

    # MaxFlow
    self.obj641.MaxFlow.setValue(999999)

    # price
    self.obj641.price.setValue(0)

    # Name
    self.obj641.Name.setValue('G2')

    # ReqFlow
    self.obj641.ReqFlow.setValue(0)

    self.obj641.graphClass_= graph_metarial
    if self.genGraphics:
       new_obj = graph_metarial(1236,350,self.obj641)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("metarial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj641.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj641)
    self.globalAndLocalPostcondition(self.obj641, rootNode)
    self.obj641.postAction( rootNode.CREATE )

    self.obj642=metarial(self)
    self.obj642.isGraphObjectVisual = True

    if(hasattr(self.obj642, '_setHierarchicalLink')):
      self.obj642._setHierarchicalLink(False)

    # MaxFlow
    self.obj642.MaxFlow.setValue(999999)

    # price
    self.obj642.price.setValue(0)

    # Name
    self.obj642.Name.setValue('G3')

    # ReqFlow
    self.obj642.ReqFlow.setValue(0)

    self.obj642.graphClass_= graph_metarial
    if self.genGraphics:
       new_obj = graph_metarial(1854,350,self.obj642)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("metarial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj642.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj642)
    self.globalAndLocalPostcondition(self.obj642, rootNode)
    self.obj642.postAction( rootNode.CREATE )

    self.obj643=metarial(self)
    self.obj643.isGraphObjectVisual = True

    if(hasattr(self.obj643, '_setHierarchicalLink')):
      self.obj643._setHierarchicalLink(False)

    # MaxFlow
    self.obj643.MaxFlow.setValue(999999)

    # price
    self.obj643.price.setValue(0)

    # Name
    self.obj643.Name.setValue('G4')

    # ReqFlow
    self.obj643.ReqFlow.setValue(0)

    self.obj643.graphClass_= graph_metarial
    if self.genGraphics:
       new_obj = graph_metarial(1442,350,self.obj643)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("metarial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj643.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj643)
    self.globalAndLocalPostcondition(self.obj643, rootNode)
    self.obj643.postAction( rootNode.CREATE )

    self.obj644=metarial(self)
    self.obj644.isGraphObjectVisual = True

    if(hasattr(self.obj644, '_setHierarchicalLink')):
      self.obj644._setHierarchicalLink(False)

    # MaxFlow
    self.obj644.MaxFlow.setValue(999999)

    # price
    self.obj644.price.setValue(0)

    # Name
    self.obj644.Name.setValue('A1 R1 G1')

    # ReqFlow
    self.obj644.ReqFlow.setValue(0)

    self.obj644.graphClass_= graph_metarial
    if self.genGraphics:
       new_obj = graph_metarial(2060,179,self.obj644)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("metarial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj644.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj644)
    self.globalAndLocalPostcondition(self.obj644, rootNode)
    self.obj644.postAction( rootNode.CREATE )

    self.obj645=metarial(self)
    self.obj645.isGraphObjectVisual = True

    if(hasattr(self.obj645, '_setHierarchicalLink')):
      self.obj645._setHierarchicalLink(False)

    # MaxFlow
    self.obj645.MaxFlow.setValue(999999)

    # price
    self.obj645.price.setValue(0)

    # Name
    self.obj645.Name.setValue('A1 R1 G4')

    # ReqFlow
    self.obj645.ReqFlow.setValue(0)

    self.obj645.graphClass_= graph_metarial
    if self.genGraphics:
       new_obj = graph_metarial(1854,179,self.obj645)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("metarial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj645.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj645)
    self.globalAndLocalPostcondition(self.obj645, rootNode)
    self.obj645.postAction( rootNode.CREATE )

    self.obj646=metarial(self)
    self.obj646.isGraphObjectVisual = True

    if(hasattr(self.obj646, '_setHierarchicalLink')):
      self.obj646._setHierarchicalLink(False)

    # MaxFlow
    self.obj646.MaxFlow.setValue(999999)

    # price
    self.obj646.price.setValue(0)

    # Name
    self.obj646.Name.setValue('A1 R1 G3')

    # ReqFlow
    self.obj646.ReqFlow.setValue(0)

    self.obj646.graphClass_= graph_metarial
    if self.genGraphics:
       new_obj = graph_metarial(2266,179,self.obj646)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("metarial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj646.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj646)
    self.globalAndLocalPostcondition(self.obj646, rootNode)
    self.obj646.postAction( rootNode.CREATE )

    self.obj647=metarial(self)
    self.obj647.isGraphObjectVisual = True

    if(hasattr(self.obj647, '_setHierarchicalLink')):
      self.obj647._setHierarchicalLink(False)

    # MaxFlow
    self.obj647.MaxFlow.setValue(999999)

    # price
    self.obj647.price.setValue(0)

    # Name
    self.obj647.Name.setValue('A1 R1 G2')

    # ReqFlow
    self.obj647.ReqFlow.setValue(0)

    self.obj647.graphClass_= graph_metarial
    if self.genGraphics:
       new_obj = graph_metarial(1648,179,self.obj647)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("metarial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj647.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj647)
    self.globalAndLocalPostcondition(self.obj647, rootNode)
    self.obj647.postAction( rootNode.CREATE )

    self.obj648=metarial(self)
    self.obj648.isGraphObjectVisual = True

    if(hasattr(self.obj648, '_setHierarchicalLink')):
      self.obj648._setHierarchicalLink(False)

    # MaxFlow
    self.obj648.MaxFlow.setValue(999999)

    # price
    self.obj648.price.setValue(0)

    # Name
    self.obj648.Name.setValue('A1 R2 G4')

    # ReqFlow
    self.obj648.ReqFlow.setValue(0)

    self.obj648.graphClass_= graph_metarial
    if self.genGraphics:
       new_obj = graph_metarial(2678,179,self.obj648)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("metarial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj648.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj648)
    self.globalAndLocalPostcondition(self.obj648, rootNode)
    self.obj648.postAction( rootNode.CREATE )

    self.obj649=metarial(self)
    self.obj649.isGraphObjectVisual = True

    if(hasattr(self.obj649, '_setHierarchicalLink')):
      self.obj649._setHierarchicalLink(False)

    # MaxFlow
    self.obj649.MaxFlow.setValue(999999)

    # price
    self.obj649.price.setValue(0)

    # Name
    self.obj649.Name.setValue('A1 R2 G3')

    # ReqFlow
    self.obj649.ReqFlow.setValue(0)

    self.obj649.graphClass_= graph_metarial
    if self.genGraphics:
       new_obj = graph_metarial(3090,179,self.obj649)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("metarial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj649.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj649)
    self.globalAndLocalPostcondition(self.obj649, rootNode)
    self.obj649.postAction( rootNode.CREATE )

    self.obj650=metarial(self)
    self.obj650.isGraphObjectVisual = True

    if(hasattr(self.obj650, '_setHierarchicalLink')):
      self.obj650._setHierarchicalLink(False)

    # MaxFlow
    self.obj650.MaxFlow.setValue(999999)

    # price
    self.obj650.price.setValue(0)

    # Name
    self.obj650.Name.setValue('A1 R2 G2')

    # ReqFlow
    self.obj650.ReqFlow.setValue(0)

    self.obj650.graphClass_= graph_metarial
    if self.genGraphics:
       new_obj = graph_metarial(2472,179,self.obj650)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("metarial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj650.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj650)
    self.globalAndLocalPostcondition(self.obj650, rootNode)
    self.obj650.postAction( rootNode.CREATE )

    self.obj651=metarial(self)
    self.obj651.isGraphObjectVisual = True

    if(hasattr(self.obj651, '_setHierarchicalLink')):
      self.obj651._setHierarchicalLink(False)

    # MaxFlow
    self.obj651.MaxFlow.setValue(999999)

    # price
    self.obj651.price.setValue(0)

    # Name
    self.obj651.Name.setValue('A1 R2 G1')

    # ReqFlow
    self.obj651.ReqFlow.setValue(0)

    self.obj651.graphClass_= graph_metarial
    if self.genGraphics:
       new_obj = graph_metarial(2884,179,self.obj651)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("metarial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj651.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj651)
    self.globalAndLocalPostcondition(self.obj651, rootNode)
    self.obj651.postAction( rootNode.CREATE )

    self.obj652=metarial(self)
    self.obj652.isGraphObjectVisual = True

    if(hasattr(self.obj652, '_setHierarchicalLink')):
      self.obj652._setHierarchicalLink(False)

    # MaxFlow
    self.obj652.MaxFlow.setValue(999999)

    # price
    self.obj652.price.setValue(0)

    # Name
    self.obj652.Name.setValue('A2 R2 G4')

    # ReqFlow
    self.obj652.ReqFlow.setValue(0)

    self.obj652.graphClass_= graph_metarial
    if self.genGraphics:
       new_obj = graph_metarial(1030,179,self.obj652)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("metarial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj652.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj652)
    self.globalAndLocalPostcondition(self.obj652, rootNode)
    self.obj652.postAction( rootNode.CREATE )

    self.obj653=metarial(self)
    self.obj653.isGraphObjectVisual = True

    if(hasattr(self.obj653, '_setHierarchicalLink')):
      self.obj653._setHierarchicalLink(False)

    # MaxFlow
    self.obj653.MaxFlow.setValue(999999)

    # price
    self.obj653.price.setValue(0)

    # Name
    self.obj653.Name.setValue('A2 R2 G3')

    # ReqFlow
    self.obj653.ReqFlow.setValue(0)

    self.obj653.graphClass_= graph_metarial
    if self.genGraphics:
       new_obj = graph_metarial(1442,179,self.obj653)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("metarial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj653.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj653)
    self.globalAndLocalPostcondition(self.obj653, rootNode)
    self.obj653.postAction( rootNode.CREATE )

    self.obj654=metarial(self)
    self.obj654.isGraphObjectVisual = True

    if(hasattr(self.obj654, '_setHierarchicalLink')):
      self.obj654._setHierarchicalLink(False)

    # MaxFlow
    self.obj654.MaxFlow.setValue(999999)

    # price
    self.obj654.price.setValue(0)

    # Name
    self.obj654.Name.setValue('A2 R2 G2')

    # ReqFlow
    self.obj654.ReqFlow.setValue(0)

    self.obj654.graphClass_= graph_metarial
    if self.genGraphics:
       new_obj = graph_metarial(824,179,self.obj654)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("metarial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj654.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj654)
    self.globalAndLocalPostcondition(self.obj654, rootNode)
    self.obj654.postAction( rootNode.CREATE )

    self.obj655=metarial(self)
    self.obj655.isGraphObjectVisual = True

    if(hasattr(self.obj655, '_setHierarchicalLink')):
      self.obj655._setHierarchicalLink(False)

    # MaxFlow
    self.obj655.MaxFlow.setValue(999999)

    # price
    self.obj655.price.setValue(0)

    # Name
    self.obj655.Name.setValue('A2 R2 G1')

    # ReqFlow
    self.obj655.ReqFlow.setValue(0)

    self.obj655.graphClass_= graph_metarial
    if self.genGraphics:
       new_obj = graph_metarial(1236,179,self.obj655)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("metarial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj655.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj655)
    self.globalAndLocalPostcondition(self.obj655, rootNode)
    self.obj655.postAction( rootNode.CREATE )

    self.obj656=metarial(self)
    self.obj656.isGraphObjectVisual = True

    if(hasattr(self.obj656, '_setHierarchicalLink')):
      self.obj656._setHierarchicalLink(False)

    # MaxFlow
    self.obj656.MaxFlow.setValue(999999)

    # price
    self.obj656.price.setValue(0)

    # Name
    self.obj656.Name.setValue('A3 R2 G4')

    # ReqFlow
    self.obj656.ReqFlow.setValue(0)

    self.obj656.graphClass_= graph_metarial
    if self.genGraphics:
       new_obj = graph_metarial(206,179,self.obj656)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("metarial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj656.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj656)
    self.globalAndLocalPostcondition(self.obj656, rootNode)
    self.obj656.postAction( rootNode.CREATE )

    self.obj657=metarial(self)
    self.obj657.isGraphObjectVisual = True

    if(hasattr(self.obj657, '_setHierarchicalLink')):
      self.obj657._setHierarchicalLink(False)

    # MaxFlow
    self.obj657.MaxFlow.setValue(999999)

    # price
    self.obj657.price.setValue(0)

    # Name
    self.obj657.Name.setValue('A3 R2 G3')

    # ReqFlow
    self.obj657.ReqFlow.setValue(0)

    self.obj657.graphClass_= graph_metarial
    if self.genGraphics:
       new_obj = graph_metarial(618,179,self.obj657)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("metarial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj657.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj657)
    self.globalAndLocalPostcondition(self.obj657, rootNode)
    self.obj657.postAction( rootNode.CREATE )

    self.obj658=metarial(self)
    self.obj658.isGraphObjectVisual = True

    if(hasattr(self.obj658, '_setHierarchicalLink')):
      self.obj658._setHierarchicalLink(False)

    # MaxFlow
    self.obj658.MaxFlow.setValue(999999)

    # price
    self.obj658.price.setValue(0)

    # Name
    self.obj658.Name.setValue('A3 R2 G2')

    # ReqFlow
    self.obj658.ReqFlow.setValue(0)

    self.obj658.graphClass_= graph_metarial
    if self.genGraphics:
       new_obj = graph_metarial(0,179,self.obj658)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("metarial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj658.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj658)
    self.globalAndLocalPostcondition(self.obj658, rootNode)
    self.obj658.postAction( rootNode.CREATE )

    self.obj659=metarial(self)
    self.obj659.isGraphObjectVisual = True

    if(hasattr(self.obj659, '_setHierarchicalLink')):
      self.obj659._setHierarchicalLink(False)

    # MaxFlow
    self.obj659.MaxFlow.setValue(999999)

    # price
    self.obj659.price.setValue(0)

    # Name
    self.obj659.Name.setValue('A3 R2 G1')

    # ReqFlow
    self.obj659.ReqFlow.setValue(0)

    self.obj659.graphClass_= graph_metarial
    if self.genGraphics:
       new_obj = graph_metarial(412,179,self.obj659)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("metarial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj659.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj659)
    self.globalAndLocalPostcondition(self.obj659, rootNode)
    self.obj659.postAction( rootNode.CREATE )

    self.obj660=operatingUnit(self)
    self.obj660.isGraphObjectVisual = True

    if(hasattr(self.obj660, '_setHierarchicalLink')):
      self.obj660._setHierarchicalLink(False)

    # OperCostProp
    self.obj660.OperCostProp.setValue(0.433333333333)

    # name
    self.obj660.name.setValue('A1 R1')

    # OperCostFix
    self.obj660.OperCostFix.setValue(0.0)

    self.obj660.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(2472,108,self.obj660)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj660.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj660)
    self.globalAndLocalPostcondition(self.obj660, rootNode)
    self.obj660.postAction( rootNode.CREATE )

    self.obj661=operatingUnit(self)
    self.obj661.isGraphObjectVisual = True

    if(hasattr(self.obj661, '_setHierarchicalLink')):
      self.obj661._setHierarchicalLink(False)

    # OperCostProp
    self.obj661.OperCostProp.setValue(0.433333333333)

    # name
    self.obj661.name.setValue('A1 R2')

    # OperCostFix
    self.obj661.OperCostFix.setValue(0.0)

    self.obj661.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(2678,108,self.obj661)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj661.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj661)
    self.globalAndLocalPostcondition(self.obj661, rootNode)
    self.obj661.postAction( rootNode.CREATE )

    self.obj662=operatingUnit(self)
    self.obj662.isGraphObjectVisual = True

    if(hasattr(self.obj662, '_setHierarchicalLink')):
      self.obj662._setHierarchicalLink(False)

    # OperCostProp
    self.obj662.OperCostProp.setValue(0.633333333333)

    # name
    self.obj662.name.setValue('A2 R2')

    # OperCostFix
    self.obj662.OperCostFix.setValue(0.0)

    self.obj662.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(1236,108,self.obj662)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj662.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj662)
    self.globalAndLocalPostcondition(self.obj662, rootNode)
    self.obj662.postAction( rootNode.CREATE )

    self.obj663=operatingUnit(self)
    self.obj663.isGraphObjectVisual = True

    if(hasattr(self.obj663, '_setHierarchicalLink')):
      self.obj663._setHierarchicalLink(False)

    # OperCostProp
    self.obj663.OperCostProp.setValue(0.5)

    # name
    self.obj663.name.setValue('A3 R2')

    # OperCostFix
    self.obj663.OperCostFix.setValue(0.0)

    self.obj663.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(412,108,self.obj663)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj663.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj663)
    self.globalAndLocalPostcondition(self.obj663, rootNode)
    self.obj663.postAction( rootNode.CREATE )

    self.obj664=operatingUnit(self)
    self.obj664.isGraphObjectVisual = True

    if(hasattr(self.obj664, '_setHierarchicalLink')):
      self.obj664._setHierarchicalLink(False)

    # OperCostProp
    self.obj664.OperCostProp.setValue(1.0)

    # name
    self.obj664.name.setValue('G1 OAF')

    # OperCostFix
    self.obj664.OperCostFix.setValue(2.0)

    self.obj664.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(1648,450,self.obj664)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj664.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj664)
    self.globalAndLocalPostcondition(self.obj664, rootNode)
    self.obj664.postAction( rootNode.CREATE )

    self.obj665=operatingUnit(self)
    self.obj665.isGraphObjectVisual = True

    if(hasattr(self.obj665, '_setHierarchicalLink')):
      self.obj665._setHierarchicalLink(False)

    # OperCostProp
    self.obj665.OperCostProp.setValue(1.0)

    # name
    self.obj665.name.setValue('G2 OAF')

    # OperCostFix
    self.obj665.OperCostFix.setValue(2.0)

    self.obj665.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(1236,450,self.obj665)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj665.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj665)
    self.globalAndLocalPostcondition(self.obj665, rootNode)
    self.obj665.postAction( rootNode.CREATE )

    self.obj666=operatingUnit(self)
    self.obj666.isGraphObjectVisual = True

    if(hasattr(self.obj666, '_setHierarchicalLink')):
      self.obj666._setHierarchicalLink(False)

    # OperCostProp
    self.obj666.OperCostProp.setValue(1.0)

    # name
    self.obj666.name.setValue('G3 OAF')

    # OperCostFix
    self.obj666.OperCostFix.setValue(2.0)

    self.obj666.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(1854,450,self.obj666)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj666.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj666)
    self.globalAndLocalPostcondition(self.obj666, rootNode)
    self.obj666.postAction( rootNode.CREATE )

    self.obj667=operatingUnit(self)
    self.obj667.isGraphObjectVisual = True

    if(hasattr(self.obj667, '_setHierarchicalLink')):
      self.obj667._setHierarchicalLink(False)

    # OperCostProp
    self.obj667.OperCostProp.setValue(1.0)

    # name
    self.obj667.name.setValue('G4 OAF')

    # OperCostFix
    self.obj667.OperCostFix.setValue(2.0)

    self.obj667.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(1442,450,self.obj667)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj667.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj667)
    self.globalAndLocalPostcondition(self.obj667, rootNode)
    self.obj667.postAction( rootNode.CREATE )

    self.obj668=operatingUnit(self)
    self.obj668.isGraphObjectVisual = True

    if(hasattr(self.obj668, '_setHierarchicalLink')):
      self.obj668._setHierarchicalLink(False)

    # OperCostProp
    self.obj668.OperCostProp.setValue(0.2)

    # name
    self.obj668.name.setValue('A1 R1 G1')

    # OperCostFix
    self.obj668.OperCostFix.setValue(2.0)

    self.obj668.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(2060,279,self.obj668)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj668.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj668)
    self.globalAndLocalPostcondition(self.obj668, rootNode)
    self.obj668.postAction( rootNode.CREATE )

    self.obj669=operatingUnit(self)
    self.obj669.isGraphObjectVisual = True

    if(hasattr(self.obj669, '_setHierarchicalLink')):
      self.obj669._setHierarchicalLink(False)

    # OperCostProp
    self.obj669.OperCostProp.setValue(0.8)

    # name
    self.obj669.name.setValue('A1 R1 G4')

    # OperCostFix
    self.obj669.OperCostFix.setValue(2.0)

    self.obj669.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(1854,279,self.obj669)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj669.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj669)
    self.globalAndLocalPostcondition(self.obj669, rootNode)
    self.obj669.postAction( rootNode.CREATE )

    self.obj670=operatingUnit(self)
    self.obj670.isGraphObjectVisual = True

    if(hasattr(self.obj670, '_setHierarchicalLink')):
      self.obj670._setHierarchicalLink(False)

    # OperCostProp
    self.obj670.OperCostProp.setValue(0.6)

    # name
    self.obj670.name.setValue('A1 R1 G3')

    # OperCostFix
    self.obj670.OperCostFix.setValue(2.0)

    self.obj670.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(2266,279,self.obj670)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj670.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj670)
    self.globalAndLocalPostcondition(self.obj670, rootNode)
    self.obj670.postAction( rootNode.CREATE )

    self.obj671=operatingUnit(self)
    self.obj671.isGraphObjectVisual = True

    if(hasattr(self.obj671, '_setHierarchicalLink')):
      self.obj671._setHierarchicalLink(False)

    # OperCostProp
    self.obj671.OperCostProp.setValue(0.4)

    # name
    self.obj671.name.setValue('A1 R1 G2')

    # OperCostFix
    self.obj671.OperCostFix.setValue(2.0)

    self.obj671.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(1648,279,self.obj671)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj671.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj671)
    self.globalAndLocalPostcondition(self.obj671, rootNode)
    self.obj671.postAction( rootNode.CREATE )

    self.obj672=operatingUnit(self)
    self.obj672.isGraphObjectVisual = True

    if(hasattr(self.obj672, '_setHierarchicalLink')):
      self.obj672._setHierarchicalLink(False)

    # OperCostProp
    self.obj672.OperCostProp.setValue(0.1)

    # name
    self.obj672.name.setValue('A1 R2 G4')

    # OperCostFix
    self.obj672.OperCostFix.setValue(2.0)

    self.obj672.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(2678,279,self.obj672)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj672.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj672)
    self.globalAndLocalPostcondition(self.obj672, rootNode)
    self.obj672.postAction( rootNode.CREATE )

    self.obj673=operatingUnit(self)
    self.obj673.isGraphObjectVisual = True

    if(hasattr(self.obj673, '_setHierarchicalLink')):
      self.obj673._setHierarchicalLink(False)

    # OperCostProp
    self.obj673.OperCostProp.setValue(0.4)

    # name
    self.obj673.name.setValue('A1 R2 G3')

    # OperCostFix
    self.obj673.OperCostFix.setValue(2.0)

    self.obj673.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(3090,279,self.obj673)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj673.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj673)
    self.globalAndLocalPostcondition(self.obj673, rootNode)
    self.obj673.postAction( rootNode.CREATE )

    self.obj674=operatingUnit(self)
    self.obj674.isGraphObjectVisual = True

    if(hasattr(self.obj674, '_setHierarchicalLink')):
      self.obj674._setHierarchicalLink(False)

    # OperCostProp
    self.obj674.OperCostProp.setValue(0.7)

    # name
    self.obj674.name.setValue('A1 R2 G2')

    # OperCostFix
    self.obj674.OperCostFix.setValue(2.0)

    self.obj674.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(2472,279,self.obj674)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj674.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj674)
    self.globalAndLocalPostcondition(self.obj674, rootNode)
    self.obj674.postAction( rootNode.CREATE )

    self.obj675=operatingUnit(self)
    self.obj675.isGraphObjectVisual = True

    if(hasattr(self.obj675, '_setHierarchicalLink')):
      self.obj675._setHierarchicalLink(False)

    # OperCostProp
    self.obj675.OperCostProp.setValue(1.0)

    # name
    self.obj675.name.setValue('A1 R2 G1')

    # OperCostFix
    self.obj675.OperCostFix.setValue(2.0)

    self.obj675.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(2884,279,self.obj675)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj675.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj675)
    self.globalAndLocalPostcondition(self.obj675, rootNode)
    self.obj675.postAction( rootNode.CREATE )

    self.obj676=operatingUnit(self)
    self.obj676.isGraphObjectVisual = True

    if(hasattr(self.obj676, '_setHierarchicalLink')):
      self.obj676._setHierarchicalLink(False)

    # OperCostProp
    self.obj676.OperCostProp.setValue(0.1)

    # name
    self.obj676.name.setValue('A2 R2 G4')

    # OperCostFix
    self.obj676.OperCostFix.setValue(2.0)

    self.obj676.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(1030,279,self.obj676)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj676.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj676)
    self.globalAndLocalPostcondition(self.obj676, rootNode)
    self.obj676.postAction( rootNode.CREATE )

    self.obj677=operatingUnit(self)
    self.obj677.isGraphObjectVisual = True

    if(hasattr(self.obj677, '_setHierarchicalLink')):
      self.obj677._setHierarchicalLink(False)

    # OperCostProp
    self.obj677.OperCostProp.setValue(0.4)

    # name
    self.obj677.name.setValue('A2 R2 G3')

    # OperCostFix
    self.obj677.OperCostFix.setValue(2.0)

    self.obj677.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(1442,279,self.obj677)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj677.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj677)
    self.globalAndLocalPostcondition(self.obj677, rootNode)
    self.obj677.postAction( rootNode.CREATE )

    self.obj678=operatingUnit(self)
    self.obj678.isGraphObjectVisual = True

    if(hasattr(self.obj678, '_setHierarchicalLink')):
      self.obj678._setHierarchicalLink(False)

    # OperCostProp
    self.obj678.OperCostProp.setValue(0.7)

    # name
    self.obj678.name.setValue('A2 R2 G2')

    # OperCostFix
    self.obj678.OperCostFix.setValue(2.0)

    self.obj678.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(824,279,self.obj678)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj678.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj678)
    self.globalAndLocalPostcondition(self.obj678, rootNode)
    self.obj678.postAction( rootNode.CREATE )

    self.obj679=operatingUnit(self)
    self.obj679.isGraphObjectVisual = True

    if(hasattr(self.obj679, '_setHierarchicalLink')):
      self.obj679._setHierarchicalLink(False)

    # OperCostProp
    self.obj679.OperCostProp.setValue(1.0)

    # name
    self.obj679.name.setValue('A2 R2 G1')

    # OperCostFix
    self.obj679.OperCostFix.setValue(2.0)

    self.obj679.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(1236,279,self.obj679)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj679.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj679)
    self.globalAndLocalPostcondition(self.obj679, rootNode)
    self.obj679.postAction( rootNode.CREATE )

    self.obj680=operatingUnit(self)
    self.obj680.isGraphObjectVisual = True

    if(hasattr(self.obj680, '_setHierarchicalLink')):
      self.obj680._setHierarchicalLink(False)

    # OperCostProp
    self.obj680.OperCostProp.setValue(0.1)

    # name
    self.obj680.name.setValue('A3 R2 G4')

    # OperCostFix
    self.obj680.OperCostFix.setValue(2.0)

    self.obj680.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(206,279,self.obj680)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj680.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj680)
    self.globalAndLocalPostcondition(self.obj680, rootNode)
    self.obj680.postAction( rootNode.CREATE )

    self.obj681=operatingUnit(self)
    self.obj681.isGraphObjectVisual = True

    if(hasattr(self.obj681, '_setHierarchicalLink')):
      self.obj681._setHierarchicalLink(False)

    # OperCostProp
    self.obj681.OperCostProp.setValue(0.4)

    # name
    self.obj681.name.setValue('A3 R2 G3')

    # OperCostFix
    self.obj681.OperCostFix.setValue(2.0)

    self.obj681.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(618,279,self.obj681)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj681.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj681)
    self.globalAndLocalPostcondition(self.obj681, rootNode)
    self.obj681.postAction( rootNode.CREATE )

    self.obj682=operatingUnit(self)
    self.obj682.isGraphObjectVisual = True

    if(hasattr(self.obj682, '_setHierarchicalLink')):
      self.obj682._setHierarchicalLink(False)

    # OperCostProp
    self.obj682.OperCostProp.setValue(0.7)

    # name
    self.obj682.name.setValue('A3 R2 G2')

    # OperCostFix
    self.obj682.OperCostFix.setValue(2.0)

    self.obj682.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(0,279,self.obj682)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj682.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj682)
    self.globalAndLocalPostcondition(self.obj682, rootNode)
    self.obj682.postAction( rootNode.CREATE )

    self.obj683=operatingUnit(self)
    self.obj683.isGraphObjectVisual = True

    if(hasattr(self.obj683, '_setHierarchicalLink')):
      self.obj683._setHierarchicalLink(False)

    # OperCostProp
    self.obj683.OperCostProp.setValue(1.0)

    # name
    self.obj683.name.setValue('A3 R2 G1')

    # OperCostFix
    self.obj683.OperCostFix.setValue(2.0)

    self.obj683.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(412,279,self.obj683)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj683.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj683)
    self.globalAndLocalPostcondition(self.obj683, rootNode)
    self.obj683.postAction( rootNode.CREATE )

    self.obj684=fromRaw(self)
    self.obj684.isGraphObjectVisual = True

    if(hasattr(self.obj684, '_setHierarchicalLink')):
      self.obj684._setHierarchicalLink(False)

    # rate
    self.obj684.rate.setValue(1.0)

    self.obj684.graphClass_= graph_fromRaw
    if self.genGraphics:
       new_obj = graph_fromRaw(2503.97990453,88.1336447318,self.obj684)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromRaw", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj684.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj684)
    self.globalAndLocalPostcondition(self.obj684, rootNode)
    self.obj684.postAction( rootNode.CREATE )

    self.obj685=fromRaw(self)
    self.obj685.isGraphObjectVisual = True

    if(hasattr(self.obj685, '_setHierarchicalLink')):
      self.obj685._setHierarchicalLink(False)

    # rate
    self.obj685.rate.setValue(1.0)

    self.obj685.graphClass_= graph_fromRaw
    if self.genGraphics:
       new_obj = graph_fromRaw(2599.97736756,77.9535198935,self.obj685)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromRaw", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj685.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj685)
    self.globalAndLocalPostcondition(self.obj685, rootNode)
    self.obj685.postAction( rootNode.CREATE )

    self.obj686=fromRaw(self)
    self.obj686.isGraphObjectVisual = True

    if(hasattr(self.obj686, '_setHierarchicalLink')):
      self.obj686._setHierarchicalLink(False)

    # rate
    self.obj686.rate.setValue(1.0)

    self.obj686.graphClass_= graph_fromRaw
    if self.genGraphics:
       new_obj = graph_fromRaw(1267.97990453,88.1336447318,self.obj686)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromRaw", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj686.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj686)
    self.globalAndLocalPostcondition(self.obj686, rootNode)
    self.obj686.postAction( rootNode.CREATE )

    self.obj687=fromRaw(self)
    self.obj687.isGraphObjectVisual = True

    if(hasattr(self.obj687, '_setHierarchicalLink')):
      self.obj687._setHierarchicalLink(False)

    # rate
    self.obj687.rate.setValue(1.0)

    self.obj687.graphClass_= graph_fromRaw
    if self.genGraphics:
       new_obj = graph_fromRaw(443.979904526,88.1336447318,self.obj687)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromRaw", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj687.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj687)
    self.globalAndLocalPostcondition(self.obj687, rootNode)
    self.obj687.postAction( rootNode.CREATE )

    self.obj688=intoMaterial(self)
    self.obj688.isGraphObjectVisual = True

    if(hasattr(self.obj688, '_setHierarchicalLink')):
      self.obj688._setHierarchicalLink(False)

    # rate
    self.obj688.rate.setValue(0.2)

    self.obj688.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(1888.11488568,338.368745829,self.obj688)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj688.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj688)
    self.globalAndLocalPostcondition(self.obj688, rootNode)
    self.obj688.postAction( rootNode.CREATE )

    self.obj689=intoMaterial(self)
    self.obj689.isGraphObjectVisual = True

    if(hasattr(self.obj689, '_setHierarchicalLink')):
      self.obj689._setHierarchicalLink(False)

    # rate
    self.obj689.rate.setValue(0.8)

    self.obj689.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(1682.11488568,338.368745829,self.obj689)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj689.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj689)
    self.globalAndLocalPostcondition(self.obj689, rootNode)
    self.obj689.postAction( rootNode.CREATE )

    self.obj690=intoMaterial(self)
    self.obj690.isGraphObjectVisual = True

    if(hasattr(self.obj690, '_setHierarchicalLink')):
      self.obj690._setHierarchicalLink(False)

    # rate
    self.obj690.rate.setValue(0.6)

    self.obj690.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(2094.11488568,338.368745829,self.obj690)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj690.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj690)
    self.globalAndLocalPostcondition(self.obj690, rootNode)
    self.obj690.postAction( rootNode.CREATE )

    self.obj691=intoMaterial(self)
    self.obj691.isGraphObjectVisual = True

    if(hasattr(self.obj691, '_setHierarchicalLink')):
      self.obj691._setHierarchicalLink(False)

    # rate
    self.obj691.rate.setValue(0.4)

    self.obj691.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(1476.11488568,338.368745829,self.obj691)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj691.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj691)
    self.globalAndLocalPostcondition(self.obj691, rootNode)
    self.obj691.postAction( rootNode.CREATE )

    self.obj692=intoMaterial(self)
    self.obj692.isGraphObjectVisual = True

    if(hasattr(self.obj692, '_setHierarchicalLink')):
      self.obj692._setHierarchicalLink(False)

    # rate
    self.obj692.rate.setValue(0.1)

    self.obj692.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(2090.78015203,354.469521694,self.obj692)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj692.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj692)
    self.globalAndLocalPostcondition(self.obj692, rootNode)
    self.obj692.postAction( rootNode.CREATE )

    self.obj693=intoMaterial(self)
    self.obj693.isGraphObjectVisual = True

    if(hasattr(self.obj693, '_setHierarchicalLink')):
      self.obj693._setHierarchicalLink(False)

    # rate
    self.obj693.rate.setValue(0.4)

    self.obj693.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(2502.78015203,354.469521694,self.obj693)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj693.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj693)
    self.globalAndLocalPostcondition(self.obj693, rootNode)
    self.obj693.postAction( rootNode.CREATE )

    self.obj694=intoMaterial(self)
    self.obj694.isGraphObjectVisual = True

    if(hasattr(self.obj694, '_setHierarchicalLink')):
      self.obj694._setHierarchicalLink(False)

    # rate
    self.obj694.rate.setValue(0.7)

    self.obj694.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(1884.78015203,354.469521694,self.obj694)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj694.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj694)
    self.globalAndLocalPostcondition(self.obj694, rootNode)
    self.obj694.postAction( rootNode.CREATE )

    self.obj695=intoMaterial(self)
    self.obj695.isGraphObjectVisual = True

    if(hasattr(self.obj695, '_setHierarchicalLink')):
      self.obj695._setHierarchicalLink(False)

    # rate
    self.obj695.rate.setValue(1.0)

    self.obj695.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(2296.78015203,354.469521694,self.obj695)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj695.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj695)
    self.globalAndLocalPostcondition(self.obj695, rootNode)
    self.obj695.postAction( rootNode.CREATE )

    self.obj696=intoMaterial(self)
    self.obj696.isGraphObjectVisual = True

    if(hasattr(self.obj696, '_setHierarchicalLink')):
      self.obj696._setHierarchicalLink(False)

    # rate
    self.obj696.rate.setValue(0.1)

    self.obj696.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(1269.05275157,316.121287404,self.obj696)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj696.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj696)
    self.globalAndLocalPostcondition(self.obj696, rootNode)
    self.obj696.postAction( rootNode.CREATE )

    self.obj697=intoMaterial(self)
    self.obj697.isGraphObjectVisual = True

    if(hasattr(self.obj697, '_setHierarchicalLink')):
      self.obj697._setHierarchicalLink(False)

    # rate
    self.obj697.rate.setValue(0.4)

    self.obj697.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(1681.05275157,316.121287404,self.obj697)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj697.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj697)
    self.globalAndLocalPostcondition(self.obj697, rootNode)
    self.obj697.postAction( rootNode.CREATE )

    self.obj698=intoMaterial(self)
    self.obj698.isGraphObjectVisual = True

    if(hasattr(self.obj698, '_setHierarchicalLink')):
      self.obj698._setHierarchicalLink(False)

    # rate
    self.obj698.rate.setValue(0.7)

    self.obj698.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(1063.05275157,316.121287404,self.obj698)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj698.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj698)
    self.globalAndLocalPostcondition(self.obj698, rootNode)
    self.obj698.postAction( rootNode.CREATE )

    self.obj699=intoMaterial(self)
    self.obj699.isGraphObjectVisual = True

    if(hasattr(self.obj699, '_setHierarchicalLink')):
      self.obj699._setHierarchicalLink(False)

    # rate
    self.obj699.rate.setValue(1.0)

    self.obj699.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(1475.05275157,316.121287404,self.obj699)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj699.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj699)
    self.globalAndLocalPostcondition(self.obj699, rootNode)
    self.obj699.postAction( rootNode.CREATE )

    self.obj700=intoMaterial(self)
    self.obj700.isGraphObjectVisual = True

    if(hasattr(self.obj700, '_setHierarchicalLink')):
      self.obj700._setHierarchicalLink(False)

    # rate
    self.obj700.rate.setValue(0.1)

    self.obj700.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(854.296452571,334.531767293,self.obj700)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj700.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj700)
    self.globalAndLocalPostcondition(self.obj700, rootNode)
    self.obj700.postAction( rootNode.CREATE )

    self.obj701=intoMaterial(self)
    self.obj701.isGraphObjectVisual = True

    if(hasattr(self.obj701, '_setHierarchicalLink')):
      self.obj701._setHierarchicalLink(False)

    # rate
    self.obj701.rate.setValue(0.4)

    self.obj701.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(1266.29645257,334.531767293,self.obj701)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj701.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj701)
    self.globalAndLocalPostcondition(self.obj701, rootNode)
    self.obj701.postAction( rootNode.CREATE )

    self.obj702=intoMaterial(self)
    self.obj702.isGraphObjectVisual = True

    if(hasattr(self.obj702, '_setHierarchicalLink')):
      self.obj702._setHierarchicalLink(False)

    # rate
    self.obj702.rate.setValue(0.7)

    self.obj702.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(648.296452571,334.531767293,self.obj702)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj702.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj702)
    self.globalAndLocalPostcondition(self.obj702, rootNode)
    self.obj702.postAction( rootNode.CREATE )

    self.obj703=intoMaterial(self)
    self.obj703.isGraphObjectVisual = True

    if(hasattr(self.obj703, '_setHierarchicalLink')):
      self.obj703._setHierarchicalLink(False)

    # rate
    self.obj703.rate.setValue(1.0)

    self.obj703.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(1060.29645257,334.531767293,self.obj703)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj703.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj703)
    self.globalAndLocalPostcondition(self.obj703, rootNode)
    self.obj703.postAction( rootNode.CREATE )

    self.obj704=intoMaterial(self)
    self.obj704.isGraphObjectVisual = True

    if(hasattr(self.obj704, '_setHierarchicalLink')):
      self.obj704._setHierarchicalLink(False)

    # rate
    self.obj704.rate.setValue(0.433333333333)

    self.obj704.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(2305.15678218,167.361798661,self.obj704)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj704.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj704)
    self.globalAndLocalPostcondition(self.obj704, rootNode)
    self.obj704.postAction( rootNode.CREATE )

    self.obj705=intoMaterial(self)
    self.obj705.isGraphObjectVisual = True

    if(hasattr(self.obj705, '_setHierarchicalLink')):
      self.obj705._setHierarchicalLink(False)

    # rate
    self.obj705.rate.setValue(0.433333333333)

    self.obj705.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(2201.57801827,167.441724026,self.obj705)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj705.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj705)
    self.globalAndLocalPostcondition(self.obj705, rootNode)
    self.obj705.postAction( rootNode.CREATE )

    self.obj706=intoMaterial(self)
    self.obj706.isGraphObjectVisual = True

    if(hasattr(self.obj706, '_setHierarchicalLink')):
      self.obj706._setHierarchicalLink(False)

    # rate
    self.obj706.rate.setValue(0.433333333333)

    self.obj706.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(2409.99299945,166.870109648,self.obj706)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj706.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj706)
    self.globalAndLocalPostcondition(self.obj706, rootNode)
    self.obj706.postAction( rootNode.CREATE )

    self.obj707=intoMaterial(self)
    self.obj707.isGraphObjectVisual = True

    if(hasattr(self.obj707, '_setHierarchicalLink')):
      self.obj707._setHierarchicalLink(False)

    # rate
    self.obj707.rate.setValue(0.433333333333)

    self.obj707.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(2098.29795564,167.468112499,self.obj707)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj707.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj707)
    self.globalAndLocalPostcondition(self.obj707, rootNode)
    self.obj707.postAction( rootNode.CREATE )

    self.obj708=intoMaterial(self)
    self.obj708.isGraphObjectVisual = True

    if(hasattr(self.obj708, '_setHierarchicalLink')):
      self.obj708._setHierarchicalLink(False)

    # rate
    self.obj708.rate.setValue(0.433333333333)

    self.obj708.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(2714.98683298,148.33772234,self.obj708)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj708.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj708)
    self.globalAndLocalPostcondition(self.obj708, rootNode)
    self.obj708.postAction( rootNode.CREATE )

    self.obj709=intoMaterial(self)
    self.obj709.isGraphObjectVisual = True

    if(hasattr(self.obj709, '_setHierarchicalLink')):
      self.obj709._setHierarchicalLink(False)

    # rate
    self.obj709.rate.setValue(0.433333333333)

    self.obj709.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(2922.01273181,145.115080048,self.obj709)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj709.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj709)
    self.globalAndLocalPostcondition(self.obj709, rootNode)
    self.obj709.postAction( rootNode.CREATE )

    self.obj710=intoMaterial(self)
    self.obj710.isGraphObjectVisual = True

    if(hasattr(self.obj710, '_setHierarchicalLink')):
      self.obj710._setHierarchicalLink(False)

    # rate
    self.obj710.rate.setValue(0.433333333333)

    self.obj710.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(2615.99299945,166.870109648,self.obj710)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj710.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj710)
    self.globalAndLocalPostcondition(self.obj710, rootNode)
    self.obj710.postAction( rootNode.CREATE )

    self.obj711=intoMaterial(self)
    self.obj711.isGraphObjectVisual = True

    if(hasattr(self.obj711, '_setHierarchicalLink')):
      self.obj711._setHierarchicalLink(False)

    # rate
    self.obj711.rate.setValue(0.433333333333)

    self.obj711.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(2820.67871454,145.518661809,self.obj711)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj711.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj711)
    self.globalAndLocalPostcondition(self.obj711, rootNode)
    self.obj711.postAction( rootNode.CREATE )

    self.obj712=intoMaterial(self)
    self.obj712.isGraphObjectVisual = True

    if(hasattr(self.obj712, '_setHierarchicalLink')):
      self.obj712._setHierarchicalLink(False)

    # rate
    self.obj712.rate.setValue(0.633333333333)

    self.obj712.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(1173.99299945,166.870109648,self.obj712)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj712.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj712)
    self.globalAndLocalPostcondition(self.obj712, rootNode)
    self.obj712.postAction( rootNode.CREATE )

    self.obj713=intoMaterial(self)
    self.obj713.isGraphObjectVisual = True

    if(hasattr(self.obj713, '_setHierarchicalLink')):
      self.obj713._setHierarchicalLink(False)

    # rate
    self.obj713.rate.setValue(0.633333333333)

    self.obj713.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(1378.67871454,145.518661809,self.obj713)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj713.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj713)
    self.globalAndLocalPostcondition(self.obj713, rootNode)
    self.obj713.postAction( rootNode.CREATE )

    self.obj714=intoMaterial(self)
    self.obj714.isGraphObjectVisual = True

    if(hasattr(self.obj714, '_setHierarchicalLink')):
      self.obj714._setHierarchicalLink(False)

    # rate
    self.obj714.rate.setValue(0.633333333333)

    self.obj714.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(1069.15678218,167.361798661,self.obj714)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj714.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj714)
    self.globalAndLocalPostcondition(self.obj714, rootNode)
    self.obj714.postAction( rootNode.CREATE )

    self.obj715=intoMaterial(self)
    self.obj715.isGraphObjectVisual = True

    if(hasattr(self.obj715, '_setHierarchicalLink')):
      self.obj715._setHierarchicalLink(False)

    # rate
    self.obj715.rate.setValue(0.633333333333)

    self.obj715.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(1272.98683298,148.33772234,self.obj715)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj715.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj715)
    self.globalAndLocalPostcondition(self.obj715, rootNode)
    self.obj715.postAction( rootNode.CREATE )

    self.obj716=intoMaterial(self)
    self.obj716.isGraphObjectVisual = True

    if(hasattr(self.obj716, '_setHierarchicalLink')):
      self.obj716._setHierarchicalLink(False)

    # rate
    self.obj716.rate.setValue(0.5)

    self.obj716.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(349.992999454,166.870109648,self.obj716)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj716.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj716)
    self.globalAndLocalPostcondition(self.obj716, rootNode)
    self.obj716.postAction( rootNode.CREATE )

    self.obj717=intoMaterial(self)
    self.obj717.isGraphObjectVisual = True

    if(hasattr(self.obj717, '_setHierarchicalLink')):
      self.obj717._setHierarchicalLink(False)

    # rate
    self.obj717.rate.setValue(0.5)

    self.obj717.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(554.678714538,145.518661809,self.obj717)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj717.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj717)
    self.globalAndLocalPostcondition(self.obj717, rootNode)
    self.obj717.postAction( rootNode.CREATE )

    self.obj718=intoMaterial(self)
    self.obj718.isGraphObjectVisual = True

    if(hasattr(self.obj718, '_setHierarchicalLink')):
      self.obj718._setHierarchicalLink(False)

    # rate
    self.obj718.rate.setValue(0.5)

    self.obj718.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(245.156782175,167.361798661,self.obj718)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj718.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj718)
    self.globalAndLocalPostcondition(self.obj718, rootNode)
    self.obj718.postAction( rootNode.CREATE )

    self.obj719=intoMaterial(self)
    self.obj719.isGraphObjectVisual = True

    if(hasattr(self.obj719, '_setHierarchicalLink')):
      self.obj719._setHierarchicalLink(False)

    # rate
    self.obj719.rate.setValue(0.5)

    self.obj719.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(448.986832981,148.33772234,self.obj719)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj719.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj719)
    self.globalAndLocalPostcondition(self.obj719, rootNode)
    self.obj719.postAction( rootNode.CREATE )

    self.obj720=intoProduct(self)
    self.obj720.isGraphObjectVisual = True

    if(hasattr(self.obj720, '_setHierarchicalLink')):
      self.obj720._setHierarchicalLink(False)

    # rate
    self.obj720.rate.setValue(1.0)

    self.obj720.graphClass_= graph_intoProduct
    if self.genGraphics:
       new_obj = graph_intoProduct(1679.93652968,493.375109847,self.obj720)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoProduct", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj720.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj720)
    self.globalAndLocalPostcondition(self.obj720, rootNode)
    self.obj720.postAction( rootNode.CREATE )

    self.obj721=intoProduct(self)
    self.obj721.isGraphObjectVisual = True

    if(hasattr(self.obj721, '_setHierarchicalLink')):
      self.obj721._setHierarchicalLink(False)

    # rate
    self.obj721.rate.setValue(1.0)

    self.obj721.graphClass_= graph_intoProduct
    if self.genGraphics:
       new_obj = graph_intoProduct(1482.36724691,484.593909153,self.obj721)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoProduct", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj721.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj721)
    self.globalAndLocalPostcondition(self.obj721, rootNode)
    self.obj721.postAction( rootNode.CREATE )

    self.obj722=intoProduct(self)
    self.obj722.isGraphObjectVisual = True

    if(hasattr(self.obj722, '_setHierarchicalLink')):
      self.obj722._setHierarchicalLink(False)

    # rate
    self.obj722.rate.setValue(1.0)

    self.obj722.graphClass_= graph_intoProduct
    if self.genGraphics:
       new_obj = graph_intoProduct(1775.56158238,504.166348622,self.obj722)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoProduct", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj722.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj722)
    self.globalAndLocalPostcondition(self.obj722, rootNode)
    self.obj722.postAction( rootNode.CREATE )

    self.obj723=intoProduct(self)
    self.obj723.isGraphObjectVisual = True

    if(hasattr(self.obj723, '_setHierarchicalLink')):
      self.obj723._setHierarchicalLink(False)

    # rate
    self.obj723.rate.setValue(1.0)

    self.obj723.graphClass_= graph_intoProduct
    if self.genGraphics:
       new_obj = graph_intoProduct(1586.8537136,484.915829787,self.obj723)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoProduct", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj723.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj723)
    self.globalAndLocalPostcondition(self.obj723, rootNode)
    self.obj723.postAction( rootNode.CREATE )

    self.obj724=fromMaterial(self)
    self.obj724.isGraphObjectVisual = True

    if(hasattr(self.obj724, '_setHierarchicalLink')):
      self.obj724._setHierarchicalLink(False)

    # rate
    self.obj724.rate.setValue(1.0)

    self.obj724.graphClass_= graph_fromMaterial
    if self.genGraphics:
       new_obj = graph_fromMaterial(1679.97925309,430.64382278,self.obj724)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj724.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj724)
    self.globalAndLocalPostcondition(self.obj724, rootNode)
    self.obj724.postAction( rootNode.CREATE )

    self.obj725=fromMaterial(self)
    self.obj725.isGraphObjectVisual = True

    if(hasattr(self.obj725, '_setHierarchicalLink')):
      self.obj725._setHierarchicalLink(False)

    # rate
    self.obj725.rate.setValue(1.0)

    self.obj725.graphClass_= graph_fromMaterial
    if self.genGraphics:
       new_obj = graph_fromMaterial(1267.97925309,430.64382278,self.obj725)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj725.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj725)
    self.globalAndLocalPostcondition(self.obj725, rootNode)
    self.obj725.postAction( rootNode.CREATE )

    self.obj726=fromMaterial(self)
    self.obj726.isGraphObjectVisual = True

    if(hasattr(self.obj726, '_setHierarchicalLink')):
      self.obj726._setHierarchicalLink(False)

    # rate
    self.obj726.rate.setValue(1.0)

    self.obj726.graphClass_= graph_fromMaterial
    if self.genGraphics:
       new_obj = graph_fromMaterial(1885.97925309,430.64382278,self.obj726)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj726.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj726)
    self.globalAndLocalPostcondition(self.obj726, rootNode)
    self.obj726.postAction( rootNode.CREATE )

    self.obj727=fromMaterial(self)
    self.obj727.isGraphObjectVisual = True

    if(hasattr(self.obj727, '_setHierarchicalLink')):
      self.obj727._setHierarchicalLink(False)

    # rate
    self.obj727.rate.setValue(1.0)

    self.obj727.graphClass_= graph_fromMaterial
    if self.genGraphics:
       new_obj = graph_fromMaterial(1473.97925309,430.64382278,self.obj727)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj727.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj727)
    self.globalAndLocalPostcondition(self.obj727, rootNode)
    self.obj727.postAction( rootNode.CREATE )

    self.obj728=fromMaterial(self)
    self.obj728.isGraphObjectVisual = True

    if(hasattr(self.obj728, '_setHierarchicalLink')):
      self.obj728._setHierarchicalLink(False)

    # rate
    self.obj728.rate.setValue(1.0)

    self.obj728.graphClass_= graph_fromMaterial
    if self.genGraphics:
       new_obj = graph_fromMaterial(2111.68277324,256.50121981,self.obj728)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj728.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj728)
    self.globalAndLocalPostcondition(self.obj728, rootNode)
    self.obj728.postAction( rootNode.CREATE )

    self.obj729=fromMaterial(self)
    self.obj729.isGraphObjectVisual = True

    if(hasattr(self.obj729, '_setHierarchicalLink')):
      self.obj729._setHierarchicalLink(False)

    # rate
    self.obj729.rate.setValue(1.0)

    self.obj729.graphClass_= graph_fromMaterial
    if self.genGraphics:
       new_obj = graph_fromMaterial(1905.68277324,256.50121981,self.obj729)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj729.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj729)
    self.globalAndLocalPostcondition(self.obj729, rootNode)
    self.obj729.postAction( rootNode.CREATE )

    self.obj730=fromMaterial(self)
    self.obj730.isGraphObjectVisual = True

    if(hasattr(self.obj730, '_setHierarchicalLink')):
      self.obj730._setHierarchicalLink(False)

    # rate
    self.obj730.rate.setValue(1.0)

    self.obj730.graphClass_= graph_fromMaterial
    if self.genGraphics:
       new_obj = graph_fromMaterial(2317.68277324,256.50121981,self.obj730)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj730.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj730)
    self.globalAndLocalPostcondition(self.obj730, rootNode)
    self.obj730.postAction( rootNode.CREATE )

    self.obj731=fromMaterial(self)
    self.obj731.isGraphObjectVisual = True

    if(hasattr(self.obj731, '_setHierarchicalLink')):
      self.obj731._setHierarchicalLink(False)

    # rate
    self.obj731.rate.setValue(1.0)

    self.obj731.graphClass_= graph_fromMaterial
    if self.genGraphics:
       new_obj = graph_fromMaterial(1699.68277324,256.50121981,self.obj731)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj731.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj731)
    self.globalAndLocalPostcondition(self.obj731, rootNode)
    self.obj731.postAction( rootNode.CREATE )

    self.obj732=fromMaterial(self)
    self.obj732.isGraphObjectVisual = True

    if(hasattr(self.obj732, '_setHierarchicalLink')):
      self.obj732._setHierarchicalLink(False)

    # rate
    self.obj732.rate.setValue(1.0)

    self.obj732.graphClass_= graph_fromMaterial
    if self.genGraphics:
       new_obj = graph_fromMaterial(2729.68277324,256.50121981,self.obj732)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj732.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj732)
    self.globalAndLocalPostcondition(self.obj732, rootNode)
    self.obj732.postAction( rootNode.CREATE )

    self.obj733=fromMaterial(self)
    self.obj733.isGraphObjectVisual = True

    if(hasattr(self.obj733, '_setHierarchicalLink')):
      self.obj733._setHierarchicalLink(False)

    # rate
    self.obj733.rate.setValue(1.0)

    self.obj733.graphClass_= graph_fromMaterial
    if self.genGraphics:
       new_obj = graph_fromMaterial(3141.68277324,256.50121981,self.obj733)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj733.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj733)
    self.globalAndLocalPostcondition(self.obj733, rootNode)
    self.obj733.postAction( rootNode.CREATE )

    self.obj734=fromMaterial(self)
    self.obj734.isGraphObjectVisual = True

    if(hasattr(self.obj734, '_setHierarchicalLink')):
      self.obj734._setHierarchicalLink(False)

    # rate
    self.obj734.rate.setValue(1.0)

    self.obj734.graphClass_= graph_fromMaterial
    if self.genGraphics:
       new_obj = graph_fromMaterial(2523.68277324,256.50121981,self.obj734)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj734.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj734)
    self.globalAndLocalPostcondition(self.obj734, rootNode)
    self.obj734.postAction( rootNode.CREATE )

    self.obj735=fromMaterial(self)
    self.obj735.isGraphObjectVisual = True

    if(hasattr(self.obj735, '_setHierarchicalLink')):
      self.obj735._setHierarchicalLink(False)

    # rate
    self.obj735.rate.setValue(1.0)

    self.obj735.graphClass_= graph_fromMaterial
    if self.genGraphics:
       new_obj = graph_fromMaterial(2935.68277324,256.50121981,self.obj735)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj735.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj735)
    self.globalAndLocalPostcondition(self.obj735, rootNode)
    self.obj735.postAction( rootNode.CREATE )

    self.obj736=fromMaterial(self)
    self.obj736.isGraphObjectVisual = True

    if(hasattr(self.obj736, '_setHierarchicalLink')):
      self.obj736._setHierarchicalLink(False)

    # rate
    self.obj736.rate.setValue(1.0)

    self.obj736.graphClass_= graph_fromMaterial
    if self.genGraphics:
       new_obj = graph_fromMaterial(1081.68277324,256.50121981,self.obj736)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj736.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj736)
    self.globalAndLocalPostcondition(self.obj736, rootNode)
    self.obj736.postAction( rootNode.CREATE )

    self.obj737=fromMaterial(self)
    self.obj737.isGraphObjectVisual = True

    if(hasattr(self.obj737, '_setHierarchicalLink')):
      self.obj737._setHierarchicalLink(False)

    # rate
    self.obj737.rate.setValue(1.0)

    self.obj737.graphClass_= graph_fromMaterial
    if self.genGraphics:
       new_obj = graph_fromMaterial(1493.68277324,256.50121981,self.obj737)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj737.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj737)
    self.globalAndLocalPostcondition(self.obj737, rootNode)
    self.obj737.postAction( rootNode.CREATE )

    self.obj738=fromMaterial(self)
    self.obj738.isGraphObjectVisual = True

    if(hasattr(self.obj738, '_setHierarchicalLink')):
      self.obj738._setHierarchicalLink(False)

    # rate
    self.obj738.rate.setValue(1.0)

    self.obj738.graphClass_= graph_fromMaterial
    if self.genGraphics:
       new_obj = graph_fromMaterial(875.682773237,256.50121981,self.obj738)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj738.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj738)
    self.globalAndLocalPostcondition(self.obj738, rootNode)
    self.obj738.postAction( rootNode.CREATE )

    self.obj739=fromMaterial(self)
    self.obj739.isGraphObjectVisual = True

    if(hasattr(self.obj739, '_setHierarchicalLink')):
      self.obj739._setHierarchicalLink(False)

    # rate
    self.obj739.rate.setValue(1.0)

    self.obj739.graphClass_= graph_fromMaterial
    if self.genGraphics:
       new_obj = graph_fromMaterial(1287.68277324,256.50121981,self.obj739)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj739.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj739)
    self.globalAndLocalPostcondition(self.obj739, rootNode)
    self.obj739.postAction( rootNode.CREATE )

    self.obj740=fromMaterial(self)
    self.obj740.isGraphObjectVisual = True

    if(hasattr(self.obj740, '_setHierarchicalLink')):
      self.obj740._setHierarchicalLink(False)

    # rate
    self.obj740.rate.setValue(1.0)

    self.obj740.graphClass_= graph_fromMaterial
    if self.genGraphics:
       new_obj = graph_fromMaterial(257.682773237,256.50121981,self.obj740)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj740.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj740)
    self.globalAndLocalPostcondition(self.obj740, rootNode)
    self.obj740.postAction( rootNode.CREATE )

    self.obj741=fromMaterial(self)
    self.obj741.isGraphObjectVisual = True

    if(hasattr(self.obj741, '_setHierarchicalLink')):
      self.obj741._setHierarchicalLink(False)

    # rate
    self.obj741.rate.setValue(1.0)

    self.obj741.graphClass_= graph_fromMaterial
    if self.genGraphics:
       new_obj = graph_fromMaterial(669.682773237,256.50121981,self.obj741)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj741.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj741)
    self.globalAndLocalPostcondition(self.obj741, rootNode)
    self.obj741.postAction( rootNode.CREATE )

    self.obj742=fromMaterial(self)
    self.obj742.isGraphObjectVisual = True

    if(hasattr(self.obj742, '_setHierarchicalLink')):
      self.obj742._setHierarchicalLink(False)

    # rate
    self.obj742.rate.setValue(1.0)

    self.obj742.graphClass_= graph_fromMaterial
    if self.genGraphics:
       new_obj = graph_fromMaterial(51.6827732371,256.50121981,self.obj742)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj742.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj742)
    self.globalAndLocalPostcondition(self.obj742, rootNode)
    self.obj742.postAction( rootNode.CREATE )

    self.obj743=fromMaterial(self)
    self.obj743.isGraphObjectVisual = True

    if(hasattr(self.obj743, '_setHierarchicalLink')):
      self.obj743._setHierarchicalLink(False)

    # rate
    self.obj743.rate.setValue(1.0)

    self.obj743.graphClass_= graph_fromMaterial
    if self.genGraphics:
       new_obj = graph_fromMaterial(463.682773237,256.50121981,self.obj743)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj743.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj743)
    self.globalAndLocalPostcondition(self.obj743, rootNode)
    self.obj743.postAction( rootNode.CREATE )

    # Connections for obj636 (graphObject_: Obj663) of type rawMaterial
    self.drawConnections(
(self.obj636,self.obj684,[2496.0, 56.0, 2504.979904526288, 72.38364473182781, 2503.979904526288, 88.13364473182781],"true", 3),
(self.obj636,self.obj685,[2496.0, 56.0, 2549.4773675579822, 62.20351989345416, 2599.9773675579822, 77.95351989345416],"true", 3) )
    # Connections for obj637 (graphObject_: Obj664) of type rawMaterial
    self.drawConnections(
(self.obj637,self.obj686,[1260.0, 56.0, 1268.9799045262882, 72.38364473182781, 1267.9799045262882, 88.13364473182781],"true", 3) )
    # Connections for obj638 (graphObject_: Obj665) of type rawMaterial
    self.drawConnections(
(self.obj638,self.obj687,[436.0, 56.0, 444.9799045262882, 72.38364473182781, 443.9799045262882, 88.13364473182781],"true", 3) )
    # Connections for obj639 (graphObject_: Obj666) of type product
    self.drawConnections(
 )
    # Connections for obj640 (graphObject_: Obj667) of type metarial
    self.drawConnections(
(self.obj640,self.obj724,[1672.0, 399.0, 1680.9792530896846, 415.14382277997964, 1679.9792530896846, 430.64382277997964],"true", 3) )
    # Connections for obj641 (graphObject_: Obj668) of type metarial
    self.drawConnections(
(self.obj641,self.obj725,[1260.0, 399.0, 1268.9792530896846, 415.14382277997964, 1267.9792530896846, 430.64382277997964],"true", 3) )
    # Connections for obj642 (graphObject_: Obj669) of type metarial
    self.drawConnections(
(self.obj642,self.obj726,[1878.0, 399.0, 1886.9792530896846, 415.14382277997964, 1885.9792530896846, 430.64382277997964],"true", 3) )
    # Connections for obj643 (graphObject_: Obj670) of type metarial
    self.drawConnections(
(self.obj643,self.obj727,[1466.0, 399.0, 1474.9792530896846, 415.14382277997964, 1473.9792530896846, 430.64382277997964],"true", 3) )
    # Connections for obj644 (graphObject_: Obj671) of type metarial
    self.drawConnections(
(self.obj644,self.obj728,[2094.0, 228.0, 2107.6827732370934, 241.0012198097823, 2111.6827732370934, 256.5012198097823],"true", 3) )
    # Connections for obj645 (graphObject_: Obj672) of type metarial
    self.drawConnections(
(self.obj645,self.obj729,[1888.0, 228.0, 1901.6827732370937, 241.0012198097823, 1905.6827732370937, 256.5012198097823],"true", 3) )
    # Connections for obj646 (graphObject_: Obj673) of type metarial
    self.drawConnections(
(self.obj646,self.obj730,[2300.0, 228.0, 2313.6827732370934, 241.0012198097823, 2317.6827732370934, 256.5012198097823],"true", 3) )
    # Connections for obj647 (graphObject_: Obj674) of type metarial
    self.drawConnections(
(self.obj647,self.obj731,[1682.0, 228.0, 1695.6827732370937, 241.0012198097823, 1699.6827732370937, 256.5012198097823],"true", 3) )
    # Connections for obj648 (graphObject_: Obj675) of type metarial
    self.drawConnections(
(self.obj648,self.obj732,[2712.0, 228.0, 2725.6827732370934, 241.0012198097823, 2729.6827732370934, 256.5012198097823],"true", 3) )
    # Connections for obj649 (graphObject_: Obj676) of type metarial
    self.drawConnections(
(self.obj649,self.obj733,[3124.0, 228.0, 3137.6827732370934, 241.0012198097823, 3141.6827732370934, 256.5012198097823],"true", 3) )
    # Connections for obj650 (graphObject_: Obj677) of type metarial
    self.drawConnections(
(self.obj650,self.obj734,[2506.0, 228.0, 2519.6827732370934, 241.0012198097823, 2523.6827732370934, 256.5012198097823],"true", 3) )
    # Connections for obj651 (graphObject_: Obj678) of type metarial
    self.drawConnections(
(self.obj651,self.obj735,[2918.0, 228.0, 2931.6827732370934, 241.0012198097823, 2935.6827732370934, 256.5012198097823],"true", 3) )
    # Connections for obj652 (graphObject_: Obj679) of type metarial
    self.drawConnections(
(self.obj652,self.obj736,[1064.0, 228.0, 1077.6827732370937, 241.0012198097823, 1081.6827732370937, 256.5012198097823],"true", 3) )
    # Connections for obj653 (graphObject_: Obj680) of type metarial
    self.drawConnections(
(self.obj653,self.obj737,[1476.0, 228.0, 1489.6827732370937, 241.0012198097823, 1493.6827732370937, 256.5012198097823],"true", 3) )
    # Connections for obj654 (graphObject_: Obj681) of type metarial
    self.drawConnections(
(self.obj654,self.obj738,[858.0, 228.0, 871.6827732370936, 241.0012198097823, 875.6827732370936, 256.5012198097823],"true", 3) )
    # Connections for obj655 (graphObject_: Obj682) of type metarial
    self.drawConnections(
(self.obj655,self.obj739,[1270.0, 228.0, 1283.6827732370937, 241.0012198097823, 1287.6827732370937, 256.5012198097823],"true", 3) )
    # Connections for obj656 (graphObject_: Obj683) of type metarial
    self.drawConnections(
(self.obj656,self.obj740,[240.0, 228.0, 253.68277323709358, 241.0012198097823, 257.68277323709356, 256.5012198097823],"true", 3) )
    # Connections for obj657 (graphObject_: Obj684) of type metarial
    self.drawConnections(
(self.obj657,self.obj741,[652.0, 228.0, 665.6827732370936, 241.0012198097823, 669.6827732370936, 256.5012198097823],"true", 3) )
    # Connections for obj658 (graphObject_: Obj685) of type metarial
    self.drawConnections(
(self.obj658,self.obj742,[34.0, 228.0, 47.68277323709358, 241.0012198097823, 51.68277323709358, 256.5012198097823],"true", 3) )
    # Connections for obj659 (graphObject_: Obj686) of type metarial
    self.drawConnections(
(self.obj659,self.obj743,[446.0, 228.0, 459.68277323709356, 241.0012198097823, 463.68277323709356, 256.5012198097823],"true", 3) )
    # Connections for obj660 (graphObject_: Obj687) named A1 R1
    self.drawConnections(
(self.obj660,self.obj704,[2491.0, 126.0, 2398.9067821750014, 151.611798660721, 2305.1567821750014, 167.361798660721],"true", 3),
(self.obj660,self.obj705,[2491.0, 126.0, 2346.8280182679064, 151.6917240262472, 2201.5780182679064, 167.4417240262472],"true", 3),
(self.obj660,self.obj706,[2491.0, 126.0, 2452.242999454488, 151.1201096477546, 2409.992999454488, 166.8701096477546],"true", 3),
(self.obj660,self.obj707,[2491.0, 126.0, 2295.047955638446, 151.7181124993186, 2098.297955638446, 167.4681124993186],"true", 3) )
    # Connections for obj661 (graphObject_: Obj688) named A1 R2
    self.drawConnections(
(self.obj661,self.obj708,[2697.0, 126.0, 2710.736832980505, 135.58772233983163, 2714.986832980505, 148.33772233983163],"true", 3),
(self.obj661,self.obj709,[2731.0, 126.0, 2827.2627318132636, 130.6150800478132, 2922.0127318132636, 145.1150800478132],"true", 3),
(self.obj661,self.obj710,[2697.0, 126.0, 2658.242999454488, 151.1201096477546, 2615.992999454488, 166.8701096477546],"true", 3),
(self.obj661,self.obj711,[2731.0, 126.0, 2777.428714537922, 131.01866180930125, 2820.678714537922, 145.51866180930125],"true", 3) )
    # Connections for obj662 (graphObject_: Obj689) named A2 R2
    self.drawConnections(
(self.obj662,self.obj712,[1255.0, 126.0, 1216.2429994544884, 151.1201096477546, 1173.9929994544884, 166.8701096477546],"true", 3),
(self.obj662,self.obj713,[1289.0, 126.0, 1335.4287145379221, 131.01866180930125, 1378.6787145379221, 145.51866180930125],"true", 3),
(self.obj662,self.obj714,[1255.0, 126.0, 1162.9067821750011, 151.611798660721, 1069.1567821750011, 167.361798660721],"true", 3),
(self.obj662,self.obj715,[1255.0, 126.0, 1268.7368329805051, 135.58772233983163, 1272.9868329805051, 148.33772233983163],"true", 3) )
    # Connections for obj663 (graphObject_: Obj690) named A3 R2
    self.drawConnections(
(self.obj663,self.obj716,[431.0, 126.0, 392.2429994544884, 151.1201096477546, 349.9929994544884, 166.8701096477546],"true", 3),
(self.obj663,self.obj717,[465.0, 126.0, 511.42871453792213, 131.01866180930125, 554.6787145379221, 145.51866180930125],"true", 3),
(self.obj663,self.obj718,[431.0, 126.0, 338.9067821750011, 151.611798660721, 245.15678217500113, 167.361798660721],"true", 3),
(self.obj663,self.obj719,[431.0, 126.0, 444.73683298050514, 135.58772233983163, 448.98683298050514, 148.33772233983163],"true", 3) )
    # Connections for obj664 (graphObject_: Obj691) named G1 OAF
    self.drawConnections(
(self.obj664,self.obj720,[1667.0, 468.0, 1678.4365296831495, 480.12510984719063, 1679.9365296831495, 493.37510984719063],"true", 3) )
    # Connections for obj665 (graphObject_: Obj692) named G2 OAF
    self.drawConnections(
(self.obj665,self.obj721,[1289.0, 468.0, 1386.3672469138317, 471.34390915261633, 1482.3672469138317, 484.59390915261633],"true", 3) )
    # Connections for obj666 (graphObject_: Obj693) named G3 OAF
    self.drawConnections(
(self.obj666,self.obj722,[1873.0, 468.0, 1825.5615823848773, 490.9163486221782, 1775.5615823848773, 504.1663486221782],"true", 3) )
    # Connections for obj667 (graphObject_: Obj694) named G4 OAF
    self.drawConnections(
(self.obj667,self.obj723,[1495.0, 468.0, 1542.353713602772, 471.6658297869167, 1586.853713602772, 484.9158297869167],"true", 3) )
    # Connections for obj668 (graphObject_: Obj695) named A1 R1 G1
    self.drawConnections(
(self.obj668,self.obj688,[2079.0, 297.0, 1984.3648856811053, 322.6187458289775, 1888.1148856811053, 338.3687458289775],"true", 3) )
    # Connections for obj669 (graphObject_: Obj696) named A1 R1 G4
    self.drawConnections(
(self.obj669,self.obj689,[1873.0, 297.0, 1778.3648856811053, 322.6187458289775, 1682.1148856811053, 338.3687458289775],"true", 3) )
    # Connections for obj670 (graphObject_: Obj697) named A1 R1 G3
    self.drawConnections(
(self.obj670,self.obj690,[2285.0, 297.0, 2190.3648856811055, 322.6187458289775, 2094.1148856811055, 338.3687458289775],"true", 3) )
    # Connections for obj671 (graphObject_: Obj698) named A1 R1 G2
    self.drawConnections(
(self.obj671,self.obj691,[1667.0, 297.0, 1572.3648856811053, 322.6187458289775, 1476.1148856811053, 338.3687458289775],"true", 3) )
    # Connections for obj672 (graphObject_: Obj699) named A1 R2 G4
    self.drawConnections(
(self.obj672,self.obj692,[2697.0, 297.0, 2394.280152027154, 330.71952169437066, 2090.780152027154, 354.46952169437066],"true", 3) )
    # Connections for obj673 (graphObject_: Obj700) named A1 R2 G3
    self.drawConnections(
(self.obj673,self.obj693,[3109.0, 297.0, 2806.280152027154, 330.71952169437066, 2502.780152027154, 354.46952169437066],"true", 3) )
    # Connections for obj674 (graphObject_: Obj701) named A1 R2 G2
    self.drawConnections(
(self.obj674,self.obj694,[2491.0, 297.0, 2188.280152027154, 330.71952169437066, 1884.7801520271541, 354.46952169437066],"true", 3) )
    # Connections for obj675 (graphObject_: Obj702) named A1 R2 G1
    self.drawConnections(
(self.obj675,self.obj695,[2903.0, 297.0, 2600.280152027154, 330.71952169437066, 2296.780152027154, 354.46952169437066],"true", 3) )
    # Connections for obj676 (graphObject_: Obj703) named A2 R2 G4
    self.drawConnections(
(self.obj676,self.obj696,[1083.0, 297.0, 1176.8027515733322, 301.6212874041445, 1269.0527515733322, 316.1212874041445],"true", 3) )
    # Connections for obj677 (graphObject_: Obj704) named A2 R2 G3
    self.drawConnections(
(self.obj677,self.obj697,[1495.0, 297.0, 1588.8027515733322, 301.6212874041445, 1681.0527515733322, 316.1212874041445],"true", 3) )
    # Connections for obj678 (graphObject_: Obj705) named A2 R2 G2
    self.drawConnections(
(self.obj678,self.obj698,[877.0, 297.0, 970.8027515733323, 301.6212874041445, 1063.0527515733322, 316.1212874041445],"true", 3) )
    # Connections for obj679 (graphObject_: Obj706) named A2 R2 G1
    self.drawConnections(
(self.obj679,self.obj699,[1289.0, 297.0, 1382.8027515733322, 301.6212874041445, 1475.0527515733322, 316.1212874041445],"true", 3) )
    # Connections for obj680 (graphObject_: Obj707) named A3 R2 G4
    self.drawConnections(
(self.obj680,self.obj700,[259.0, 297.0, 557.0464525712106, 310.7817672929545, 854.2964525712106, 334.5317672929545],"true", 3) )
    # Connections for obj681 (graphObject_: Obj708) named A3 R2 G3
    self.drawConnections(
(self.obj681,self.obj701,[671.0, 297.0, 969.0464525712106, 310.7817672929545, 1266.2964525712105, 334.5317672929545],"true", 3) )
    # Connections for obj682 (graphObject_: Obj709) named A3 R2 G2
    self.drawConnections(
(self.obj682,self.obj702,[53.0, 297.0, 351.0464525712105, 310.7817672929545, 648.2964525712106, 334.5317672929545],"true", 3) )
    # Connections for obj683 (graphObject_: Obj710) named A3 R2 G1
    self.drawConnections(
(self.obj683,self.obj703,[465.0, 297.0, 763.0464525712106, 310.7817672929545, 1060.2964525712105, 334.5317672929545],"true", 3) )
    # Connections for obj684 (graphObject_: Obj711) of type fromRaw
    self.drawConnections(
(self.obj684,self.obj660,[2503.979904526288, 88.13364473182781, 2502.979904526288, 103.88364473182781, 2492.0, 119.0],"true", 3) )
    # Connections for obj685 (graphObject_: Obj713) of type fromRaw
    self.drawConnections(
(self.obj685,self.obj661,[2599.9773675579822, 77.95351989345416, 2650.4773675579822, 93.70351989345416, 2698.0, 119.0],"true", 3) )
    # Connections for obj686 (graphObject_: Obj715) of type fromRaw
    self.drawConnections(
(self.obj686,self.obj662,[1267.9799045262882, 88.13364473182781, 1266.9799045262882, 103.88364473182781, 1256.0, 119.0],"true", 3) )
    # Connections for obj687 (graphObject_: Obj717) of type fromRaw
    self.drawConnections(
(self.obj687,self.obj663,[443.9799045262882, 88.13364473182781, 442.9799045262882, 103.88364473182781, 432.0, 119.0],"true", 3) )
    # Connections for obj688 (graphObject_: Obj719) of type intoMaterial
    self.drawConnections(
(self.obj688,self.obj640,[1888.1148856811053, 338.3687458289775, 1791.8648856811053, 354.1187458289775, 1694.0, 360.0],"true", 3) )
    # Connections for obj689 (graphObject_: Obj721) of type intoMaterial
    self.drawConnections(
(self.obj689,self.obj643,[1682.1148856811053, 338.3687458289775, 1585.8648856811053, 354.1187458289775, 1488.0, 360.0],"true", 3) )
    # Connections for obj690 (graphObject_: Obj723) of type intoMaterial
    self.drawConnections(
(self.obj690,self.obj642,[2094.1148856811055, 338.3687458289775, 1997.8648856811053, 354.1187458289775, 1900.0, 360.0],"true", 3) )
    # Connections for obj691 (graphObject_: Obj725) of type intoMaterial
    self.drawConnections(
(self.obj691,self.obj641,[1476.1148856811053, 338.3687458289775, 1379.8648856811053, 354.1187458289775, 1282.0, 360.0],"true", 3) )
    # Connections for obj692 (graphObject_: Obj727) of type intoMaterial
    self.drawConnections(
(self.obj692,self.obj643,[2090.780152027154, 354.46952169437066, 1787.2801520271541, 378.21952169437066, 1483.0, 392.0],"true", 3) )
    # Connections for obj693 (graphObject_: Obj729) of type intoMaterial
    self.drawConnections(
(self.obj693,self.obj642,[2502.780152027154, 354.46952169437066, 2199.280152027154, 378.21952169437066, 1895.0, 392.0],"true", 3) )
    # Connections for obj694 (graphObject_: Obj731) of type intoMaterial
    self.drawConnections(
(self.obj694,self.obj641,[1884.7801520271541, 354.46952169437066, 1581.2801520271541, 378.21952169437066, 1277.0, 392.0],"true", 3) )
    # Connections for obj695 (graphObject_: Obj733) of type intoMaterial
    self.drawConnections(
(self.obj695,self.obj640,[2296.780152027154, 354.46952169437066, 1993.2801520271541, 378.21952169437066, 1689.0, 392.0],"true", 3) )
    # Connections for obj696 (graphObject_: Obj735) of type intoMaterial
    self.drawConnections(
(self.obj696,self.obj643,[1269.0527515733322, 316.1212874041445, 1361.3027515733322, 330.6212874041445, 1452.0, 355.0],"true", 3) )
    # Connections for obj697 (graphObject_: Obj737) of type intoMaterial
    self.drawConnections(
(self.obj697,self.obj642,[1681.0527515733322, 316.1212874041445, 1773.3027515733322, 330.6212874041445, 1864.0, 355.0],"true", 3) )
    # Connections for obj698 (graphObject_: Obj739) of type intoMaterial
    self.drawConnections(
(self.obj698,self.obj641,[1063.0527515733322, 316.1212874041445, 1155.3027515733322, 330.6212874041445, 1246.0, 355.0],"true", 3) )
    # Connections for obj699 (graphObject_: Obj741) of type intoMaterial
    self.drawConnections(
(self.obj699,self.obj640,[1475.0527515733322, 316.1212874041445, 1567.3027515733322, 330.6212874041445, 1658.0, 355.0],"true", 3) )
    # Connections for obj700 (graphObject_: Obj743) of type intoMaterial
    self.drawConnections(
(self.obj700,self.obj643,[854.2964525712106, 334.5317672929545, 1151.5464525712105, 358.2817672929545, 1448.0, 392.0],"true", 3) )
    # Connections for obj701 (graphObject_: Obj745) of type intoMaterial
    self.drawConnections(
(self.obj701,self.obj642,[1266.2964525712105, 334.5317672929545, 1563.5464525712105, 358.2817672929545, 1860.0, 392.0],"true", 3) )
    # Connections for obj702 (graphObject_: Obj747) of type intoMaterial
    self.drawConnections(
(self.obj702,self.obj641,[648.2964525712106, 334.5317672929545, 945.5464525712106, 358.2817672929545, 1242.0, 392.0],"true", 3) )
    # Connections for obj703 (graphObject_: Obj749) of type intoMaterial
    self.drawConnections(
(self.obj703,self.obj640,[1060.2964525712105, 334.5317672929545, 1357.5464525712105, 358.2817672929545, 1654.0, 392.0],"true", 3) )
    # Connections for obj704 (graphObject_: Obj751) of type intoMaterial
    self.drawConnections(
(self.obj704,self.obj644,[2305.1567821750014, 167.361798660721, 2211.4067821750014, 183.111798660721, 2116.0, 189.0],"true", 3) )
    # Connections for obj705 (graphObject_: Obj753) of type intoMaterial
    self.drawConnections(
(self.obj705,self.obj645,[2201.5780182679064, 167.4417240262472, 2056.3280182679064, 183.1917240262472, 1910.0, 189.0],"true", 3) )
    # Connections for obj706 (graphObject_: Obj755) of type intoMaterial
    self.drawConnections(
(self.obj706,self.obj646,[2409.992999454488, 166.8701096477546, 2367.742999454488, 182.6201096477546, 2322.0, 189.0],"true", 3) )
    # Connections for obj707 (graphObject_: Obj757) of type intoMaterial
    self.drawConnections(
(self.obj707,self.obj647,[2098.297955638446, 167.4681124993186, 1901.5479556384462, 183.2181124993186, 1704.0, 189.0],"true", 3) )
    # Connections for obj708 (graphObject_: Obj759) of type intoMaterial
    self.drawConnections(
(self.obj708,self.obj648,[2714.986832980505, 148.33772233983163, 2719.236832980505, 161.08772233983163, 2714.0, 177.0],"true", 3) )
    # Connections for obj709 (graphObject_: Obj761) of type intoMaterial
    self.drawConnections(
(self.obj709,self.obj649,[2922.0127318132636, 145.1150800478132, 3016.7627318132636, 159.6150800478132, 3110.0, 184.0],"true", 3) )
    # Connections for obj710 (graphObject_: Obj763) of type intoMaterial
    self.drawConnections(
(self.obj710,self.obj650,[2615.992999454488, 166.8701096477546, 2573.742999454488, 182.6201096477546, 2528.0, 189.0],"true", 3) )
    # Connections for obj711 (graphObject_: Obj765) of type intoMaterial
    self.drawConnections(
(self.obj711,self.obj651,[2820.678714537922, 145.51866180930125, 2863.928714537922, 160.01866180930125, 2904.0, 184.0],"true", 3) )
    # Connections for obj712 (graphObject_: Obj767) of type intoMaterial
    self.drawConnections(
(self.obj712,self.obj652,[1173.9929994544884, 166.8701096477546, 1131.7429994544884, 182.6201096477546, 1086.0, 189.0],"true", 3) )
    # Connections for obj713 (graphObject_: Obj769) of type intoMaterial
    self.drawConnections(
(self.obj713,self.obj653,[1378.6787145379221, 145.51866180930125, 1421.9287145379221, 160.01866180930125, 1462.0, 184.0],"true", 3) )
    # Connections for obj714 (graphObject_: Obj771) of type intoMaterial
    self.drawConnections(
(self.obj714,self.obj654,[1069.1567821750011, 167.361798660721, 975.4067821750011, 183.111798660721, 880.0, 189.0],"true", 3) )
    # Connections for obj715 (graphObject_: Obj773) of type intoMaterial
    self.drawConnections(
(self.obj715,self.obj655,[1272.9868329805051, 148.33772233983163, 1277.2368329805051, 161.08772233983163, 1272.0, 177.0],"true", 3) )
    # Connections for obj716 (graphObject_: Obj775) of type intoMaterial
    self.drawConnections(
(self.obj716,self.obj656,[349.9929994544884, 166.8701096477546, 307.7429994544884, 182.6201096477546, 262.0, 189.0],"true", 3) )
    # Connections for obj717 (graphObject_: Obj777) of type intoMaterial
    self.drawConnections(
(self.obj717,self.obj657,[554.6787145379221, 145.51866180930125, 597.9287145379221, 160.01866180930125, 638.0, 184.0],"true", 3) )
    # Connections for obj718 (graphObject_: Obj779) of type intoMaterial
    self.drawConnections(
(self.obj718,self.obj658,[245.15678217500113, 167.361798660721, 151.40678217500113, 183.111798660721, 56.0, 189.0],"true", 3) )
    # Connections for obj719 (graphObject_: Obj781) of type intoMaterial
    self.drawConnections(
(self.obj719,self.obj659,[448.98683298050514, 148.33772233983163, 453.23683298050514, 161.08772233983163, 448.0, 177.0],"true", 3) )
    # Connections for obj720 (graphObject_: Obj783) of type intoProduct
    self.drawConnections(
(self.obj720,self.obj639,[1679.9365296831495, 493.37510984719063, 1681.4365296831495, 506.62510984719063, 1673.0, 521.0],"true", 3) )
    # Connections for obj721 (graphObject_: Obj785) of type intoProduct
    self.drawConnections(
(self.obj721,self.obj639,[1482.3672469138317, 484.59390915261633, 1578.3672469138317, 497.84390915261633, 1673.0, 521.0],"true", 3) )
    # Connections for obj722 (graphObject_: Obj787) of type intoProduct
    self.drawConnections(
(self.obj722,self.obj639,[1775.5615823848773, 504.1663486221782, 1725.5615823848773, 517.4163486221782, 1673.0, 521.0],"true", 3) )
    # Connections for obj723 (graphObject_: Obj789) of type intoProduct
    self.drawConnections(
(self.obj723,self.obj639,[1586.853713602772, 484.9158297869167, 1631.353713602772, 498.1658297869167, 1673.0, 521.0],"true", 3) )
    # Connections for obj724 (graphObject_: Obj791) of type fromMaterial
    self.drawConnections(
(self.obj724,self.obj664,[1679.9792530896846, 430.64382277997964, 1678.9792530896846, 446.14382277997964, 1668.0, 461.0],"true", 3) )
    # Connections for obj725 (graphObject_: Obj793) of type fromMaterial
    self.drawConnections(
(self.obj725,self.obj665,[1267.9792530896846, 430.64382277997964, 1266.9792530896846, 446.14382277997964, 1256.0, 461.0],"true", 3) )
    # Connections for obj726 (graphObject_: Obj795) of type fromMaterial
    self.drawConnections(
(self.obj726,self.obj666,[1885.9792530896846, 430.64382277997964, 1884.9792530896846, 446.14382277997964, 1874.0, 461.0],"true", 3) )
    # Connections for obj727 (graphObject_: Obj797) of type fromMaterial
    self.drawConnections(
(self.obj727,self.obj667,[1473.9792530896846, 430.64382277997964, 1472.9792530896846, 446.14382277997964, 1462.0, 461.0],"true", 3) )
    # Connections for obj728 (graphObject_: Obj799) of type fromMaterial
    self.drawConnections(
(self.obj728,self.obj668,[2111.6827732370934, 256.5012198097823, 2115.6827732370934, 272.0012198097823, 2110.0, 290.0],"true", 3) )
    # Connections for obj729 (graphObject_: Obj801) of type fromMaterial
    self.drawConnections(
(self.obj729,self.obj669,[1905.6827732370937, 256.5012198097823, 1909.6827732370937, 272.0012198097823, 1904.0, 290.0],"true", 3) )
    # Connections for obj730 (graphObject_: Obj803) of type fromMaterial
    self.drawConnections(
(self.obj730,self.obj670,[2317.6827732370934, 256.5012198097823, 2321.6827732370934, 272.0012198097823, 2316.0, 290.0],"true", 3) )
    # Connections for obj731 (graphObject_: Obj805) of type fromMaterial
    self.drawConnections(
(self.obj731,self.obj671,[1699.6827732370937, 256.5012198097823, 1703.6827732370937, 272.0012198097823, 1698.0, 290.0],"true", 3) )
    # Connections for obj732 (graphObject_: Obj807) of type fromMaterial
    self.drawConnections(
(self.obj732,self.obj672,[2729.6827732370934, 256.5012198097823, 2733.6827732370934, 272.0012198097823, 2728.0, 290.0],"true", 3) )
    # Connections for obj733 (graphObject_: Obj809) of type fromMaterial
    self.drawConnections(
(self.obj733,self.obj673,[3141.6827732370934, 256.5012198097823, 3145.6827732370934, 272.0012198097823, 3140.0, 290.0],"true", 3) )
    # Connections for obj734 (graphObject_: Obj811) of type fromMaterial
    self.drawConnections(
(self.obj734,self.obj674,[2523.6827732370934, 256.5012198097823, 2527.6827732370934, 272.0012198097823, 2522.0, 290.0],"true", 3) )
    # Connections for obj735 (graphObject_: Obj813) of type fromMaterial
    self.drawConnections(
(self.obj735,self.obj675,[2935.6827732370934, 256.5012198097823, 2939.6827732370934, 272.0012198097823, 2934.0, 290.0],"true", 3) )
    # Connections for obj736 (graphObject_: Obj815) of type fromMaterial
    self.drawConnections(
(self.obj736,self.obj676,[1081.6827732370937, 256.5012198097823, 1085.6827732370937, 272.0012198097823, 1080.0, 290.0],"true", 3) )
    # Connections for obj737 (graphObject_: Obj817) of type fromMaterial
    self.drawConnections(
(self.obj737,self.obj677,[1493.6827732370937, 256.5012198097823, 1497.6827732370937, 272.0012198097823, 1492.0, 290.0],"true", 3) )
    # Connections for obj738 (graphObject_: Obj819) of type fromMaterial
    self.drawConnections(
(self.obj738,self.obj678,[875.6827732370936, 256.5012198097823, 879.6827732370936, 272.0012198097823, 874.0, 290.0],"true", 3) )
    # Connections for obj739 (graphObject_: Obj821) of type fromMaterial
    self.drawConnections(
(self.obj739,self.obj679,[1287.6827732370937, 256.5012198097823, 1291.6827732370937, 272.0012198097823, 1286.0, 290.0],"true", 3) )
    # Connections for obj740 (graphObject_: Obj823) of type fromMaterial
    self.drawConnections(
(self.obj740,self.obj680,[257.68277323709356, 256.5012198097823, 261.68277323709356, 272.0012198097823, 256.0, 290.0],"true", 3) )
    # Connections for obj741 (graphObject_: Obj825) of type fromMaterial
    self.drawConnections(
(self.obj741,self.obj681,[669.6827732370936, 256.5012198097823, 673.6827732370936, 272.0012198097823, 668.0, 290.0],"true", 3) )
    # Connections for obj742 (graphObject_: Obj827) of type fromMaterial
    self.drawConnections(
(self.obj742,self.obj682,[51.68277323709358, 256.5012198097823, 55.68277323709358, 272.0012198097823, 50.0, 290.0],"true", 3) )
    # Connections for obj743 (graphObject_: Obj829) of type fromMaterial
    self.drawConnections(
(self.obj743,self.obj683,[463.68277323709356, 256.5012198097823, 467.68277323709356, 272.0012198097823, 462.0, 290.0],"true", 3) )

newfunction = pnsEx4_MDL

loadedMMName = 'pns_META'

atom3version = '0.3'
