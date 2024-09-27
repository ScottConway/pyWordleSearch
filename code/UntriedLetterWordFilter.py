from code.Entry import Entry
from code.RegxWordFilter import RegxWordFilter

import re


class UntriedLetterWordFilter(RegxWordFilter):
    def __init__(self):
        RegxWordFilter.__init__(self)

    def updateSinglePattern(self, index, entry: Entry):
        wordLetter = entry.word[index]
        # print(wordLetter)
        self.filterPattern = self.removeCharacterFromAllPatterns(wordLetter, entry)

        return self.filterPattern

    def removeCharacterFromPattern(self, pattern, wordCharacter, patternCharacter):
        return pattern.replace(wordCharacter, "")

    def getFilterName(self) -> str:
        return "UntriedLetterWordFilter"

    def wordMatchesPattern(self, word):
        return re.match(self.buildPattern(self.filterPattern), word)
