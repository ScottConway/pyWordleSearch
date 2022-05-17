#!/usr/bin/env python3

import argparse
import re
from operator import itemgetter

mustHaveCharacters = set()

firstLetterWeight = {'w': 411, 'n': 325, 's': 1560, 'f': 595, 'p': 857, 'c': 920, 'b': 908, 't': 815, 'l': 575,
                     'd': 681, 'h': 488, 'j': 202, 'k': 375, 'a': 736, 'v': 242, 'o': 262, 'g': 637, 'e': 303, 'r': 628,
                     'i': 165, 'm': 693, 'z': 105, 'u': 189, 'q': 78, 'y': 181, 'x': 16}
secondLetterWeight = {'o': 2093, 'i': 1380, 'w': 163, 'e': 1626, 'y': 267, 'l': 697, 't': 239, 'a': 2260, 'r': 940,
                      'h': 544, 'u': 1185, 'b': 81, 'x': 57, 'm': 188, 's': 93, 'n': 345, 'v': 52, 'd': 84, 'g': 75,
                      'f': 24, 'p': 228, 'k': 95, 'c': 176, 'q': 15, 'z': 29, 'j': 11}
thirdLetterWeight = {'m': 510, 'k': 268, 'a': 1235, 'e': 882, 'l': 848, 'n': 962, 'o': 989, 'b': 334, 'u': 666,
                     'f': 178, 'r': 1197, 'p': 363, 'i': 1047, 's': 531, 'x': 133, 'd': 390, 't': 615, 'y': 213,
                     'g': 362, 'w': 271, 'v': 240, 'c': 392, 'h': 120, 'z': 142, 'q': 13, 'j': 46}
fourthLetterWeight = {'e': 2323, 'a': 1073, 'c': 406, 'n': 786, 'g': 422, 'r': 716, 'd': 471, 'p': 418, 'o': 696,
                      'i': 880, 's': 515, 't': 897, 'l': 771, 'm': 402, 'u': 401, 'k': 500, 'f': 233, 'y': 108,
                      'w': 128, 'z': 126, 'h': 235, 'v': 155, 'j': 29, 'b': 242, 'x': 12, 'q': 2}
fifthLetterWeight = {'n': 530, 'u': 67, 'k': 257, 's': 3950, 'd': 822, 'i': 280, 't': 726, 'y': 1297, 'a': 679,
                     'e': 1519, 'l': 475, 'h': 367, 'w': 64, 'g': 143, 'p': 147, 'c': 127, 'r': 673, 'x': 70, 'o': 388,
                     'm': 182, 'f': 82, 'b': 59, 'v': 4, 'z': 32, 'j': 3, 'q': 4}

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


def updatePatternList(patternList, testWord, result, untriedPatternList):
    for i in range(5):
        patternList = updatePattern(i, patternList, testWord[i], result[i], result)
        for y in range(5):
            untriedPatternList[y] = untriedPatternList[y].replace(testWord[i], "")

    return patternList, untriedPatternList


def printPattern(patternList):
    for pattern in patternList:
        print(pattern)


def determineWeight(word):
    wordSum = firstLetterWeight[word[0]] + secondLetterWeight[word[1]] + thirdLetterWeight[word[2]] + \
              fourthLetterWeight[word[3]] + fifthLetterWeight[word[4]]
    uniqueLetters = set()

    for letter in word:
        uniqueLetters.add(letter)

    wordSum += (1000 * len(uniqueLetters))

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


def narrowUntriedWordList(wordList, pattern):
    newWordList = list()
    for word in wordList:
        match = re.match(pattern, word)

        if match:
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


def printTopWordleWeightWords():
    print("Top weighted Wordle Words")
    count = 0
    for k, v in sorted(wordWeightDictionary.items(), key=itemgetter(1), reverse=True):
        print(f'{k}, {v}')
        count += 1
        if count > 10:
            break


def narrowFullWordList(fullWordList, commonWordList, wordleWordList):
    fullWordSet = set(fullWordList)
    fullWordSet = fullWordSet.difference(commonWordList).difference(wordleWordList)
    return list(fullWordSet)


def printTopTenUntriedWords(wordList):
    if len(wordList) > 0:
        print("Top suggestions from all untried letters")
        wordList.sort(key=getWordWeight, reverse=True)
        print(wordList[0:10])


def main():
    parser = argparse.ArgumentParser(
        description='Helper program for wordle game.')
    parser.add_argument('--version', action='version', version='%(prog)s 2.1.0')

    patternList = ["[abcdefghijklmnopqrstuvwxyz]", "[abcdefghijklmnopqrstuvwxyz]", "[abcdefghijklmnopqrstuvwxyz]",
                   "[abcdefghijklmnopqrstuvwxyz]", "[abcdefghijklmnopqrstuvwxyz]"]
    checkPattern = buildPattern(patternList)

    untriedPatternList = ["[abcdefghijklmnopqrstuvwxyz]", "[abcdefghijklmnopqrstuvwxyz]",
                          "[abcdefghijklmnopqrstuvwxyz]",
                          "[abcdefghijklmnopqrstuvwxyz]", "[abcdefghijklmnopqrstuvwxyz]"]
    untriedCheckPattern = buildPattern(untriedPatternList)

    wordList = buildWordList('wordleWords.txt')
    untriedWords = list(wordList)
    # uncomment to see a list of top wordle words by letter weight
    # printTopWordleWeightWords()
    commonWordList = buildWordList('commonFiveLetterWords.txt')
    fullWordList = buildWordList('fiveLetterWords.txt')

    while len(checkPattern) > 5 and (len(wordList) > 1 or len(commonWordList) > 1):
        initialWordListSize = len(wordList)
        initialCommonSetSize = len(commonWordList)
        testWord = ""
        result = ""
        goodWord = False
        goodPattern = False

        #printPattern(untriedPatternList)
        untriedWords = narrowUntriedWordList(untriedWords, untriedCheckPattern)
        printTopTenUntriedWords(wordList=untriedWords)

        while not goodWord:
            testWord = input("Word entered in wordle: ")
            goodWord = validateWord(testWord)

        while not goodPattern:
            result = input(
                "Enter result from wordle x - no match, y - match wrong position, g - correct letter in correct "
                "position: ")
            goodPattern = validatePattern(result)

        # printPattern(patternList)

        patternList, untriedPatternList = updatePatternList(patternList, testWord, result, untriedPatternList)
        checkPattern = buildPattern(patternList)
        untriedCheckPattern = buildPattern(untriedPatternList)

        # printPattern(patternList)

        wordList = narrowWordList(wordList, checkPattern)
        commonWordList = narrowWordList(commonWordList, checkPattern)
        fullWordList = narrowWordList(fullWordList, checkPattern)

        fullWordList = narrowFullWordList(fullWordList=fullWordList, commonWordList=commonWordList,
                                          wordleWordList=wordList)
        updatedwordListSize = len(wordList)
        updatedCommonSetSize = len(commonWordList)

        print("")
        print(
            f'Your choice has narrowed the possibilities of Wordle words from {initialWordListSize} to {updatedwordListSize}')
        wordList.sort(key=getWordWeight, reverse=True)
        print(wordList)

        if len(commonWordList) > 0:
            print(
                f'Your choice has narrowed the common possibilities from {initialCommonSetSize} to {updatedCommonSetSize}')
            commonWordList.sort(key=getWordWeight, reverse=True)
            print(commonWordList)

        if len(fullWordList) > 0:
            print("Exotic words")
            fullWordList.sort(key=getWordWeight, reverse=True)
            print(fullWordList)


if __name__ == '__main__':
    main()
