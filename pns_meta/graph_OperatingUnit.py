"""
__graph_OperatingUnit.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
___________________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_OperatingUnit(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 163, 21
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
        h = drawing.create_rectangle(self.translate([0.0, 4.0, 93.0, 19.0]), tags = self.tag, stipple = '', width = 1, outline = '', fill = '#000000')
        self.gf9 = GraphicalForm(drawing, h, "gf9")
        self.graphForms.append(self.gf9)

        h = drawing.create_oval(self.translate([22.0, 5.0, 22.0, 5.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([44.0, 4.0, 44.0, 4.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([71.0, 4.0, 71.0, 4.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([21.0, 19.0, 21.0, 19.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([44.0, 19.0, 44.0, 19.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([70.0, 19.0, 70.0, 19.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        if self.semanticObject: drawText = self.semanticObject.Name.toString()
        else: drawText = "<Name>"
        font = tkFont.Font( family='Helvetica', size=12, weight='bold', slant='roman', underline=0)
        h = drawing.create_text(self.translate([127.0, 10.0, 127.0, -31.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["Name"] = h
        self.gf16 = GraphicalForm(drawing, h, 'gf16', fontObject=font)
        self.graphForms.append(self.gf16)



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

new_class = graph_OperatingUnit
