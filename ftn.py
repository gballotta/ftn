__author__ = 'GiovanniMusic'

import MaxPlus
from ftntag import FtnBaseTag

class FtnTag(FtnBaseTag):
    def getfromnode(self, node):
        propsbuf = MaxPlus.WStr()
        node.GetUserPropBuffer(propsbuf)
        self._parse(str(propsbuf))
        self._getclasses()

    def puttonode(self, node):
        propsbuf = MaxPlus.WStr(self._renderpropbuffer())
        node.SetUserPropBuffer(propsbuf)
