G = 'g'
Y = 'y'
MaxWordSize = 5


class Entry:
    """
    An Entry is a single entry in the wordle game.

    Attributes:
        word (str): The word entered by the user.
        pattern (str): The pattern returned by the wordle game.
    """
    def __init__(self, word: str, pattern: str):
        self.word = word
        self.pattern = pattern

    def mustHaveLettersSet(self) -> set:
        """
        Returns a set of letters in a word whose pattern is either y or g.  Meaning these are
        letters that will be found in the wordle answer.
        :return: Set of letters that will be found in the wordle answer.
        """
        letterSet = set()

        numLetters = min(len(self.word), len(self.pattern))
        for i in range(numLetters):
            wordLetter = self.word[i]
            patternLetter = self.pattern[i]
            if patternLetter == Y or patternLetter == G:
                letterSet.add(wordLetter)

        return letterSet

    def mustHaveLetterCount(self) -> dict[str, int]:
        """
        Returns a dictionary mapping letters to how many times they appear in the word.
        This main purpose of this is filtering the main word dictionary to ensure that the best word
        options are retained.
        :return: Map of letters to how many times they appear in the word.
        """
        letterCount = {}
        numLetters = min(len(self.word), len(self.pattern))
        for i in range(numLetters):
            wordLetter = self.word[i]
            if wordLetter in letterCount:
                continue

            numFound = 0
            for j in range(i, numLetters):
                patternLetter = self.pattern[j]
                if self.word[j] == wordLetter and (patternLetter == 'y' or patternLetter == 'g'):
                    numFound += 1

            if numFound > 0:
                letterCount[wordLetter] = numFound

        return letterCount
