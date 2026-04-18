#!/usr/bin/env python3

def calculator():
    print("Simple Calculator")
    print("Operations: +  -  *  /")

    # Take user input
    num1 = float(input("Enter first number: "))
    op = input("Enter operation (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    # Perform calculation
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print(" Cannot divide by zero")
            return
    else:
        print(" Invalid operation")
        return

    print(" Result:", result)


# Run the program
calculator()
