import random

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

def play_hangman():
    words = ["python", "hangman", "computer", "keyboard", "program"]
    word = random.choice(words)
    guessed_letters = []
    attempts = 7
    

    print("=== HANGMAN GAME ===")

    while attempts > 0:
        print("\nWord: " + display_word(word, guessed_letters))
        print(f"Attempts left: {attempts}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter!")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")
        else:
            attempts -= 1
            print("Wrong guess!")

        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You guessed the word correctly: {word}")
            break
    else:
        print(f"\nGame Over! The word was: {word}")

if __name__ == "__main__":
    play_hangman()