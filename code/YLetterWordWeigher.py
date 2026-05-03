import code

from code.EntryList import EntryList
from code.WordWeigher import WordWeigher


class YLetterWordWeigher(WordWeigher):
    def determineWeight(self, upperWord) -> int:
        word = upperWord.lower()
        wordSum = WordWeigher.firstLetterWeight[word[0]] + WordWeigher.secondLetterWeight[word[1]] + \
                  WordWeigher.thirdLetterWeight[word[2]] + \
                  WordWeigher.fourthLetterWeight[word[3]] + WordWeigher.fifthLetterWeight[word[4]]
        uniqueLetters = set()
        yLetters = code.EntryList.entryListInstance.yLetterSet()
        matchedYLetters = 0

        for letter in word:
            uniqueLetters.add(letter)
            if letter in yLetters:
                matchedYLetters += 1

        wordSum += (1000 * len(uniqueLetters))
        wordSum += (1000 * matchedYLetters)

        return wordSum

    def __init__(self):
        super().__init__()
