#!/usr/bin/env python3

# Script that cracks password hashes.

# --- Find the Passwords---

# Created by Justin Gardner
# August 4th, 2024

import crypt
import os

def test_password(hashed_password, \
                  algorithm_salt, plaintext_password):
    crypted_password = crypt.crypt( \
        plaintext_password, algorithm_salt)
    if hashed_password == crypted_password:
        return True
    return False

def read_dictionary(dictionary_file):
    with open(dictionary_file, "r") as f:
        message = f.read()
    return message

password_dictionary = read_dictionary("/home/justincase/Desktop/PythonforCybersecurity/start/CH06/10-million-password-list-top-1000000.txt")
hashed_password = input("What is the hashed password? ")
algorithm_salt = input("What is the algorithm and salt? ")

for password in password_dictionary.splitlines():
    result = test_password(hashed_password, \
                           algorithm_salt, password)
    if result:
        print("Match found: {0}".format(password))
        break
else:
    print("Sorry, no match was found.")