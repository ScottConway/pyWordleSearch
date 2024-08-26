from code.Entry import Entry
from code.EntryList import EntryList


class WordleDisplayHelper:

    @staticmethod
    def firstPrompt():
        print()
        print("Enter the word, or word-pattern, or help for other commands")
        print()

    @staticmethod
    def printHelp():
        print()
        print("help: prints this help message")
        print("history: display past entries.")
        print("quit or exit: quit the program")
        print()
        input("Press enter to continue")

    @staticmethod
    def printWordAlreadyUsed(entry:Entry, entryList:EntryList):
        print()
        print(f'{entry.word} is already used')
        print()
        WordleDisplayHelper.printEntryList(entryList)
        print()
        input("Press enter to continue")

    @staticmethod
    def printEntryList(entryList:EntryList):
        print("Past Entries:")
        for i in range(len(entryList.entries)):
            entry = entryList.entries[i]
            print(f'{i}: {entry.word}  -  {entry.pattern}')

    @staticmethod
    def printUnhandledError(errorMessage:str, entry:Entry, entryList:EntryList):
        print()
        print(f'The entry {entry.word} failed with the following error: {errorMessage}')
        WordleDisplayHelper.printEntryList(entryList)
        print()
        input("Press enter to continue")

    @staticmethod
    def printTooManyMustHaveLetters(entryList):
        print()
        print('Too many must-have letters have been identified.')
        WordleDisplayHelper.printEntryList(entryList)
        print()
        input("Press enter to continue")