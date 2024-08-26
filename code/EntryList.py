from code.Entry import Entry


class EntryList:
    mustHaveLetters = set()

    def __init__(self):
        self.entries = []
        self.entryDictionary = {}

    def updateMustHaveLetters(self, entry: Entry):
        for i in range(5):
            wordLetter = entry.word[i]
            patternLetter = entry.pattern[i]
            if patternLetter == 'y' or patternLetter == 'g':
                self.mustHaveLetters.add(wordLetter)

    def add(self, entry: Entry):
        if entry.word in self.entryDictionary:
            raise ValueError(f'{entry.word} already used.')

        self.updateMustHaveLetters(entry)
        if len(self.mustHaveLetters) > 5:
            raise Exception('Typo in word or pattern as you have identified matches in more than five letters!')

        self.entries.append(entry)
        self.entryDictionary[entry.word] = entry

    @staticmethod
    def mustHaveLetterSet():
        return EntryList.mustHaveLetters.copy()

    @classmethod
    def clear(cls):
        EntryList.mustHaveLetters.clear()

    def validateEntry(self, entry: Entry) -> tuple[bool, str]:
        if entry.word in self.entryDictionary:
            return False, 'Word already used.'

        entryMustHaveLetters = entry.mustHaveLettersSet()
        listMustHaveLetters = self.mustHaveLetters.copy()

        unionSet = listMustHaveLetters | entryMustHaveLetters
        if len(unionSet) > 5:
            return False, 'Too many must have letters.'

        return True, "no error"
