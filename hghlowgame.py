import random
from All_games.celeb_info import Game_list
from All_games.art import logo, logo1, logo2

def format(account):
    '''format the acconut data return in into a printable format'''
    account_name = account['Name']
    account_Descript = account['Descriptions']
    account_follo = account['Follower_count']
    account_Country = account['Country']
    return f"{account_name}, a {account_Descript}, from {account_Country}."

def comparism(guess, A_follower, B_follower):
    if A_follower > B_follower:
        return guess == 'A'
    else:
        return guess == 'B'

def convert_followers(followers):
    if followers.endswith('M'):
        return float(followers[:-1]) * 1000000


# importing ascii
print(logo1)
score = 0
account_B = random.choice(Game_list)
is_game_over = False

while not is_game_over:
    # random selection of the list/dictionary
    account_A = account_B
    account_B = random.choice(Game_list)
    if account_A == account_B:
        account_B = random.choice(Game_list)

    # print(account_A, account_B)
    print(f"Compare A: {format(account_A)}")
    print(logo2)
    print(f"Against B: {format(account_B)}")

    guess = input("Who has the more followers, A or B: ").upper()

    # comparism()
    A_follower = account_A['Follower_count']
    B_follower = account_B['Follower_count']

    A_follower_num = convert_followers(A_follower)
    B_follower_num = convert_followers(B_follower)

    is_correct = comparism(guess, A_follower_num, B_follower_num)
    if is_correct:
        score += 1
        print(f"You are right, A = {A_follower}, while B = {B_follower}\n your score = {score}")

    else:
        is_game_over = True
        print(f"You are wrong A = {A_follower}, while B = {B_follower}\nGame Over! your final score = {score}")

