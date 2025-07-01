

class LetterStatistics:
    def __init__(self, count: int, exactCount: bool):
        super().__init__()

        if count < 0 or count > 5:
            raise ValueError('Count must be between 0 and 5!')

        self.count = count
        self.exactCount = exactCount


