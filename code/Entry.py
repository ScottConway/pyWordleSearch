import dataclasses


class Entry:
    def __init__(self, word, pattern):
        self.word = word
        self.pattern = pattern

    def mustHaveLettersSet(self) -> set:
        letterSet = set()

        numLetters = min(len(self.word), len(self.pattern))
        for i in range(numLetters):
            wordLetter = self.word[i]
            patternLetter = self.pattern[i]
            if patternLetter == 'y' or patternLetter == 'g':
                letterSet.add(wordLetter)

        return letterSet

    def mustHaveLetterCount(self) -> dict[str, int]:
        letterCount = {}
        numLetters = min(len(self.word), len(self.pattern))
        for i in range(numLetters):
            wordLetter = self.word[i]
            if wordLetter in letterCount:
                continue

            numFound = 0
            for j in range(i, numLetters):
                patternLetter = self.pattern[j]
                if self.word[j] == wordLetter and (patternLetter == 'y' or patternLetter == 'g'):
                    numFound += 1

            if numFound > 0:
                letterCount[wordLetter] = numFound

        return letterCount
