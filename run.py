"""
import section
"""
from termcolor import colored

player_name = ''

def game_intro():
    """
    Run games intro
    """
    print(colored(('Welcomme Welcome to Fantasy Football!'), 'green')) 
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
    if chose_game_rules.lower() == 'y':
        game_rules()
    elif chose_game_rules.lower() == 'n':
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
    if reday_to_start.lower() == 'y':
        choose_name()
    elif reday_to_start.lower() == 'n':
        print('To bad, maybe next time')
        game_intro ()
    else:
        print('wrong character, please try again')
        game_rules()


def choose_name():
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
        print('Wrong choice, please try again')
        choose_training()
        
def training_strength():
    """
    Runs when the users choose strenght in start_game
    """
    player_name
    print(f"All forms of training are essential, but {player_name} has a special passion to build muscles")
    print("Seeing oneself become stronger and stronger is very satisfying")
    print(f"Also, {player_name} needs the strength on the football field, as {player_name} plays as:")
    choose_position_one()

def training_endurance():
    """
    Runs when the users choose endurance in start_game
    """
    player_name
    print(f"All forms of training are important, but {player_name} has a special passion for endurance")
    print(f"Being able to run both more and longer than opponents makes {player_name} stand out")
    print(f"especially in the last quarter of a football match! This is crucial as {player_name} plays as:")
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
        print('wrong character, please try again')
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
        print('wrong character, please try again')
        choose_position_two()

def goalkeeper():
    """
    Runs when the users choose goalkeeper in choose_position_one
    """
    player_name
    print('Being a goalkeeper is a vulnerable position, noticeable immediately when making a mistake')
    print('The competition is also higher since only one goalkeeper is needed on the field')
    print(f"However, all the effort pays off when, after just two seasons, {player_name} gets recruited by:")
    drafted_one()

def defender():
    """
    Runs when the users choose defender in choose_position_one
    """
    player_name
    print('Being a defender is a demanding and physical position!')
    print(f"{player_name} fights and works hard every match and training session to improve and learn from mistakes")
    print(f"After two seasons with GIF Sundsvall, all the hard work pays off, and {player_name} gets recruited by:")
    drafted_two()

def striker():
    """
    Runs when the users choose striker in choose_position_two
    """
    player_name
    print(f"Endurance is crucial for a striker, it involves constant starts and rushes, and {player_name} loves it!")
    print(f"Thanks to {player_name} diligent training, the first season with GIF Sundsvall goes extremely well!")
    print('So well that NAME gets recruited by:')
    drafted_three()

def midfielder():
    """
    Runs when the users choose midfielder in choose_position_two
    """
    player_name
    print(f"As a playmaker, endurance is essential, and luckily {player_name} loves to run!") 
    print(f"{player_name} runs so much that after just one season with GIF Sundsvall, two major teams express interest in recruiting {player_name}.")
    print(f"{player_name} goes to:")
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
        print('wrong character, please try again')
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
        print('wrong character, please try again')
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
        print('wrong character, please try again')
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
        print('wrong character, please try again')
        drafted_four()

def team_halmstad():
    """
    Runs when the users choose Halmstad in drafted_one
    """
    player_name
    print(f"Halmstad is a stable mid-table team in need of a goalkeeper, and {player_name} quickly makes a name for themselves in both the club and the city.")
    print(f"The matches go on, {player_name} performs well, and the team does okay but never rises above mid-table.")
    print(f"{player_name} stays for five seasons before a knee injury ends their playing career.")
    print(f"{player_name} decides to become:")
    next_step_one()

def team_orebro():
    """
    Runs when the users choose Örebro in drafted_one
    """
    player_name
    print(f"Örebro has an experienced goalkeeper, so {player_name} doesn't get many minutes on the field.")
    print(f"{player_name} plays in smaller cups and less critical matches, performing well but still not getting a spot in the first team.")
    print(f"However, before the derby, the regular goalkeeper falls ill, giving {player_name} a chance.")
    print(f"{player_name} performs exceptionally, making crucial saves, and the team wins!")
    print(f"After that match, NAME gets more playing time, and more clubs express interest. NAME stays for three seasons before finally moving to")
    next_step_two()

def team_malmo():
    """
    Runs when the users choose Malmö in drafted_two
    """
    player_name
    print(f"Malmö performs well, but {player_name} struggles to make a name for themselves on the field.")
    print(f"{player_name} gets limited playing time and isn't a regular player after the first season.")
    print(f"However, {player_name} improves during the second season, becoming a solid starter.")
    print(f"After four seasons with Malmö, NAME gets recruited by:")
    next_step_three()

def team_elfsborg():
    """
    Runs when the users choose Elfsborg in drafted_two
    """
    player_name
    print(f"{player_name} fits into Elfsborg quickly and effectively.")
    print(f"After just one season, {player_name} has already made a name for themselves in the entire league.")
    print(f"The future looks bright, but then the unexpected happens – during a collision, {player_name} breaks their ankle.")
    print(f"After surgery and rehab, it's clear that {player_name} won't be able to come back as an elite player.")
    print(f"{player_name} decides to pursue a career as:")
    next_step_four()

def team_sirius():
    """
    Runs when the users choose IK Sirius in drafted_three
    """
    player_name
    print(f"{player_name} absolutely loves playing for Sirius! The team feels like home immediately, and {player_name} gains significant trust.")
    print(f"In the second season, {player_name} wins the top scorer title and is offered a contract with:")
    next_step_five()

def team_goteborg():
    """
    Runs when the users choose IFK Göteborg in drafted_three
    """
    player_name
    print(f"{player_name} enjoys playing in Göteborg; the team, atmosphere, and coach are good.")
    print(f"The team is a mid-table one, fighting for every point, and {player_name} enjoys it.")
    print(f"{player_name} has an okay first season, followed by good second and third seasons.")
    print(f"However, after three seasons, Örebro needs to sell {player_name} for financial reasons.")
    print(f"{player_name} receives offers from two clubs and chooses to go to:")
    next_step_six(player_name)

def team_aik():
    """
    Runs when the users choose AIK in drafted_four
    """
    player_name
    print(f"The first season with AIK is challenging. {player_name} keeps on fighting, but things don't go well for the team.")
    print(f"Midway through the season, the coach is fired.")
    print(f"The new coach recognizes {player_name}´s potential, resulting in more playing time and attention.")
    print(f"The team finishes at the bottom, but {player_name} receives offers from:")
    next_step_seven()

def team_djurgarden():
    """
    Runs when the users choose Djurgården IF in drafted_four
    """
    player_name
    print(f"It's challenging for {player_name} to break into a highly performing Malmö team.")
    print(f"The team tops the league and has stable midfielders. {player_name} keeps fighting and continues focusing on endurance.")
    print(f"After two seasons, playing time increases, and after four seasons, {player_name} becomes a seasoned and reliable starter.")
    print(f"fter six seasons with Malmö, {player_name} is recruited by:")
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
        print('wrong character, please try again')
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
        print('wrong character, please try again')
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
        print('wrong character, please try again')
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
        print('wrong character, please try again')
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
        print('wrong character, please try again')
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
        print('wrong character, please try again')
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
        print('wrong character, please try again')
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
        print('wrong character, please try again')
        next_step_eight()

def youth_coach():
    """
    Runs when user choose Coach for u-21 in next_step_one
    """
    player_name
    print(f"{player_name} starts their coaching career with hometown club GIF Sundsvall but quickly advances")
    print(f"After five seasons, {player_name} receives an offer to become the national team coach for the U-21 national team.")
    print(f"{player_name} accepts and manages to win the U-21 European Championship.")
    end_game()

def goalkeeper_coach():
    """
    Runs when user choose Goalkeeper coach in next_step_one
    """
    player_name
    print('Text about goalkeeper coach')
    end_game()

def team_milan():
    """
    Runs when user choose Milan in next_step_two
    """
    player_name
    print('Text about milan')
    end_game()

def team_fullham():
    """
    Runs when user choose Fullham in next_step_three
    """
    player_name
    print('Text about fulllham')
    end_game()

def team_leeds():
    """
    Runs when user choose Leeds in next_step_three
    """
    player_name
    print(f"{player_name} initially struggles in the English league, but after two seasons, physicality and playing time increase.")
    print(f"{player_name} performs well and stays with the club for a remarkable nine seasons.")
    end_game()

def team_copenhagen():
    """
    Runs when user choose Copenhagen in next_step_three
    """
    player_name
    print(f"Things go well for {player_name} in FC Copenhagen, and after two seasons, the team plays in the Champions League.")
    print("Even though the Danish league doesn't have the same standard, it becomes a good advertising window.")
    print(f"After these matches, more top clubs show interest in {player_name}.")
    end_game()

def coach():
    """
    Runs when user choose coach in next_step_four
    """
    player_name
    print('Text about coach')
    end_game()

def junior_coach():
    """
    Runs when user choose Coach for minors in next_step_four
    """
    player_name
    print('Text about coach - junior')
    end_game()

def team_roma():
    """
    Runs when user choose Roma in next_step_five
    """
    player_name
    print('Text about roma')
    end_game()

def team_inter():
    """
    Runs when user choose Inter in next_step_five
    """
    player_name
    print('Text about inter')
    end_game()

def team_westham():
    """
    Runs when user choose Westham in next_step_six
    """
    player_name
    print(f"{player_name} falls out of favor with supporters after a heavy derby loss.")
    print(f"The conflict escalates to the point where {player_name} is benched.")
    print(f"{player_name} is forced to change teams after just one year, returning to IFK Göteborg.")
    end_game()

def team_manchester():
    """
    Runs when user choose manchester united in next_step_six
    """
    player_name
    print(f"{player_name} has to fight their way into the team but gains more and more trust, playing in more critical matches.")
    print(f"{player_name} plays four seasons with Manchester United, and one of those seasons results in winning the Champions League!")
    end_game()

def team_ajax():
    """
    Runs when user choose ajax in next_step_seven
    """
    player_name
    print(f"{player_name} gains significant trust from the coach immediately.")
    print(f"{player_name} plays well, adapts to the pace and playing style right away.")
    print(f"When the coach gets a new contract with Liverpool FC, he takes {player_name} with him!")
    end_game()

def team_lissabon():
    """
    Runs when user choose Lissabon in next_step_seven
    """
    player_name
    print(f"{player_name} makes a very good first impression, and both the coach and supporters see {player_name} as the team's star player after the first season")
    print("Sporting Lisbon even wins the Europa League one year.")
    end_game()

def team_newcastle():
    """
    Runs when user choose newcastle in next_step_eight
    """
    player_name
    print('Text about newcaste')
    end_game()

def team_stoke():
    """
    Runs when user choose stoke in next_step_eight
    """
    player_name
    print('Text about stoke')
    end_game()

def end_game():
    print('Thanks for playing! XXXX PLAY AGAIN?')
    play_again = input('Do you want to play again? y/n\n')
    if play_again.lower() == 'y':
        choose_game_rules()
    elif play_again.lower() == 'n':
        print('To bad, bye until next time')
        game_intro()
    else:
        print('wrong character, please try again')
        end_game()
 

def main():
    """
    starts the first function
    """
    game_intro()
    """choose_game_rules()
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
    drafted_one()"""

main()
