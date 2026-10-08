import All_games.cal as cal

#  Calculator APPS
def add(n1, n2):
  """Use for additions"""
  return n1 + n2
 
def subtract(n1, n2):
  return n1 - n2
 
def multiply(n1, n2):
  return n1 * n2
 
def divide(n1, n2):
  return n1 / n2

operations = {
  '+': add,
  '-': subtract,
  '*': multiply,
  '/': divide,
}
# print(operations['-'](4, 8))
def calculator():
  Accomulated = True

  num1 = float(input("Enter a number: "))

  while Accomulated:

    for symbols in operations:
      print(symbols)

    Operations_symbol = input("Enter one of these symbols: ")
    num2 = float(input("Enter the second number: "))
    answer = operations[Operations_symbol](num1, num2)
    print(f"{num1} {Operations_symbol} {num2} = {answer}")

    choice = input(f"type 'y' if u want to continue with {answer}, or 'n' if u want to start a new calculations: ").lower()

    if choice == 'y':
      num1 = answer

    else:
      Accomulated = False
      print("\n" * 20)

      calculator()
      
calculator()      
