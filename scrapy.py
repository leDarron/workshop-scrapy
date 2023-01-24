##
## EPITECH PROJECT, 2023
## scrapy
## File description:
## scrapy
##


#EX01
def numbers():
    for i in range(100):
        n = i + 1
        if (n % 3 == 0):
            print("Three")
        elif (n % 5 == 0):
            print("Five")
        else:
            print(n)


# EX02
def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

def calculate(l):
    if (type(l) != list):
        return False
    res = 0
    for item in l:
        if type(item) == str and is_integer(item):
                res += int(item)
    return res


#EX03
def del_char(s, pos):
    i = 0
    new = ""
    while i < pos:
        new += s[i]
        i += 1
    i += 1
    while i < len(s):
        new += s[i]
        i += 1
    return new

def is_anagram(s1: str, s2: str):
    tmp = -1
    for i in range(len(s1)):
        tmp = -1
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                tmp = j
        if tmp == -1:
            return False
        s2 = del_char(s2, tmp)
    return True

def anagrams(word, tab):
    res = []
    for item in tab:
        if is_anagram(item, word):
            res.append(item)
    return res




