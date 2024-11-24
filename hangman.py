import random
import time

"""
Hangman Game
Author: Ako Suminoe
License: MIT License"
This project is developed by [AkoSuminoe](https://github.com/AkoSuminoe).
"""

# ASCII art for Hangman stages
hangman_stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

# Simple animation when the player guesses the word correctly
def celebration_animation():
    print("\n* * * Congratulations! * * *")
    time.sleep(0.5)
    print("🥳🥳🥳")
    time.sleep(0.5)
    print("💥💥💥 BOOM! 💥💥💥")
    time.sleep(0.5)
    print("🎉🎉🎉 You won! 🎉🎉🎉")
    time.sleep(0.5)

# Simple animation when the player makes a wrong guess
def wrong_guess_animation():
    print("\nOh no, wrong guess!")
    time.sleep(0.5)
    print("😱💥❌💥😱")
    time.sleep(0.5)
    print("Try again!")
    time.sleep(0.5)

# Function to load words from a file
def load_words():
    try:
        with open("words.txt", "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print("Error: 'words.txt' file not found.")
        return []


# Function to play Hangman game
def hangman_game(word, players):
    guessed_word = ["_"] * len(word)
    wrong_guesses = 0
    max_attempts = len(hangman_stages) - 1
    turn = 0
    print("\nThe word to guess:")
    print(" ".join(guessed_word))

    while wrong_guesses < max_attempts:
        print(hangman_stages[wrong_guesses])
        current_player = players[turn % len(players)]
        print(f"It's {current_player}'s turn!")

        guess = input(f"{current_player}, enter your guess: ").lower()
        if guess in guessed_word:
            print(f"You already guessed {guess}.")
            continue

        if guess in word:
            print(f"Good guess! {guess} is in the word.")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            print(f"Sorry, {guess} is not in the word.")
            wrong_guess_animation()
            wrong_guesses += 1

        print(" ".join(guessed_word))

        # Check if the word is completely guessed
        if "_" not in guessed_word:
            print(hangman_stages[wrong_guesses])
            print(f"Congratulations! {current_player} wins! The word was: {word}")
            return

        if guess == word:
            print(hangman_stages[wrong_guesses])
            celebration_animation()
            print(f"Congratulations! {current_player} wins! The word was: {word}")
            return

        turn += 1

    # Game over if max attempts are reached
    print(hangman_stages[wrong_guesses])
    print(f"Game Over! The word was: {word}")


# Main function to manage game flow
def main():
    while True:
        # Multiplayer question
        multiplayer_question = input("Do you want to play Hangman multiplayer? (yes/no): ").lower()

        if multiplayer_question in ["yes", "y"]:
            # Multiplayer mode
            player_count = int(input("How many players? "))
            player_list = [input(f"Enter player {i + 1} name: ") for i in range(player_count)]
            print(f"Welcome to Hangman multiplayer! Players: {player_list}")

            # Ask for database usage in multiplayer mode
            database_question = input("Do you want to play Hangman with a database? (yes/no): ").lower()
            if database_question in ["yes", "y"]:
                words = load_words()
                if not words:
                    print("No words available in the database.")
                    return
                word = random.choice(words)
                hangman_game(word, player_list)
            elif database_question in ["no", "n"]:
                word = input("Enter the word to guess: ").lower()
                hangman_game(word, player_list)
            break

        elif multiplayer_question in ["no", "n"]:
            # Single-player mode
            database_question = input("Do you want to play Hangman with a database? (yes/no): ").lower()
            if database_question in ["yes", "y"]:
                words = load_words()
                if not words:
                    print("No words available in the database.")
                    return
                word = random.choice(words)
                hangman_game(word, ["Player1"])
            elif database_question in ["no", "n"]:
                word = input("Enter the word to guess: ").lower()
                hangman_game(word, ["Player1"])
            break
        else:
            print("Invalid choice. Please type 'yes' or 'no'.")


if __name__ == "__main__":
    main()
