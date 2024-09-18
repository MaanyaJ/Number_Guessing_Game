#Number guessing game

import random

random_number = random.randint(1, 100)
attempts = 0

print("."*50)
print("HELLO!!!")
print("Welcome to the Number Guessing Game!")
print("Rules of the game are simple!")
print("I'm thinking of a number from 1 to 100.")
print("You have to take a guess of it")
print("Once you guess the number, the game will end!")
print("Let's get started!")
print("."*50)

while True:
    print("\n")
    guess = int(input("Take a guess: "))
    attempts += 1

    if guess < random_number:
            print("OOPS! Wrong guess!(Think of a higher number)")
    elif guess > random_number:
            print("OOPS! Wrong guess!(Think of a lower number)")
    else:
       print("\n")
       print("."*65)
       print(f"Yaayyy! Congratulations! You guessed the number in {attempts} attempts.")
       print("I hope you had fun playing this game!")
       print("Bye! Have a nice day :)")
       print("."*65)
       break

