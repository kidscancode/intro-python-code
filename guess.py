# KidsCanCode - Intro to Programming
# Random number guessing game
import random

secret_number = random.randrange(1, 101)

guess = 0
tries = 0
while guess != secret_number:
    guess = int(input("Guess a number: "))
    tries = tries + 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("You got it!")
        print("Number of tries: ", tries)


