"""
__pns_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: sam
Modified: Sat Apr  1 11:15:35 2017
_________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from CD_Class3 import *
from CD_Association3 import *
from graph_CD_Association3 import *
from graph_CD_Class3 import *
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

def pns_MDL(self, rootNode, CD_ClassDiagramsV3RootNode=None):

    # --- Generating attributes code for ASG CD_ClassDiagramsV3 ---
    if( CD_ClassDiagramsV3RootNode ): 
        # name
        CD_ClassDiagramsV3RootNode.name.setValue('pns')

        # author
        CD_ClassDiagramsV3RootNode.author.setValue('NOUARKkharkhachiHoussam')

        # showCardinalities
        CD_ClassDiagramsV3RootNode.showCardinalities.setValue((None, 1))
        CD_ClassDiagramsV3RootNode.showCardinalities.config = 0

        # showAssociationBox
        CD_ClassDiagramsV3RootNode.showAssociationBox.setValue((None, 1))
        CD_ClassDiagramsV3RootNode.showAssociationBox.config = 0

        # description
        CD_ClassDiagramsV3RootNode.description.setValue('\n')
        CD_ClassDiagramsV3RootNode.description.setHeight(15)

        # showAttributes
        CD_ClassDiagramsV3RootNode.showAttributes.setValue((None, 1))
        CD_ClassDiagramsV3RootNode.showAttributes.config = 0

        # showActions
        CD_ClassDiagramsV3RootNode.showActions.setValue((None, 1))
        CD_ClassDiagramsV3RootNode.showActions.config = 0

        # showConditions
        CD_ClassDiagramsV3RootNode.showConditions.setValue((None, 1))
        CD_ClassDiagramsV3RootNode.showConditions.config = 0

        # attributes
        CD_ClassDiagramsV3RootNode.attributes.setActionFlags([ 1, 1, 1, 0])
        lcobj1 =[]
        cobj1=ATOM3Attribute(self.types)
        cobj1.setValue(('name', 'String', None, ('Key', 1), ('Direct Editing', 1)))
        cobj1.initialValue=ATOM3String('', 20)
        cobj1.isDerivedAttribute = False
        lcobj1.append(cobj1)
        cobj1=ATOM3Attribute(self.types)
        cobj1.setValue(('author', 'String', None, ('Key', 0), ('Direct Editing', 1)))
        cobj1.initialValue=ATOM3String('Annonymous', 20)
        cobj1.isDerivedAttribute = False
        lcobj1.append(cobj1)
        cobj1=ATOM3Attribute(self.types)
        cobj1.setValue(('description', 'Text', None, ('Key', 0), ('Direct Editing', 1)))
        cobj1.initialValue=ATOM3Text('\n', 60,15 )
        cobj1.isDerivedAttribute = False
        lcobj1.append(cobj1)
        CD_ClassDiagramsV3RootNode.attributes.setValue(lcobj1)

        # constraints
        CD_ClassDiagramsV3RootNode.constraints.setActionFlags([ 1, 1, 1, 0])
        lcobj1 =[]
        CD_ClassDiagramsV3RootNode.constraints.setValue(lcobj1)
    # --- ASG attributes over ---


    self.obj34=CD_Class3(self)
    self.obj34.isGraphObjectVisual = True

    if(hasattr(self.obj34, '_setHierarchicalLink')):
      self.obj34._setHierarchicalLink(False)

    # QOCA
    self.obj34.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj34.Graphical_Appearance.setValue( ('rawMaterial', self.obj34))

    # name
    self.obj34.name.setValue('rawMaterial')

    # attributes
    self.obj34.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MaxFlow', 'Integer', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Integer(999999)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ReqFlow', 'Integer', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Integer(0)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('price', 'Integer', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Integer(0)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj34.attributes.setValue(lcobj2)

    # Abstract
    self.obj34.Abstract.setValue((None, 0))
    self.obj34.Abstract.config = 0

    # cardinality
    self.obj34.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('fromRaw', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj34.cardinality.setValue(lcobj2)

    # display
    self.obj34.display.setValue('Attributes:\n  - MaxFlow :: Integer\n  - Name :: String\n  - ReqFlow :: Integer\n  - price :: Integer\nMultiplicities:\n  - To fromRaw: 0 to N\n')
    self.obj34.display.setHeight(15)

    # Actions
    self.obj34.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj34.Actions.setValue(lcobj2)

    # Constraints
    self.obj34.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj34.Constraints.setValue(lcobj2)

    self.obj34.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(10.5698439605,0.700062790382,self.obj34)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.85
       new_obj.layConstraints['scale'] = [1.0, 1.0241803278688526]
    else: new_obj = None
    self.obj34.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj34)
    self.globalAndLocalPostcondition(self.obj34, rootNode)
    self.obj34.postAction( rootNode.CREATE )

    self.obj35=CD_Class3(self)
    self.obj35.isGraphObjectVisual = True

    if(hasattr(self.obj35, '_setHierarchicalLink')):
      self.obj35._setHierarchicalLink(False)

    # QOCA
    self.obj35.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj35.Graphical_Appearance.setValue( ('product', self.obj35))

    # name
    self.obj35.name.setValue('product')

    # attributes
    self.obj35.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MaxFlow', 'Integer', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Integer(999999)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ReqFlow', 'Integer', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Integer(0)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('price', 'Integer', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Integer(0)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj35.attributes.setValue(lcobj2)

    # Abstract
    self.obj35.Abstract.setValue((None, 0))
    self.obj35.Abstract.config = 0

    # cardinality
    self.obj35.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('intoProduct', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj35.cardinality.setValue(lcobj2)

    # display
    self.obj35.display.setValue('Attributes:\n  - MaxFlow :: Integer\n  - Name :: String\n  - ReqFlow :: Integer\n  - price :: Integer\nMultiplicities:\n  - From intoProduct: 0 to N\n')
    self.obj35.display.setHeight(15)

    # Actions
    self.obj35.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj35.Actions.setValue(lcobj2)

    # Constraints
    self.obj35.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj35.Constraints.setValue(lcobj2)

    self.obj35.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(480.0,0.0,self.obj35)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.74
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj35.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj35)
    self.globalAndLocalPostcondition(self.obj35, rootNode)
    self.obj35.postAction( rootNode.CREATE )

    self.obj36=CD_Class3(self)
    self.obj36.isGraphObjectVisual = True

    if(hasattr(self.obj36, '_setHierarchicalLink')):
      self.obj36._setHierarchicalLink(False)

    # QOCA
    self.obj36.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj36.Graphical_Appearance.setValue( ('metarial', self.obj36))

    # name
    self.obj36.name.setValue('metarial')

    # attributes
    self.obj36.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MaxFlow', 'Integer', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Integer(999999)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ReqFlow', 'Integer', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Integer(0)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('price', 'Integer', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Integer(0)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj36.attributes.setValue(lcobj2)

    # Abstract
    self.obj36.Abstract.setValue((None, 0))
    self.obj36.Abstract.config = 0

    # cardinality
    self.obj36.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('intoMaterial', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('fromMaterial', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj36.cardinality.setValue(lcobj2)

    # display
    self.obj36.display.setValue('Attributes:\n  - MaxFlow :: Integer\n  - Name :: String\n  - ReqFlow :: Integer\n  - price :: Integer\nMultiplicities:\n  - From intoMaterial: 0 to N\n  - To fromMaterial: 0 to N\n')
    self.obj36.display.setHeight(15)

    # Actions
    self.obj36.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj36.Actions.setValue(lcobj2)

    # Constraints
    self.obj36.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj36.Constraints.setValue(lcobj2)

    self.obj36.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(240.0,400.0,self.obj36)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.85
       new_obj.layConstraints['scale'] = [1.0, 1.1704918032786886]
    else: new_obj = None
    self.obj36.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj36)
    self.globalAndLocalPostcondition(self.obj36, rootNode)
    self.obj36.postAction( rootNode.CREATE )

    self.obj37=CD_Class3(self)
    self.obj37.isGraphObjectVisual = True

    if(hasattr(self.obj37, '_setHierarchicalLink')):
      self.obj37._setHierarchicalLink(False)

    # QOCA
    self.obj37.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj37.Graphical_Appearance.setValue( ('operatingUnit', self.obj37))

    # name
    self.obj37.name.setValue('operatingUnit')

    # attributes
    self.obj37.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('OperCostFix', 'Float', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Float(0.0)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('OperCostProp', 'Float', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Float(0.0)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj37.attributes.setValue(lcobj2)

    # Abstract
    self.obj37.Abstract.setValue((None, 0))
    self.obj37.Abstract.config = 0

    # cardinality
    self.obj37.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('fromRaw', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('intoProduct', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('intoMaterial', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('fromMaterial', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj37.cardinality.setValue(lcobj2)

    # display
    self.obj37.display.setValue('Attributes:\n  - OperCostFix :: Float\n  - OperCostProp :: Float\n  - name :: String\nMultiplicities:\n  - From fromRaw: 0 to N\n  - To intoProduct: 0 to N\n  - To intoMaterial: 0 to N\n  - From fromMaterial: 0 to N\n')
    self.obj37.display.setHeight(15)

    # Actions
    self.obj37.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj37.Actions.setValue(lcobj2)

    # Constraints
    self.obj37.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj37.Constraints.setValue(lcobj2)

    self.obj37.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(240.0,180.0,self.obj37)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.85
       new_obj.layConstraints['scale'] = [1.0, 1.3168032786885246]
    else: new_obj = None
    self.obj37.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj37)
    self.globalAndLocalPostcondition(self.obj37, rootNode)
    self.obj37.postAction( rootNode.CREATE )

    self.obj38=CD_Association3(self)
    self.obj38.isGraphObjectVisual = True

    if(hasattr(self.obj38, '_setHierarchicalLink')):
      self.obj38._setHierarchicalLink(False)

    # QOCA
    self.obj38.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj38.Graphical_Appearance.setValue( ('fromRaw', self.obj38))
    self.obj38.Graphical_Appearance.linkInfo=linkEditor(self,self.obj38.Graphical_Appearance.semObject, "fromRaw")
    self.obj38.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj38.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj38.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj38.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj38.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj38.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj38.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj38.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj38.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('fromRaw_1stLink', self.obj38.Graphical_Appearance.linkInfo.FirstLink))
    self.obj38.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj38.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj38.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj38.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj38.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj38.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj38.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj38.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj38.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj38.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj38.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj38.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('fromRaw_1stSegment', self.obj38.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj38.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj38.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj38.Graphical_Appearance.linkInfo.Center.setValue( ('fromRaw_Center', self.obj38.Graphical_Appearance.linkInfo))
    self.obj38.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj38.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj38.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj38.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj38.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj38.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj38.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj38.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj38.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj38.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj38.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj38.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('fromRaw_2ndSegment', self.obj38.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj38.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj38.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj38.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj38.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj38.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj38.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj38.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj38.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj38.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj38.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('fromRaw_2ndLink', self.obj38.Graphical_Appearance.linkInfo.SecondLink))
    self.obj38.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj38.Graphical_Appearance.semObject
    self.obj38.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj38.Graphical_Appearance.semObject
    self.obj38.Graphical_Appearance.linkInfo.Center.semObject=self.obj38.Graphical_Appearance.semObject
    self.obj38.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj38.Graphical_Appearance.semObject
    self.obj38.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj38.Graphical_Appearance.semObject

    # name
    self.obj38.name.setValue('fromRaw')

    # displaySelect
    self.obj38.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj38.displaySelect.config = 0

    # attributes
    self.obj38.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('rate', 'Float', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Float(0.0)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj38.attributes.setValue(lcobj2)

    # cardinality
    self.obj38.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('rawMaterial', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('operatingUnit', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj38.cardinality.setValue(lcobj2)

    # display
    self.obj38.display.setValue('Attributes:\n  - rate :: Float\nMultiplicities:\n  - From rawMaterial: 0 to N\n  - To operatingUnit: 0 to N\n')
    self.obj38.display.setHeight(15)

    # Actions
    self.obj38.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj38.Actions.setValue(lcobj2)

    # Constraints
    self.obj38.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj38.Constraints.setValue(lcobj2)

    self.obj38.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(95.0,231.0,self.obj38)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.337, 1.185483870967742]
    else: new_obj = None
    self.obj38.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj38)
    self.globalAndLocalPostcondition(self.obj38, rootNode)
    self.obj38.postAction( rootNode.CREATE )

    self.obj39=CD_Association3(self)
    self.obj39.isGraphObjectVisual = True

    if(hasattr(self.obj39, '_setHierarchicalLink')):
      self.obj39._setHierarchicalLink(False)

    # QOCA
    self.obj39.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj39.Graphical_Appearance.setValue( ('intoMaterial', self.obj39))
    self.obj39.Graphical_Appearance.linkInfo=linkEditor(self,self.obj39.Graphical_Appearance.semObject, "intoMaterial")
    self.obj39.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj39.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj39.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj39.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj39.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj39.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj39.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj39.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj39.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('intoMaterial_1stLink', self.obj39.Graphical_Appearance.linkInfo.FirstLink))
    self.obj39.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj39.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj39.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj39.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj39.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj39.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj39.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj39.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj39.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj39.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj39.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj39.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('intoMaterial_1stSegment', self.obj39.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj39.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj39.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj39.Graphical_Appearance.linkInfo.Center.setValue( ('intoMaterial_Center', self.obj39.Graphical_Appearance.linkInfo))
    self.obj39.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj39.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj39.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj39.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj39.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj39.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj39.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj39.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj39.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj39.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj39.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj39.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('intoMaterial_2ndSegment', self.obj39.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj39.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj39.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj39.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj39.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj39.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj39.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj39.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj39.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj39.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj39.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('intoMaterial_2ndLink', self.obj39.Graphical_Appearance.linkInfo.SecondLink))
    self.obj39.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj39.Graphical_Appearance.semObject
    self.obj39.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj39.Graphical_Appearance.semObject
    self.obj39.Graphical_Appearance.linkInfo.Center.semObject=self.obj39.Graphical_Appearance.semObject
    self.obj39.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj39.Graphical_Appearance.semObject
    self.obj39.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj39.Graphical_Appearance.semObject

    # name
    self.obj39.name.setValue('intoMaterial')

    # displaySelect
    self.obj39.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj39.displaySelect.config = 0

    # attributes
    self.obj39.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('rate', 'Float', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Float(0.0)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj39.attributes.setValue(lcobj2)

    # cardinality
    self.obj39.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('operatingUnit', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('metarial', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj39.cardinality.setValue(lcobj2)

    # display
    self.obj39.display.setValue('Attributes:\n  - rate :: Float\nMultiplicities:\n  - From operatingUnit: 0 to N\n  - To metarial: 0 to N\n')
    self.obj39.display.setHeight(15)

    # Actions
    self.obj39.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj39.Actions.setValue(lcobj2)

    # Constraints
    self.obj39.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj39.Constraints.setValue(lcobj2)

    self.obj39.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(103.0,422.0,self.obj39)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.4280000000000002, 1.185483870967742]
    else: new_obj = None
    self.obj39.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj39)
    self.globalAndLocalPostcondition(self.obj39, rootNode)
    self.obj39.postAction( rootNode.CREATE )

    self.obj40=CD_Association3(self)
    self.obj40.isGraphObjectVisual = True

    if(hasattr(self.obj40, '_setHierarchicalLink')):
      self.obj40._setHierarchicalLink(False)

    # QOCA
    self.obj40.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj40.Graphical_Appearance.setValue( ('intoProduct', self.obj40))
    self.obj40.Graphical_Appearance.linkInfo=linkEditor(self,self.obj40.Graphical_Appearance.semObject, "intoProduct")
    self.obj40.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj40.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj40.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj40.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj40.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj40.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj40.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj40.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj40.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('intoProduct_1stLink', self.obj40.Graphical_Appearance.linkInfo.FirstLink))
    self.obj40.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj40.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj40.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj40.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj40.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj40.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj40.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj40.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj40.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj40.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj40.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj40.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('intoProduct_1stSegment', self.obj40.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj40.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj40.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj40.Graphical_Appearance.linkInfo.Center.setValue( ('intoProduct_Center', self.obj40.Graphical_Appearance.linkInfo))
    self.obj40.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj40.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj40.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj40.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj40.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj40.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj40.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj40.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj40.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj40.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj40.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj40.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('intoProduct_2ndSegment', self.obj40.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj40.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj40.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj40.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj40.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj40.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj40.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj40.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj40.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj40.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj40.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('intoProduct_2ndLink', self.obj40.Graphical_Appearance.linkInfo.SecondLink))
    self.obj40.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj40.Graphical_Appearance.semObject
    self.obj40.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj40.Graphical_Appearance.semObject
    self.obj40.Graphical_Appearance.linkInfo.Center.semObject=self.obj40.Graphical_Appearance.semObject
    self.obj40.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj40.Graphical_Appearance.semObject
    self.obj40.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj40.Graphical_Appearance.semObject

    # name
    self.obj40.name.setValue('intoProduct')

    # displaySelect
    self.obj40.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj40.displaySelect.config = 0

    # attributes
    self.obj40.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('rate', 'Float', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Float(0.0)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj40.attributes.setValue(lcobj2)

    # cardinality
    self.obj40.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('operatingUnit', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('product', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj40.cardinality.setValue(lcobj2)

    # display
    self.obj40.display.setValue('Attributes:\n  - rate :: Float\nMultiplicities:\n  - From operatingUnit: 0 to N\n  - To product: 0 to N\n')
    self.obj40.display.setHeight(15)

    # Actions
    self.obj40.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj40.Actions.setValue(lcobj2)

    # Constraints
    self.obj40.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj40.Constraints.setValue(lcobj2)

    self.obj40.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(577.0,233.0,self.obj40)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.4280000000000002, 1.185483870967742]
    else: new_obj = None
    self.obj40.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj40)
    self.globalAndLocalPostcondition(self.obj40, rootNode)
    self.obj40.postAction( rootNode.CREATE )

    self.obj41=CD_Association3(self)
    self.obj41.isGraphObjectVisual = True

    if(hasattr(self.obj41, '_setHierarchicalLink')):
      self.obj41._setHierarchicalLink(False)

    # QOCA
    self.obj41.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj41.Graphical_Appearance.setValue( ('fromMaterial', self.obj41))
    self.obj41.Graphical_Appearance.linkInfo=linkEditor(self,self.obj41.Graphical_Appearance.semObject, "fromMaterial")
    self.obj41.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj41.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj41.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj41.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj41.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj41.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj41.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj41.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj41.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('fromMaterial_1stLink', self.obj41.Graphical_Appearance.linkInfo.FirstLink))
    self.obj41.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj41.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj41.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj41.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj41.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj41.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj41.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj41.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj41.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj41.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj41.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj41.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('fromMaterial_1stSegment', self.obj41.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj41.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj41.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj41.Graphical_Appearance.linkInfo.Center.setValue( ('fromMaterial_Center', self.obj41.Graphical_Appearance.linkInfo))
    self.obj41.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj41.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj41.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj41.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj41.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj41.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj41.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj41.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj41.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj41.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj41.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj41.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('fromMaterial_2ndSegment', self.obj41.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj41.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj41.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj41.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj41.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj41.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj41.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj41.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj41.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj41.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj41.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('fromMaterial_2ndLink', self.obj41.Graphical_Appearance.linkInfo.SecondLink))
    self.obj41.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj41.Graphical_Appearance.semObject
    self.obj41.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj41.Graphical_Appearance.semObject
    self.obj41.Graphical_Appearance.linkInfo.Center.semObject=self.obj41.Graphical_Appearance.semObject
    self.obj41.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj41.Graphical_Appearance.semObject
    self.obj41.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj41.Graphical_Appearance.semObject

    # name
    self.obj41.name.setValue('fromMaterial')

    # displaySelect
    self.obj41.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj41.displaySelect.config = 0

    # attributes
    self.obj41.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('rate', 'Float', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Float(0.0)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj41.attributes.setValue(lcobj2)

    # cardinality
    self.obj41.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('metarial', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('operatingUnit', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj41.cardinality.setValue(lcobj2)

    # display
    self.obj41.display.setValue('Attributes:\n  - rate :: Float\nMultiplicities:\n  - From metarial: 0 to N\n  - To operatingUnit: 0 to N\n')
    self.obj41.display.setHeight(15)

    # Actions
    self.obj41.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj41.Actions.setValue(lcobj2)

    # Constraints
    self.obj41.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj41.Constraints.setValue(lcobj2)

    self.obj41.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(548.0,405.0,self.obj41)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.302, 1.185483870967742]
    else: new_obj = None
    self.obj41.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj41)
    self.globalAndLocalPostcondition(self.obj41, rootNode)
    self.obj41.postAction( rootNode.CREATE )

    # Connections for obj34 (graphObject_: Obj12) named rawMaterial
    self.drawConnections(
(self.obj34,self.obj38,[86.13968792099999, 141.40012558076398, 95.0, 231.0],"true", 2) )
    # Connections for obj35 (graphObject_: Obj13) named product
    self.drawConnections(
 )
    # Connections for obj36 (graphObject_: Obj14) named metarial
    self.drawConnections(
(self.obj36,self.obj41,[431.0, 491.327868852459, 569.0, 500.0, 548.0, 405.0],"true", 3) )
    # Connections for obj37 (graphObject_: Obj15) named operatingUnit
    self.drawConnections(
(self.obj37,self.obj40,[431.0, 233.31967213114754, 577.0, 233.0],"true", 2),
(self.obj37,self.obj39,[241.0, 338.6639344262295, 142.0, 342.0, 103.0, 422.0],"true", 3) )
    # Connections for obj38 (graphObject_: Obj16) named fromRaw
    self.drawConnections(
(self.obj38,self.obj37,[95.0, 231.0, 241.0, 233.31967213114754],"true", 2) )
    # Connections for obj39 (graphObject_: Obj18) named intoMaterial
    self.drawConnections(
(self.obj39,self.obj36,[103.0, 422.0, 110.0, 533.0, 241.0, 520.5901639344262],"true", 3) )
    # Connections for obj40 (graphObject_: Obj20) named intoProduct
    self.drawConnections(
(self.obj40,self.obj35,[577.0, 233.0, 596.0, 141.0],"true", 2) )
    # Connections for obj41 (graphObject_: Obj22) named fromMaterial
    self.drawConnections(
(self.obj41,self.obj37,[548.0, 405.0, 542.0, 316.0, 431.0, 305.7438524590164],"true", 3) )

newfunction = pns_MDL

loadedMMName = 'CD_ClassDiagramsV3_META'

atom3version = '0.3'
