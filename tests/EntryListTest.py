import unittest

from code.Entry import Entry
from code.EntryList import EntryList


class EntryListTest(unittest.TestCase):

    def setUp(self):
        self.entry1 = Entry('aword', 'yxyyg')
        self.entry2 = Entry('bword', 'gxyyg')

    def tearDown(self):
        EntryList.clear()

    def test_something(self):
        entryList = EntryList()
        entryList.add(self.entry1)
        entryList.add(self.entry2)
        self.assertEqual(2, len(entryList.entries))

    def test_mustHaveLetters(self):
        entryList = EntryList()
        entryList.add(self.entry1)
        letterSet = EntryList.mustHaveLetterSet()
        self.assertEqual(4, len(letterSet))
        entryList.add(self.entry2)
        letterSet = EntryList.mustHaveLetterSet()
        self.assertEqual(5, len(letterSet))

    def test_valueErrorIfSameWord(self):
        entryList = EntryList()
        entryList.add(self.entry1)
        with self.assertRaises(ValueError) as context:
            entryList.add(self.entry1)

        self.assertTrue(f'{self.entry1.word} already used.' in str(context.exception))

    def test_exceptionIfTooManyMustHaveLetters(self):
        firstFiveLetters = Entry('abcde', 'yyyyy')
        nextFiveLetters = Entry('fghij', 'yyyyy')
        entryList = EntryList()
        entryList.add(firstFiveLetters)
        letterSet = EntryList.mustHaveLetterSet()
        self.assertEqual(5, len(letterSet))
        with self.assertRaises(Exception) as context:
            entryList.add(nextFiveLetters)

        self.assertTrue('Typo in word or pattern as you have identified matches in more than five letters!' in str(
            context.exception))


if __name__ == '__main__':
    unittest.main()
