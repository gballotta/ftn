__author__ = 'GiovanniMusic'

from ftntag import FtnBaseTag

class FtnBaseSelector(object):
    def __init__(self, inodescollection):
        """
        self.tagger  la classe Tag da utilizzare.
        Qui viene utilizzato FtnBaseTag ma nella versione per 3d studio
        va rimpiazzato con il tagger appropriato
        """
        self.tagger = FtnBaseTag()
        self.selection = []  # lista contenente tutti gli INodes selezionati
        self.inodescollection = inodescollection

    def select(self, selector='*'):
        self.selection = []
        self.executecommands(self.parseselector(selector))
        return self.selection

    def parseselector(self, stringa):
        return stringa.split(',')

    def executecommands(self, comandi):
        for i in comandi:
            if i[0] == '&':
                self.selectionand(i[1:])
            elif i[0] == '|':
                self.selectionor(i[1:])
            elif i[0] == '!':
                self.selectionnot(i[1:])
            else:
                self.selectionsel(i)

    def selectionsel(self, cid):
        for i in self.inodescollection:
            self.tagger.getfromnode(i)
            if self.tagger.hasclass(cid):
                if i not in self.selection:
                    self.selection.append(i)

    def selectionand(self, cid):
        filtrati = []
        for i in self.selection:
            self.tagger.getfromnode(i)
            if self.tagger.hasclass(cid):
                filtrati.append(i)
        self.selection = []
        self.selection.extend(filtrati)

    def selectionor(self, cid):
        self.selectionsel(cid)

    def selectionnot(self, cid):
        for i in self.inodescollection:
            self.tagger.getfromnode(i)
            if self.tagger.hasclass(cid):
                if i in self.selection:
                    self.selection.remove(i)