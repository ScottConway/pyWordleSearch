import argparse

import streamlit as st

import code.EntryList

from code.Entry import Entry
from code.WordListDirector import WordListDirector
from code.WordleDisplayHelper import WordleDisplayHelper
from code.EntryList import EntryList


def main():
    parser = argparse.ArgumentParser(
        description='Helper program for wordle game.')
    parser.add_argument('--version', action='version', version='%(prog)s 3.0.3')
    director = WordListDirector()

    if code.EntryList.entryListInstance is None:
        code.EntryList.entryListInstance = EntryList()

    finished = False

    st.write("Input word and pattern ie atone-xxyyg")
    testWord = st.text_input(label='Input word and pattern ie atone-xxyyg', key='inputResult', max_chars=11,
                           help='Input word and pattern ie atone-xxyyg')

    if testWord:
        result = testWord[-5:]
        testWord = testWord[0:5]
        entry = Entry(testWord, result)

        isValid, errorMessage = code.EntryList.entryListInstance.validateEntry(entry)
        if isValid:
            code.EntryList.entryListInstance.add(entry)
            director.applyEntry(entry)
            entryListValues = [f"{x.word} - {x.pattern}" for x in code.EntryList.entryListInstance.entries]
            st.write("Entries")
            st.write(entryListValues)
            st.write("Report")
            st.write(director.reportString())

        else:
            if errorMessage == 'Word already used.':
                WordleDisplayHelper.printWordAlreadyUsed(entry, code.EntryList.entryListInstance)
            elif errorMessage == 'Too many must have letters.':
                WordleDisplayHelper.printTooManyMustHaveLetters(code.EntryList.entryListInstance)
            else:
                WordleDisplayHelper.printUnhandledError(errorMessage, entry, code.EntryList.entryListInstance)
    else:
        st.write("Report")
        st.write(director.initialReportString())




if __name__ == '__main__':
    main()