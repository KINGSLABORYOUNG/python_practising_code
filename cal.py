# import test_code
logo = '''
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''
# print(logo)
# print(test_code.user_name1)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiple(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# operate = multiple
# print(operate(3, 2))

operators = {
    '+': add,
    '-': subtract,
    '*': multiple,
    '/': divide
}

# def non():
#     accumulate = True
#     num1 = float(input("Enter number: "))
#     while accumulate:
#         for symbol in operators:
#             print(symbol)

#         operations_sign = input("choice one of these operators: ")
#         num2 = float(input("Enter ur second number: "))
#         answer = operators[operations_sign](num1, num2)
#         print(f"{num1} {operations_sign} {num2} = {answer}")

#         choice = input(f"Type 'y' if u want to continue with '{answer}' or 'no' if u wish to start a new calculation: ").lower()

#         if choice == 'y':
#                 num1 = answer
        
#         else:
#             accumulate = False
#             print("\n" * 10)
#             non()

# accumulate = True
# num1 = float(input("Enter number: "))

# while accumulate:
#     for symbol in operators:
#         print(symbol)

#     operations_sign = input("choice one of these operators: ")
#     num2 = float(input("Enter ur second number: "))
#     answer = operators[operations_sign](num1, num2)
#     print(f"{num1} {operations_sign} {num2} = {answer}")

#     choice = input(f"Type 'y' if u want to continue with '{answer}' or 'no' if u wish to start a new calculation: ").lower()

#     if choice == 'y':
#         num1 = answer

#     else:
#         accumulate = False
#         print("\n" * 10)
#         non()