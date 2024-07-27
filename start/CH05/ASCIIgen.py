#!/usr/bin/env python3
# ASCII generator
# Uses chr() to create ASCII characters
# By Justin Gardner

for i in range(127):
    print ("{0}\t'{1}'".format(i, chr(i)))