#!/usr/bin/env python3
# The script generates a promt asking if it is a good day. -40 points
# The script takes the text entry from the user and stores it as a variable. -30 points
# The script provides the appropriate responses. Test case one passes, test case two passes,
# test case 3 passes. -30 points
# Created by Justin Gardner on 7-5-2024

day = input("Is today a good day? Please answer y/n... ")

#Created a function for the for loop
def send_message():
    for i in range(10):
        print("Yeah it is.")

# Calling the above function
if day == "y":
    send_message()
    
elif day == "n":
    print("I am sorry to hear that... :(")
else:
    print("You did not make the right selection. Goodbye...")