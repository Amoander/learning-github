# Number guessing game, with error handling
import random

secret = random.randint(1, 10)
guess = 0
guesses = 0

print("I'm thinking of a number between 1 and 10.")

while guess != secret:
    try:
        guess = int(input("Your guess: "))
    except ValueError:
        print("Please enter a whole number, like 7")
        continue

    if guess < 1 or guess > 10:
        print("Stay between 1 and 10!")
        continue

    guesses = guesses + 1

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")

print("You got it in", guesses, "guesses!")