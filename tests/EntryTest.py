import unittest

from code.Entry import Entry


class EntryTestCase(unittest.TestCase):
    def test_mustHaveLetters(self):
        entry = Entry("foggy", "xxxgy")
        letterSet = entry.mustHaveLettersSet()

        self.assertEqual(2, len(letterSet))  # add assertion here
        self.assertTrue('g' in letterSet)
        self.assertTrue('y' in letterSet)


if __name__ == '__main__':
    unittest.main()
