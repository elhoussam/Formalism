"""
__pns2_META.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: sam
Modified: Sun Jan 29 10:03:51 2017
___________________________________________________________________
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

def pns2_META(self, rootNode, ButtonsRootNode=None):

    # --- Generating attributes code for ASG Buttons ---
    if( ButtonsRootNode ): 
        # RowSize
        ButtonsRootNode.RowSize.setValue(4)

        # Formalism_File
        ButtonsRootNode.Formalism_File.setValue('pns2_MM.py')

        # Formalism_Name
        ButtonsRootNode.Formalism_Name.setValue('pns2_META')
    # --- ASG attributes over ---


    self.obj21=ButtonConfig(self)
    self.obj21.isGraphObjectVisual = True

    if(hasattr(self.obj21, '_setHierarchicalLink')):
      self.obj21._setHierarchicalLink(False)

    # Action
    self.obj21.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nself.modelAttributes(self.ASGroot.getASGbyName("pns2_META")) '))

    # Drawing_Mode
    self.obj21.Drawing_Mode.setValue((' ', 0))
    self.obj21.Drawing_Mode.config = 0

    # Contents
    self.obj21.Contents.Text.setValue('Edit')
    self.obj21.Contents.Image.setValue('pns2/icons/btnE.gif')
    self.obj21.Contents.lastSelected= "Image"

    self.obj21.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(135,10,self.obj21)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21)
    self.globalAndLocalPostcondition(self.obj21, rootNode)
    self.obj21.postAction( rootNode.CREATE )

    self.obj22=ButtonConfig(self)
    self.obj22.isGraphObjectVisual = True

    if(hasattr(self.obj22, '_setHierarchicalLink')):
      self.obj22._setHierarchicalLink(False)

    # Action
    self.obj22.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nfrom HelpDialog import HelpDialog\nHelpDialog(["pns2_METAHelp.txt"])\n '))

    # Drawing_Mode
    self.obj22.Drawing_Mode.setValue((' ', 0))
    self.obj22.Drawing_Mode.config = 0

    # Contents
    self.obj22.Contents.Text.setValue('Help')
    self.obj22.Contents.Image.setValue('pns2/icons/btn?.gif')
    self.obj22.Contents.lastSelected= "Image"

    self.obj22.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(135,80,self.obj22)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj22.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj22)
    self.globalAndLocalPostcondition(self.obj22, rootNode)
    self.obj22.postAction( rootNode.CREATE )

    self.obj23=ButtonConfig(self)
    self.obj23.isGraphObjectVisual = True

    if(hasattr(self.obj23, '_setHierarchicalLink')):
      self.obj23._setHierarchicalLink(False)

    # Action
    self.obj23.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewrawMaterial (self, wherex, wherey)\n'))

    # Drawing_Mode
    self.obj23.Drawing_Mode.setValue((' ', 1))
    self.obj23.Drawing_Mode.config = 0

    # Contents
    self.obj23.Contents.Text.setValue('New rawMaterial')
    self.obj23.Contents.Image.setValue('pns2/icons/d.gif')
    self.obj23.Contents.lastSelected= "Image"

    self.obj23.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(260,150,self.obj23)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj23.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj23)
    self.globalAndLocalPostcondition(self.obj23, rootNode)
    self.obj23.postAction( rootNode.CREATE )

    self.obj24=ButtonConfig(self)
    self.obj24.isGraphObjectVisual = True

    if(hasattr(self.obj24, '_setHierarchicalLink')):
      self.obj24._setHierarchicalLink(False)

    # Action
    self.obj24.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewproduct (self, wherex, wherey)\n'))

    # Drawing_Mode
    self.obj24.Drawing_Mode.setValue((' ', 1))
    self.obj24.Drawing_Mode.config = 0

    # Contents
    self.obj24.Contents.Text.setValue('New product')
    self.obj24.Contents.Image.setValue('pns2/icons/p.gif')
    self.obj24.Contents.lastSelected= "Image"

    self.obj24.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(10,10,self.obj24)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj24.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj24)
    self.globalAndLocalPostcondition(self.obj24, rootNode)
    self.obj24.postAction( rootNode.CREATE )

    self.obj25=ButtonConfig(self)
    self.obj25.isGraphObjectVisual = True

    if(hasattr(self.obj25, '_setHierarchicalLink')):
      self.obj25._setHierarchicalLink(False)

    # Action
    self.obj25.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewmetarial (self, wherex, wherey)\n'))

    # Drawing_Mode
    self.obj25.Drawing_Mode.setValue((' ', 1))
    self.obj25.Drawing_Mode.config = 0

    # Contents
    self.obj25.Contents.Text.setValue('New metarial')
    self.obj25.Contents.Image.setValue('pns2/icons/m.gif')
    self.obj25.Contents.lastSelected= "Image"

    self.obj25.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(135,146,self.obj25)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj25.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj25)
    self.globalAndLocalPostcondition(self.obj25, rootNode)
    self.obj25.postAction( rootNode.CREATE )

    self.obj26=ButtonConfig(self)
    self.obj26.isGraphObjectVisual = True

    if(hasattr(self.obj26, '_setHierarchicalLink')):
      self.obj26._setHierarchicalLink(False)

    # Action
    self.obj26.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewoperatingUnit (self, wherex, wherey)\n'))

    # Drawing_Mode
    self.obj26.Drawing_Mode.setValue((' ', 1))
    self.obj26.Drawing_Mode.config = 0

    # Contents
    self.obj26.Contents.Text.setValue('pns2/icons/btnT.gif')
    self.obj26.Contents.Image.setValue('pns2/icons/btnT.gif')
    self.obj26.Contents.lastSelected= "Image"

    self.obj26.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(260,212,self.obj26)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj26.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj26)
    self.globalAndLocalPostcondition(self.obj26, rootNode)
    self.obj26.postAction( rootNode.CREATE )

    # Connections for obj21 (graphObject_: Obj0) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj22 (graphObject_: Obj1) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj23 (graphObject_: Obj2) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj24 (graphObject_: Obj3) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj25 (graphObject_: Obj4) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj26 (graphObject_: Obj5) of type ButtonConfig
    self.drawConnections(
 )

newfunction = pns2_META

loadedMMName = 'Buttons'

atom3version = '0.3'
