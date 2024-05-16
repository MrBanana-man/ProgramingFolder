
def minus(num1, num2):
    output = num1 - num2
    print(output)

def plus(num1, num2):
    output = num1 + num2 
    print(output)

def times(num1, num2):
    output = num1 * num2 
    print(output)

def divide(num1, num2):
    output = num1 / num2 
    print(output)

print("First num: ")
num1 = int(input())

print("Choose calculation mode: ")
operation = input()

print("Second num: ")
num2 = int(input())

if operation == "times":
    times(num1, num2)
if operation == "devied":
    divide(num1, num2)
if operation == "plus":
    plus(num1, num2)
if operation == "minus":
    minus(num1, num2)

