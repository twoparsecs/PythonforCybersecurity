#!/usr/bin/env python3
# A more complex "Hello World" script in python with Inputs
# Created by Justin Gardner 7/1/2024

yourName = input("What is your name? ")
print("Hello {0}".format(yourName))
print("The only easy day was yesterday.")

age = int(input("What is your age? "))
futureAge = str(age + 2)
message = " in two years you will be "
print(yourName + message + futureAge)
