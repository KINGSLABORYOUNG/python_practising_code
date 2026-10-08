letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt\n").lower()
Text = input("Type your message! \n").lower()
shift = int(input("Type the shift Number.\n"))



def caesar(original_text, shift_amount, encode_or_decode):
    output = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for alphabet in original_text:
        if letters not in 'Text':
            output += alphabet
        else: 
            shifted_position = alphabet.index(letters) + shift_amount
            shifted_position %= len(letters)
            output += letters[shifted_position]
            print(f"Here is {encode_or_decode}d word: {output}")

    start_again = True
    while start_again:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt\n").lower()
        Text = input("Type your message! \n").lower()
        shift = int(input("Type the shift Number.\n"))

        restart = input("Type 'yes' to continue with caeser cipher text or 'no' for otherwise\n").lower()
        if restart == 'no':
            start_again = False
            print("Goodbye!!")
 
caesar(original_text=Text, shift_amount=shift, encode_or_decode=direction)



# encrption(original_text=Text, shift_amount=shift)

# decrption(original_text=Text, shift_amount=shift)
