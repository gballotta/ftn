__author__ = 'GiovanniMusic'

import unittest
import ftntag

class MyTestCase(unittest.TestCase):

    def setUp(self):
        class Tag(ftntag.FtnBaseTag):
            pass

        self.classe = Tag()
        self.daparsare = "ftnclass = alfa,sandro\r\nftnid = uno\r\naltro = qualcosaltro,altroancora\r\n"

    def test_parse_caso1(self):
        self.classe._parse(self.daparsare)
        caso1 = {'ftnclass': ['alfa', 'sandro'], 'ftnid': ['uno'], 'altro': ['qualcosaltro', 'altroancora']}
        caso2 = self.classe.propBuffer
        self.assertEqual(caso1, caso2)

    def test_parse_caso2(self):
        daparsare = ""
        self.classe._parse(daparsare)
        caso1 = {}
        caso2 = self.classe.propBuffer
        self.assertEqual(caso1, caso2)

    def test_parse_caso3(self):
        daparsare = "cognome = ballotta"
        self.classe._parse(daparsare)
        caso1 = {'cognome': ['ballotta']}
        caso2 = self.classe.propBuffer
        self.assertEqual(caso1, caso2)

    def test_getclasses_caso1(self):
        self.classe._parse(self.daparsare)
        self.classe._getclasses()
        caso1 = ['alfa', 'sandro']
        caso2 = self.classe.classes
        self.assertEqual(caso1, caso2)

    def test_getclasses_caso2(self):
        self.classe._parse("cognome = ballotta")
        self.classe._getclasses()
        caso1 = []
        caso2 = self.classe.classes
        self.assertEqual(caso1, caso2)

    def test_hasclass_true(self):
        self.classe._parse(self.daparsare)
        self.classe._getclasses()
        caso1 = self.classe.hasclass('alfa')
        self.assertTrue(caso1)

    def test_hasclass_false(self):
        self.classe._parse(self.daparsare)
        self.classe._getclasses()
        caso1 = self.classe.hasclass('teta')
        self.assertFalse(caso1)

    def test_addclass_new(self):
        self.classe._parse(self.daparsare)
        self.classe._getclasses()
        self.classe.addclass('teta')
        caso1 = ['alfa', 'sandro', 'teta']
        self.assertEqual(self.classe.classes, caso1)

    def test_addclass_exists(self):
        self.classe._parse(self.daparsare)
        self.classe._getclasses()
        self.classe.addclass('sandro')
        caso1 = ['alfa', 'sandro']
        self.assertEqual(self.classe.classes, caso1)

    def test_removeclass_exists(self):
        self.classe._parse(self.daparsare)
        self.classe._getclasses()
        self.classe.removeclass('alfa')
        self.assertEqual(self.classe.classes, ['sandro'])

    def test_removeclass_notexists(self):
        self.classe._parse(self.daparsare)
        self.classe._getclasses()
        self.classe.removeclass('teta')
        self.assertEqual(self.classe.classes, ['alfa', 'sandro'])

    def test_updatepropbuffer_hasclasses(self):
        self.classe._parse(self.daparsare)
        self.classe._getclasses()
        self.classe.addclass('teta')
        self.classe._updatepropbuffer()
        self.assertEqual(self.classe.propBuffer['ftnclass'], ['alfa', 'sandro', 'teta'])

    def test_updatepropbuffer_hasnotclasses(self):
        self.classe._parse("cognome = ballotta")
        self.classe._getclasses()
        self.classe._updatepropbuffer()
        self.assertFalse('ftnclass' in self.classe.propBuffer)

    def test_renderpropbuffer(self):
        self.classe._parse("cognome = ballotta,berruti\r\n")
        self.classe._getclasses()
        caso1 = self.classe._renderpropbuffer()
        self.assertEqual(caso1, "cognome = ballotta,berruti\r\n")

if __name__ == '__main__':
    unittest.main()
