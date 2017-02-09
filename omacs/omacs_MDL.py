"""
__omacs_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: sam
Modified: Sat Feb  4 20:01:27 2017
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


    self.obj2291=CD_Class3(self)
    self.obj2291.isGraphObjectVisual = True

    if(hasattr(self.obj2291, '_setHierarchicalLink')):
      self.obj2291._setHierarchicalLink(False)

    # QOCA
    self.obj2291.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj2291.Graphical_Appearance.setValue( ('Agent', self.obj2291))

    # name
    self.obj2291.name.setValue('Agent')

    # attributes
    self.obj2291.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj2291.attributes.setValue(lcobj2)

    # Abstract
    self.obj2291.Abstract.setValue((None, 0))
    self.obj2291.Abstract.config = 0

    # cardinality
    self.obj2291.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('posses', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('CapableOf', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj2291.cardinality.setValue(lcobj2)

    # display
    self.obj2291.display.setValue('Attributes:\n  - name :: String\n  - price :: Integer\nMultiplicities:\n  - To posses: 0 to N\n  - To CapableOf: 0 to N\n')
    self.obj2291.display.setHeight(15)

    # Actions
    self.obj2291.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj2291.Actions.setValue(lcobj2)

    # Constraints
    self.obj2291.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj2291.Constraints.setValue(lcobj2)

    self.obj2291.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(20.0,20.0,self.obj2291)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0844262295081968]
    else: new_obj = None
    self.obj2291.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2291)
    self.globalAndLocalPostcondition(self.obj2291, rootNode)
    self.obj2291.postAction( rootNode.CREATE )

    self.obj2292=CD_Class3(self)
    self.obj2292.isGraphObjectVisual = True

    if(hasattr(self.obj2292, '_setHierarchicalLink')):
      self.obj2292._setHierarchicalLink(False)

    # QOCA
    self.obj2292.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj2292.Graphical_Appearance.setValue( ('Capabilitie', self.obj2292))

    # name
    self.obj2292.name.setValue('Capabilitie')

    # attributes
    self.obj2292.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj2292.attributes.setValue(lcobj2)

    # Abstract
    self.obj2292.Abstract.setValue((None, 0))
    self.obj2292.Abstract.config = 0

    # cardinality
    self.obj2292.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('posses', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('require', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj2292.cardinality.setValue(lcobj2)

    # display
    self.obj2292.display.setValue('Attributes:\n  - name :: String\nMultiplicities:\n  - From posses: 0 to N\n  - From require: 0 to N\n')
    self.obj2292.display.setHeight(15)

    # Actions
    self.obj2292.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj2292.Actions.setValue(lcobj2)

    # Constraints
    self.obj2292.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj2292.Constraints.setValue(lcobj2)

    self.obj2292.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(540.0,20.0,self.obj2292)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2292.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2292)
    self.globalAndLocalPostcondition(self.obj2292, rootNode)
    self.obj2292.postAction( rootNode.CREATE )

    self.obj2293=CD_Class3(self)
    self.obj2293.isGraphObjectVisual = True

    if(hasattr(self.obj2293, '_setHierarchicalLink')):
      self.obj2293._setHierarchicalLink(False)

    # QOCA
    self.obj2293.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj2293.Graphical_Appearance.setValue( ('Role', self.obj2293))

    # name
    self.obj2293.name.setValue('Role')

    # attributes
    self.obj2293.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj2293.attributes.setValue(lcobj2)

    # Abstract
    self.obj2293.Abstract.setValue((None, 0))
    self.obj2293.Abstract.config = 0

    # cardinality
    self.obj2293.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('CapableOf', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('require', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('achieve', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj2293.cardinality.setValue(lcobj2)

    # display
    self.obj2293.display.setValue('Attributes:\n  - name :: String\nMultiplicities:\n  - From CapableOf: 0 to N\n  - To require: 0 to N\n  - To achieve: 0 to N\n')
    self.obj2293.display.setHeight(15)

    # Actions
    self.obj2293.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj2293.Actions.setValue(lcobj2)

    # Constraints
    self.obj2293.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj2293.Constraints.setValue(lcobj2)

    self.obj2293.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(20.0,400.0,self.obj2293)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.01171875, 1.0844262295081968]
    else: new_obj = None
    self.obj2293.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2293)
    self.globalAndLocalPostcondition(self.obj2293, rootNode)
    self.obj2293.postAction( rootNode.CREATE )

    self.obj2294=CD_Class3(self)
    self.obj2294.isGraphObjectVisual = True

    if(hasattr(self.obj2294, '_setHierarchicalLink')):
      self.obj2294._setHierarchicalLink(False)

    # QOCA
    self.obj2294.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj2294.Graphical_Appearance.setValue( ('Goal', self.obj2294))

    # name
    self.obj2294.name.setValue('Goal')

    # attributes
    self.obj2294.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj2294.attributes.setValue(lcobj2)

    # Abstract
    self.obj2294.Abstract.setValue((None, 0))
    self.obj2294.Abstract.config = 0

    # cardinality
    self.obj2294.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('achieve', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj2294.cardinality.setValue(lcobj2)

    # display
    self.obj2294.display.setValue('Attributes:\n  - name :: String\nMultiplicities:\n  - From achieve: 0 to N\n')
    self.obj2294.display.setHeight(15)

    # Actions
    self.obj2294.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj2294.Actions.setValue(lcobj2)

    # Constraints
    self.obj2294.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj2294.Constraints.setValue(lcobj2)

    self.obj2294.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(560.0,400.0,self.obj2294)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2294.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2294)
    self.globalAndLocalPostcondition(self.obj2294, rootNode)
    self.obj2294.postAction( rootNode.CREATE )

    self.obj2295=CD_Association3(self)
    self.obj2295.isGraphObjectVisual = True

    if(hasattr(self.obj2295, '_setHierarchicalLink')):
      self.obj2295._setHierarchicalLink(False)

    # QOCA
    self.obj2295.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj2295.Graphical_Appearance.setValue( ('posses', self.obj2295))
    self.obj2295.Graphical_Appearance.linkInfo=linkEditor(self,self.obj2295.Graphical_Appearance.semObject, "posses")
    self.obj2295.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj2295.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj2295.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj2295.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj2295.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj2295.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj2295.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj2295.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj2295.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('posses_1stLink', self.obj2295.Graphical_Appearance.linkInfo.FirstLink))
    self.obj2295.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj2295.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj2295.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj2295.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj2295.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj2295.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj2295.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj2295.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj2295.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj2295.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj2295.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj2295.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('posses_1stSegment', self.obj2295.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj2295.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj2295.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj2295.Graphical_Appearance.linkInfo.Center.setValue( ('posses_Center', self.obj2295.Graphical_Appearance.linkInfo))
    self.obj2295.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj2295.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj2295.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj2295.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj2295.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj2295.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj2295.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj2295.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj2295.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj2295.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj2295.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj2295.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('posses_2ndSegment', self.obj2295.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj2295.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj2295.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj2295.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj2295.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj2295.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj2295.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj2295.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj2295.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj2295.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj2295.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('posses_2ndLink', self.obj2295.Graphical_Appearance.linkInfo.SecondLink))
    self.obj2295.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj2295.Graphical_Appearance.semObject
    self.obj2295.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj2295.Graphical_Appearance.semObject
    self.obj2295.Graphical_Appearance.linkInfo.Center.semObject=self.obj2295.Graphical_Appearance.semObject
    self.obj2295.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj2295.Graphical_Appearance.semObject
    self.obj2295.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj2295.Graphical_Appearance.semObject

    # name
    self.obj2295.name.setValue('posses')

    # displaySelect
    self.obj2295.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj2295.displaySelect.config = 0

    # attributes
    self.obj2295.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('rate', 'Float', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Float(0.0)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj2295.attributes.setValue(lcobj2)

    # cardinality
    self.obj2295.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Capabilitie', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Agent', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj2295.cardinality.setValue(lcobj2)

    # display
    self.obj2295.display.setValue('Attributes:\n  - rate :: Float\nMultiplicities:\n  - To Capabilitie: 0 to N\n  - From Agent: 0 to N\n')
    self.obj2295.display.setHeight(15)

    # Actions
    self.obj2295.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj2295.Actions.setValue(lcobj2)

    # Constraints
    self.obj2295.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj2295.Constraints.setValue(lcobj2)

    self.obj2295.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(385.0,89.0,self.obj2295)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.169, 1.185483870967742]
    else: new_obj = None
    self.obj2295.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2295)
    self.globalAndLocalPostcondition(self.obj2295, rootNode)
    self.obj2295.postAction( rootNode.CREATE )

    self.obj2296=CD_Association3(self)
    self.obj2296.isGraphObjectVisual = True

    if(hasattr(self.obj2296, '_setHierarchicalLink')):
      self.obj2296._setHierarchicalLink(False)

    # QOCA
    self.obj2296.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj2296.Graphical_Appearance.setValue( ('CapableOf', self.obj2296))
    self.obj2296.Graphical_Appearance.linkInfo=linkEditor(self,self.obj2296.Graphical_Appearance.semObject, "CapableOf")
    self.obj2296.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj2296.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj2296.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj2296.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj2296.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj2296.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj2296.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj2296.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj2296.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('CapableOf_1stLink', self.obj2296.Graphical_Appearance.linkInfo.FirstLink))
    self.obj2296.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj2296.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj2296.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj2296.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj2296.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj2296.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj2296.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj2296.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj2296.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj2296.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj2296.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj2296.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('CapableOf_1stSegment', self.obj2296.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj2296.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj2296.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj2296.Graphical_Appearance.linkInfo.Center.setValue( ('CapableOf_Center', self.obj2296.Graphical_Appearance.linkInfo))
    self.obj2296.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj2296.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj2296.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj2296.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj2296.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj2296.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj2296.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj2296.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj2296.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj2296.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj2296.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj2296.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('CapableOf_2ndSegment', self.obj2296.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj2296.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj2296.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj2296.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj2296.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj2296.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj2296.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj2296.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj2296.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj2296.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj2296.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('CapableOf_2ndLink', self.obj2296.Graphical_Appearance.linkInfo.SecondLink))
    self.obj2296.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj2296.Graphical_Appearance.semObject
    self.obj2296.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj2296.Graphical_Appearance.semObject
    self.obj2296.Graphical_Appearance.linkInfo.Center.semObject=self.obj2296.Graphical_Appearance.semObject
    self.obj2296.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj2296.Graphical_Appearance.semObject
    self.obj2296.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj2296.Graphical_Appearance.semObject

    # name
    self.obj2296.name.setValue('CapableOf')

    # displaySelect
    self.obj2296.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj2296.displaySelect.config = 0

    # attributes
    self.obj2296.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj2296.attributes.setValue(lcobj2)

    # cardinality
    self.obj2296.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Agent', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj2296.cardinality.setValue(lcobj2)

    # display
    self.obj2296.display.setValue('Multiplicities:\n  - To Role: 0 to N\n  - From Agent: 0 to N\n')
    self.obj2296.display.setHeight(15)

    # Actions
    self.obj2296.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj2296.Actions.setValue(lcobj2)

    # Constraints
    self.obj2296.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj2296.Constraints.setValue(lcobj2)

    self.obj2296.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(121.78125,281.0,self.obj2296)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.05, 1.0]
    else: new_obj = None
    self.obj2296.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2296)
    self.globalAndLocalPostcondition(self.obj2296, rootNode)
    self.obj2296.postAction( rootNode.CREATE )

    self.obj2297=CD_Association3(self)
    self.obj2297.isGraphObjectVisual = True

    if(hasattr(self.obj2297, '_setHierarchicalLink')):
      self.obj2297._setHierarchicalLink(False)

    # QOCA
    self.obj2297.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj2297.Graphical_Appearance.setValue( ('require', self.obj2297))
    self.obj2297.Graphical_Appearance.linkInfo=linkEditor(self,self.obj2297.Graphical_Appearance.semObject, "require")
    self.obj2297.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj2297.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj2297.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj2297.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj2297.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj2297.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj2297.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj2297.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj2297.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('require_1stLink', self.obj2297.Graphical_Appearance.linkInfo.FirstLink))
    self.obj2297.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj2297.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj2297.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj2297.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj2297.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj2297.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj2297.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj2297.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj2297.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj2297.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj2297.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj2297.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('require_1stSegment', self.obj2297.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj2297.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj2297.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj2297.Graphical_Appearance.linkInfo.Center.setValue( ('require_Center', self.obj2297.Graphical_Appearance.linkInfo))
    self.obj2297.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj2297.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj2297.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj2297.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj2297.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj2297.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj2297.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj2297.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj2297.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj2297.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj2297.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj2297.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('require_2ndSegment', self.obj2297.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj2297.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj2297.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj2297.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj2297.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj2297.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj2297.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj2297.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj2297.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj2297.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj2297.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('require_2ndLink', self.obj2297.Graphical_Appearance.linkInfo.SecondLink))
    self.obj2297.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj2297.Graphical_Appearance.semObject
    self.obj2297.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj2297.Graphical_Appearance.semObject
    self.obj2297.Graphical_Appearance.linkInfo.Center.semObject=self.obj2297.Graphical_Appearance.semObject
    self.obj2297.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj2297.Graphical_Appearance.semObject
    self.obj2297.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj2297.Graphical_Appearance.semObject

    # name
    self.obj2297.name.setValue('require')

    # displaySelect
    self.obj2297.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj2297.displaySelect.config = 0

    # attributes
    self.obj2297.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('rate', 'Float', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Float(0.0)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj2297.attributes.setValue(lcobj2)

    # cardinality
    self.obj2297.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Capabilitie', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj2297.cardinality.setValue(lcobj2)

    # display
    self.obj2297.display.setValue('Attributes:\n  - rate :: Float\nMultiplicities:\n  - To Capabilitie: 0 to N\n  - From Role: 0 to N\n')
    self.obj2297.display.setHeight(15)

    # Actions
    self.obj2297.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj2297.Actions.setValue(lcobj2)

    # Constraints
    self.obj2297.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj2297.Constraints.setValue(lcobj2)

    self.obj2297.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(394.578125,291.0,self.obj2297)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.169, 1.185483870967742]
    else: new_obj = None
    self.obj2297.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2297)
    self.globalAndLocalPostcondition(self.obj2297, rootNode)
    self.obj2297.postAction( rootNode.CREATE )

    self.obj2298=CD_Association3(self)
    self.obj2298.isGraphObjectVisual = True

    if(hasattr(self.obj2298, '_setHierarchicalLink')):
      self.obj2298._setHierarchicalLink(False)

    # QOCA
    self.obj2298.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj2298.Graphical_Appearance.setValue( ('achieve', self.obj2298))
    self.obj2298.Graphical_Appearance.linkInfo=linkEditor(self,self.obj2298.Graphical_Appearance.semObject, "achieve")
    self.obj2298.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj2298.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj2298.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj2298.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj2298.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj2298.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj2298.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj2298.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj2298.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('achieve_1stLink', self.obj2298.Graphical_Appearance.linkInfo.FirstLink))
    self.obj2298.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj2298.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj2298.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj2298.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj2298.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj2298.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj2298.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj2298.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj2298.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj2298.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj2298.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj2298.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('achieve_1stSegment', self.obj2298.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj2298.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj2298.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj2298.Graphical_Appearance.linkInfo.Center.setValue( ('achieve_Center', self.obj2298.Graphical_Appearance.linkInfo))
    self.obj2298.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj2298.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj2298.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj2298.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj2298.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj2298.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj2298.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj2298.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj2298.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj2298.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj2298.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj2298.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('achieve_2ndSegment', self.obj2298.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj2298.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj2298.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj2298.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj2298.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj2298.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj2298.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj2298.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj2298.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj2298.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj2298.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('achieve_2ndLink', self.obj2298.Graphical_Appearance.linkInfo.SecondLink))
    self.obj2298.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj2298.Graphical_Appearance.semObject
    self.obj2298.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj2298.Graphical_Appearance.semObject
    self.obj2298.Graphical_Appearance.linkInfo.Center.semObject=self.obj2298.Graphical_Appearance.semObject
    self.obj2298.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj2298.Graphical_Appearance.semObject
    self.obj2298.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj2298.Graphical_Appearance.semObject

    # name
    self.obj2298.name.setValue('achieve')

    # displaySelect
    self.obj2298.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj2298.displaySelect.config = 0

    # attributes
    self.obj2298.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj2298.attributes.setValue(lcobj2)

    # cardinality
    self.obj2298.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Goal', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj2298.cardinality.setValue(lcobj2)

    # display
    self.obj2298.display.setValue('Multiplicities:\n  - To Goal: 0 to N\n  - From Role: 0 to N\n')
    self.obj2298.display.setHeight(15)

    # Actions
    self.obj2298.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj2298.Actions.setValue(lcobj2)

    # Constraints
    self.obj2298.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj2298.Constraints.setValue(lcobj2)

    self.obj2298.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(386.080078125,476.0,self.obj2298)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2298.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2298)
    self.globalAndLocalPostcondition(self.obj2298, rootNode)
    self.obj2298.postAction( rootNode.CREATE )

    # Connections for obj2291 (graphObject_: Obj1162) named Agent
    self.drawConnections(
(self.obj2291,self.obj2295,[211.0, 94.92131147540987, 385.0, 89.0],"true", 2),
(self.obj2291,self.obj2296,[136.0, 173.0, 121.78125, 281.0],"true", 2) )
    # Connections for obj2292 (graphObject_: Obj1163) named Capabilitie
    self.drawConnections(
 )
    # Connections for obj2293 (graphObject_: Obj1164) named Role
    self.drawConnections(
(self.obj2293,self.obj2297,[212.81640625, 444.55737704918033, 394.578125, 291.0],"true", 2),
(self.obj2293,self.obj2298,[212.81640625, 474.9213114754098, 386.080078125, 476.0],"true", 2) )
    # Connections for obj2294 (graphObject_: Obj1165) named Goal
    self.drawConnections(
 )
    # Connections for obj2295 (graphObject_: Obj1166) named posses
    self.drawConnections(
(self.obj2295,self.obj2292,[385.0, 89.0, 541.0, 89.0],"true", 2) )
    # Connections for obj2296 (graphObject_: Obj1168) named CapableOf
    self.drawConnections(
(self.obj2296,self.obj2293,[121.78125, 281.0, 136.9375, 401.1803278688525],"true", 2) )
    # Connections for obj2297 (graphObject_: Obj1170) named require
    self.drawConnections(
(self.obj2297,self.obj2292,[394.578125, 291.0, 541.0, 141.0],"true", 2) )
    # Connections for obj2298 (graphObject_: Obj1172) named achieve
    self.drawConnections(
(self.obj2298,self.obj2294,[386.080078125, 476.0, 561.0, 469.0],"true", 2) )

newfunction = omacs_MDL

loadedMMName = 'CD_ClassDiagramsV3_META'

atom3version = '0.3'
