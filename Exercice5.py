import unittest
# Importation des fonctions à tester
from string_utils import est_palindrome, inverser_chaine, compter_voyelles

# Classe de test
class TestStringUtils(unittest.TestCase):

    def test_est_palindrome(self):
        self.assertTrue(est_palindrome("Radar"))
        self.assertTrue(est_palindrome("Laval"))
        self.assertFalse(est_palindrome("Bonjour"))
        self.assertTrue(est_palindrome("Esope reste ici et se repose"))
        self.assertTrue(est_palindrome("Kayak"))
    
    def test_inverser_chaine(self):
        self.assertEqual(inverser_chaine("Python"), "nohtyP")
        self.assertEqual(inverser_chaine("radar"), "radar")
        self.assertEqual(inverser_chaine(""), "")
        self.assertEqual(inverser_chaine("123abc"), "cba321")

    def test_compter_voyelles(self):
        self.assertEqual(compter_voyelles("Bonjour tout le monde"), 8)
        self.assertEqual(compter_voyelles("PYTHON"), 1)
        self.assertEqual(compter_voyelles("xyz"), 1)
        self.assertEqual(compter_voyelles("AEIOUY"), 6)
        self.assertEqual(compter_voyelles("bcdfg"), 0)

# Chargement et exécution des tests
test_string_utils = unittest.TestLoader().loadTestsFromTestCase(TestStringUtils)
unittest.TextTestRunner().run(test_string_utils)