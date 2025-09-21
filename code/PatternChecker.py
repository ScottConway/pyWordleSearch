import re
class PatternChecker:
    """
    This class validates the pattern resulting from an wordle search.

    A valid pattern is five characters long and consists of only g, x, and/or y.
    """
    @staticmethod
    def validate(pattern: str) -> tuple[bool, str, str]:
        """
        Validates a pattern.
        :param pattern:
        :return:  goodPattern: True if pattern is valid, False otherwise.
                  checkedPattern: The pattern passed in for validation - lowercased.
                  error: an error message if the pattern is invalid.
        """
        goodPattern = True
        checkedPattern = pattern
        error = ""

        match = re.match("^[xygXYG]{5}$", pattern)
        if match is None:
            error = "The wordle result must be five characters and consist of g, x, or y (upper or lowercased)."
            goodPattern = False
        else:
            checkedPattern = checkedPattern.lower()

        return goodPattern, checkedPattern, error
