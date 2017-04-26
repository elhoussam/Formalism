"""
__pns_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: USER
Modified: Wed Apr 26 11:30:59 2017
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


    self.obj49=CD_Class3(self)
    self.obj49.isGraphObjectVisual = True

    if(hasattr(self.obj49, '_setHierarchicalLink')):
      self.obj49._setHierarchicalLink(False)

    # QOCA
    self.obj49.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj49.Graphical_Appearance.setValue( ('rawMaterial', self.obj49))

    # name
    self.obj49.name.setValue('rawMaterial')

    # attributes
    self.obj49.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj49.attributes.setValue(lcobj2)

    # Abstract
    self.obj49.Abstract.setValue((None, 0))
    self.obj49.Abstract.config = 0

    # cardinality
    self.obj49.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('fromRaw', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj49.cardinality.setValue(lcobj2)

    # display
    self.obj49.display.setValue('Attributes:\n  - MaxFlow :: Integer\n  - Name :: String\n  - ReqFlow :: Integer\n  - price :: Integer\nMultiplicities:\n  - To fromRaw: 0 to N\n')
    self.obj49.display.setHeight(15)

    # Actions
    self.obj49.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj49.Actions.setValue(lcobj2)

    # Constraints
    self.obj49.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj49.Constraints.setValue(lcobj2)

    self.obj49.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(10.5698439605,0.700062790382,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.85
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj49.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj49)
    self.globalAndLocalPostcondition(self.obj49, rootNode)
    self.obj49.postAction( rootNode.CREATE )

    self.obj50=CD_Class3(self)
    self.obj50.isGraphObjectVisual = True

    if(hasattr(self.obj50, '_setHierarchicalLink')):
      self.obj50._setHierarchicalLink(False)

    # QOCA
    self.obj50.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj50.Graphical_Appearance.setValue( ('product', self.obj50))

    # name
    self.obj50.name.setValue('product')

    # attributes
    self.obj50.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj50.attributes.setValue(lcobj2)

    # Abstract
    self.obj50.Abstract.setValue((None, 0))
    self.obj50.Abstract.config = 0

    # cardinality
    self.obj50.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('intoProduct', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj50.cardinality.setValue(lcobj2)

    # display
    self.obj50.display.setValue('Attributes:\n  - MaxFlow :: Integer\n  - Name :: String\n  - ReqFlow :: Integer\n  - price :: Integer\nMultiplicities:\n  - From intoProduct: 0 to N\n')
    self.obj50.display.setHeight(15)

    # Actions
    self.obj50.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj50.Actions.setValue(lcobj2)

    # Constraints
    self.obj50.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj50.Constraints.setValue(lcobj2)

    self.obj50.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(480.0,0.0,self.obj50)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.74
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj50.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj50)
    self.globalAndLocalPostcondition(self.obj50, rootNode)
    self.obj50.postAction( rootNode.CREATE )

    self.obj51=CD_Class3(self)
    self.obj51.isGraphObjectVisual = True

    if(hasattr(self.obj51, '_setHierarchicalLink')):
      self.obj51._setHierarchicalLink(False)

    # QOCA
    self.obj51.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj51.Graphical_Appearance.setValue( ('metarial', self.obj51))

    # name
    self.obj51.name.setValue('metarial')

    # attributes
    self.obj51.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj51.attributes.setValue(lcobj2)

    # Abstract
    self.obj51.Abstract.setValue((None, 0))
    self.obj51.Abstract.config = 0

    # cardinality
    self.obj51.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('intoMaterial', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('fromMaterial', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj51.cardinality.setValue(lcobj2)

    # display
    self.obj51.display.setValue('Attributes:\n  - MaxFlow :: Integer\n  - Name :: String\n  - ReqFlow :: Integer\n  - price :: Integer\nMultiplicities:\n  - From intoMaterial: 0 to N\n  - To fromMaterial: 0 to N\n')
    self.obj51.display.setHeight(15)

    # Actions
    self.obj51.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj51.Actions.setValue(lcobj2)

    # Constraints
    self.obj51.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj51.Constraints.setValue(lcobj2)

    self.obj51.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(240.0,400.0,self.obj51)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.85
       new_obj.layConstraints['scale'] = [1.0, 1.1016393442622952]
    else: new_obj = None
    self.obj51.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj51)
    self.globalAndLocalPostcondition(self.obj51, rootNode)
    self.obj51.postAction( rootNode.CREATE )

    self.obj52=CD_Class3(self)
    self.obj52.isGraphObjectVisual = True

    if(hasattr(self.obj52, '_setHierarchicalLink')):
      self.obj52._setHierarchicalLink(False)

    # QOCA
    self.obj52.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj52.Graphical_Appearance.setValue( ('operatingUnit', self.obj52))

    # name
    self.obj52.name.setValue('operatingUnit')

    # attributes
    self.obj52.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj52.attributes.setValue(lcobj2)

    # Abstract
    self.obj52.Abstract.setValue((None, 0))
    self.obj52.Abstract.config = 0

    # cardinality
    self.obj52.cardinality.setActionFlags([ 0, 1, 0, 0])
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
    self.obj52.cardinality.setValue(lcobj2)

    # display
    self.obj52.display.setValue('Attributes:\n  - OperCostFix :: Float\n  - OperCostProp :: Float\n  - name :: String\nMultiplicities:\n  - From fromRaw: 0 to N\n  - To intoProduct: 0 to N\n  - To intoMaterial: 0 to N\n  - From fromMaterial: 0 to N\n')
    self.obj52.display.setHeight(15)

    # Actions
    self.obj52.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj52.Actions.setValue(lcobj2)

    # Constraints
    self.obj52.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj52.Constraints.setValue(lcobj2)

    self.obj52.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(240.0,180.0,self.obj52)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.85
       new_obj.layConstraints['scale'] = [1.0, 1.239344262295082]
    else: new_obj = None
    self.obj52.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52)
    self.globalAndLocalPostcondition(self.obj52, rootNode)
    self.obj52.postAction( rootNode.CREATE )

    self.obj53=CD_Association3(self)
    self.obj53.isGraphObjectVisual = True

    if(hasattr(self.obj53, '_setHierarchicalLink')):
      self.obj53._setHierarchicalLink(False)

    # QOCA
    self.obj53.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj53.Graphical_Appearance.setValue( ('fromRaw', self.obj53))
    self.obj53.Graphical_Appearance.linkInfo=linkEditor(self,self.obj53.Graphical_Appearance.semObject, "fromRaw")
    self.obj53.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj53.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj53.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj53.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj53.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj53.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj53.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj53.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj53.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('fromRaw_1stLink', self.obj53.Graphical_Appearance.linkInfo.FirstLink))
    self.obj53.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj53.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj53.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj53.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj53.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj53.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj53.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj53.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj53.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj53.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj53.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj53.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('fromRaw_1stSegment', self.obj53.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj53.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj53.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj53.Graphical_Appearance.linkInfo.Center.setValue( ('fromRaw_Center', self.obj53.Graphical_Appearance.linkInfo))
    self.obj53.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj53.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj53.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj53.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj53.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj53.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj53.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj53.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj53.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj53.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj53.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj53.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('fromRaw_2ndSegment', self.obj53.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj53.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj53.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj53.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj53.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj53.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj53.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj53.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj53.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj53.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj53.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('fromRaw_2ndLink', self.obj53.Graphical_Appearance.linkInfo.SecondLink))
    self.obj53.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj53.Graphical_Appearance.semObject
    self.obj53.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj53.Graphical_Appearance.semObject
    self.obj53.Graphical_Appearance.linkInfo.Center.semObject=self.obj53.Graphical_Appearance.semObject
    self.obj53.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj53.Graphical_Appearance.semObject
    self.obj53.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj53.Graphical_Appearance.semObject

    # name
    self.obj53.name.setValue('fromRaw')

    # displaySelect
    self.obj53.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj53.displaySelect.config = 0

    # attributes
    self.obj53.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('rate', 'Float', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Float(0.0)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj53.attributes.setValue(lcobj2)

    # cardinality
    self.obj53.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('rawMaterial', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('operatingUnit', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj53.cardinality.setValue(lcobj2)

    # display
    self.obj53.display.setValue('Attributes:\n  - rate :: Float\nMultiplicities:\n  - From rawMaterial: 0 to N\n  - To operatingUnit: 0 to N\n')
    self.obj53.display.setHeight(15)

    # Actions
    self.obj53.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj53.Actions.setValue(lcobj2)

    # Constraints
    self.obj53.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj53.Constraints.setValue(lcobj2)

    self.obj53.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(95.0,231.0,self.obj53)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.316, 1.0161290322580647]
    else: new_obj = None
    self.obj53.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj53)
    self.globalAndLocalPostcondition(self.obj53, rootNode)
    self.obj53.postAction( rootNode.CREATE )

    self.obj54=CD_Association3(self)
    self.obj54.isGraphObjectVisual = True

    if(hasattr(self.obj54, '_setHierarchicalLink')):
      self.obj54._setHierarchicalLink(False)

    # QOCA
    self.obj54.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj54.Graphical_Appearance.setValue( ('intoMaterial', self.obj54))
    self.obj54.Graphical_Appearance.linkInfo=linkEditor(self,self.obj54.Graphical_Appearance.semObject, "intoMaterial")
    self.obj54.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj54.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj54.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj54.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj54.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj54.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj54.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj54.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj54.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('intoMaterial_1stLink', self.obj54.Graphical_Appearance.linkInfo.FirstLink))
    self.obj54.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj54.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj54.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj54.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj54.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj54.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj54.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj54.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj54.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj54.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj54.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj54.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('intoMaterial_1stSegment', self.obj54.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj54.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj54.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj54.Graphical_Appearance.linkInfo.Center.setValue( ('intoMaterial_Center', self.obj54.Graphical_Appearance.linkInfo))
    self.obj54.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj54.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj54.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj54.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj54.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj54.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj54.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj54.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj54.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj54.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj54.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj54.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('intoMaterial_2ndSegment', self.obj54.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj54.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj54.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj54.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj54.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj54.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj54.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj54.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj54.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj54.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj54.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('intoMaterial_2ndLink', self.obj54.Graphical_Appearance.linkInfo.SecondLink))
    self.obj54.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj54.Graphical_Appearance.semObject
    self.obj54.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj54.Graphical_Appearance.semObject
    self.obj54.Graphical_Appearance.linkInfo.Center.semObject=self.obj54.Graphical_Appearance.semObject
    self.obj54.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj54.Graphical_Appearance.semObject
    self.obj54.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj54.Graphical_Appearance.semObject

    # name
    self.obj54.name.setValue('intoMaterial')

    # displaySelect
    self.obj54.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj54.displaySelect.config = 0

    # attributes
    self.obj54.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('rate', 'Float', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Float(0.0)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj54.attributes.setValue(lcobj2)

    # cardinality
    self.obj54.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('operatingUnit', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('metarial', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj54.cardinality.setValue(lcobj2)

    # display
    self.obj54.display.setValue('Attributes:\n  - rate :: Float\nMultiplicities:\n  - From operatingUnit: 0 to N\n  - To metarial: 0 to N\n')
    self.obj54.display.setHeight(15)

    # Actions
    self.obj54.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj54.Actions.setValue(lcobj2)

    # Constraints
    self.obj54.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj54.Constraints.setValue(lcobj2)

    self.obj54.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(103.0,422.0,self.obj54)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.4, 1.0161290322580647]
    else: new_obj = None
    self.obj54.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj54)
    self.globalAndLocalPostcondition(self.obj54, rootNode)
    self.obj54.postAction( rootNode.CREATE )

    self.obj55=CD_Association3(self)
    self.obj55.isGraphObjectVisual = True

    if(hasattr(self.obj55, '_setHierarchicalLink')):
      self.obj55._setHierarchicalLink(False)

    # QOCA
    self.obj55.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj55.Graphical_Appearance.setValue( ('intoProduct', self.obj55))
    self.obj55.Graphical_Appearance.linkInfo=linkEditor(self,self.obj55.Graphical_Appearance.semObject, "intoProduct")
    self.obj55.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj55.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj55.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj55.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj55.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj55.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj55.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj55.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj55.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('intoProduct_1stLink', self.obj55.Graphical_Appearance.linkInfo.FirstLink))
    self.obj55.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj55.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj55.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj55.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj55.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj55.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj55.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj55.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj55.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj55.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj55.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj55.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('intoProduct_1stSegment', self.obj55.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj55.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj55.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj55.Graphical_Appearance.linkInfo.Center.setValue( ('intoProduct_Center', self.obj55.Graphical_Appearance.linkInfo))
    self.obj55.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj55.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj55.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj55.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj55.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj55.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj55.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj55.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj55.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj55.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj55.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj55.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('intoProduct_2ndSegment', self.obj55.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj55.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj55.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj55.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj55.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj55.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj55.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj55.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj55.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj55.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj55.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('intoProduct_2ndLink', self.obj55.Graphical_Appearance.linkInfo.SecondLink))
    self.obj55.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj55.Graphical_Appearance.semObject
    self.obj55.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj55.Graphical_Appearance.semObject
    self.obj55.Graphical_Appearance.linkInfo.Center.semObject=self.obj55.Graphical_Appearance.semObject
    self.obj55.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj55.Graphical_Appearance.semObject
    self.obj55.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj55.Graphical_Appearance.semObject

    # name
    self.obj55.name.setValue('intoProduct')

    # displaySelect
    self.obj55.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj55.displaySelect.config = 0

    # attributes
    self.obj55.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('rate', 'Float', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Float(0.0)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj55.attributes.setValue(lcobj2)

    # cardinality
    self.obj55.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('operatingUnit', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('product', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj55.cardinality.setValue(lcobj2)

    # display
    self.obj55.display.setValue('Attributes:\n  - rate :: Float\nMultiplicities:\n  - From operatingUnit: 0 to N\n  - To product: 0 to N\n')
    self.obj55.display.setHeight(15)

    # Actions
    self.obj55.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj55.Actions.setValue(lcobj2)

    # Constraints
    self.obj55.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj55.Constraints.setValue(lcobj2)

    self.obj55.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(577.0,233.0,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.4, 1.0161290322580647]
    else: new_obj = None
    self.obj55.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)
    self.obj55.postAction( rootNode.CREATE )

    self.obj56=CD_Association3(self)
    self.obj56.isGraphObjectVisual = True

    if(hasattr(self.obj56, '_setHierarchicalLink')):
      self.obj56._setHierarchicalLink(False)

    # QOCA
    self.obj56.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj56.Graphical_Appearance.setValue( ('fromMaterial', self.obj56))
    self.obj56.Graphical_Appearance.linkInfo=linkEditor(self,self.obj56.Graphical_Appearance.semObject, "fromMaterial")
    self.obj56.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj56.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj56.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj56.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj56.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj56.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj56.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj56.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj56.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('fromMaterial_1stLink', self.obj56.Graphical_Appearance.linkInfo.FirstLink))
    self.obj56.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj56.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj56.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj56.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj56.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj56.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj56.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj56.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj56.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj56.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj56.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj56.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('fromMaterial_1stSegment', self.obj56.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj56.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj56.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj56.Graphical_Appearance.linkInfo.Center.setValue( ('fromMaterial_Center', self.obj56.Graphical_Appearance.linkInfo))
    self.obj56.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj56.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj56.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj56.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj56.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj56.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj56.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj56.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj56.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj56.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj56.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj56.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('fromMaterial_2ndSegment', self.obj56.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj56.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj56.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj56.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj56.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj56.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj56.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj56.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj56.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj56.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj56.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('fromMaterial_2ndLink', self.obj56.Graphical_Appearance.linkInfo.SecondLink))
    self.obj56.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj56.Graphical_Appearance.semObject
    self.obj56.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj56.Graphical_Appearance.semObject
    self.obj56.Graphical_Appearance.linkInfo.Center.semObject=self.obj56.Graphical_Appearance.semObject
    self.obj56.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj56.Graphical_Appearance.semObject
    self.obj56.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj56.Graphical_Appearance.semObject

    # name
    self.obj56.name.setValue('fromMaterial')

    # displaySelect
    self.obj56.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj56.displaySelect.config = 0

    # attributes
    self.obj56.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('rate', 'Float', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Float(0.0)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj56.attributes.setValue(lcobj2)

    # cardinality
    self.obj56.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('metarial', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('operatingUnit', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj56.cardinality.setValue(lcobj2)

    # display
    self.obj56.display.setValue('Attributes:\n  - rate :: Float\nMultiplicities:\n  - From metarial: 0 to N\n  - To operatingUnit: 0 to N\n')
    self.obj56.display.setHeight(15)

    # Actions
    self.obj56.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj56.Actions.setValue(lcobj2)

    # Constraints
    self.obj56.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj56.Constraints.setValue(lcobj2)

    self.obj56.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(548.0,405.0,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.2530000000000001, 1.0161290322580647]
    else: new_obj = None
    self.obj56.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)
    self.obj56.postAction( rootNode.CREATE )

    # Connections for obj49 (graphObject_: Obj12) named rawMaterial
    self.drawConnections(
(self.obj49,self.obj53,[86.13968792099999, 141.40012558076398, 95.0, 231.0],"true", 2) )
    # Connections for obj50 (graphObject_: Obj13) named product
    self.drawConnections(
 )
    # Connections for obj51 (graphObject_: Obj14) named metarial
    self.drawConnections(
(self.obj51,self.obj56,[431.0, 491.327868852459, 569.0, 500.0, 548.0, 405.0],"true", 3) )
    # Connections for obj52 (graphObject_: Obj15) named operatingUnit
    self.drawConnections(
(self.obj52,self.obj55,[431.0, 233.31967213114754, 577.0, 233.0],"true", 2),
(self.obj52,self.obj54,[241.0, 338.6639344262295, 142.0, 342.0, 103.0, 422.0],"true", 3) )
    # Connections for obj53 (graphObject_: Obj16) named fromRaw
    self.drawConnections(
(self.obj53,self.obj52,[95.0, 231.0, 241.0, 233.31967213114754],"true", 2) )
    # Connections for obj54 (graphObject_: Obj18) named intoMaterial
    self.drawConnections(
(self.obj54,self.obj51,[103.0, 422.0, 110.0, 533.0, 241.0, 520.5901639344262],"true", 3) )
    # Connections for obj55 (graphObject_: Obj20) named intoProduct
    self.drawConnections(
(self.obj55,self.obj50,[577.0, 233.0, 596.0, 141.0],"true", 2) )
    # Connections for obj56 (graphObject_: Obj22) named fromMaterial
    self.drawConnections(
(self.obj56,self.obj52,[548.0, 405.0, 542.0, 316.0, 431.0, 305.7438524590164],"true", 3) )

newfunction = pns_MDL

loadedMMName = 'CD_ClassDiagramsV3_META'

atom3version = '0.3'
