def game_intro():
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
    print(f"But {player_name} trains every day to progress further and what {player_name} enjoys training the most is")
    choose_training(player_name)

def choose_training(player_name):
    choose_training_option = input('choose 1 or 2:\n1. Strength \n2. Endurance \n')
    if choose_training_option == '1':
        training_strength(player_name)
    elif choose_training_option == '2':
        training_endurance(player_name)
    else:
        print('Wrong choice, please try again')
        choose_training(player_name)
        
def training_strength(player_name):
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
    choose_position_one_options = input('1. Goalkeeper\n2. Defender\n')
    if choose_position_one_options == '1':
        goalkeeper(player_name)
    elif  choose_position_one_options == '2':
        defender(player_name)
    else:
        print('wrong character, please try again')
        choose_position_one(player_name)

def choose_position_two(player_name):
    """
    Runs the options from the function training_endurance
    """
    choose_position_two_options = input ('1. Striker\n2. Midfielder\n')
    if choose_position_two_options == '1':
        striker(player_name)
    elif choose_position_two_options == '2':
        midfielder(player_name)
    else:
        print('wrong character, please try again')
        choose_position_two(player_name)
    

def goalkeeper(player_name):
    """
    Runs when the users choose goalkeeper in choose_position_one
    """
    print('Being a goalkeeper is a vulnerable position, noticeable immediately when making a mistake')
    print('The competition is also higher since only one goalkeeper is needed on the field')
    print(f"However, all the effort pays off when, after just two seasons, {player_name} gets recruited by:")
    drafted_one()

def defender(player_name):
    """
    Runs when the users choose defender in choose_position_one
    """
    print('Being a defender is a demanding and physical position!')
    print(f"{player_name} fights and works hard every match and training session to improve and learn from mistakes")
    print(f"After two seasons with GIF Sundsvall, all the hard work pays off, and {player_name} gets recruited by:")
    drafted_two()

def striker(player_name):
    """
    Runs when the users choose striker in choose_position_two
    """
    print(f"Endurance is crucial for a striker, it involves constant starts and rushes, and {player_name} loves it!")
    print(f"Thanks to {player_name} diligent training, the first season with GIF Sundsvall goes extremely well!")
    print('So well that NAME gets recruited by:')
    drafted_three()

def midfielder(player_name):
    """
    Runs when the users choose midfielder in choose_position_two
    """
    print(f"As a playmaker, endurance is essential, and luckily {player_name} loves to run!") 
    print(f"{player_name} runs so much that after just one season with GIF Sundsvall, two major teams express interest in recruiting {player_name}.")
    print(f"{player_name} goes to:")
    drafted_four()

def drafted_one(player_name):
    """
    Runs the options from the function goalkeeper
    """
    drafted_one_options = input ('1. Halmstad BK \n2. Örebro \n')
    if drafted_one_options == '1':
        team_halmstad(player_name)
    elif drafted_one_options == '2':
        team_orebro(player_name)
    else:
        print('wrong character, please try again')
        drafted_one(player_name)

def drafted_two(player_name):
    """
    Runs the options from the function defender
    """
    drafted_two_options = input('1. Malmö FF \n2. Elfsborg \n')
    if drafted_two_options == '1':
        team_malmo(player_name)
    elif drafted_two_options == '2':
        team_elfsborg(player_name)
    else:
        print('wrong character, please try again')
        drafted_two(player_name)

def drafted_three(player_name):
    """
    Runs the options from the function striker
    """
    drafted_three_options = input('1. IK Sirius \n2. IFK Göteborg \n')
    if drafted_three_options == '1':
        team_sirius(player_name)
    elif drafted_three_options == '2':
        team_goteborg(player_name)
    else:
        print('wrong character, please try again')
        drafted_three(player_name)

def drafted_four(player_name):
    """
    Runs the options from the function midfielder
    """
    drafted_four_options = input('1. AIK \n2. Djurgården IF \n')
    if drafted_four_options == '1':
        team_aik(player_name)
    elif drafted_four_options == '2':
        team_djurgarden(player_name)
    else:
        print('wrong character, please try again')
        drafted_four(player_name)

def team_halmstad(player_name):
    """
    Runs when the users choose Halmstad in drafted_one
    """
    print(f"Halmstad is a stable mid-table team in need of a goalkeeper, and {player_name} quickly makes a name for themselves in both the club and the city.")
    print(f"The matches go on, {player_name} performs well, and the team does okay but never rises above mid-table.")
    print(f"{player_name} stays for five seasons before a knee injury ends their playing career.")
    print(f"{player_name} decides to become:")
    next_step_one(player_name)

def team_orebro(player_name):
    """
    Runs when the users choose Örebro in drafted_one
    """
    print(f"{player_name} enjoys playing in Örebro; the team, atmosphere, and coach are good.")
    print(f"The team is a mid-table one, fighting for every point, and {player_name} enjoys it.")
    print(f"{player_name} has an okay first season, followed by good second and third seasons.")
    print(f"However, after three seasons, Örebro needs to sell {player_name} for financial reasons.")
    print(f"{player_name} receives offers from two clubs and chooses to go to:")
    next_step_two(player_name)

def team_malmo(player_name):
     """
    Runs when the users choose Malmö in drafted_two
    """
    print(f"Malmö performs well, but {player_name} struggles to make a name for themselves on the field.")
    print(f"{player_name} gets limited playing time and isn't a regular player after the first season.")
    print(f"However, {player_name} improves during the second season, becoming a solid starter.")
    print(f"After four seasons with Malmö, NAME gets recruited by:")
    next_step_three()

def team_elfsborg(player_name):
    print('elfsborg')

def team_sirius(player_name):
    print('sirius')

def team_goteborg(player_name):
    print('göteborg')

def team_aik(player_name):
    print('aik')

def team_djurgarden(player_name):
    print('Djurgården')

def next_step_one(player_name):
    """
    Runs the options from the function team_halmstad
    """
    next_step_one_options = input('1. Coach for u-21 \n2. Goalkeeper coach \n')
    if next_step_one_options = '1':
        youth_coach(player_name)
    elif next_step_one_options = '2':
        goalkeeper_coach(player_name)
    else: 
        print('wrong character, please try again')
        next_step_one(player_name)

def next_step_two(player_name):
    """
    Runs the options from the function team_orebro
    """
    next_step_two_options = input('1. Milan \n2. Fullham \n')
    if next_step_two_options == '1':
        team_milan(player_name)
    elif next_step_two_options == '2':
        team_fullham(player_name)
    else:
        print('wrong character, please try again')
        next_step_two(player_name)

def next_step_three(player_name):
    """
    Runs the options from the function team_malmo
    """
    next_step_three_options = input('1. Leeds \n2. Copenhagen \n')
    if next_step_three_options = '1':
        team_leeds(player_name)
    elif next_step_three_options = '2':
        team_copenhagen(player_name)
    else:
        print('wrong character, please try again')
        next_step_three(player_name)


def youth_coach(player_name):
    print('juniortränare')

def goalkeeper_coach(player_name):
    print('goal coach')

def team_milan(player_name):
    print('milan')

def team_fullham(player_name):
    print('fulllham')

def team_leeds(player_name):
    print('leeds')

def team_copenhagen(player_name):
    print('copehagen')



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
