import argparse
import code.EntryList

from code.Entry import Entry
from code.WordListDirector import WordListDirector
from code.WordleDisplayHelper import WordleDisplayHelper
from code.EntryList import EntryList


def main():
    parser = argparse.ArgumentParser(
        description='Helper program for wordle game.')
    parser.add_argument('--version', action='version', version='%(prog)s 3.0.2')
    director = WordListDirector()

    if code.EntryList.entryListInstance is None:
        code.EntryList.entryListInstance = EntryList()

    finished = False

    director.printInitialReport()

    while not finished:
        WordleDisplayHelper.firstPrompt()

        testWord = input("Word entered in wordle: ")
        splitWord = False
        result = ""
        if testWord.lower() == 'help':
            WordleDisplayHelper.printHelp()
            continue
        elif testWord.lower() == 'history':
            WordleDisplayHelper.printEntryList(code.EntryList.entryListInstance)
            print()
            continue
        elif testWord.lower() == 'redisplay':
            director.printReport()
            continue
        elif testWord.lower() == 'quit' or testWord.lower() == 'exit':
            finished = True
            continue
        elif len(testWord) > 5 and testWord[5] == '-':
            result = testWord[-5:]
            testWord = testWord[0:5]
            splitWord = True

        if not splitWord:
            result = input(
                "Enter result from wordle x - no match, y - match wrong position, g - correct letter in correct "
                "position: ")

        entry = Entry(testWord, result)

        isValid, errorMessage = code.EntryList.entryListInstance.validateEntry(entry)
        if isValid:
            code.EntryList.entryListInstance.add(entry)
            director.applyEntry(entry)
            director.printReport()
        else:
            if errorMessage == 'Word already used.':
                WordleDisplayHelper.printWordAlreadyUsed(entry, code.EntryList.entryListInstance)
            elif errorMessage == 'Too many must have letters.':
                WordleDisplayHelper.printTooManyMustHaveLetters(code.EntryList.entryListInstance)
            else:
                WordleDisplayHelper.printUnhandledError(errorMessage, entry, code.EntryList.entryListInstance)

            continue


if __name__ == '__main__':
    main()
