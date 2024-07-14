from code.WordWeigher import WordWeigher
from pyWordleOriginal import firstLetterWeight, secondLetterWeight, thirdLetterWeight, fourthLetterWeight, \
    fifthLetterWeight


class WordleWordWeigher(WordWeigher):
    def determineWeight(self, upperWord) -> int:
        word = upperWord.lower()
        wordSum = firstLetterWeight[word[0]] + secondLetterWeight[word[1]] + thirdLetterWeight[word[2]] + \
                  fourthLetterWeight[word[3]] + fifthLetterWeight[word[4]]
        uniqueLetters = set()

        for letter in word:
            uniqueLetters.add(letter)

        wordSum += (1000 * len(uniqueLetters))

        return wordSum

    def __init__(self):
        super().__init__()

