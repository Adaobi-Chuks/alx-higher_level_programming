#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    
    if (len(sys.argv) - 1) != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
        
    operator = sys.argv[2]    
    if (operator != '+') and (operator != '-') and (operator != '*') and (operator != '/'):
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)
        
    from calculator_1 import add, sub, mul, div
    a = sys.argv[1]
    b = sys.argv[3]
    
    if operator == '+':
        print(f'{a} {operator} {b} = {add(a, b)}')
    elif operator == '-':
        print(f'{a} {operator} {b} = {sub(a, b)}')
    elif operator == '*':
        print(f'{a} {operator} {b} = {mul(a, b)}')
    elif operator == '/':
        print(f'{a} {operator} {b} = {div(a, b)}')    
