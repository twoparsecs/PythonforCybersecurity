#!/usr/bin/env/ python3

# readReport.py

# Created by Justin Gardner
# August 11th, 2024

# --- Read and Report on Logs ---

# import modules

import os

# open and read file

dir_path = os.path.dirname(os.path.realpath(__file__))
file_name = '/logfile.log'

file_path = dir_path + file_name

f = open(file_path, 'r')

page404list = []

while True:
    line = f.readline()
    if line:
        if "404 " in line:
            path = (line.strip()).split()[6]
            error = (line.strip()).split()[8]
            if path not in page404list:
                page404list.append(path)
                print(error, "\t", path)
            
    if not line:
        break

print(f"Total unique 404 paths: {len(page404list)}")