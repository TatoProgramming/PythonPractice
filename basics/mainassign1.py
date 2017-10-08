#
# # ===============Tato Assign 1=========================
# ##current time based on system
# import datetime
# # generate random int
# import random
#
# print("Name please", end=' ')
# name = input()
#
# print(f"Greetings {name}, what year were you born?", end=' ')
# year = float(input())
#
#
# now = datetime.datetime.now()
# curYear = now.year
#
# ##cannot add str so muct cast into ints
#
# age = curYear - year
#
# print(f"O so that means you are {age} years old")
#
# dogOp = 1 / 8
# dogYear = age * dogOp
#
# print(f"If you are {age} then that means you are {dogYear} years old in dog years")
#
# autoYear = curYear - 1885
# interYear = curYear - 1983
# choYear = curYear - 1954
#
# print(f"Do you realize that is has been {autoYear} since automobiles were invented")
# print(f"It has been {interYear} since the internet came to be")
# print(f"And {choYear} years since M&M's")
#
# deathAge = age + random.randint(1, 100)
# deathYear = int(float(year) + deathAge)
#
# print(f"Your deathklok says you will die when you are {deathAge} in the year {deathYear} ")
#
#
#
# #=========================================automate practice 1=======================


## if, elif, else pract
## will stop on true statement

# name = "Garrus"
# bad = 1000
# if name == "Tali":
#     print("Good girl Tali")
# elif bad < 9:
#     print("You must still be a good dog")
# elif bad <= 100:
#     print("Naughty puppy")
# else:
#     print("You must be bad puppy Garrus")
#     print("Good girl Tali")

# ======================while loops!====================
##while break (not that great)

# while True:
#     print("Is Garrus a good dog")
#     dog = input()
#     if dog == "yes":
#         print("good boy")
#         break
#     elif dog == "no":
#         print("bad dog")
#         break
#

# while True:
#     print("Is Tali a good girl?")
#     dog=input()
#     if dog !="yes":
#         continue
#     print("she is. Is garrus?")
#     pup =input()
#     if pup == "no":
#         print("he is a boy")
#         break

# ===================for loops==============

##execute block specific amount of times

# print("what is your name?")
# name=input()
# for i in range (7):
#   print(f"hello {name}")
#
#
#
# total = 0
# for num in range(101):
#     total = total + num
# print(total)

#
# for i in range(0,49,7):
#     print(i)
#
# #counting down
#
# for i in range(100,0,-5):
#     print(i)


##MULTIPLICATION TABLE
# print("times table")
# print("number plz")
# num = int(input())
#
# print("choose another")
# other= int(input())
#
# for i in range(1, 1 + num):     #1 + includes the input
#     for x in range(1, 1+other): #other number horizontal in table
#         print(i * x, end=" ")   #create times table,insert space
#     print()                     #creates new line after 1st loop


### the x diamond pattern
#
# print("choose a number:")
# put= int(input())

put = 5
# for i in range(0,1+put):
#     for y in range((i*2)+1):
#         print("X", end=" ")
#     for z in range(i-1, put):
#         print("x", end=" ")
# #     print()
#
# for i in range(put):
#     for x in range(put-i):      #acending leading spaces
#         print(" " , end="")
#     for q in range(put):
#         print("x", end="")
#     print()
# for l in range(put, 2, 1):
#     print("x", end=" ")


#
#

# =================importing==================

#
# import random
#
# for i in range(0, 27, 3):
#     print(random.randint(1, 27))
#
# import random, sys, os, math

# import sys
#
# while True:
#     print("Type exit to exit")
#     response = input()
#     if response == "exit":
#         sys.exit()
#     print(f"You typed {response}.")

# spam = 0
# if spam == 1:
#     print("hello")
# elif spam < 2:
#     print("greetings")
# else:
#     print("Howdy")
#
#
# for num in range(0,10,1):
#     print(num)
# #
# i=0
# while i <= 10:
#     print(i)
# #     i=i+1
#
#
# ##====================DICE========================
#
# import random
#
# die = [4, 6, 8, 10, 20]
# print(die)
#
# #prompt for die
# print("Choose a Dice")
# userdie = int(input())
#
#
# while userdie not in die:
#     print("Choose a correct die")
#     userdie = int(input())
# print()
#
#
# print("How many times would you like to roll the die?")
# roll = int(input())
#
# while roll > 50:
#     print("try a smaller number")
#     roll = int(input())
# print()
#
# for event in range(roll):
#     dyRoll= random.randint(0,userdie)
#     print(f"You rolled a {dyRoll}")



# for userdie in die:
#     if userdie == 4:
#         for userdie in range(roll):
#             die4 = random.randint(1, 4)
#             print(f"The die rolls a {die4}")
#     if userdie == 6:
#         for userdie in range(roll):
#             die6 = random.randint(1, 6)
#             print(f"The die rolls a {die6}")
#     if userdie == 8:
#         for userdie in range(roll):
#             die8 = random.randint(1, 8)
#             print(f"The die rolls a {die8}")
#     if userdie == 10:
#         for userdie in range(roll):
#             die10 = random.randint(1, 10)
#             print(f"The die rolls a {die10}")
#     if userdie == 20:
#         for userdie in range(roll):
#             die20 = random.randint(1, 20)
#             print(f"The die rolls a {die20}")
#




#
#
#
# while userdie != die:
#     print("Try again")
#     userdie = int(input())
# print(f"You chose to roll a {userdie} die")
#
# print("How many times would you like to roll the die?")
# roll = int(input())
#
# while roll > 50:
#     print("try a smaller number")
#     roll = int(input())
# print()
#
# if userdie == die:
#     for userdie in range(roll):
#         die4 = random.randint(1, 4)
#         print(f"The die rolls a {die4}")






# while True:
#     if userdie!=die:
#         print("Try again")
#         userdie=input()
# print(f"You chose {userdie}")
# if userdie==die:
#         print("OK")










# while userdie != die:
#     print("Try again")
#     userdie = input()
#     if userdie==die:
#         print("Awesome")
# print("ok")
#
#


# ================FUNCTIONS==========#
