def myfunc():
    print('This is my function')


myfunc()
myfunc()


def addtwonumbers():
    num1 = int(input('Enter first Number: '))
    num2 = int(input('Enter second Number: '))
    print(f'The sum of {num1} and {num2} is {num1 + num2}')


addtwonumbers()


def calculator():
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    operator = input('Enter Operator: ')
    if operator == '+':
        print(num1 + num2)
    elif operator == '-':
        print(num1 - num2)
    elif operator == '*':
        print(num1 * num2)
    elif operator == '/':
        print(num1 / num2)
    elif operator == '**':
        print(num1 ** num2)
    else:
        print("Invalid Input")


calculator()
