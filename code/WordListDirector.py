from code.Entry import Entry
from code.WordList import WordList
from code.WordleListManager import WordleListManager


class WordListDirector:
    def __init__(self):
        self.commonList = WordList('commonFiveLetterWords.txt')
        self.wordleList = WordList('wordleWords.txt')
        self.fullList = WordList('fiveLetterWords.txt')
        self.managerList = []
        self.managerList.append(WordleListManager(self.commonList, 'Common Five Letter Words'))
        self.managerList.append(WordleListManager(self.wordleList, 'Wordle Words'))
        self.managerList.append(WordleListManager(self.fullList, 'Full List Five Letter Words'))

    def applyEntry(self, entry:Entry):
        for manager in self.managerList:
            manager.applyEntry(entry)

    def printReport(self):
        for manager in self.managerList:
            manager.printReport()

    def printInitialReport(self):
        for manager in self.managerList:
            manager.printInitialReport()