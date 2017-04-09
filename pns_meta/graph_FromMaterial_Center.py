"""
__graph_FromMaterial_Center.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
_________________________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_FromMaterial_Center(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 62, 21
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
        if self.semanticObject: drawText = self.semanticObject.Rate.toString()
        else: drawText = "<Rate>"
        font = tkFont.Font( family='Helvetica', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([37.0, 16.0, 37.0, 11.0])[:2], tags = self.tag, font=font, fill = 'red1', anchor = 'center', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["Rate"] = h
        self.gf33 = GraphicalForm(drawing, h, 'gf33', fontObject=font)
        self.graphForms.append(self.gf33)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        imageDict[ 'p.gif' ] = ''+\
'R0lGODlhMgAyAPecAGatqGetqGasqWesqWatqWetqWeuqGauqWeuqWesqmatqmeuqmitqGitqWiuqWit'+\
'qmiuqmmuqm6xrW+xrnCyrnGyrnGyr3Kzr3OzsHS0sHW1sXa1sXa1sne2sni2sni2s3m3s3q3tHu4tHy5'+\
'tX+6toC7t4G7t4G7uIK7uIK8uYvBvozBvo3Bvo3Cv47Cv4/DwJDDwJHEwZPEwpXGw5bGxJfHxJjHxZjI'+\
'xZnIxZrIxprJxpvJxpvJx5zKx53Kx53KyJ7LyKDMyaHMyqHNyqLNyqPNy6TOy6TOzKfPzafQzanQzqrR'+\
'z63T0LDV0rHV07LV07LW07PW1LTW1bTX1bbX1rva2bzb2cDd3MLe3cTf3sXf3sXg3sbg38fh38jh4Mni'+\
'4cri4cvj4c3k48/l5NDm5NHm5dLn5tPn5tPo5tTo59Xo59bp6Nfp6Njq6dnq6dnr6trr6tvr6tvs69zs'+\
'697t7N/u7eDu7eHv7uLv7uPw7+Tw7+Tx8OXx8Obx8efy8ejy8ujz8unz8+rz8+v09Oz19O319e729u/2'+\
'9u/39vD39/H39/H49/L4+PP5+PT5+fX6+fX6+vb6+vf6+vf7+/j7+/n8/Pr8/Pv9/fz9/f3+/v7+/v7/'+\
'/////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'+\
'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'+\
'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'+\
'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'+\
'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'+\
'ACH5BAEAAJ0ALAAAAAAyADIAAAj+ADsJHEiwYMEIBRIqVGiwocOHDRdKnFgAokWIFDNSvMixk8aEFkCA'+\
'sPCxYkeHFDsEAcPHEqeXnCzxARMkxMaTBCdG2AEHps+fL+HsQCgRp0eJNQIBXfozkI2JJyWCWMOUEyVF'+\
'hyZVPdOh6EWJMRoBrePEBUmFFlw4qQOUkYsBCiNYlBgEaBYTBQAUIDrRRBagPbyiVNjjJxwSeksqPNHT'+\
'Z2CGgxO6+NlEMcUIUX6+WBhRIQixLy3tmJiYr0YeLl8q6go5p8I0PkdPtICE5aRGh8QsyUBxh88znF0n'+\
'9A3TicQIFqxoXWqpSwfTBTLDfNr66F6lQaHLUFQVZiPqcRv+cwrEd+BC4i9JSNyRunvoJBJJxG69UDwW'+\
'iZPdA5WtsAvMNcF55hNeaB2iH1CTgLDQCT6xZlJCEdT1Uh0SVXHgUl1IxNZLQTC0EBjFLTTBchf+pKBC'+\
'0nGSYVwK8QGTC4kVAESJSzGxUH6c5MGiQu2dlZB/NP4kBl8YwGQJdAVYABMlEuUR5E+HSETiCBOBAFOU'+\
'C2H3JExwKWRgelXCpMhCEXy5pVVdJsTdSycW0KWSLzG5EB1nvhSIRJXA5ONCPS4E5JlqLAQnJ5UgWYCL'+\
'L7nA14x1KnEjTDoqlCaILxmn0ASU1NlmAU7ABIZCAFgnISd3SGTFmffFdQdMHSYkkEL+HfiEgohmlpjg'+\
'QiY0CFl9MK2o0AvtXSiDRJRyAkeACtlgZAnrlWgJfAuhMJ+r5kGopRzQuVArU5MMS6Z4fAT3qkLocWLp'+\
'QhlUQSJQVzwnUYqceEtttQmdMa1EKoGRR1Z3jIHEnoT9Ji69BXSwyL2WTVQYTIs4aFJBNwYbhaEfRRAB'+\
'FT5Z4sLAECvEKExyEJhwCXT6BATHHXscLCdZzFrSCX/CxN9ec90Imk93RPGCwxi8EMWqPymigmAYLdQB'+\
'GlVZMskhK//m8MNfkSmDliXyUQNUOEEXQQ3iuZeGDUgaRbBCGQTRRUsZ50HT0/OKPa5GE3QAwgQVu91Z'+\
'wljb/RAJ3lDrHXVGdgcEADs='        

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

new_class = graph_FromMaterial_Center
