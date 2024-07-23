#!/usr/bin/env python3

# IT-102 Scripting for Dummies
# Encryption Module

# Justin Gardner
# 7-23-2024

# ----- Rot13 -----

# get the user message and encrypt it

userMessage = input("What is your message to encrypt: ")
userMessage = userMessage.lower()
cipherText = ""
# get ascii integer for each character 

for letter in userMessage:
    ascii_index = ord(letter)
                      
    ascii_index += 13

    if ascii_index > 96 & ascii_index < 123:
        addChar = chr(ascii_index)
    elif ascii_index > 122 & ascii_index < 149: 
        addChar = chr(addChar - 26)

    cipherText += addChar

print(cipherText)



# encrypte each character

# add character to cipher text