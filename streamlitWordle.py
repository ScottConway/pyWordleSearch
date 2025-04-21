import argparse

import streamlit as st
import re

import code.EntryList
from code.Entry import Entry
from code.EntryList import EntryList
from code.WordListDirector import WordListDirector
from code.WordleDisplayHelper import WordleDisplayHelper


def main():
    ENTRY_PATTERN = "[a-z]{5}-[xyg]{5}"
    parser = argparse.ArgumentParser(
        description='Helper program for wordle game.')
    parser.add_argument('--version', action='version', version='%(prog)s 3.1.0')

    if "director" not in st.session_state:
        st.session_state["director"] = WordListDirector()

    director = st.session_state["director"]

    if code.EntryList.entryListInstance is None:
        code.EntryList.entryListInstance = EntryList()

    st.write("Input word and pattern ie atone-xxyyg")
    testWord = st.text_input(label='Input word and pattern ie atone-xxyyg', key='inputResult', max_chars=11,
                             help='Input word and pattern ie atone-xxyyg')

    col1, col2 = st.columns(2)

    with col1:
        resetPressed = st.button('Reset')

    with col2:
        helpPressed = st.button('Help')

    if resetPressed:
        director = WordListDirector()
        st.session_state["director"] = director
        code.EntryList.entryListInstance.reset()
        st.header("Report")
        st.write(director.initialReportString())
    elif helpPressed:
        display_help(director)
    elif testWord:
        if testWord.lower() == 'help':
            display_help(director)

        elif testWord.lower() == 'restart':
            director = WordListDirector()
            st.session_state["director"] = director
            code.EntryList.entryListInstance.reset()
            st.header("Report")
            st.write(director.initialReportString())
        elif len(testWord) != 11 or testWord[5] != '-':
            st.markdown(''':red[Incorrect format for entry must be a five letter word
            followed by a dash (-) then a five letter pattern.   
            The pattern is either the letter x for no match for that character position,  
            y for a match but incorrect position or g for correct match in correct position.]
            ''')
        else:
            testWord = testWord.lower()
            if not re.fullmatch(ENTRY_PATTERN, testWord):
                st.write(f'{testWord} is not a valid entry!  It must have five characters, a dash then five pattern '
                         f'characters (xyg)')
            else:
                result = testWord[-5:]
                testWord = testWord[0:5]
                entry = Entry(testWord, result)

                isValid, errorMessage = code.EntryList.entryListInstance.validateEntry(entry)
                if isValid:
                    code.EntryList.entryListInstance.add(entry)
                    director.applyEntry(entry)
                    entryListValues = [f"{x.word} - {x.pattern}" for x in code.EntryList.entryListInstance.entries]
                    st.header("Entries")
                    st.write(entryListValues)
                    st.header("Report")
                    if result.lower()=='ggggg':
                        st.header("YOU WON!")
                    else:
                        st.write(director.reportString())

                else:
                    if errorMessage == 'Word already used.':
                        st.write(WordleDisplayHelper.wordAleadyUsedMessage(entry, code.EntryList.entryListInstance))
                    elif errorMessage == 'Too many must have letters.':
                        st.write(WordleDisplayHelper.tooManyMustHaveLettersMessage())
                    else:
                        st.write(WordleDisplayHelper.unhandledErrorMessage(errorMessage, entry))

    else:
        st.header("Report")
        st.write(director.initialReportString())


def display_help(director):
    st.write(WordleDisplayHelper.helpMessage())
    if code.EntryList.entryListInstance.hasEntries():
        entryListValues = [f"{x.word} - {x.pattern}" for x in code.EntryList.entryListInstance.entries]
        st.header("Entries")
        st.write(entryListValues)
        st.header("Report")
        st.write(director.reportString())
    else:
        st.header("Report")
        st.write(director.initialReportString())


if __name__ == '__main__':
    main()
