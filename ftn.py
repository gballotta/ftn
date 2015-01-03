__author__ = 'GiovanniMusic'

import MaxPlus
from ftntag import FtnBaseTag
from ftnselector import FtnBaseSelector

class FtnTag(FtnBaseTag):
    def getfromnode(self, node):
        self.classes = []
        propsbuf = MaxPlus.WStr()
        node.GetUserPropBuffer(propsbuf)
        self.parse(str(propsbuf))
        self.getclasses()

    def puttonode(self, node):
        propsbuf = MaxPlus.WStr(self.renderpropbuffer())
        node.SetUserPropBuffer(propsbuf)


class FtnSelector(FtnBaseSelector):
    def __init__(self, inodescollection):
        super(FtnSelector, self).__init__(inodescollection)
        self.tagger = FtnTag()
