import unittest

# Fonction à tester
def somme_entiers_inferieurs(n):
    somme = sum(range(n))
    return somme

# Classe de test
class TestSommeEntiersInferieurs(unittest.TestCase):
    def test_somme_entiers_inferieurs(self):
        # Assertions pour vérifier les résultats attendus
        self.assertEqual(somme_entiers_inferieurs(5), 10)  # 0+1+2+3+4
        self.assertEqual(somme_entiers_inferieurs(1), 0)   # aucun entier strictement < 1
        self.assertEqual(somme_entiers_inferieurs(10), 45) # 0+1+...+9
        self.assertEqual(somme_entiers_inferieurs(0), 0)   # aucun entier < 0
        self.assertEqual(somme_entiers_inferieurs(3), 3)   # 0+1+2

# Définition d'un objet test
test_somme = unittest.TestLoader().loadTestsFromTestCase(TestSommeEntiersInferieurs)

# Exécution du test
unittest.TextTestRunner().run(test_somme)
