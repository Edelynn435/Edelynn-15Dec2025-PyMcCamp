# Write all your codes for Day 1 here.
# COMMENT out the previous task before going on to the next task
# print("hello from day1 I am Edelynn")
# print("I study at Ngee Ann Secondary School")
# print("I live in Tampines")
# print("I am 14 years old")
# print("If I have $2000, I would travel to Korea")

# for i in range(10):
#     print("3")

########################################################################
# Task 1:



########################################################################
# Task 2:



########################################################################
# Task 3:

# zoo1 = "hedgehog"
# zoo2 = "chameleon"
# zoo3 = "crocodile"
# print(zoo1)
# print(zoo2)
# print(zoo3)



########################################################################
# Task 4:
# var1 = 20
# var2 = 26
# var3 = (var1) + (var2)
# print(var3)

# var1 = 10
# var2 = 2
# var3 = (var1) / (var2)
# print(var3)

# var1 = 10
# var2 = 2
# var3 = (var1) * (var2)
# print(var3)

# var1 = 10
# var2 = 2
# var3 = (var1) - (var2)
# print(var3)

# var1 = 10
# var2 = 2
# var3 = (var1) + (var2)
# print(var3)









########################################################################
# Task 5:

# name = "Edelynn"
# food = "noodles"
# print("My name is " + name)
# print("I like to eat " + food)

# def greetings(): 
#     print("hello")
#     print("My name is Edelynn")
#     print("I love to draw")

# greetings() # call a function
# greetings() # call a function




########################################################################
# Task 6:

# def intro(name): 
#     print("Nice to meet you, " + name)
#     print(name)

# intro("Amy")
# intro("Chris")

########################################################################
# Task 7:
#addition
# def addition(num1, num2):
#     print(num1 + num2)
    
# addition(20, 26)

# #multiplication 
# def multiplication(num1, num2):
#     print(num1 * num2)

# multiplication(20, 26)

# #substraction
# def substraction(num1, num2):
#     print(num1 - num2)

# substraction(20, 26)

# #division
# def division(num1, num2):
#     print(num1 / num2)

# division(20, 26)

########################################################################
# Additional exercises:
# for i in range(3):
#     num1 = random.randint
#     num2 = random.randint 

# name = Steve
# title = King 
# print("I am " + name)
# print("You shall know me as " + title + name)
import random
score = 0  
for i in range(3):
    num1 = random.randint(10,30)
    num2 = random.randint(10,30)

    answer = input(f"What is {num1} + {num2}: ")
    if int(answer) == int(num1) + int(num2):
        print("CORRECT")
        score = score+1
    else:
        print("INCORRECT")

print(score/3*100)

    