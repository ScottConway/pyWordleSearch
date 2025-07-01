import unittest

from code.Entry import Entry
from code.EntryStatistics import EntryStatistics
from code.LetterStatistics import LetterStatistics


class MyTestCase(unittest.TestCase):
    def test_noMatches(self):
        entry = Entry("foggy", "xxxxx")
        entryStats = EntryStatistics()
        entryStats.buildLetterStatistics(entry)

        self.assertEqual(0, len(entryStats.wordLetters))

    def test_matches(self):
        entry = Entry("foggy", "yxxxg")
        entryStats = EntryStatistics()
        entryStats.buildLetterStatistics(entry)

        wordLetters = entryStats.wordLetters
        self.assertEqual(2, len(wordLetters))
        self.assertTrue('f' in entryStats.wordLetters)
        self.assertTrue('y' in entryStats.wordLetters)

        fLetterStats:LetterStatistics = entryStats.wordLetters['f']
        self.assertFalse(fLetterStats.exactCount)

        yLetterStats: LetterStatistics = entryStats.wordLetters['y']
        self.assertFalse(yLetterStats.exactCount)

    def test_exactMatches(self):
        entry = Entry("foggy", "yxgxg")
        entryStats = EntryStatistics()
        entryStats.buildLetterStatistics(entry)

        wordLetters = entryStats.wordLetters
        self.assertEqual(3, len(wordLetters))
        self.assertTrue('f' in entryStats.wordLetters)
        self.assertTrue('y' in entryStats.wordLetters)
        self.assertTrue('g' in entryStats.wordLetters)

        fLetterStats:LetterStatistics = entryStats.wordLetters['f']
        self.assertFalse(fLetterStats.exactCount)

        yLetterStats: LetterStatistics = entryStats.wordLetters['y']
        self.assertFalse(yLetterStats.exactCount)

        gLetterStats: LetterStatistics = entryStats.wordLetters['g']
        self.assertTrue(gLetterStats.exactCount)


if __name__ == '__main__':
    unittest.main()
