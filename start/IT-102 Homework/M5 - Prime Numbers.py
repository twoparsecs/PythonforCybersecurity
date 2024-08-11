#!/usr/bin/env Python3

# ---Prime Numbers---

# Created by Justin Gardner
# August 5th 2024


# Define function to return true or false regarding prime or not

def is_prime(number):
    if number  <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def main():
    try:
        user_input = int(input("Enter any number to determine if it is prime: "))
        if user_input == 0:
            print("0 is neither prime, nor composite...")
        elif is_prime(user_input):
            print(f"{user_input} is a prime number!")
        else:
            print(f"{user_input} is not a prime number.")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()