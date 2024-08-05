#!/usr/bin/env python3

# Script that cracks password hashes.

# --- Find the Passwords---

# Created by Justin Gardner
# August 4th, 2024

import crypt
import os

def test_password(hashed_password, algorithm_salt, plaintext_password):
    crypted_password = crypt.crypt(plaintext_password, algorithm_salt)
    return hashed_password == crypted_password

def read_file(file_path):
    try:
        with open(file_path, "r") as f:
            return f.readlines()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return []

def parse_shadowfile(shadow_file_path):
    users = []
    lines = read_file(shadow_file_path)
    for line in lines:
        if line.strip() and not line.startswith('#'):  # Skip empty lines and comments
            parts = line.strip().split(':')
            if len(parts) >= 2:
                name = parts[0]
                hashed_password_data = parts[1]
                if '$' in hashed_password_data:
                    hash_parts = hashed_password_data.split('$')
                    if len(hash_parts) >= 4:
                        hash_type = hash_parts[1]
                        salt = f"${hash_parts[1]}${hash_parts[2]}"
                        hashed_password = hash_parts[3]
                        users.append({
                            "name": name,
                            "hash_type": hash_type,
                            "salt": salt,
                            "hashed_password": hashed_password
                        })
    return users

def attack_user(user, password_dictionary):
    for password in password_dictionary.splitlines():
        if test_password(user["hashed_password"], user["salt"], password):
            print(f"Match found for {user['name']}: {password}")
            return True
    print(f"No match found for {user['name']}")
    return False

def attack_all_users(shadow_file_path, password_file_path):
    users = parse_shadowfile(shadow_file_path)
    password_dictionary = read_file(password_file_path)
    password_dictionary = ''.join(password_dictionary)  # Convert list of lines to a single string

    for user in users:
        print(f"Attacking user: {user['name']}")
        attack_user(user, password_dictionary)

if __name__ == "__main__":
    shadow_file_path = input("Enter the path to the shadow file: ")
    password_file_path = "/home/justincase/Desktop/PythonforCybersecurity/start/CH06/10-million-password-list-top-10000.txt"
    attack_all_users(shadow_file_path, password_file_path)