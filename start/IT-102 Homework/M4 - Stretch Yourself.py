#!/usr/bin/env Python3

# ---Divisible by X---
# Create a script that prompts the user for a number and a divisor
# Create a functioon named is_divisible and pass in the number and divisor as parameters
# The function should return true or false if the number was cleanly divisible
# The script reports if the number was divisible
# Created by Justin Gardner
# July 9th, 2024


def is_divisible(number, divisor):
    if  divisor == 0:
        raise ValueError("Divisor cannot be zero.")
    
    return number % divisor == 0
        
def game():
    try:
        number = int(input("Give me a number: "))
        divisor = int(input("OK. Now give me a divisor: "))
        quotient = number / divisor
    
        if is_divisible(number, divisor):
            print(f"The quotient is: {quotient}. {number} is cleanly divisible by {divisor}.")
        else:
            print(f"The quotient is: {quotient}. {number} is not cleanly divisible by {divisor}.")

        play_again = input("Would you like to try again? (y/n): ")

        if play_again.lower() == "y":
            game()
        else:
            print("Thank you for playing.")

    except ValueError as e:
        print(f"Error: {e}")
        game()

game()


    