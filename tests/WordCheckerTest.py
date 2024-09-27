import unittest

from code.WordChecker import WordChecker


class MyTestCase(unittest.TestCase):
    def test_wordTooSmall(self):
        goodWord, finalWord, error = WordChecker.validate("Duck")
        self.assertFalse(goodWord)
        self.assertEqual('Duck', finalWord)
        self.assertEqual("Wordle words must only be five characters long.", error)  # add assertion here

    def test_wordTooLarge(self):
        goodWord, finalWord, error = WordChecker.validate("Trucks")
        self.assertFalse(goodWord)
        self.assertEqual('Trucks', finalWord)
        self.assertEqual("Wordle words must only be five characters long.", error)

    def test_goodWord(self):
        goodWord, finalWord, error = WordChecker.validate("Truck")
        self.assertTrue(goodWord)
        self.assertEqual('truck', finalWord)
        self.assertEqual("", error)

    def test_removeSpaces(self):
        goodWord, finalWord, error = WordChecker.validate("  TruCk  ")
        self.assertEqual('truck', finalWord)
        self.assertTrue(goodWord)
        self.assertEqual("", error)

    def test_illegalWord(self):
        goodWord, finalWord, error = WordChecker.validate("Duck1")
        self.assertFalse(goodWord)
        self.assertEqual('Duck1', finalWord)
        self.assertEqual("The wordle word must be five alphabetic characters long.", error)


if __name__ == '__main__':
    unittest.main()
