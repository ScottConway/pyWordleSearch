#!/usr/bin/env python3

import argparse
import re

mustHaveCharacters = set()
letterWeight = {"e": 1116, "a": 849, "r": 758, "i": 754, "o": 716,
                "t": 695, "n": 665, "s": 574, "l": 549, "c": 454,
                "u": 363, "d": 338, "p": 317, "m": 301, "h": 300,
                "g": 247, "b": 207, "f": 181, "y": 178, "w": 129,
                "k": 110, "v": 101, "x": 29, "z": 27, "j": 20, "q": 19}
wordWeightDictionary = {}


def buildPattern(patternList):
    patternString = ""

    for pattern in patternList:
        patternString += pattern

    return patternString


def removeCharacterFromPattern(pattern, wordCharacter, patternCharacter):
    if len(pattern) > 1 and patternCharacter != 'g':
        return pattern.replace(wordCharacter, "")

    return pattern


def updatePattern(index, patternList, wordCharacter, resultCharacter, resultPattern):
    if resultCharacter == 'x':
        if wordCharacter in mustHaveCharacters:
            patternList[index] = removeCharacterFromPattern(patternList[index], wordCharacter, resultPattern[index])
        else:
            for i in range(5):
                patternList[i] = removeCharacterFromPattern(patternList[i], wordCharacter, resultPattern[i])

    if resultCharacter == 'y':
        value = removeCharacterFromPattern(patternList[index], wordCharacter, resultPattern[index])
        patternList[index] = value
        mustHaveCharacters.add(wordCharacter)

    if resultCharacter == 'g':
        patternList[index] = wordCharacter
        mustHaveCharacters.add(wordCharacter)

    return patternList


def updatePatternList(patternList, testWord, result):
    for i in range(5):
        patternList = updatePattern(i, patternList, testWord[i], result[i], result)

    return patternList


def printPattern(patternList):
    for pattern in patternList:
        print(pattern)


def determineWeight(word):
    wordSum = 0
    firstLetter = word[0]
    lastLetter = word[4]
    for letter in word:
        wordSum += letterWeight[letter]

    if "taodw".find(firstLetter) != -1:
        wordSum += 1000

    if "esdt".find(lastLetter) != -1:
        wordSum += 1000

    return wordSum


def buildWordList(fileName):
    file = open(fileName, "r")
    wordList = list()

    for line in file:
        word = line.strip('\n')
        if re.match("[a-z]{5}", word):
            wordList.append(word)
            wordWeightDictionary.update({word: determineWeight(word)})
        else:
            print(f'{word} is invalid as all words must be five alphabetic letter.  Ignored from {fileName}')

    return wordList


def hasRequiredCharacters(word):
    if len(mustHaveCharacters) == 0:
        return True

    for letter in mustHaveCharacters:
        if word.find(letter) == -1:
            return False

    return True


def narrowWordList(wordList, pattern):
    newWordList = list()
    for word in wordList:
        match = re.match(pattern, word)

        if match and hasRequiredCharacters(word):
            newWordList.append(word)

    return newWordList


def validateWord(testWord):
    goodWord = True

    if len(testWord) != 5:
        print("Wordle words must only be five characters long.")
        goodWord = False

    return goodWord


def validatePattern(pattern):
    goodPattern = True

    match = re.match("^[xyg]{5}$", pattern)
    if match is None:
        print("The wordle result must be five characters and const of g, x, or y.")
        goodPattern = False

    return goodPattern


def getWordWeight(word):
    return wordWeightDictionary[word]


def main():
    parser = argparse.ArgumentParser(
        description='Helper program for wordle game.')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0.0')

    patternList = ["[abcdefghijklmnopqrstuvwxyz]", "[abcdefghijklmnopqrstuvwxyz]", "[abcdefghijklmnopqrstuvwxyz]",
                   "[abcdefghijklmnopqrstuvwxyz]", "[abcdefghijklmnopqrstuvwxyz]"]
    checkPattern = buildPattern(patternList)
    wordList = buildWordList('fiveLetterWords.txt')
    commonWordList = buildWordList('commonFiveLetterWords.txt')

    while len(checkPattern) > 5 and (len(wordList) > 1 or len(commonWordList) > 1):
        initialWordListSize = len(wordList)
        initialCommonSetSize = len(commonWordList)
        testWord = ""
        result = ""
        goodWord = False
        goodPattern = False

        while not goodWord:
            testWord = input("Word entered in wordle: ")
            goodWord = validateWord(testWord)

        while not goodPattern:
            result = input(
                "Enter result from wordle x - no match, y - match wrong position, g - correct letter in correct "
                "position: ")
            goodPattern = validatePattern(result)

        # printPattern(patternList)

        patternList = updatePatternList(patternList, testWord, result)
        checkPattern = buildPattern(patternList)

        # printPattern(patternList)

        wordList = narrowWordList(wordList, checkPattern)
        commonWordList = narrowWordList(commonWordList, checkPattern)
        updatedwordListSize = len(wordList)
        updatedCommonSetSize = len(commonWordList)

        print(f'Your choice has narrowed the full possibilities from {initialWordListSize} to {updatedwordListSize}')
        wordList.sort(key=getWordWeight, reverse=True)
        print(wordList)

        print(
            f'Your choice has narrowed the common possibilities from {initialCommonSetSize} to {updatedCommonSetSize}')
        commonWordList.sort(key=getWordWeight, reverse=True)
        print(commonWordList)


if __name__ == '__main__':
    main()
