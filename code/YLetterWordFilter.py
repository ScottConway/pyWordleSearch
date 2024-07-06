from code.RegxWordFilter import RegxWordFilter
from code.Entry import Entry


class YLetterWordFilter(RegxWordFilter):
    def __init__(self):
        RegxWordFilter.__init__(self)

    def updateSinglePattern(self, index, entry: Entry):
        patternLetter = entry.pattern[index]
        wordLetter = entry.word[index]

        # print(f"Letter {wordLetter} has pattern {patternLetter}.")

        if patternLetter == 'x' and wordLetter not in self.mustHaveCharacters:
            # print(f"    Letter {wordLetter} has pattern {patternLetter} and is mustHaveCharacters.")
            self.filterPattern = self.removeCharacterFromAllPatterns(wordLetter, entry)

        if patternLetter == 'y':
            # print(f"     Letter {wordLetter} has pattern {patternLetter} and is going trough the y filter.")
            self.filterPattern[index] = self.removeCharacterFromPattern(self.filterPattern[index], wordLetter,
                                                                        patternLetter)
            self.mustHaveCharacters.add(wordLetter)

        return self.filterPattern
