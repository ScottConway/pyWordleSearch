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

