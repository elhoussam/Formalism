import xml.etree.cElementTree as ET
 

def CheckAttr(parent, name  , ID , Type  , xN  , yN    ,beginID  , endID , rate ):
	nodeType = "Operating Unit"
	if parent != None :
		print "\t Parent.tag : " + str(parent.tag)
	if name != "None" :
		print "\t Name : " + str(name)
	if ID != "0" :
		print "\t ID : " + str(ID)
	if Type != "None" :
		print "\t Type : " + str(Type)
		nodeType ="Material"
	if xN != "-1" :
		print "\t xN : " + str(xN)
	if yN != "-1" :
		print "\t yN : " + str(yN)
	if beginID != "0" :
		print "\t beginID : " + str(beginID)
	if endID != "0" :
		print "\t endID : " + str(endID)
		nodeType = "Edges"
	if rate != "0" :
		print "\t rate : " + str(rate)
	print "* * * New Node is "+nodeType
		
def newMaterial(  parent=None , name= "None" , ID="0" , Type= "None" , xN ='-1', yN ='-1' ,price='-1' ,reqF = 0  ,maxF =999999 ):
	node = ET.SubElement(parent, "Material",ID=str(ID),Name=name,Type=str(Type))
    
	
	print 'add Cords into node		-NewNode-'
	#Create Corde for the node material
	cords = ET.SubElement(node, "Coords")
	ET.SubElement(cords, "X").text = str( xN )
	ET.SubElement(cords, "Y").text = str( yN )
	    
	if price != '-1' or  reqF != 0  or maxF !=999999 :
		print 'Detect Price'
		ParameterList = ET.SubElement(node, "ParameterList")
		ET.SubElement(ParameterList, "Parameter",Name="price",Value=str( price) )
		if reqF == 0 : reqF = '-1'
		ET.SubElement(ParameterList, "Parameter",Name="reqflow",Value= str(reqF) )
		if maxF == 999999 : maxF = '-1'
		ET.SubElement(ParameterList, "Parameter",Name="maxflow",Value=str(maxF) )
			 		 		 
	print 'add Label into node		-NewNode-'
	#Create Label for the Material
	label = ET.SubElement(node, "Label",Text = str(name))
	offset = ET.SubElement(label,  "Offset")
	ET.SubElement(offset, "X").text =   str(5)
	ET.SubElement(offset, "Y").text =   str(0)
	
	print 'End		-NewNode-'
	return node 
	
def newOpUnit(  parent=None , name= "None" , ID="0"   , xN ='-1', yN ='-1'  , costP = '0'  ,costF ='0' ):
	node = ET.SubElement(parent, "OperatingUnit",ID=str(ID),Name=name )
   
	print 'add Cords into node		-NewNode-'
	#Create Corde for the node material
	cords = ET.SubElement(node, "Coords")
	ET.SubElement(cords, "X").text = str( xN )
	ET.SubElement(cords, "Y").text = str( yN )
	
	if  costF != '0'  or costP !='0' :
		print 'Detect Cost'
		ParameterList = ET.SubElement(node, "ParameterList")
		if costF == '0' : costF = '-1'
		ET.SubElement(ParameterList, "Parameter",Name="opercostfix",Value= str(costF) )
		if costP == '0' : costP = '-1'
		ET.SubElement(ParameterList, "Parameter",Name="opercostprop",Value=str(costP) )
	    
		 		 		 
	print 'add Label into node		-NewNode-'
	#Create Label for the Material
	label = ET.SubElement(node, "Label",Text = str(name))
	offset = ET.SubElement(label,  "Offset")
	ET.SubElement(offset, "X").text =   str(5)
	ET.SubElement(offset, "Y").text =   str(0)
	
	print 'End		-NewNode-'
	return node 

 
def newEdges(  parent  , name  , ID    , xN  , yN    ,beginID   , endID    ):
	node = ET.SubElement(parent, "Edge",ID=str(ID),BeginID=str(beginID),EndID=str(endID),Rate=str(name),Title=str(name) , ArrowOnCenter="true" , ArrowPosition="50") 
   
	print 'add Cords into node		-NewNode-'
	#Create Corde for the node material
	cords = ET.SubElement(node, "Coords")
	ET.SubElement(cords, "X").text = str( xN )
	ET.SubElement(cords, "Y").text = str( yN )
		 		 		 
	print 'add Label into node		-NewNode-'
	#Create Label for the Material
	label = ET.SubElement(node, "Label",Text = str(name))
	offset = ET.SubElement(label,  "Offset")
	ET.SubElement(offset, "X").text =   str(5)
	ET.SubElement(offset, "Y").text =   str(0)
	
	print 'NewEdges'
	return node 
 

def newNode(parent=None , name= "None" , ID="0" , Type= "None" , xN ='-1', yN ='-1'  ,beginID = '0' , endID = '0', rate = '0' , price='-1' ,costF='-1' , costP ='-1' ):
	CheckAttr(parent, name  , ID , Type  , xN  , yN    ,beginID  , endID , rate  )
	print 'Start		-NewNode-'
	
	print 'Decide if Mat | Edge | OpUnit		-NewNode-'
	if parent.tag == 'Materials' : node = ET.SubElement(parent, "Material",ID=str(ID),Name=name,Type=str(Type)) 
	elif parent.tag == 'Edges' : node = ET.SubElement(parent, "Edge",ID=str(ID),BeginID=str(beginID),EndID=str(endID),Rate=str(rate),Title=str(rate) , ArrowOnCenter="true" , ArrowPosition="50") 
	else : node = ET.SubElement(parent, "OperatingUnit",ID=str(ID),Name=name ) 
	
	
	print 'add Cords into node		-NewNode-'
	#Create Corde for the node material
	cords = ET.SubElement(node, "Coords")
	ET.SubElement(cords, "X").text = str( xN )
	ET.SubElement(cords, "Y").text = str( yN )
	
	#Add Some ParameterList :P to the node
	# add like 
	# add like Parameter = ET.SubElement(ParameterList, "name",Text = "PriceOrReqFlowETCETC","value",Text = str(name))
	
	if price != '-1' :
		print 'Detect Price'
		ParameterList = ET.SubElement(node, "ParameterList")
	if costF != '-1' and costP != '-1' :
		
		print 'Detect opercost Fix && Prop'
		ParameterList = ET.SubElement(node, "ParameterList")
		ET.SubElement(ParameterList,"Parameter",  Name = "opercostfix", Value = str(costF))
		ET.SubElement(ParameterList,"Parameter",  Name = "opercostprop", Value = str(costP))
	
	print 'add Label into node		-NewNode-'
	#Create Label for the Material
	label = ET.SubElement(node, "Label",Text = str(name))
	offset = ET.SubElement(label,  "Offset")
	ET.SubElement(offset, "X").text =   str(5)
	ET.SubElement(offset, "Y").text =   str(0)
	
	print 'End		-NewNode-'
	return node 
 
	 
