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

    def addEntry(self, entry):
        entryStatistics = EntryStatistics()
        entryStatistics.buildLetterStatistics(entry)
        self.addEntryStatistics(entryStatistics)

    def reportString(self) -> str:
        report = ''
        for key in self.gameWordListStats:
            letterStat = self.gameWordListStats[key]
            report += key + ': ' + str(letterStat.count)
            if letterStat.exactCount:
                report += '*'
            report += ' \t '
        report += '\n'
        return report

    def doesWordMatchCounts(self, word:str) -> bool:
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


