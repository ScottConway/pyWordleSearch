import unittest

from code.Entry import Entry
from code.EntryList import EntryList


class EntryListTest(unittest.TestCase):

    def setUp(self):
        self.entry1 = Entry('aword', 'yxyyg')
        self.entry2 = Entry('bword', 'gxyyg')

    def test_something(self):
        entryList = EntryList()
        entryList.add(self.entry1)
        entryList.add(self.entry2)
        self.assertEqual(2, len(entryList.entries))

    def test_valueErrorIfSameWord(self):
        entryList = EntryList()
        entryList.add(self.entry1)
        with self.assertRaises(ValueError) as context:
            entryList.add(self.entry1)

        self.assertTrue(f'{self.entry1.word} already used.' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
