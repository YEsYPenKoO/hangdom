
import random

import string


WORDLIST_FILENAME = 'words.txt'

# 1--------------------------------------

def load_words():
    print('Loading word list from file...')
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    wordlist = line.split()
    print(' ', len(wordlist), 'words loaded.')
    return wordlist

def choose_word(wordlist):
    return random.choice(wordlist)

wordlist = load_words()

def is_word_guessed(ttg_word, letters_guessed):
    return all(elem in letters_guessed for elem in ttg_word)

def get_guessed_word(secret_word, letters_guessed):
    res = []

    for i in secret_word:
        if i in letters_guessed :
            res.append(i)
        else:
            res.append('_ ')

    return ''.join(res)

def get_av_letters(letters_guessed):
    res = ''
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            res += letter
    return res

def check_warning(warning, guesses_left):
    if warning>0:
        warning-=1
        alert=f'You have {warning} warnings left:'
    else:
        guesses_left-=1
        alert='You have no warnings left, therefore you lose one guess:'
    return (warning, guesses_left, alert)

# 2------------------------|


def show_possible_matches(my_word):
    poss_m = []
    for guest in wordlist:
        if match_with_gaps(my_word, guest) == True:
            poss_m.append(guest)
    if len(poss_m) == 0:
        return("Matches can not be found")
    else:
        poss_m1 = " ".join(poss_m)
        return poss_m1


def match_with_gaps(my_word, other_word):
    my_word = [elem for elem in my_word if not elem.isspace()]
    return len(other_word) == len(my_word) and all(
     (my_word.count(char) == other_word.count(char)) for char in my_word if char != '_') and all(
      my_word[i] == other_word[i] or my_word[i] == "_" for i in range(len(my_word)))



# 1(1)--------------------------------


def hints_hangman(secret_word):

    print("I am thinking of a word that is", len(secret_word),"letters long...")

    v = ['a' , 'e' , 'u' , 'i' , 'o']
    guesses_left=6
    warning = 3
    guessed_letters=[]

    while guesses_left>0 and not is_word_guessed(secret_word, guessed_letters):
        rule1=True
        while rule1:
            print('You have',guesses_left, 'guesses left.')

            print('Available letters:',get_av_letters(guessed_letters))
            letter = str(input("Please guess a letter: ")).lower()
            # 0--------------|

            if letter == "*":
                print("Possible matches:",
                      show_possible_matches(get_guessed_word(secret_word, guessed_letters)))

            if letter in set(string.ascii_lowercase) and  len(letter)==1 and letter not in guessed_letters:
                guessed_letters.append(letter)

                # 1-----
                if letter in secret_word:
                    print('Good guess: ', get_guessed_word(secret_word, guessed_letters))
                    print('')
                    rule1 = False

                elif letter not in secret_word:
                    if letter in v:
                        guesses_left-=2
                    elif letter not in v:
                        guesses_left-=1
                    print('Oops! That letter is not in my word:',get_guessed_word(secret_word, guessed_letters))
                    print('')
            elif letter not in set(string.ascii_lowercase) or letter in guessed_letters or len(letter)!=1:
                check=check_warning(warning, guesses_left)\

                # 2-----
                if letter in guessed_letters:
                    warn='You have already guessed that letter.'
                else:
                    warn='It is not a valid letter.'
                guesses_left = check[1]
                warning=check[0]
                print('Oops!', warn, check[2], get_guessed_word(secret_word, guessed_letters))
                print('')

            # 3------
            if guesses_left <= 0 or is_word_guessed(secret_word, guessed_letters)==True:
                break
        if is_word_guessed(secret_word, guessed_letters) == True and guesses_left>0:
            print('Congratulations, you won! Your total score is:', len(set(secret_word))*guesses_left)
            print('')
        elif guesses_left<=0 and is_word_guessed(secret_word, guessed_letters)!=True:
            print('Sorry, you ran out of guesses. The word is: ', secret_word)
            print('')


# 2(1)--------------------------------

def hard_hangman(secret_word):

    print("I am thinking of a word that is", len(secret_word),"letters long...")

    v = ['a' , 'e' , 'u' , 'i' , 'o']
    guesses_left=6
    warning = 3
    guessed_letters=[]

    while guesses_left>0 and not is_word_guessed(secret_word, guessed_letters):
        rule1=True
        while rule1:
            print('You have',guesses_left, 'guesses left.')

            print('Available letters:',get_av_letters(guessed_letters))
            letter=str(input('Please guess a letter: ')).lower()
            if letter == '*':
                show_possible_matches(get_guessed_word(secret_word, guessed_letters))
            if letter in set(string.ascii_lowercase) and len(letter)==1 and letter not in guessed_letters:
                guessed_letters.append(letter)

                # 1-----
                if letter in secret_word:
                    print('Good guess: ',get_guessed_word(secret_word, guessed_letters))
                    print('')
                    rule1=False
                elif letter not in secret_word:
                    if letter in v:
                        guesses_left-=2
                    elif letter not in v:
                        guesses_left-=1
                    print('Oops! That letter is not in my word:',get_guessed_word(secret_word, guessed_letters))
                    print('')
            elif letter not in set(string.ascii_lowercase) or letter in guessed_letters or len(letter)!=1:
                check=check_warning(warning, guesses_left)\

                # 2-----
                if letter in guessed_letters:
                    warn='You have already guessed that letter.'
                else:
                    warn='It is not a valid letter.'
                guesses_left=check[1]
                warning=check[0]
                print('Oops!', warn, check[2], get_guessed_word(secret_word, guessed_letters))
                print('')

            # 3------
            if guesses_left<=0 or is_word_guessed(secret_word, guessed_letters)==True:
                break
        if is_word_guessed(secret_word, guessed_letters) == True and guesses_left>0:
            print('Congratulations, you won! Your total score is:', len(set(secret_word))*guesses_left)
            print('')
        elif guesses_left<=0 and is_word_guessed(secret_word, guessed_letters)!=True:
            print('Sorry, you ran out of guesses. The word is: ', secret_word)
            print('')




if __name__ == "__main__":
    print('you can play a different variation of the game. choose from: ')
    print('1. normal mode hangman (with hints)')
    print('2. hard mode hangman (without hints)')
    secret_word=choose_word(wordlist)
    answer = int(input())
    if answer == 1:
        hints_hangman(secret_word)
    elif answer == 2 :
        hard_hangman(secret_word)
