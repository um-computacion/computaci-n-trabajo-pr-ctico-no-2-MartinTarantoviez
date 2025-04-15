import unittest
from src.palindromes import is_palindrome

class TestPalindromesSimples(unittest.TestCase):
    def test_palindrome_sometemos(self):
        self.assertTrue(is_palindrome("ala"))
    def test_palindrome_neuquen(self):
        self.assertTrue(is_palindrome("neuquen"))
    def test_palindrome_arañara(self):
        self.assertTrue(is_palindrome("camac"))

if __name__ == '__main__':
    unittest.main()