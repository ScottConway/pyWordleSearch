import unittest

from code.WordleWordWeigher import WordleWordWeigher


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.wordleWordWeigher = WordleWordWeigher()

    def test_moreUniqueLettersIncreaseWeight(self):
        self.assertGreater(self.wordleWordWeigher.determineWeight('stone'),
                           self.wordleWordWeigher.determineWeight('hubby'),
                           'ERROR stone should have a lower weight than hubby')

    def test_isCaseInsensitive(self):
        self.assertEqual(self.wordleWordWeigher.determineWeight('STONE'), self.wordleWordWeigher.determineWeight('stone'))

    def test_uniqueLettersWeightTest2(self):
        self.assertGreater(self.wordleWordWeigher.determineWeight('lewis'),
                           self.wordleWordWeigher.determineWeight('press'),
                           'ERROR lewis should have a lower weight than press')

if __name__ == '__main__':
    unittest.main()
