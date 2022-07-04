#!/usr/bin/python3
def uppercase(str):
    new_string = ''
    i = 0
    for char in str:
        if (ord(char) >= 97):
            num = (ord(char))-32
            char1 = chr(num)
            new_string += char1
            i += 1
        else:
            new_string += char
    print(new_string)
