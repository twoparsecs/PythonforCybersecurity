#!/usr/bin/env python3
# Script that hashes a password with provided salt
# By Justin Gardner
# 7-31-2024

#---HASH with SALT---

import crypt

plain_pass = input("Create a new password: ")
salt = input("What is the salt? ")

print("MD5      : {0}".format(crypt.crypt( \
    plain_pass,"$1$" + salt)))