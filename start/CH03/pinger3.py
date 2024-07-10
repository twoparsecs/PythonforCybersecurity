#!/usr/bin/env python3
# Third example of pinging from Python
# By Justin Gardner

import platform
import os

ip_prefix = "192.168.0."
current_os = platform.system().lower

for final_octet in range(254):
    ip = ip_prefix + str(final_octet + 1)
    if current_os == "windows":
        ping_cmd = f"ping -c 1 -w 2 {ip} > nul"
    else:
        ping_cmd = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"

    exit_code = os.system(ping_cmd)
    if exit_code == 0:
        print("{0} is online".format(ip))