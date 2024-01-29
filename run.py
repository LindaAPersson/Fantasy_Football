def game_intro ():
    """
    Run games intro
    """
    print('Welcomme Welcome to Fantasy Football!') 
    print('Do you have what it takes to make it all the way to the Premier League?')
    print('If you make the right decisions, anything is possible!')
    print('Create your player and let the game begin!')
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
    print('start rules')


def start_game():
    print('start game')

def main():
    """
    starts the first function
    """
    game_intro()


main()
