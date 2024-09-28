# pyWordleSearch Object Oriented Rewrite
python script to help me out in wordle.

## Simple flow

The idea is to type in a five letter word then type in the result returned from wordle where X is no match, Y is yellow for that position and G for green. 

### example

>python3 pyWordle.py
>
>Enter the word, or word-pattern, or help for other commands
>
>Word entered in wordle: atone-yxxxy
> 
	 - 	 Wordle Words
	 - 	 - 	 Matched words: ['gavel', 'dewar', 'fakey', 'hayed', 'herma', 'fazes', 'bares', 'sepad', 'gapes', 'wakes']
	 - 	 - 	 Y Letter words: ['gavel', 'dewar', 'fakey', 'hayed', 'herma', 'fazes', 'bares', 'sepad', 'gapes', 'wakes']
	 - 	 - 	 Untried Letter words: ['kipps', 'pukus', 'muils', 'lyric', 'fuggy', 'bulky', 'flurr', 'hully', 'durgy', 'ribby']

	 - 	 Common Five Letter Words
	 - 	 - 	 Matched words: ['beach', 'begad', 'bread', 'break', 'cheap', 'clear', 'cream', 'dream', 'early', 'equal']
	 - 	 - 	 Y Letter words: ['beach', 'begad', 'bread', 'break', 'cheap', 'clear', 'cream', 'dream', 'early', 'equal']
	 - 	 - 	 Untried Letter words: ['build', 'child', 'civil', 'climb', 'dimly', 'drily', 'dryly', 'dully', 'frick', 'fully']

	 - 	 Full List Five Letter Words
	 - 	 - 	 Matched words: ['baaed', 'babel', 'babes', 'bagel', 'bayed', 'baked', 'baker', 'bakes', 'baled', 'balei']
	 - 	 - 	 Y Letter words: ['baaed', 'babel', 'babes', 'bagel', 'bayed', 'baked', 'baker', 'bakes', 'baled', 'balei']
	 - 	 - 	 Untried Letter words: ['bhili', 'bibby', 'bibbs', 'bichy', 'biddy', 'bidri', 'bidry', 'biffy', 'biffs', 'bifid']
>
>Enter the word, or word-pattern, or help for other commands
>
> Word entered in wordle: cares-xyxyx
> 
	 - 	 Wordle Words
	 - 	 - 	 Matched words: ['kehua', 'pedal', 'medal', 'weamb', 'kwela', 'email', 'gleam', 'dedal', 'pepla', 'heady']
	 - 	 - 	 Y Letter words: ['kehua', 'pedal', 'medal', 'weamb', 'kwela', 'email', 'gleam', 'dedal', 'pepla', 'heady']
	 - 	 - 	 Untried Letter words: ['fuggy', 'bulky', 'hully', 'wimpy', 'bivvy', 'lummy', 'bilgy', 'flimp', 'kudzu', 'limby']

	 - 	 Common Five Letter Words
	 - 	 - 	 Matched words: ['begad', 'equal', 'heavy', 'hella', 'ideal', 'legal', 'yeeha']
	 - 	 - 	 Y Letter words: ['begad', 'equal', 'heavy', 'hella', 'ideal', 'legal', 'yeeha']
	 - 	 - 	 Untried Letter words: ['build', 'dimly', 'dully', 'fully', 'imply', 'jildi', 'plumb']

	 - 	 Full List Five Letter Words
	 - 	 - 	 Matched words: ['beady', 'beaky', 'beala', 'beamy', 'beaux', 'bebay', 'bedad', 'beday', 'begad', 'begay']
	 - 	 - 	 Y Letter words: ['beady', 'beaky', 'beala', 'beamy', 'beaux', 'bebay', 'bedad', 'beday', 'begad', 'begay']
	 - 	 - 	 Untried Letter words: ['bhili', 'bibby', 'biddy', 'biffy', 'bifid', 'biggy', 'bigly', 'bilbi', 'bilby', 'bilgy']

>
>Enter the word, or word-pattern, or help for other commands
> 
>Word entered in wordle: pedal-xgxyx
> 
	 - 	 Wordle Words
	 - 	 - 	 Matched words: ['kehua', 'weamb', 'mekka', 'keema', 'gemma', 'beamy', 'heavy', 'beaux', 'beaky']
	 - 	 - 	 Y Letter words: ['kehua', 'weamb', 'mekka', 'keema', 'gleba', 'gemma', 'beamy', 'heavy', 'edema', 'ulema']
	 - 	 - 	 Untried Letter words: ['fuggy', 'bivvy', 'jimmy', 'quiff', 'hubby', 'yummy', 'fuffy', 'huzzy', 'zuzim', 'mummy']

	 - 	 Common Five Letter Words
	 - 	 - 	 Matched words: ['heavy', 'yeeha']
	 - 	 - 	 Y Letter words: ['heavy', 'yeeha']

	 - 	 Full List Five Letter Words
	 - 	 - 	 Matched words: ['beaky', 'beamy', 'beaux', 'bemba', 'gemma', 'heavy', 'heazy', 'weaky']
	 - 	 - 	 Y Letter words: ['beaky', 'beamy', 'beaux', 'bemba', 'edema', 'ediya', 'ekaha', 'eliza', 'gemma', 'gleba']
	 - 	 - 	 Untried Letter words: ['bibby', 'biffy', 'biggy', 'bivvy', 'bubby', 'buffi', 'buffy', 'buggy', 'buzzy', 'figgy']

>
>Enter the word, or word-pattern, or help for other commands
>
>Word entered in wordle: heavy-ggggg
> 
	 - 	 Wordle Words
	 - 	 - 	 Matched words: ['heavy']
	 - 	 - 	 Y Letter words: ['kehua', 'weamb', 'mekka', 'keema', 'gleba', 'gemma', 'beamy', 'heavy', 'edema', 'ulema']
	 - 	 - 	 Untried Letter words: ['quiff', 'zuzim', 'zimbi', 'immix', 'buffi', 'gummi', 'jugum', 'mujik', 'kibbi']

	 - 	 Common Five Letter Words
	 - 	 - 	 Matched words: ['heavy']
	 - 	 - 	 Y Letter words: ['heavy', 'yeeha']

	 - 	 Full List Five Letter Words
	 - 	 - 	 Matched words: ['heavy']
	 - 	 - 	 Y Letter words: ['beaky', 'beamy', 'beaux', 'bemba', 'edema', 'ediya', 'ekaha', 'eliza', 'gemma', 'gleba']
	 - 	 - 	 Untried Letter words: ['buffi', 'gibbi', 'immix', 'izumi', 'jiqui', 'jugum', 'kikki', 'kukui', 'kumbi', 'mujik']
>
>Enter the word, or word-pattern, or help for other commands
>
> Word entered in wordle: help
>
>help: prints this help message
>history: display past entries.
>quit or exit: quit the program
>
>Press enter to continue
>
>Enter the word, or word-pattern, or help for other commands
>
>Word entered in wordle: history
>Past Entries:
> 
>0: atone  -  yxxxy  
>1: cares  -  xyxyx  
>2: pedal  -  xgxyx  
>3: heavy  -  ggggg  
>
>Enter the word, or word-pattern, or help for other commands
>
>Word entered in wordle: quit



