from code.WordWeigher import WordWeigher


class WordleWordWeigher(WordWeigher):
    def determineWeight(self, upperWord) -> int:
        word = upperWord.lower()
        wordSum = WordWeigher.firstLetterWeight[word[0]] + WordWeigher.secondLetterWeight[word[1]] + \
                  WordWeigher.thirdLetterWeight[word[2]] + \
                  WordWeigher.fourthLetterWeight[word[3]] + WordWeigher.fifthLetterWeight[word[4]]
        uniqueLetters = set()

        for letter in word:
            uniqueLetters.add(letter)

        wordSum += (4000 * len(uniqueLetters))

        return wordSum

    def __init__(self):
        super().__init__()
