"""
__graph_operatingUnit.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
___________________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_operatingUnit(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 107, 19
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
        h = drawing.create_rectangle(self.translate([0.0, 0.0, 107.00000000000004, 19.0]), tags = self.tag, stipple = '', width = 4, outline = '', fill = 'black')
        self.gf3 = GraphicalForm(drawing, h, "gf3")
        self.graphForms.append(self.gf3)

        h = drawing.create_oval(self.translate([23.0, 18.0, 23.0, 18.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([71.0, 19.0, 71.0, 19.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([22.0, 3.0, 22.0, 3.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([67.0, 1.0, 67.0, 1.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        imageDict[ 'd.gif' ] = ''+\
'R0lGODlhMgA0APZWAHGjU3KjUnOjUnKiU3KjU3OjU3GkU3KkU3OkU3GjVHOiVHKjVHOjVHKkVHSkVXWl'+\
'VnamWHinWnupXn2qYH6rYoGtZYOuaIWvaoWwa4mxb4qzcIy0c421dI61dZK4epS5fJa6f5i8gZ6/iJ/A'+\
'iqXEkaXFkqbFkqjGlK7KnbHMoLLNobTOpLjQqLvTrL7Ur7/VscTZt8fausfbu8jbu8rdv8zdwMzewc3e'+\
'ws7fw9DgxtHhxtTjytXkzNflztjm0Nnm0dvo0+Hr2uLs2+Pt3ebu4Onx5Orx5ezy5+3z6fH27fH27vP3'+\
'8PT48vf69fj79/n7+Pv8+vz9+/z9/P3+/P7+/v7//v///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'+\
'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'+\
'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAFcALAAAAAAyADQAAAf+gFeC'+\
'g4SFhQIEiYqJB4aOj5COi5OUBJGXkZWalZidVweboZONno+ip5OlhaisqaqtsIqlsbSWmAu1tJe4ubqQ'+\
'vbWQvMCwC5LEuYbIyYQ0Mc/QMTc51NXW19Y8P9vc3d4/M4QmVuTl5ufo6erpURmEBD/r8vP0K7ZXiRZO'+\
'9Pz9VkMPEglSpMKfwXUbZOFLtGDIwYflXCxaqGgDxIdHIDRQ1ADUIhcXDYY4BeFISH4xUDUAcXKeEgmt'+\
'brRcNwLWBCUz0eWgNS5nOScWasXzaeVELn0+gQArONMJBlEUKS1oODMF1KiVNLQMEjDUQFEwooRMGMoY'+\
'1koRTEJkgWrQKZaFGLt6dXuKxkMQbd+JkrDEIIy8ekX15JcE5qljonj0EwF41Smk826gMos4FNN1TCY0'+\
'rqzpgcN1Jk6R2iVqg9h0PDZnEvUi3ZOnV2eFKokOxTBNquhuglsuyMa5uXVXkkkuigbgwR1TmtDXClvc'+\
'yVffHndE7sTonhAp2uFh0Wjs4MOLH38lEAA7'        

        return imageDict

new_class = graph_operatingUnit
