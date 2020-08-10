"""
Carson Pemble
8/10/2020
Dice Roller

"""
import random

print("\nWelcome to Carson's Dice Roller Program.")

try:
    number_of_dice = int(input("How many dice do you want me to roll?  "))
except ValueError:
    print("The number of dice must be an integer. (Ex: 1 or 3)")
    number_of_dice = int(input("How many dice do you want me to roll?  "))

try:
    number_of_sides = int(input("How many sides should each dice have?  "))
except ValueError:
    print("The number of sides must be an integer. (Ex: 6 or 20)")
    number_of_sides = int(input("How many sides should each dice have?  "))

list_of_rolls = []

for i in range(number_of_dice):
    # print("rolling a dice... ")
    dice_roll = random.randint(1, number_of_sides)
    list_of_rolls.append(dice_roll)

print("\nYour dice rolls were: ", list_of_rolls)

total = 0
for number in list_of_rolls:
    total += number

print("The total of your rolls were: ", total)
