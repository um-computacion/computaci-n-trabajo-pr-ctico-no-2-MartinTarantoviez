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

class TestPalindromesEdgeCases(unittest.TestCase):
    def test_cadena_vacia(self):
        self.assertTrue(is_palindrome(""))
    def test_una_letra_minuscula(self):
        self.assertTrue(is_palindrome("a"))
    def test_una_letra_mayuscula(self):
        self.assertTrue(is_palindrome("M"))
    def test_solo_espacios(self):
        self.assertTrue(is_palindrome("         "))
    def test_simbolos_no_letras(self):
        self.assertTrue(is_palindrome("!&$"))
    def test_numero_unico(self):
        self.assertTrue(is_palindrome("9"))
if __name__ == '__main__':
    unittest.main()