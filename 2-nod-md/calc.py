#!/usr/bin/env python
def summa(first, second):
    output = first + second
    return output

def atnemsana(first, second):
    output = first - second
    return output

def multiplikacija(first, second):
    output = first * second
    return output

def dalisana(first, second): 
    output = first / second
    return output
    
def eksponenta(first, second):
    output = first ** second
    return output

def check_float(num):
    try:
        float(num)
        return float(num)
    except ValueError:
        exit("Nepareiza ievade")

def check_cool(given):
    if given == 69:
        print("Nice :D")
    elif 68 < given < 70:
        print("Tuvu!")
    return given

def check_operator(op):
    if (op == '+') or (op == '-') or (op == '*') or (op == '/') or (op == 'eksp') or (op == '^'):
        return op
    else:
        exit("Nepareiza ievadīts operators")

## Šo daļu nedzēst!
if __name__ == "__main__":
    print("Testēt funkciju:", __name__)
    assert summa(1,2) == 3
    assert atnemsana(3,1) == 2
    assert multiplikacija(1,2) == 2
    assert dalisana(2,2) == 1
    assert eksponenta(2,2) == 4
else:
    print("Modulis palaists importējot:", __name__)
