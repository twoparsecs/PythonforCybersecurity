#!/usr/bin/env python3
# Sample script that reads from a file
# By Justin Gardner

ip_file = open("ips.txt", "r")
ip_addresses = ip_file.read()
print(ip_addresses)

ip_file.close()