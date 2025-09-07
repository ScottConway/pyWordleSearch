from code.Entry import *

entryListInstance = None

class EntryList:
    """
    Maintains a list of Entry instances and performs work across them.

    Maintains sets of letters that have been tried, letters that have identified as in the final answer (mustHaveLetters),
    letters that have been noted as a G (correct letter in the correct location), and letters that have been noted as
    a Y (correct letter in an incorrect location).

    Attributes:
        entries : the list of Entry instances for processing.
        entryDictionary : a dictionary mapping Entry words to Entry instances for quick instances.
    """
    mustHaveLetters = set()
    gLetters = set()
    yLetters = set()
    triedLetters = set()

    def __init__(self):
        self.entries = []
        self.entryDictionary = {}

    def hasEntries(self) -> bool:
        """
        Returns True if the list is not empty.
        :return: if there are entries in the list
        """
        return len(self.entries) > 0

    def reset(self):
        """
        Resets the EntryList to its initial state.
        """
        self.entries = []
        self.entryDictionary = {}
        self.mustHaveLetters = set()
        self.gLetters = set()
        self.yLetters = set()
        self.triedLetters = set()

    def updateMustHaveLetters(self, entry: Entry):
        """
        Updates the mustHaveLetters attribute with the information from an Entry instance.
        :param entry: an Entry instance
        """
        for i in range(MaxWordSize):
            wordLetter = entry.word[i]
            patternLetter = entry.pattern[i]
            self.triedLetters.add(wordLetter)
            if patternLetter == Y or patternLetter == G:
                self.mustHaveLetters.add(wordLetter)
                if patternLetter == G:
                    self.gLetters.add(wordLetter)
                else:
                    self.yLetters.add(wordLetter)

    def add(self, entry: Entry):
        """
        Adds an Entry instance to the list and entryDictionary.
        :param entry:
        """
        if entry.word in self.entryDictionary:
            raise ValueError(f'{entry.word} already used.')

        self.updateMustHaveLetters(entry)
        if len(self.mustHaveLetters) > MaxWordSize:
            raise Exception('Typo in word or pattern as you have identified matches in more than five letters across all entries!')

        self.entries.append(entry)
        self.entryDictionary[entry.word] = entry

    @staticmethod
    def mustHaveLetterSet():
        return EntryList.mustHaveLetters.copy()

    @staticmethod
    def yLetterSet():
        return EntryList.yLetters.copy()

    @staticmethod
    def triedLetterSet():
        return EntryList.triedLetters.copy()

    @classmethod
    def clear(cls):
        EntryList.mustHaveLetters.clear()
        EntryList.yLetters.clear()
        EntryList.triedLetters.clear()
        EntryList.gLetters.clear()

    def validateEntry(self, entry: Entry) -> tuple[bool, str]:
        if entry.word in self.entryDictionary:
            return False, 'Word already used.'

        entryMustHaveLetters = entry.mustHaveLettersSet()
        listMustHaveLetters = self.mustHaveLetters.copy()

        unionSet = listMustHaveLetters | entryMustHaveLetters
        if len(unionSet) > MaxWordSize:
            return False, 'Too many must have letters.'

        return True, "no error"
