import sys
import calc

first = sys.argv[1]
first = calc.check_float(first)
operator = sys.argv[2]
operators = calc.check_operator(operator)
second = sys.argv[3]
second = calc.check_float(second)

if operator == '+':
    print(calc.summa(first, second))
elif operator == '-':
    print(calc.atnemsana(first, second))
elif operator == '*':
    print(calc.multiplikacija(first, second))
elif operator == '/':
    print(calc.dalisana(first, second))
elif ((operators == 'eksp') or (operators == '^')):
    print(calc.eksponenta(first, second))
else: 
    exit("Failed to do the operation")



