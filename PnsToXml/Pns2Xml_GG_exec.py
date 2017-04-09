# _ Pns2Xml_GG_exec.py ____________________________________________________________________________
# Pns2Xml : a class that subclasifies GraphGrammar. File generated automatically by ATOM3.
# ___________________________________________________________________________________________
from GraphGrammar import *
from VisitRaw_GG_rule import *
from VisitMat_GG_rule import *
from VisitProduct_GG_rule import *
from VisitOpUnit_GG_rule import *
from Visit1EdgeRAW_GG_rule import *
from Visit2EdgeFINAL_GG_rule import *
from Visit3EdgeMat_GG_rule import *
from Visit4EdgeMat_GG_rule import *
class Pns2Xml_GG_exec (GraphGrammar):
   def __init__ (self, parent):
      GraphGrammar.__init__(self, [VisitRaw_GG_rule(parent) , VisitMat_GG_rule(parent) , VisitProduct_GG_rule(parent) , VisitOpUnit_GG_rule(parent) , Visit1EdgeRAW_GG_rule(parent) , Visit2EdgeFINAL_GG_rule(parent) , Visit3EdgeMat_GG_rule(parent) , Visit4EdgeMat_GG_rule(parent)])
   def initialAction(self, graph):
      global iD
      iD = 1
      global ET
      import xml.etree.cElementTree as ET
      # main Nodes
      global pgraph 
      pgraph = ET.Element("PGraph")
      global materials
      materials = ET.SubElement(pgraph, "Materials")
      global edges
      edges = ET.SubElement(pgraph, "Edges")
      global opunits
      opunits = ET.SubElement(pgraph, "OperatingUnits") 
      
      

   def finalAction(self, graph):
      import Pns2Xml_GG_exec
      import time 
      import os
      
      print 'Start Final Action '
      name  = str(os.getcwd())+'/pns'+str(int(time.time()))+'.pgsx'
      print name
      tree = Pns2Xml_GG_exec.ET.ElementTree( Pns2Xml_GG_exec.pgraph )
      tree.write(name,xml_declaration=True,encoding="utf-8",method ="xml")
      
      print 'End Final Action '
      
      

importedModules = ['VisitRaw_GG_rule', 'VisitMat_GG_rule', 'VisitProduct_GG_rule', 'VisitOpUnit_GG_rule', 'Visit1EdgeRAW_GG_rule', 'Visit2EdgeFINAL_GG_rule', 'Visit3EdgeMat_GG_rule', 'Visit4EdgeMat_GG_rule']

