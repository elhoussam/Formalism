"""
__graph_fromRaw_Center.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
____________________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_fromRaw_Center(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 57, 21
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
        if self.semanticObject: drawText = self.semanticObject.rate.toString()
        else: drawText = "<rate>"
        font = tkFont.Font( family='Helvetica', size=12, weight='bold', slant='roman', underline=0)
        h = drawing.create_text(self.translate([28.0, 10.0, 28.0, -31.0])[:2], tags = self.tag, font=font, fill = 'springGreen4', anchor = 'center', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["rate"] = h
        self.gf4 = GraphicalForm(drawing, h, 'gf4', fontObject=font)
        self.graphForms.append(self.gf4)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_fromRaw_Center
