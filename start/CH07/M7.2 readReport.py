#!/usr/bin/env/ python3

# readReport.py

# Created by Justin Gardner
# August 11th, 2024

# --- Read and Report on Logs ---

# import modules

import os
from collections import defaultdict

dir_path = os.path.dirname(os.path.realpath(__file__))
file_name = 'newaccess.log'

file_path = os.path.join(dir_path, file_name)

response_code_count = defaultdict(int)

try:
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) > 8:
                response_code = parts[8]
                response_code_count[response_code] += 1

except Exception as e:
    print("An error occurred: {}".format(e))

print("{:<25} {:>10}".format('HTTP Response Code', 'Occurrences'))
print("-" * 35)
for code, count in sorted(response_code_count.items()):
    print("{:<25} {:>10}".format(code, count))