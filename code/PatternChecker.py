import re
class PatternChecker:

    @staticmethod
    def validate(pattern):
        goodPattern = True
        checkedPattern = pattern
        error = ""

        match = re.match("^[xygXYG]{5}$", pattern)
        if match is None:
            error = "The wordle result must be five characters and consist of g, x, or y."
            goodPattern = False
        else:
            checkedPattern = checkedPattern.lower()

        return goodPattern, checkedPattern, error
