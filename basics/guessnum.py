# ==============GUESS THE NUMBER=================
import random

guesses = 1

print("Guess the number between 0 and 10")
userNum = int(input())

mysNum = random.randint(0, 10 + 1)

while userNum < mysNum:
    print("Too low")
    userNum = int(input("try again \n"))
    guesses = + guesses + 1
    if userNum > mysNum:
        print("too high")
        userNum = int(input("try again \n"))
        guesses = + 1
if userNum == mysNum:
    if guesses < 7:
        print(f"Awesome! you guessed the number in {guesses} guesses")
    if guesses > 7:
        print(f"Wow if took you {guesses} guesses to guess {mysNum}, you must be a dumbshit")
