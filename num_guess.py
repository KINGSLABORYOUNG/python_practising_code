from random import randint
# Text to ASCII Art Generator: Create ASCII Art from Text

print("Welcome to number guessing game!!!")
print("I'm thinking of a number between 1 & 100.")
guess = randint(1, 100)
print(guess)

hard_level = 5
easy_level = 10



# let the user choose a level
level = input("choose a difficulty, type 'hard' or 'easy': ").lower()

# tell the user the number of attemps they have
attempts = 0
if level == 'easy':
   attempts = easy_level

elif level == 'hard':
   attempts = hard_level

else:
    print("Sorry! your selection wasn't from the listed options.\n Game Over")

keep_guess = False
while  not keep_guess and attempts > 0:

    user_guess = int(input("Guess the number: "))
    if user_guess < guess:
        print("Too low, guess again")
        attempts -= 1
        if attempts > 0:
            print(f"'{attempts}' attempts left")
            

    elif user_guess > guess:
        print("Too high, guess again")
        attempts -= 1
        if attempts > 0:
           print(f"'{attempts}' attempts left")  

    else:
        keep_guess = True
        print("Congrat, You Win")

if not keep_guess:
    print(f"Game Over! The number was {guess}. Better luck next time!")

