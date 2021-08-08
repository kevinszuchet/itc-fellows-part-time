import random

welcome_message = """
     |/|
     |/|
     |/|
     |/|
     |/|
     |/|
     |/| /¯)
     |/|/\/
     |/|\/
    (¯¯¯)
    (¯¯¯)
    (¯¯¯)
    (¯¯¯)
    (¯¯¯)
    /¯¯/\
   / ,^./\
  / /   \/\
 / /     \/\
( (       )/)
| |       |/|
| |       |/|
| |       |/|
( (       )/)
 \ \     / /
  \ `---' /
   `-----'    
"""


def ask_for_guess():
    question = "What is your guess? "
    guess = input(question)
    while not guess or not guess.isalpha() or len(guess) > 1 or not len(guess):
        guess = input(f"Please enter a valid guess. {question}")
    return guess.lower()


def main():
    print(welcome_message)
    word = random.choice(words)
    word_guessed = ['*'] * len(word)
    attempts = 10
    guesses = []
    while attempts > 0 and '*' in word_guessed:
        print(f"You have {attempts} guesses")
        print(f"The word is: {''.join(word_guessed)}")
        guess = ask_for_guess()
        if guess in guesses:
            print(f"You've already entered the letter {guess}. Try with another one...")
            continue
        guesses.append(guess)
        if guess.lower() not in word.lower():
            attempts -= 1
            if not attempts:
                print("That was your last attempt. I hope you'll do better next time...")
                print(f"The word was: {word}")
                return
            print("Wrong choice buddy, try again!")
            continue

        for i, letter in enumerate(word):
            if letter.lower() == guess.lower():
                word_guessed[i] = letter

    print("Well done! You are a hangman ninja. Enjoy your reward (?")


with open('files/hangman_words.txt') as words_file:
    words = words_file.read().splitlines()

main()
