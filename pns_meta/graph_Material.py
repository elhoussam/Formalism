"""
__graph_Material.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
______________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_Material(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 71, 50
        graphEntity.__init__(self, x, y)
        self.ChangesAtRunTime = 0
        self.constraintList = []
        if self.semanticObject: atribs = self.semanticObject.attributesToDraw()
        else: atribs = None
        self.graphForms = []
        self.imageDict = self.getImageDict()

    def DrawObject(self, drawing, showGG = 0):
        self.dc = drawing
        if showGG and self.semanticObject: self.drawGGLabel(drawing)
        self.image_gf0 = PhotoImage(format='gif',data=self.imageDict['m.gif' ])
        h = drawing.create_image(self.translate([34.0, 25.0]), tags = self.tag, image = self.image_gf0)
        self.gf0 = GraphicalForm(drawing, h, 'gf0', 'm.gif')
        self.graphForms.append(self.gf0)

        h = drawing.create_oval(self.translate([34.0, 50.0, 34.0, 50.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([32.0, 1.0, 32.0, 1.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([10.0, 23.0, 10.0, 23.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([58.0, 20.0, 58.0, 20.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([15.0, 42.0, 15.0, 42.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([53.0, 42.0, 53.0, 42.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        if self.semanticObject: drawText = self.semanticObject.Name.toString()
        else: drawText = "<Name>"
        font = tkFont.Font( family='Helvetica', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([35.0, 28.0, 35.0, -3.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["Name"] = h
        self.gf2 = GraphicalForm(drawing, h, 'gf2', fontObject=font)
        self.graphForms.append(self.gf2)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        imageDict[ 'm.gif' ] = ''+\
'R0lGODlhMgAyAPQAAFt4U1p5U1t5U1t6U1x5U1x6U1t4VFp5VFt5VFt4VVt5VVp6VFt6VFp6VVx4VFx5'+\
'VAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAABAALAAA'+\
'AAAyADIAAAWSICSOZFkWSKqqZuu+7SrPCGzDdE7fPITqQFnvFSwKhySj8jhcOlm9p7R2m05tVisuKyVy'+\
'r6ZvNiwGj8rjM9q81ooGbXBcPn9C6tLCD7/c84sJf4KDhIWGh4iJOXeKKyKNjoyQVHCQSZZqjSWam4ox'+\
'iF6FW4QFWIQ8g018SBAEdayZZbAllV+zn263L35BukhAtyEAOw=='        

        return imageDict

new_class = graph_Material
