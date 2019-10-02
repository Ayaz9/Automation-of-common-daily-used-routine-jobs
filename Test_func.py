import random, turtle

# first = input("Enter the first number : ")
# second = input("Enter the second number: ")
#
# if first.isdigit() and second.isdigit() :
#     num1 = int(first)
#     num2 = int(second)
#     if num1 > num2:
#         print("This is the biggest number : {}".format(num1))
#     elif num2 > num1 :
#         print("This is the biggest number : {}".format(num2))
#     elif num1 == num2:
#         print("{} and {} are equal".format(num1,num2))
# else:
#     print("Please enter integer as it is required to enter digits")
#

# num = random.randint(0,100)
# while True:
#     usr_input = input("please guess the number: ")
#     if num > int(usr_input):
#         print("high")
#     elif num < int(usr_input):
#         print("Low")
#     if num == int(usr_input):
#         print("Congratulations, the number was : {}".format(num))
#     else:
#         continue
#
#


# this works
# entry = int(input("Please enter the number: "))
# i = 1
# while i<= entry:
#     print("*"*i)
#     i+=1
# #

# This works
# while True:
#     entry = input("Please enter the number: ")
#     a = int(entry) - 2
#     print("*"*int(entry))
#     for i in range(a):
#         print("*" + " "*a + "*")
#     print("*"*int(entry))
#


# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print “Fizz” instead of the
# number and for the multiples of five print “Buzz”. For
# numbers which are multiples of both three and five
# print “FizzBuzz”.


#
# for i in range(1,101):
#     if (i % 3 == 0) and (i % 5 == 0):
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)


#
# def average(numbers: list) -> float:
#     return sum(numbers)/len(numbers)
# numbers = [6,7,8,10, 17, 80]
# result = average(numbers)
# print(result)
#

#
# a = []
# with open("alice.txt", "r") as f:
#     for i in f:
#         if "CHAPTER" in i:
#             b = i.split(". ")[1]
#             print(b)
#



import turtle

print(turtle.position())
def func1():
    turtle.pendown()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    print(turtle.position())
    turtle.penup()

def func2():
    turtle.setx(20)
    turtle.sety(20)

for i in range(4):
    func1()
    func2()

turtle.done()
