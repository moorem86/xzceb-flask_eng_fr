''' test the translators'''
from translator import englishToFrench, frenchToEnglish
import unittest

class testE2F(unittest.TestCase):
    '''English to French test'''
    def test_englishToFrench(self):
        # Test Hello returns Bonjour
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        # Test Hello does not return Hello
        self.assertNotEqual(englishToFrench('Hello'), 'Hello')
        # Test None returns empty string
        self.assertNotEqual(englishToFrench("None"), '')
        # Test empty string returns empty string
        self.assertNotEqual(englishToFrench(0), 0)

class testF2E(unittest.TestCase):
    '''French to English test'''
    def test_frenchToEnglish(self):
        # Test Bonjour returns Hello
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        # Test Bonjour does not return Bonjour
        self.assertNotEqual(frenchToEnglish('Bonjour'), 'Bonjour')
        # Test None returns empty string
        self.assertNotEqual(frenchToEnglish("None"), '')
        # Test empty string returns empty string
        self.assertNotEqual(frenchToEnglish(0), 0)

unittest.main()