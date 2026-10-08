def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

def exponent(n1, n2):
    return n1 ** n2

def mudule (n1, n2):
    return n1 % n2

def floordivision (n1, n2):
    return n1 // n2

# a = 10 // 3
# print(a)

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': division,
    '**': exponent,
    '%': mudule,
    '//': floordivision
}

# print(operations['**'](5, 2))

