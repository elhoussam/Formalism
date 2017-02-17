"""
__omacs_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: sam
Modified: Wed Feb 15 12:18:44 2017
___________________________________________________________________
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

def omacs_MDL(self, rootNode, CD_ClassDiagramsV3RootNode=None):

    # --- Generating attributes code for ASG CD_ClassDiagramsV3 ---
    if( CD_ClassDiagramsV3RootNode ): 
        # name
        CD_ClassDiagramsV3RootNode.name.setValue('omacss')

        # author
        CD_ClassDiagramsV3RootNode.author.setValue('houssam nouar kherkhachi')

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


    self.obj47=CD_Class3(self)
    self.obj47.isGraphObjectVisual = True

    if(hasattr(self.obj47, '_setHierarchicalLink')):
      self.obj47._setHierarchicalLink(False)

    # QOCA
    self.obj47.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj47.Graphical_Appearance.setValue( ('Agent', self.obj47))

    # name
    self.obj47.name.setValue('Agent')

    # attributes
    self.obj47.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('price', 'Integer', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Integer(0)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj47.attributes.setValue(lcobj2)

    # Abstract
    self.obj47.Abstract.setValue((None, 0))
    self.obj47.Abstract.config = 0

    # cardinality
    self.obj47.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('posses', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('CapableOf', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj47.cardinality.setValue(lcobj2)

    # display
    self.obj47.display.setValue('Attributes:\n  - name :: String\n  - price :: Integer\nMultiplicities:\n  - To posses: 0 to N\n  - To CapableOf: 0 to N\n')
    self.obj47.display.setHeight(15)

    # Actions
    self.obj47.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj47.Actions.setValue(lcobj2)

    # Constraints
    self.obj47.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj47.Constraints.setValue(lcobj2)

    self.obj47.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(0.0,20.0,self.obj47)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0844262295081968]
    else: new_obj = None
    self.obj47.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj47)
    self.globalAndLocalPostcondition(self.obj47, rootNode)
    self.obj47.postAction( rootNode.CREATE )

    self.obj48=CD_Class3(self)
    self.obj48.isGraphObjectVisual = True

    if(hasattr(self.obj48, '_setHierarchicalLink')):
      self.obj48._setHierarchicalLink(False)

    # QOCA
    self.obj48.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj48.Graphical_Appearance.setValue( ('Capabilitie', self.obj48))

    # name
    self.obj48.name.setValue('Capabilitie')

    # attributes
    self.obj48.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj48.attributes.setValue(lcobj2)

    # Abstract
    self.obj48.Abstract.setValue((None, 0))
    self.obj48.Abstract.config = 0

    # cardinality
    self.obj48.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('posses', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('requir', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj48.cardinality.setValue(lcobj2)

    # display
    self.obj48.display.setValue('Attributes:\n  - name :: String\nMultiplicities:\n  - From posses: 0 to N\n  - From requir: 0 to N\n')
    self.obj48.display.setHeight(15)

    # Actions
    self.obj48.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj48.Actions.setValue(lcobj2)

    # Constraints
    self.obj48.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj48.Constraints.setValue(lcobj2)

    self.obj48.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(540.0,20.0,self.obj48)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj48.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj48)
    self.globalAndLocalPostcondition(self.obj48, rootNode)
    self.obj48.postAction( rootNode.CREATE )

    self.obj49=CD_Class3(self)
    self.obj49.isGraphObjectVisual = True

    if(hasattr(self.obj49, '_setHierarchicalLink')):
      self.obj49._setHierarchicalLink(False)

    # QOCA
    self.obj49.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj49.Graphical_Appearance.setValue( ('Role', self.obj49))

    # name
    self.obj49.name.setValue('Role')

    # attributes
    self.obj49.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
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
    cobj2.setValue(('CapableOf', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('achieve', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('requir', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj49.cardinality.setValue(lcobj2)

    # display
    self.obj49.display.setValue('Attributes:\n  - name :: String\nMultiplicities:\n  - From CapableOf: 0 to N\n  - To achieve: 0 to N\n  - To requir: 0 to N\n')
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
       new_obj = graph_CD_Class3(20.0,400.0,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.01171875, 1.0844262295081968]
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
    self.obj50.Graphical_Appearance.setValue( ('Goal', self.obj50))

    # name
    self.obj50.name.setValue('Goal')

    # attributes
    self.obj50.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
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
    cobj2.setValue(('achieve', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj50.cardinality.setValue(lcobj2)

    # display
    self.obj50.display.setValue('Attributes:\n  - name :: String\nMultiplicities:\n  - From achieve: 0 to N\n')
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
       new_obj = graph_CD_Class3(520.0,400.0,self.obj50)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj50.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj50)
    self.globalAndLocalPostcondition(self.obj50, rootNode)
    self.obj50.postAction( rootNode.CREATE )

    self.obj51=CD_Association3(self)
    self.obj51.isGraphObjectVisual = True

    if(hasattr(self.obj51, '_setHierarchicalLink')):
      self.obj51._setHierarchicalLink(False)

    # QOCA
    self.obj51.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj51.Graphical_Appearance.setValue( ('posses', self.obj51))
    self.obj51.Graphical_Appearance.linkInfo=linkEditor(self,self.obj51.Graphical_Appearance.semObject, "posses")
    self.obj51.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj51.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj51.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj51.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj51.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj51.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj51.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj51.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj51.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('posses_1stLink', self.obj51.Graphical_Appearance.linkInfo.FirstLink))
    self.obj51.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj51.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj51.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj51.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj51.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj51.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj51.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj51.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj51.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj51.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj51.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj51.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('posses_1stSegment', self.obj51.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj51.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj51.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj51.Graphical_Appearance.linkInfo.Center.setValue( ('posses_Center', self.obj51.Graphical_Appearance.linkInfo))
    self.obj51.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj51.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj51.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj51.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj51.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj51.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj51.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj51.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj51.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj51.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj51.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj51.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('posses_2ndSegment', self.obj51.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj51.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj51.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj51.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj51.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj51.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj51.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj51.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj51.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj51.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj51.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('posses_2ndLink', self.obj51.Graphical_Appearance.linkInfo.SecondLink))
    self.obj51.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj51.Graphical_Appearance.semObject
    self.obj51.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj51.Graphical_Appearance.semObject
    self.obj51.Graphical_Appearance.linkInfo.Center.semObject=self.obj51.Graphical_Appearance.semObject
    self.obj51.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj51.Graphical_Appearance.semObject
    self.obj51.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj51.Graphical_Appearance.semObject

    # name
    self.obj51.name.setValue('posses')

    # displaySelect
    self.obj51.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj51.displaySelect.config = 0

    # attributes
    self.obj51.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('rate', 'Float', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Float(0.0)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj51.attributes.setValue(lcobj2)

    # cardinality
    self.obj51.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Capabilitie', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Agent', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj51.cardinality.setValue(lcobj2)

    # display
    self.obj51.display.setValue('Attributes:\n  - rate :: Float\nMultiplicities:\n  - To Capabilitie: 0 to N\n  - From Agent: 0 to N\n')
    self.obj51.display.setHeight(15)

    # Actions
    self.obj51.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj51.Actions.setValue(lcobj2)

    # Constraints
    self.obj51.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj51.Constraints.setValue(lcobj2)

    self.obj51.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(385.0,89.0,self.obj51)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.169, 1.185483870967742]
    else: new_obj = None
    self.obj51.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj51)
    self.globalAndLocalPostcondition(self.obj51, rootNode)
    self.obj51.postAction( rootNode.CREATE )

    self.obj52=CD_Association3(self)
    self.obj52.isGraphObjectVisual = True

    if(hasattr(self.obj52, '_setHierarchicalLink')):
      self.obj52._setHierarchicalLink(False)

    # QOCA
    self.obj52.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj52.Graphical_Appearance.setValue( ('CapableOf', self.obj52))
    self.obj52.Graphical_Appearance.linkInfo=linkEditor(self,self.obj52.Graphical_Appearance.semObject, "CapableOf")
    self.obj52.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj52.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj52.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj52.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj52.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj52.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj52.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj52.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj52.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('CapableOf_1stLink', self.obj52.Graphical_Appearance.linkInfo.FirstLink))
    self.obj52.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj52.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj52.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj52.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj52.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj52.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj52.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj52.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj52.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj52.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj52.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj52.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('CapableOf_1stSegment', self.obj52.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj52.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj52.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj52.Graphical_Appearance.linkInfo.Center.setValue( ('CapableOf_Center', self.obj52.Graphical_Appearance.linkInfo))
    self.obj52.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj52.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj52.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj52.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj52.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj52.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj52.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj52.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj52.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj52.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj52.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj52.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('CapableOf_2ndSegment', self.obj52.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj52.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj52.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj52.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj52.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj52.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj52.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj52.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj52.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj52.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj52.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('CapableOf_2ndLink', self.obj52.Graphical_Appearance.linkInfo.SecondLink))
    self.obj52.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj52.Graphical_Appearance.semObject
    self.obj52.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj52.Graphical_Appearance.semObject
    self.obj52.Graphical_Appearance.linkInfo.Center.semObject=self.obj52.Graphical_Appearance.semObject
    self.obj52.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj52.Graphical_Appearance.semObject
    self.obj52.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj52.Graphical_Appearance.semObject

    # name
    self.obj52.name.setValue('CapableOf')

    # displaySelect
    self.obj52.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj52.displaySelect.config = 0

    # attributes
    self.obj52.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj52.attributes.setValue(lcobj2)

    # cardinality
    self.obj52.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Agent', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj52.cardinality.setValue(lcobj2)

    # display
    self.obj52.display.setValue('Multiplicities:\n  - To Role: 0 to N\n  - From Agent: 0 to N\n')
    self.obj52.display.setHeight(15)

    # Actions
    self.obj52.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj52.Actions.setValue(lcobj2)

    # Constraints
    self.obj52.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj52.Constraints.setValue(lcobj2)

    self.obj52.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(100.78125,285.0,self.obj52)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.05, 1.0]
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
    self.obj53.Graphical_Appearance.setValue( ('achieve', self.obj53))
    self.obj53.Graphical_Appearance.linkInfo=linkEditor(self,self.obj53.Graphical_Appearance.semObject, "achieve")
    self.obj53.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj53.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj53.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj53.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj53.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj53.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj53.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj53.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj53.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('achieve_1stLink', self.obj53.Graphical_Appearance.linkInfo.FirstLink))
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
    self.obj53.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('achieve_1stSegment', self.obj53.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj53.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj53.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj53.Graphical_Appearance.linkInfo.Center.setValue( ('achieve_Center', self.obj53.Graphical_Appearance.linkInfo))
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
    self.obj53.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('achieve_2ndSegment', self.obj53.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj53.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj53.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj53.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj53.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj53.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj53.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj53.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj53.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj53.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj53.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('achieve_2ndLink', self.obj53.Graphical_Appearance.linkInfo.SecondLink))
    self.obj53.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj53.Graphical_Appearance.semObject
    self.obj53.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj53.Graphical_Appearance.semObject
    self.obj53.Graphical_Appearance.linkInfo.Center.semObject=self.obj53.Graphical_Appearance.semObject
    self.obj53.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj53.Graphical_Appearance.semObject
    self.obj53.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj53.Graphical_Appearance.semObject

    # name
    self.obj53.name.setValue('achieve')

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
    cobj2.setValue(('Goal', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj53.cardinality.setValue(lcobj2)

    # display
    self.obj53.display.setValue('Attributes:\n  - rate :: Float\nMultiplicities:\n  - To Goal: 0 to N\n  - From Role: 0 to N\n')
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
       new_obj = graph_CD_Association3(386.080078125,476.0,self.obj53)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.185483870967742]
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
    self.obj54.Graphical_Appearance.setValue( ('requir', self.obj54))
    self.obj54.Graphical_Appearance.linkInfo=linkEditor(self,self.obj54.Graphical_Appearance.semObject, "requir")
    self.obj54.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj54.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj54.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj54.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj54.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj54.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj54.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj54.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj54.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('requir_1stLink', self.obj54.Graphical_Appearance.linkInfo.FirstLink))
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
    self.obj54.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('requir_1stSegment', self.obj54.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj54.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj54.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj54.Graphical_Appearance.linkInfo.Center.setValue( ('requir_Center', self.obj54.Graphical_Appearance.linkInfo))
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
    self.obj54.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('requir_2ndSegment', self.obj54.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj54.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj54.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj54.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj54.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj54.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj54.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj54.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj54.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj54.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj54.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('requir_2ndLink', self.obj54.Graphical_Appearance.linkInfo.SecondLink))
    self.obj54.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj54.Graphical_Appearance.semObject
    self.obj54.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj54.Graphical_Appearance.semObject
    self.obj54.Graphical_Appearance.linkInfo.Center.semObject=self.obj54.Graphical_Appearance.semObject
    self.obj54.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj54.Graphical_Appearance.semObject
    self.obj54.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj54.Graphical_Appearance.semObject

    # name
    self.obj54.name.setValue('requir')

    # displaySelect
    self.obj54.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj54.displaySelect.config = 0

    # attributes
    self.obj54.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj54.attributes.setValue(lcobj2)

    # cardinality
    self.obj54.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Capabilitie', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj54.cardinality.setValue(lcobj2)

    # display
    self.obj54.display.setValue('Multiplicities:\n  - To Capabilitie: 0 to N\n  - From Role: 0 to N\n')
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
       new_obj = graph_CD_Association3(381.25,300.25,self.obj54)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.169, 1.0]
    else: new_obj = None
    self.obj54.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj54)
    self.globalAndLocalPostcondition(self.obj54, rootNode)
    self.obj54.postAction( rootNode.CREATE )

    # Connections for obj47 (graphObject_: Obj27) named Agent
    self.drawConnections(
(self.obj47,self.obj51,[191.0, 94.92131147540987, 385.0, 89.0],"true", 2),
(self.obj47,self.obj52,[116.0, 173.0, 100.78125, 285.0],"true", 2) )
    # Connections for obj48 (graphObject_: Obj28) named Capabilitie
    self.drawConnections(
 )
    # Connections for obj49 (graphObject_: Obj29) named Role
    self.drawConnections(
(self.obj49,self.obj53,[212.81640625, 474.9213114754098, 386.080078125, 476.0],"true", 2),
(self.obj49,self.obj54,[177.40625, 413.0, 265.0, 275.0, 294.5, 295.5, 381.25, 300.25],"true", 4) )
    # Connections for obj50 (graphObject_: Obj30) named Goal
    self.drawConnections(
 )
    # Connections for obj51 (graphObject_: Obj31) named posses
    self.drawConnections(
(self.obj51,self.obj48,[385.0, 89.0, 541.0, 89.0],"true", 2) )
    # Connections for obj52 (graphObject_: Obj33) named CapableOf
    self.drawConnections(
(self.obj52,self.obj49,[100.78125, 285.0, 96.46875, 413.0],"true", 2) )
    # Connections for obj53 (graphObject_: Obj35) named achieve
    self.drawConnections(
(self.obj53,self.obj50,[386.080078125, 476.0, 521.0, 469.0],"true", 2) )
    # Connections for obj54 (graphObject_: Obj37) named requir
    self.drawConnections(
(self.obj54,self.obj48,[381.25, 300.25, 468.0, 305.0, 612.0, 294.0, 616.0, 161.0],"true", 4) )

newfunction = omacs_MDL

loadedMMName = 'CD_ClassDiagramsV3_META'

atom3version = '0.3'
