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
        except ValueError:
            print("Please input numeric decimal input only")

def process_inputs(x, y, func):
    return func(x, y)

def request_function():
    while True:
        try:
            print("Input number to select function: [0] Add, [1] Subtract, [2] Multiply, [3] Divide")
            sel = int(input())
            if sel == 0:
                return add
            elif sel == 1:
                return subtract
            elif sel == 2:
                return multiply
            elif sel == 3:
                return divide
        except ValueError:
            print("You must input a number")

func = request_function()
x = request_input("x")
y = request_input("y")
print("Answer: ", process_inputs(x, y, func))