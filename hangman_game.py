# Hangman Game Project - Maria Jose

# import libraries
import random

# initialize variables
guess_count = 0
guess_letters = []
current_word = []
random_word = []
word_list = []
letter = ""

# datasets
list_easy = ["mood", "love", "wood", "beer", "year", "loss", "user", "road", "desk", "cell",
             "girl", "debt", "role", "lake", "food", "wife", "bird", "gate", "exam", "disk"]
list_medium = ["shiver", "modest", "flight", "import", "murder", "retain", "strong", "global",
               "method", "normal", "bottom", "heaven", "hunter", "resign", "stress", "immune",
               "dealer", "velvet", "assume", "census"]
list_hard = ["strategy", "currency", "judgment", "relation", "guidance", "customer", "category",
             "addition", "quantity", "platform", "resource", "software", "database", "activity",
             "delivery", "stranger", "property", "response", "audience", "employer"]

# function to select the level
def select_level():
    global word_list, guess_count
    # select level menu
    print("Please select the level you want to play:")
    print("1. Easy      ( word lenght = 4, attempts = 8 )")
    print("2. Medium    ( word lenght = 6, attempts = 7 )")
    print("3. Hard      ( word lenght = 8, attempts = 6 )")
    # loop for valid input
    while True:
        level = input(f"Enter the level: ").strip().lower()  # remove extra spaces and lowercase
        if level.isnumeric() and level in "123":    # validate if letter is character
            if level == "1":                        # level easy
                word_list = list_easy
                guess_count = 8
                print("You selected the Easy level. Good luck!\n")
                break
            if level == "2":                        # level medium
                word_list = list_medium
                guess_count = 7
                print("You selected the Medium level. Good luck!\n")
                break
            if level == "3":                        # level hard
                word_list = list_hard
                guess_count = 6
                print("You selected the Hard level. Good luck!\n")
                break
        else:                                       # validate wrong inputs
            print("Invalid level. Try again.")
            continue
    return level, word_list, guess_count

# function to generate the word
def generate_word():
    global random_word, current_word
    random_word = random.choice(word_list)      # generate a random word from the list
    random_word = list(random_word)             # random word to list
    current_word = ["_"] * len(random_word)     # initialize current empty
    return random_word, current_word

# function to print messages
def print_current():
    global random_word, current_word, guess_letters, guess_count
    # messages to be printed
    print("Current word: " + " ".join(current_word))                # current word list as string
    print("Guessed letters/words: " + ", ".join(guess_letters))     # guess letters list as string
    print(f"Incorrect guesses remaining: {guess_count}")
    return current_word

# function to verify input as string o entire word
def verify_input():
    while True:                                 # verify if input is letter
        letter = input(f"Guess a letter (a-z): ").strip().lower()      # remove extra spaces and lowercase
        if letter.isalpha():                    # validate if letter is character
            if not letter in guess_letters and len(letter) == 1: # letter not used before
                break
            elif len(letter) > 1:               # validate wrong length
                print("Error. Enter only one character.")
            else:                               # validate duplicates
                print(f"The letter '{letter}' was already used.")
                continue
        else:                                   # validate wrong inputs
            print("Error. Enter a valid letter.")
            continue
    return letter

# function to guess the word
def guess_word(l):
    global guess_letters, random_word, guess_count
    # for verifying if letter is contained into the word
    for i in range(len(random_word)):
        if random_word[i] == l:
            current_word[i] = l                 # replaces the letter if matching
    # to print guess messages
    if l in random_word:
        print(f"Good job! '{l}' is in the word.\n")
    else:
        print(f"Sorry, '{l}' is not in the word.\n")
        guess_count -= 1
    # append the letter to the guess letters list
    guess_letters.append(l)
    return guess_count

# main function
def main():
    global random_word, current_word, letter, guess_count
    print("Welcome to Hangman!\n")
    select_level()          # select the level function
    generate_word()         # initial generate word function
    while True:
        print_current()       # print current function
        letter = verify_input()     # user letter input function
        guess_word(letter)          # guess the word function

        # loop to finish or continue the game
        if "".join(random_word) == "".join(current_word):       # compare if matches as strings (not list)
            print(f"Congratulations! You guessed the word: '" + "".join(random_word) + "'.")
            break
        elif guess_count == 0:                                  # end game if attempts reached 0
            print(f"Game over! The word was: '" + "".join(random_word) + "'.")
            break

main()
