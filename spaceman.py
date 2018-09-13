import random
import signal
import time
# import only system from os
from os import system, name

# define our clear function
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    secret_word = random.choice(words_list).rstrip()
    return secret_word


incorrect_guesses = 0
secret_word = load_word()
word = []
guessed_letters = []


# Creates empty spaces for secret_word
def create_guessed_word(secret_word):
    for i in secret_word:
        word.append("_")

# add letter to guessed letter list
def update_guessed_letters(letter):
    if letter not in guessed_letters:
        guessed_letters.append(letter)

# Check if letter is in secret_word
def check_guess(letter):
    global incorrect_guesses
    if letter.isalpha() and len(letter) == 1:
        if letter in secret_word:
            find_letter_position(letter)
            update_guessed_letters(letter)
        else:
            incorrect_guesses += 1
            update_guessed_letters(letter)
    else:
        print("Not a valid letter ")

# Find the position of letter in secret_word
def find_letter_position(letter):
    for i, item in enumerate(secret_word):
        if item == letter:
            add_letters(letter, i)

# replaces _ with correctly guessed letter
def add_letters(letter, position):
    #will add correct letter to empty slots
    word[position] = letter

# Print progress of game
def print_progress():
    print(' '.join(word))
    print("Guessed Letters: " + ' '.join(guessed_letters) + " | Incorrect Guesses: " + str(incorrect_guesses))
    print("")


guessed_word = create_guessed_word(secret_word)

while True:
    try:
        clear()
        print_progress()
        check_guess(input("Guess a Letter "))

        if "_" not in word:
            clear()
            print_progress()
            print("You win! The word was " + secret_word)
            break
        elif incorrect_guesses == 7:
            print("You lose! The word was " + secret_word)
            break
    except EOFError:
        # Can't EOFError now!
        print("""
        Traceback (most recent call last):
        File "spaceman.py", line 81, in <module>
        check_guess(input("Guess a Letter "))
        EOFError
        """)
        time.sleep(2)
        print("Just kidding")
        time.sleep(1)
