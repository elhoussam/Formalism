"""
__pnsEx3_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: sam
Modified: Sat May 13 15:53:06 2017
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

def pnsEx3_MDL(self, rootNode, pnsRootNode=None):

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


    self.obj356=rawMaterial(self)
    self.obj356.isGraphObjectVisual = True

    if(hasattr(self.obj356, '_setHierarchicalLink')):
      self.obj356._setHierarchicalLink(False)

    # MaxFlow
    self.obj356.MaxFlow.setValue(999999)

    # price
    self.obj356.price.setValue(5)

    # Name
    self.obj356.Name.setValue('A1')

    # ReqFlow
    self.obj356.ReqFlow.setValue(0)

    self.obj356.graphClass_= graph_rawMaterial
    if self.genGraphics:
       new_obj = graph_rawMaterial(824,0,self.obj356)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rawMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj356.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj356)
    self.globalAndLocalPostcondition(self.obj356, rootNode)
    self.obj356.postAction( rootNode.CREATE )

    self.obj358=rawMaterial(self)
    self.obj358.isGraphObjectVisual = True

    if(hasattr(self.obj358, '_setHierarchicalLink')):
      self.obj358._setHierarchicalLink(False)

    # MaxFlow
    self.obj358.MaxFlow.setValue(999999)

    # price
    self.obj358.price.setValue(5)

    # Name
    self.obj358.Name.setValue('A2')

    # ReqFlow
    self.obj358.ReqFlow.setValue(0)

    self.obj358.graphClass_= graph_rawMaterial
    if self.genGraphics:
       new_obj = graph_rawMaterial(206,0,self.obj358)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rawMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj358.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj358)
    self.globalAndLocalPostcondition(self.obj358, rootNode)
    self.obj358.postAction( rootNode.CREATE )

    self.obj360=operatingUnit(self)
    self.obj360.isGraphObjectVisual = True

    if(hasattr(self.obj360, '_setHierarchicalLink')):
      self.obj360._setHierarchicalLink(False)

    # OperCostProp
    self.obj360.OperCostProp.setValue(0.5)

    # name
    self.obj360.name.setValue('A1 R1')

    # OperCostFix
    self.obj360.OperCostFix.setValue(0.0)

    self.obj360.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(824,108,self.obj360)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj360.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj360)
    self.globalAndLocalPostcondition(self.obj360, rootNode)
    self.obj360.postAction( rootNode.CREATE )

    self.obj362=operatingUnit(self)
    self.obj362.isGraphObjectVisual = True

    if(hasattr(self.obj362, '_setHierarchicalLink')):
      self.obj362._setHierarchicalLink(False)

    # OperCostProp
    self.obj362.OperCostProp.setValue(0.5)

    # name
    self.obj362.name.setValue('A1 R2')

    # OperCostFix
    self.obj362.OperCostFix.setValue(0.0)

    self.obj362.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(618,108,self.obj362)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj362.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj362)
    self.globalAndLocalPostcondition(self.obj362, rootNode)
    self.obj362.postAction( rootNode.CREATE )

    self.obj364=operatingUnit(self)
    self.obj364.isGraphObjectVisual = True

    if(hasattr(self.obj364, '_setHierarchicalLink')):
      self.obj364._setHierarchicalLink(False)

    # OperCostProp
    self.obj364.OperCostProp.setValue(0.5)

    # name
    self.obj364.name.setValue('A1 R3')

    # OperCostFix
    self.obj364.OperCostFix.setValue(0.0)

    self.obj364.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(1030,108,self.obj364)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj364.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj364)
    self.globalAndLocalPostcondition(self.obj364, rootNode)
    self.obj364.postAction( rootNode.CREATE )

    self.obj366=operatingUnit(self)
    self.obj366.isGraphObjectVisual = True

    if(hasattr(self.obj366, '_setHierarchicalLink')):
      self.obj366._setHierarchicalLink(False)

    # OperCostProp
    self.obj366.OperCostProp.setValue(0.25)

    # name
    self.obj366.name.setValue('A2 R2')

    # OperCostFix
    self.obj366.OperCostFix.setValue(0.0)

    self.obj366.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(0,108,self.obj366)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj366.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj366)
    self.globalAndLocalPostcondition(self.obj366, rootNode)
    self.obj366.postAction( rootNode.CREATE )

    self.obj368=operatingUnit(self)
    self.obj368.isGraphObjectVisual = True

    if(hasattr(self.obj368, '_setHierarchicalLink')):
      self.obj368._setHierarchicalLink(False)

    # OperCostProp
    self.obj368.OperCostProp.setValue(0.25)

    # name
    self.obj368.name.setValue('A2 R3')

    # OperCostFix
    self.obj368.OperCostFix.setValue(0.0)

    self.obj368.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(206,108,self.obj368)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj368.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj368)
    self.globalAndLocalPostcondition(self.obj368, rootNode)
    self.obj368.postAction( rootNode.CREATE )

    self.obj381=operatingUnit(self)
    self.obj381.isGraphObjectVisual = True

    if(hasattr(self.obj381, '_setHierarchicalLink')):
      self.obj381._setHierarchicalLink(False)

    # OperCostProp
    self.obj381.OperCostProp.setValue(1.0)

    # name
    self.obj381.name.setValue('G1 OAF')

    # OperCostFix
    self.obj381.OperCostFix.setValue(2.0)

    self.obj381.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(824,450,self.obj381)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj381.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj381)
    self.globalAndLocalPostcondition(self.obj381, rootNode)
    self.obj381.postAction( rootNode.CREATE )

    self.obj384=operatingUnit(self)
    self.obj384.isGraphObjectVisual = True

    if(hasattr(self.obj384, '_setHierarchicalLink')):
      self.obj384._setHierarchicalLink(False)

    # OperCostProp
    self.obj384.OperCostProp.setValue(1.0)

    # name
    self.obj384.name.setValue('G2 OAF')

    # OperCostFix
    self.obj384.OperCostFix.setValue(2.0)

    self.obj384.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(412,450,self.obj384)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj384.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj384)
    self.globalAndLocalPostcondition(self.obj384, rootNode)
    self.obj384.postAction( rootNode.CREATE )

    self.obj387=operatingUnit(self)
    self.obj387.isGraphObjectVisual = True

    if(hasattr(self.obj387, '_setHierarchicalLink')):
      self.obj387._setHierarchicalLink(False)

    # OperCostProp
    self.obj387.OperCostProp.setValue(1.0)

    # name
    self.obj387.name.setValue('G3 OAF')

    # OperCostFix
    self.obj387.OperCostFix.setValue(2.0)

    self.obj387.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(618,450,self.obj387)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj387.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj387)
    self.globalAndLocalPostcondition(self.obj387, rootNode)
    self.obj387.postAction( rootNode.CREATE )

    self.obj391=operatingUnit(self)
    self.obj391.isGraphObjectVisual = True

    if(hasattr(self.obj391, '_setHierarchicalLink')):
      self.obj391._setHierarchicalLink(False)

    # OperCostProp
    self.obj391.OperCostProp.setValue(0.11)

    # name
    self.obj391.name.setValue('A1 R1 G1')

    # OperCostFix
    self.obj391.OperCostFix.setValue(2.0)

    self.obj391.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(824,279,self.obj391)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj391.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj391)
    self.globalAndLocalPostcondition(self.obj391, rootNode)
    self.obj391.postAction( rootNode.CREATE )

    self.obj395=operatingUnit(self)
    self.obj395.isGraphObjectVisual = True

    if(hasattr(self.obj395, '_setHierarchicalLink')):
      self.obj395._setHierarchicalLink(False)

    # OperCostProp
    self.obj395.OperCostProp.setValue(0.12)

    # name
    self.obj395.name.setValue('A1 R1 G2')

    # OperCostFix
    self.obj395.OperCostFix.setValue(2.0)

    self.obj395.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(618,279,self.obj395)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj395.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj395)
    self.globalAndLocalPostcondition(self.obj395, rootNode)
    self.obj395.postAction( rootNode.CREATE )

    self.obj399=operatingUnit(self)
    self.obj399.isGraphObjectVisual = True

    if(hasattr(self.obj399, '_setHierarchicalLink')):
      self.obj399._setHierarchicalLink(False)

    # OperCostProp
    self.obj399.OperCostProp.setValue(0.22)

    # name
    self.obj399.name.setValue('A1 R2 G2')

    # OperCostFix
    self.obj399.OperCostFix.setValue(2.0)

    self.obj399.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(412,279,self.obj399)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj399.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj399)
    self.globalAndLocalPostcondition(self.obj399, rootNode)
    self.obj399.postAction( rootNode.CREATE )

    self.obj403=operatingUnit(self)
    self.obj403.isGraphObjectVisual = True

    if(hasattr(self.obj403, '_setHierarchicalLink')):
      self.obj403._setHierarchicalLink(False)

    # OperCostProp
    self.obj403.OperCostProp.setValue(0.44)

    # name
    self.obj403.name.setValue('A1 R3 G3')

    # OperCostFix
    self.obj403.OperCostFix.setValue(2.0)

    self.obj403.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(1030,279,self.obj403)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj403.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj403)
    self.globalAndLocalPostcondition(self.obj403, rootNode)
    self.obj403.postAction( rootNode.CREATE )

    self.obj407=operatingUnit(self)
    self.obj407.isGraphObjectVisual = True

    if(hasattr(self.obj407, '_setHierarchicalLink')):
      self.obj407._setHierarchicalLink(False)

    # OperCostProp
    self.obj407.OperCostProp.setValue(0.22)

    # name
    self.obj407.name.setValue('A2 R2 G2')

    # OperCostFix
    self.obj407.OperCostFix.setValue(2.0)

    self.obj407.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(0,279,self.obj407)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj407.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj407)
    self.globalAndLocalPostcondition(self.obj407, rootNode)
    self.obj407.postAction( rootNode.CREATE )

    self.obj411=operatingUnit(self)
    self.obj411.isGraphObjectVisual = True

    if(hasattr(self.obj411, '_setHierarchicalLink')):
      self.obj411._setHierarchicalLink(False)

    # OperCostProp
    self.obj411.OperCostProp.setValue(0.44)

    # name
    self.obj411.name.setValue('A2 R3 G3')

    # OperCostFix
    self.obj411.OperCostFix.setValue(2.0)

    self.obj411.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(206,279,self.obj411)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj411.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj411)
    self.globalAndLocalPostcondition(self.obj411, rootNode)
    self.obj411.postAction( rootNode.CREATE )

    self.obj370=metarial(self)
    self.obj370.isGraphObjectVisual = True

    if(hasattr(self.obj370, '_setHierarchicalLink')):
      self.obj370._setHierarchicalLink(False)

    # MaxFlow
    self.obj370.MaxFlow.setValue(999999)

    # price
    self.obj370.price.setValue(0)

    # Name
    self.obj370.Name.setValue('G1')

    # ReqFlow
    self.obj370.ReqFlow.setValue(0)

    self.obj370.graphClass_= graph_metarial
    if self.genGraphics:
       new_obj = graph_metarial(824,350,self.obj370)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("metarial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj370.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj370)
    self.globalAndLocalPostcondition(self.obj370, rootNode)
    self.obj370.postAction( rootNode.CREATE )

    self.obj372=metarial(self)
    self.obj372.isGraphObjectVisual = True

    if(hasattr(self.obj372, '_setHierarchicalLink')):
      self.obj372._setHierarchicalLink(False)

    # MaxFlow
    self.obj372.MaxFlow.setValue(999999)

    # price
    self.obj372.price.setValue(0)

    # Name
    self.obj372.Name.setValue('G2')

    # ReqFlow
    self.obj372.ReqFlow.setValue(0)

    self.obj372.graphClass_= graph_metarial
    if self.genGraphics:
       new_obj = graph_metarial(412,350,self.obj372)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("metarial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj372.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj372)
    self.globalAndLocalPostcondition(self.obj372, rootNode)
    self.obj372.postAction( rootNode.CREATE )

    self.obj374=metarial(self)
    self.obj374.isGraphObjectVisual = True

    if(hasattr(self.obj374, '_setHierarchicalLink')):
      self.obj374._setHierarchicalLink(False)

    # MaxFlow
    self.obj374.MaxFlow.setValue(999999)

    # price
    self.obj374.price.setValue(0)

    # Name
    self.obj374.Name.setValue('G3')

    # ReqFlow
    self.obj374.ReqFlow.setValue(0)

    self.obj374.graphClass_= graph_metarial
    if self.genGraphics:
       new_obj = graph_metarial(618,350,self.obj374)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("metarial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj374.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj374)
    self.globalAndLocalPostcondition(self.obj374, rootNode)
    self.obj374.postAction( rootNode.CREATE )

    self.obj392=metarial(self)
    self.obj392.isGraphObjectVisual = True

    if(hasattr(self.obj392, '_setHierarchicalLink')):
      self.obj392._setHierarchicalLink(False)

    # MaxFlow
    self.obj392.MaxFlow.setValue(999999)

    # price
    self.obj392.price.setValue(0)

    # Name
    self.obj392.Name.setValue('A1 R1 G1')

    # ReqFlow
    self.obj392.ReqFlow.setValue(0)

    self.obj392.graphClass_= graph_metarial
    if self.genGraphics:
       new_obj = graph_metarial(824,179,self.obj392)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("metarial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj392.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj392)
    self.globalAndLocalPostcondition(self.obj392, rootNode)
    self.obj392.postAction( rootNode.CREATE )

    self.obj396=metarial(self)
    self.obj396.isGraphObjectVisual = True

    if(hasattr(self.obj396, '_setHierarchicalLink')):
      self.obj396._setHierarchicalLink(False)

    # MaxFlow
    self.obj396.MaxFlow.setValue(999999)

    # price
    self.obj396.price.setValue(0)

    # Name
    self.obj396.Name.setValue('A1 R1 G2')

    # ReqFlow
    self.obj396.ReqFlow.setValue(0)

    self.obj396.graphClass_= graph_metarial
    if self.genGraphics:
       new_obj = graph_metarial(618,179,self.obj396)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("metarial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj396.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj396)
    self.globalAndLocalPostcondition(self.obj396, rootNode)
    self.obj396.postAction( rootNode.CREATE )

    self.obj400=metarial(self)
    self.obj400.isGraphObjectVisual = True

    if(hasattr(self.obj400, '_setHierarchicalLink')):
      self.obj400._setHierarchicalLink(False)

    # MaxFlow
    self.obj400.MaxFlow.setValue(999999)

    # price
    self.obj400.price.setValue(0)

    # Name
    self.obj400.Name.setValue('A1 R2 G2')

    # ReqFlow
    self.obj400.ReqFlow.setValue(0)

    self.obj400.graphClass_= graph_metarial
    if self.genGraphics:
       new_obj = graph_metarial(412,179,self.obj400)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("metarial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj400.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj400)
    self.globalAndLocalPostcondition(self.obj400, rootNode)
    self.obj400.postAction( rootNode.CREATE )

    self.obj404=metarial(self)
    self.obj404.isGraphObjectVisual = True

    if(hasattr(self.obj404, '_setHierarchicalLink')):
      self.obj404._setHierarchicalLink(False)

    # MaxFlow
    self.obj404.MaxFlow.setValue(999999)

    # price
    self.obj404.price.setValue(0)

    # Name
    self.obj404.Name.setValue('A1 R3 G3')

    # ReqFlow
    self.obj404.ReqFlow.setValue(0)

    self.obj404.graphClass_= graph_metarial
    if self.genGraphics:
       new_obj = graph_metarial(1030,179,self.obj404)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("metarial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj404.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj404)
    self.globalAndLocalPostcondition(self.obj404, rootNode)
    self.obj404.postAction( rootNode.CREATE )

    self.obj408=metarial(self)
    self.obj408.isGraphObjectVisual = True

    if(hasattr(self.obj408, '_setHierarchicalLink')):
      self.obj408._setHierarchicalLink(False)

    # MaxFlow
    self.obj408.MaxFlow.setValue(999999)

    # price
    self.obj408.price.setValue(0)

    # Name
    self.obj408.Name.setValue('A2 R2 G2')

    # ReqFlow
    self.obj408.ReqFlow.setValue(0)

    self.obj408.graphClass_= graph_metarial
    if self.genGraphics:
       new_obj = graph_metarial(0,179,self.obj408)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("metarial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj408.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj408)
    self.globalAndLocalPostcondition(self.obj408, rootNode)
    self.obj408.postAction( rootNode.CREATE )

    self.obj412=metarial(self)
    self.obj412.isGraphObjectVisual = True

    if(hasattr(self.obj412, '_setHierarchicalLink')):
      self.obj412._setHierarchicalLink(False)

    # MaxFlow
    self.obj412.MaxFlow.setValue(999999)

    # price
    self.obj412.price.setValue(0)

    # Name
    self.obj412.Name.setValue('A2 R3 G3')

    # ReqFlow
    self.obj412.ReqFlow.setValue(0)

    self.obj412.graphClass_= graph_metarial
    if self.genGraphics:
       new_obj = graph_metarial(206,179,self.obj412)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("metarial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj412.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj412)
    self.globalAndLocalPostcondition(self.obj412, rootNode)
    self.obj412.postAction( rootNode.CREATE )

    self.obj380=product(self)
    self.obj380.isGraphObjectVisual = True

    if(hasattr(self.obj380, '_setHierarchicalLink')):
      self.obj380._setHierarchicalLink(False)

    # MaxFlow
    self.obj380.MaxFlow.setValue(999999)

    # price
    self.obj380.price.setValue(0)

    # Name
    self.obj380.Name.setValue('OAF')

    # ReqFlow
    self.obj380.ReqFlow.setValue(0)

    self.obj380.graphClass_= graph_product
    if self.genGraphics:
       new_obj = graph_product(618,521,self.obj380)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("product", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj380.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj380)
    self.globalAndLocalPostcondition(self.obj380, rootNode)
    self.obj380.postAction( rootNode.CREATE )

    self.obj382=fromMaterial(self)
    self.obj382.isGraphObjectVisual = True

    if(hasattr(self.obj382, '_setHierarchicalLink')):
      self.obj382._setHierarchicalLink(False)

    # rate
    self.obj382.rate.setValue(1.0)

    self.obj382.graphClass_= graph_fromMaterial
    if self.genGraphics:
       new_obj = graph_fromMaterial(855.737086465,430.879758202,self.obj382)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj382.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj382)
    self.globalAndLocalPostcondition(self.obj382, rootNode)
    self.obj382.postAction( rootNode.CREATE )

    self.obj385=fromMaterial(self)
    self.obj385.isGraphObjectVisual = True

    if(hasattr(self.obj385, '_setHierarchicalLink')):
      self.obj385._setHierarchicalLink(False)

    # rate
    self.obj385.rate.setValue(1.0)

    self.obj385.graphClass_= graph_fromMaterial
    if self.genGraphics:
       new_obj = graph_fromMaterial(444.337807112,430.492398809,self.obj385)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj385.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj385)
    self.globalAndLocalPostcondition(self.obj385, rootNode)
    self.obj385.postAction( rootNode.CREATE )

    self.obj388=fromMaterial(self)
    self.obj388.isGraphObjectVisual = True

    if(hasattr(self.obj388, '_setHierarchicalLink')):
      self.obj388._setHierarchicalLink(False)

    # rate
    self.obj388.rate.setValue(1.0)

    self.obj388.graphClass_= graph_fromMaterial
    if self.genGraphics:
       new_obj = graph_fromMaterial(649.978915441,430.399035151,self.obj388)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj388.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj388)
    self.globalAndLocalPostcondition(self.obj388, rootNode)
    self.obj388.postAction( rootNode.CREATE )

    self.obj393=fromMaterial(self)
    self.obj393.isGraphObjectVisual = True

    if(hasattr(self.obj393, '_setHierarchicalLink')):
      self.obj393._setHierarchicalLink(False)

    # rate
    self.obj393.rate.setValue(1.0)

    self.obj393.graphClass_= graph_fromMaterial
    if self.genGraphics:
       new_obj = graph_fromMaterial(875.568960332,256.488862275,self.obj393)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj393.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj393)
    self.globalAndLocalPostcondition(self.obj393, rootNode)
    self.obj393.postAction( rootNode.CREATE )

    self.obj397=fromMaterial(self)
    self.obj397.isGraphObjectVisual = True

    if(hasattr(self.obj397, '_setHierarchicalLink')):
      self.obj397._setHierarchicalLink(False)

    # rate
    self.obj397.rate.setValue(1.0)

    self.obj397.graphClass_= graph_fromMaterial
    if self.genGraphics:
       new_obj = graph_fromMaterial(669.573905866,256.257840786,self.obj397)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj397.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj397)
    self.globalAndLocalPostcondition(self.obj397, rootNode)
    self.obj397.postAction( rootNode.CREATE )

    self.obj401=fromMaterial(self)
    self.obj401.isGraphObjectVisual = True

    if(hasattr(self.obj401, '_setHierarchicalLink')):
      self.obj401._setHierarchicalLink(False)

    # rate
    self.obj401.rate.setValue(1.0)

    self.obj401.graphClass_= graph_fromMaterial
    if self.genGraphics:
       new_obj = graph_fromMaterial(463.783974511,256.60991939,self.obj401)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj401.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj401)
    self.globalAndLocalPostcondition(self.obj401, rootNode)
    self.obj401.postAction( rootNode.CREATE )

    self.obj405=fromMaterial(self)
    self.obj405.isGraphObjectVisual = True

    if(hasattr(self.obj405, '_setHierarchicalLink')):
      self.obj405._setHierarchicalLink(False)

    # rate
    self.obj405.rate.setValue(1.0)

    self.obj405.graphClass_= graph_fromMaterial
    if self.genGraphics:
       new_obj = graph_fromMaterial(1081.68759415,256.269975897,self.obj405)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj405.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj405)
    self.globalAndLocalPostcondition(self.obj405, rootNode)
    self.obj405.postAction( rootNode.CREATE )

    self.obj409=fromMaterial(self)
    self.obj409.isGraphObjectVisual = True

    if(hasattr(self.obj409, '_setHierarchicalLink')):
      self.obj409._setHierarchicalLink(False)

    # rate
    self.obj409.rate.setValue(1.0)

    self.obj409.graphClass_= graph_fromMaterial
    if self.genGraphics:
       new_obj = graph_fromMaterial(51.5199586435,256.305737285,self.obj409)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj409.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj409)
    self.globalAndLocalPostcondition(self.obj409, rootNode)
    self.obj409.postAction( rootNode.CREATE )

    self.obj413=fromMaterial(self)
    self.obj413.isGraphObjectVisual = True

    if(hasattr(self.obj413, '_setHierarchicalLink')):
      self.obj413._setHierarchicalLink(False)

    # rate
    self.obj413.rate.setValue(1.0)

    self.obj413.graphClass_= graph_fromMaterial
    if self.genGraphics:
       new_obj = graph_fromMaterial(242.524577994,260.861308847,self.obj413)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj413.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj413)
    self.globalAndLocalPostcondition(self.obj413, rootNode)
    self.obj413.postAction( rootNode.CREATE )

    self.obj383=intoProduct(self)
    self.obj383.isGraphObjectVisual = True

    if(hasattr(self.obj383, '_setHierarchicalLink')):
      self.obj383._setHierarchicalLink(False)

    # rate
    self.obj383.rate.setValue(1.0)

    self.obj383.graphClass_= graph_intoProduct
    if self.genGraphics:
       new_obj = graph_intoProduct(745.301840365,504.390372225,self.obj383)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoProduct", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj383.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj383)
    self.globalAndLocalPostcondition(self.obj383, rootNode)
    self.obj383.postAction( rootNode.CREATE )

    self.obj386=intoProduct(self)
    self.obj386.isGraphObjectVisual = True

    if(hasattr(self.obj386, '_setHierarchicalLink')):
      self.obj386._setHierarchicalLink(False)

    # rate
    self.obj386.rate.setValue(1.0)

    self.obj386.graphClass_= graph_intoProduct
    if self.genGraphics:
       new_obj = graph_intoProduct(557.000722908,484.691771822,self.obj386)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoProduct", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj386.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj386)
    self.globalAndLocalPostcondition(self.obj386, rootNode)
    self.obj386.postAction( rootNode.CREATE )

    self.obj389=intoProduct(self)
    self.obj389.isGraphObjectVisual = True

    if(hasattr(self.obj389, '_setHierarchicalLink')):
      self.obj389._setHierarchicalLink(False)

    # rate
    self.obj389.rate.setValue(1.0)

    self.obj389.graphClass_= graph_intoProduct
    if self.genGraphics:
       new_obj = graph_intoProduct(649.937699489,493.135491646,self.obj389)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoProduct", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj389.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj389)
    self.globalAndLocalPostcondition(self.obj389, rootNode)
    self.obj389.postAction( rootNode.CREATE )

    self.obj375=fromRaw(self)
    self.obj375.isGraphObjectVisual = True

    if(hasattr(self.obj375, '_setHierarchicalLink')):
      self.obj375._setHierarchicalLink(False)

    # rate
    self.obj375.rate.setValue(1.0)

    self.obj375.graphClass_= graph_fromRaw
    if self.genGraphics:
       new_obj = graph_fromRaw(855.87628537,88.5486817113,self.obj375)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromRaw", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj375.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj375)
    self.globalAndLocalPostcondition(self.obj375, rootNode)
    self.obj375.postAction( rootNode.CREATE )

    self.obj376=fromRaw(self)
    self.obj376.isGraphObjectVisual = True

    if(hasattr(self.obj376, '_setHierarchicalLink')):
      self.obj376._setHierarchicalLink(False)

    # rate
    self.obj376.rate.setValue(1.0)

    self.obj376.graphClass_= graph_fromRaw
    if self.genGraphics:
       new_obj = graph_fromRaw(763.074026367,100.714226374,self.obj376)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromRaw", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj376.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj376)
    self.globalAndLocalPostcondition(self.obj376, rootNode)
    self.obj376.postAction( rootNode.CREATE )

    self.obj377=fromRaw(self)
    self.obj377.isGraphObjectVisual = True

    if(hasattr(self.obj377, '_setHierarchicalLink')):
      self.obj377._setHierarchicalLink(False)

    # rate
    self.obj377.rate.setValue(1.0)

    self.obj377.graphClass_= graph_fromRaw
    if self.genGraphics:
       new_obj = graph_fromRaw(951.873748401,78.3685568729,self.obj377)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromRaw", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj377.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj377)
    self.globalAndLocalPostcondition(self.obj377, rootNode)
    self.obj377.postAction( rootNode.CREATE )

    self.obj378=fromRaw(self)
    self.obj378.isGraphObjectVisual = True

    if(hasattr(self.obj378, '_setHierarchicalLink')):
      self.obj378._setHierarchicalLink(False)

    # rate
    self.obj378.rate.setValue(1.0)

    self.obj378.graphClass_= graph_fromRaw
    if self.genGraphics:
       new_obj = graph_fromRaw(145.634335201,100.299189395,self.obj378)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromRaw", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj378.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj378)
    self.globalAndLocalPostcondition(self.obj378, rootNode)
    self.obj378.postAction( rootNode.CREATE )

    self.obj379=fromRaw(self)
    self.obj379.isGraphObjectVisual = True

    if(hasattr(self.obj379, '_setHierarchicalLink')):
      self.obj379._setHierarchicalLink(False)

    # rate
    self.obj379.rate.setValue(1.0)

    self.obj379.graphClass_= graph_fromRaw
    if self.genGraphics:
       new_obj = graph_fromRaw(238.436594204,88.1336447318,self.obj379)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromRaw", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj379.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj379)
    self.globalAndLocalPostcondition(self.obj379, rootNode)
    self.obj379.postAction( rootNode.CREATE )

    self.obj414=intoMaterial(self)
    self.obj414.isGraphObjectVisual = True

    if(hasattr(self.obj414, '_setHierarchicalLink')):
      self.obj414._setHierarchicalLink(False)

    # rate
    self.obj414.rate.setValue(0.11)

    self.obj414.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(856.414870379,321.074400891,self.obj414)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj414.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj414)
    self.globalAndLocalPostcondition(self.obj414, rootNode)
    self.obj414.postAction( rootNode.CREATE )

    self.obj415=intoMaterial(self)
    self.obj415.isGraphObjectVisual = True

    if(hasattr(self.obj415, '_setHierarchicalLink')):
      self.obj415._setHierarchicalLink(False)

    # rate
    self.obj415.rate.setValue(0.12)

    self.obj415.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(551.07230534,337.964836901,self.obj415)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj415.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj415)
    self.globalAndLocalPostcondition(self.obj415, rootNode)
    self.obj415.postAction( rootNode.CREATE )

    self.obj416=intoMaterial(self)
    self.obj416.isGraphObjectVisual = True

    if(hasattr(self.obj416, '_setHierarchicalLink')):
      self.obj416._setHierarchicalLink(False)

    # rate
    self.obj416.rate.setValue(0.22)

    self.obj416.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(444.635404612,321.086499179,self.obj416)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj416.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj416)
    self.globalAndLocalPostcondition(self.obj416, rootNode)
    self.obj416.postAction( rootNode.CREATE )

    self.obj417=intoMaterial(self)
    self.obj417.isGraphObjectVisual = True

    if(hasattr(self.obj417, '_setHierarchicalLink')):
      self.obj417._setHierarchicalLink(False)

    # rate
    self.obj417.rate.setValue(0.44)

    self.obj417.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(858.114885681,338.368745829,self.obj417)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj417.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj417)
    self.globalAndLocalPostcondition(self.obj417, rootNode)
    self.obj417.postAction( rootNode.CREATE )

    self.obj418=intoMaterial(self)
    self.obj418.isGraphObjectVisual = True

    if(hasattr(self.obj418, '_setHierarchicalLink')):
      self.obj418._setHierarchicalLink(False)

    # rate
    self.obj418.rate.setValue(0.22)

    self.obj418.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(239.293672817,316.157295397,self.obj418)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj418.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj418)
    self.globalAndLocalPostcondition(self.obj418, rootNode)
    self.obj418.postAction( rootNode.CREATE )

    self.obj419=intoMaterial(self)
    self.obj419.isGraphObjectVisual = True

    if(hasattr(self.obj419, '_setHierarchicalLink')):
      self.obj419._setHierarchicalLink(False)

    # rate
    self.obj419.rate.setValue(0.44)

    self.obj419.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(445.052751573,316.121287404,self.obj419)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj419.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj419)
    self.globalAndLocalPostcondition(self.obj419, rootNode)
    self.obj419.postAction( rootNode.CREATE )

    self.obj420=intoMaterial(self)
    self.obj420.isGraphObjectVisual = True

    if(hasattr(self.obj420, '_setHierarchicalLink')):
      self.obj420._setHierarchicalLink(False)

    # rate
    self.obj420.rate.setValue(0.5)

    self.obj420.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(860.828616264,148.562235573,self.obj420)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj420.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj420)
    self.globalAndLocalPostcondition(self.obj420, rootNode)
    self.obj420.postAction( rootNode.CREATE )

    self.obj421=intoMaterial(self)
    self.obj421.isGraphObjectVisual = True

    if(hasattr(self.obj421, '_setHierarchicalLink')):
      self.obj421._setHierarchicalLink(False)

    # rate
    self.obj421.rate.setValue(0.5)

    self.obj421.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(761.79115358,166.864145038,self.obj421)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj421.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj421)
    self.globalAndLocalPostcondition(self.obj421, rootNode)
    self.obj421.postAction( rootNode.CREATE )

    self.obj422=intoMaterial(self)
    self.obj422.isGraphObjectVisual = True

    if(hasattr(self.obj422, '_setHierarchicalLink')):
      self.obj422._setHierarchicalLink(False)

    # rate
    self.obj422.rate.setValue(0.55)

    self.obj422.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(556.030490534,167.167194121,self.obj422)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj422.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj422)
    self.globalAndLocalPostcondition(self.obj422, rootNode)
    self.obj422.postAction( rootNode.CREATE )

    self.obj423=intoMaterial(self)
    self.obj423.isGraphObjectVisual = True

    if(hasattr(self.obj423, '_setHierarchicalLink')):
      self.obj423._setHierarchicalLink(False)

    # rate
    self.obj423.rate.setValue(0.3)

    self.obj423.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(1066.91160597,148.22583685,self.obj423)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj423.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj423)
    self.globalAndLocalPostcondition(self.obj423, rootNode)
    self.obj423.postAction( rootNode.CREATE )

    self.obj424=intoMaterial(self)
    self.obj424.isGraphObjectVisual = True

    if(hasattr(self.obj424, '_setHierarchicalLink')):
      self.obj424._setHierarchicalLink(False)

    # rate
    self.obj424.rate.setValue(0.25)

    self.obj424.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(37.0972332379,148.286219461,self.obj424)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj424.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj424)
    self.globalAndLocalPostcondition(self.obj424, rootNode)
    self.obj424.postAction( rootNode.CREATE )

    self.obj425=intoMaterial(self)
    self.obj425.isGraphObjectVisual = True

    if(hasattr(self.obj425, '_setHierarchicalLink')):
      self.obj425._setHierarchicalLink(False)

    # rate
    self.obj425.rate.setValue(0.3)

    self.obj425.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(243.008957889,148.222226085,self.obj425)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj425.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj425)
    self.globalAndLocalPostcondition(self.obj425, rootNode)
    self.obj425.postAction( rootNode.CREATE )

    # Connections for obj356 (graphObject_: Obj254) of type rawMaterial
    self.drawConnections(
(self.obj356,self.obj375,[18.896380843299994, 132.41503697948, 855.8762853695881, 88.54868171130781],"true", 2),
(self.obj356,self.obj376,[18.896380843299994, 132.41503697948, 763.0740263667426, 100.71422637447046],"true", 2),
(self.obj356,self.obj377,[18.896380843299994, 132.41503697948, 951.8737484012821, 78.36855687293415],"true", 2) )
    # Connections for obj358 (graphObject_: Obj256) of type rawMaterial
    self.drawConnections(
(self.obj358,self.obj378,[370.456689678, 156.0, 145.63433520144252, 100.29918939499045],"true", 2),
(self.obj358,self.obj379,[370.456689678, 156.0, 238.43659420428813, 88.13364473182781],"true", 2) )
    # Connections for obj360 (graphObject_: Obj258) named A1 R1
    self.drawConnections(
(self.obj360,self.obj420,[49.896380843299994, -113.58496302052001, 860.8286162641775, 148.56223557298716],"true", 2),
(self.obj360,self.obj421,[49.896380843299994, -113.58496302052001, 761.7911535804984, 166.8641450379026],"true", 2) )
    # Connections for obj362 (graphObject_: Obj260) named A1 R2
    self.drawConnections(
(self.obj362,self.obj422,[61.896380843299994, -29.58496302052, 556.0304905340445, 167.16719412058308],"true", 2) )
    # Connections for obj364 (graphObject_: Obj262) named A1 R3
    self.drawConnections(
(self.obj364,self.obj423,[247.8963808433, -71.58496302052001, 1066.9116059668506, 148.22583685027485],"true", 2) )
    # Connections for obj366 (graphObject_: Obj264) named A2 R2
    self.drawConnections(
(self.obj366,self.obj424,[372.456689678, 71.0, 37.09723323787256, 148.28621946137997],"true", 2) )
    # Connections for obj368 (graphObject_: Obj266) named A2 R3
    self.drawConnections(
(self.obj368,self.obj425,[206.45668967799998, 54.0, 243.00895788944365, 148.2222260846105],"true", 2) )
    # Connections for obj381 (graphObject_: Obj284) named G1 OAF
    self.drawConnections(
(self.obj381,self.obj383,[81.50863730422, 293.4406169305, 745.3018403651239, 504.39037222521165],"true", 2) )
    # Connections for obj384 (graphObject_: Obj289) named G2 OAF
    self.drawConnections(
(self.obj384,self.obj386,[193.2410183265, 170.5360232515, 557.000722907756, 484.69177182163276],"true", 2) )
    # Connections for obj387 (graphObject_: Obj294) named G3 OAF
    self.drawConnections(
(self.obj387,self.obj389,[346.0, 265.5, 649.9376994887715, 493.1354916461191],"true", 2) )
    # Connections for obj391 (graphObject_: Obj300) named A1 R1 G1
    self.drawConnections(
(self.obj391,self.obj414,[364.0, 31.0, 856.4148703790486, 321.0744008907871],"true", 2) )
    # Connections for obj395 (graphObject_: Obj305) named A1 R1 G2
    self.drawConnections(
(self.obj395,self.obj415,[492.0, -24.0, 551.0723053399203, 337.9648369008526],"true", 2) )
    # Connections for obj399 (graphObject_: Obj310) named A1 R2 G2
    self.drawConnections(
(self.obj399,self.obj416,[368.0, 190.0, 444.6354046118039, 321.0864991788503],"true", 2) )
    # Connections for obj403 (graphObject_: Obj315) named A1 R3 G3
    self.drawConnections(
(self.obj403,self.obj417,[349.0, -1.0, 858.1148856811054, 338.36874582897747],"true", 2) )
    # Connections for obj407 (graphObject_: Obj320) named A2 R2 G2
    self.drawConnections(
(self.obj407,self.obj418,[521.0, -13.0, 239.2936728170465, 316.15729539650846],"true", 2) )
    # Connections for obj411 (graphObject_: Obj325) named A2 R3 G3
    self.drawConnections(
(self.obj411,self.obj419,[344.0, 7.0, 445.05275157333233, 316.1212874041445],"true", 2) )
    # Connections for obj370 (graphObject_: Obj268) of type metarial
    self.drawConnections(
(self.obj370,self.obj382,[9.017274608440005, 514.881233861, 855.7370864646355, 430.87975820196465],"true", 2) )
    # Connections for obj372 (graphObject_: Obj270) of type metarial
    self.drawConnections(
(self.obj372,self.obj385,[226.48203665300002, 255.07204650300002, 444.3378071117936, 430.49239880919185],"true", 2) )
    # Connections for obj374 (graphObject_: Obj272) of type metarial
    self.drawConnections(
(self.obj374,self.obj388,[562.0, 454.0, 649.9789154407313, 430.39903515061667],"true", 2) )
    # Connections for obj392 (graphObject_: Obj301) of type metarial
    self.drawConnections(
(self.obj392,self.obj393,[230.789190284, 190.039999993, 875.5689603323508, 256.48886227529033],"true", 2) )
    # Connections for obj396 (graphObject_: Obj306) of type metarial
    self.drawConnections(
(self.obj396,self.obj397,[294.78919028400003, 162.539999993, 669.5739058663621, 256.2578407855317],"true", 2) )
    # Connections for obj400 (graphObject_: Obj311) of type metarial
    self.drawConnections(
(self.obj400,self.obj401,[326.19135264600004, 218.1743834515, 463.7839745107611, 256.6099193900902],"true", 2) )
    # Connections for obj404 (graphObject_: Obj316) of type metarial
    self.drawConnections(
(self.obj404,self.obj405,[382.0, 164.5, 1081.6875941517633, 256.26997589714864],"true", 2) )
    # Connections for obj408 (graphObject_: Obj321) of type metarial
    self.drawConnections(
(self.obj408,self.obj409,[416.69135264600004, 160.6743834515, 51.519958643450536, 256.30573728527145],"true", 2) )
    # Connections for obj412 (graphObject_: Obj326) of type metarial
    self.drawConnections(
(self.obj412,self.obj413,[365.5, 124.5, 242.52457799365988, 260.86130884663055],"true", 2) )
    # Connections for obj380 (graphObject_: Obj283) of type product
    self.drawConnections(
 )
    # Connections for obj382 (graphObject_: Obj285) of type fromMaterial
    self.drawConnections(
(self.obj382,self.obj381,[855.7370864646355, 430.87975820196465, 854.6099271385805, 446.51960396933964, 843.50863730422, 461.4406169305],"true", 3) )
    # Connections for obj385 (graphObject_: Obj290) of type fromMaterial
    self.drawConnections(
(self.obj385,self.obj384,[444.3378071117936, 430.4923988091918, 443.2775525301686, 445.8583929963168, 432.2410183265, 460.5360232515],"true", 3) )
    # Connections for obj388 (graphObject_: Obj295) of type fromMaterial
    self.drawConnections(
(self.obj388,self.obj387,[649.9789154407313, 430.39903515061667, 648.9789154407313, 445.77403515061667, 638.0, 460.5],"true", 3) )
    # Connections for obj393 (graphObject_: Obj302) of type fromMaterial
    self.drawConnections(
(self.obj393,self.obj391,[875.5689603323508, 256.48886227529033, 879.6216627613508, 271.9788622770403, 874.0, 290.0],"true", 3) )
    # Connections for obj397 (graphObject_: Obj307) of type fromMaterial
    self.drawConnections(
(self.obj397,self.obj395,[669.573905866362, 256.25784078553164, 673.626608295362, 271.87284078728163, 668.0, 290.0],"true", 3) )
    # Connections for obj401 (graphObject_: Obj312) of type fromMaterial
    self.drawConnections(
(self.obj401,self.obj399,[463.7839745107611, 256.60991939009017, 467.7361363492611, 272.06632352721516, 462.0, 290.0],"true", 3) )
    # Connections for obj405 (graphObject_: Obj317) of type fromMaterial
    self.drawConnections(
(self.obj405,self.obj403,[1081.6875941517633, 256.26997589714864, 1085.6875941517633, 271.89497589714864, 1080.0, 290.0],"true", 3) )
    # Connections for obj409 (graphObject_: Obj322) of type fromMaterial
    self.drawConnections(
(self.obj409,self.obj407,[51.519958643450536, 256.30573728527145, 55.597120481950526, 271.88714142239644, 50.0, 290.0],"true", 3) )
    # Connections for obj413 (graphObject_: Obj327) of type fromMaterial
    self.drawConnections(
(self.obj413,self.obj411,[242.52457799365988, 260.86130884663055, 239.14957799365988, 276.48630884663055, 226.0, 290.0],"true", 3) )
    # Connections for obj383 (graphObject_: Obj287) of type intoProduct
    self.drawConnections(
(self.obj383,self.obj380,[745.3018403651239, 504.39037222521165, 695.4246810390689, 517.5302179925866, 643.0, 521.0],"true", 3) )
    # Connections for obj386 (graphObject_: Obj292) of type intoProduct
    self.drawConnections(
(self.obj386,self.obj380,[557.000722907756, 484.69177182163276, 601.4404683261309, 498.05776600875777, 643.0, 521.0],"true", 3) )
    # Connections for obj389 (graphObject_: Obj297) of type intoProduct
    self.drawConnections(
(self.obj389,self.obj380,[649.9376994887715, 493.1354916461191, 651.4376994887715, 506.5104916461191, 643.0, 521.0],"true", 3) )
    # Connections for obj375 (graphObject_: Obj273) of type fromRaw
    self.drawConnections(
(self.obj375,self.obj360,[855.8762853695881, 88.54868171130781, 854.8762853695881, 104.29868171130781, 843.8963808433, 119.41503697947999],"true", 3) )
    # Connections for obj376 (graphObject_: Obj275) of type fromRaw
    self.drawConnections(
(self.obj376,self.obj362,[763.0740263667426, 100.71422637447044, 718.8240263667426, 118.21422637447044, 670.8963808433, 126.41503697947999],"true", 3) )
    # Connections for obj377 (graphObject_: Obj277) of type fromRaw
    self.drawConnections(
(self.obj377,self.obj364,[951.8737484012821, 78.36855687293415, 1002.3737484012821, 94.11855687293415, 1049.8963808433, 119.41503697947999],"true", 3) )
    # Connections for obj378 (graphObject_: Obj279) of type fromRaw
    self.drawConnections(
(self.obj378,self.obj366,[145.63433520144252, 100.29918939499045, 101.38433520144252, 117.79918939499045, 53.456689677999975, 126.0],"true", 3) )
    # Connections for obj379 (graphObject_: Obj281) of type fromRaw
    self.drawConnections(
(self.obj379,self.obj368,[238.43659420428813, 88.13364473182781, 237.43659420428813, 103.88364473182781, 226.45668967799998, 119.0],"true", 3) )
    # Connections for obj414 (graphObject_: Obj329) of type intoMaterial
    self.drawConnections(
(self.obj414,self.obj370,[856.4148703790487, 321.0744008907871, 858.1691890311587, 333.7947093560371, 850.01727460844, 347.881233861],"true", 3) )
    # Connections for obj415 (graphObject_: Obj331) of type intoMaterial
    self.drawConnections(
(self.obj415,self.obj372,[551.0723053399203, 337.9648369008526, 506.4428145031702, 353.73284852660265, 458.482036653, 360.072046503],"true", 3) )
    # Connections for obj416 (graphObject_: Obj333) of type intoMaterial
    self.drawConnections(
(self.obj416,self.obj372,[444.6354046118039, 321.0864991788503, 446.5059137750539, 333.85451080460035, 438.482036653, 348.072046503],"true", 3) )
    # Connections for obj417 (graphObject_: Obj335) of type intoMaterial
    self.drawConnections(
(self.obj417,self.obj374,[858.1148856811054, 338.3687458289775, 761.8648856811054, 354.1187458289775, 664.0, 360.0],"true", 3) )
    # Connections for obj418 (graphObject_: Obj337) of type intoMaterial
    self.drawConnections(
(self.obj418,self.obj372,[239.2936728170465, 316.15729539650846, 331.6641819802965, 330.6753070222585, 422.482036653, 355.072046503],"true", 3) )
    # Connections for obj419 (graphObject_: Obj339) of type intoMaterial
    self.drawConnections(
(self.obj419,self.obj374,[445.0527515733323, 316.1212874041445, 537.3027515733323, 330.6212874041445, 628.0, 355.0],"true", 3) )
    # Connections for obj420 (graphObject_: Obj341) of type intoMaterial
    self.drawConnections(
(self.obj420,self.obj392,[860.8286162641775, 148.56223557298713, 865.0518186243526, 161.21847632636715, 859.789190284, 177.039999993],"true", 3) )
    # Connections for obj421 (graphObject_: Obj343) of type intoMaterial
    self.drawConnections(
(self.obj421,self.obj396,[761.7911535804984, 166.8641450379026, 719.5143559406735, 182.39538579128262, 673.789190284, 188.539999993],"true", 3) )
    # Connections for obj422 (graphObject_: Obj345) of type intoMaterial
    self.drawConnections(
(self.obj422,self.obj400,[556.0304905340445, 167.16719412058308, 513.8542334847194, 182.8570307385881, 468.19135264600004, 189.1743834515],"true", 3) )
    # Connections for obj423 (graphObject_: Obj347) of type intoMaterial
    self.drawConnections(
(self.obj423,self.obj404,[1066.9116059668506, 148.22583685027485, 1071.1875107560256, 160.74707760540485, 1066.0, 176.5],"true", 3) )
    # Connections for obj424 (graphObject_: Obj349) of type intoMaterial
    self.drawConnections(
(self.obj424,self.obj408,[37.09723323787256, 148.28621946137997, 41.155898979872575, 160.95481532425498, 35.69135264600004, 176.6743834515],"true", 3) )
    # Connections for obj425 (graphObject_: Obj351) of type intoMaterial
    self.drawConnections(
(self.obj425,self.obj412,[243.00895788944365, 148.22222608461047, 247.01978546994366, 160.84722608461047, 241.5, 176.5],"true", 3) )

newfunction = pnsEx3_MDL

loadedMMName = 'pns_META'

atom3version = '0.3'
