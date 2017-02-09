"""
__pns2_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: sam
Modified: Sun Jan 29 10:08:21 2017
__________________________________________________________________
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

def pns2_MDL(self, rootNode, CD_ClassDiagramsV3RootNode=None):

    # --- Generating attributes code for ASG CD_ClassDiagramsV3 ---
    if( CD_ClassDiagramsV3RootNode ): 
        # name
        CD_ClassDiagramsV3RootNode.name.setValue('pns2')

        # author
        CD_ClassDiagramsV3RootNode.author.setValue('houssam nouar')

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


    self.obj84=CD_Class3(self)
    self.obj84.isGraphObjectVisual = True

    if(hasattr(self.obj84, '_setHierarchicalLink')):
      self.obj84._setHierarchicalLink(False)

    # QOCA
    self.obj84.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj84.Graphical_Appearance.setValue( ('rawMaterial', self.obj84))

    # name
    self.obj84.name.setValue('rawMaterial')

    # attributes
    self.obj84.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj84.attributes.setValue(lcobj2)

    # Abstract
    self.obj84.Abstract.setValue((None, 0))
    self.obj84.Abstract.config = 0

    # cardinality
    self.obj84.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('fromRaw', (('Source', 'Destination'), 0), '1', 'N'))
    lcobj2.append(cobj2)
    self.obj84.cardinality.setValue(lcobj2)

    # display
    self.obj84.display.setValue('Attributes:\n  - Name :: String\nMultiplicities:\n  - To fromRaw: 1 to N\n')
    self.obj84.display.setHeight(15)

    # Actions
    self.obj84.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj84.Actions.setValue(lcobj2)

    # Constraints
    self.obj84.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj84.Constraints.setValue(lcobj2)

    self.obj84.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(10.5698439605,0.700062790382,self.obj84)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.85
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj84.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj84)
    self.globalAndLocalPostcondition(self.obj84, rootNode)
    self.obj84.postAction( rootNode.CREATE )

    self.obj85=CD_Class3(self)
    self.obj85.isGraphObjectVisual = True

    if(hasattr(self.obj85, '_setHierarchicalLink')):
      self.obj85._setHierarchicalLink(False)

    # QOCA
    self.obj85.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj85.Graphical_Appearance.setValue( ('product', self.obj85))

    # name
    self.obj85.name.setValue('product')

    # attributes
    self.obj85.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj85.attributes.setValue(lcobj2)

    # Abstract
    self.obj85.Abstract.setValue((None, 0))
    self.obj85.Abstract.config = 0

    # cardinality
    self.obj85.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('intoProduct', (('Source', 'Destination'), 1), '1', 'N'))
    lcobj2.append(cobj2)
    self.obj85.cardinality.setValue(lcobj2)

    # display
    self.obj85.display.setValue('Attributes:\n  - Name :: String\nMultiplicities:\n  - From intoProduct: 1 to N\n')
    self.obj85.display.setHeight(15)

    # Actions
    self.obj85.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj85.Actions.setValue(lcobj2)

    # Constraints
    self.obj85.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj85.Constraints.setValue(lcobj2)

    self.obj85.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(480.0,0.0,self.obj85)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.74
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj85.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj85)
    self.globalAndLocalPostcondition(self.obj85, rootNode)
    self.obj85.postAction( rootNode.CREATE )

    self.obj86=CD_Class3(self)
    self.obj86.isGraphObjectVisual = True

    if(hasattr(self.obj86, '_setHierarchicalLink')):
      self.obj86._setHierarchicalLink(False)

    # QOCA
    self.obj86.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj86.Graphical_Appearance.setValue( ('metarial', self.obj86))

    # name
    self.obj86.name.setValue('metarial')

    # attributes
    self.obj86.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj86.attributes.setValue(lcobj2)

    # Abstract
    self.obj86.Abstract.setValue((None, 0))
    self.obj86.Abstract.config = 0

    # cardinality
    self.obj86.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('intoMaterial', (('Source', 'Destination'), 1), '1', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('fromMaterial', (('Source', 'Destination'), 0), '1', 'N'))
    lcobj2.append(cobj2)
    self.obj86.cardinality.setValue(lcobj2)

    # display
    self.obj86.display.setValue('Attributes:\n  - Name :: String\nMultiplicities:\n  - From intoMaterial: 1 to N\n  - To fromMaterial: 1 to N\n')
    self.obj86.display.setHeight(15)

    # Actions
    self.obj86.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj86.Actions.setValue(lcobj2)

    # Constraints
    self.obj86.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj86.Constraints.setValue(lcobj2)

    self.obj86.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(240.0,400.0,self.obj86)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.85
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj86.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj86)
    self.globalAndLocalPostcondition(self.obj86, rootNode)
    self.obj86.postAction( rootNode.CREATE )

    self.obj87=CD_Class3(self)
    self.obj87.isGraphObjectVisual = True

    if(hasattr(self.obj87, '_setHierarchicalLink')):
      self.obj87._setHierarchicalLink(False)

    # QOCA
    self.obj87.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj87.Graphical_Appearance.setValue( ('operatingUnit', self.obj87))

    # name
    self.obj87.name.setValue('operatingUnit')

    # attributes
    self.obj87.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj87.attributes.setValue(lcobj2)

    # Abstract
    self.obj87.Abstract.setValue((None, 0))
    self.obj87.Abstract.config = 0

    # cardinality
    self.obj87.cardinality.setActionFlags([ 0, 1, 0, 0])
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
    self.obj87.cardinality.setValue(lcobj2)

    # display
    self.obj87.display.setValue('Multiplicities:\n  - From fromRaw: 0 to N\n  - To intoProduct: 0 to N\n  - To intoMaterial: 0 to N\n  - From fromMaterial: 0 to N\n')
    self.obj87.display.setHeight(15)

    # Actions
    self.obj87.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj87.Actions.setValue(lcobj2)

    # Constraints
    self.obj87.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj87.Constraints.setValue(lcobj2)

    self.obj87.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(240.0,180.0,self.obj87)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.85
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj87.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj87)
    self.globalAndLocalPostcondition(self.obj87, rootNode)
    self.obj87.postAction( rootNode.CREATE )

    self.obj88=CD_Association3(self)
    self.obj88.isGraphObjectVisual = True

    if(hasattr(self.obj88, '_setHierarchicalLink')):
      self.obj88._setHierarchicalLink(False)

    # QOCA
    self.obj88.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj88.Graphical_Appearance.setValue( ('fromRaw', self.obj88))
    self.obj88.Graphical_Appearance.linkInfo=linkEditor(self,self.obj88.Graphical_Appearance.semObject, "fromRaw")
    self.obj88.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj88.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj88.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj88.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj88.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj88.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj88.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj88.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj88.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('fromRaw_1stLink', self.obj88.Graphical_Appearance.linkInfo.FirstLink))
    self.obj88.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj88.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj88.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj88.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj88.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj88.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj88.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj88.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj88.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj88.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj88.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj88.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('fromRaw_1stSegment', self.obj88.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj88.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj88.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj88.Graphical_Appearance.linkInfo.Center.setValue( ('fromRaw_Center', self.obj88.Graphical_Appearance.linkInfo))
    self.obj88.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj88.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj88.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj88.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj88.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj88.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj88.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj88.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj88.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj88.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj88.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj88.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('fromRaw_2ndSegment', self.obj88.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj88.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj88.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj88.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj88.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj88.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj88.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj88.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj88.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj88.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj88.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('fromRaw_2ndLink', self.obj88.Graphical_Appearance.linkInfo.SecondLink))
    self.obj88.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj88.Graphical_Appearance.semObject
    self.obj88.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj88.Graphical_Appearance.semObject
    self.obj88.Graphical_Appearance.linkInfo.Center.semObject=self.obj88.Graphical_Appearance.semObject
    self.obj88.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj88.Graphical_Appearance.semObject
    self.obj88.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj88.Graphical_Appearance.semObject

    # name
    self.obj88.name.setValue('fromRaw')

    # displaySelect
    self.obj88.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj88.displaySelect.config = 0

    # attributes
    self.obj88.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('rate', 'Float', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Float(0.0)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj88.attributes.setValue(lcobj2)

    # cardinality
    self.obj88.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('rawMaterial', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('operatingUnit', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj88.cardinality.setValue(lcobj2)

    # display
    self.obj88.display.setValue('Attributes:\n  - rate :: Float\nMultiplicities:\n  - From rawMaterial: 0 to N\n  - To operatingUnit: 0 to N\n')
    self.obj88.display.setHeight(15)

    # Actions
    self.obj88.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj88.Actions.setValue(lcobj2)

    # Constraints
    self.obj88.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj88.Constraints.setValue(lcobj2)

    self.obj88.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(95.0,231.0,self.obj88)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.337, 1.185483870967742]
    else: new_obj = None
    self.obj88.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj88)
    self.globalAndLocalPostcondition(self.obj88, rootNode)
    self.obj88.postAction( rootNode.CREATE )

    self.obj89=CD_Association3(self)
    self.obj89.isGraphObjectVisual = True

    if(hasattr(self.obj89, '_setHierarchicalLink')):
      self.obj89._setHierarchicalLink(False)

    # QOCA
    self.obj89.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj89.Graphical_Appearance.setValue( ('intoMaterial', self.obj89))
    self.obj89.Graphical_Appearance.linkInfo=linkEditor(self,self.obj89.Graphical_Appearance.semObject, "intoMaterial")
    self.obj89.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj89.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj89.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj89.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj89.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj89.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj89.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj89.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj89.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('intoMaterial_1stLink', self.obj89.Graphical_Appearance.linkInfo.FirstLink))
    self.obj89.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj89.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj89.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj89.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj89.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj89.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj89.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj89.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj89.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj89.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj89.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj89.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('intoMaterial_1stSegment', self.obj89.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj89.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj89.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj89.Graphical_Appearance.linkInfo.Center.setValue( ('intoMaterial_Center', self.obj89.Graphical_Appearance.linkInfo))
    self.obj89.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj89.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj89.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj89.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj89.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj89.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj89.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj89.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj89.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj89.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj89.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj89.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('intoMaterial_2ndSegment', self.obj89.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj89.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj89.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj89.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj89.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj89.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj89.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj89.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj89.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj89.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj89.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('intoMaterial_2ndLink', self.obj89.Graphical_Appearance.linkInfo.SecondLink))
    self.obj89.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj89.Graphical_Appearance.semObject
    self.obj89.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj89.Graphical_Appearance.semObject
    self.obj89.Graphical_Appearance.linkInfo.Center.semObject=self.obj89.Graphical_Appearance.semObject
    self.obj89.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj89.Graphical_Appearance.semObject
    self.obj89.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj89.Graphical_Appearance.semObject

    # name
    self.obj89.name.setValue('intoMaterial')

    # displaySelect
    self.obj89.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj89.displaySelect.config = 0

    # attributes
    self.obj89.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('rate', 'Float', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Float(0.0)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj89.attributes.setValue(lcobj2)

    # cardinality
    self.obj89.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('operatingUnit', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('metarial', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj89.cardinality.setValue(lcobj2)

    # display
    self.obj89.display.setValue('Attributes:\n  - rate :: Float\nMultiplicities:\n  - From operatingUnit: 0 to N\n  - To metarial: 0 to N\n')
    self.obj89.display.setHeight(15)

    # Actions
    self.obj89.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj89.Actions.setValue(lcobj2)

    # Constraints
    self.obj89.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj89.Constraints.setValue(lcobj2)

    self.obj89.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(103.0,422.0,self.obj89)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.4280000000000002, 1.185483870967742]
    else: new_obj = None
    self.obj89.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj89)
    self.globalAndLocalPostcondition(self.obj89, rootNode)
    self.obj89.postAction( rootNode.CREATE )

    self.obj90=CD_Association3(self)
    self.obj90.isGraphObjectVisual = True

    if(hasattr(self.obj90, '_setHierarchicalLink')):
      self.obj90._setHierarchicalLink(False)

    # QOCA
    self.obj90.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj90.Graphical_Appearance.setValue( ('intoProduct', self.obj90))
    self.obj90.Graphical_Appearance.linkInfo=linkEditor(self,self.obj90.Graphical_Appearance.semObject, "intoProduct")
    self.obj90.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj90.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj90.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj90.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj90.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj90.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj90.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj90.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj90.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('intoProduct_1stLink', self.obj90.Graphical_Appearance.linkInfo.FirstLink))
    self.obj90.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj90.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj90.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj90.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj90.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj90.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj90.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj90.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj90.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj90.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj90.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj90.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('intoProduct_1stSegment', self.obj90.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj90.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj90.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj90.Graphical_Appearance.linkInfo.Center.setValue( ('intoProduct_Center', self.obj90.Graphical_Appearance.linkInfo))
    self.obj90.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj90.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj90.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj90.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj90.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj90.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj90.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj90.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj90.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj90.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj90.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj90.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('intoProduct_2ndSegment', self.obj90.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj90.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj90.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj90.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj90.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj90.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj90.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj90.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj90.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj90.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj90.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('intoProduct_2ndLink', self.obj90.Graphical_Appearance.linkInfo.SecondLink))
    self.obj90.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj90.Graphical_Appearance.semObject
    self.obj90.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj90.Graphical_Appearance.semObject
    self.obj90.Graphical_Appearance.linkInfo.Center.semObject=self.obj90.Graphical_Appearance.semObject
    self.obj90.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj90.Graphical_Appearance.semObject
    self.obj90.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj90.Graphical_Appearance.semObject

    # name
    self.obj90.name.setValue('intoProduct')

    # displaySelect
    self.obj90.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj90.displaySelect.config = 0

    # attributes
    self.obj90.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('rate', 'Float', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Float(0.0)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj90.attributes.setValue(lcobj2)

    # cardinality
    self.obj90.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('operatingUnit', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('product', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj90.cardinality.setValue(lcobj2)

    # display
    self.obj90.display.setValue('Attributes:\n  - rate :: Float\nMultiplicities:\n  - From operatingUnit: 0 to N\n  - To product: 0 to N\n')
    self.obj90.display.setHeight(15)

    # Actions
    self.obj90.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj90.Actions.setValue(lcobj2)

    # Constraints
    self.obj90.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj90.Constraints.setValue(lcobj2)

    self.obj90.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(577.0,233.0,self.obj90)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.4280000000000002, 1.185483870967742]
    else: new_obj = None
    self.obj90.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj90)
    self.globalAndLocalPostcondition(self.obj90, rootNode)
    self.obj90.postAction( rootNode.CREATE )

    self.obj91=CD_Association3(self)
    self.obj91.isGraphObjectVisual = True

    if(hasattr(self.obj91, '_setHierarchicalLink')):
      self.obj91._setHierarchicalLink(False)

    # QOCA
    self.obj91.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj91.Graphical_Appearance.setValue( ('fromMaterial', self.obj91))
    self.obj91.Graphical_Appearance.linkInfo=linkEditor(self,self.obj91.Graphical_Appearance.semObject, "fromMaterial")
    self.obj91.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj91.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj91.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj91.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj91.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj91.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj91.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj91.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj91.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('fromMaterial_1stLink', self.obj91.Graphical_Appearance.linkInfo.FirstLink))
    self.obj91.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj91.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj91.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj91.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj91.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj91.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj91.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj91.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj91.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj91.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj91.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj91.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('fromMaterial_1stSegment', self.obj91.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj91.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj91.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj91.Graphical_Appearance.linkInfo.Center.setValue( ('fromMaterial_Center', self.obj91.Graphical_Appearance.linkInfo))
    self.obj91.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj91.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj91.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj91.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj91.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj91.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj91.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj91.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj91.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj91.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj91.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj91.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('fromMaterial_2ndSegment', self.obj91.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj91.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj91.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj91.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj91.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj91.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj91.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj91.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj91.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj91.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj91.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('fromMaterial_2ndLink', self.obj91.Graphical_Appearance.linkInfo.SecondLink))
    self.obj91.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj91.Graphical_Appearance.semObject
    self.obj91.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj91.Graphical_Appearance.semObject
    self.obj91.Graphical_Appearance.linkInfo.Center.semObject=self.obj91.Graphical_Appearance.semObject
    self.obj91.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj91.Graphical_Appearance.semObject
    self.obj91.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj91.Graphical_Appearance.semObject

    # name
    self.obj91.name.setValue('fromMaterial')

    # displaySelect
    self.obj91.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj91.displaySelect.config = 0

    # attributes
    self.obj91.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('rate', 'Float', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Float(0.0)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj91.attributes.setValue(lcobj2)

    # cardinality
    self.obj91.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('metarial', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('operatingUnit', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj91.cardinality.setValue(lcobj2)

    # display
    self.obj91.display.setValue('Attributes:\n  - rate :: Float\nMultiplicities:\n  - From metarial: 0 to N\n  - To operatingUnit: 0 to N\n')
    self.obj91.display.setHeight(15)

    # Actions
    self.obj91.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj91.Actions.setValue(lcobj2)

    # Constraints
    self.obj91.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj91.Constraints.setValue(lcobj2)

    self.obj91.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(548.0,405.0,self.obj91)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.302, 1.185483870967742]
    else: new_obj = None
    self.obj91.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj91)
    self.globalAndLocalPostcondition(self.obj91, rootNode)
    self.obj91.postAction( rootNode.CREATE )

    # Connections for obj84 (graphObject_: Obj25) named rawMaterial
    self.drawConnections(
(self.obj84,self.obj88,[86.13968792099999, 141.40012558076398, 95.0, 231.0],"true", 2) )
    # Connections for obj85 (graphObject_: Obj26) named product
    self.drawConnections(
 )
    # Connections for obj86 (graphObject_: Obj27) named metarial
    self.drawConnections(
(self.obj86,self.obj91,[431.0, 496.0, 569.0, 500.0, 548.0, 405.0],"true", 3) )
    # Connections for obj87 (graphObject_: Obj28) named operatingUnit
    self.drawConnections(
(self.obj87,self.obj90,[431.0, 221.0, 577.0, 233.0],"true", 2),
(self.obj87,self.obj89,[241.0, 301.0, 142.0, 342.0, 103.0, 422.0],"true", 3) )
    # Connections for obj88 (graphObject_: Obj29) named fromRaw
    self.drawConnections(
(self.obj88,self.obj87,[95.0, 231.0, 241.0, 221.0],"true", 2) )
    # Connections for obj89 (graphObject_: Obj31) named intoMaterial
    self.drawConnections(
(self.obj89,self.obj86,[103.0, 422.0, 110.0, 533.0, 241.0, 521.0],"true", 3) )
    # Connections for obj90 (graphObject_: Obj33) named intoProduct
    self.drawConnections(
(self.obj90,self.obj85,[577.0, 233.0, 596.0, 141.0],"true", 2) )
    # Connections for obj91 (graphObject_: Obj35) named fromMaterial
    self.drawConnections(
(self.obj91,self.obj87,[548.0, 405.0, 542.0, 316.0, 431.0, 301.0],"true", 3) )

newfunction = pns2_MDL

loadedMMName = 'CD_ClassDiagramsV3_META'

atom3version = '0.3'
