#!/usr/bin/env python3
# Create a script that prompts the user for a number, and 
# tells the user if the number is EVEN
# Created by Justin Gardner 7-5-2024

number_str = input("Please input any number: ")
number = int(number_str)

if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number is not even")