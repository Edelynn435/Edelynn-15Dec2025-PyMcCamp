# Write all your codes for Day 3 here.
# COMMENT out the previous task before going on to the next task


########################################################################
# Task 1:
# yourname = input("What is your name?")
# title = input("What is your title?")
# task = input("What is your task?")
# print(yourname, title, "orders the peasants to" + task)



########################################################################
# Task 2:



########################################################################
# Task 3:
# num1 = input("What is the first number?")
# num2 = input("What is the secodn number?")
# answer = int(num1) + int(num2)
# print("the answer is", answer)

########################################################################
# Task 4:
# hidden_password = "Alohomora!"
# guess = input("Do you know my password?")

# if hidden_password == guess:
#     print("You may come in!")
# else:
#     print("Don't give up, please try again")



########################################################################
# Task 5:



########################################################################
# Task 6:
# yourage = 21
# guess = input("What is your age?")

# if yourage <= int(guess):
#     print("You may vote for the next president!")
# else:
#     print("You are not old enough to vote.")

hidden_password = "passme"
is_correct = False
for i in range(3):
    guess = input("Do you know the password?")

    if hidden_password == guess:
        print("Please come in!")
        is_correct = True
        break 
    else:
        print("It's okay, try again!")

if is_correct == False:
    print("Your account is locked.")

########################################################################
# Task 7:



########################################################################
# Task 8:



########################################################################
# Additional exercises:
import random

score = 0

for i in range(3):
    num1 = random.randint(10, 30)
    num2 = random.randint(10, 30)
input(f"What is {num1} + {num2}?")
if 

          
