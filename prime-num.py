# user_input = int(input("Enter number to check if is prime num: "))

# if user_input % 2 == 0:
#     print(f"Number {user_input} is not a prime number cus 2 can go")

# elif user_input % 3 == 0:
#     print(f"Number {user_input} is not a prime number, cus 3 can go")
# else:
#     print(f"Number {user_input} is a prime Number")

def continue_check():

    user_input = int(input("Enter number to check if is prime num: "))
    if user_input < 2:
        print(f"'{user_input}' is not a prime number!")

    else:

        is_prime = True
        for numbers in range(2, user_input):
            
            if user_input % numbers == 0:
                is_prime = False
                break

        if is_prime:
            # print(f"'{user_input}' is a prime number!")
            print(f"'{user_input}' is a prime number!")

        else:
            print(f"'{user_input}' is not a prime number!")

print(continue_check())

wish_to_continue = input("Type 'Y' to continue or 'N' to stop: \n").upper()
while wish_to_continue == 'Y':
    continue_check()
    wish_to_continue = input("Type 'Y' to continue or 'N' to stop: \n").upper()
