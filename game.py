import random
from tkinter import *

import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.") # IT'S OVER 9000!
    return wordlist

def choose_word(wordlist):
    return random.choice(wordlist)

wordlist = load_words()



