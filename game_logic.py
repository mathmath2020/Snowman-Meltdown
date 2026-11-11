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


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = input("Guess a letter: ").lower().strip()

        # Validate single alphabetical character
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.\n")
            continue

        # Prevent penalizing repeated guesses
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try another letter.\n")
            continue

        # Update guessed letters and evaluate guess
        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            mistakes += 1
            print(f"Sorry, '{guess}' is not in the word.")

        # Check win condition
        if all(letter in guessed_letters for letter in secret_word):
            display_game_state(mistakes, secret_word, guessed_letters)
            print("Congratulations, you saved the snowman!")
            return

    # Loss condition when max_mistakes is reached
    display_game_state(mistakes, secret_word, guessed_letters)
    print(f"Game Over! The snowman melted. The secret word was '{secret_word}'.")
