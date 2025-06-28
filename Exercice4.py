import unittest

# Fonction à tester 
def factorielle(n):
    if n < 0:
        raise ValueError("La factorielle n'est pas définie pour les entiers négatifs.")
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

# Classe de test
class TestFactorielle(unittest.TestCase):
    def test_valeurs_positives(self):
        self.assertEqual(factorielle(0), 1)
        self.assertEqual(factorielle(1), 1)
        self.assertEqual(factorielle(5), 120)
        self.assertEqual(factorielle(7), 5040)

    def test_valeur_negative(self):
        with self.assertRaises(ValueError):
            factorielle(-3)

# Chargement et exécution des tests
test_factorielle = unittest.TestLoader().loadTestsFromTestCase(TestFactorielle)
unittest.TextTestRunner().run(test_factorielle)
