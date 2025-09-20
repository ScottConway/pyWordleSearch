from code.Entry import Entry
from code.LetterStatistics import LetterStatistics


class EntryStatistics:
    """
    This class maintains the statistics of a single entry
    """
    def __init__(self):
        self.wordLetters = {}

    def buildLetterStatistics(self, entry: Entry):
        """
        Builds the statistics of a single entry
        :param entry:
        """
        # Determine the smallest between the entry word and entry pattern (both should be 5)
        numLetters = min(len(entry.word), len(entry.pattern))
        for i in range(numLetters):
            wordLetter: str = entry.word[i]
            exactMatch = False  # if the letter is matched in the correct position
            letterMissing = False # true if the letter is not found
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
