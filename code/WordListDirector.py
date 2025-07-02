from code.Entry import Entry
from code.EntryListStatistics import EntryListStatistics
from code.EntryStatistics import EntryStatistics
from code.WordList import WordList
from code.WordleListManager import WordleListManager


class WordListDirector:
    def __init__(self):
        self.commonList = WordList('commonFiveLetterWords.txt')
        self.wordleList = WordList('wordleWords.txt')
        self.fullList = WordList('fiveLetterWords.txt')
        self.managerList = []
        self.managerList.append(WordleListManager(self.commonList, '### Common Five Letter Words'))
        self.managerList.append(WordleListManager(self.wordleList, '### Wordle Words'))
        self.managerList.append(WordleListManager(self.fullList, '### Full List Five Letter Words'))
        self.entryListStatistics = EntryListStatistics()

    def applyEntry(self, entry:Entry):
        self.entryListStatistics.addEntry(entry)
        for manager in self.managerList:
            manager.applyEntry(entry)

    def printReport(self):
        for manager in self.managerList:
            manager.printReport()

    def reportString(self) -> str:
        report = ''
        if self.entryListStatistics.totalMatchedCount() > 0:
            report += '**Required letter counts (\\* - exact count)** \n\n'
            report += self.entryListStatistics.reportString()
        for manager in self.managerList:
            report += manager.reportListString()

        return report

    def printInitialReport(self):
        for manager in self.managerList:
            manager.printInitialReport()

    def initialReportString(self) -> str:
        report = ''
        for manager in self.managerList:
            report += manager.initialReportString()
        return report