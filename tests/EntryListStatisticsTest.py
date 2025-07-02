import unittest

from code.Entry import Entry
from code.EntryListStatistics import EntryListStatistics
from code.EntryStatistics import EntryStatistics
from code.LetterStatistics import LetterStatistics


class EntryListStatisticsTest(unittest.TestCase):
    def setUp(self):
        self.stats = EntryListStatistics()

    def test_initialState(self):
        self.assertEqual(0, len(self.stats.gameWordListStats))
        self.assertEqual(0, self.stats.totalMatchedCount())
        self.assertTrue(self.stats.doesWordMatchCounts('foggy'))
        self.assertTrue(self.stats.doesWordMatchCounts('abcde'))

    def test_addEntryStatisticsAndClear(self):
        entry = Entry("foggy", "yxxxg")
        self.stats.addEntry(entry)

        wordLetters = self.stats.gameWordListStats
        self.assertEqual(2, len(wordLetters))
        self.assertEqual(2, self.stats.totalMatchedCount())
        self.assertTrue('f' in wordLetters)
        self.assertTrue('y' in wordLetters)

        self.stats.clear()
        self.assertEqual(0, len(self.stats.gameWordListStats))
        self.assertEqual(0, self.stats.totalMatchedCount())

    def test_doesWordMatchCounts(self):
        entry = Entry("foggy", "yxxxg")
        self.stats.addEntry(entry)

        wordLetters = self.stats.gameWordListStats
        self.assertEqual(2, len(wordLetters))
        self.assertEqual(2, self.stats.totalMatchedCount())
        self.assertTrue('f' in wordLetters)
        self.assertTrue('y' in wordLetters)
        self.assertTrue(self.stats.doesWordMatchCounts('foggy'))
        self.assertFalse(self.stats.doesWordMatchCounts('abcde'))

        self.stats.clear()
        self.assertEqual(0, len(self.stats.gameWordListStats))
        self.assertEqual(0, self.stats.totalMatchedCount())
        self.assertTrue(self.stats.doesWordMatchCounts('foggy'))
        self.assertTrue(self.stats.doesWordMatchCounts('abcde'))

    def test_addMultipleEntries(self):
        #for this test the main word is misty
        entry = Entry("atone", "xyxxx")
        entryStats = EntryStatistics()
        entryStats.buildLetterStatistics(entry)

        self.stats.addEntryStatistics(entryStats)

        wordLetters = self.stats.gameWordListStats
        self.assertEqual(1, len(wordLetters))
        self.assertEqual(1, self.stats.totalMatchedCount())
        self.assertTrue('t' in wordLetters)

        entry = Entry("gifts", "xgxgy")
        entryStats = EntryStatistics()
        entryStats.buildLetterStatistics(entry)

        self.stats.addEntryStatistics(entryStats)
        self.assertEqual(3, self.stats.totalMatchedCount())

        wordLetters = self.stats.gameWordListStats
        self.assertEqual(3, len(wordLetters))
        self.assertTrue('t' in wordLetters)
        self.assertTrue('i' in wordLetters)
        self.assertTrue('s' in wordLetters)

        entry = Entry("dirty", "xgxgg")
        entryStats = EntryStatistics()
        entryStats.buildLetterStatistics(entry)

        self.stats.addEntryStatistics(entryStats)
        self.assertEqual(4, self.stats.totalMatchedCount())

        wordLetters = self.stats.gameWordListStats
        self.assertEqual(4, len(wordLetters))

        self.assertTrue('t' in wordLetters)
        letterStats:LetterStatistics = wordLetters['t']
        self.assertFalse(letterStats.exactCount)
        self.assertEqual(1, letterStats.count)

        self.assertTrue('i' in wordLetters)
        letterStats: LetterStatistics = wordLetters['i']
        self.assertFalse(letterStats.exactCount)
        self.assertEqual(1, letterStats.count)

        self.assertTrue('s' in wordLetters)
        letterStats: LetterStatistics = wordLetters['s']
        self.assertFalse(letterStats.exactCount)
        self.assertEqual(1, letterStats.count)

        self.assertTrue('y' in wordLetters)
        letterStats: LetterStatistics = wordLetters['y']
        self.assertFalse(letterStats.exactCount)
        self.assertEqual(1, letterStats.count)

    def test_multiLetterEntries(self):
        #for this test the main word is brass
        entry = Entry("darts", "xyyxg")
        self.stats.addEntry(entry)
        self.assertEqual(3, self.stats.totalMatchedCount())

        wordLetters = self.stats.gameWordListStats
        self.assertEqual(3, len(wordLetters))

        self.assertTrue('a' in wordLetters)
        letterStats: LetterStatistics = wordLetters['a']
        self.assertFalse(letterStats.exactCount)
        self.assertEqual(1, letterStats.count)

        self.assertTrue('r' in wordLetters)
        letterStats: LetterStatistics = wordLetters['r']
        self.assertFalse(letterStats.exactCount)
        self.assertEqual(1, letterStats.count)

        self.assertTrue('s' in wordLetters)
        letterStats: LetterStatistics = wordLetters['s']
        self.assertFalse(letterStats.exactCount)
        self.assertEqual(1, letterStats.count)

        entry = Entry("swiss", "xxxgg")
        self.stats.addEntry(entry)
        self.assertEqual(4, self.stats.totalMatchedCount())

        wordLetters = self.stats.gameWordListStats
        self.assertEqual(3, len(wordLetters))

        self.assertTrue('a' in wordLetters)
        letterStats: LetterStatistics = wordLetters['a']
        self.assertFalse(letterStats.exactCount)
        self.assertEqual(1, letterStats.count)

        self.assertTrue('r' in wordLetters)
        letterStats: LetterStatistics = wordLetters['r']
        self.assertFalse(letterStats.exactCount)
        self.assertEqual(1, letterStats.count)

        self.assertTrue('s' in wordLetters)
        letterStats: LetterStatistics = wordLetters['s']
        self.assertTrue(letterStats.exactCount)
        self.assertEqual(2, letterStats.count)


if __name__ == '__main__':
    unittest.main()
