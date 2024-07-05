import dataclasses

class Entry:
    def __init__(self, word, pattern, error=""):
        self.word = word
        self.pattern = pattern
        self.error = error
