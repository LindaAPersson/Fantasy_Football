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
    print('Write the rules XXXX and  \n')
    reday_to_start = input('are you reday to start the game? y/n \n')
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

def choose_training():
    choose_training = input ('1. Strenght \n2. Endurance \n')

    if choose_training == '1':
        training_strenght(player_name)
    elif choose_training == '2':
        training_endurance(player_name)
    else:
        print('wrong character, please try again')
        choose_training()
        
def training_strenght(player_name):
    """
    Runs when the users choose strenght in start_game
    """
    print(f"All forms of training are essential, but {player_name} has a special passion to build muscles")
    print("Seeing oneself become stronger and stronger is very satisfying")
    print(f"Also, {player_name} needs the strength on the football field, as {player_name} plays as:")
    choose_position_one()

def training_endurance(player_name):
    """
    Runs when the users choose endurance in start_game
    """
    print(f"All forms of training are important, but {player_name} has a special passion for endurance")
    print(f"Being able to run both more and longer than opponents makes {player_name} stand out")
    print(f"especially in the last quarter of a football match! This is crucial as {player_name} plays as:")
    choose_position_two()

def choose_position_one():
    """
    Runs the options from the function training_strenght
    """
    choose_position_one = input('1. Goalkeeper\n2. Defender\n')
    if choose_position_one == '1':
        goalkeeper()
    elif  choose_position_one == '2':
        defender()
    else:
        print('wrong character, please try again')
        choose_position_one()

def choose_position_two():
    """
    Runs the options from the function training_endurance
    """
    choose_position_two = input ('1. Striker\n2. Midfielder\n')
    if choose_position_two == '1':
        striker()
    elif choose_position_two == '2':
        midfielder()
    else:
        print('wrong character, please try again')
        choose_position_two()
    

def goalkeeper():
    print('goalkeeper')

def defender():
    print('defender')

def striker():
    print('striker')

def midfielder():
    print('midfielder') 

def main():
    """
    starts the first function
    """
    game_intro()
    choose_game_rules()
    game_rules()
    choose_name()
    player_name = choose_name()
    start_game(player_name)
    choose_training()
    training_strenght(player_name)
    training_endurance(player_name)
    choose_position_one(player_name)



game_intro()
