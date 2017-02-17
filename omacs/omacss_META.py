"""
__omacss_META.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: sam
Modified: Wed Feb 15 11:03:03 2017
_____________________________________________________________________
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

def omacss_META(self, rootNode, ButtonsRootNode=None):

    # --- Generating attributes code for ASG Buttons ---
    if( ButtonsRootNode ): 
        # RowSize
        ButtonsRootNode.RowSize.setValue(4)

        # Formalism_File
        ButtonsRootNode.Formalism_File.setValue('omacss_MM.py')

        # Formalism_Name
        ButtonsRootNode.Formalism_Name.setValue('omacss_META')
    # --- ASG attributes over ---


    self.obj40=ButtonConfig(self)
    self.obj40.isGraphObjectVisual = True

    if(hasattr(self.obj40, '_setHierarchicalLink')):
      self.obj40._setHierarchicalLink(False)

    # Action
    self.obj40.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nself.modelAttributes(self.ASGroot.getASGbyName("omacss_META")) '))

    # Drawing_Mode
    self.obj40.Drawing_Mode.setValue((' ', 0))
    self.obj40.Drawing_Mode.config = 0

    # Contents
    self.obj40.Contents.Text.setValue('Edit')
    self.obj40.Contents.Image.setValue('omacs/icons/btnE.gif')
    self.obj40.Contents.lastSelected= "Image"

    self.obj40.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(10,10,self.obj40)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj40.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj40)
    self.globalAndLocalPostcondition(self.obj40, rootNode)
    self.obj40.postAction( rootNode.CREATE )

    self.obj41=ButtonConfig(self)
    self.obj41.isGraphObjectVisual = True

    if(hasattr(self.obj41, '_setHierarchicalLink')):
      self.obj41._setHierarchicalLink(False)

    # Action
    self.obj41.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nfrom HelpDialog import HelpDialog\nHelpDialog(["omacss_METAHelp.txt"])\n '))

    # Drawing_Mode
    self.obj41.Drawing_Mode.setValue((' ', 0))
    self.obj41.Drawing_Mode.config = 0

    # Contents
    self.obj41.Contents.Text.setValue('Help')
    self.obj41.Contents.Image.setValue('omacs/icons/btn?.gif')
    self.obj41.Contents.lastSelected= "Image"

    self.obj41.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(135,80,self.obj41)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj41.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj41)
    self.globalAndLocalPostcondition(self.obj41, rootNode)
    self.obj41.postAction( rootNode.CREATE )

    self.obj42=ButtonConfig(self)
    self.obj42.isGraphObjectVisual = True

    if(hasattr(self.obj42, '_setHierarchicalLink')):
      self.obj42._setHierarchicalLink(False)

    # Action
    self.obj42.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewAgent (self, wherex, wherey)\n'))

    # Drawing_Mode
    self.obj42.Drawing_Mode.setValue((' ', 1))
    self.obj42.Drawing_Mode.config = 0

    # Contents
    self.obj42.Contents.Text.setValue('New Agent')
    self.obj42.Contents.Image.setValue('omacs/icons/aa.gif')
    self.obj42.Contents.lastSelected= "Image"

    self.obj42.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(275,150,self.obj42)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj42.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42)
    self.globalAndLocalPostcondition(self.obj42, rootNode)
    self.obj42.postAction( rootNode.CREATE )

    self.obj43=ButtonConfig(self)
    self.obj43.isGraphObjectVisual = True

    if(hasattr(self.obj43, '_setHierarchicalLink')):
      self.obj43._setHierarchicalLink(False)

    # Action
    self.obj43.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewCapabilitie (self, wherex, wherey)\n'))

    # Drawing_Mode
    self.obj43.Drawing_Mode.setValue((' ', 1))
    self.obj43.Drawing_Mode.config = 0

    # Contents
    self.obj43.Contents.Text.setValue('New Capabilitie')
    self.obj43.Contents.Image.setValue('omacs/icons/cc.gif')
    self.obj43.Contents.lastSelected= "Image"

    self.obj43.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(160.0,20.0,self.obj43)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj43.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj43)
    self.globalAndLocalPostcondition(self.obj43, rootNode)
    self.obj43.postAction( rootNode.CREATE )

    self.obj44=ButtonConfig(self)
    self.obj44.isGraphObjectVisual = True

    if(hasattr(self.obj44, '_setHierarchicalLink')):
      self.obj44._setHierarchicalLink(False)

    # Action
    self.obj44.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewRole (self, wherex, wherey)\n'))

    # Drawing_Mode
    self.obj44.Drawing_Mode.setValue((' ', 1))
    self.obj44.Drawing_Mode.config = 0

    # Contents
    self.obj44.Contents.Text.setValue('New Role')
    self.obj44.Contents.Image.setValue('omacs/icons/rr.gif')
    self.obj44.Contents.lastSelected= "Image"

    self.obj44.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(140.0,180.0,self.obj44)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj44.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj44)
    self.globalAndLocalPostcondition(self.obj44, rootNode)
    self.obj44.postAction( rootNode.CREATE )

    self.obj45=ButtonConfig(self)
    self.obj45.isGraphObjectVisual = True

    if(hasattr(self.obj45, '_setHierarchicalLink')):
      self.obj45._setHierarchicalLink(False)

    # Action
    self.obj45.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewGoal (self, wherex, wherey)\n'))

    # Drawing_Mode
    self.obj45.Drawing_Mode.setValue((' ', 1))
    self.obj45.Drawing_Mode.config = 0

    # Contents
    self.obj45.Contents.Text.setValue('New Goal')
    self.obj45.Contents.Image.setValue('omacs/icons/gg.gif')
    self.obj45.Contents.lastSelected= "Image"

    self.obj45.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(400.0,140.0,self.obj45)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj45.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj45)
    self.globalAndLocalPostcondition(self.obj45, rootNode)
    self.obj45.postAction( rootNode.CREATE )

    # Connections for obj40 (graphObject_: Obj12) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj41 (graphObject_: Obj13) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj42 (graphObject_: Obj14) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj43 (graphObject_: Obj15) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj44 (graphObject_: Obj16) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj45 (graphObject_: Obj17) of type ButtonConfig
    self.drawConnections(
 )

newfunction = omacss_META

loadedMMName = 'Buttons'

atom3version = '0.3'
