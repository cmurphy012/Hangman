import random
import string
from words import words


def get_word(words):
    rand_word = random.choice(words)
    while "-" in rand_word or " " in rand_word:
        rand_word = random.choice(words)

    return rand_word.upper()


def hangman():
    word = get_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print("You have", lives, "lives left and yuo have used these letters: ", " ".join(used_letters))

        current_word = [letter if letter in used_letters else "_" for letter in word]
        print("Current word is: ", " ".join(current_word))

        guess = input("Guess a letter: ").upper()
        if guess in alphabet - used_letters:
            used_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
            else:
                lives -= 1
                print("Letter is not in word")

        elif guess in used_letters:
            print("You have already guessed this letter!")

        else:
            print("Invalid character, please try again")

    if lives == 0:
        print("You are out of lives, Game Over!")
    else:
        print("Congrats, you guessed the word! It was:", word)

hangman()
