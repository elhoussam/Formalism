"""
__graph_Capabilitie.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
_________________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_Capabilitie(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 70, 40.0
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
        self.image_gf15 = PhotoImage(format='gif',data=self.imageDict['cc.gif' ])
        h = drawing.create_image(self.translate([31.0, 23.0]), tags = self.tag, image = self.image_gf15)
        self.gf15 = GraphicalForm(drawing, h, 'gf15', 'cc.gif')
        self.graphForms.append(self.gf15)

        h = drawing.create_oval(self.translate([31.0, 43.0, 31.0, 43.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([31.0, 3.0, 31.0, 3.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        if self.semanticObject: drawText = self.semanticObject.name.toString()
        else: drawText = "<name>"
        font = tkFont.Font( family='Helvetica', size=12, weight='bold', slant='roman', underline=0)
        h = drawing.create_text(self.translate([31.0, 27.0, 31.0, 5.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["name"] = h
        self.gf5 = GraphicalForm(drawing, h, 'gf5', fontObject=font)
        self.graphForms.append(self.gf5)



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

        imageDict[ 'cc.gif' ] = ''+\
'R0lGODlhKgAnAPYAAAFFrQVIrglLrgBGsAVLtAlNswZOuQhPug9QswpRvRNTtBhWtB1athJVuxZZvRtb'+\
'vCFdtiFfvCRhuytlvC5ovTJpvThuvwxVww5Yxw9ZyBZawh1fwxFczBNf0R9hxhlhzBVi1Rlk1Bdl2Rhm'+\
'2xpo3iNjxClmwixpxSVozipryzJswzFuyjtywzVxzDx1yiBo1Clv1y5x1y1x2DR01Dl41xxs4x9v6B9w'+\
'6SFy7CN28iV59id7+Sh9/EJ2xEd6xk19xUJ3yEN5ykp+zFB/xkp/0EN80UyAzlSEzlmHy1yIykyD1UyF'+\
'21OF0laI1FuL1FSK2luO2l+R22WPzmGO0mWR1GuU02+Y1WOT22mW2m2Z3HCX0XKZ1XKc3Hif2neg3Xuh'+\
'2VWM4FyR4HOf4HSg4Huk4YGk2oSp4oqu5I+z6JKy4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'+\
'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAGoALAAAAAAqACcAAAf+gGqC'+\
'g4SFhVeGiYqKFRULEhALEAULBAUFCgEClwoCCwKTEAxAi4kBAKipAASsra6rqKcAAaWFFbOprqwFBr0G'+\
'lqwBwqk/tYMQSUkMAAOsvQfQGkQGCS4qQC4SDw+3s8ZqPlJGExM9Qg4rQiklTC4lZkwlK0FNLk5fJioP'+\
'PxNJxgxaFBBIEOSLEi5XuKSAwqUIGihQnChxQoWKFRdIqkiR8sCYhCoNDDigkmYKlhRZnnA580QMCi9X'+\
'nkC50kTJCZJaqlCopaAAkilBmGCB6QWKGDFhyIBBE+VKFJlXnGBxQYVLEBUFWJR6QKDBkXhKoLQYg4WG'+\
'jDBLZIAJA2OGjBj+M1AoabHOiYoDKhZRYHUgwYULGTh8WPIChGERIkAkNsyhQ4cMGTBcSJDAQIFFLAj0'+\
'/XuBQ+MQh0WMGI24NIjHkTkfKEDKEJQNBKj9Dcwh9OgauEnoNg0CcuoDBk4k2tIA2l/PHQ7fxs089wjE'+\
'hh9LBu4gUQkDBzgjVzyCBHMbN27YsIG7O/TAGf5WzltIAvbZjbl7rxH+Bg4c4ceXXwz5Aob1hiSwWWfx'+\
'jeYdeDjkoKCC+JFHQmIdeCYZZQYU4kMBm2GAQW0g3AbeDTnooMMODIpXw4MQpkZZAUIQ0oBmfm3IYXc1'+\
'IBjiDjzsoEMO+OW2GAeRCWiAAoNs4cBAMXr+ZhiN4CmIY4473mfDbqd5pp5IUggyASuU+adkhyPgBuKN'+\
'OEbp4HNVBlkZAR2pwUIzshG45IFjirgjjzg4SEJ0HEg2GSvsCcCXX4DNGGaN9i3IIHkn7gmCZ+mtSYAA'+\
'amixSmyEyrgkk/bdlx+jaEbIgXoHsAKAEWMwAGeGgRnW4YE15EmefjVA92ifV7LCQg+CLCAQNX7Rppxu'+\
'8zW3249ATpYAAQ4sUEgEBSAJH4dgdkcsiotFmJqyCbBXSBUPxIlBYMmFJtpoIyjGZ3/KSlBGKSo0QKiX'+\
'1LqqrquQpvcfQd+c8ECm435ZbpW3QqZhAht8M0gXGnTpH22eRRzxtglXaCCcwoQ00TBn/mmooZXJqqcE'+\
'xoY0cYLDnPnJMWUaVEGyIucAO6+ykzlgxMu1lEDZzgL2XALO3+jTSqkGSHAx0MZQAcGLBCjQgAtIk4zE'+\
'JlpFjTMiQAcCADs='        

        imageDict[ 'c.gif' ] = ''+\
'R0lGODlhPAA4APcAAAFFrARIrwpLrgVLtAxOsQdOuQhPug1QtQpRvRNTsxlWthtZtRJVuxZZvhxbuyFd'+\
'tiVhuipkuzBnujNquwxVww5Yxw9ZyBZbwxpewxFczBlfyRNf0R1gxRtizRVi1Rxl0hdk2Bhm2xpo3iNj'+\
'wylmwyxpwiRmyidqzixtzzNswzpvwDVwxz1zxTRxzjx3zyZs1Stu0zZ21Th20Tx51Bxs4x9v6B9w6SFy'+\
'7CN28iV59id7+Sh9/EN2w0p7xER6ykx+y1B+xUR91UN/2FKDzFiFzFyIyEuC00OA2kuE21SG0VWJ11uL'+\
'1FOK3VuN2V2Q3mGMzWeRz2+Vz3CXz2aS1WyW1G6Y12KT3WmV2W+Z2HSa0nKc236h13qi3lyR4XKg5Huj'+\
'4H6o5nSn8YWm14Sm2YWo3Y2t3JSx3Ji134Gn4IKp44qt446x5JS05Jm345u45JO26pu66ZO485W++pi/'+\
'+qG85KO/6p7E/aTA56vC5abB6a3F6a/I7bHG5rXJ57DH6bPK67rO7L7S77XP97rP8LnR98LT68jX7cPW'+\
'8sbY88va8NPf8d7n9uXs+Ovy+wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'+\
'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'+\
'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'+\
'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'+\
'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'+\
'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'+\
'ACH5BAEAAI4ALAAAAAA8ADgAAAj+AB0JHEiwoMGDjuYgXMiw4cA4As5EASBFDIAeEyHwEEAgAoEFHgE8'+\
'SAAgQoSSQABIkELggZgJQQg5ZPgEgM2bOAEE2BlAJ08AA4DqzJnzycyFRG/yDDCgqdOnTn0mtXn0YJak'+\
'PKE2LVBgQNeuUKXmLFS14AScPYE6/cq1rVu3UNPenFCWIIAJZsxEYLq2LYK/CAwwWPPXwAotDsoUaDMg'+\
'RdMzO2/WFSjlQaIJE8b0LWDAAAXAny/U+YzgwogRbQqsMOCnaYqfAPhMXlCmB18FgApVMaCFTKArFLQE'+\
'AsThwqA9fzS0uIIagZofjPiMWDOABSA+CxLU7YndKQIGBv7+UCDDpUKgCxoqGOGigdGFJl98gDHhhsIe'+\
'BPdZDwB0QEKZAHUVEQAeDgzQGQN0/LEIB2q4UAEbLTQxyCBsdLCHBSfkMUMaJ7hRwR4U/PGXHw0sggce'+\
'fQRwRlkHBDDGEAYasMQUFOhhghpGWAAHCoNkMAMcH/SIAhxCcAhHBeKJh8AfDADiQAMM7FTVAkw5kEgS'+\
'SayRBBtGMHKCGnkIcUgGiAgBB5CNMPGGE0XCAIcFf1gQiBIXiLhHEiz80JQYR/HgFAlkkDECBVx8oUQH'+\
'alixRgwbHPEGEkx40AUYXngAAxIfMJGBExbI8IUJSiDQABdqpNAVFDP14JQBoFFQgQX+sKoxwwYbeGDr'+\
'rbjemkEGG2QAqwUVUEAaWAPMBMFWrArrKqy7IvFCriBEK22utPbqa7DCAtbUGA0pcixXfynLbLW3hgBC'+\
'COiee266H4Bg666+wqrsX1350JASWxWAgLAVvApvueuiKwINNIhgcLrR6rorsNkiwFUDYTDUhVes7rvs'+\
'v7aiK3DBBBM88MHmuvvurv02zBUbCyliqr4WU2DBrrXaGjDHHdfssQjpKszwsAWUwBBXyQo7bswa22wD'+\
'DTYkjXTHBouQsAfw7uxwVwvpCa7FL/Mq88YEJ32D1zZ8ffTN074rNb10IMSCV+G6/DKtGYdgcNdh32D3'+\
'3WKPfbD+u7UuPC9XKSDkFctCv13rujV7fQMOjDOOd83TRt1vYVQblMXg4fZruAcaD1yD143jkEPjdidt'+\
'A8h8L2yByQPgYRARmPNbAa9Ey03w53YzrkMOOuw+eukd52w2sIABbhCyFvurNechdFxD7qLnsMMOvjuu'+\
'dME59wprsPRWPlAZ+X52cQbl2o574zpMP/3uONytt7keVHstzwP0QdAUWwGmOczMN09DDecTXfrWN7r2'+\
'fa1ge4vfwiqwr8B0JQIE2Qnbkjc7uPXvdnXLgQapR70Cis1j6LKV9hjWvaYMBA98udr4auc86GnwhaT7'+\
'YAIVuD3SGAAsgKCMBFWovJity3P+dVuc6ELXvusdTGckvGFTAqAAgdgEeVh729b8RzC8OY50NqhB8EIY'+\
'P+2VbGpLJIAjCpGW/CUva4f7YcfwhrewjQ2EfLMWtko4gJ0UQg1PRJ64YFa7gVVRcY/TGw24SKv5ZYsr'+\
'SwSAAOQAhZ4whTNB6+EUqdi1pdlskFxUoCHptUQIyEYgV1kV4V6FRg9Ea2N+vCQIhVfIGpaQKQeBkRn5'+\
'hcaY9c92CGQazkLWxQXO8YZdMcNCDjBLWm5AA3Bzl8bk1rRdakxkvQTWF+nFgGIxBA8RUGHhNiezUwYM'+\
'YabsorWkecgCsCARR4mduIZ2q6eFgHPQFKfqVtcwBPisLG7aAE8BlOU2eFXLlrkSYSEXyM/AuG4yjmAA'+\
'4VxFSsP9M37iLKQG4oUtCujLXggVSCKW4LC2NdSfvAqpteYZLO4FxgUZLcgIGlAxZfXro1lTHUULigAj'+\
'TCGlBhEEElrlKoaSsqHbe1VBDTACOeAUIVS4gGc8w8+SlZShNEUAB9pwVIbkAZLJaiA/51XPv1R1Jn4Y'+\
'AWcAE64GkrUwDPDDV6vC0hsW762d6QwL1loXQLzlrm0hA10R+gRi5ssrXtHCXlP6H61UZ7BHdUOLdrIF'+\
'xK41AQ9oomPXaofBBgQAOw=='        

        return imageDict

new_class = graph_Capabilitie
