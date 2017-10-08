
# ===============Tato Assign 1=========================
##current time based on system
import datetime
# generate random int
import random

print("Name please", end=' ')
name = input()

print(f"Greetings {name}, what year were you born?", end=' ')
year = float(input())


now = datetime.datetime.now()
curYear = now.year

##cannot add str so muct cast into ints

age = curYear - year

print(f"O so that means you are {age} years old")

dogOp = 1 / 8
dogYear = age * dogOp

print(f"If you are {age} then that means you are {dogYear} years old in dog years")

autoYear = curYear - 1885
interYear = curYear - 1983
choYear = curYear - 1954

print(f"Do you realize that is has been {autoYear} since automobiles were invented")
print(f"It has been {interYear} since the internet came to be")
print(f"And {choYear} years since M&M's")

deathAge = age + random.randint(1, 100)
deathYear = int(float(year) + deathAge)

print(f"Your deathklok says you will die when you are {deathAge} in the year {deathYear} ")
