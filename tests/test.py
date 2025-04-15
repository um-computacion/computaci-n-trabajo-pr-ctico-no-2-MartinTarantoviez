import unittest
from src.palindromes import is_palindrome

class TestPalindromesSimples(unittest.TestCase):
    def test_palindrome_sometemos(self):
        self.assertTrue(is_palindrome("ala"))
    def test_palindrome_neuquen(self):
        self.assertTrue(is_palindrome("neuquen"))
    def test_palindrome_arañara(self):
        self.assertTrue(is_palindrome("camac"))

class TestPalindromesFrases(unittest.TestCase):
    def test_palindrome_amaplan(self):
        self.assertTrue(is_palindrome("Dábale arroz a la zorra el abad"))
    def test_palindrome_adan(self):
        self.assertTrue(is_palindrome("Sé verlas al revés"))
    def test_palindrome_nolemon(self):
        self.assertTrue(is_palindrome("ama ala ama"))

class TestFrasesNoPalindromas(unittest.TestCase):

    def test_frase_con_simbolos(self):
        self.assertFalse(is_palindrome("caminando ando"))
    def test_frase_larga(self):
        self.assertFalse(is_palindrome("computacion"))
    def test_frase_casi_palindromo(self):
        self.assertFalse(is_palindrome("Peron"))

if __name__ == '__main__':
    unittest.main()