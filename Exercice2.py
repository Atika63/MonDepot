import unittest

# Fonction à tester
def puissance(a, b):
    return a ** b

# Classe de test
class TestPuissance(unittest.TestCase):
    def test_puissance(self):
        # Assertions pour vérifier si le résultat est conforme à ce qui est attendu
        self.assertEqual(puissance(2, 3), 8)
        self.assertEqual(puissance(5, 2), 25)
        self.assertEqual(puissance(9, 1), 9)
        self.assertEqual(puissance(10, 0), 1)
        self.assertEqual(puissance(0, 3), 0)
        self.assertEqual(puissance(2, -2), 0.25)
        self.assertEqual(puissance(-3, 3), -27)

# Définition d'un objet test
test_puissance = unittest.TestLoader().loadTestsFromTestCase(TestPuissance)

# Exécution du test
unittest.TextTestRunner().run(test_puissance)
