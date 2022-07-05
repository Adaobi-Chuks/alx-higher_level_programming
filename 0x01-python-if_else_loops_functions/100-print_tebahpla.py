#!/usr/bin/python3
count = 2
lower = 122
upper = 90
for i in range(26):
    if (count % 2) == 0:
        char = chr(lower)
    else:
        char = chr(upper)
    count += 1
    lower -= 1
    upper -= 1
    print('{}'.format(char), end='')
