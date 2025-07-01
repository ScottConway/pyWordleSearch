from code.EntryStatistics import EntryStatistics


class EntryListStatistics:
    def __init__(self):
        self.gameWordListStats = {}

    def addEntryStatistics(self, entryStats: EntryStatistics):
        for key in entryStats.wordLetters:
            if key not in self.gameWordListStats:
                self.gameWordListStats[key] = entryStats.wordLetters[key]
            elif not self.gameWordListStats[key].exactCount and self.gameWordListStats[key].count < entryStats.wordLetters[key].count:
                self.gameWordListStats[key] = entryStats.wordLetters[key]

    def clear(self):
        self.gameWordListStats = {}

    def totalMatchedCount(self) -> int:
        totalMatchedCount = 0
        for letterStat in self.gameWordListStats.values():
            totalMatchedCount += letterStat.count

        return totalMatchedCount

