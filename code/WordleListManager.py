from code.Entry import Entry
from code.UntriedLetterWordFilter import UntriedLetterWordFilter
from code.UntriedLetterWordWeigher import UntriedLetterWordWeigher
from code.WordList import WordList
from code.WordleWordFilter import WordleWordFilter
from code.WordleWordWeigher import WordleWordWeigher
from code.YLetterWordFilter import YLetterWordFilter
from code.YLetterWordWeigher import YLetterWordWeigher


def createWordleFilterWordlist(wordList:WordList) -> WordList:
    filteredWordList = WordList(wordList)
    wordFilter = WordleWordFilter()
    filteredWordList.addWordFilter(wordFilter)
    weigher = WordleWordWeigher()
    filteredWordList.addWordWeigher(weigher)
    return filteredWordList


def createYLetterFilterWordlist(wordList:WordList) -> WordList:
    filteredWordList = WordList(wordList)
    wordFilter = YLetterWordFilter()
    filteredWordList.addWordFilter(wordFilter)
    weigher = YLetterWordWeigher()
    filteredWordList.addWordWeigher(weigher)
    return filteredWordList


def createUntriedLetterFilterWordlist(wordList:WordList) -> WordList:
    filteredWordList = WordList(wordList)
    wordFilter = UntriedLetterWordFilter()
    filteredWordList.addWordFilter(wordFilter)
    weigher = UntriedLetterWordWeigher()
    filteredWordList.addWordWeigher(weigher)
    return filteredWordList


def reportList(wordleList:WordList, header:str):
    if len(wordleList.wordList) == 0:
        return

    print(f'\t - \t - \t {header}: {wordleList.wordList[0:10]}')

def reportListString(wordleList:WordList, header:str) -> str:
    if len(wordleList.wordList) == 0:
        return ""
    wordleList.sortWords()
    returnString = f'{header}: {wordleList.wordList[0:10]}'
    return returnString

class WordleListManager:
    def __init__(self, wordList:WordList, managerName:str):
        self.managerName = managerName
        self.listOfLists = []

        self.wordleList = createWordleFilterWordlist(wordList)
        self.listOfLists.append(self.wordleList)
        self.yLetterList = createYLetterFilterWordlist(wordList)
        self.listOfLists.append(self.yLetterList)
        self.untriedLetterList = createUntriedLetterFilterWordlist(wordList)
        self.listOfLists.append(self.untriedLetterList)

    def applyEntry(self, entry:Entry):
        for wordList in self.listOfLists:
            wordList.filterList(entry)

    def printReport(self):

        totalWords = len(self.wordleList.wordList) + len(self.untriedLetterList.wordList) + len(self.yLetterList.wordList)
        if totalWords == 0:
            return

        print(f'\t - \t {self.managerName}')
        reportList(self.wordleList, 'Matched words')
        reportList(self.yLetterList, 'Y Letter words')
        reportList(self.untriedLetterList, 'Untried Letter words')
        print()

    def reportListString(self) -> str:
        totalWords = len(self.wordleList.wordList) + len(self.untriedLetterList.wordList) + len(
            self.yLetterList.wordList)
        if totalWords == 0:
            return ""

        returnString = f"{self.managerName}\n\n"

        returnString += reportListString(self.wordleList, 'Matched words')
        returnString += "\n\n"
        returnString += reportListString(self.yLetterList, 'Y Letter words')
        returnString += "\n\n"
        returnString += reportListString(self.untriedLetterList, 'Untried Letter words')
        returnString += "\n\n"

        return returnString

    def printInitialReport(self):

        totalWords = len(self.untriedLetterList.wordList)
        if totalWords == 0:
            return

        print(f'\t - \t {self.managerName}')
        reportList(self.untriedLetterList, 'Untried Letter words')
        print()

    def initialReportString(self) -> str:
        totalWords = len(self.untriedLetterList.wordList)
        if totalWords == 0:
            return ""

        returnString = f'{self.managerName}\n\n'
        returnString += reportListString(self.untriedLetterList, 'Untried Letter words')
        returnString += "\n\n"
        return returnString