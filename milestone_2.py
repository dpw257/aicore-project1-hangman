import random

word_list = ['pear', 'banana', 'cherry', 'apple', 'plum']

word = random.choice(word_list)

guess = input("enter a single letter: ")

if len(guess) == 1 and guess.isalpha():
    print("Nice guess")
else:
    print("Oops! That is not a valid input.")




