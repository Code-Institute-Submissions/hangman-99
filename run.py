"""
Used for libraries and imports
"""
import random  # Randomly selects a word for the game
import os  # Used to clear screen
import pyfiglet  # import pyfiglet module for ascii art
import colorama  # Adds color to game text
from colorama import Fore, Style
from lives import lives_left  # Hangman lives visual from lives.py

colorama.init(autoreset=True)


def game_intro():
    '''
    Game welcome and request users name and prints Hello name
    '''
    title = pyfiglet.figlet_format(
        "Lets play", font="standard", justify="center"
        )
    title2 = pyfiglet.figlet_format(
        "Hangman", font="standard", justify="center"
        )
    print(Fore.BLUE+Style.BRIGHT + title)
    print(Fore.MAGENTA+Style.BRIGHT + title2)
    print("HELLO Player")
    name = " "
    while True:
        name = input("Please enter your name: \n")

        if name.isalpha() is not True:
            print(f'{Fore.RED+Style.BRIGHT}Error: Your name must'
                  'be alphabetic only.\n')
        else:
            print("\n")
            print(f'{Fore.MAGENTA+Style.BRIGHT}Hello {name}!')
            return name


def start_game():
    '''
    Starts the game with options:
    1 to play - default level easy
    2 to select level of play
    3 to see the game rules
    '''
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
    difficulty = False
    while not difficulty:
        options = input("\n ").lower()
        if options == "e":
            difficulty = True
            num_lives = 10
            return num_lives

        elif options == "n":
            difficulty = True
            num_lives = 7
            return num_lives

        elif options == "h":
            difficulty = True
            num_lives = 5
            return num_lives
        else:
            print("\n Please choose E, N or H to select your level")


def get_random_word():
    """
    Picks a random word from words.txt
    """
    random_word = random.choice(open("words.txt", "r").read().split('\n'))
    return random_word.lower()


def game_rules():
    """
    Explains to the User how to play the game
    """
    print(
        """
    Welcome to countries of the world hangman game
    This is a guess the word game

    THE RULES

    Guess the word by inputting letters
    If you guess the wrong letter, you lose a life
    Your hangman will then start to build
    When you reach 0 lives your will be HANGED

    Good luck
    """
    )
    input(Fore.BLUE+Style.BRIGHT + " Press press enter to go"
          " back to the main menu\n ")
    print("\n")
    start_game()


def hangman_lives(lives):
    """
    Displays Hangman visuals
    """
    for _ in lives_left:
        return lives_left[lives]


def play_game(word, num_lives):
    """
    Runs the game and starts all the gameplay logic.
    """
    word_to_guess = '_' * len(word)
    game_over = False
    guesses = []
    lives = num_lives
    print(f'\nLives: {lives}\n')
    print('What country are you looking for? '+' '.join(word_to_guess) + '\n')

    while not game_over and lives > 0:
        user_guess = input("Please guess a letter:\n ").lower()
        try:
            if len(user_guess) > 1:
                raise ValueError(f"{Fore.RED+Style.BRIGHT}"
                                 f"You can only guess 1 letter at a time. "
                                 f"You guessed {len(user_guess)}")
            elif not user_guess.isalpha():
                raise ValueError(f"{Fore.RED+Style.BRIGHT}"
                                 f"You can only guess letters."
                                 f"You guessed {user_guess},is not a letter.")
            elif len(user_guess) == 1 and user_guess.isalpha():
                if user_guess in guesses:
                    raise ValueError(f"{Fore.RED+Style.BRIGHT}"
                                     f"You have already guessed {user_guess}.")
                elif user_guess not in word:
                    print(f"{Fore.RED+Style.BRIGHT}"
                          f"{(user_guess)} is not in the word.")
                    print(f"{Fore.RED+Style.BRIGHT} You Lose a Life!")
                    guesses.append(user_guess)
                    lives -= 1
                else:
                    print(f"{Fore.GREEN+Style.BRIGHT}"
                          f"{user_guess} is a part of the word")

                    guesses.append(user_guess)
                    word_to_guess_list = list(word_to_guess)
                    indices = [i for i, letter in enumerate(word)
                               if letter == user_guess]
                    for index in indices:
                        word_to_guess_list[index] = user_guess
                        word_to_guess = "".join(word_to_guess_list)
                    if "_" not in word_to_guess:
                        game_over = True

        except ValueError as input_error:
            print(f'{input_error}\n Please try again.\n')
            continue

        print(hangman_lives(lives))

        if lives > 0:
            print(f"Lives: {lives}\n")
            print("The country to guess: " + " ".join(word_to_guess) + "\n")
            print(" Letters guessed: " + ", ".join(sorted(guesses)) + "\n")

    if game_over:
        print(f'Well done! You guessed the word: {word}')
        win_game()
    else:
        print('You have no lives left.')
        print(f'The word you were looking for was: {word}')
        game_end()

    restart_game(num_lives)


def game_end():
    """
    Graphic for game over display
    """
    end = pyfiglet.figlet_format('"Game Over",'
                                 'font="standard", justify="center"')
    print(Fore.RED+Style.BRIGHT + end)


def win_game():
    """
    Graphic for win game display
    """
    win = pyfiglet.figlet_format("YOU WIN", font="standard", justify="center")
    print(Fore.GREEN+Style.BRIGHT + win)


def restart_game(num_lives):
    """
    Gives the user the option to restart the game or return to main screen
    """
    game_restart = False

    while not game_restart:
        restart = input(f"{Fore.GREEN+Style.BRIGHT}"
                        f"\nWould you like yo play again"
                        f"\nPlease type y for Yes & n for No: ").lower()
        try:
            if restart == "y":
                game_restart = True
                hangman_game = get_random_word()
                play_game(hangman_game, num_lives)
            elif restart == "n":
                game_restart = True
                print("\n")
                main()
            else:
                raise ValueError(f"{Fore.RED+Style.BRIGHT}"
                                 f"Please type either y or n,"
                                 f"to make your choice. You typed{(restart)}")

        except ValueError as e_values:
            print(f"{e_values}.\n{Fore.RED+Style.BRIGHT}"
                  f"Please try again\n")


def clear_screen():
    """
    Used to clear Terminal screen
    """
    os.system("clear")


def main():
    """
    Runs functions used for the Game
    """
    game_intro()
    difficulty = start_game()
    if difficulty == "default":
        num_lives = 10
    else:
        num_lives = select_game_level()
    word = get_random_word()
    play_game(word, num_lives)


if __name__ == "__main__":
    main()
