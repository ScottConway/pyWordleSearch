import re
from abc import ABC, abstractmethod
from code.Entry import Entry

INITIAL_PATTERN = ["[abcdefghijklmnopqrstuvwxyz]", "[abcdefghijklmnopqrstuvwxyz]", "[abcdefghijklmnopqrstuvwxyz]",
                   "[abcdefghijklmnopqrstuvwxyz]", "[abcdefghijklmnopqrstuvwxyz]"]


class RegxWordFilter(ABC):
    def __init__(self):
        self.filterPattern = INITIAL_PATTERN

    def buildPattern(self, patternList):
        patternString = ""

        for pattern in patternList:
            patternString += pattern

        return patternString

    def wordMatchesPattern(self, word):
        return re.match(self.buildPattern(self.filterPattern), word)

    def updatefilterPattern(self, entry):
        for i in range(5):
            self.filterPattern = self.updateSinglePattern(i, entry)

    @abstractmethod
    def updateSinglePattern(self, index, entry):
        pass

    def removeCharacterFromPattern(self, pattern, wordCharacter, patternCharacter):
        if len(pattern) > 1 and patternCharacter != 'g':
            return pattern.replace(wordCharacter, "")

        return pattern

    def removeCharacterFromAllPatterns(self, wordCharacter, entry: Entry):
        for i in range(5):
            self.filterPattern[i] = self.removeCharacterFromPattern(self.filterPattern[i], wordCharacter,
                                                                    entry.pattern[i])
        return self.filterPattern
