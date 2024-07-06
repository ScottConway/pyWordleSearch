from code.RegxWordFilter import RegxWordFilter
from code.Entry import Entry


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
