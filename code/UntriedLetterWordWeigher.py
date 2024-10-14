from code.EntryList import EntryList
from code.WordWeigher import WordWeigher
from pyWordleOriginal import firstLetterWeight, secondLetterWeight, thirdLetterWeight, fourthLetterWeight, \
    fifthLetterWeight


class UntriedLetterWordWeigher(WordWeigher):
    def determineWeight(self, upperWord) -> int:
        word = upperWord.lower()
        wordSum = firstLetterWeight[word[0]] + secondLetterWeight[word[1]] + thirdLetterWeight[word[2]] + \
                  fourthLetterWeight[word[3]] + fifthLetterWeight[word[4]]
        uniqueLetters = set()
        mustHaveLetters = EntryList.mustHaveLetterSet()
        untriedLetters = 0

        for letter in word:
            uniqueLetters.add(letter)
            if letter not in mustHaveLetters:
                untriedLetters += 1

        wordSum += (1000 * len(uniqueLetters))
        wordSum += (1000 * untriedLetters)

        return wordSum

    def __init__(self):
        super().__init__()

