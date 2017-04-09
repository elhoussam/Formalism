"""
__omacs_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: sam
Modified: Fri Mar 31 17:02:49 2017
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
        CD_ClassDiagramsV3RootNode.name.setValue('omacs')

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


    self.obj855=CD_Class3(self)
    self.obj855.isGraphObjectVisual = True

    if(hasattr(self.obj855, '_setHierarchicalLink')):
      self.obj855._setHierarchicalLink(False)

    # QOCA
    self.obj855.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj855.Graphical_Appearance.setValue( ('Agent', self.obj855))

    # name
    self.obj855.name.setValue('Agent')

    # attributes
    self.obj855.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj855.attributes.setValue(lcobj2)

    # Abstract
    self.obj855.Abstract.setValue((None, 0))
    self.obj855.Abstract.config = 0

    # cardinality
    self.obj855.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('posses', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('CapableOf', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj855.cardinality.setValue(lcobj2)

    # display
    self.obj855.display.setValue('Attributes:\n  - name :: String\n  - price :: Integer\nMultiplicities:\n  - To posses: 0 to N\n  - To CapableOf: 0 to N\n')
    self.obj855.display.setHeight(15)

    # Actions
    self.obj855.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj855.Actions.setValue(lcobj2)

    # Constraints
    self.obj855.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj855.Constraints.setValue(lcobj2)

    self.obj855.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(20.0,20.0,self.obj855)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0844262295081968]
    else: new_obj = None
    self.obj855.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj855)
    self.globalAndLocalPostcondition(self.obj855, rootNode)
    self.obj855.postAction( rootNode.CREATE )

    self.obj856=CD_Class3(self)
    self.obj856.isGraphObjectVisual = True

    if(hasattr(self.obj856, '_setHierarchicalLink')):
      self.obj856._setHierarchicalLink(False)

    # QOCA
    self.obj856.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj856.Graphical_Appearance.setValue( ('Capabilitie', self.obj856))

    # name
    self.obj856.name.setValue('Capabilitie')

    # attributes
    self.obj856.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj856.attributes.setValue(lcobj2)

    # Abstract
    self.obj856.Abstract.setValue((None, 0))
    self.obj856.Abstract.config = 0

    # cardinality
    self.obj856.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('posses', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('require', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj856.cardinality.setValue(lcobj2)

    # display
    self.obj856.display.setValue('Attributes:\n  - name :: String\nMultiplicities:\n  - From posses: 0 to N\n  - From require: 0 to N\n')
    self.obj856.display.setHeight(15)

    # Actions
    self.obj856.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj856.Actions.setValue(lcobj2)

    # Constraints
    self.obj856.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj856.Constraints.setValue(lcobj2)

    self.obj856.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(540.0,20.0,self.obj856)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj856.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj856)
    self.globalAndLocalPostcondition(self.obj856, rootNode)
    self.obj856.postAction( rootNode.CREATE )

    self.obj857=CD_Class3(self)
    self.obj857.isGraphObjectVisual = True

    if(hasattr(self.obj857, '_setHierarchicalLink')):
      self.obj857._setHierarchicalLink(False)

    # QOCA
    self.obj857.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj857.Graphical_Appearance.setValue( ('Role', self.obj857))

    # name
    self.obj857.name.setValue('Role')

    # attributes
    self.obj857.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj857.attributes.setValue(lcobj2)

    # Abstract
    self.obj857.Abstract.setValue((None, 0))
    self.obj857.Abstract.config = 0

    # cardinality
    self.obj857.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('CapableOf', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('achieve', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('require', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj857.cardinality.setValue(lcobj2)

    # display
    self.obj857.display.setValue('Attributes:\n  - name :: String\nMultiplicities:\n  - From CapableOf: 0 to N\n  - To achieve: 0 to N\n  - To require: 0 to N\n')
    self.obj857.display.setHeight(15)

    # Actions
    self.obj857.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj857.Actions.setValue(lcobj2)

    # Constraints
    self.obj857.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj857.Constraints.setValue(lcobj2)

    self.obj857.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(20.0,400.0,self.obj857)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.01171875, 1.0844262295081968]
    else: new_obj = None
    self.obj857.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj857)
    self.globalAndLocalPostcondition(self.obj857, rootNode)
    self.obj857.postAction( rootNode.CREATE )

    self.obj858=CD_Class3(self)
    self.obj858.isGraphObjectVisual = True

    if(hasattr(self.obj858, '_setHierarchicalLink')):
      self.obj858._setHierarchicalLink(False)

    # QOCA
    self.obj858.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj858.Graphical_Appearance.setValue( ('Goal', self.obj858))

    # name
    self.obj858.name.setValue('Goal')

    # attributes
    self.obj858.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj858.attributes.setValue(lcobj2)

    # Abstract
    self.obj858.Abstract.setValue((None, 0))
    self.obj858.Abstract.config = 0

    # cardinality
    self.obj858.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('achieve', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj858.cardinality.setValue(lcobj2)

    # display
    self.obj858.display.setValue('Attributes:\n  - name :: String\nMultiplicities:\n  - From achieve: 0 to N\n')
    self.obj858.display.setHeight(15)

    # Actions
    self.obj858.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj858.Actions.setValue(lcobj2)

    # Constraints
    self.obj858.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj858.Constraints.setValue(lcobj2)

    self.obj858.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(520.0,400.0,self.obj858)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj858.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj858)
    self.globalAndLocalPostcondition(self.obj858, rootNode)
    self.obj858.postAction( rootNode.CREATE )

    self.obj859=CD_Association3(self)
    self.obj859.isGraphObjectVisual = True

    if(hasattr(self.obj859, '_setHierarchicalLink')):
      self.obj859._setHierarchicalLink(False)

    # QOCA
    self.obj859.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj859.Graphical_Appearance.setValue( ('posses', self.obj859))
    self.obj859.Graphical_Appearance.linkInfo=linkEditor(self,self.obj859.Graphical_Appearance.semObject, "posses")
    self.obj859.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj859.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj859.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj859.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj859.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj859.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj859.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj859.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj859.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('posses_1stLink', self.obj859.Graphical_Appearance.linkInfo.FirstLink))
    self.obj859.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj859.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj859.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj859.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj859.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj859.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj859.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj859.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj859.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj859.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj859.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj859.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('posses_1stSegment', self.obj859.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj859.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj859.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj859.Graphical_Appearance.linkInfo.Center.setValue( ('posses_Center', self.obj859.Graphical_Appearance.linkInfo))
    self.obj859.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj859.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj859.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj859.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj859.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj859.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj859.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj859.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj859.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj859.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj859.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj859.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('posses_2ndSegment', self.obj859.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj859.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj859.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj859.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj859.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj859.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj859.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj859.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj859.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj859.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj859.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('posses_2ndLink', self.obj859.Graphical_Appearance.linkInfo.SecondLink))
    self.obj859.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj859.Graphical_Appearance.semObject
    self.obj859.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj859.Graphical_Appearance.semObject
    self.obj859.Graphical_Appearance.linkInfo.Center.semObject=self.obj859.Graphical_Appearance.semObject
    self.obj859.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj859.Graphical_Appearance.semObject
    self.obj859.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj859.Graphical_Appearance.semObject

    # name
    self.obj859.name.setValue('posses')

    # displaySelect
    self.obj859.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj859.displaySelect.config = 0

    # attributes
    self.obj859.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('rate', 'Float', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Float(0.0)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj859.attributes.setValue(lcobj2)

    # cardinality
    self.obj859.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Capabilitie', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Agent', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj859.cardinality.setValue(lcobj2)

    # display
    self.obj859.display.setValue('Attributes:\n  - rate :: Float\nMultiplicities:\n  - To Capabilitie: 0 to N\n  - From Agent: 0 to N\n')
    self.obj859.display.setHeight(15)

    # Actions
    self.obj859.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj859.Actions.setValue(lcobj2)

    # Constraints
    self.obj859.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj859.Constraints.setValue(lcobj2)

    self.obj859.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(385.0,89.0,self.obj859)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.169, 1.185483870967742]
    else: new_obj = None
    self.obj859.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj859)
    self.globalAndLocalPostcondition(self.obj859, rootNode)
    self.obj859.postAction( rootNode.CREATE )

    self.obj860=CD_Association3(self)
    self.obj860.isGraphObjectVisual = True

    if(hasattr(self.obj860, '_setHierarchicalLink')):
      self.obj860._setHierarchicalLink(False)

    # QOCA
    self.obj860.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj860.Graphical_Appearance.setValue( ('CapableOf', self.obj860))
    self.obj860.Graphical_Appearance.linkInfo=linkEditor(self,self.obj860.Graphical_Appearance.semObject, "CapableOf")
    self.obj860.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj860.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj860.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj860.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj860.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj860.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj860.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj860.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj860.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('CapableOf_1stLink', self.obj860.Graphical_Appearance.linkInfo.FirstLink))
    self.obj860.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj860.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj860.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj860.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj860.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj860.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj860.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj860.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj860.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj860.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj860.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj860.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('CapableOf_1stSegment', self.obj860.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj860.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj860.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj860.Graphical_Appearance.linkInfo.Center.setValue( ('CapableOf_Center', self.obj860.Graphical_Appearance.linkInfo))
    self.obj860.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj860.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj860.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj860.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj860.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj860.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj860.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj860.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj860.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj860.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj860.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj860.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('CapableOf_2ndSegment', self.obj860.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj860.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj860.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj860.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj860.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj860.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj860.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj860.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj860.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj860.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj860.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('CapableOf_2ndLink', self.obj860.Graphical_Appearance.linkInfo.SecondLink))
    self.obj860.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj860.Graphical_Appearance.semObject
    self.obj860.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj860.Graphical_Appearance.semObject
    self.obj860.Graphical_Appearance.linkInfo.Center.semObject=self.obj860.Graphical_Appearance.semObject
    self.obj860.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj860.Graphical_Appearance.semObject
    self.obj860.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj860.Graphical_Appearance.semObject

    # name
    self.obj860.name.setValue('CapableOf')

    # displaySelect
    self.obj860.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj860.displaySelect.config = 0

    # attributes
    self.obj860.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('rate', 'Float', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Float(0.0)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj860.attributes.setValue(lcobj2)

    # cardinality
    self.obj860.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Agent', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj860.cardinality.setValue(lcobj2)

    # display
    self.obj860.display.setValue('Attributes:\n  - rate :: Float\nMultiplicities:\n  - To Role: 0 to N\n  - From Agent: 0 to N\n')
    self.obj860.display.setHeight(15)

    # Actions
    self.obj860.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj860.Actions.setValue(lcobj2)

    # Constraints
    self.obj860.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj860.Constraints.setValue(lcobj2)

    self.obj860.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(100.78125,285.0,self.obj860)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.05, 1.185483870967742]
    else: new_obj = None
    self.obj860.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj860)
    self.globalAndLocalPostcondition(self.obj860, rootNode)
    self.obj860.postAction( rootNode.CREATE )

    self.obj861=CD_Association3(self)
    self.obj861.isGraphObjectVisual = True

    if(hasattr(self.obj861, '_setHierarchicalLink')):
      self.obj861._setHierarchicalLink(False)

    # QOCA
    self.obj861.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj861.Graphical_Appearance.setValue( ('achieve', self.obj861))
    self.obj861.Graphical_Appearance.linkInfo=linkEditor(self,self.obj861.Graphical_Appearance.semObject, "achieve")
    self.obj861.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj861.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj861.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj861.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj861.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj861.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj861.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj861.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj861.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('achieve_1stLink', self.obj861.Graphical_Appearance.linkInfo.FirstLink))
    self.obj861.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj861.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj861.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj861.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj861.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj861.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj861.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj861.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj861.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj861.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj861.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj861.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('achieve_1stSegment', self.obj861.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj861.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj861.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj861.Graphical_Appearance.linkInfo.Center.setValue( ('achieve_Center', self.obj861.Graphical_Appearance.linkInfo))
    self.obj861.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj861.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj861.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj861.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj861.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj861.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj861.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj861.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj861.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj861.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj861.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj861.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('achieve_2ndSegment', self.obj861.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj861.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj861.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj861.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj861.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj861.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj861.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj861.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj861.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj861.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj861.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('achieve_2ndLink', self.obj861.Graphical_Appearance.linkInfo.SecondLink))
    self.obj861.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj861.Graphical_Appearance.semObject
    self.obj861.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj861.Graphical_Appearance.semObject
    self.obj861.Graphical_Appearance.linkInfo.Center.semObject=self.obj861.Graphical_Appearance.semObject
    self.obj861.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj861.Graphical_Appearance.semObject
    self.obj861.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj861.Graphical_Appearance.semObject

    # name
    self.obj861.name.setValue('achieve')

    # displaySelect
    self.obj861.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj861.displaySelect.config = 0

    # attributes
    self.obj861.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('rate', 'Float', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Float(0.0)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj861.attributes.setValue(lcobj2)

    # cardinality
    self.obj861.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Goal', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj861.cardinality.setValue(lcobj2)

    # display
    self.obj861.display.setValue('Attributes:\n  - rate :: Float\nMultiplicities:\n  - To Goal: 0 to N\n  - From Role: 0 to N\n')
    self.obj861.display.setHeight(15)

    # Actions
    self.obj861.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj861.Actions.setValue(lcobj2)

    # Constraints
    self.obj861.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj861.Constraints.setValue(lcobj2)

    self.obj861.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(386.080078125,476.0,self.obj861)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.185483870967742]
    else: new_obj = None
    self.obj861.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj861)
    self.globalAndLocalPostcondition(self.obj861, rootNode)
    self.obj861.postAction( rootNode.CREATE )

    self.obj862=CD_Association3(self)
    self.obj862.isGraphObjectVisual = True

    if(hasattr(self.obj862, '_setHierarchicalLink')):
      self.obj862._setHierarchicalLink(False)

    # QOCA
    self.obj862.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj862.Graphical_Appearance.setValue( ('require', self.obj862))
    self.obj862.Graphical_Appearance.linkInfo=linkEditor(self,self.obj862.Graphical_Appearance.semObject, "require")
    self.obj862.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj862.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj862.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj862.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj862.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj862.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj862.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj862.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj862.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('require_1stLink', self.obj862.Graphical_Appearance.linkInfo.FirstLink))
    self.obj862.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj862.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj862.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj862.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj862.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj862.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj862.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj862.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj862.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj862.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj862.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj862.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('require_1stSegment', self.obj862.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj862.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj862.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj862.Graphical_Appearance.linkInfo.Center.setValue( ('require_Center', self.obj862.Graphical_Appearance.linkInfo))
    self.obj862.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj862.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj862.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj862.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj862.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj862.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj862.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj862.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj862.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj862.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj862.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj862.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('require_2ndSegment', self.obj862.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj862.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj862.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj862.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj862.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj862.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj862.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj862.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj862.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj862.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj862.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('require_2ndLink', self.obj862.Graphical_Appearance.linkInfo.SecondLink))
    self.obj862.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj862.Graphical_Appearance.semObject
    self.obj862.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj862.Graphical_Appearance.semObject
    self.obj862.Graphical_Appearance.linkInfo.Center.semObject=self.obj862.Graphical_Appearance.semObject
    self.obj862.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj862.Graphical_Appearance.semObject
    self.obj862.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj862.Graphical_Appearance.semObject

    # name
    self.obj862.name.setValue('require')

    # displaySelect
    self.obj862.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj862.displaySelect.config = 0

    # attributes
    self.obj862.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj862.attributes.setValue(lcobj2)

    # cardinality
    self.obj862.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Capabilitie', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj862.cardinality.setValue(lcobj2)

    # display
    self.obj862.display.setValue('Multiplicities:\n  - To Capabilitie: 0 to N\n  - From Role: 0 to N\n')
    self.obj862.display.setHeight(15)

    # Actions
    self.obj862.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj862.Actions.setValue(lcobj2)

    # Constraints
    self.obj862.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj862.Constraints.setValue(lcobj2)

    self.obj862.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(381.25,277.25,self.obj862)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.169, 1.0]
    else: new_obj = None
    self.obj862.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj862)
    self.globalAndLocalPostcondition(self.obj862, rootNode)
    self.obj862.postAction( rootNode.CREATE )

    # Connections for obj855 (graphObject_: Obj152) named Agent
    self.drawConnections(
(self.obj855,self.obj859,[211.0, 94.92131147540987, 385.0, 89.0],"true", 2),
(self.obj855,self.obj860,[96.0, 173.0, 100.78125, 285.0],"true", 2) )
    # Connections for obj856 (graphObject_: Obj153) named Capabilitie
    self.drawConnections(
 )
    # Connections for obj857 (graphObject_: Obj154) named Role
    self.drawConnections(
(self.obj857,self.obj861,[212.81640625, 474.9213114754098, 386.080078125, 476.0],"true", 2),
(self.obj857,self.obj862,[177.40625, 401.1803278688525, 294.5, 272.5, 265.0, 275.0, 381.25, 300.25],"true", 4) )
    # Connections for obj858 (graphObject_: Obj155) named Goal
    self.drawConnections(
 )
    # Connections for obj859 (graphObject_: Obj156) named posses
    self.drawConnections(
(self.obj859,self.obj856,[385.0, 89.0, 541.0, 89.0],"true", 2) )
    # Connections for obj860 (graphObject_: Obj158) named CapableOf
    self.drawConnections(
(self.obj860,self.obj857,[100.78125, 285.0, 96.46875, 401.1803278688525],"true", 2) )
    # Connections for obj861 (graphObject_: Obj160) named achieve
    self.drawConnections(
(self.obj861,self.obj858,[386.080078125, 476.0, 521.0, 469.0],"true", 2) )
    # Connections for obj862 (graphObject_: Obj162) named require
    self.drawConnections(
(self.obj862,self.obj856,[381.25, 300.25, 612.0, 294.0, 468.0, 305.0, 616.0, 161.0],"true", 4) )

newfunction = omacs_MDL

loadedMMName = 'CD_ClassDiagramsV3_META'

atom3version = '0.3'
