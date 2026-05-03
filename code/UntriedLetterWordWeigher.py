import code

from code.EntryList import EntryList
from code.WordWeigher import WordWeigher


class UntriedLetterWordWeigher(WordWeigher):
    def determineWeight(self, upperWord) -> int:
        word = upperWord.lower()
        wordSum = WordWeigher.firstLetterWeight[word[0]] + WordWeigher.secondLetterWeight[word[1]] + \
                  WordWeigher.thirdLetterWeight[word[2]] + \
                  WordWeigher.fourthLetterWeight[word[3]] + WordWeigher.fifthLetterWeight[word[4]]
        uniqueLetters = set()
        untriedLetters = code.EntryList.entryListInstance.mustHaveLetterSet()
        untriedLetterCount = 0

        for letter in word:
            uniqueLetters.add(letter)
            if letter not in untriedLetters:
                untriedLetterCount += 1

        wordSum += (1000 * len(uniqueLetters))
        wordSum += (1000 * untriedLetterCount)

        return wordSum

    def __init__(self):
        super().__init__()
