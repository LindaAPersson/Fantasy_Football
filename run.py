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

def choose_training(player_name):
    choose_training = input ('1. Strenght \n2. Endurance \n')

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
    print(f"All forms of training are essential, but {player_name} has a special passion to build muscles")
    print("Seeing oneself become stronger and stronger is very satisfying")
    print(f"Also, {player_name} needs the strength on the football field, as {player_name} plays as:")
    choose_position_one(player_name)

def training_endurance(player_name):
    """
    Runs when the users choose endurance in start_game
    """
    print(f"All forms of training are important, but {player_name} has a special passion for endurance")
    print(f"Being able to run both more and longer than opponents makes {player_name} stand out")
    print(f"especially in the last quarter of a football match! This is crucial as {player_name} plays as:")
    choose_position_two(player_name)

def choose_position_one(player_name):
    """
    Runs the options from the function training_strenght
    """
    choose_position_one = input('1. Goalkeeper\n2. Defender\n')
    if choose_position_one == '1':
        goalkeeper(player_name)
    elif  choose_position_one == '2':
        defender(player_name)
    else:
        print('wrong character, please try again')
        choose_position_one()

def choose_position_two(player_name):
    """
    Runs the options from the function training_endurance
    """
    choose_position_two = input ('1. Striker\n2. Midfielder\n')
    if choose_position_two == '1':
        striker(player_name)
    elif choose_position_two == '2':
        midfielder(player_name)
    else:
        print('wrong character, please try again')
        choose_position_two(player_name)
    

def goalkeeper(player_name):
    print('Being a goalkeeper is a vulnerable position, noticeable immediately when making a mistake')
    print('The competition is also higher since only one goalkeeper is needed on the field')
    print(f"However, all the effort pays off when, after just two seasons, {player_name} gets recruited by:")
    drafted_one()

def defender(player_name):
    print('defender')

def striker(player_name):
    print('striker')

def midfielder(player_name):
    print('midfielder') 

def drafted_one():
    drafted_one = input ('1. Halmstad BK \n2. Örebro \n')
    if drafted_one == '1':
        team_halmstad()
    elif drafted_one == '2':
        team_orebro()
    else:
        print('wrong character, please try again')
        drafted_one()



def team_halmstad():
    print('halmstad')

def team_orebro():
    print('örebro')

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
    choose_position_one()
    choose_position_two()
    goalkeeper(player_name)
    defender(player_name)
    striker(player_name)
    midfielder(player_name)
    drafted_one()



game_intro()
