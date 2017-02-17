"""
__omacsMODEL2_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: sam
Modified: Fri Feb 17 14:56:11 2017
_________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from Agent import *
from Capabilitie import *
from Role import *
from Goal import *
from posses import *
from achieve import *
from requir import *
from operatingUnit import *
from metarial import *
from fromMaterial import *
from intoMaterial import *
from graph_posses import *
from graph_operatingUnit import *
from graph_achieve import *
from graph_Goal import *
from graph_Agent import *
from graph_Capabilitie import *
from graph_intoMaterial import *
from graph_metarial import *
from graph_requir import *
from graph_fromMaterial import *
from graph_Role import *
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

def omacsMODEL2_MDL(self, rootNode, omacssRootNode=None, pns2RootNode=None):

    # --- Generating attributes code for ASG omacss ---
    if( omacssRootNode ): 
        # author
        omacssRootNode.author.setValue('Houssam Sam')

        # description
        omacssRootNode.description.setValue('\n')
        omacssRootNode.description.setHeight(15)

        # name
        omacssRootNode.name.setValue('modelOMACS1')
    # --- ASG attributes over ---


    # --- Generating attributes code for ASG pns2 ---
    if( pns2RootNode ): 
        # author
        pns2RootNode.author.setValue('Annonymous')

        # description
        pns2RootNode.description.setValue('\n')
        pns2RootNode.description.setHeight(15)

        # name
        pns2RootNode.name.setValue('')
        pns2RootNode.name.setNone()
    # --- ASG attributes over ---


    self.obj468=Agent(self)
    self.obj468.isGraphObjectVisual = True

    if(hasattr(self.obj468, '_setHierarchicalLink')):
      self.obj468._setHierarchicalLink(False)

    # price
    self.obj468.price.setValue(0)

    # name
    self.obj468.name.setValue('a1')

    self.obj468.graphClass_= graph_Agent
    if self.genGraphics:
       new_obj = graph_Agent(140.0,60.0,self.obj468)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Agent", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj468.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj468)
    self.globalAndLocalPostcondition(self.obj468, rootNode)
    self.obj468.postAction( rootNode.CREATE )

    self.obj469=Agent(self)
    self.obj469.isGraphObjectVisual = True

    if(hasattr(self.obj469, '_setHierarchicalLink')):
      self.obj469._setHierarchicalLink(False)

    # price
    self.obj469.price.setValue(0)

    # name
    self.obj469.name.setValue('a2')

    self.obj469.graphClass_= graph_Agent
    if self.genGraphics:
       new_obj = graph_Agent(320.0,40.0,self.obj469)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Agent", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj469.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj469)
    self.globalAndLocalPostcondition(self.obj469, rootNode)
    self.obj469.postAction( rootNode.CREATE )

    self.obj470=Agent(self)
    self.obj470.isGraphObjectVisual = True

    if(hasattr(self.obj470, '_setHierarchicalLink')):
      self.obj470._setHierarchicalLink(False)

    # price
    self.obj470.price.setValue(0)

    # name
    self.obj470.name.setValue('a3')

    self.obj470.graphClass_= graph_Agent
    if self.genGraphics:
       new_obj = graph_Agent(520.0,60.0,self.obj470)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Agent", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj470.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj470)
    self.globalAndLocalPostcondition(self.obj470, rootNode)
    self.obj470.postAction( rootNode.CREATE )

    self.obj471=Capabilitie(self)
    self.obj471.isGraphObjectVisual = True

    if(hasattr(self.obj471, '_setHierarchicalLink')):
      self.obj471._setHierarchicalLink(False)

    # name
    self.obj471.name.setValue('C1')

    self.obj471.graphClass_= graph_Capabilitie
    if self.genGraphics:
       new_obj = graph_Capabilitie(120.0,220.0,self.obj471)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Capabilitie", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj471.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj471)
    self.globalAndLocalPostcondition(self.obj471, rootNode)
    self.obj471.postAction( rootNode.CREATE )

    self.obj472=Capabilitie(self)
    self.obj472.isGraphObjectVisual = True

    if(hasattr(self.obj472, '_setHierarchicalLink')):
      self.obj472._setHierarchicalLink(False)

    # name
    self.obj472.name.setValue('C2')

    self.obj472.graphClass_= graph_Capabilitie
    if self.genGraphics:
       new_obj = graph_Capabilitie(240.0,220.0,self.obj472)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Capabilitie", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj472.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj472)
    self.globalAndLocalPostcondition(self.obj472, rootNode)
    self.obj472.postAction( rootNode.CREATE )

    self.obj473=Capabilitie(self)
    self.obj473.isGraphObjectVisual = True

    if(hasattr(self.obj473, '_setHierarchicalLink')):
      self.obj473._setHierarchicalLink(False)

    # name
    self.obj473.name.setValue('C3')

    self.obj473.graphClass_= graph_Capabilitie
    if self.genGraphics:
       new_obj = graph_Capabilitie(400.0,220.0,self.obj473)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Capabilitie", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj473.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj473)
    self.globalAndLocalPostcondition(self.obj473, rootNode)
    self.obj473.postAction( rootNode.CREATE )

    self.obj474=Capabilitie(self)
    self.obj474.isGraphObjectVisual = True

    if(hasattr(self.obj474, '_setHierarchicalLink')):
      self.obj474._setHierarchicalLink(False)

    # name
    self.obj474.name.setValue('C4')

    self.obj474.graphClass_= graph_Capabilitie
    if self.genGraphics:
       new_obj = graph_Capabilitie(520.0,220.0,self.obj474)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Capabilitie", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj474.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj474)
    self.globalAndLocalPostcondition(self.obj474, rootNode)
    self.obj474.postAction( rootNode.CREATE )

    self.obj475=Role(self)
    self.obj475.isGraphObjectVisual = True

    if(hasattr(self.obj475, '_setHierarchicalLink')):
      self.obj475._setHierarchicalLink(False)

    # name
    self.obj475.name.setValue('R1')

    self.obj475.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(220.0,340.0,self.obj475)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj475.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj475)
    self.globalAndLocalPostcondition(self.obj475, rootNode)
    self.obj475.postAction( rootNode.CREATE )

    self.obj476=Role(self)
    self.obj476.isGraphObjectVisual = True

    if(hasattr(self.obj476, '_setHierarchicalLink')):
      self.obj476._setHierarchicalLink(False)

    # name
    self.obj476.name.setValue('R2')

    self.obj476.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(420.0,360.0,self.obj476)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj476.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj476)
    self.globalAndLocalPostcondition(self.obj476, rootNode)
    self.obj476.postAction( rootNode.CREATE )

    self.obj477=Goal(self)
    self.obj477.isGraphObjectVisual = True

    if(hasattr(self.obj477, '_setHierarchicalLink')):
      self.obj477._setHierarchicalLink(False)

    # name
    self.obj477.name.setValue('G2')

    self.obj477.graphClass_= graph_Goal
    if self.genGraphics:
       new_obj = graph_Goal(280.0,500.0,self.obj477)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Goal", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj477.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj477)
    self.globalAndLocalPostcondition(self.obj477, rootNode)
    self.obj477.postAction( rootNode.CREATE )

    self.obj478=Goal(self)
    self.obj478.isGraphObjectVisual = True

    if(hasattr(self.obj478, '_setHierarchicalLink')):
      self.obj478._setHierarchicalLink(False)

    # name
    self.obj478.name.setValue('G3')

    self.obj478.graphClass_= graph_Goal
    if self.genGraphics:
       new_obj = graph_Goal(460.0,480.0,self.obj478)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Goal", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj478.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj478)
    self.globalAndLocalPostcondition(self.obj478, rootNode)
    self.obj478.postAction( rootNode.CREATE )

    self.obj479=Goal(self)
    self.obj479.isGraphObjectVisual = True

    if(hasattr(self.obj479, '_setHierarchicalLink')):
      self.obj479._setHierarchicalLink(False)

    # name
    self.obj479.name.setValue('G4')

    self.obj479.graphClass_= graph_Goal
    if self.genGraphics:
       new_obj = graph_Goal(580.0,460.0,self.obj479)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Goal", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj479.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj479)
    self.globalAndLocalPostcondition(self.obj479, rootNode)
    self.obj479.postAction( rootNode.CREATE )

    self.obj480=Goal(self)
    self.obj480.isGraphObjectVisual = True

    if(hasattr(self.obj480, '_setHierarchicalLink')):
      self.obj480._setHierarchicalLink(False)

    # name
    self.obj480.name.setValue('G1')

    self.obj480.graphClass_= graph_Goal
    if self.genGraphics:
       new_obj = graph_Goal(140.0,480.0,self.obj480)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Goal", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj480.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj480)
    self.globalAndLocalPostcondition(self.obj480, rootNode)
    self.obj480.postAction( rootNode.CREATE )

    self.obj482=posses(self)
    self.obj482.isGraphObjectVisual = True

    if(hasattr(self.obj482, '_setHierarchicalLink')):
      self.obj482._setHierarchicalLink(False)

    # rate
    self.obj482.rate.setValue(0.0)

    self.obj482.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(303.0,160.5,self.obj482)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj482.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj482)
    self.globalAndLocalPostcondition(self.obj482, rootNode)
    self.obj482.postAction( rootNode.CREATE )

    self.obj483=posses(self)
    self.obj483.isGraphObjectVisual = True

    if(hasattr(self.obj483, '_setHierarchicalLink')):
      self.obj483._setHierarchicalLink(False)

    # rate
    self.obj483.rate.setValue(0.0)

    self.obj483.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(383.0,160.5,self.obj483)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj483.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj483)
    self.globalAndLocalPostcondition(self.obj483, rootNode)
    self.obj483.postAction( rootNode.CREATE )

    self.obj484=posses(self)
    self.obj484.isGraphObjectVisual = True

    if(hasattr(self.obj484, '_setHierarchicalLink')):
      self.obj484._setHierarchicalLink(False)

    # rate
    self.obj484.rate.setValue(0.0)

    self.obj484.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(483.0,170.5,self.obj484)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj484.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj484)
    self.globalAndLocalPostcondition(self.obj484, rootNode)
    self.obj484.postAction( rootNode.CREATE )

    self.obj485=posses(self)
    self.obj485.isGraphObjectVisual = True

    if(hasattr(self.obj485, '_setHierarchicalLink')):
      self.obj485._setHierarchicalLink(False)

    # rate
    self.obj485.rate.setValue(0.0)

    self.obj485.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(403.0,170.5,self.obj485)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj485.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj485)
    self.globalAndLocalPostcondition(self.obj485, rootNode)
    self.obj485.postAction( rootNode.CREATE )

    self.obj486=posses(self)
    self.obj486.isGraphObjectVisual = True

    if(hasattr(self.obj486, '_setHierarchicalLink')):
      self.obj486._setHierarchicalLink(False)

    # rate
    self.obj486.rate.setValue(0.0)

    self.obj486.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(543.0,170.5,self.obj486)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj486.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj486)
    self.globalAndLocalPostcondition(self.obj486, rootNode)
    self.obj486.postAction( rootNode.CREATE )

    self.obj488=posses(self)
    self.obj488.isGraphObjectVisual = True

    if(hasattr(self.obj488, '_setHierarchicalLink')):
      self.obj488._setHierarchicalLink(False)

    # rate
    self.obj488.rate.setValue(0.0)

    self.obj488.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(153.0,170.5,self.obj488)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj488.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj488)
    self.globalAndLocalPostcondition(self.obj488, rootNode)
    self.obj488.postAction( rootNode.CREATE )

    self.obj489=posses(self)
    self.obj489.isGraphObjectVisual = True

    if(hasattr(self.obj489, '_setHierarchicalLink')):
      self.obj489._setHierarchicalLink(False)

    # rate
    self.obj489.rate.setValue(0.0)

    self.obj489.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(213.0,170.5,self.obj489)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj489.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj489)
    self.globalAndLocalPostcondition(self.obj489, rootNode)
    self.obj489.postAction( rootNode.CREATE )

    self.obj490=posses(self)
    self.obj490.isGraphObjectVisual = True

    if(hasattr(self.obj490, '_setHierarchicalLink')):
      self.obj490._setHierarchicalLink(False)

    # rate
    self.obj490.rate.setValue(0.0)

    self.obj490.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(293.0,170.5,self.obj490)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj490.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj490)
    self.globalAndLocalPostcondition(self.obj490, rootNode)
    self.obj490.postAction( rootNode.CREATE )

    self.obj526=posses(self)
    self.obj526.isGraphObjectVisual = True

    if(hasattr(self.obj526, '_setHierarchicalLink')):
      self.obj526._setHierarchicalLink(False)

    # rate
    self.obj526.rate.setValue(0.0)

    self.obj526.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(353.0,170.5,self.obj526)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj526.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj526)
    self.globalAndLocalPostcondition(self.obj526, rootNode)
    self.obj526.postAction( rootNode.CREATE )

    self.obj531=posses(self)
    self.obj531.isGraphObjectVisual = True

    if(hasattr(self.obj531, '_setHierarchicalLink')):
      self.obj531._setHierarchicalLink(False)

    # rate
    self.obj531.rate.setValue(0.0)

    self.obj531.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(443.0,160.5,self.obj531)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj531.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj531)
    self.globalAndLocalPostcondition(self.obj531, rootNode)
    self.obj531.postAction( rootNode.CREATE )

    self.obj491=achieve(self)
    self.obj491.isGraphObjectVisual = True

    if(hasattr(self.obj491, '_setHierarchicalLink')):
      self.obj491._setHierarchicalLink(False)

    # rate
    self.obj491.rate.setValue(0.0)

    self.obj491.graphClass_= graph_achieve
    if self.genGraphics:
       new_obj = graph_achieve(176.5,409.5,self.obj491)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("achieve", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj491.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj491)
    self.globalAndLocalPostcondition(self.obj491, rootNode)
    self.obj491.postAction( rootNode.CREATE )

    self.obj492=achieve(self)
    self.obj492.isGraphObjectVisual = True

    if(hasattr(self.obj492, '_setHierarchicalLink')):
      self.obj492._setHierarchicalLink(False)

    # rate
    self.obj492.rate.setValue(0.0)

    self.obj492.graphClass_= graph_achieve
    if self.genGraphics:
       new_obj = graph_achieve(244.5,466.5,self.obj492)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("achieve", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj492.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj492)
    self.globalAndLocalPostcondition(self.obj492, rootNode)
    self.obj492.postAction( rootNode.CREATE )

    self.obj493=achieve(self)
    self.obj493.isGraphObjectVisual = True

    if(hasattr(self.obj493, '_setHierarchicalLink')):
      self.obj493._setHierarchicalLink(False)

    # rate
    self.obj493.rate.setValue(0.0)

    self.obj493.graphClass_= graph_achieve
    if self.genGraphics:
       new_obj = graph_achieve(343.5,451.5,self.obj493)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("achieve", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj493.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj493)
    self.globalAndLocalPostcondition(self.obj493, rootNode)
    self.obj493.postAction( rootNode.CREATE )

    self.obj494=achieve(self)
    self.obj494.isGraphObjectVisual = True

    if(hasattr(self.obj494, '_setHierarchicalLink')):
      self.obj494._setHierarchicalLink(False)

    # rate
    self.obj494.rate.setValue(0.0)

    self.obj494.graphClass_= graph_achieve
    if self.genGraphics:
       new_obj = graph_achieve(385.5,415.5,self.obj494)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("achieve", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj494.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj494)
    self.globalAndLocalPostcondition(self.obj494, rootNode)
    self.obj494.postAction( rootNode.CREATE )

    self.obj495=achieve(self)
    self.obj495.isGraphObjectVisual = True

    if(hasattr(self.obj495, '_setHierarchicalLink')):
      self.obj495._setHierarchicalLink(False)

    # rate
    self.obj495.rate.setValue(0.0)

    self.obj495.graphClass_= graph_achieve
    if self.genGraphics:
       new_obj = graph_achieve(273.0,459.5,self.obj495)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("achieve", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj495.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj495)
    self.globalAndLocalPostcondition(self.obj495, rootNode)
    self.obj495.postAction( rootNode.CREATE )

    self.obj496=achieve(self)
    self.obj496.isGraphObjectVisual = True

    if(hasattr(self.obj496, '_setHierarchicalLink')):
      self.obj496._setHierarchicalLink(False)

    # rate
    self.obj496.rate.setValue(0.0)

    self.obj496.graphClass_= graph_achieve
    if self.genGraphics:
       new_obj = graph_achieve(384.5,447.5,self.obj496)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("achieve", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj496.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj496)
    self.globalAndLocalPostcondition(self.obj496, rootNode)
    self.obj496.postAction( rootNode.CREATE )

    self.obj497=achieve(self)
    self.obj497.isGraphObjectVisual = True

    if(hasattr(self.obj497, '_setHierarchicalLink')):
      self.obj497._setHierarchicalLink(False)

    # rate
    self.obj497.rate.setValue(0.0)

    self.obj497.graphClass_= graph_achieve
    if self.genGraphics:
       new_obj = graph_achieve(453.5,423.5,self.obj497)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("achieve", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj497.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj497)
    self.globalAndLocalPostcondition(self.obj497, rootNode)
    self.obj497.postAction( rootNode.CREATE )

    self.obj498=achieve(self)
    self.obj498.isGraphObjectVisual = True

    if(hasattr(self.obj498, '_setHierarchicalLink')):
      self.obj498._setHierarchicalLink(False)

    # rate
    self.obj498.rate.setValue(0.0)

    self.obj498.graphClass_= graph_achieve
    if self.genGraphics:
       new_obj = graph_achieve(493.5,413.5,self.obj498)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("achieve", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj498.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj498)
    self.globalAndLocalPostcondition(self.obj498, rootNode)
    self.obj498.postAction( rootNode.CREATE )

    self.obj499=requir(self)
    self.obj499.isGraphObjectVisual = True

    if(hasattr(self.obj499, '_setHierarchicalLink')):
      self.obj499._setHierarchicalLink(False)

    self.obj499.graphClass_= graph_requir
    if self.genGraphics:
       new_obj = graph_requir(432.5,310.0,self.obj499)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("requir", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj499.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj499)
    self.globalAndLocalPostcondition(self.obj499, rootNode)
    self.obj499.postAction( rootNode.CREATE )

    self.obj500=requir(self)
    self.obj500.isGraphObjectVisual = True

    if(hasattr(self.obj500, '_setHierarchicalLink')):
      self.obj500._setHierarchicalLink(False)

    self.obj500.graphClass_= graph_requir
    if self.genGraphics:
       new_obj = graph_requir(352.5,310.0,self.obj500)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("requir", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj500.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj500)
    self.globalAndLocalPostcondition(self.obj500, rootNode)
    self.obj500.postAction( rootNode.CREATE )

    self.obj501=requir(self)
    self.obj501.isGraphObjectVisual = True

    if(hasattr(self.obj501, '_setHierarchicalLink')):
      self.obj501._setHierarchicalLink(False)

    self.obj501.graphClass_= graph_requir
    if self.genGraphics:
       new_obj = graph_requir(492.5,310.0,self.obj501)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("requir", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj501.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj501)
    self.globalAndLocalPostcondition(self.obj501, rootNode)
    self.obj501.postAction( rootNode.CREATE )

    self.obj502=requir(self)
    self.obj502.isGraphObjectVisual = True

    if(hasattr(self.obj502, '_setHierarchicalLink')):
      self.obj502._setHierarchicalLink(False)

    self.obj502.graphClass_= graph_requir
    if self.genGraphics:
       new_obj = graph_requir(332.5,300.0,self.obj502)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("requir", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj502.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj502)
    self.globalAndLocalPostcondition(self.obj502, rootNode)
    self.obj502.postAction( rootNode.CREATE )

    self.obj503=requir(self)
    self.obj503.isGraphObjectVisual = True

    if(hasattr(self.obj503, '_setHierarchicalLink')):
      self.obj503._setHierarchicalLink(False)

    self.obj503.graphClass_= graph_requir
    if self.genGraphics:
       new_obj = graph_requir(252.5,300.0,self.obj503)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("requir", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj503.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj503)
    self.globalAndLocalPostcondition(self.obj503, rootNode)
    self.obj503.postAction( rootNode.CREATE )

    self.obj504=requir(self)
    self.obj504.isGraphObjectVisual = True

    if(hasattr(self.obj504, '_setHierarchicalLink')):
      self.obj504._setHierarchicalLink(False)

    self.obj504.graphClass_= graph_requir
    if self.genGraphics:
       new_obj = graph_requir(192.5,300.0,self.obj504)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("requir", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj504.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj504)
    self.globalAndLocalPostcondition(self.obj504, rootNode)
    self.obj504.postAction( rootNode.CREATE )

    self.obj528=operatingUnit(self)
    self.obj528.isGraphObjectVisual = True

    if(hasattr(self.obj528, '_setHierarchicalLink')):
      self.obj528._setHierarchicalLink(False)

    # name
    self.obj528.name.setValue('')
    self.obj528.name.setNone()

    self.obj528.graphClass_= graph_operatingUnit
    if self.genGraphics:
       new_obj = graph_operatingUnit(780.0,100.0,self.obj528)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("operatingUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj528.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj528)
    self.globalAndLocalPostcondition(self.obj528, rootNode)
    self.obj528.postAction( rootNode.CREATE )

    self.obj527=metarial(self)
    self.obj527.isGraphObjectVisual = True

    if(hasattr(self.obj527, '_setHierarchicalLink')):
      self.obj527._setHierarchicalLink(False)

    # Name
    self.obj527.Name.setValue('')
    self.obj527.Name.setNone()

    self.obj527.graphClass_= graph_metarial
    if self.genGraphics:
       new_obj = graph_metarial(840.0,160.0,self.obj527)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("metarial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj527.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj527)
    self.globalAndLocalPostcondition(self.obj527, rootNode)
    self.obj527.postAction( rootNode.CREATE )

    self.obj530=fromMaterial(self)
    self.obj530.isGraphObjectVisual = True

    if(hasattr(self.obj530, '_setHierarchicalLink')):
      self.obj530._setHierarchicalLink(False)

    # rate
    self.obj530.rate.setValue(0.0)

    self.obj530.graphClass_= graph_fromMaterial
    if self.genGraphics:
       new_obj = graph_fromMaterial(834.5,86.0,self.obj530)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("fromMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj530.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj530)
    self.globalAndLocalPostcondition(self.obj530, rootNode)
    self.obj530.postAction( rootNode.CREATE )

    self.obj529=intoMaterial(self)
    self.obj529.isGraphObjectVisual = True

    if(hasattr(self.obj529, '_setHierarchicalLink')):
      self.obj529._setHierarchicalLink(False)

    # rate
    self.obj529.rate.setValue(0.0)

    self.obj529.graphClass_= graph_intoMaterial
    if self.genGraphics:
       new_obj = graph_intoMaterial(837.897196262,140.5,self.obj529)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("intoMaterial", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj529.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj529)
    self.globalAndLocalPostcondition(self.obj529, rootNode)
    self.obj529.postAction( rootNode.CREATE )

    # Connections for obj468 (graphObject_: Obj452) named a1
    self.drawConnections(
(self.obj468,self.obj488,[165.0, 122.0, 153.0, 170.5],"true", 2),
(self.obj468,self.obj489,[165.0, 122.0, 213.0, 170.5],"true", 2),
(self.obj468,self.obj490,[165.0, 122.0, 293.0, 170.5],"true", 2),
(self.obj468,self.obj526,[165.0, 122.0, 353.0, 170.5],"true", 2) )
    # Connections for obj469 (graphObject_: Obj453) named a2
    self.drawConnections(
(self.obj469,self.obj482,[345.0, 102.0, 303.0, 160.5],"true", 2),
(self.obj469,self.obj483,[345.0, 102.0, 383.0, 160.5],"true", 2),
(self.obj469,self.obj531,[345.0, 102.0, 443.0, 160.5],"true", 2) )
    # Connections for obj470 (graphObject_: Obj454) named a3
    self.drawConnections(
(self.obj470,self.obj484,[545.0, 122.0, 483.0, 170.5],"true", 2),
(self.obj470,self.obj485,[545.0, 122.0, 403.0, 170.5],"true", 2),
(self.obj470,self.obj486,[545.0, 122.0, 543.0, 170.5],"true", 2) )
    # Connections for obj471 (graphObject_: Obj455) named C1
    self.drawConnections(
 )
    # Connections for obj472 (graphObject_: Obj456) named C2
    self.drawConnections(
 )
    # Connections for obj473 (graphObject_: Obj457) named C3
    self.drawConnections(
 )
    # Connections for obj474 (graphObject_: Obj458) named C4
    self.drawConnections(
 )
    # Connections for obj475 (graphObject_: Obj459) named R1
    self.drawConnections(
(self.obj475,self.obj502,[244.0, 341.0, 332.5, 300.0],"true", 2),
(self.obj475,self.obj503,[244.0, 341.0, 252.5, 300.0],"true", 2),
(self.obj475,self.obj504,[244.0, 341.0, 192.5, 300.0],"true", 2),
(self.obj475,self.obj491,[244.0, 386.0, 176.5, 409.5],"true", 2),
(self.obj475,self.obj492,[244.0, 386.0, 244.5, 466.5],"true", 2),
(self.obj475,self.obj493,[244.0, 386.0, 343.5, 451.5],"true", 2),
(self.obj475,self.obj494,[244.0, 386.0, 385.5, 415.5],"true", 2) )
    # Connections for obj476 (graphObject_: Obj460) named R2
    self.drawConnections(
(self.obj476,self.obj499,[444.0, 361.0, 432.5, 310.0],"true", 2),
(self.obj476,self.obj500,[444.0, 361.0, 352.5, 310.0],"true", 2),
(self.obj476,self.obj501,[444.0, 361.0, 492.5, 310.0],"true", 2),
(self.obj476,self.obj495,[444.0, 406.0, 333.0, 438.5, 273.0, 459.5],"true", 3),
(self.obj476,self.obj496,[444.0, 406.0, 384.5, 447.5],"true", 2),
(self.obj476,self.obj497,[444.0, 406.0, 453.5, 423.5],"true", 2),
(self.obj476,self.obj498,[444.0, 406.0, 493.5, 413.5],"true", 2) )
    # Connections for obj477 (graphObject_: Obj461) named G2
    self.drawConnections(
 )
    # Connections for obj478 (graphObject_: Obj462) named G3
    self.drawConnections(
 )
    # Connections for obj479 (graphObject_: Obj463) named G4
    self.drawConnections(
 )
    # Connections for obj480 (graphObject_: Obj464) named G1
    self.drawConnections(
 )
    # Connections for obj482 (graphObject_: Obj467) of type posses
    self.drawConnections(
(self.obj482,self.obj472,[303.0, 160.5, 261.0, 219.0],"true", 2) )
    # Connections for obj483 (graphObject_: Obj469) of type posses
    self.drawConnections(
(self.obj483,self.obj473,[383.0, 160.5, 421.0, 219.0],"true", 2) )
    # Connections for obj484 (graphObject_: Obj471) of type posses
    self.drawConnections(
(self.obj484,self.obj473,[483.0, 170.5, 421.0, 219.0],"true", 2) )
    # Connections for obj485 (graphObject_: Obj473) of type posses
    self.drawConnections(
(self.obj485,self.obj472,[403.0, 170.5, 261.0, 219.0],"true", 2) )
    # Connections for obj486 (graphObject_: Obj475) of type posses
    self.drawConnections(
(self.obj486,self.obj474,[543.0, 170.5, 541.0, 219.0],"true", 2) )
    # Connections for obj488 (graphObject_: Obj479) of type posses
    self.drawConnections(
(self.obj488,self.obj471,[153.0, 170.5, 141.0, 219.0],"true", 2) )
    # Connections for obj489 (graphObject_: Obj481) of type posses
    self.drawConnections(
(self.obj489,self.obj472,[213.0, 170.5, 261.0, 219.0],"true", 2) )
    # Connections for obj490 (graphObject_: Obj483) of type posses
    self.drawConnections(
(self.obj490,self.obj473,[293.0, 170.5, 421.0, 219.0],"true", 2) )
    # Connections for obj526 (graphObject_: Obj517) of type posses
    self.drawConnections(
(self.obj526,self.obj474,[353.0, 170.5, 541.0, 219.0],"true", 2) )
    # Connections for obj531 (graphObject_: Obj525) of type posses
    self.drawConnections(
(self.obj531,self.obj474,[443.0, 160.5, 541.0, 219.0],"true", 2) )
    # Connections for obj491 (graphObject_: Obj485) of type achieve
    self.drawConnections(
(self.obj491,self.obj480,[176.5, 409.5, 163.0, 481.0],"true", 2) )
    # Connections for obj492 (graphObject_: Obj487) of type achieve
    self.drawConnections(
(self.obj492,self.obj477,[244.5, 466.5, 303.0, 501.0],"true", 2) )
    # Connections for obj493 (graphObject_: Obj489) of type achieve
    self.drawConnections(
(self.obj493,self.obj478,[343.5, 451.5, 483.0, 481.0],"true", 2) )
    # Connections for obj494 (graphObject_: Obj491) of type achieve
    self.drawConnections(
(self.obj494,self.obj479,[385.5, 415.5, 603.0, 461.0],"true", 2) )
    # Connections for obj495 (graphObject_: Obj493) of type achieve
    self.drawConnections(
(self.obj495,self.obj480,[273.0, 459.5, 213.0, 480.5, 163.0, 481.0],"true", 3) )
    # Connections for obj496 (graphObject_: Obj495) of type achieve
    self.drawConnections(
(self.obj496,self.obj477,[384.5, 447.5, 303.0, 501.0],"true", 2) )
    # Connections for obj497 (graphObject_: Obj497) of type achieve
    self.drawConnections(
(self.obj497,self.obj478,[453.5, 423.5, 483.0, 481.0],"true", 2) )
    # Connections for obj498 (graphObject_: Obj499) of type achieve
    self.drawConnections(
(self.obj498,self.obj479,[493.5, 413.5, 603.0, 461.0],"true", 2) )
    # Connections for obj499 (graphObject_: Obj501) of type requir
    self.drawConnections(
(self.obj499,self.obj473,[432.5, 310.0, 421.0, 259.0],"true", 2) )
    # Connections for obj500 (graphObject_: Obj502) of type requir
    self.drawConnections(
(self.obj500,self.obj472,[352.5, 310.0, 261.0, 259.0],"true", 2) )
    # Connections for obj501 (graphObject_: Obj503) of type requir
    self.drawConnections(
(self.obj501,self.obj474,[492.5, 310.0, 541.0, 259.0],"true", 2) )
    # Connections for obj502 (graphObject_: Obj504) of type requir
    self.drawConnections(
(self.obj502,self.obj473,[332.5, 300.0, 421.0, 259.0],"true", 2) )
    # Connections for obj503 (graphObject_: Obj505) of type requir
    self.drawConnections(
(self.obj503,self.obj472,[252.5, 300.0, 261.0, 259.0],"true", 2) )
    # Connections for obj504 (graphObject_: Obj506) of type requir
    self.drawConnections(
(self.obj504,self.obj471,[192.5, 300.0, 141.0, 259.0],"true", 2) )
    # Connections for obj528 (graphObject_: Obj520) named 
    self.drawConnections(
(self.obj528,self.obj529,[823.7943925233645, 116.0, 837.8971962616822, 140.5],"true", 2) )
    # Connections for obj527 (graphObject_: Obj519) of type metarial
    self.drawConnections(
(self.obj527,self.obj530,[867.0, 161.0, 892.0, 35.0, 834.5, 86.0],"true", 3) )
    # Connections for obj530 (graphObject_: Obj523) of type fromMaterial
    self.drawConnections(
(self.obj530,self.obj528,[834.5, 86.0, 777.0, 137.0, 794.1869158878504, 115.5263157894737],"true", 3) )
    # Connections for obj529 (graphObject_: Obj521) of type intoMaterial
    self.drawConnections(
(self.obj529,self.obj527,[837.8971962616822, 140.5, 852.0, 165.0],"true", 2) )

newfunction = omacsMODEL2_MDL

loadedMMName = ['omacss_META', 'pns2_META']

atom3version = '0.3'
