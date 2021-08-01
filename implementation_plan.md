# Implementation plan

## Overall process:

### 1
Design the game’s features which should be easy to code and meet criteria
### 2 
Break down features into functional parts and visualise them in a control flow diagram 
### 3 
Interpret diagram to create list of codable functions and elements which will accomplish the tasks
### 4
Write pseudo-code 
### 5
Translate pseudo-code into code
### 6
Implement code
### 7
Test 


## Checklist for feature implementation - in descending order of importance

###  Critical features:

### *Card creation*
Use a function to generate a shuffled list of a subset of ascii symbols
* fit into control flow diagram
* choose ascii symbols
* write code for doubling and shuffling
* write for loop to iterate making cards
* test output


### *Board display*
Use a function to draw the board filled with ‘cards’.
* fit into control flow diagram 
* write for loop to iterate through cards dictionary
* write conditionals for cards printing face up or down
* get function to accept optional parameter of card
* test board function
* implement screen clearing before each print
* make the board look nice
	

### *Card selection (input step)*
Use a while loop containing the 2 turns, each with their own input variables
* fit into control flow diagram
* write input variables
* write function to check for errors on input
    * inputs are valid
    * input for turn 2 is different to turn 1
* test functions - input passes to print board and flips card
* write error messages
* implement function to pause screen after Turn 2
* write while loop which breaks if user inputs “exit” 


### *Pair matching*
Use a conditional structure in the Turns loop to check if the selected pair match (and not outside that scope)
* fit into control flow diagram
* write conditional structure for matching each round
* write function which checks if all cards have been matched for win condition
* test matching works
* test that game can be finished


### Low priority features:

### *Scoring*
Use a round count variable with += 1 per round. Use a function to record time taken from game start to win condition
* call datetime.time twice and subtract difference
* write code for round counter
* test game to finish to see if score works

### *Difficulty setting*
use bash arguments for selecting difficulty, increasing the size of the board
* write bash script which accepts args
* code difficulty setting into app
* each function of the entire program(?) would have to include another optional parameter from the bash script
* bash argument changes scope of most functions
* test game can be run in each mode by running application through bash script

### *Play again option*
Use a while loop containing the whole main function - breaks if player chooses not to play again
* write while loop
* test if the game can be played multiple times with a different board of cards without exiting

	
