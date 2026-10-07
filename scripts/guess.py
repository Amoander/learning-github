# Number guessing game
import random

secret = random.randint(1, 10)
guess = 0
guesses = 0

print("I'm thinking of a number between 1 and 10.")

while guess != secret:
    guess = int(input("Your guess: "))
    guesses = guesses + 1

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")

print("You got it in", guesses, "guesses!")