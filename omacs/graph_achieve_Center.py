"""
__graph_achieve_Center.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
____________________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_achieve_Center(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 55, 21
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
        font = tkFont.Font( family='Helvetica', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([40.0, 20.0, 40.0, -10.0])[:2], tags = self.tag, font=font, fill = 'green', anchor = 'center', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["rate"] = h
        self.gf26 = GraphicalForm(drawing, h, 'gf26', fontObject=font)
        self.graphForms.append(self.gf26)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        imageDict[ 'Agent.gif' ] = ''+\
'R0lGODlhRgBGAPekAJ2uK52vK56uKp6uK56vK5+vK52vLJ+uLJ6vLJ2wK56wKp+wKp6wK5+wK5+wLJ+w'+\
'LaCwLqCxL6CxMKGxMaGyMqKyM6OzNaOzNqOzN6S0N6S0OaW1Oqa1PKa2PKa2Pae3P6i3QKi3Qam4RKq5'+\
'Raq5Rqu5Rqu6R6u6SKy6Say7Sq27S628TK68Ta68Tq+9ULC+UrC+U7G/VbK/VrLAV7PAWbPBWrTBWrTB'+\
'W7TCXLXCXrbCX7bDYLfEYrfEY7jEZLjFZLnFZbnFZrnGZ7rGabvHab3Ibr3Jb77Kcr/Kcr/LdMDLdcDL'+\
'dsHMd8HMeMLMecLNesTOfcTPf8XPgMXPgcbQgcfRhMfRhcfRhsjShsjSh8nSicvUjMvUjszVkM3Wkc7W'+\
'k87XlM/Xlc/Xls/Yl9DYmNHZmtHZm9LanNLantTcodXco9XcpNfeqdjfqdjfqtnfq9ngrdrgrtvhsNzi'+\
'stzis93jtd7kt9/lud/luuDmvM3Nzc7Ozs/Pz+LnwOTpxOXqxubqx+bqyOfryufry+fsy+jszOjszens'+\
'zuntz+ru0eru0uvu0+zv1e3w1+3w2O3x2e7x2u/y3fHz3/L04vL04/L15PP15PT25vT25/X36vb47Pf5'+\
'7vj58Pr78/v89vz8+P39+/3+/P7+/f///v///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'+\
'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'+\
'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'+\
'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'+\
'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'+\
'ACH5BAEAAKUALAAAAABGAEYAAAj+AEsJHEiwoMGDA/UQ5IOwocOHEBsyTEhQoUA9FiNq3Ogw40Y+HjmK'+\
'PAhypMmTIws0CFCgAMsAEFxCgIlQz0SUEEMKjBmgp8uXP3sCDYDz5M1SQ10qVZq0qcGjRREynfqyKVWl'+\
'MyvqRBnyqtClWOSg+YJFCQugCJxGdTi0Jwczgi5BqlrAUpgSMuR4YfrCglqKa5FSlWFJCQQIkkJU5RSl'+\
'Jw4gQFFMctKyKoSFUDViJMiTKYRLUSp3QPCzASglAYDIGMoDVCCfdIni9Liy7Y5Ril0iQHCBdIZRgeg8'+\
'wgH7wCEzj1jaODuT5eW1tZkGQOAEt0sXZx55SVtilIwHc1r+VI3ihcmlnhYuqYn583kpPpkjukTRgSVT'+\
'HaOIsPxw2wbLF6OUgEAJFKxUgAWLVADEJwg0AMQbisFWwEAlQQTfQD8JwtgBQFGQSR5LSRKGSz+MgkFP'+\
'NFAWQBiUzTAKBRAc8gFMFUgn0k1AeZHIJ4e88JUSo2DhUxyHBNBCIKN4gYUTdmBRwguEQPBAdyGQlxYK'+\
'mVAx1ElMoZAHCn+AYgYFPzmRSSNz/BGHYrt1gIIMQCiBQgt/qNHTbzYkQmYAWuCAxRkHLEWhRpW9xAgF'+\
'ISySiSVEHDATBC68sGdQlKYFRHOgHMLEVBQ8kgcFPiW01XsDAaXUGWbY8UEHbYDSSAn+0tHlFVOaJJIW'+\
'U3ZwgkQe9fWUE4Zt2XAITyvwKqGpsU3lkhn+MWXGJ/4B8QhPG81EFQSNWHvYrBJ6hWxLUYyCWgBtFCFo'+\
'RFaRW8Rq6S6V7LdCpQYKF/Z15qtAFR50rFJVLFJCu8l6u5QSUXTSBmk93QoUQjfV1tQPoHLrrsRAQdDG'+\
'tABDFJ1VFP/UMV1bwNouRNwCrKzJbRVgbbru6cThrB97jPLE+1Z8kcslxxzzzAsvlFHNNFPM884usZXz'+\
'zETzLJtU7e489NANHDAoQU8nbbVa+Qp09dZVs+QzhlyHjfK9+nYt9s7uGWT22lanXRDQbMdNlUMNnC33'+\
'yPjadNPuy3fbPXfeBVnr99hXzfqQzIPD3FS6D9nXN+FJeUVSRog/rjhVVlFo0YWlJg6wyUxpzrTnl6dr'+\
'n0aWQ07xRqlL/LHUDdk0UFqRKz340rIXBFVl0ulsue4QKRz0535PmFLKSD/OkUfd2i532rkz3NW7rt+9'+\
'9HujOjT80WGvRX3TcTeAUtaCLR42VQ1An/3kau8rdlvXl7JZVDTLPRUCgSG0Me9rV5X/1G8r1Pnid5H4'+\
'LK8hcNuZ+P7HEYT5zmsMjJ0BBTK2ACywJhPESQYD6LEIavB/64tgCG/kQY1skCQnLCHwblYR0V1EhR8s'+\
'IAwDAgA7'        

        imageDict[ 'aa.gif' ] = ''+\
'R0lGODlhMQAxAPcAAJyuJ5yuKJ2uKJyuKZ2uKZ2vKZ6uKZ2uKp2vKp2vK56uKp6vKp6vK5+vK56vLJ+v'+\
'LJ+vLZ+wK5+wLJ6wLZ+wLZ+wLp+xL6CwLaCwL6CxMKGxMKCxMaGxMaCyMaCyMqGyMqGyM6KyMqKyM6Ky'+\
'NKKzNKKzNaKzNqOzN6O0OKS0OKW0OKS0OaS0OqW1OqW1PKa1PKa2Pae2Paa2Pqe3P6e3QKi3QKi3Qam4'+\
'Qqm4Q6m4Ram5Raq4RKq5Raq5Rqu5R6u6R6u6Say7Say6Sqy7S627TK28TK68Ta68Tq+9T7C+UrC+U7C+'+\
'VLG+VLG/VLK/VbK/VrLAV7PAWLPBWrPBW7TCXLXCXrbCX7bDYLfEYbfEYrjEYrjEY7nFZrnGZ7rGZ7rG'+\
'aLrGabvGabvHabzHbLvIa73Ibr3Jbr7JcL7Jcb/KcsDLdcHLd8DMdsHMd8HMeMLNesPNe8POfcTOfcTP'+\
'fsXPgMXPgcbPgcXQgcfRg8fRhcjShsjSh8jSiMnSiMnTisrUjMvUjMvUjcvUjszUj83Wkc3Wks/Xls/Y'+\
'ltDYmNHZmtHZm9LandPandPbn9PboNTboNXco9bdpdfep9jfqdjfq9ngq9vhr9vhsNvisdzisdzist3j'+\
'tN3jtd3jtt7ktt7kt9/kud/lueDluuHmvOHmvc3Nzc7Ozs/Pz+PowePow+Xqx+bqyOjszAAAAAAAAAAA'+\
'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'+\
'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'+\
'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'+\
'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'+\
'ACH5BAEAAK0ALAAAAAAxADEAAAj+AFsJHEiwoEGCpQ4qXMjwYMKGECMqfCixosWCEhhoZCAho4OPFy9q'+\
'zLhRIwAGJ0tqDNlQ5UYHRqhAMTLDQUmQAimyLPmBSp9HTzR62QSGTZwLDD7cIFGSJcGXEugEulGGCsoo'+\
'm1oYiYL0g6FCJHG20rmQYoSSQD71SEriA4MrrPr0QaGxx6VPH2bckHDWQcgLJDVSQTWDwZRJXgCkuRTF'+\
'jVsJbvJc+jDkERGNDi7kjMiARqArNhn0UHWFQYpLaRjQYSSBhhEJSe4YAdVCDZgPJCVAPCVQ441Pqwbd'+\
'YHBhUKYnNhD1acFoEhg3sgvR/JQlD4kehaDY1M1ZI53Fqcr+fCDhJpGeNDVJzOjxhH2eFh9IPYoCYAiU'+\
'PmlIbla4EQAYQG6wAYoka33glksa4SYBKIa4BUAPnzAiHgMNhabRDIwUdoUXSCGokgMSeLEWAzNMUsgN'+\
'hSSx0kIWchTIEwd6+OFHGkVwAiKSwAfjivyppIZjMgbJwBCJZHJDSk0dhOAMMQqJ4AdyjOFhj05WyVML'+\
'CPqlpJVcCrkZRV2GOeWWYpa5EZlmlrlfb2maeVBgbXLJXUFxijknQWfV2eVAvLGpp5UD6dTinzJGQCWh'+\
'Qd45lp+Iyshdn081KiNDkk5KaaUuHQTpoJUGulCemEoEJ6ISaLaoQwNhSqFAkF7aaEU8YBJq6qkM6TRq'+\
'mRHcSVZEoKbpFFm+IuQUQZwiGMFZwxq0ayuOKrpmsgtRuCq0EC1bLbXDtortQn1aa1FAADs='        

        return imageDict

new_class = graph_achieve_Center
