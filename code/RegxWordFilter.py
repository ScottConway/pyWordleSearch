import re
from abc import ABC, abstractmethod

from code.Entry import Entry


class RegxWordFilter(ABC):
    def __init__(self):
        self.filterPattern = ["[abcdefghijklmnopqrstuvwxyz]", "[abcdefghijklmnopqrstuvwxyz]",
                              "[abcdefghijklmnopqrstuvwxyz]",
                              "[abcdefghijklmnopqrstuvwxyz]", "[abcdefghijklmnopqrstuvwxyz]"]
        self.mustHaveCharacters = set()

    def buildPattern(self, patternList):
        patternString = ""

        for pattern in patternList:
            patternString += pattern

        return patternString

    def hasRequiredCharacters(self, word):
        if len(self.mustHaveCharacters) == 0:
            return True

        for letter in self.mustHaveCharacters:
            if word.find(letter) == -1:
                return False

        return True

    def wordMatchesPattern(self, word):
        return re.match(self.buildPattern(self.filterPattern), word) and self.hasRequiredCharacters(word)

    def updatefilterPattern(self, entry):
        for i in range(5):
            # print(self.filterPattern)
            self.filterPattern = self.updateSinglePattern(i, entry)
            # print(self.filterPattern)
            # print('--------------------------')

    @abstractmethod
    def updateSinglePattern(self, index, entry):
        pass

    @abstractmethod
    def getFilterName(self) -> str:
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
