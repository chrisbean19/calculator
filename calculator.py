def multiply(x, y):
    return x*y

def add(x, y):
    return x+y

def subtract(x, y):
    return x-y

def divide(x, y):
    if y == 0:
        y = 0.001
    return x/y

def request_input(which):
    while True:
        try:
            print("Input " + which + ": ")
            x = float(input())
            return x
        except TypeError:
            print("Please input numeric decimal input only")

def process_inputs(x, y, func):
    return func(x, y)

x = request_input("x")
y = request_input("y")