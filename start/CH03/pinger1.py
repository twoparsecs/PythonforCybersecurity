#!/usr/bin/env python3
# First example of pinging from Python
# By Justin Gardner


import platform
import os

ip = "192.168.0.100"

ping_cmd = f"ping -c 5 -w 5 {ip} > /dev/null 2>&1"
exit_code = os.system(ping_cmd)

if exit_code == 0:
    print("{0} is online.".format(ip))