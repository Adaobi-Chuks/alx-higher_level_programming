#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1, sys
    
    if (len(sys.argv) - 1) != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
        
    if (sys.argv[2] != ('+' and '-' and '*' and '/')):
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)
        
    a = sys.argv[1]
    b = sys.argv[3]
    operator = sys.argv[2]
    
    if operator == '+':
        print(f'{a} {operator} {b} = {calculator_1.add(a, b)}')
    elif operator == '-':
        print(f'{a} {operator} {b} = {calculator_1.sub(a, b)}')
    elif operator == '*':
        print(f'{a} {operator} {b} = {calculator_1.mul(a, b)}')
    elif operator == '/':
        print(f'{a} {operator} {b} = {calculator_1.div(a, b)}')    
