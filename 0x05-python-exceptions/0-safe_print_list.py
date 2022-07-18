#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    temp = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            temp += 1
        print()
        return temp
    except Exception:
        print()
        return temp
