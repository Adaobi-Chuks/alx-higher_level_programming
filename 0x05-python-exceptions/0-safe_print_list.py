#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    temp = 0
    for i in my_list:
        temp += 1
    print(temp)
    if x <= temp:
        for i in range(x):
            print(my_list[i], end="")
