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
        # Test Hello returns Bonjour
        self.assertEqual(frenchToEnglish('Hello'), 'Bonjour')
        # Test Hello does not return Hello
        self.assertNotEqual(frenchToEnglish('Hello'), 'Hello')
        # Test None returns empty string
        self.assertNotEqual(frenchToEnglish("None"), '')
        # Test empty string returns empty string
        self.assertNotEqual(frenchToEnglish(0), 0)

unittest.main()