import unittest

from translator import translate_en_to_fr, translate_fr_to_en


class TestSquare(unittest.TestCase):

    def test_en_to_fr_one_word(self):
        self.assertEqual(translate_en_to_fr('Hello'), 'Bonjour')  # Translate one word English to French

    def test_En_To_Fr(self):
        self.assertEqual(translate_en_to_fr("Please, follow me and don't stop!"),
                                         "S'il vous plaît, suivez-moi et ne vous arrêtez pas !")  # Translate one sentence English to French

    def test_fr_to_en_one_Word(self):
        self.assertEqual(translate_fr_to_en('Concombre'), 'Cucumber')  # Translate one word French to English

    def test_fr_to_en(self):
        self.assertNotEqual(translate_fr_to_en("S'il vous plaît, suivez-moi et ne vous arrêtez pas!"),
                            "Please, follow me and don't stop!")  # Translate one sentence French to English

    def test_numbers(self):
        self.assertEqual(translate_en_to_fr('2'), '2')  # Test numbers

    def test_fr_to_en_none(self):
        self.assertRaises(ValueError, translate_fr_to_en, None) # Test None parameter for French to English

    def test_en_to_f_none(self):
        self.assertRaises(ValueError,translate_fr_to_en, None) # Test None parameter for English to French


unittest.main()
