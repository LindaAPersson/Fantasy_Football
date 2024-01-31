# the text in the game
#import section 
from termcolor import colored, cprint
import effect 

def rules():
    effect.slow(
        "\nHow to you play!\n" 
        'All instructions are in the game.\n'
        'For yes and no questions, just respond with y or n and press enter.\n'
        'When entering your name, you can write whatever you want, but it should only consist of letters.\n'
        'When choosing your career path, just respond with 1 or 2, and press enter\n'
        'Have fun and good luck!\n'
    )

def training_strength_story(player_name):
    """
    Runs the story when the users choose strenght in start_game
    """
    print(f"All forms of training are essential, but {player_name} has a special passion to build muscles")
    print("Seeing oneself become stronger and stronger is very satisfying")
    print(f"Also, {player_name} needs the strength on the football field, as {player_name} plays as:")

def training_endurance_story(player_name):
    """
    Runs the story when the users choose endurance in start_game
    """
    print(f"All forms of training are important, but {player_name} has a special passion for endurance")
    print(f"Being able to run both more and longer than opponents makes {player_name} stand out")
    print(f"especially in the last quarter of a football match! This is crucial as {player_name} plays as:")

def goalkeeper_story(player_name):
    """
    Runs the story when the users choose goalkeeper in choose_position_one
    """
    print('Being a goalkeeper is a vulnerable position, noticeable immediately when making a mistake')
    print('The competition is also higher since only one goalkeeper is needed on the field')
    print(f"However, all the effort pays off when, after just two seasons, {player_name} gets recruited by:")

def defender_story(player_name):
    """
    Runs the story when the users choose defender in choose_position_one
    """
    print('Being a defender is a demanding and physical position!')
    print(f"{player_name} fights and works hard every match and training session to improve and learn from mistakes")
    print(f"After two seasons with GIF Sundsvall, all the hard work pays off, and {player_name} gets recruited by:")

def striker_story(player_name):
    """
    Runs the story when the users choose striker in choose_position_two
    """
    print(f"Endurance is crucial for a striker, it involves constant starts and rushes, and {player_name} loves it!")
    print(f"Thanks to {player_name} diligent training, the first season with GIF Sundsvall goes extremely well!")
    print('So well that NAME gets recruited by:')

def midfielder_story(player_name):
    """
    Runs the story when the users choose midfielder in choose_position_two
    """
    print(f"As a playmaker, endurance is essential, and luckily {player_name} loves to run!") 
    print(f"{player_name} runs so much that after just one season with GIF Sundsvall, two major teams express interest in recruiting {player_name}.")
    print(f"{player_name} goes to:")

def team_halmstad_story(player_name):
    """
    Runs the stry when the users choose Halmstad in drafted_one
    """
    print(f"Halmstad is a stable mid-table team in need of a goalkeeper, and {player_name} quickly makes a name for themselves in both the club and the city.")
    print(f"The matches go on, {player_name} performs well, and the team does okay but never rises above mid-table.")
    print(f"{player_name} stays for five seasons before a knee injury ends their playing career.")
    print(f"{player_name} decides to become:")

def team_orebro_story(player_name):
    """
    Runs the story when the users choose Örebro in drafted_one
    """
    print(f"Örebro has an experienced goalkeeper, so {player_name} doesn't get many minutes on the field.")
    print(f"{player_name} plays in smaller cups and less critical matches, performing well but still not getting a spot in the first team.")
    print(f"However, before the derby, the regular goalkeeper falls ill, giving {player_name} a chance.")
    print(f"{player_name} performs exceptionally, making crucial saves, and the team wins!")
    print(f"After that match, {player_name} gets more playing time, and more clubs express interest. {player_name} stays for three seasons before finally moving to")

def team_malmo_story(player_name):
    """
    Runs the story when the users choose Malmö in drafted_two
    """
    print(f"Malmö performs well, but {player_name} struggles to make a name for themselves on the field.")
    print(f"{player_name} gets limited playing time and isn't a regular player after the first season.")
    print(f"However, {player_name} improves during the second season, becoming a solid starter.")
    print(f"After four seasons with Malmö, NAME gets recruited by:")

def team_elfsborg_story(player_name):
    """
    Runs the story when the users choose Elfsborg in drafted_two
    """
    print(f"{player_name} fits into Elfsborg quickly and effectively.")
    print(f"After just one season, {player_name} has already made a name for themselves in the entire league.")
    print(f"The future looks bright, but then the unexpected happens – during a collision, {player_name} breaks their ankle.")
    print(f"After surgery and rehab, it's clear that {player_name} won't be able to come back as an elite player.")
    print(f"{player_name} decides to pursue a career as:")

def team_sirius_story(player_name):
    """
    Runs the story when the users choose IK Sirius in drafted_three
    """
    print(f"{player_name} absolutely loves playing for Sirius! The team feels like home immediately, and {player_name} gains significant trust.")
    print(f"In the second season, {player_name} wins the top scorer title and is offered a contract with:")

def team_goteborg_story(player_name):
    """
    Runs the story when the users choose IFK Göteborg in drafted_three
    """
    print(f"{player_name} enjoys playing in Göteborg; the team, atmosphere, and coach are good.")
    print(f"The team is a mid-table one, fighting for every point, and {player_name} enjoys it.")
    print(f"{player_name} has an okay first season, followed by good second and third seasons.")
    print(f"However, after three seasons, Örebro needs to sell {player_name} for financial reasons.")
    print(f"{player_name} receives offers from two clubs and chooses to go to:")

def team_aik_story(player_name):
    """
    Runs the story when the users choose AIK in drafted_four
    """
    print(f"The first season with AIK is challenging. {player_name} keeps on fighting, but things don't go well for the team.")
    print(f"Midway through the season, the coach is fired.")
    print(f"The new coach recognizes {player_name}´s potential, resulting in more playing time and attention.")
    print(f"The team finishes at the bottom, but {player_name} receives offers from:")

def team_djurgarden_story(player_name):
    """
    Runs the story when the users choose Djurgården IF in drafted_four
    """
    print(f"It's challenging for {player_name} to break into a highly performing Malmö team.")
    print(f"The team tops the league and has stable midfielders. {player_name} keeps fighting and continues focusing on endurance.")
    print(f"After two seasons, playing time increases, and after four seasons, {player_name} becomes a seasoned and reliable starter.")
    print(f"fter six seasons with Malmö, {player_name} is recruited by:")

def youth_coach_story(player_name):
    """
    Runs the story when user choose Coach for u-21 in next_step_one
    """
    print(f"{player_name} starts their coaching career with hometown club GIF Sundsvall but quickly advances")
    print(f"After five seasons, {player_name} receives an offer to become the national team coach for the U-21 national team.")
    print(f"{player_name} accepts and manages to win the U-21 European Championship.")

def goalkeeper_coach_story(player_name):
    """
    Runs the story when user choose Goalkeeper coach in next_step_one
    """
    print(f"{player_name} quickly shifts focus from the injury and immediately starts their coaching education.")
    print(f"The results are clear; just a year later, {player_name} becomes the goalkeeper coach for AIK")
    print(f"After five seasons there, {player_name} is recruited by Arsenal.")

def team_milan_story(player_name):
    """
    Runs the story when user choose Milan in next_step_two
    """
    print(f"Milan and {player_name} fit like a glove!")
    print(f"{player_name} plays for Milan for a whole 8 seasons and even wins the top scorer title one year.")
    print(f"After that, {player_name} goes to Miami to conclude their career.")

def team_fullham_story(player_name):
    """
    Runs the story when user choose Fullham in next_step_three
    """
    print(f"{player_name} integrates well into the team and gains a lot of trust from the coach.")
    print("Everything is heading in the right direction until the unfortunate happens.")
    print(f"{player_name} tears their achilles tendon during the second season and never returns to their explosive self again.")

def team_leeds_story(player_name):
    """
    Runs the story when user choose Leeds in next_step_three
    """
    print(f"{player_name} initially struggles in the English league, but after two seasons, physicality and playing time increase.")
    print(f"{player_name} performs well and stays with the club for a remarkable nine seasons.")

def team_copenhagen_story(player_name):
    """
    Runs the story when user choose Copenhagen in next_step_three
    """
    print(f"Things go well for {player_name} in FC Copenhagen, and after two seasons, the team plays in the Champions League.")
    print("Even though the Danish league doesn't have the same standard, it becomes a good advertising window.")
    print(f"After these matches, more top clubs show interest in {player_name}.")

def coach_story(player_name):
    """
    Runs the story when user choose coach in next_step_four
    """
    print(f"{player_name} begins their coaching career at IK Sirius, and it starts a bit hesitantly.")
    print(f"But after some time, {player_name} becomes more comfortable, and the results start to show.")
    print(f"After 6 seasons with Sirius, {player_name} becomes the national team coach for Sweden.")

def junior_coach_story(player_name):
    """
    Runs the story when user choose Coach for minors in next_step_four
    """
    print(f"{player_name} is asked to help with the Elfsborg's junior team, and {player_name} accepts.")
    print(f"Initially, {player_name} doesn't quite see the purpose of it,")
    print(f" but after a while, {player_name} becomes attached to the players and provides valuable input.")
    print(f"The team participates and wins the Gothia Cup with {player_name} as the head coach.")

def team_roma_story(player_name):
    """
    Runs the story when user choose Roma in next_step_five
    """
    print(f"{player_name} works their way into the new team and enjoys it in Roma.")
    print(f"so much so that {player_name} stays there until the end of their career.")
    print(f"Roma and {player_name} achieve much together, but the greatest feat was when they won Serie A.")

def team_inter_story(player_name):
    """
    Runs the story when user choose Inter in next_step_five
    """
    print(f"{player_name} continues to perform and score goals.")
    print(f"After four years in Inter, {player_name} is recruited by Manchester City,")
    print(f"and it doesn't take long before {player_name} makes a name for themselves there too!")

def team_westham_story(player_name):
    """
    Runs the story when user choose Westham in next_step_six
    """
    print(f"{player_name} falls out of favor with supporters after a heavy derby loss.")
    print(f"The conflict escalates to the point where {player_name} is benched.")
    print(f"{player_name} is forced to change teams after just one year, returning to IFK Göteborg.")

def team_manchester_story(player_name):
    """
    Runs the story when user choose manchester united in next_step_six
    """
    print(f"{player_name} has to fight their way into the team but gains more and more trust, playing in more critical matches.")
    print(f"{player_name} plays four seasons with Manchester United, and one of those seasons results in winning the Champions League!")

def team_ajax_story(player_name):
    """
    Runs the story when user choose ajax in next_step_seven
    """
    print(f"{player_name} gains significant trust from the coach immediately.")
    print(f"{player_name} plays well, adapts to the pace and playing style right away.")
    print(f"When the coach gets a new contract with Liverpool FC, he takes {player_name} with him!")

def team_lissabon_story(player_name):
    """
    Runs the story when user choose Lissabon in next_step_seven
    """
    print(f"{player_name} makes a very good first impression, and both the coach and supporters see {player_name} as the team's star player after the first season")
    print("Sporting Lisbon even wins the Europa League one year.")

def team_newcastle_story(player_name):
    """
    Runs the story when user choose newcastle in next_step_eight
    """
    print(f"The adjustment to moving to England is challenging for {player_name}; it takes a long time before {player_name} adapts. ")
    print("This is also noticeable on the football field. The first season with Newcastle is not good.")
    print(f"However, the coach continues to believe in {player_name}, and after two seasons with the club, the results finally start to come!")

def team_stoke_story(player_name):
    """
    Runs the story when user choose stoke in next_step_eight
    """
    print(f"There is nothing that can stop {player_name} in their new club.")
    print(f"Unfortunately, {player_name} doesn't stay long in Stoke as they are recruited by PSG after just two seasons.")