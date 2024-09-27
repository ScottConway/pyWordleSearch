# pyWordleSearch
python script to help me out in wordle.

## Simple flow

The idea is to type in a five letter word then type in the result returned from wordle where X is no match, Y is yellow for that position and G for green. 

### example

>Top suggestions from all untried letters
>['cares', 'bares', 'pares', 'tares', 'cores', 'bores', 'mares', 'pores', 'canes', 'dares']
>Word entered in wordle: atone-xxxyy
>
>Your choice has narrowed the possibilities of Wordle words from 12947 to 269
> 
>['cines', 'bines', 'pines', 'mines', 'dines', 'rines', 'fines', 'lines', 'sines', 'dunes', 'runes', 'wines', 'lunes', 'kines', 'vines', 'benes', 'zines', 'penes', 'menes', 'denes', 'genes', 'lenes', 'senes', 'nides', 'pynes']
> 
>Your choice has narrowed the common possibilities from 530 to 10
> 
>['henry', 'green', 'begin', 'newly', 'never', 'queen', 'under', 'inner', 'index', 'enemy']
> 
>Exotic words
> 
>['renes', 'niels', 'genys', 'hiney', 'piner', 'sumen', 'cinel', 'hiren', 'winer', 'senex', 'nizey', 'phren', 'ginep', 'chien', 'finew', 'bizen', 'snyed', 'pensy', 'riden', 'wisen', 'cerin', 'weren', 'mendy', 'renky', 'lifen']
> 
>Y weighted word list possibilities from 12947 to 269
> 
>Top ten y list
> 
>['mened', 'kines', 'vixen', 'yeven', 'neves', 'liney', 'enmew', 'kneel', 'enews', 'lumen']
> 
>Top suggestions from all untried letters
> 
>['cirls', 'birls', 'pirls', 'puris', 'curls', 'burls', 'dirls', 'purls', 'birks', 'girls']
> 
>Word entered in wordle: pines-xxyyx
> 
>
>Your choice has narrowed the possibilities of Wordle words from 269 to 16
> 
>['nerdy', 'nervy', 'newly', 'nelly', 'begun', 'needy', 'neeld', 'quern', 'rerun', 'neddy', 'queyn', 'neemb', 'enemy', 'knell', 'enurn', 'enzym']
> 
>Your choice has narrowed the common possibilities from 10 to 2
> 
>['newly', 'enemy']
> 
>Exotic words
> 
>['berun', 'kevyn', 'nehru', 'nebby', 'nexum', 'neffy', 'needn', 'exhbn', 'encyc']
> 
>Y weighted word list possibilities from 12947 to 16
> 
>Top ten y list
> 
>['nervy', 'begun', 'nerdy', 'enemy', 'enzym', 'quern', 'needy', 'neemb', 'queyn', 'neeld']
> 
>Top suggestions from all untried letters
> 
>['curly', 'burly', 'murly', 'gurly', 'curdy', 'hurly', 'murky', 'gurdy', 'durgy', 'curvy']
> 
>Word entered in wordle: nerdy-yggxx
>
>Your choice has narrowed the possibilities of Wordle words from 16 to 1
> 
>['rerun']
> 
>Exotic words
> 
>['berun']
> 
>Y weighted word list possibilities from 12947 to 3
> 
>Top ten y list
> 
>['quern', 'enurn', 'rerun']
> 

## Changes in version 2.0.0

Replaced the commonFiveLetterWords.txt with a word list from https://github.com/tabatkins/wordle-list which is supposed
to have been taken from the Wordle source code.

Changed the generic letter weight map with weight maps generated from https://github.com/ScottConway/pyWordleStats

## Changes in version 2.1.0

Put the common five letter list back.  Now displays wordle words, common words, then a list from the full words that
are not already displayed in the wordle or common words (exotic words).

At the beginning of each iteration print a list of most possible words from untried letters. 

## Changes in version 2.2.0

Now you can enter the word and pattern at the first prompt delimited by a dash. 

`Word entered in wordle: cares-xxxxg`

## Changes in version 2.3.0

Added a new list of alternate words weighted by letters marked by y in the pattern the highest if you want to narrow 
down where the yellows should really go. 

If you determine a letter is yellow or green and later mark it with an x in the pattern you will now get an error message.

Similarly, if you mark a letter as x and then later mark it as y or g you will get an error.   This will hopefully prevent 
errors due to typos in the pattern. 

## Changes in version 2.4.0

The common lists had no size limit causing a lot of scrolling.   Limited size of lists to 25.   

If pattern is all green then print a success message instead of an empty word list. 

Changed the weighting on repeated letters in the yWord weighting.   Basically if I have g, r, and f as y pattern letters then 
in the list of y words I want to see 'grift' before I see 'fluff' 

##  Changes in version 2.4.1

Commented out the feature I added in 2.3.0 where I keep a history of the pattern entered for letters and if a x goes to y/g 
vice versa I printed out an error message.   This is because I did not take into account duplicate letters.  In this 
case I had a word veils-xgxgg and then tried bells-xgxgg and that got an error because the letter l was g in veils but 
the FIRST l in bells was an x.   So I need to come up with an solution that takes duplicate letters into account. 

By the same token I can take that knowledge and beef up my mustHaveCharacters set to a map with letters and counts 
because using the results I can determine if there are repeating characters and ensure the words in the suggestion lists
have those repeats. 