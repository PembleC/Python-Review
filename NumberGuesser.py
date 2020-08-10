"""
Carson Pemble
8/10/2020
Number Guesser
"""
import random
import time

print("\nWelcome to Carson's Number Guessing Game!")

max_number = int(input("What should be the max number I can pick? "))
computers_number = random.randint(1, max_number)
time.sleep(0.5)
print("Ok, I have a number.")

user_number = int(input("\nWhat is your guess? "))
attempts = 1

while computers_number != user_number:
    if user_number < computers_number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")
    attempts += 1
    user_number = int(input("\nWhat is your guess? "))

print("That's Correct! I was thinking of the number: ", computers_number)
print("It took you", attempts, "tries to guess my number.")

if attempts == 1:
    print("WOW! I bow before your god tier guessing strategy!!!!")

elif attempts <= 3:
    print("Amazing job!!!")

elif attempts <= 5:
    print("Great job!!")

elif attempts <= 10:
    print("Good job!")
