#!/usr/bin/env python3

# IT-102 Scripting for Dummies
# Encryption Module

# Justin Gardner
# 7-23-2024

from cryptography.fernet import Fernet

Fernet.generate_key()

key = Fernet.generate_key()
print(key)

message = input("What would you like to encrypt: ")
message = message.lower()
message = message.encode()
cipherText = Fernet(key).encrypt(message)
print(cipherText)