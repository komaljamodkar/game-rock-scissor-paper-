import random
def game_rules(play1Input, play2Input):
    if play1Input == play2Input:
        return 0
    elif play1Input == 'paper' and play2Input == 'scissors':
        return play2Input
    elif play1Input == 'scissors' and play2Input == 'rock':
        return play2Input
    elif play1Input == 'rock' and play2Input == 'paper':
        return play2Input
    else:
        return play1Input

# Check user inputs
def start_game():
    # Player 1: asks input again if entered anything other than rock, paper, scissors
    while True:
        player1 = input('Player 1, You choose rock, paper or scissors?: ')
        if player1 not in ['rock', 'paper', 'scissors']:
            print ("Invalid input. Please try again.")
            continue
        break
        
    # Player 2: asks input again if entered anything other than rock, paper, scissors
    while True:
        player2 = input('Player 2, You choose rock, paper or scissors?: ')
        if player2 not in ['rock', 'paper', 'scissors']:
            print ("Invalid input. Please try again.")
            continue
        break
        
    return game_rules(player1, player2)

# Check user inputs
def start_gamec():
    # Player 1: asks input again if entered anything other than rock, paper, scissors
    while True:
        player1 = input('Player 1, You choose rock, paper or scissors?: ')
        if player1 not in ['rock', 'paper', 'scissors']:
            print ("Invalid input. Please try again.")
            continue
        break
        
    # Player 2: asks input again if entered anything other than rock, paper, scissors
    
    aList = ['rock','paper','scissors']     
    choosen=random.sample(aList, 1)
    player2=''.join(map(str,choosen))
    print("player 2 choose :",player2)
        
    return game_rules(player1, player2)



# Execute game and declare result
while True:
    usr_command = input('Shall we start a new Game? {Y/N}').lower()

    
    # should not type anything other than y OR n, else display error
    if usr_command not in ['y', 'n']:
        print ("Invalid input. Please try again.")
        continue
    
    if usr_command.lower() == 'n':
        print("ok,Thanks..")
        break
    else:
        usr_command = input('Play With computer/user? {C/U}').lower()
        if usr_command not in ['c', 'u']:
            print ("Invalid input. Please try again.")
            continue
    
        elif usr_command.lower() == 'c':
            ret = start_gamec()
        
            if ret == 0:
                print ("It's a tie")
            else:
                print ("Congratulations!", ret, "wins.")
        else:
            ret = start_game()
        
            if ret == 0:
                print ("It's a tie")
            else:
                print ("Congratulations!", ret, "wins.")
