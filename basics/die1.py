


##====================DICE========================

import random

die = [4, 6, 8, 10, 20]
print(die)

#prompt for die
print("Choose a Dice")
userdie = int(input())


while userdie not in die:
    print("Choose a correct die")
    userdie = int(input())
print()


print("How many times would you like to roll the die?")
roll = int(input())

while roll > 50:
    print("try a smaller number")
    roll = int(input())
print()

for event in range(roll):
    dyRoll= random.randint(0,userdie)
    print(f"You rolled a {dyRoll}")