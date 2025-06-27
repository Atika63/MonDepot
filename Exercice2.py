import unittest

class TestMultiplication(unittest.TestCase):
        def test_multiplication(self):
    # Assertions pour vérifier si le résultat est conforme à ce qui est attendu
         self.assertEqual(multiplication(1, 3), 3)
         self.assertEqual(multiplication(2, 8), 16)
         self.assertEqual(multiplication(4, 3), 12)

         self.assertEqual(multiplication(0, 5), 0)
         self.assertEqual(multiplication(5, 0), 0)
 # Définition d'un objet test
test_multiplication = unittest.TestLoader().loadTestsFromTestCase(TestMultiplication)  # On charge les tests depuis la classe
 
# Exécution du test
unittest.TextTestRunner().run(TestMultiplication)        