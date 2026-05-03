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
        """
        Overrides RegxWordFilter to remove the mustHaveLetters checked because we want to focus on
        letters that have not been tried.   I didn't do a !hasRequiredCharacters because I don't want to
        focus entirely of untriedLetters if none exists - we just weigh it such that untriedLetters have a
        much higher weight than matched letters.
        :param word:
        :return: if the word matches the pattern. 
        """
        return re.match(self.buildPattern(self.filterPattern), word)
