__author__ = 'GiovanniMusic'

import unittest
import ftnselector
import ftntag


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.alfa = {'ftnclass': ['legno', 'finitura']}
        self.beta = {'ftnclass': ['legno'], 'vray': ['si']}
        self.gamma = {'ftnclass': ['finitura', 'metallo']}

        class FtnTagMock(ftntag.FtnBaseTag):
            def getfromnode(self, node):
                self.classes = node['ftnclass']

        class FtnSelectorMock(ftnselector.FtnBaseSelector):
            def __init__(self, inodescollection):
                self.tagger = FtnTagMock()
                self.selection = []  # lista contenente tutti gli INodes selezionati
                self.inodescollection = inodescollection

        self.classe = FtnSelectorMock([self.alfa, self.beta, self.gamma])

    def test_initialization(self):
        self.assertEqual(self.classe.inodescollection, [self.alfa, self.beta, self.gamma])

    def test_parseselector(self):
        risultato = self.classe.parseselector('alfa,sandro')
        self.assertEqual(risultato, ['alfa', 'sandro'])

    def test_selectionsel(self):
        self.classe.selectionsel('legno')
        self.assertEqual(self.classe.selection, [self.alfa, self.beta])

    def test_selectionand(self):
        self.classe.selectionsel('finitura')
        self.classe.selectionand('metallo')
        self.assertEqual(self.classe.selection, [self.gamma])

    def test_selectionor(self):
        self.classe.selectionsel('finitura')
        self.classe.selectionor('metallo')
        self.assertEqual(self.classe.selection, [self.alfa, self.gamma])

    def test_selectionnot(self):
        self.classe.selectionsel('legno')
        self.classe.selectionnot('finitura')
        self.assertEqual(self.classe.selection, [self.beta])

    def test_executecommands1(self):
        self.classe.executecommands(['finitura', '&metallo'])
        self.assertEqual(self.classe.selection, [self.gamma])

    def test_executecommands2(self):
        self.classe.executecommands(['finitura', '|legno'])
        self.assertEqual(self.classe.selection, [self.alfa, self.gamma, self.beta])

    def test_executecommands3(self):
        self.classe.executecommands(['finitura', '!metallo'])
        self.assertEqual(self.classe.selection, [self.alfa])

    def test_executecommands4(self):
        self.classe.executecommands(['finitura', '|legno', '!metallo'])
        self.assertEqual(self.classe.selection, [self.alfa, self.beta])

    def test_functional_select1(self):
        risultato = self.classe.select('finitura,&metallo')
        self.assertEqual(risultato, [self.gamma])

    def test_functional_select2(self):
        risultato = self.classe.select('finitura,|legno,!metallo')
        self.assertEqual(risultato, [self.alfa, self.beta])


if __name__ == '__main__':
    unittest.main()
