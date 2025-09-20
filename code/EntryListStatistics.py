from code.EntryStatistics import EntryStatistics
from code.Entry import *


class EntryListStatistics:
    """
    This class maintains a list of entry statistics for all entries in a game.

    This is used to check words for possible matches.
    """
    def __init__(self):
        self.gameWordListStats = {}

    def addEntryStatistics(self, entryStats: EntryStatistics):
        """
        Adds an Entry Statistics object to this list

        Attributes:
            entryStats (EntryStatistics): Entry Statistics object
        """
        if entryStats is not None:
            for key in entryStats.wordLetters:
                if key not in self.gameWordListStats:
                    self.gameWordListStats[key] = entryStats.wordLetters[key]
                elif not self.gameWordListStats[key].exactCount and self.gameWordListStats[key].count < entryStats.wordLetters[key].count:
                    self.gameWordListStats[key] = entryStats.wordLetters[key]

    def clear(self):
        """
        Resets the statistics list.
        """
        self.gameWordListStats = {}

    def totalMatchedCount(self) -> int:
        """
        returns the total number of matches found.
        """
        totalMatchedCount = 0
        for letterStat in self.gameWordListStats.values():
            totalMatchedCount += letterStat.count

        return totalMatchedCount

    def addEntry(self, entry: Entry):
        """
        Generates statistics for an Entry object and adds it to the list.
        :param entry:
        """
        if entry is not None:
            entryStatistics = EntryStatistics()
            entryStatistics.buildLetterStatistics(entry)
            self.addEntryStatistics(entryStatistics)

    def reportString(self) -> str:
        """
        Returns a string representation of this list
        :return: an overglorified toString :)
        """
        report = ''
        for key in self.gameWordListStats:
            letterStat = self.gameWordListStats[key]
            report += f"{key}: {letterStat.count}{'*' if letterStat.exactCount else ''} \t"
        report += '\n'
        return report

    def doesWordMatchCounts(self, word:str) -> bool:
        """
        checks the word to see if it matches the stored statistics.
        :param word:
        :return: True if the word matches the stored statistics, False otherwise
        """
        if word is None or len(word) != MaxWordSize:
            return False

        for key in self.gameWordListStats:
            letterStat = self.gameWordListStats[key]
            occurrences = word.count(key)
            if occurrences == 0:
                return False

            if letterStat.exactCount and occurrences != letterStat.count:
                return False
            elif occurrences < letterStat.count:
                return False

        return True


