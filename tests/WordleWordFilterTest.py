import unittest
from code.WordleWordFilter import WordleWordFilter
from code.Entry import Entry

WORD1 = "abcde"
WORD2 = "truck"
WORD3 = "lucky"
WORD4 = "broad"
WORD5 = "board"

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.filter = WordleWordFilter()

    def test_initialState(self):
        self.assertTrue(self.filter.wordMatchesPattern(WORD1))
        self.assertTrue(self.filter.wordMatchesPattern(WORD2))
        self.assertTrue(self.filter.wordMatchesPattern(WORD3))
        self.assertTrue(self.filter.wordMatchesPattern(WORD4))
        self.assertTrue(self.filter.wordMatchesPattern(WORD5))

        entry = Entry('abcde', 'yyxyx')
        self.filter.updatefilterPattern(entry)

        self.assertFalse(self.filter.wordMatchesPattern(WORD1))
        self.assertFalse(self.filter.wordMatchesPattern(WORD2))
        self.assertFalse(self.filter.wordMatchesPattern(WORD3))
        self.assertTrue(self.filter.wordMatchesPattern(WORD4))
        self.assertTrue(self.filter.wordMatchesPattern(WORD5))


if __name__ == '__main__':
    unittest.main()