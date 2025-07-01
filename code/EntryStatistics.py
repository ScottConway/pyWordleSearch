from code.Entry import Entry
from code.LetterStatistics import LetterStatistics


class EntryStatistics:
    def __init__(self):
        self.wordLetters = {}

    def buildLetterStatistics(self, entry: Entry):
        numLetters = min(len(entry.word), len(entry.pattern))
        for i in range(numLetters):
            wordLetter: str = entry.word[i]
            exactMatch = False
            letterMissing = False
            if wordLetter in self.wordLetters:
                continue

            numFound = 0
            for j in range(i, numLetters):
                patternLetter = entry.pattern[j]
                if entry.word[j] == wordLetter:
                    if patternLetter == 'y' or patternLetter == 'g':
                        numFound += 1
                    else:
                        letterMissing = True

            if numFound > 0:
                if letterMissing:
                    exactMatch = True

                letterStatistics: LetterStatistics = LetterStatistics(numFound, exactMatch)

                self.wordLetters[wordLetter] = letterStatistics
