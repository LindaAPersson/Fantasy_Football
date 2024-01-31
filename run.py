"""
import section
"""
from termcolor import colored
import story

player_name = ''

def game_intro():
    """
    Run games intro
    """
    print(r"""
     o__        o__     |   |\
    /|          /\      |   |X\
    / > o        <\     |   |XX\
    """)
    print(colored('\nWelcomme Welcome to Fantasy Football!\n', 'white', 'on_green', attrs=['bold'])) 
    print('Do you have what it takes to make it all the way to the Premier League?')
    print('If you make the right decisions, anything is possible!\n')
    
    choose_game_rules()


def choose_game_rules():
    """
    Explainns the rules/ how to play the game
    """
    chose_game_rules = input(colored(
        'But first, do you want to read the rules/ how to play the game? y/n \n', 'blue'
    ))
    if chose_game_rules.lower() == 'y':
        game_rules()
    elif chose_game_rules.lower() == 'n':
        choose_name()
    else:
        print(colored('wrong character, please try again', 'red'))
        choose_game_rules()


def game_rules():
    """
    The rules of the game/how to play
    """
    story.rules()
    reday_to_start = input('are you reday to start the game? y/n \n')
    if reday_to_start.lower() == 'y':
        choose_name()
    elif reday_to_start.lower() == 'n':
        print('To bad, maybe next time')
        game_intro ()
    else:
        print(colored('wrong character, please try again', 'red'))
        game_rules()


def choose_name():
    """
    Lets the user choose a name for the player
    """
    print("Let´s begin!")
    global player_name
    choose_player_name = input(
        'What´s your name fotballplayer? \n'
    )
    while not choose_player_name.isalpha():
        print('Input must contain only alphabetic')
        choose_player_name = input(
            'What´s your name fotballplayer? \n'
        )

    player_name = choose_player_name
    start_game()


def start_game():
    """
    Starts the game
    """
    player_name
    print(f"Hello {player_name}, let´s see how long you can go!\n")
    print(f"{player_name} is a young and promising football player who loves and lives for the sport.")
    print(f"Currently, {player_name} is part of a smaller team in Division 1 in Sweden, GIF Sundsvall.")
    print(f"But {player_name} trains every day to progress further and what {player_name} enjoys training the most is")
    choose_training()

def choose_training():
    choose_training_option = input('choose 1 or 2:\n1. Strength \n2. Endurance \n')
    if choose_training_option == '1':
        training_strength()
    elif choose_training_option == '2':
        training_endurance()
    else:
        print(colored('wrong character, please try again', 'red'))
        choose_training()
        
def training_strength():
    """
    Runs when the users choose strenght in start_game
    """
    story.training_strength_story(player_name)
    choose_position_one()

def training_endurance():
    """
    Runs when the users choose endurance in start_game
    """
    story.training_endurance_story(player_name)
    choose_position_two()

def choose_position_one():
    """
    Runs the options from the function training_strenght
    """
    choose_position_one_options = input('1. Goalkeeper\n2. Defender\n')
    if choose_position_one_options == '1':
        goalkeeper()
    elif  choose_position_one_options == '2':
        defender()
    else:
        print(colored('wrong character, please try again', 'red'))
        choose_position_one()

def choose_position_two():
    """
    Runs the options from the function training_endurance
    """
    choose_position_two_options = input ('1. Striker\n2. Midfielder\n')
    if choose_position_two_options == '1':
        striker()
    elif choose_position_two_options == '2':
        midfielder()
    else:
        print(colored('wrong character, please try again', 'red'))
        choose_position_two()

def goalkeeper():
    """
    Runs when the users choose goalkeeper in choose_position_one
    """
    story.goalkeeper_story(player_name)
    drafted_one()

def defender():
    """
    Runs when the users choose defender in choose_position_one
    """
    story.defender_story(player_name)
    drafted_two()

def striker():
    """
    Runs when the users choose striker in choose_position_two
    """
    story.striker_story(player_name)
    drafted_three()

def midfielder():
    """
    Runs when the users choose midfielder in choose_position_two
    """
    story.midfielder_story(player_name)
    drafted_four()

def drafted_one():
    """
    Runs the options from the function goalkeeper
    """
    drafted_one_options = input ('1. Halmstad BK \n2. Örebro \n')
    if drafted_one_options == '1':
        team_halmstad()
    elif drafted_one_options == '2':
        team_orebro()
    else:
        print(colored('wrong character, please try again', 'red'))
        drafted_one()

def drafted_two():
    """
    Runs the options from the function defender
    """
    drafted_two_options = input('1. Malmö FF \n2. Elfsborg \n')
    if drafted_two_options == '1':
        team_malmo()
    elif drafted_two_options == '2':
        team_elfsborg()
    else:
        print(colored('wrong character, please try again', 'red'))
        drafted_two()

def drafted_three():
    """
    Runs the options from the function striker
    """
    drafted_three_options = input('1. IK Sirius \n2. IFK Göteborg \n')
    if drafted_three_options == '1':
        team_sirius()
    elif drafted_three_options == '2':
        team_goteborg()
    else:
        print(colored('wrong character, please try again', 'red'))
        drafted_three()

def drafted_four():
    """
    Runs the options from the function midfielder
    """
    drafted_four_options = input('1. AIK \n2. Djurgården IF \n')
    if drafted_four_options == '1':
        team_aik()
    elif drafted_four_options == '2':
        team_djurgarden()
    else:
        print(colored('wrong character, please try again', 'red'))
        drafted_four()

def team_halmstad():
    """
    Runs when the users choose Halmstad in drafted_one
    """
    story.team_halmstad_story(player_name)
    next_step_one()

def team_orebro():
    """
    Runs when the users choose Örebro in drafted_one
    """
    story.team_orebro_story(player_name)
    next_step_two()

def team_malmo():
    """
    Runs when the users choose Malmö in drafted_two
    """
    story.team_malmo_story(player_name)
    next_step_three()

def team_elfsborg():
    """
    Runs when the users choose Elfsborg in drafted_two
    """
    story.team_elfsborg_story(player_name)
    next_step_four()

def team_sirius():
    """
    Runs when the users choose IK Sirius in drafted_three
    """
    story.team_sirius_story(player_name)
    next_step_five()

def team_goteborg():
    """
    Runs when the users choose IFK Göteborg in drafted_three
    """
    story.team_goteborg_story(player_name)
    next_step_six()

def team_aik():
    """
    Runs when the users choose AIK in drafted_four
    """
    story.team_aik_story(player_name)
    next_step_seven()

def team_djurgarden():
    """
    Runs when the users choose Djurgården IF in drafted_four
    """
    story.team_djurgarden_story(player_name)
    next_step_eight()

def next_step_one():
    """
    Runs the options from the function team_halmstad
    """
    next_step_one_options = input('1. Coach for u-21 \n2. Goalkeeper coach \n')
    if next_step_one_options == '1':
        youth_coach()
    elif next_step_one_options == '2':
        goalkeeper_coach()
    else: 
        print(colored('wrong character, please try again', 'red'))
        next_step_one()

def next_step_two():
    """
    Runs the options from the function team_orebro
    """
    next_step_two_options = input('1. Milan \n2. Fullham \n')
    if next_step_two_options == '1':
        team_milan()
    elif next_step_two_options == '2':
        team_fullham()
    else:
        print(colored('wrong character, please try again', 'red'))
        next_step_two()

def next_step_three():
    """
    Runs the options from the function team_malmo
    """
    next_step_three_options = input('1. Leeds \n2. Copenhagen \n')
    if next_step_three_options == '1':
        team_leeds()
    elif next_step_three_options == '2':
        team_copenhagen()
    else:
        print(colored('wrong character, please try again', 'red'))
        next_step_three()

def next_step_four():
    """
    Runs the options from the function team_elfsborg
    """
    next_step_four_options = input('1. Coach \n2. Coach for minors \n')
    if next_step_four_options == '1':
        coach()
    elif next_step_four_options == '2':
        junior_coach()
    else:
        print(colored('wrong character, please try again', 'red'))
        next_step_four()

def next_step_five():
    """
    Runs the options from the function team_sirus
    """
    next_step_five_options = input('1. Roma \n2. Inter \n')
    if next_step_five_options == '1':
        team_roma()
    elif next_step_five_options == '2':
        team_inter()
    else:
        print(colored('wrong character, please try again', 'red'))
        next_step_five()

def next_step_six():
    """
    Runs the options from the function team_goteborg
    """
    next_step_six_options = input('1. Westham United \n2. Manchester United \n')
    if next_step_six_options == '1':
        team_westham()
    elif next_step_six_options == '2':
        team_manchester()
    else:
        print(colored('wrong character, please try again', 'red'))
        next_step_six()

def next_step_seven():
    """
    Runs the options from the function AIK
    """
    next_step_seven_options = input('1. Ajax \n2. lissabon \n')
    if next_step_seven_options == '1':
        team_ajax()
    elif next_step_seven_options == '2':
        team_lissabon()
    else:
        print(colored('wrong character, please try again', 'red'))
        next_step_seven()

def next_step_eight():
    """
    Runs the options from the function djurgarden
    """
    next_step_eight_options = input('1. Newcastle United \n2. Stoke \n')
    if next_step_eight_options == '1':
        team_newcastle()
    elif next_step_eight_options == '2':
        team_stoke()
    else:
        print(colored('wrong character, please try again', 'red'))
        next_step_eight()

def youth_coach():
    """
    Runs when user choose Coach for u-21 in next_step_one
    """
    story.youth_coach_story(player_name)
    end_game()

def goalkeeper_coach():
    """
    Runs when user choose Goalkeeper coach in next_step_one
    """
    story.goalkeeper_coach_story(player_name)
    end_game()

def team_milan():
    """
    Runs when user choose Milan in next_step_two
    """
    story.team_milan_story(player_name)
    end_game()

def team_fullham():
    """
    Runs when user choose Fullham in next_step_three
    """
    story.team_fullham_story(player_name)
    end_game()

def team_leeds():
    """
    Runs when user choose Leeds in next_step_three
    """
    story.team_leeds_story(player_name)
    end_game()

def team_copenhagen():
    """
    Runs when user choose Copenhagen in next_step_three
    """
    story.team_copenhagen_story(player_name)
    end_game()

def coach():
    """
    Runs when user choose coach in next_step_four
    """
    story.coach_story(player_name)
    end_game()

def junior_coach():
    """
    Runs when user choose Coach for minors in next_step_four
    """
    story.junior_coach_story(player_name)
    end_game()

def team_roma():
    """
    Runs when user choose Roma in next_step_five
    """
    story.team_roma_story(player_name)
    end_game()

def team_inter():
    """
    Runs when user choose Inter in next_step_five
    """
    story.team_inter_story(player_name)
    end_game()

def team_westham():
    """
    Runs when user choose Westham in next_step_six
    """
    story.team_westham_story(player_name)
    end_game()

def team_manchester():
    """
    Runs when user choose manchester united in next_step_six
    """
    story.team_manchester_story(player_name)
    end_game()

def team_ajax():
    """
    Runs when user choose ajax in next_step_seven
    """
    story.team_ajax_story(player_name)
    end_game()

def team_lissabon():
    """
    Runs when user choose Lissabon in next_step_seven
    """
    story.team_lissabon_story(player_name)
    end_game()

def team_newcastle():
    """
    Runs when user choose newcastle in next_step_eight
    """
    story.team_newcastle_story(player_name)
    end_game()

def team_stoke():
    """
    Runs when user choose stoke in next_step_eight
    """
    story.team_stoke_story(player_name)
    end_game()

def end_game():
    print('Thanks for playing!')
    play_again = input('Do you want to play again? y/n\n')
    if play_again.lower() == 'y':
        choose_game_rules()
    elif play_again.lower() == 'n':
        print('To bad, bye until next time')
        game_intro()
    else:
        print(colored('wrong character, please try again', 'red'))
        end_game()
 

def main():
    """
    starts the first function
    """
    game_intro()
    start_game()
    """choose_game_rules()
    game_rules()
    choose_name()
    player_name = choose_name()
    
    choose_training()
    training_strenght(player_name)
    training_endurance(player_name)
    choose_position_one()
    choose_position_two()
    goalkeeper(player_name)
    defender(player_name)
    striker(player_name)
    midfielder(player_name)
    drafted_one()"""

main()
