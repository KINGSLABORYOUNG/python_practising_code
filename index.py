# HANGLE MAN GAME
import random
select_list = ["man", "woman", "lady", "gentle", "aanad"]

random_choice = random.choice(select_list)
print(random_choice)

place_holder = ""
word_len = len(random_choice)

for i in range(0, word_len):
    place_holder += "_"
print(place_holder)

game_over = False
correction_list = []

while not game_over:
    user_choice = input("Guess the word to save a soul\n").lower()
    # print(user_choice)
    display = ""
    for letter in random_choice:
        if letter == user_choice:
            display += letter
            correction_list.append(letter)
        elif letter in correction_list:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("You win")

