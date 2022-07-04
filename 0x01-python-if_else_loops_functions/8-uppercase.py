#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if (str >=90):
            print('{:s}'.format(chr((ord(char))-32)), end='')
    print()
