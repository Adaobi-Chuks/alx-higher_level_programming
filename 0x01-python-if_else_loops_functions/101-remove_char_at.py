#!/usr/bin/python3
def remove_char_at(str, n):
    new_string = ''
    position = -1
    for char in str:
        position += 1
        if position == n:
            continue
        new_string += char
    return new_string
