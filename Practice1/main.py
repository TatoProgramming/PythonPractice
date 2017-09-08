# --------- Exercise 1: printing ---------
#
# print("Hello World!")
# print("Hello Again")
# print("I like typing this.")
# print("This is fun.")
# print('Yay! Printing.')
# print("I'd much rather you 'not'.")
# print('I "said" do not touch this.')
# print("Taylor Tali Garrus")
#
# print('I said "Hello World".')

# ---------- Exercise 2: ----------

#  A comment, this is so you can read your program later
#  Anything after the # is ignored by python
#
# print("I could have code like this.") # and the comment is ignored
#
#  You can also use a comment to "disable" or comment out code:
# print("This won't run.")

# print("This will run.")

# ========= Exercise 3 ===========
# ----operators
# print("I will now count my chickens:")
#
# print("Hens", 25 + 30 / 6)
# print("Roosters", 100 - 25 * 3 % 4)
#
# print("Now I will count the eggs:")
#
# print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
#
# print(5 + 3 + 6 / 12)
# print(5 + 6 - 6 / 8)
#
# print("Is it true that  3+2<5-7")
#
# print(3 + 2 < 5 - 7)
#
# print("What is 3+2?", 3 + 2)
# print("What is 5-7?", 5 - 7)
#
# print("Oh, that's why it is False.")
#
# print("How about some more.")
#
# print("Is it greater?", 5 > -2)
# print("Is it greater or equal?", 5 >= -2)
# print("Is it less or equal?", 5 <= -2)


# ===========Exercise 4================
# -----defining variables and variable names
# =: assignment operator
# cars = 100
# spaceInACar = 4.0
# drivers = 30
# passengers = 90
# carsNotDriven = cars - drivers
# carsDriven = drivers
# carpoolCapacity = carsDriven * spaceInACar
# averagePassengersPerCar = passengers / carsDriven
#
#
# print("There are", cars, "cars available.")
# print("There are only", drivers, "drivers available")
# print("There will be", carsNotDriven, "empty cars today.")
# print("We can transport", carpoolCapacity, "people today.")
# print("We have", passengers, "to carpool today.")
# print("We need to put about", averagePassengersPerCar, "in each car.")
# print(cars==drivers) #== tests whether have the same value



# ========Exercise 5====================
#
# my_name = 'Arin'
# my_age = 24  # not a lie
# my_height = 67  # inches (just a random number)
# my_weight = 140  # pounds
# my_eyes = 'blue'
# my_teeth = 'whitish'
# my_hair = 'brownish blonde'
#

### f is for format, allows for assigned variables into strings

# print(f"Let's talk about {my_name}.")
# print(f"She is {my_height} inches tall")
# print(f"She is {my_weight} pounds")
# print("Actually that is not too heavy.")
# print(f"She has {my_eyes} eyes and {my_hair} hair.")
# print(f"Her teeth are usually {my_teeth} depending on the wine")
#
# # this line is trickyyyy
#
# total = my_age + my_height + my_weight
# print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")



# ===========Exercise 6===================

# # Strings and text
# ## putting variables into strings
# typesOfPeople = 10
# x = f"There are {typesOfPeople} types of people"
#
# binary = "binary"
# doNot = "don't"
# y = f"Those who know {binary} and those who {doNot}."
#
# print(x)
# print(y)
#
# print(f"I said: {x}")
# print(f"I also said: '{y}'")
#
# hilarious =
# pract= "Nope"
# jokeEvaluation = "Isn't that joke so funny?! {}"
#
# ##different way to format
#
# print(jokeEvaluation.format(hilarious))
#
# print(jokeEvaluation.format(pract))
#
# print(jokeEvaluation.format("YA!!"))
#
#
# w = "This is the left side of..."
# e = "a string with a right side."
#
# print(w + e)


# ============Exercise 6=======================

# # Just more printing
#
# print("Mary had a little lamb.")
#
# #similar to ex5 format
# #str instead of var
# #could use f in front of str
# print("Its fleece was white as {}.".format('snow'))
# print("And everywhere that Mary went.")
# print("." * 10)
#
# end1 = "C"
# end2 = "h"
# end3 = "e"
# end4 = "e"
# end5 = "s"
# end6 = "e"
# end7 = "B"
# end8 = "u"
# end9 = "r"
# end10 = "g"
# end11 = "e"
# end12 = "r"
#
## end replaces the new line with a space (dont put a  new line)
# print(end1 + end2 + end3 + end4 + end5 + end6, end=" ")
# print(end7 + end8 + end9 + end10 + end11 + end12)


# ============Exercise 7==================
#
# # more printing
# # complicated formatting of a string
#
# #turnm format variable into other strings
# formatter = "{} {} {} {}"
#
# print(formatter.format(1, 2, 3, 4)) # take formatter str, call format func, pass format to 4 arguments
# print(formatter.format("one","two","three","four"))
# print(formatter.format(True,False,False,True))
# print(formatter.format(formatter,formatter,formatter,formatter))
# print(formatter.format(
#     "Hello",
#     "Tali is cute",
#     "Garrus is a shit head",
#     "I love my doggies"
# ))

###INSERT OTHER EXERCISES DONE ON TABLET

##/ is escape

# =============Exercise 10 (again)==========

##/ is escape

# height="I am 5'4\" tall."
# height2='I am 5\'4" tall.'
#
# print(height)
# print(height2)

# tabbyCat = "\t I'm tabbed in."
# persianCat = "I'm split \non a line"
# backslashCat = "I'm \\ a \\ cat"
#
# fatCat = """
# I'll do a list:
# \t* Cat food
# \t* Fishies
# \t* Catnip\n\t* Grass
# """
#
# print(tabbyCat)
# print(persianCat)
# print(backslashCat)
# print(fatCat)
#
# gar = "garrus smells \a really bad"  # made a box?
# tal = "tali is \f a good puppy"  # an up arrow?
# octo = " octal \ooo value?"  # nothing happened
#
# print(gar)
# print(tal)
# print(octo)


# =================Exercise 11=================

# Asking questions
# input
#
# print("How old are you?", end=' ')  # end tells print not to end the line with a new line char but go to the next line
# age = input()
# print("How tall are you?", end=' ')
# height = input()
# print("How much do you weigh?", end=' ')
# weight = input()
#
# print(f"So, you're {age} old, {height} tall and {weight} heavy.")

## this did not work
# print("bullshit about number 1", end=' ')
# num1=input()
# print("bullshit about number 2", end=' ')
# num2=input()
#
# print(num1+num2)
#



# ============Exercise 12===================

# #Prompting people
# #another input eg
# y = input("Name? ")
#
# age = input("How old are you? ")
# height = input("How tall are you? ")
# weight = input("How much do you weight? ")
#
# print(f"Hello {y}! So, you're {age} old, {height} tall and {weight} heavy.")

# ===============Exercise 13================

# from sys import argv #argv= argument variable
# #sys =modules, libraries syn
#
# script, first, second, third = argv
#
# print("The script is called: ", script)
# print("Your first variable is: ", first)
# print("Your second variable is: ", second)
# print("Your third variable is: ", third)
#

# ==============Exercise 14===================

from sys import argv

# script, user_name = argv
# prompt = '>'
#
# print(f"Hi {user_name}, I'm the {script} script.")
# print("I'd like to ask you a few questions.")
# print(f"Do you like me {user_name}?")
# likes= input(prompt)
#
# print(f"Where do you live {user_name}?")
# lives=input(prompt)
#
# print("What kind of computer do you have?")
# computer= input(prompt)
#
# print(f"""
# Alright, so you said {likes} about liking me.
# You live in {lives}.
# And you have a {computer} computer. Nice.
# """)
#
#


#============Exercise===========================