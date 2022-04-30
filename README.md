# pyWordleSearch
python script to help me out in wordle.

## Simple flow

The idea is to type in a five letter word then type in the result returned from wordle where X is no match, Y is yellow for that position and G for green. 

### example

>/usr/bin/python3 /Users/sconway/PycharmProjects/pyWordleSearch/pyWordle.py
>
>Word entered in wordle: atone
>
>Enter result from wordle x - no match, y - match wrong position, g - correct letter in correct position: yyxyx
>
>Your choice has narrowed the full possibilities from 15920 to 105
>
>['tunas', 'tangs', 'wants', 'tanks', 'tania', 'tanan', 'tairn', 'tarin', 'train', 'tanti', 'tinta', 'titan', 'nasat', 'rants', 'sanit', 'tacan', 'nants', 'inact', 'danta', 'tanha', 'snast', 'tuarn', 'uniat', 'tanga', 'inapt', 'banat', 'manit', 'tahin', 'canst', 'cants', 'sanct', 'tanya', 'tangi', 'thatn', 'kanat', 'tanak', 'tanka', 'natus', 'fanit', 'tunal', 'pants', 'twain', 'witan', 'hants', 'qanat', 'takin', 'gnast', 'gnats', 'tunca', 'unact', 'taxin', 'tansy', 'unapt', 'thuan', 'unhat', 'tunga', 'ratan', 'niata', 'naght', 'tufan', 'tandy', 'intra', 'tunka', 'nitta', 'thawn', 'tangy', 'santa', 'satan', 'hankt', 'natal', 'satin', 'wanty', 'catan', 'latin', 'tanzy', 'manta', 'untar', 'uinta', 'ganta', 'patin', 'pinta', 'batan', 'matin', 'ranty', 'fanti', 'snath', 'natty', 'kitan', 'vinta', 'natch', 'nasty', 'santy', 'nantz', 'punta', 'untap', 'canty', 'bantu', 'panty', 'manty', 'katun', 'untax', 'banty', 'jantu', 'junta', 'janty']
>
>Your choice has narrowed the common possibilities from 530 to 2
>
>['train', 'nasty']
>
>Word entered in wordle: train
>
>Enter result from wordle x - no match, y - match wrong position, g - correct letter in correct position: ggggg
>
>Your choice has narrowed the full possibilities from 105 to 1
>
>['train']
>
>Your choice has narrowed the common possibilities from 2 to 1
>
>['train']
>
>Process finished with exit code 0


## Todo list

1. DONE - Create a separate regex pattern of all letters that are Y or G and ensure that all words presented have those letters.  Currently I am seeing situations words are showing up missing letters previously identified as yellow. 
2. If I use a letter twice in a word I am seeing situations where there is one Y and one X.   To me this means the letter is used only once in the word and my pattern matching should account for that. 
3. DONE - Additional safety/error checking code.  Word and pattern have exactly five characters.  Check the correctness of the pattern.
4. DONE - Ordered result list by a weighting based on the frequency in which the letters occur in the english language. 
5. DONE - Add a check when reading the input files to ensure that all the words are five characters and contain only letters. 