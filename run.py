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
        start_game()
    else:
        print('wrong character, please try again')
        choose_game_rules()

def game_rules():
    """
    The rules of the game/how to play
    """
    print('Write the rules XXXX and are you reday to start the game? y/n \n')
    if chose_game_rules == 'y':
        start_game()
    elif chose_game_rules == 'n':
        print('To bad, maybe next time')
        game_intro ()
    else:
        print('wrong character, please try again')

def start_game():
    """
    Starts the game
    """
    print("Let´s begin!")
    player_name = input(
        'What´s your name fotballplayer? \n'
    )
    print(f"Hello {player_name}, let´s see how long you can go!\n")
    print(f"{player_name} is a young and promising football player who loves and lives for the sport.")
    print(f"Currently, {player_name} is part of a smaller team in Division 1 in Sweden, GIF Sundsvall.")
    print(f"But {player_name} trains every day to progress further and what {player_name} enjoys training the most is (choose 1 or 2):")
    choose_training = input (
        '1. Strenght \n2. Endurance \n'
        )
    if choose_training == '1':
        training_strenght()
    elif choose_training == '2':
        training_endurance()
    else:
        print('wrong character, please try again')
        choose_training()
        
def training_strenght():
    print('styrka funktionen')
def training_endurance():
    print('kondiion functioen')


def main():
    """
    starts the first function
    """
    game_intro()


main()
