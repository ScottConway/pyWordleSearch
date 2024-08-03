import unittest

from code.WordList import WordList
from code.WordleWordFilter import WordleWordFilter
from code.Entry import Entry
from code.YLetterWordFilter import YLetterWordFilter

WORD1 = "abcde"
WORD2 = "truck"
WORD3 = "lucky"
WORD4 = "broad"
WORD5 = "board"
BADWORD = "badword"


class MyTestCase(unittest.TestCase):

    def setUp(self):
        simpleList = [WORD1, WORD2, WORD3, WORD4, WORD5, BADWORD]
        self.wordList = WordList(simpleList)

    def test_initialState(self):
        self.assertEqual(5, len(self.wordList.wordList))

    def test_addMultipleWordFiltersRaisesException(self):
        wordFilter = WordleWordFilter()
        wordFilter2 = YLetterWordFilter()
        self.wordList.addWordFilter(wordFilter2)
        with self.assertRaises(Exception) as context:
            self.wordList.addWordFilter(wordFilter)

        self.assertTrue('WordFilter already assigned to WordList' in str(context.exception))

    def test_filterEntry(self):
        wordFilter = WordleWordFilter()
        self.wordList.addWordFilter(wordFilter)
        entry = Entry('abcde', 'yyxyx')
        self.wordList.filterList(entry)
        self.assertEqual(2, len(self.wordList.wordList))

    def test_filterListWithoutFilterRaisesException(self):
        entry = Entry('abcde', 'yyxyx')

        with self.assertRaises(Exception) as context:
            self.wordList.filterList(entry)

        self.assertTrue('WordFilter has not been assigned to WordList' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
