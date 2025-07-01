import unittest

from code.LetterStatistics import LetterStatistics


class MyTestCase(unittest.TestCase):
    def test_happyPath(self):
        testLetterCount = LetterStatistics(5, False)
        self.assertEqual(5, testLetterCount.count)
        self.assertFalse(testLetterCount.exactCount)

    def test_ExceptionOnNegativeCount(self):
        with self.assertRaises(ValueError) as context:
            testLetterCount = LetterStatistics(-1, False)

        self.assertTrue('Count must be between 0 and 5!' in str(context.exception))

    def test_ExceptionOnLargeCount(self):
        with self.assertRaises(ValueError) as context:
            testLetterCount = LetterStatistics(6, False)

        self.assertTrue('Count must be between 0 and 5!' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
