import copy

from code.Entry import Entry
from code.RegxWordFilter import RegxWordFilter
from code.WordChecker import WordChecker
from code.WordWeigher import WordWeigher


class WordList:

    def __init__(self, data):
        self.wordList = list()
        self.wordFilter = None
        self.wordWeigher = None
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
        elif isinstance(data, WordList):
            self.wordList = copy.deepcopy(data.wordList)
        else:
            raise ValueError(f"Data type {type(data)} not supported - only list, str, and WordList allowed")

    def addWordFilter(self, wordFilter: RegxWordFilter):
        if self.wordFilter is None:
            self.wordFilter = wordFilter
        else:
            raise Exception('WordFilter already assigned to WordList')

    def addWordWeigher(self, wordWeigher: WordWeigher):
        if self.wordWeigher is None:
            self.wordWeigher = wordWeigher
        else:
            raise Exception('WordWeigher already assigned to WordList')

    def filterList(self, entry: Entry):
        if self.wordFilter is None:
            raise Exception('WordFilter has not been assigned to WordList')
        self.wordFilter.updatefilterPattern(entry)
        self.wordList = [word for word in self.wordList if self.wordFilter.wordMatchesPattern(word)]

    def sortWords(self):
        if self.wordWeigher is not None:
            self.wordList.sort(key=self.wordWeigher.determineWeight, reverse=True)

    def printTopWords(self):
        self.sortWords()
        print(self.wordList[0:25])
