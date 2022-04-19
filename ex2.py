#!/usr/bin/env python3

##
## EPITECH PROJECT, 2022
## scrapy
## File description:
## ex2
##

def isInt(n):
    try:
        int(n)
        it_is = True
    except ValueError:
        it_is = False
    return it_is

def calculate(l):
    sum = 0
    numeric = False
    if type(l) != list:
        return False
    for item in l:
        if isInt(item) and type(item) == str:
            sum += int(item)
            numeric = True
    if numeric == True:
        return sum
    else:
        return True

print(calculate(['4', '3', '-2']))
print(calculate(453))
print(calculate(['nothing', 3, '8', 2, '1']))
print(calculate('54'))