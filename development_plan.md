## Memory Game
#### *Oliver Landreth*

# Development Plan


## Statement of Purpose and Scope

- describe at a high level what the application will do

This terminal application is a game of Memory. A grid of ‘cards’ with hidden identities is displayed on-screen. The player inputs coordinates to select and reveal cards in pairs, attempting to remember their identities and grid position before a short timer resets the cards back to their hidden state. When the player reveals a pair of cards with the same identity, the pair are matched and remain revealed until the game ends. Once all cards are matched, the player wins and the total game time and number of attempts are returned as their score.

- identify the problem it will solve and explain why you are developing it

This game is intended to be used as productive entertainment. Short term memory is a fundamental, yet undertrained mental ability. By practicing with this game, the player will hopefully notice an improvement to memory function in general life.   

- identify the target audience

Anyone seeking to improve their mental faculties while passing time is encouraged to play. Games are low-commitment and typically conclude within several minutes. All ages are appropriate, however a basic proficiency with computers is required. The game can be played in easy or hard mode (4x4 or 6x6 grid)



## Keywords disambiguation:
I will use the following nomenclature throughout this documentation
### Turn 
* a single input consisting of a letter and number coordinate pair eg. b3
results in a 'card flip' ie. the card's value will now show instead of blank space
### Round 
* the unit for score-keeping. Consists of 2 Turns. Each round the pairs of 'cards' are matched.
### Match
* Identical card pair recognised for win condition
### Game
* The application runs from start to finish

## Features

### *Card creation*
The board’s cards are created at the start of each game with the init_board() function. This uses a for loop within a for loop to iterate through each possible grid coordinate. Each card is itself a dictionary named after the grid coordinate, nested within another dictionary, the “board” variable.
The card dictionaries each have a key called “Value” which ties to their face identity; an ascii symbol taken from a custom list I made based on their looks. They also have a “Matched” key, referring to a boolean used to track when they are successfully matched. 
Each game the symbols used are paired and ‘shuffled’ using the imported random.shuffle() function before being assigned to a card, resulting in a randomised position on the board.

### *Board display*
The print board function prints a visually appealing grid with axes labeled for coordinate selection.
The function takes the “board” variable and another optional parameter, a list containing user inputs in the form of grid coordinates.
A for loop iterates through each card, and using a conditional structure prints the card’s symbol if the card has been selected this turn or has been previously matched. Otherwise a blank space is printed.
Before each time the board is printed, the terminal window is cleared using the os system function system(‘clear’). This gives the visual impression of a static board of cards rather than a scrolling terminal. The user is also prevented from scrolling upwards to cheat

### *Card selection* 
The game takes place within a while loop consisting of 2 input Turns
Each Turn the player inputs coordinates into the terminal to reveal cards. The coordinates are handed to the print_board() function as additional arguments. The board is then printed with the selected card revealed
During the second Turn of each round, the board will print with both cards revealed
At the end of the second Turn each round, the application pauses operation for 2 seconds using the imported time.sleep() function. This gives players a limited time to memorise the currently revealed cards before the next round starts
Card selection is the main input step for the game, therefore it includes error handling structures. Using while loops the input steps loop until valid inputs are received. The is_invalid_input() function is a series of conditionals which checks if each input is the correct length (2 digits) and that each input digit is a valid grid row or column. Invalid inputs return the appropriate error message. 

### *Pair matching*
Each Turn ends with a conditional structure for matching. This compares the symbol Values for both selected cards. If the values are identical, both cards’ Matched boolean is set to True. They will remain revealed until the game ends
The game’s turns loop indefinitely until all cards have been matched. The function is_game_finished(board) iterates through the cards and checks their ‘Matched’ boolean. When all are True the loop breaks and the game ends

### *Scoring*
Total time taken for each game is calculated as the difference between an initial and final variable, using the imported time.perf_counter() function
The number of rounds taken to finish the game is also recorded in a variable. Each round the count has +=1 applied

### *Play again option*
The game’s main sequence including initial board/card creation is contained within a while loop which allows for a new game to be played without exiting first. If the user enters “no” when prompted after game win, the application will instead exit

### *Difficulty setting*
The user can select the difficulty of the game by inputting an argument when they launch the application.

for easy mode (4x4 grid):

    ./wrapper.sh

for hard mode (6x6 grid):

    ./wrapper.sh hard 


## User Interaction and Experience

- how the user will find out how to interact with / use each feature

The user can read installation and usage instructions for the application in the included help file. Additionally, there are gameplay instructions and rules printed to the screen before each game starts.

- how the user will interact with / use each feature
	
#### *Choosing difficulty*
The user must input their desired choice for game difficulty as a bash argument when they open the application. eg.
for easy mode:

    ./wrapper.sh

for hard mode:

    ./wrapper.sh hard

### *Card selection*
This is the only in-game feature with user interaction. The user enters coordinates into the terminal to reveal the corresponding card. Instructions for entering a valid input are shown before and during gameplay

- how errors will be handled by the application and displayed to the user

User input errors are detected using a function containing conditionals to catch each possible type of error. Inputs are contained within while loops which break upon valid input, determined by the function. Invalid inputs return an appropriate error message and do not break the loop, thereby allowing uninterrupted play. 




## Control Flow Diagram

![](memory%20control%20flow%20diagram.png)