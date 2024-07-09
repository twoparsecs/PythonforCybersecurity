#!/usr/bin/env python3
# A simple calculator to show math and conditionals
# Created by Justin Gardner

first_num = float(input("What is the first number? "))
activity = input("What activity? ( + - * /) ")
second_num = float(input("What is the second number? "))

if activity == "+":
    print(first_num + second_num)
if activity == "-":
    print(first_num - second_num)
if activity == "*":
    print(first_num * second_num)
if activity == "/":
    print(first_num / second_num)