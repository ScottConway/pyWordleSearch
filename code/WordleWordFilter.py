from code.RegxWordFilter import RegxWordFilter
from code.Entry import Entry


class WordleWordFilter(RegxWordFilter):
    def __init__(self):
        RegxWordFilter.__init__(self)

    def updateSinglePattern(self, index, entry):
        patternLetter = entry.pattern[index]
        wordLetter = entry.word[index]

        if patternLetter == 'x':
            if wordLetter in self.mustHaveCharacters:
                self.filterPattern[index] = self.removeCharacterFromPattern(self.filterPattern[index], wordLetter,
                                                                            patternLetter)
            else:
                self.filterPattern = self.removeCharacterFromAllPatterns(wordLetter, entry)

        if patternLetter == 'y':
            self.filterPattern[index] = self.removeCharacterFromPattern(self.filterPattern[index], wordLetter,
                                                                        patternLetter)
            self.mustHaveCharacters.add(wordLetter)

        if patternLetter == 'g':
            self.filterPattern[index] = wordLetter
            self.mustHaveCharacters.add(wordLetter)

        return self.filterPattern
