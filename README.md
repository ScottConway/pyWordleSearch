# pyWordleSearch
python script to help me out in wordle.

## Simple flow

The idea is to type in a five letter word then type in the result returned from wordle where X is no match, Y is yellow for that position and G for green. 

### example

Enter word:  atone
Enter result: xyxxg

then the user will see a list of words that match that pattern and previous patterns as well and will keep looping until the result is all green or the user types exit. 

## Todo list

1. Create a separate regex pattern of all letters that are Y or G and ensure that all words presented have those letters.  Currently I am seeing situations words are showing up missing letters previously identified as yellow. 
2. If I use a letter twice in a word I am seeing situations where there is one Y and one X.   To me this means the letter is used only once in the word and my pattern matching should account for that. 
3. Additional safety/error checking code.   Like ensuring the word entered matches the existing pattern.   Word and pattern have exactly five characters.  Check the correctness of the pattern.