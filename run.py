import random

import colorama
from colorama import Fore, Style
from lives import lives_left

colorama.init(autoreset=True)


def game_intro():
    '''
    Game welcome and request users name and prints Hello name
    '''
    print(
        """
        ██      ███████ ████████ ███████     ██████  ██       █████  ██    ██
        ██      ██         ██    ██          ██   ██ ██      ██   ██  ██  ██
        ██      █████      ██    ███████     ██████  ██      ███████   ████
        ██      ██         ██         ██     ██      ██      ██   ██    ██
        ███████ ███████    ██    ███████     ██      ███████ ██   ██    ██

        ██   ██  █████  ███    ██  ██████  ███    ███  █████  ███    ██
        ██   ██ ██   ██ ████   ██ ██       ████  ████ ██   ██ ████   ██
        ███████ ███████ ██ ██  ██ ██   ███ ██ ████ ██ ███████ ██ ██  ██
        ██   ██ ██   ██ ██  ██ ██ ██    ██ ██  ██  ██ ██   ██ ██  ██ ██
        ██   ██ ██   ██ ██   ████  ██████  ██      ██ ██   ██ ██   ████
        """
    )
    print("Welcome")
    name = " "
    while True:
        name = input("Please enter your name: \n")

        if name.isalpha() is not True:
            print("Error: Your name must be alphabetic only.\n")
        else:
            print(f'{Fore.YELLOW+Style.BRIGHT}Hello {name}!')
            return name

def start_game():

    print("Press 1 to Start playing game")
    print("Press 2 to Choose the level to play at")
    print("Press 3 to Read the rules")
    options = False
    while not options:
        settings = input("\n ")
        if settings == "1":
            options = True
            difficulty = "default"
            return difficulty

        elif settings == "2":
            options = True
            select_game_level()

        elif settings == "3":
            options = True
            game_rules()

        else:
            print(" Please select 1, 2 or 3 to make your choice")

def select_game_level():
    """
    Function to select level
    """
    print("Please select a level\n")
    print("Press e for Easy")
    print("Press n for Normal")
    print("Press h for Hard")
    level = False

    while not level:
        options = input("\n ").lower()
        if options == "e":
            level = True
            level_lives = 10
            return level_lives

        elif options == "n":
            level = True
            level_lives = 7
            return level_lives

        elif options == "h":
            level = True
            level_lives = 5
            return level_lives

        else:
            print("\n Please choose E, N or H to select your level")


def get_random_word():
    """
    Picks a random word from words.txt
    """
    random_word = random.choice(open("words.txt", "r").read().split('\n'))
    return random_word.upper()

def game_rules():
    """
    Explains to the User how to play the game
    """
    print("Welcome to World Countires Hangman rules")
    print("This is a guess the word game")
    print("Guess the word by inputting letters")
    print("If you guess the wrong letter you loose a life")
    print("Your Hang-Hangman will then start to build")
    print("When you reach 0 lives your will be HANGED!")
    print("Good luck")
    print("Press enter to return to the main menu")


def hangman_lives(lives):
    """
    Displays Hangman visuals
    """
    for _ in lives_left:
        return lives_left[lives]

def main():
    """
    Runs functions used for the Game
    """
    game_intro()
    start_game()

main()
