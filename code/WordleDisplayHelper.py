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
        print("history: display past entries")
        print("redisplay: redisplay last set of hints")
        print("restart: clear history and start over")
        print("quit or exit: quit the program")
        print()

    @staticmethod
    def helpMessage() -> str:
        helpString = """\n\n
        help: prints this help message.\n\n
        restart: clear history and start over.
        """
        return helpString

    @staticmethod
    def printWordAlreadyUsed(entry:Entry, entryList:EntryList):
        print()
        print(f'{entry.word} is already used')
        print()
        WordleDisplayHelper.printEntryList(entryList)
        print()
        input("Press enter to continue")

    @staticmethod
    def wordAleadyUsedMessage(entry:Entry, entryList:EntryList) -> str:
        returnString = f'{entry.word} is already used\n\n'
        return returnString

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
    def unhandledErrorMessage(errorMessage:str, entry:Entry) -> str:
        returnString = f'The entry {entry.word} failed with the following error: {errorMessage}\n\n'
        return returnString

    @staticmethod
    def printTooManyMustHaveLetters(entryList):
        print()
        print('Too many must-have letters have been identified.')
        WordleDisplayHelper.printEntryList(entryList)
        print()
        input("Press enter to continue")

    @staticmethod
    def tooManyMustHaveLettersMessage() -> str:
        returnString = 'Too many must-have letters have been identified.\n\n'
        return returnString