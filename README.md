# pyWordleSearch
python script to help me out in wordle.

**Table of Contents**

- [Original pyWordleSearch - version 2.x](OriginalPWS.md)  
- [OO Rewrite of pyWordleSearch - version 3.x](OORewrite.md)
- [Streamlit UI for OO Rewrite](StreamlitPWS.md)

## ToDo list

### Low-hanging fruit

- [x] Add a restart command to start over after finishing, or after a mistake, instead of quiting the app and starting over from the command line.

### Stretch/Long term goals

- [ ] Add a must-have characters map to supplement the set that counts and ensures the correct number of letters for faster filtering
- [ ] Better double letter logic for the above - see [this reddit post](https://www.reddit.com/r/wordle/comments/rypous/do_wordles_have_double_letters/).
- [x] Add a streamlit UI 

## Changes in version 3.1.0

- Added streamlit UI!!  Not as flashy as I had initially envisioned but fully functional.  Will look at improvements in later releases.

## Changes in version 3.0.3

- Added restart command. 

## Changes in version 3.0.2

- Added the YLetterWordWeigher to give more weight to words with more Y letters.
- Added the UntriedLetterWordWeigher to give more weight to words with untried letters.
- Removed the "Press enter to continue" input from non error messages. 

## Changes in version 3.0.1

- Add a redisplay command to redisplay hints
- Wired in WordWeigher to sort all lists by wordle weights
- display initial hints at start

## Changes in version 3.0.0

- Initial rewrite. 

**Older versions are in original pyWordleSearch readme**