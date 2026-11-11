import random

# Snowman ASCII Art stages
STAGES = [
    # Stage 0: Full snowman
    """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
     """,
    # Stage 1: Bottom part starts melting
    """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     """,
    # Stage 2: Only the head remains
    """
      ___  
     /___\\ 
     (o o) 
     """,
    # Stage 3: Snowman completely melted
    """
      ___  
     /___\\ 
     """
]

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
    print()


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    while mistakes < len(STAGES) - 1:
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = input("Guess a letter: ").lower()
        print("You guessed:", guess)

        if guess not in guessed_letters:
            guessed_letters.append(guess)
        if guess not in secret_word:
            mistakes += 1

        # Check if all letters in secret_word have been guessed
        if all(letter in guessed_letters for letter in secret_word):
            display_game_state(mistakes, secret_word, guessed_letters)
            print("Congratulations, you saved the snowman!")
            return

    # If the loop finishes because mistakes reached the max stage
    display_game_state(mistakes, secret_word, guessed_letters)
    print("Game over! The snowman melted. The word was:", secret_word)


if __name__ == "__main__":
    play_game()