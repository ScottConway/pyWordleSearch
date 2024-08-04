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


class WordListCopyConstructorIntegrationTest(unittest.TestCase):

    def setUp(self):
        simpleList = [WORD1, WORD2, WORD3, WORD4, WORD5, BADWORD]
        self.wordList = WordList(simpleList)
        self.otherWordList = WordList(self.wordList)

    def test_initialState(self):
        self.assertEqual(5, len(self.wordList.wordList))
        self.assertEqual(5, len(self.otherWordList.wordList))


    def test_filterEntry(self):
        wordFilter = WordleWordFilter()
        yWordFilter = YLetterWordFilter()
        self.wordList.addWordFilter(wordFilter)
        self.otherWordList.addWordFilter(yWordFilter)
        entry = Entry('abcde', 'yyxyx')
        self.wordList.filterList(entry)
        self.assertEqual(2, len(self.wordList.wordList))
        self.assertEqual(5, len(self.otherWordList.wordList))
        self.otherWordList.filterList(entry)
        self.assertEqual(2, len(self.wordList.wordList))
        self.assertEqual(2, len(self.otherWordList.wordList))


if __name__ == '__main__':
    unittest.main()
