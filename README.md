# pyWordleSearch
python script to help me out in wordle.

## Simple flow

The idea is to type in a five letter word then type in the result returned from wordle where X is no match, Y is yellow for that position and G for green. 

### example

>sconway@Scott-Conways-MacBook pyWordleSearch % ./pyWordle.py
>Top suggestions from all untried letters
>['cares', 'bares', 'pares', 'tares', 'cores', 'bores', 'mares', 'pores', 'canes', 'dares']
>Word entered in wordle: atone
>Enter result from wordle x - no match, y - match wrong position, g - correct letter in correct position: yxyxx
>Your choice has narrowed the possibilities of Wordle words from 12947 to 361
>['boras', 'moras', 'coals', 'goras', 'boars', 'colas', 'soras', 'bolas', 'horas', 'faros', 'koras', 'boaks', 'goals', 'calos', 'saros', 'molas', 'foals', 'haros', 'soars', 'comas', 'bomas', 'solas', 'hoars', 'karos', 'codas', 'goads', 'roads', 'kolas', 'soaks', 'camos', 'loads', 'roams', 'foams', 'soaps', 'loams', 'halos', 'voars', 'doabs', 'lomas', 'capos', 'somas', 'dopas', 'woads', 'pacos', 'goafs', 'homas', 'loafs', 'mowas', 'koaps', 'socas', 'sodas', 'moyas', 'sobas', 'dagos', 'moxas', 'gapos', 'fados', 'soyas', 'hokas', 'makos', 'sados', 'sofas', 'sagos', 'hoyas', 'mayos', 'sojas', 'praos', 'yogas', 'kagos', 'lazos', 'roars', 'kohas', 'gajos', 'kayos', 'jiaos', 'cocas', 'boabs', 'bobas', 'chaos', 'dosas', 'orals', 'uraos', 'oumas', 'dados', 'oasis', 'ohias', 'oupas', 'kokas', 'orcas', 'soapy', 'okras', 'sarod', 'opals', 'obias', 'soral', 'moray', 'coaly', 'odals', 'ovals', 'foray', 'solar', 'savoy', 'coady', 'sorda', 'goary', 'solah', 'ogams', 'opahs', 'ollas', 'hoary', 'sargo', 'board', 'coria', 'odahs', 'coral', 'copay', 'boral', 'poral', 'sowar', 'okays', 'foamy', 'loamy', 'bolar', 'ofays', 'sofar', 'sapor', 'carol', 'polar', 'moria', 'hoagy', 'moral', 'borak', 'salop', 'parol', 'goral', 'coram', 'savor', 'sopra', 'molar', 'sokah', 'hoard', 'borax', 'woald', 'horal', 'carom', 'sorra', 'moira', 'bardo', 'salvo', 'cargo', 'douar', 'dolia', 'dorsa', 'foram', 'carob', 'pargo', 'folia', 'comal', 'coarb', 'korai', 'carbo', 'pagod', 'polka', 'roary', 'boyar', 'sambo', 'poach', 'volar', 'copal', 'cobia', 'podia', 'dorba', 'doula', 'maiko', 'podal', 'daiko', 'dorad', 'parvo', 'largo', 'salol', 'doura', 'cowal', 'domal', 'voila', 'gobar', 'dowar', 'goura', 'rolag', 'romal', 'copra', 'pokal', 'lobar', 'joram', 'korma', 'cobra', 'roach', 'modal', 'garbo', 'valor', 'dolma', 'payor', 'coala', 'coxal', 'forza', 'loach', 'colza', 'boyla', 'dosai', 'sajou', 'focal', 'logia', 'galop', 'boxla', 'dobla', 'radio', 'pilao', 'labor', 'mayor', 'koura', 'douma', 'maror', 'joual', 'dobra', 'campo', 'royal', 'barro', 'roral', 'favor', 'mowra', 'macro', 'qorma', 'yarco', 'gopak', 'louma', 'loral', 'kogal', 'waldo', 'morra', 'major', 'coyau', 'poaka', 'raupo', 'boyau', 'pulao', 'gompa', 'basho', 'jowar', 'galvo', 'vocal', 'hopak', 'cohab', 'vapor', 'shako', 'dosha', 'horah', 'dogma', 'gadso', 'molal', 'farro', 'jalop', 'koala', 'cobza', 'bayou', 'oracy', 'baloo', 'rojak', 'mocha', 'molla', 'miaou', 'saddo', 'miaow', 'cahow', 'gambo', 'coach', 'mohua', 'chiao', 'macho', 'claro', 'wacko', 'karoo', 'vodka', 'spado', 'holla', 'hodad', 'vocab', 'guaco', 'havoc', 'diazo', 'kapow', 'yapok', 'hallo', 'gadjo', 'hodja', 'bobak', 'draco', 'bravo', 'local', 'comma', 'jambo', 'basso', 'ovary', 'chado', 'bobac', 'casco', 'zambo', 'bocca', 'yakow', 'loyal', 'fossa', 'razor', 'bazoo', 'oakum', 'bacco', 'yowza', 'caboc', 'lasso', 'cabob', 'orach', 'ouija', 'kokra', 'orgia', 'gazoo', 'razoo', 'mambo', 'omrah', 'cacao', 'volva', 'kokam', 'orval', 'whamo', 'kapok', 'wokka', 'orixa', 'koppa', 'wazoo', 'wahoo', 'kazoo', 'cocoa', 'omlah', 'kabob', 'zoppa', 'yahoo', 'oidia', 'baboo', 'oscar', 'chaco', 'lazzo', 'poppa', 'imago', 'momma', 'oflag', 'okapi', 'igapo', 'gogga', 'ollav', 'omasa', 'ogham', 'oshac', 'ossia', 'occam', 'offal']
>Your choice has narrowed the common possibilities from 530 to 13
>['board', 'moral', 'howay', 'radio', 'royal', 'major', 'coach', 'wacko', 'havoc', 'kapow', 'hallo', 'bravo', 'local']
>Exotic words
>['maros', 'cados', 'fogas', 'cayos', 'wocas', 'pahos', 'wokas', 'kados', 'vamos', 'majos', 'jakos', 'basos', 'orias', 'soary', 'solay', 'soaky', 'ozias', 'doray', 'foaly', 'coaid', 'sarpo', 'somal', 'poria', 'sorva', 'corah', 'soapi', 'coaxy', 'carlo', 'doria', 'woady', 'salmo', 'mario', 'solfa', 'calor', 'sofia', 'balor', 'bailo', 'cafoy', 'baroi', 'cairo', 'fario', 'sacro', 'cardo', 'horla', 'pardo', 'korah', 'dorab', 'marok', 'morga', 'bolag', 'marko', 'baioc', 'holia', 'vario', 'forma', 'koila', 'codal', 'dargo', 'marco', 'bocal', 'copia', 'polab', 'fardo', 'occas', 'molka', 'rosal', 'bagio', 'pomak', 'cabio', 'balow', 'parao', 'couma', 'palmo', 'koali', 'caroa', 'burao', 'sosia', 'oaric', 'bowla', 'samoa', 'bozal', 'dogal', 'jalor', 'mohar', 'caupo', 'voraz', 'gobia', 'pablo', 'mopla', 'karou', 'coroa', 'posca', 'gouda', 'lohar', 'dogra', 'falco', 'balao', 'korwa', 'kaimo', 'jarmo', 'pasmo', 'goala', 'daijo', 'kogia', 'loxia', 'bayok', 'gorra', 'colla', 'filao', 'volga', 'forra', 'padou', 'somma', 'daroo', 'domba', 'shado', 'iodal', 'callo', 'kogai', 'garoo', 'ballo', 'madoc', 'loasa', 'koroa', 'rambo', 'bacao', 'wasco', 'cajou', 'hawok', 'lodha', 'mowha', 'haloa', 'kouza', 'kosha', 'prado', 'couac', 'popal', 'washo', 'zosma', 'macao', 'papio', 'jacko', 'pharo', 'bossa', 'mohwa', 'huaco', 'vacuo', 'kohua', 'drago', 'zohak', 'cravo', 'gagor', 'jacob', 'kamao', 'oasal', 'pompa', 'mocoa', 'passo', 'lobal', 'ousia', 'oolak', 'oulap', 'jakob', 'coppa', 'baubo', 'oadal', 'orary', 'caddo', 'lokao', 'bahoo', 'capoc', 'homam', 'wayao', 'kokia', 'jiboa', 'oukia', 'vacoa', 'fodda', 'mafoo', 'kodak', 'magog', 'biabo', 'macco', 'vijao', 'orgal', 'flavo', 'oopak', 'oriya', 'haddo', 'cocao', 'yaboo', 'wappo', 'oliva', 'gazoz', 'crcao', 'yazoo', 'ozark', 'ovula', 'oskar', 'ygapo', 'olcha', 'oryza', 'idaho', 'oozoa', 'osaka', 'omaha', 'ossal', 'icaco']
> 
>Top suggestions from all untried letters
>['cirls', 'birls', 'pirls', 'puris', 'curls', 'burls', 'dirls', 'purls', 'birks', 'girls']
>Word entered in wordle: girls
>Enter result from wordle x - no match, y - match wrong position, g - correct letter in correct position: xxxyg
>Your choice has narrowed the possibilities of Wordle words from 361 to 13
>['colas', 'bolas', 'calos', 'molas', 'solas', 'kolas', 'loads', 'loams', 'halos', 'lomas', 'loafs', 'lazos', 'ollas']
>
>Top suggestions from all untried letters
>['bumpy', 'dumky', 'dumpy', 'mucky', 'ducky', 'humpy', 'duchy', 'jumpy', 'jumby', 'bumph']
>Word entered in wordle: duchy
>Enter result from wordle x - no match, y - match wrong position, g - correct letter in correct position: xxxyx
>Your choice has narrowed the possibilities of Wordle words from 13 to 1
>['halos']
>sconway@Scott-Conways-MacBook pyWordleSearch %  
>

## Changes in version 2.0.0

Replaced the commonFiveLetterWords.txt with a word list from https://github.com/tabatkins/wordle-list which is supposed
to have been taken from the Wordle source code.

Changed the generic letter weight map with weight maps generated from https://github.com/ScottConway/pyWordleStats

## Changes in version 2.1.0

Put the common five letter list back.  Now displays wordle words, common words, then a list from the full words that
are not already displayed in the wordle or common words (exotic words).

At the beginning of each iteration print a list of most possible words from untried letters. 

## Todo list

1. DONE - Create a separate regex pattern of all letters that are Y or G and ensure that all words presented have those letters.  Currently I am seeing situations words are showing up missing letters previously identified as yellow. 
2. If I use a letter twice in a word I am seeing situations where there is one Y and one X.   To me this means the letter is used only once in the word and my pattern matching should account for that. 
3. DONE - Additional safety/error checking code.  Word and pattern have exactly five characters.  Check the correctness of the pattern.
4. DONE - Ordered result list by a weighting based on the frequency in which the letters occur in the english language. 
5. DONE - Add a check when reading the input files to ensure that all the words are five characters and contain only letters. 