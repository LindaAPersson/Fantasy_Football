
# Fantasy Football

[Fantasy Football](https://fantasyfootball-pp3-b369c54e5451.herokuapp.com/) is a text-based game for those who have a moment to spare and want to immerse themselves in the wonderful world of football.

![Am i responsve](../assets/readme-img/responsiv.png)

## How to play:

Fantasy Football is a completely text-based game where the user progresses by choosing different options provided by the game. The game begins by welcoming the player and asking if they want to read the instructions for the game. The player can respond with 'y' for yes and 'n' for no.
Once the player has finished reading the instructions and clicked to start the game, they can choose a name for their football player.
After that, a background story begins to unfold on the screen. When it is complete, the player starts choosing the career path for their football player. This is done by offering the player two different options, and the player chooses the one they think fits best by entering 1 or 2. A short story will be displayed on the screen for each choice.
When the player has worked through all the options, they are offered the choice to play again or to exit the game.

## User Story:

### First-time user:
- I am interested in football and want to pass the time with a text-based game.
- I want to influence the direction the game takes.

### Second-time user:
- I am interested in football and want to pass the time with a text-based game.
- I want to see if my player takes a different career path compared to the last time I played.

## Flowchart:
To design the game, I created a flowchart to get an overview of all the parts I would need to work on. This helped me see where I needed to start the process. However, during the project, I also added some more features, for example 'How to play'.

![Flowchart](../Fantasy_Football/assets/readme-img/flowchart.png)

## Site structure:
The code I have created for the game mainly consists of three Python documents: run.py, story.py, and effect.py. 
I have chosen to divide the code into three documents to make it easier to read.

- run.py: Consists of the main functions that make the game run, and the input functions.
- story.py: Contains the short stories played out when the user progresses through the game.
- effect.py: Includes the function that makes it appear as if the text is being written in real-time.

### Packages:
The different packages I have installed are:

- Termcolor: This allows setting different colors for text and its background.
- Sys: It is part of the Python Standard Library and provides access to some variables used or maintained by the Python interpreter.
- Time: It is part of the Python Standard Library and provides various time-related functions.

## Design:
To add some more life into the game than just plain text, I have chosen to add a bit of color and ASCII art. 
For the welcome text, I opted for white text on a green background to symbolize how a football field looks.

The instructions have a blue color to stand out from the rest of the text, making it clear to the user that this text is not part of the game.

In areas where users are expected to contribute information, I added a green text color. I did this to ensure that users easily notice that something different is happening here.

If users input incorrect characters at these inputs, a red error message will appear. This is to prompt users to react immediately when something didn't go as intended.

When the game is over, it thanks the player for participating, and another ASCII art is displayed along with the question of whether the user wants to play again. If the user chooses not to, the game says 'goodbye' on a yellow background. This is to make sure users understand that something significant has occurred.

## Features:
### Welcome:
When you arrive at the game, you are greeted by an ASCII image resembling a football field. Along with it is a text designed to invite the user's curiosity and make them want to start playing.

![Welcome text](../Fantasy_Football/assets/readme-img/startpage.png)

### Instructions:
After the welcome text, the user can choose to read the instructions if they wish.
If the user wants to read the instructions, they appear in blue.

![Instructions](../Fantasy_Football/assets/readme-img/instructions.png)

### Name input:
To make the game more personal, the user can choose a name for the football player that will last throughout the entire game. A Name can only contain letters; otherwise, an error message is displayed, and the player must choose a new name.

![Name input](../Fantasy_Football/assets/readme-img/name-input.png)
![Name input wrong](../Fantasy_Football/assets/readme-img/name-input-wrong.png)

### Game story:
Once the player has entered a name, the game's story begins to unfold. It starts with a brief background story, followed by two alternatives on how the player wants to guide their football player. The small stories that appear between the alternatives are written as if they are happening in real-time. I did this to make the game feel more personal, as if what is written is happening only to this specific player. There are a total of 31 small stories in this game that are displayed depending on how the player chooses to navigate through the game. Below are examples of one story from each phase.

![Option1](../Fantasy_Football/assets/readme-img/first-option.png)
![Option1](../Fantasy_Football/assets/readme-img/second-option.png)
![Option1](../Fantasy_Football/assets/readme-img/third-option.png)
![Option1](../Fantasy_Football/assets/readme-img/fourth-option.png)

### End game:
When the player has gone through all the alternatives, a short concluding story about how it went for the football player follows. After that, there is a 'Thanks for playing' text and an ASCII image of a football. The game also asks the player if they want to play again. If the player wants to, they are taken to the instructions again. If the player wants to exit the game, a 'goodbye' text is displayed on a yellow background.

![End of the game](../Fantasy_Football/assets/readme-img/endgame.png)
![Exit the game](../Fantasy_Football/assets/readme-img/exit-game.png)

## Future implementations:
### Code:
- Refactor the code so that it does not need to be repeated. This makes the files smaller and easier to read.
- Enable players to exit the game whenever they want to make it more user-friendly.

### Game Concept:
Allow players to choose which team they want to join. This way, the game could be extended with the existing built-in stories and the random function.

## Testing

### PEP8 Linter
Testing the code with PEP8 Linter, on all three sites came back clear.

![PEP8 Linter run.py](../Fantasy_Football/assets/readme-img/pep-run.png)
![PEP8 Linter story.py](../Fantasy_Football/assets/readme-img/pep-story.png)
![PEP8 Linter effect.py](../Fantasy_Football/assets/readme-img/pep-effect.png)

### Input testing
Yes or no input
| Test/function | Action | Expectation | Result |
| :-----------| :----:| :----:|:----:|
| Invalid input - choose_game_rules | Entered: space, number, enter  | app informs user of invalid data & prompts the user to try again | Works as expected |
| Valid input - choose_game_rules | Entered: Y,y,N,n | app proceeds to next function | Works as expected |
| Invalid input - game_rules | Entered: space, number, enter  | app informs user of invalid data & prompts the user to try again | Works as expected |
| Valid input - game_rules | Entered: Y,y,N,n | app proceeds to next function | Works as expected |
| Invalid input - end_game | Entered: space, number, enter  | app informs user of invalid data & prompts the user to try again | Works as expected |
| Valid input - end_game | Entered: Y,y,N,n | app proceeds to next function | Works as expected |

Text input
| Test/function | Action | Expectation | Result |
| :-----------| :----:| :----:|:----:|
| Invalid input - choose_name | Entered: space, number, enter  | app informs user of invalid data & prompts the user to try again | Works as expected |
| Valid input - choose_name| Entered: only letters | app proceeds to next function | Works as expected |

1 or 2 option input
| Test/function | Action | Expectation | Result |
| :-----------| :----:| :----:|:----:|
| Invalid input - choose_training| Entered: space, letter, enter  | app informs user of invalid data & prompts the user to try again | Works as expected |
| Valid input - choose_training | Entered: 1 or 2 | app proceeds to next function | Works as expected |
| Invalid input - choose_position_one| Entered: space, letter, enter  | app informs user of invalid data & prompts the user to try again | Works as expected |
| Valid input - choose_position_one | Entered: 1 or 2 | app proceeds to next function | Works as expected |
| Invalid input - choose_position_two| Entered: space, letter, enter  | app informs user of invalid data & prompts the user to try again | Works as expected |
| Valid input - choose_position_two | Entered: 1 or 2 | app proceeds to next function | Works as expected |
| Invalid input - drafted_one| Entered: space, letter, enter  | app informs user of invalid data & prompts the user to try again | Works as expected |
| Valid input - drafted_one | Entered: 1 or 2 | app proceeds to next function | Works as expected |
| Invalid input - drafted_two| Entered: space, letter, enter  | app informs user of invalid data & prompts the user to try again | Works as expected |
| Valid input - drafted_two | Entered: 1 or 2 | app proceeds to next function | Works as expected |
| Invalid input - drafted_three| Entered: space, letter, enter  | app informs user of invalid data & prompts the user to try again | Works as expected |
| Valid input - drafted_three | Entered: 1 or 2 | app proceeds to next function | Works as expected |
| Invalid input - drafted_four| Entered: space, letter, enter  | app informs user of invalid data & prompts the user to try again | Works as expected |
| Valid input - drafted_four | Entered: 1 or 2 | app proceeds to next function | Works as expected |
| Invalid input - next_step_one| Entered: space, letter, enter  | app informs user of invalid data & prompts the user to try again | Works as expected |
| Valid input - next_step_one | Entered: 1 or 2 | app proceeds to next function | Works as expected |
| Invalid input - next_step_two| Entered: space, letter, enter  | app informs user of invalid data & prompts the user to try again | Works as expected |
| Valid input - next_step_two | Entered: 1 or 2 | app proceeds to next function | Works as expected |
| Invalid input - next_step_three| Entered: space, letter, enter  | app informs user of invalid data & prompts the user to try again | Works as expected |
| Valid input - next_step_three | Entered: 1 or 2 | app proceeds to next function | Works as expected |
| Invalid input - next_step_four| Entered: space, letter, enter  | app informs user of invalid data & prompts the user to try again | Works as expected |
| Valid input - next_step_four | Entered: 1 or 2 | app proceeds to next function | Works as expected |
| Invalid input - next_step_five| Entered: space, letter, enter  | app informs user of invalid data & prompts the user to try again | Works as expected |
| Valid input - next_step_five | Entered: 1 or 2 | app proceeds to next function | Works as expected |
| Invalid input - next_step_six| Entered: space, letter, enter  | app informs user of invalid data & prompts the user to try again | Works as expected |
| Valid input - next_step_six | Entered: 1 or 2 | app proceeds to next function | Works as expected |
| Invalid input - next_step_seven| Entered: space, letter, enter  | app informs user of invalid data & prompts the user to try again | Works as expected |
| Valid input - next_step_seven | Entered: 1 or 2 | app proceeds to next function | Works as expected |
| Invalid input - next_step_eight| Entered: space, letter, enter  | app informs user of invalid data & prompts the user to try again | Works as expected |
| Valid input - next_step_eight | Entered: 1 or 2 | app proceeds to next function | Works as expected |

## Bugs:
There are no bugs in the game right now, as far as I know.

A bug that my mentor found when testing the game was that the user could proceed through "choose_name" without entering anything.
This was fixed using the .isalpha() function, so now the user must enter at least one letter to proceed in the game.

## Deployment:
First, I created a new repository on GitHub using a template provided by Code Institute. I took the following steps:

1. Log into GitHub.
2. Locate the right template.
3. Click on "Use this template" to create a new repository.
4. Choose a repository name and create the repository.
5. The development environment used for this project was GitPod.

The project was deployed using Heroku, following these steps:

First, the Code Institute template provides a document called "requirements.txt," and this file needs to contain a list of all libraries the project needs to run. Otherwise, Heroku won't be able to run the project.

Then follow these steps:
1. Login to Heroku (Create an account if necessary).
2. Click on "New" in the Heroku dashboard and select "Create new app."
3. Write a name for the app, choose your region, and click "Create App."
4. In the settings tab for the new application, create one Config var with the name PORT and a value of 8000.
5. Add two buildpack scripts: Python and Nodejs (in that order).
6. In the deployment tab, select GitHub as the deployment method and confirm your choice.
7. In the "Connect to GitHub" field, search for your repository name and click on the connect button next to the right repository.
8. Choose between automatic deploys or manual deploys. I chose automatic deploys.
9. When the app is deployed, a link will appear at the bottom of the page.

After these steps were taken, the application was deployed at the following link: [Fantasy Football](https://fantasyfootball-pp3-b369c54e5451.herokuapp.com/)

## Credits:
Firstly, I want to express a big thank you to my mentor who provided me with numerous ideas on what to do for the game. Additionally, she finds all the bugs that I might overlook!

### Code:
The code for the "slow()" function, which makes the text appear as if it's being written in real-time, is modeled after this [YouTube tutorial](https://www.youtube.com/watch?v=Z1_camyBMDo)

### ASCII Art:
The football field at the beginning of the game and the football at the end of the game are taken from: [ASCII Art](https://www.asciiart.eu/sports-and-outdoors/soccer)

### Termcolor:
The package that allows for changing the text color and background color is downloaded from here: [Termcolor](https://pypi.org/project/termcolor/)