Help File

System/hardware requirements:
This application was written and tested using wsl ubuntu 20.04. Therefore it is recommended the user runs it in a linux based environment.

Requires Python 3 to be installed. Please enter the following into terminal to check:

    python3 --version




To run the game, enter the following into the terminal: 

    cd assignment

for easy mode:

	./wrapper.sh

for hard mode:
	
	./wrapper.sh hard



Dependencies:
All modules used are native to python 3, and therefore the user may decide to skip the installation step of creating a virtual environment if they wish.
Otherwise, type the following into the terminal before running:

    python3 -m venv venv

    source venv/bin/activate

random - random.shuffle() function used to shuffle the cards at the start of each game

os system - system('clear') function used to clear terminal of previous outputs each time the application prints

time - time.sleep() function used to pause application each round to view cards
time.perf_counter() function used to track game time for scoring



Features of the application:

Board  - The game starts by drawing a grid. The x axis is labelled with letters while the y axis has numbers. These allow for Grid coordinate selection during gameplay. Each coordinate contains a ‘card’ with a hidden value of one ASCII symbol. 

Card selection - The player inputs their card selection as grid coordinates, for example ‘b3’ will refer to the card in the second column, third row. Selected cards will ‘flip’ to reveal their face-side symbol. Cards are revealed in pairs, meaning a timer will automatically revert both to being hidden 2s after the second selection of each pair. 

Pair matching - The game recognises when a selected pair match. The pair will then remain flipped so the player can track their progress. When all pairs are matched, the game ends, printing the total game time and number of rounds taken to finish as the player’s score.

If the user wishes to exit the application before game completion:
Please type “exit” into the terminal during gameplay



