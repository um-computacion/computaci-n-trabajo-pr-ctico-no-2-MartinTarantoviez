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

if __name__ == '__main__':
    unittest.main()