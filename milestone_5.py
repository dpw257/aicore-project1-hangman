import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for i in range(len(self.word))]
        self.num_lives = num_lives
        self.num_letters = len(self.word)
        self.list_of_guesses = ['_']

    def check_guess(self, guess):
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i in range(len(self.word)):
                if guess == self.word[i]:
                    self.word_guessed[i] = guess
                    print(self.word_guessed)
                    self.num_letters -= 1
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left.")
            

            
    def ask_for_input(self):
        guess = input("Enter a single letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid letter. Please enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess)
            print(f"{self.num_letters} letters left to guess.")


word_list = ['pear', 'banana', 'cherry', 'apple', 'plum']

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            print(f"The word was {game.word}")
            break
        elif game.num_letters == 0:
            print(f"YOU WIN! The word was {game.word}.")
            break
        elif game.num_letters > 0:
            game.ask_for_input()

play_game(word_list)






