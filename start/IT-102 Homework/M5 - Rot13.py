#!/usr/bin/env python3

# Script that encrypts/decrypts text using ROT13

# --- ROT13 ---
# By Justin Gardner 
# July 27, 2024

# Prompt the user for the source messaage to encrypt

source_message = input("What message would you like to encrypt? ")
source_message = source_message.upper()
cipher_message = ""

# Loop through each letter in the source message
for letter in source_message:
    # Convert to ascii equivalent
    ascii_num = ord(letter)
    # Check to see if an alphabetic character(a-z) character,
    # if not, skip
    if ascii_num >= 65 and ascii_num <= 90:
        # Add 13 to ascii_num to "shift" it by 13
        new_ascii = ascii_num + 13
        if new_ascii > 90:
            new_ascii = new_ascii - 26
        cipher_message = cipher_message +chr(new_ascii)
    else:
        cipher_message = cipher_message + chr(ascii_num)

print("Message has been converted:")
print(cipher_message)