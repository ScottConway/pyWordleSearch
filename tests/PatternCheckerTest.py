import unittest

from code.PatternChecker import PatternChecker


class PatternCheckerTest(unittest.TestCase):
    def test_wordTooSmall(self):
        goodPattern, finalPattern, error = PatternChecker.validate('xxXx')
        self.assertFalse(goodPattern)
        self.assertEqual('xxXx', finalPattern)  # add assertion here
        self.assertEqual("The wordle result must be five characters and consist of g, x, or y.", error)

    def test_wordTooLarge(self):
        goodPattern, finalPattern, error = PatternChecker.validate('xxXxyg')
        self.assertFalse(goodPattern)
        self.assertEqual('xxXxyg', finalPattern)  # add assertion here
        self.assertEqual("The wordle result must be five characters and consist of g, x, or y.", error)

    def test_badPattern(self):
        goodPattern, finalPattern, error = PatternChecker.validate('xygAa')
        self.assertFalse(goodPattern)
        self.assertEqual('xygAa', finalPattern)  # add assertion here
        self.assertEqual("The wordle result must be five characters and consist of g, x, or y.", error)

    def test_goodPattern(self):
        goodPattern, finalPattern, error = PatternChecker.validate('XYGxg')
        self.assertTrue(goodPattern)
        self.assertEqual('xygxg', finalPattern)  # add assertion here
        self.assertEqual("", error)


if __name__ == '__main__':
    unittest.main()
