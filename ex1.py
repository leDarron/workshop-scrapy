#!/usr/bin/env python3

##
## EPITECH PROJECT, 2022
## scrapy
## File description:
## ex1
##

for i in range(1, 101):
    if i%3 == 0 and i%5 == 0:
        print("ThreeFive")
    elif i%3 == 0:
        print("Three")
    elif i%5 == 0:
        print("Five")
    else:
        print(i)