# =======FUNCTIONS======#
#
# def hello():
#     print("howdy!")
#     print("Howdy!!!")
#     print("Hello there.")
#
#
# hello()
# hello()
# hello()
#
#
#
#
# def hello(name):        ##name is a parameter: arg stored w/in func
#     print(f"Hello {name}")
#
# hello ("Alice")
# hello("Bob")        ##prints b/c of func
#

# =======RETURN=======#

import random

# #
# def getAnswer(answerNumber):
#     if answerNumber == 1:
#         return "It is certain"        ## value or express that func should return
#     elif answerNumber == 2:
#         return "It is decidedly so"
#     elif answerNumber == 3:
#         return "Yes"
#     elif answerNumber == 4:
#         return "reply hazy try again"
#     elif answerNumber == 5:
#         return "ask again later"
#     elif answerNumber == 6:
#         return "concentrate and ask again"
#     elif answerNumber == 7:
#         return "my reply is no"
#     elif answerNumber == 8:
#         return "outlook not so good"
#     elif answerNumber == 9:
#         return "very doubtful"
#
# #
# # r = random.randint(1, 9)      ##r is stored in para
# # fortune = getAnswer(r)        ##getAnswer fucn called with r as arg
# # print(fortune)
#
# print(getAnswer(random.randint(1,9)))       ## condensed arg

#=======KEYWORD AGR AND PRINT=======

print("cats", "dogs", "bunnies")
print("cats", "dogs", "bunnies", sep=",")       ##adds commas 
print("cats", end=" ")
print("dogs", end=" ")
print("bunnies")
