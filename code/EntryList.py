from code.Entry import Entry


class EntryList:
    def __init__(self):
        self.entries = []
        self.entryDictionary = {}

    def add(self, entry: Entry):
        if entry.word in self.entryDictionary:
            raise ValueError(f'{entry.word} already used.')

        self.entries.append(entry)
        self.entryDictionary[entry.word] = entry
