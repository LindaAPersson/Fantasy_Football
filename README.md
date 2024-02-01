
# Fantasy Football

[Fantasy Football](https://fantasyfootball-pp3-b369c54e5451.herokuapp.com/) is a text-based game for those who have a moment to spare and want to immerse themselves in the wonderful world of football.

IMAGE RESPONSIVE

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

FLOWCHART

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

WELCOME

### Instructions:
After the welcome text, the user can choose to read the instructions if they wish.
If the user wants to read the instructions, they appear in blue.

INSTRUCTIONS

### Name input:
To make the game more personal, the user can choose a name for the football player that will last throughout the entire game. A Name can only contain letters; otherwise, an error message is displayed, and the player must choose a new name.

NAME INPUT
NAME INPUT WRONG

### Game story:
Once the player has entered a name, the game's story begins to unfold. It starts with a brief background story, followed by two alternatives on how the player wants to guide their football player. The small stories that appear between the alternatives are written as if they are happening in real-time. I did this to make the game feel more personal, as if what is written is happening only to this specific player. There are a total of 31 small stories in this game that are displayed depending on how the player chooses to navigate through the game. Below are examples of one story from each phase.

GAME STORY
1
2
3

### End game:
When the player has gone through all the alternatives, a short concluding story about how it went for the football player follows. After that, there is a 'Thanks for playing' text and an ASCII image of a football. The game also asks the player if they want to play again. If the player wants to, they are taken to the instructions again. If the player wants to exit the game, a 'goodbye' text is displayed on a yellow background.

ENDGAME




## Testing
y/n input
| Test/function | Action | Expectation | Result |
| :-----------| :----:| :----:|:----:|
| Invalid input - choose_game_rules | Entered: space, number, enter  | app informs user of invalid data & prompts the user to try again | Works as expected |
| Valid input - choose_game_rules | Entered: Y,y,N,n | app proceeds to next function | Works as expected |
| Invalid input - game_rules | Entered: space, number, enter  | app informs user of invalid data & prompts the user to try again | Works as expected |
| Valid input - game_rules | Entered: Y,y,N,n | app proceeds to next function | Works as expected |
| Invalid input - end_game | Entered: space, number, enter  | app informs user of invalid data & prompts the user to try again | Works as expected |
| Valid input - end_game | Entered: Y,y,N,n | app proceeds to next function | Works as expected |

text input
| Test/function | Action | Expectation | Result |
| :-----------| :----:| :----:|:----:|
| Invalid input - choose_name | Entered: space, number, enter  | app informs user of invalid data & prompts the user to try again | Works as expected |
| Valid input - choose_name| Entered: only letters | app proceeds to next function | Works as expected |

1/2 input
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

