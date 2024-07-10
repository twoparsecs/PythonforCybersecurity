#!/usr/bin/env python3
# Sixth example of pinging from Python
# Writing log messages to a file
# By Justin Gardner
# Jully 9th, 2024

import platform
import os
from datetime import datetime

os.chdir("/home/justincase/Desktop/PythonforCybersecurity/start/CH04")

def write_log(message):
    now = str(datetime.now()) + "\t"
    message = now + str(message) + "\n"
    f = open("pinger.log", "a")
    f.write(message)
    f.close()

def ping_host(ip):
    current_os = platform.system().lower()
    if current_os == "windows":
        ping_cmd = f"ping -n 1 -w 2 {ip} > nul"
    else:
        ping_cmd = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"
    exit_code = os.system(ping_cmd)
    return exit_code

def import_addresses():
    lines = []
    f = open("ips.txt", "r")
    for line in f:
        line = line.strip()
        lines.append(line)
    return lines

write_log("Reading IPs from ips.txt")
ip_addresses = import_addresses()
write_log("Imported {0} IPs".format(len(ip_addresses)))

for ip in ip_addresses:
    exit_code = ping_host(ip)
    if exit_code == 0:
        write_log("{0} is online".format(ip))
    else:
        write_log("{0} is offline.".format(ip))