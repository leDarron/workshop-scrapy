#!/usr/bin/env python3

##
## EPITECH PROJECT, 2022
## scrapy
## File description:
## ex3
##

def isAnagram(w1, w2):
    if sorted(w1) == sorted(w2):
        return True
    return False

def anagrams(word, l):
    ret = []
    for item in l:
        if isAnagram(word, item):
            ret.append(item)
    return ret

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
print(anagrams('laser', ['lazing', 'lazy',  'lacer']))