import re

from code.WordChecker import WordChecker
from code.RegxWordFilter import RegxWordFilter
from code.Entry import Entry


class WordList:

    def __init__(self, data):
        self.wordList = list()
        self.wordFilter = None
        if isinstance(data, list):
            for line in data:
                word = line.strip('\n')
                goodWord, checkedWord, error = WordChecker.validate(word)
                if goodWord:
                    self.wordList.append(checkedWord)
                else:
                    print(f'{word} is invalid as all words must be five alphabetic letter.  Ignored from {data}')
        elif isinstance(data, str):
            file = open(data, "r")

            for line in file:
                word = line.strip('\n')
                goodWord, checkedWord, error = WordChecker.validate(word)
                if goodWord:
                    self.wordList.append(checkedWord)
                else:
                    print(f'{word} is invalid as all words must be five alphabetic letter.  Ignored from {data}')
        else:
            raise ValueError(f"Data type {type(data)} not supported - only list and str allowed")

    def addWordFilter(self, wordFilter: RegxWordFilter):
        if self.wordFilter is None:
            self.wordFilter = wordFilter
        else:
            raise Exception('WordFilter already assigned to WordList')

    def filterList(self, entry: Entry):
        if self.wordFilter is None:
            raise Exception('WordFilter has not been assigned to WordList')
        self.wordFilter.updatefilterPattern(entry)
        self.wordList = [word for word in self.wordList if self.wordFilter.wordMatchesPattern(word)]




