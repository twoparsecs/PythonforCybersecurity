#!/usr/bin/env/ python3

# createLogEntry.py

# Created by Justin Gardner
# August 8th, 2024

# --- Create Logs to File Script ---

# import modules
 
import datetime
import hashlib

def create_log_entry(ip_address, identd, username, \
                     resource_message, http_return_code, return_size, log_file='logfile.log'):
    now = datetime.datetime.now()
    str_now = now.astimezone().strftime('%d/%b/%Y:%H:%M:%S %z')
    log_entry = (f'{ip_address} {identd} {username} - [{str_now}] '
                 f'"{resource_message}" {http_return_code} {return_size}\n')
    
    with open(log_file, 'a') as file:
        file.write(log_entry)
    
    with open(log_file, 'rb') as file:
        file_contents = file.read()
        file_hash = hashlib.sha256(file_contents).hexdigest()

    with open(f'{log_file}.hash', 'w') as hash_file:
        hash_file.write(file_hash)

    print(f"Log entry added to {log_file}. Integrity hash saved to {log_file}.hash")

if __name__ == "__main__":
    create_log_entry(
        ip_address='192.168.1.1',
        identd='-',
        username='justincase',
        resource_message='POST /administrator/index.php HTTP/1.0',
        http_return_code='404',
        return_size='2048'
    )