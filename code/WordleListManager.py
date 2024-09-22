from code.Entry import Entry
from code.UntriedLetterWordFilter import UntriedLetterWordFilter
from code.WordList import WordList
from code.WordleWordFilter import WordleWordFilter
from code.YLetterWordFilter import YLetterWordFilter


def createWordleFilterWordlist(wordList:WordList) -> WordList:
    filteredWordList = WordList(wordList)
    wordFilter = WordleWordFilter()
    filteredWordList.addWordFilter(wordFilter)
    return filteredWordList


def createYLetterFilterWordlist(wordList:WordList) -> WordList:
    filteredWordList = WordList(wordList)
    wordFilter = YLetterWordFilter()
    filteredWordList.addWordFilter(wordFilter)
    return filteredWordList


def createUntriedLetterFilterWordlist(wordList:WordList) -> WordList:
    filteredWordList = WordList(wordList)
    wordFilter = UntriedLetterWordFilter()
    filteredWordList.addWordFilter(wordFilter)
    return filteredWordList


class WordleListManager:
    def __init__(self, wordList:WordList, managerName:str):
        self.managerName = managerName
        self.listOfLists = []
        self.listOfLists.append(createWordleFilterWordlist(wordList))
        self.listOfLists.append(createYLetterFilterWordlist(wordList))
        self.listOfLists.append(createUntriedLetterFilterWordlist(wordList))

    def applyEntry(self, entry:Entry):
        for wordList in self.listOfLists:
            wordList.filterList(entry)

