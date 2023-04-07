import random

class Hangman:
    def __init__(self, words):
        self.words = words
        self.word = random.choice(words)
        self.guesses = []
        self.max_attempts = 6
        self.attempts = 0
        self.hangman = ['''
            _______
           |       |
                   |
                   |
                   |
                   |
          =========''', '''
            _______
           |       |
           O       |
                   |
                   |
                   |
          =========''', '''
            _______
           |       |
           O       |
           |       |
                   |
                   |
          =========''', '''
            _______
           |       |
           O       |
          /|       |
                   |
                   |
          =========''', '''
            _______
           |       |
           O       |
          /|\      |
                   |
                   |
          =========''', '''
            _______
           |       |
           O       |
          /|\      |
          /        |
                   |
          =========''', '''
            _______
           |       |
           O       |
          /|\      |
          / \      |
                   |
          =========''']

    def show_hangman(self):
        print(self.hangman[self.attempts])

    def play(self):
        while True:
            # Display the current state of the hangman figure
            self.show_hangman()

            # Display the progress of the word
            progress = ""
            for letter in self.word:
                if letter in self.guesses:
                    progress += letter
                else:
                    progress += "_"
            print(progress)

            # Ask the user to guess a letter
            guess = input("Guess a letter: ")

            # Check if the guessed letter is in the word
            if guess in self.word:
                self.guesses.append(guess)
                if set(self.word) == set(self.guesses):
                    print(f"Congratulations! You guessed the word '{self.word}'")
                    break
            else:
                print(f"Sorry, the letter '{guess}' is not in the word.")
                self.attempts += 1

                # Check if the user has run out of attempts
                if self.attempts == self.max_attempts:
                    self.show_hangman()
                    print(f"Game over. The word was '{self.word}'.")
                    break


# Define the words for the game
words = ["apple", "banana", "orange", "jackfruit", "grape", "mango"]

# Create a Hangman object and play the game
hangman = Hangman(words)
hangman.play()