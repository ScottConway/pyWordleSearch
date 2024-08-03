import re

from code import WordChecker


class WordList:
    def __init__(self, data):
        if isinstance(data, list):
            self.wordList = data
        elif isinstance(data, str):
            file = open(data, "r")
            self.wordList = list()

            for line in file:
                word = line.strip('\n')
                goodWord, checkedWord, error = WordChecker.validate(word)
                if goodWord:
                    self.wordList.append(checkedWord)
                else:
                    print(f'{word} is invalid as all words must be five alphabetic letter.  Ignored from {data}')
        else:
            raise ValueError(f"Data type {type(data)} not supported - only list and str allowed")
