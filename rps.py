import random
import time
#Variables
user_sel = None
moves = ('rock', 'paper', 'scissors')
opp_sel = None
game = 0
wins = 0
losses = 0
#Loop
print('welcome to rock, paper, scissors...\n')
while True:
#Moves
    user_sel = input(f'[1]rock \n[2]paper \n[3]scissors \n[input]: ')
    opp_sel = random.choice(moves)
#Rock
    if user_sel == '1' and opp_sel == 'rock':
        time.sleep(1)
        print('\nopponent selects rock... \nDRAW! \n')
        time.sleep(1)
        game = game + 1
        print('---Score---\n[game]:', game, '\n[wins]:', wins, '\n[losses]:', losses, '\n')
        time.sleep(1)
        continue

    if user_sel == '1' and opp_sel == 'paper':
        time.sleep(1)
        print('\nopponent selects paper... \nYOU LOSE! \n')
        time.sleep(1)
        game = game + 1
        losses = losses + 1
        print('---Score---\n[game]:', game, '\n[wins]:', wins, '\n[losses]:', losses, '\n')
        time.sleep(1)
        continue

    if user_sel == '1' and opp_sel == 'scissors':
        time.sleep(1)
        print('\nopponent selects scissors... \nYOU WIN! \n')
        time.sleep(1)
        game = game + 1
        wins = wins + 1
        print('---Score---\n[game]:', game, '\n[wins]:', wins, '\n[losses]:', losses, '\n')
        time.sleep(1)
        continue
#Paper
    if user_sel == '2' and opp_sel == 'rock':
        time.sleep(1)
        print('\nopponent selects rock... \nYOU WIN! \n')
        time.sleep(1)
        game = game + 1
        wins = wins + 1
        print('---Score---\n[game]:', game, '\n[wins]:', wins, '\n[losses]:', losses, '\n')
        time.sleep(1)
        continue

    if user_sel == '2' and opp_sel == 'paper':
        time.sleep(1)
        print('\nopponent selects paper... \nDRAW! \n')
        time.sleep(1)
        game = game + 1
        print('---Score---\n[game]:', game, '\n[wins]:', wins, '\n[losses]:', losses, '\n')
        time.sleep(1)
        continue

    if user_sel == '2' and opp_sel == 'scissors':
        time.sleep(1)
        print('\nopponent selects scissors... \nYOU LOSE! \n')
        time.sleep(1)
        game = game + 1
        losses = losses + 1
        print('---Score---\n[game]:', game, '\n[wins]:', wins, '\n[losses]:', losses, '\n')
        time.sleep(1)
        continue
#Scissors
    if user_sel == '3' and opp_sel == 'rock':
        time.sleep(1)
        print('\nopponent selects rock... \nYOU LOSE! \n')
        time.sleep(1)
        game = game + 1
        losses = losses + 1
        print('---Score---\n[game]:', game, '\n[wins]:', wins, '\n[losses]:', losses, '\n')
        time.sleep(1)
        continue

    if user_sel == '3' and opp_sel == 'paper':
        time.sleep(1)
        print('\nopponent selects paper... \nYOU WIN! \n')
        time.sleep(1)
        game = game + 1
        wins = wins + 1
        print('---Score---\n[game]:', game, '\n[wins]:', wins, '\n[losses]:', losses, '\n')
        time.sleep(1)
        continue

    if user_sel == '3' and opp_sel == 'scissors':
        time.sleep(1)
        print('\nopponent selects scissors... \nDRAW! \n')
        time.sleep(1)
        game = game + 1
        print('---Score---\n[game]:', game, '\n[wins]:', wins, '\n[losses]:', losses, '\n')
        time.sleep(1)
        continue
#Quit
    if user_sel == 'quit': quit()
#Input Error
    if not user_sel == '1' or '2' or '3':
        print('\ninvalid input, try again...\n')
        continue
