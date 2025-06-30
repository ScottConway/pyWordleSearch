import unittest

from code.Entry import Entry


class EntryTestCase(unittest.TestCase):
    def test_mustHaveLetters(self):
        entry = Entry("foggy", "xxxgy")
        letterSet = entry.mustHaveLettersSet()

        self.assertEqual(2, len(letterSet))  # add assertion here
        self.assertTrue('g' in letterSet)
        self.assertTrue('y' in letterSet)

    def test_mustHaveLetterCount(self):
        entry = Entry("foggy", "xxxgy")
        letterCount = entry.mustHaveLetterCount()
        self.assertEqual(2, len(letterCount))
        self.assertTrue('g' in letterCount)
        self.assertTrue('y' in letterCount)
        self.assertEqual(1, letterCount['g'])
        self.assertEqual(1, letterCount['y'])


    def test_mustHaveLetterCountWithDuplicate(self):
        entry = Entry("foggy", "xxygy")
        letterCount = entry.mustHaveLetterCount()
        self.assertEqual(2, len(letterCount))
        self.assertTrue('g' in letterCount)
        self.assertTrue('y' in letterCount)
        self.assertEqual(2, letterCount['g'])
        self.assertEqual(1, letterCount['y'])

if __name__ == '__main__':
    unittest.main()
