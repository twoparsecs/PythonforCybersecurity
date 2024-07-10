#!/usr/bin/env python3
# Fifth example of pinging from Python
# Reading IPs from a file
# By Justin Gardner

import platform
import os

def ping_host(ip):
    current_os = platform.system().lower()
    if current_os == "windows":
        ping_cmd = f"ping -n 1 -w 2 {ip} > nul"
    else:
        ping_cmd = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"
    exit_code = os.system(ping_cmd)
    return exit_code

def import_adresses():
    lines = []
    new_dir = "/home/justincase/Desktop/PythonforCybersecurity/start/CH04"
    os.chdir(new_dir)
    f = open("ips.txt", "r")
    for line in f:
        line = line.strip()
        lines.append(line)
    
    return lines
    
ip_addresses = import_adresses()

for ip in ip_addresses:
    exit_code = ping_host(ip)
    if exit_code == 0:
        print("{0} is online.".format(ip))
    else:
        print("{0} is offline or not reachable.".format(ip))

