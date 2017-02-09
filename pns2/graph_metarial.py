"""
__graph_metarial.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
______________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_metarial(graphEntity):

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
        self.image_gf8 = PhotoImage(format='gif',data=self.imageDict['m.gif' ])
        h = drawing.create_image(self.translate([25.0, 25.0]), tags = self.tag, image = self.image_gf8)
        self.gf8 = GraphicalForm(drawing, h, 'gf8', 'm.gif')
        self.graphForms.append(self.gf8)

        h = drawing.create_oval(self.translate([24.0, 50.0, 24.0, 50.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([10.0, 44.0, 10.0, 44.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([37.0, 45.0, 37.0, 45.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([27.0, 1.0, 27.0, 1.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([12.0, 5.0, 12.0, 5.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([41.0, 7.0, 41.0, 7.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        if self.semanticObject: drawText = self.semanticObject.Name.toString()
        else: drawText = "<Name>"
        font = tkFont.Font( family='Helvetica', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([27.0, 22.0, 27.0, 16.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["Name"] = h
        self.gf12 = GraphicalForm(drawing, h, 'gf12', fontObject=font)
        self.graphForms.append(self.gf12)



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

new_class = graph_metarial
