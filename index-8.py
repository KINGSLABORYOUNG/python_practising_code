# def agree():
#     a = 8
#     b = 3
#     if a == b:
#         print("Arrive")
#     else:
#         print("Go home")

# agree()

# def life_in_weeks(age):
#     years_remaining = 90 - age
#     weeks_remaining = 52 * years_remaining
#     print(f"You have {weeks_remaining} weeks remaining. workd harder!")

# life_in_weeks(30)

# def weeks_like(name, locations):
#     print(f"Hell {name}!")
#     print(f"How is {locations}?")
# # this is known as locations argument
# weeks_like("Angela", "Newyork")

# # keyargument
# weeks_like(locations="london", name="Endowa")

# a = 4 % 25
# b = 25 % 4
# print(a, b)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 'p', 'u', 'v', 'w', 'x', 'y','z']
user = input("enter a leter ").lower()
integer = int(input("Shift number: "))
# shift = letters.index(user)
# print(shift)

def encrption(original_text, shift_amount):
    list = ""
    for alphabet in original_text:
        shifted_postion = letters.index(alphabet) + shift_amount
        shifted_postion %= len(letters)
        list += letters[shifted_postion]
        print(f"Here is encodered word: {list}")

            
def decrption(original_text, shift_amount):
    cypher_text = ""
    for alphabet in original_text:
        shifted_position = letters.index(alphabet) - shift_amount
        shifted_position %= len(letters)
        cypher_text += letters[shifted_position]
    print(f"Here is decodered word: {cypher_text}")

encrption(original_text=user, shift_amount=integer)
