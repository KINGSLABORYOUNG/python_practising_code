import random
from game_list import Game_list, logo1, logo2

def format(account):
    acc_name = account['Name']
    acc_Descript = account['Descriptions']
    acc_Country = account['Country']
    return f"{acc_name} a {acc_Descript} from {acc_Country}."

            
def compare(guess, a_follo, b_follo):
    if a_follo > b_follo:
        return guess == 'A'
    else:
        return guess == 'B'
    
    
def covert_num(followers):
    if followers.endswith('M'):
        return float(followers[:-1]) * 1000000

    
# printout art
print(logo1)
account_b = random.choice(Game_list)
score = 0

Game_over = False

while not Game_over:
    account_a = account_b
    account_b = random.choice(Game_list)
    if account_a == account_b:
        account_b = random.choice(Game_list)

    # printout a random list no.1
    print(f"Compare A: {format(account_a)}")

    # printout a 2nd art
    print(logo2)
    
    # printout a random list no.2
    print(f"Against B: {format(account_b)}")

    # user guesses
    guess = input("Who has more followers: ").upper()

    a_follo = account_a['Follower_count']
    b_follo = account_b['Follower_count']

    a_follo_num = covert_num(a_follo)
    b_follo_num = covert_num(b_follo)

    is_correct = compare(guess, a_follo_num, b_follo_num)
    if is_correct:
        score += 1
        print(f"You are right. A = {a_follo}, B = {b_follo} you score {score}")

    else:
        print(f"Sorry, its Game Over!! A = {a_follo}, B = {b_follo}\n your final score {score}")
        Game_over = True


    # repeat while is right, stop when it wrong