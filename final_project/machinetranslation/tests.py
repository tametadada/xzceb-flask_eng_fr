import unittest
from translator import englishToFrench, frenchToEnglish


class TestTranslateFunctions(unittest.TestCase):
    def test_nul(self):
        self.assertEqual(englishToFrench(None), None)
        self.assertEqual(frenchToEnglish(None), None)

    def test_hello(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello' )

    def test_new(self):
        self.assertNotEqual(englishToFrench(
            "I'm happy today"),
            "j'étais heureux hier"
        )
        self.assertNotEqual(frenchToEnglish(
            "j'étais heureux hier"),
            "I'm happy today"
        )


if __name__ == '__main__':
    unittest.main()