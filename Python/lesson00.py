# Automatic Dice Roller
# Written by Jadam

from random import randint
print ("Automatic Dice Roller")

min = 1
max = 6

roll_again = ""
while roll_again == "":
    print ("Rollin the die")
    print ("You Rolled...",randint(min,max))
    roll_again = input("Roll them doggos again?")
    if ("x") in roll_again.lower():
        roll_again = False

