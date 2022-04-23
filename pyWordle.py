#!/usr/bin/env python3

import argparse
import re

mustHaveCharacters = set()

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
        for i in range(5):
            patternList[i] = removeCharacterFromPattern(patternList[i], wordCharacter, resultPattern[i])

    if resultCharacter == 'y':
        value = removeCharacterFromPattern(patternList[index], wordCharacter, resultPattern[index])
        patternList[index] = value
        mustHaveCharacters.update({wordCharacter})

    if resultCharacter == 'g':
        patternList[index] = wordCharacter
        mustHaveCharacters.update({wordCharacter})

    return patternList


def updatePatternList(patternList, testWord, result):
    for i in range(5):
        patternList = updatePattern(i, patternList, testWord[i], result[i], result)

    return patternList

def printPattern(patternList):
    for pattern in patternList:
        print(pattern)

def buildWordSet():
    file = open('fiveLetterWords.txt', "r")
    wordSet = set()

    for line in file:
        word = line.strip('\n')
        wordSet.update({word})

    return wordSet


def hasRequiredCharacters(word):
    if len(mustHaveCharacters) == 0:
        return True

    for letter in mustHaveCharacters:
        if word.find(letter) == -1:
            return False

    return True


def narrowWordSet(wordSet, pattern):
    newWordSet = set()
    for word in wordSet:
        match = re.match(pattern, word)

        if match and hasRequiredCharacters(word):
            newWordSet.update({word})

    return newWordSet


def validateWord(testWord):
    goodWord = True

    if len(testWord) != 5:
        print("Wordle words must only be five characters long.")
        goodWord = False

    return goodWord


def validatePattern(pattern):
    goodPattern = True

    match = re.match("^[xyg]{5}$", pattern)
    if match == None:
        print("The wordle result must be five characters and const of g, x, or y.")
        goodPattern = False

    return goodPattern


def main():
    parser = argparse.ArgumentParser(
        description='Helper program for wordle game.')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0.0')

    patternList = ["[abcdefghijklmnopqrstuvwxyz]","[abcdefghijklmnopqrstuvwxyz]","[abcdefghijklmnopqrstuvwxyz]","[abcdefghijklmnopqrstuvwxyz]","[abcdefghijklmnopqrstuvwxyz]"]
    checkPattern = buildPattern(patternList)
    wordSet = buildWordSet()

    while len(checkPattern) > 5 and len(wordSet) > 1:
        initialWordSetSize = len(wordSet)
        testWord = ""
        result = ""
        goodWord = False
        goodPattern = False

        while not goodWord:
            testWord = input("Word entered in wordle: ")
            goodWord = validateWord(testWord)

        while not goodPattern:
            result = input("Enter result from wordle x - no match, y - match wrong position, g - correct letter in correct position: ")
            goodPattern = validatePattern(result)

        printPattern(patternList)

        patternList = updatePatternList(patternList, testWord, result)
        checkPattern = buildPattern(patternList)

        printPattern(patternList)

        wordSet = narrowWordSet(wordSet, checkPattern)
        updatedWordSetSize = len(wordSet)

        print(f'Your choice has narrowed the possibilities from {initialWordSetSize} to {updatedWordSetSize}')
        print(wordSet)


if __name__ == '__main__':
    main()