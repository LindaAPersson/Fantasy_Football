def game_intro ():
    """
    Run games intro
    """
    print('Welcomme Welcome to Fantasy Football!') 
    print('Do you have what it takes to make it all the way to the Premier League?')
    print('If you make the right decisions, anything is possible!')
    choose_game_rules()

def choose_game_rules():
    """
    Explainns the rules/ how to play the game
    """
    chose_game_rules = input(
        'But first, do you want to read the rules/ how to play the game? y/n \n'
    )
    if chose_game_rules == 'y':
        game_rules()
    elif chose_game_rules == 'n':
        choose_name()
    else:
        print('wrong character, please try again')
        choose_game_rules()

def game_rules():
    """
    The rules of the game/how to play
    """
    print('Write the rules XXXX and are you reday to start the game? \n')
    reday_to_start = input('y/n \n')
    if reday_to_start == 'y':
        choose_name()
    elif reday_to_start == 'n':
        print('To bad, maybe next time')
        game_intro ()
    else:
        print('wrong character, please try again')
        game_rules()

def choose_name():
    print("Let´s begin!")
    player_name = input(
        'What´s your name fotballplayer? \n'
    )
    start_game(player_name)
    return player_name

def start_game(player_name):
    """
    Starts the game
    """
    print(f"Hello {player_name}, let´s see how long you can go!\n")
    print(f"{player_name} is a young and promising football player who loves and lives for the sport.")
    print(f"Currently, {player_name} is part of a smaller team in Division 1 in Sweden, GIF Sundsvall.")
    print(f"But {player_name} trains every day to progress further and what {player_name} enjoys training the most is (choose 1 or 2):")
    choose_training(player_name)

def choose_training(player_name): 
    choose_training = input (
        '1. Strenght \n2. Endurance \n'
        )
    if choose_training == '1':
        training_strenght(player_name)
    elif choose_training == '2':
        training_endurance(player_name)
    else:
        print('wrong character, please try again')
    choose_training(player_name)
    
        
def training_strenght(player_name):
    """
    Runs when the users choose strenght in start_game
    """
    print('styrka')

def training_endurance(player_name):
    """
    Runs when the users choose endurance in start_game
    """
    print('kondiion functioen')

def main():
    """
    starts the first function
    """
    game_intro()
    player_name = choose_name()
    start_game(player_name)
    choose_training(player_name)
    training_strenght(player_name)
    training_endurance(player_name)



main()
