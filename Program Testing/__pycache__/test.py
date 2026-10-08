from cal import operations

def Calculator():
    user_num1 = float(input("Enter a number: "))

    To_proceed = True

    while To_proceed:

        for symbol in operations:
            print(symbol)

        operand = input("Enter one of these symbols: ")
        user_num2 = float(input("Enter the second num: "))

        Answer = operations[operand](user_num1, user_num2)
        print(f"{user_num1} {operand} {user_num2} = {Answer}") 

        user_choice = input("Type 'y' to continue with the Answer, or 'n' if not to: ").lower()
        if user_choice == 'y':
            user_num1 = Answer

        else:
            To_proceed = False
            print('\n' * 15)
            Calculator()

Calculator()