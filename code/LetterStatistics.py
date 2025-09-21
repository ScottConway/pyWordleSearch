

class LetterStatistics:
    """
    contains the statistics for a single letter in a Wordle game.
    """
    def __init__(self, count: int, exactCount: bool):
        """
        Initialize self.  See help(type(self)) for accurate signature.

        :param count:  Number of occurrences of the letter (0-5).
        :param exactCount:  if the number of occurrences is EXACT - meaning there is certainty that there are no more
        occurrences of this letter.
        """
        if count < 0 or count > 5:
            raise ValueError('Count must be between 0 and 5!')

        self.count: int = count
        self.exactCount: bool = exactCount


