"""
__graph_product.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
_____________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_product(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 76, 71
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
        self.image_gf0 = PhotoImage(format='gif',data=self.imageDict['p.gif' ])
        h = drawing.create_image(self.translate([25.0, 25.0]), tags = self.tag, image = self.image_gf0)
        self.gf0 = GraphicalForm(drawing, h, 'gf0', 'p.gif')
        self.graphForms.append(self.gf0)

        h = drawing.create_oval(self.translate([25.0, 0.0, 25.0, 0.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        if self.semanticObject: drawText = self.semanticObject.Name.toString()
        else: drawText = "<Name>"
        font = tkFont.Font( family='Helvetica', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([40.0, 60.0, 40.0, 46.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["Name"] = h
        self.gf2 = GraphicalForm(drawing, h, 'gf2', fontObject=font)
        self.graphForms.append(self.gf2)



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

        return imageDict

new_class = graph_product
