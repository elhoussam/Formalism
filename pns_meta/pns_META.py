"""
__pns_META.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: sam
Modified: Fri Mar 31 16:05:25 2017
__________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from ButtonConfig import *
from graph_ButtonConfig import *
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

def pns_META(self, rootNode, ButtonsRootNode=None):

    # --- Generating attributes code for ASG Buttons ---
    if( ButtonsRootNode ): 
        # RowSize
        ButtonsRootNode.RowSize.setValue(4)

        # Formalism_File
        ButtonsRootNode.Formalism_File.setValue('pns_MM.py')

        # Formalism_Name
        ButtonsRootNode.Formalism_Name.setValue('pns_META')
    # --- ASG attributes over ---


    self.obj29=ButtonConfig(self)
    self.obj29.isGraphObjectVisual = True

    if(hasattr(self.obj29, '_setHierarchicalLink')):
      self.obj29._setHierarchicalLink(False)

    # Action
    self.obj29.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nself.modelAttributes(self.ASGroot.getASGbyName("pns_META")) '))

    # Drawing_Mode
    self.obj29.Drawing_Mode.setValue((' ', 0))
    self.obj29.Drawing_Mode.config = 0

    # Contents
    self.obj29.Contents.Text.setValue('Edit')
    self.obj29.Contents.Image.setValue('pns_meta/icons/btnE.gif')
    self.obj29.Contents.lastSelected= "Image"

    self.obj29.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(10,10,self.obj29)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj29.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj29)
    self.globalAndLocalPostcondition(self.obj29, rootNode)
    self.obj29.postAction( rootNode.CREATE )

    self.obj30=ButtonConfig(self)
    self.obj30.isGraphObjectVisual = True

    if(hasattr(self.obj30, '_setHierarchicalLink')):
      self.obj30._setHierarchicalLink(False)

    # Action
    self.obj30.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nfrom HelpDialog import HelpDialog\nHelpDialog(["pns_METAHelp.txt"])\n '))

    # Drawing_Mode
    self.obj30.Drawing_Mode.setValue((' ', 0))
    self.obj30.Drawing_Mode.config = 0

    # Contents
    self.obj30.Contents.Text.setValue('Help')
    self.obj30.Contents.Image.setValue('pns_meta/icons/btn?.gif')
    self.obj30.Contents.lastSelected= "Image"

    self.obj30.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(135,80,self.obj30)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj30.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj30)
    self.globalAndLocalPostcondition(self.obj30, rootNode)
    self.obj30.postAction( rootNode.CREATE )

    self.obj31=ButtonConfig(self)
    self.obj31.isGraphObjectVisual = True

    if(hasattr(self.obj31, '_setHierarchicalLink')):
      self.obj31._setHierarchicalLink(False)

    # Action
    self.obj31.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewrawMaterial (self, wherex, wherey)\n'))

    # Drawing_Mode
    self.obj31.Drawing_Mode.setValue((' ', 1))
    self.obj31.Drawing_Mode.config = 0

    # Contents
    self.obj31.Contents.Text.setValue('New rawMaterial')
    self.obj31.Contents.Image.setValue('pns_meta/icons/d.gif')
    self.obj31.Contents.lastSelected= "Image"

    self.obj31.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(260,150,self.obj31)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj31.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31)
    self.globalAndLocalPostcondition(self.obj31, rootNode)
    self.obj31.postAction( rootNode.CREATE )

    self.obj32=ButtonConfig(self)
    self.obj32.isGraphObjectVisual = True

    if(hasattr(self.obj32, '_setHierarchicalLink')):
      self.obj32._setHierarchicalLink(False)

    # Action
    self.obj32.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewproduct (self, wherex, wherey)\n'))

    # Drawing_Mode
    self.obj32.Drawing_Mode.setValue((' ', 1))
    self.obj32.Drawing_Mode.config = 0

    # Contents
    self.obj32.Contents.Text.setValue('New product')
    self.obj32.Contents.Image.setValue('pns_meta/icons/p.gif')
    self.obj32.Contents.lastSelected= "Image"

    self.obj32.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(160.0,20.0,self.obj32)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj32.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj32)
    self.globalAndLocalPostcondition(self.obj32, rootNode)
    self.obj32.postAction( rootNode.CREATE )

    self.obj33=ButtonConfig(self)
    self.obj33.isGraphObjectVisual = True

    if(hasattr(self.obj33, '_setHierarchicalLink')):
      self.obj33._setHierarchicalLink(False)

    # Action
    self.obj33.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewmetarial (self, wherex, wherey)\n'))

    # Drawing_Mode
    self.obj33.Drawing_Mode.setValue((' ', 1))
    self.obj33.Drawing_Mode.config = 0

    # Contents
    self.obj33.Contents.Text.setValue('New metarial')
    self.obj33.Contents.Image.setValue('pns_meta/icons/m.gif')
    self.obj33.Contents.lastSelected= "Image"

    self.obj33.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(320.0,80.0,self.obj33)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj33.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj33)
    self.globalAndLocalPostcondition(self.obj33, rootNode)
    self.obj33.postAction( rootNode.CREATE )

    self.obj34=ButtonConfig(self)
    self.obj34.isGraphObjectVisual = True

    if(hasattr(self.obj34, '_setHierarchicalLink')):
      self.obj34._setHierarchicalLink(False)

    # Action
    self.obj34.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewoperatingUnit (self, wherex, wherey)\n'))

    # Drawing_Mode
    self.obj34.Drawing_Mode.setValue((' ', 1))
    self.obj34.Drawing_Mode.config = 0

    # Contents
    self.obj34.Contents.Text.setValue('New operatingUnit')
    self.obj34.Contents.Image.setValue('pns_meta/icons/btnT.gif')
    self.obj34.Contents.lastSelected= "Image"

    self.obj34.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(80.0,140.0,self.obj34)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj34.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj34)
    self.globalAndLocalPostcondition(self.obj34, rootNode)
    self.obj34.postAction( rootNode.CREATE )

    # Connections for obj29 (graphObject_: Obj0) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj30 (graphObject_: Obj1) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj31 (graphObject_: Obj2) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj32 (graphObject_: Obj3) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj33 (graphObject_: Obj4) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj34 (graphObject_: Obj5) of type ButtonConfig
    self.drawConnections(
 )

newfunction = pns_META

loadedMMName = 'Buttons'

atom3version = '0.3'
