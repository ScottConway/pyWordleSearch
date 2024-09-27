import re
class WordChecker:

    @staticmethod
    def validate(word):
        goodWord = True
        word = word.replace(" ", "")
        checkedWord = word
        error = ""

        if len(word) != 5:
            error = "Wordle words must only be five characters long."
            goodWord = False
            return goodWord, checkedWord, error

        match = re.match("^[a-zA-Z]{5}$", word)
        if match is None:
            error = "The wordle word must be five alphabetic characters long."
            goodWord = False
        else:
            checkedWord = checkedWord.lower()

        return goodWord, checkedWord, error
