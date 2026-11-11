import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the current snowman stage and the secret word with underscores."""
    print(STAGES[mistakes])

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word: " + display_word.strip())
    print("Guessed letters:", ", ".join(sorted(guessed_letters)))
    print()


def get_valid_guess(guessed_letters):
    """Prompts the user until a single, unguessed alphabetical character is entered."""
    while True:
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single alphabetical letter (A-Z).\n")
        elif guess in guessed_letters:
            print(f"You already guessed '{guess}'. Please choose a different letter.\n")
        else:
            return guess


def play_game():
    """Runs a single round of Snowman Meltdown."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("\nWelcome to Snowman Meltdown!")

    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = get_valid_guess(guessed_letters)

        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            mistakes += 1
            print(f"Sorry, '{guess}' is not in the word.")

        if all(letter in guessed_letters for letter in secret_word):
            display_game_state(mistakes, secret_word, guessed_letters)
            print("Congratulations, you saved the snowman!")
            return

    display_game_state(mistakes, secret_word, guessed_letters)
    print(f"Game Over! The snowman melted. The secret word was '{secret_word}'.")


def start_game():
    """Manages the replay loop so the user can play multiple rounds."""
    while True:
        play_game()

        while True:
            replay = input("\nDo you want to play again? (y/n): ").lower().strip()
            if replay in ("y", "yes"):
                break
            elif replay in ("n", "no"):
                print("Thanks for playing Snowman Meltdown! Goodbye!")
                return
            else:
                print("Please enter 'y' for yes or 'n' for no.")
