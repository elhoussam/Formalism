"""
__level2modelOMCAS_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: sam
Modified: Sun Feb 19 16:53:17 2017
______________________________________________________________________________
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
from graph_posses import *
from graph_achieve import *
from graph_Goal import *
from graph_Role import *
from graph_Capabilitie import *
from graph_requir import *
from graph_Agent import *
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

def level2modelOMCAS_MDL(self, rootNode, omacssRootNode=None):

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


    self.obj2256=Agent(self)
    self.obj2256.isGraphObjectVisual = True

    if(hasattr(self.obj2256, '_setHierarchicalLink')):
      self.obj2256._setHierarchicalLink(False)

    # price
    self.obj2256.price.setValue(0)

    # name
    self.obj2256.name.setValue('a1')

    self.obj2256.graphClass_= graph_Agent
    if self.genGraphics:
       new_obj = graph_Agent(120.0,100.0,self.obj2256)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Agent", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2256.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2256)
    self.globalAndLocalPostcondition(self.obj2256, rootNode)
    self.obj2256.postAction( rootNode.CREATE )

    self.obj2257=Agent(self)
    self.obj2257.isGraphObjectVisual = True

    if(hasattr(self.obj2257, '_setHierarchicalLink')):
      self.obj2257._setHierarchicalLink(False)

    # price
    self.obj2257.price.setValue(0)

    # name
    self.obj2257.name.setValue('a2')

    self.obj2257.graphClass_= graph_Agent
    if self.genGraphics:
       new_obj = graph_Agent(320.0,40.0,self.obj2257)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Agent", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2257.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2257)
    self.globalAndLocalPostcondition(self.obj2257, rootNode)
    self.obj2257.postAction( rootNode.CREATE )

    self.obj2258=Agent(self)
    self.obj2258.isGraphObjectVisual = True

    if(hasattr(self.obj2258, '_setHierarchicalLink')):
      self.obj2258._setHierarchicalLink(False)

    # price
    self.obj2258.price.setValue(0)

    # name
    self.obj2258.name.setValue('a3')

    self.obj2258.graphClass_= graph_Agent
    if self.genGraphics:
       new_obj = graph_Agent(500.0,60.0,self.obj2258)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Agent", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2258.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2258)
    self.globalAndLocalPostcondition(self.obj2258, rootNode)
    self.obj2258.postAction( rootNode.CREATE )

    self.obj2259=Capabilitie(self)
    self.obj2259.isGraphObjectVisual = True

    if(hasattr(self.obj2259, '_setHierarchicalLink')):
      self.obj2259._setHierarchicalLink(False)

    # name
    self.obj2259.name.setValue('c1')

    self.obj2259.graphClass_= graph_Capabilitie
    if self.genGraphics:
       new_obj = graph_Capabilitie(100.0,280.0,self.obj2259)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Capabilitie", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2259.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2259)
    self.globalAndLocalPostcondition(self.obj2259, rootNode)
    self.obj2259.postAction( rootNode.CREATE )

    self.obj2260=Capabilitie(self)
    self.obj2260.isGraphObjectVisual = True

    if(hasattr(self.obj2260, '_setHierarchicalLink')):
      self.obj2260._setHierarchicalLink(False)

    # name
    self.obj2260.name.setValue('c2')

    self.obj2260.graphClass_= graph_Capabilitie
    if self.genGraphics:
       new_obj = graph_Capabilitie(220.0,280.0,self.obj2260)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Capabilitie", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2260.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2260)
    self.globalAndLocalPostcondition(self.obj2260, rootNode)
    self.obj2260.postAction( rootNode.CREATE )

    self.obj2261=Capabilitie(self)
    self.obj2261.isGraphObjectVisual = True

    if(hasattr(self.obj2261, '_setHierarchicalLink')):
      self.obj2261._setHierarchicalLink(False)

    # name
    self.obj2261.name.setValue('c3')

    self.obj2261.graphClass_= graph_Capabilitie
    if self.genGraphics:
       new_obj = graph_Capabilitie(380.0,260.0,self.obj2261)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Capabilitie", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2261.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2261)
    self.globalAndLocalPostcondition(self.obj2261, rootNode)
    self.obj2261.postAction( rootNode.CREATE )

    self.obj2262=Capabilitie(self)
    self.obj2262.isGraphObjectVisual = True

    if(hasattr(self.obj2262, '_setHierarchicalLink')):
      self.obj2262._setHierarchicalLink(False)

    # name
    self.obj2262.name.setValue('c4')

    self.obj2262.graphClass_= graph_Capabilitie
    if self.genGraphics:
       new_obj = graph_Capabilitie(540.0,280.0,self.obj2262)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Capabilitie", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2262.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2262)
    self.globalAndLocalPostcondition(self.obj2262, rootNode)
    self.obj2262.postAction( rootNode.CREATE )

    self.obj2263=Role(self)
    self.obj2263.isGraphObjectVisual = True

    if(hasattr(self.obj2263, '_setHierarchicalLink')):
      self.obj2263._setHierarchicalLink(False)

    # name
    self.obj2263.name.setValue('R1')

    self.obj2263.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(200.0,400.0,self.obj2263)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2263.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2263)
    self.globalAndLocalPostcondition(self.obj2263, rootNode)
    self.obj2263.postAction( rootNode.CREATE )

    self.obj2264=Role(self)
    self.obj2264.isGraphObjectVisual = True

    if(hasattr(self.obj2264, '_setHierarchicalLink')):
      self.obj2264._setHierarchicalLink(False)

    # name
    self.obj2264.name.setValue('R2')

    self.obj2264.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(420.0,400.0,self.obj2264)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2264.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2264)
    self.globalAndLocalPostcondition(self.obj2264, rootNode)
    self.obj2264.postAction( rootNode.CREATE )

    self.obj2265=Goal(self)
    self.obj2265.isGraphObjectVisual = True

    if(hasattr(self.obj2265, '_setHierarchicalLink')):
      self.obj2265._setHierarchicalLink(False)

    # name
    self.obj2265.name.setValue('g1')

    self.obj2265.graphClass_= graph_Goal
    if self.genGraphics:
       new_obj = graph_Goal(120.0,520.0,self.obj2265)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Goal", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2265.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2265)
    self.globalAndLocalPostcondition(self.obj2265, rootNode)
    self.obj2265.postAction( rootNode.CREATE )

    self.obj2266=Goal(self)
    self.obj2266.isGraphObjectVisual = True

    if(hasattr(self.obj2266, '_setHierarchicalLink')):
      self.obj2266._setHierarchicalLink(False)

    # name
    self.obj2266.name.setValue('g2')

    self.obj2266.graphClass_= graph_Goal
    if self.genGraphics:
       new_obj = graph_Goal(300.0,600.0,self.obj2266)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Goal", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2266.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2266)
    self.globalAndLocalPostcondition(self.obj2266, rootNode)
    self.obj2266.postAction( rootNode.CREATE )

    self.obj2267=Goal(self)
    self.obj2267.isGraphObjectVisual = True

    if(hasattr(self.obj2267, '_setHierarchicalLink')):
      self.obj2267._setHierarchicalLink(False)

    # name
    self.obj2267.name.setValue('g3')

    self.obj2267.graphClass_= graph_Goal
    if self.genGraphics:
       new_obj = graph_Goal(420.0,600.0,self.obj2267)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Goal", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2267.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2267)
    self.globalAndLocalPostcondition(self.obj2267, rootNode)
    self.obj2267.postAction( rootNode.CREATE )

    self.obj2268=Goal(self)
    self.obj2268.isGraphObjectVisual = True

    if(hasattr(self.obj2268, '_setHierarchicalLink')):
      self.obj2268._setHierarchicalLink(False)

    # name
    self.obj2268.name.setValue('g4')

    self.obj2268.graphClass_= graph_Goal
    if self.genGraphics:
       new_obj = graph_Goal(540.0,520.0,self.obj2268)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Goal", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2268.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2268)
    self.globalAndLocalPostcondition(self.obj2268, rootNode)
    self.obj2268.postAction( rootNode.CREATE )

    self.obj2269=posses(self)
    self.obj2269.isGraphObjectVisual = True

    if(hasattr(self.obj2269, '_setHierarchicalLink')):
      self.obj2269._setHierarchicalLink(False)

    # rate
    self.obj2269.rate.setValue(0.3)

    self.obj2269.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(110.0,229.75,self.obj2269)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.4299999999999968, 1.2199999999999998]
    else: new_obj = None
    self.obj2269.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2269)
    self.globalAndLocalPostcondition(self.obj2269, rootNode)
    self.obj2269.postAction( rootNode.CREATE )

    self.obj2270=posses(self)
    self.obj2270.isGraphObjectVisual = True

    if(hasattr(self.obj2270, '_setHierarchicalLink')):
      self.obj2270._setHierarchicalLink(False)

    # rate
    self.obj2270.rate.setValue(0.5)

    self.obj2270.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(190.0,246.75,self.obj2270)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2270.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2270)
    self.globalAndLocalPostcondition(self.obj2270, rootNode)
    self.obj2270.postAction( rootNode.CREATE )

    self.obj2271=posses(self)
    self.obj2271.isGraphObjectVisual = True

    if(hasattr(self.obj2271, '_setHierarchicalLink')):
      self.obj2271._setHierarchicalLink(False)

    # rate
    self.obj2271.rate.setValue(0.5)

    self.obj2271.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(302.5,255.0,self.obj2271)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2271.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2271)
    self.globalAndLocalPostcondition(self.obj2271, rootNode)
    self.obj2271.postAction( rootNode.CREATE )

    self.obj2272=posses(self)
    self.obj2272.isGraphObjectVisual = True

    if(hasattr(self.obj2272, '_setHierarchicalLink')):
      self.obj2272._setHierarchicalLink(False)

    # rate
    self.obj2272.rate.setValue(0.3)

    self.obj2272.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(433.0,244.5,self.obj2272)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2272.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2272)
    self.globalAndLocalPostcondition(self.obj2272, rootNode)
    self.obj2272.postAction( rootNode.CREATE )

    self.obj2273=posses(self)
    self.obj2273.isGraphObjectVisual = True

    if(hasattr(self.obj2273, '_setHierarchicalLink')):
      self.obj2273._setHierarchicalLink(False)

    # rate
    self.obj2273.rate.setValue(0.7)

    self.obj2273.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(256.0,165.75,self.obj2273)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2273.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2273)
    self.globalAndLocalPostcondition(self.obj2273, rootNode)
    self.obj2273.postAction( rootNode.CREATE )

    self.obj2274=posses(self)
    self.obj2274.isGraphObjectVisual = True

    if(hasattr(self.obj2274, '_setHierarchicalLink')):
      self.obj2274._setHierarchicalLink(False)

    # rate
    self.obj2274.rate.setValue(0.5)

    self.obj2274.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(373.0,180.5,self.obj2274)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2274.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2274)
    self.globalAndLocalPostcondition(self.obj2274, rootNode)
    self.obj2274.postAction( rootNode.CREATE )

    self.obj2275=posses(self)
    self.obj2275.isGraphObjectVisual = True

    if(hasattr(self.obj2275, '_setHierarchicalLink')):
      self.obj2275._setHierarchicalLink(False)

    # rate
    self.obj2275.rate.setValue(0.7)

    self.obj2275.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(509.0,234.5,self.obj2275)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2275.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2275)
    self.globalAndLocalPostcondition(self.obj2275, rootNode)
    self.obj2275.postAction( rootNode.CREATE )

    self.obj2276=posses(self)
    self.obj2276.isGraphObjectVisual = True

    if(hasattr(self.obj2276, '_setHierarchicalLink')):
      self.obj2276._setHierarchicalLink(False)

    # rate
    self.obj2276.rate.setValue(0.2)

    self.obj2276.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(564.5,204.25,self.obj2276)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2276.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2276)
    self.globalAndLocalPostcondition(self.obj2276, rootNode)
    self.obj2276.postAction( rootNode.CREATE )

    self.obj2277=posses(self)
    self.obj2277.isGraphObjectVisual = True

    if(hasattr(self.obj2277, '_setHierarchicalLink')):
      self.obj2277._setHierarchicalLink(False)

    # rate
    self.obj2277.rate.setValue(0.4)

    self.obj2277.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(323.0,170.5,self.obj2277)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2277.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2277)
    self.globalAndLocalPostcondition(self.obj2277, rootNode)
    self.obj2277.postAction( rootNode.CREATE )

    self.obj2278=posses(self)
    self.obj2278.isGraphObjectVisual = True

    if(hasattr(self.obj2278, '_setHierarchicalLink')):
      self.obj2278._setHierarchicalLink(False)

    # rate
    self.obj2278.rate.setValue(0.9)

    self.obj2278.graphClass_= graph_posses
    if self.genGraphics:
       new_obj = graph_posses(472.0,150.5,self.obj2278)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("posses", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2278.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2278)
    self.globalAndLocalPostcondition(self.obj2278, rootNode)
    self.obj2278.postAction( rootNode.CREATE )

    self.obj2279=achieve(self)
    self.obj2279.isGraphObjectVisual = True

    if(hasattr(self.obj2279, '_setHierarchicalLink')):
      self.obj2279._setHierarchicalLink(False)

    # rate
    self.obj2279.rate.setValue(0.2)

    self.obj2279.graphClass_= graph_achieve
    if self.genGraphics:
       new_obj = graph_achieve(161.25,464.75,self.obj2279)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("achieve", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2279.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2279)
    self.globalAndLocalPostcondition(self.obj2279, rootNode)
    self.obj2279.postAction( rootNode.CREATE )

    self.obj2280=achieve(self)
    self.obj2280.isGraphObjectVisual = True

    if(hasattr(self.obj2280, '_setHierarchicalLink')):
      self.obj2280._setHierarchicalLink(False)

    # rate
    self.obj2280.rate.setValue(0.4)

    self.obj2280.graphClass_= graph_achieve
    if self.genGraphics:
       new_obj = graph_achieve(265.75,522.75,self.obj2280)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("achieve", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2280.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2280)
    self.globalAndLocalPostcondition(self.obj2280, rootNode)
    self.obj2280.postAction( rootNode.CREATE )

    self.obj2281=achieve(self)
    self.obj2281.isGraphObjectVisual = True

    if(hasattr(self.obj2281, '_setHierarchicalLink')):
      self.obj2281._setHierarchicalLink(False)

    # rate
    self.obj2281.rate.setValue(0.6)

    self.obj2281.graphClass_= graph_achieve
    if self.genGraphics:
       new_obj = graph_achieve(344.5,532.5,self.obj2281)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("achieve", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2281.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2281)
    self.globalAndLocalPostcondition(self.obj2281, rootNode)
    self.obj2281.postAction( rootNode.CREATE )

    self.obj2282=achieve(self)
    self.obj2282.isGraphObjectVisual = True

    if(hasattr(self.obj2282, '_setHierarchicalLink')):
      self.obj2282._setHierarchicalLink(False)

    # rate
    self.obj2282.rate.setValue(0.8)

    self.obj2282.graphClass_= graph_achieve
    if self.genGraphics:
       new_obj = graph_achieve(441.0,476.0,self.obj2282)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("achieve", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.98
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2282.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2282)
    self.globalAndLocalPostcondition(self.obj2282, rootNode)
    self.obj2282.postAction( rootNode.CREATE )

    self.obj2283=achieve(self)
    self.obj2283.isGraphObjectVisual = True

    if(hasattr(self.obj2283, '_setHierarchicalLink')):
      self.obj2283._setHierarchicalLink(False)

    # rate
    self.obj2283.rate.setValue(0.1)

    self.obj2283.graphClass_= graph_achieve
    if self.genGraphics:
       new_obj = graph_achieve(541.25,464.25,self.obj2283)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("achieve", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2283.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2283)
    self.globalAndLocalPostcondition(self.obj2283, rootNode)
    self.obj2283.postAction( rootNode.CREATE )

    self.obj2284=achieve(self)
    self.obj2284.isGraphObjectVisual = True

    if(hasattr(self.obj2284, '_setHierarchicalLink')):
      self.obj2284._setHierarchicalLink(False)

    # rate
    self.obj2284.rate.setValue(0.4)

    self.obj2284.graphClass_= graph_achieve
    if self.genGraphics:
       new_obj = graph_achieve(486.5,569.5,self.obj2284)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("achieve", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2284.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2284)
    self.globalAndLocalPostcondition(self.obj2284, rootNode)
    self.obj2284.postAction( rootNode.CREATE )

    self.obj2285=achieve(self)
    self.obj2285.isGraphObjectVisual = True

    if(hasattr(self.obj2285, '_setHierarchicalLink')):
      self.obj2285._setHierarchicalLink(False)

    # rate
    self.obj2285.rate.setValue(0.7)

    self.obj2285.graphClass_= graph_achieve
    if self.genGraphics:
       new_obj = graph_achieve(383.5,483.5,self.obj2285)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("achieve", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2285.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2285)
    self.globalAndLocalPostcondition(self.obj2285, rootNode)
    self.obj2285.postAction( rootNode.CREATE )

    self.obj2286=achieve(self)
    self.obj2286.isGraphObjectVisual = True

    if(hasattr(self.obj2286, '_setHierarchicalLink')):
      self.obj2286._setHierarchicalLink(False)

    # rate
    self.obj2286.rate.setValue(1.0)

    self.obj2286.graphClass_= graph_achieve
    if self.genGraphics:
       new_obj = graph_achieve(281.5,445.5,self.obj2286)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("achieve", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2286.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2286)
    self.globalAndLocalPostcondition(self.obj2286, rootNode)
    self.obj2286.postAction( rootNode.CREATE )

    self.obj2287=requir(self)
    self.obj2287.isGraphObjectVisual = True

    if(hasattr(self.obj2287, '_setHierarchicalLink')):
      self.obj2287._setHierarchicalLink(False)

    self.obj2287.graphClass_= graph_requir
    if self.genGraphics:
       new_obj = graph_requir(172.5,360.0,self.obj2287)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("requir", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj2287.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2287)
    self.globalAndLocalPostcondition(self.obj2287, rootNode)
    self.obj2287.postAction( rootNode.CREATE )

    self.obj2288=requir(self)
    self.obj2288.isGraphObjectVisual = True

    if(hasattr(self.obj2288, '_setHierarchicalLink')):
      self.obj2288._setHierarchicalLink(False)

    self.obj2288.graphClass_= graph_requir
    if self.genGraphics:
       new_obj = graph_requir(232.5,360.0,self.obj2288)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("requir", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj2288.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2288)
    self.globalAndLocalPostcondition(self.obj2288, rootNode)
    self.obj2288.postAction( rootNode.CREATE )

    self.obj2289=requir(self)
    self.obj2289.isGraphObjectVisual = True

    if(hasattr(self.obj2289, '_setHierarchicalLink')):
      self.obj2289._setHierarchicalLink(False)

    self.obj2289.graphClass_= graph_requir
    if self.genGraphics:
       new_obj = graph_requir(311.25,348.0,self.obj2289)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("requir", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj2289.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2289)
    self.globalAndLocalPostcondition(self.obj2289, rootNode)
    self.obj2289.postAction( rootNode.CREATE )

    self.obj2290=requir(self)
    self.obj2290.isGraphObjectVisual = True

    if(hasattr(self.obj2290, '_setHierarchicalLink')):
      self.obj2290._setHierarchicalLink(False)

    self.obj2290.graphClass_= graph_requir
    if self.genGraphics:
       new_obj = graph_requir(531.25,359.0,self.obj2290)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("requir", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj2290.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2290)
    self.globalAndLocalPostcondition(self.obj2290, rootNode)
    self.obj2290.postAction( rootNode.CREATE )

    self.obj2291=requir(self)
    self.obj2291.isGraphObjectVisual = True

    if(hasattr(self.obj2291, '_setHierarchicalLink')):
      self.obj2291._setHierarchicalLink(False)

    self.obj2291.graphClass_= graph_requir
    if self.genGraphics:
       new_obj = graph_requir(324.5,373.0,self.obj2291)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("requir", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj2291.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2291)
    self.globalAndLocalPostcondition(self.obj2291, rootNode)
    self.obj2291.postAction( rootNode.CREATE )

    self.obj2292=requir(self)
    self.obj2292.isGraphObjectVisual = True

    if(hasattr(self.obj2292, '_setHierarchicalLink')):
      self.obj2292._setHierarchicalLink(False)

    self.obj2292.graphClass_= graph_requir
    if self.genGraphics:
       new_obj = graph_requir(422.5,350.0,self.obj2292)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("requir", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj2292.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2292)
    self.globalAndLocalPostcondition(self.obj2292, rootNode)
    self.obj2292.postAction( rootNode.CREATE )

    # Connections for obj2256 (graphObject_: Obj1048) named a1
    self.drawConnections(
(self.obj2256,self.obj2269,[145.0, 162.0, 116.0, 200.5, 110.0, 229.75],"true", 3),
(self.obj2256,self.obj2270,[145.0, 162.0, 166.0, 217.5, 190.0, 246.75],"true", 3),
(self.obj2256,self.obj2271,[145.0, 162.0, 276.0, 282.0, 302.5, 255.0],"true", 3),
(self.obj2256,self.obj2272,[145.0, 162.0, 415.0, 261.0, 433.0, 244.5],"true", 3) )
    # Connections for obj2257 (graphObject_: Obj1049) named a2
    self.drawConnections(
(self.obj2257,self.obj2273,[345.0, 102.0, 282.0, 121.5, 256.0, 165.75],"true", 3),
(self.obj2257,self.obj2274,[345.0, 102.0, 373.0, 180.5],"true", 2),
(self.obj2257,self.obj2275,[345.0, 102.0, 509.0, 234.5],"true", 2) )
    # Connections for obj2258 (graphObject_: Obj1050) named a3
    self.drawConnections(
(self.obj2258,self.obj2276,[525.0, 122.0, 560.5, 170.0, 564.5, 204.25],"true", 3),
(self.obj2258,self.obj2277,[525.0, 122.0, 323.0, 170.5],"true", 2),
(self.obj2258,self.obj2278,[525.0, 122.0, 472.0, 150.5],"true", 2) )
    # Connections for obj2259 (graphObject_: Obj1051) named c1
    self.drawConnections(
 )
    # Connections for obj2260 (graphObject_: Obj1052) named c2
    self.drawConnections(
 )
    # Connections for obj2261 (graphObject_: Obj1053) named c3
    self.drawConnections(
 )
    # Connections for obj2262 (graphObject_: Obj1054) named c4
    self.drawConnections(
 )
    # Connections for obj2263 (graphObject_: Obj1055) named R1
    self.drawConnections(
(self.obj2263,self.obj2287,[224.0, 401.0, 172.5, 360.0],"true", 2),
(self.obj2263,self.obj2288,[224.0, 401.0, 232.5, 360.0],"true", 2),
(self.obj2263,self.obj2289,[224.0, 401.0, 267.0, 373.5, 311.25, 348.0],"true", 3),
(self.obj2263,self.obj2279,[224.0, 446.0, 181.5, 446.0, 161.25, 464.75],"true", 3),
(self.obj2263,self.obj2280,[224.0, 446.0, 241.0, 504.0, 265.75, 522.75],"true", 3),
(self.obj2263,self.obj2281,[224.0, 446.0, 243.0, 535.0, 344.5, 532.5],"true", 3),
(self.obj2263,self.obj2282,[224.0, 446.0, 286.0, 486.0, 441.0, 476.0],"true", 3) )
    # Connections for obj2264 (graphObject_: Obj1056) named R2
    self.drawConnections(
(self.obj2264,self.obj2290,[444.0, 401.0, 502.0, 379.5, 531.25, 359.0],"true", 3),
(self.obj2264,self.obj2291,[444.0, 401.0, 324.5, 373.0],"true", 2),
(self.obj2264,self.obj2292,[444.0, 401.0, 422.5, 350.0],"true", 2),
(self.obj2264,self.obj2283,[444.0, 446.0, 511.5, 445.5, 541.25, 464.25],"true", 3),
(self.obj2264,self.obj2284,[444.0, 446.0, 486.5, 569.5],"true", 2),
(self.obj2264,self.obj2285,[444.0, 446.0, 383.5, 483.5],"true", 2),
(self.obj2264,self.obj2286,[444.0, 446.0, 281.5, 445.5],"true", 2) )
    # Connections for obj2265 (graphObject_: Obj1057) named g1
    self.drawConnections(
 )
    # Connections for obj2266 (graphObject_: Obj1058) named g2
    self.drawConnections(
 )
    # Connections for obj2267 (graphObject_: Obj1059) named g3
    self.drawConnections(
 )
    # Connections for obj2268 (graphObject_: Obj1060) named g4
    self.drawConnections(
 )
    # Connections for obj2269 (graphObject_: Obj1061) of type posses
    self.drawConnections(
(self.obj2269,self.obj2259,[110.0, 229.75, 104.0, 259.0, 121.0, 279.0],"true", 3) )
    # Connections for obj2270 (graphObject_: Obj1063) of type posses
    self.drawConnections(
(self.obj2270,self.obj2260,[190.0, 246.75, 214.0, 276.0, 241.0, 279.0],"true", 3) )
    # Connections for obj2271 (graphObject_: Obj1065) of type posses
    self.drawConnections(
(self.obj2271,self.obj2261,[302.5, 255.0, 329.0, 228.0, 401.0, 259.0],"true", 3) )
    # Connections for obj2272 (graphObject_: Obj1067) of type posses
    self.drawConnections(
(self.obj2272,self.obj2262,[433.0, 244.5, 451.0, 228.0, 561.0, 279.0],"true", 3) )
    # Connections for obj2273 (graphObject_: Obj1069) of type posses
    self.drawConnections(
(self.obj2273,self.obj2260,[256.0, 165.75, 230.0, 210.0, 241.0, 279.0],"true", 3) )
    # Connections for obj2274 (graphObject_: Obj1071) of type posses
    self.drawConnections(
(self.obj2274,self.obj2261,[373.0, 180.5, 401.0, 259.0],"true", 2) )
    # Connections for obj2275 (graphObject_: Obj1073) of type posses
    self.drawConnections(
(self.obj2275,self.obj2262,[509.0, 234.5, 561.0, 279.0],"true", 2) )
    # Connections for obj2276 (graphObject_: Obj1075) of type posses
    self.drawConnections(
(self.obj2276,self.obj2262,[564.5, 204.25, 568.5, 238.5, 561.0, 279.0],"true", 3) )
    # Connections for obj2277 (graphObject_: Obj1077) of type posses
    self.drawConnections(
(self.obj2277,self.obj2260,[323.0, 170.5, 241.0, 279.0],"true", 2) )
    # Connections for obj2278 (graphObject_: Obj1079) of type posses
    self.drawConnections(
(self.obj2278,self.obj2261,[472.0, 150.5, 401.0, 259.0],"true", 2) )
    # Connections for obj2279 (graphObject_: Obj1081) of type achieve
    self.drawConnections(
(self.obj2279,self.obj2265,[161.25, 464.75, 141.0, 483.5, 143.0, 521.0],"true", 3) )
    # Connections for obj2280 (graphObject_: Obj1083) of type achieve
    self.drawConnections(
(self.obj2280,self.obj2266,[265.75, 522.75, 290.5, 541.5, 323.0, 601.0],"true", 3) )
    # Connections for obj2281 (graphObject_: Obj1085) of type achieve
    self.drawConnections(
(self.obj2281,self.obj2267,[344.5, 532.5, 446.0, 530.0, 443.0, 601.0],"true", 3) )
    # Connections for obj2282 (graphObject_: Obj1087) of type achieve
    self.drawConnections(
(self.obj2282,self.obj2268,[441.0, 476.0, 596.0, 466.0, 563.0, 521.0],"true", 3) )
    # Connections for obj2283 (graphObject_: Obj1089) of type achieve
    self.drawConnections(
(self.obj2283,self.obj2268,[541.25, 464.25, 571.0, 483.0, 563.0, 521.0],"true", 3) )
    # Connections for obj2284 (graphObject_: Obj1091) of type achieve
    self.drawConnections(
(self.obj2284,self.obj2267,[486.5, 569.5, 443.0, 601.0],"true", 2) )
    # Connections for obj2285 (graphObject_: Obj1093) of type achieve
    self.drawConnections(
(self.obj2285,self.obj2266,[383.5, 483.5, 323.0, 601.0],"true", 2) )
    # Connections for obj2286 (graphObject_: Obj1095) of type achieve
    self.drawConnections(
(self.obj2286,self.obj2265,[281.5, 445.5, 143.0, 521.0],"true", 2) )
    # Connections for obj2287 (graphObject_: Obj1097) of type requir
    self.drawConnections(
(self.obj2287,self.obj2259,[172.5, 360.0, 121.0, 319.0],"true", 2) )
    # Connections for obj2288 (graphObject_: Obj1098) of type requir
    self.drawConnections(
(self.obj2288,self.obj2260,[232.5, 360.0, 241.0, 319.0],"true", 2) )
    # Connections for obj2289 (graphObject_: Obj1099) of type requir
    self.drawConnections(
(self.obj2289,self.obj2261,[311.25, 348.0, 355.5, 322.5, 401.0, 299.0],"true", 3) )
    # Connections for obj2290 (graphObject_: Obj1100) of type requir
    self.drawConnections(
(self.obj2290,self.obj2262,[531.25, 359.0, 560.5, 338.5, 561.0, 319.0],"true", 3) )
    # Connections for obj2291 (graphObject_: Obj1101) of type requir
    self.drawConnections(
(self.obj2291,self.obj2260,[324.5, 373.0, 241.0, 319.0],"true", 2) )
    # Connections for obj2292 (graphObject_: Obj1102) of type requir
    self.drawConnections(
(self.obj2292,self.obj2261,[422.5, 350.0, 401.0, 299.0],"true", 2) )

newfunction = level2modelOMCAS_MDL

loadedMMName = 'omacss_META'

atom3version = '0.3'
