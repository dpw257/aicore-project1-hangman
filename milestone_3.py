import random

word_list = ['pear', 'banana', 'cherry', 'apple', 'plum']

word = random.choice(word_list)

def check_guess(guess):
    if len(guess) == 1 and guess.isalpha():
        if guess in word:
            print(f"Good guess! {guess} is in the word.")
            return guess
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
    else:
        print("Invalid letter. Please enter a single alphabetical character.")

def ask_for_input():
    guess = input("Enter a single letter: ")
    return guess.lower()

letters = ""
while True:
    guess = ask_for_input()
    check_guess(guess)
    answer = ""
    letters += guess
    for w in word:
        if w in letters:
            answer += w
        else:
            answer += "_"
    print(answer)
    if answer == word:
        print("YOU WIN!")
        break
        
    




