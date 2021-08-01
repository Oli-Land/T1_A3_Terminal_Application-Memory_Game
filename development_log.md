# Status Updates

## Log entry 1

Rough control flow diagram completed. All essential features described with dot points in the project implementation plan. I have decided to avoid using matrices to display the game’s cards in favour of simplicity. At this stage I have coded a list of lists containing the cards’ identities, and another list of lists containing the board of blank card backs. Each card is given a different symbol from a list each time the app runs. I have defined a function to print the board, but it’s not very visually appealing yet. I have a series of conditionals which successfully references the cards from user input, however I am yet to figure out how to best approach modifying the board variables throughout the game, as they need to show when selected, but disappear when matched.
Next I will focus on turning all my code so far into separate concise functions.

## Log entry 2

I have discarded much of the original code, as it was turning into a giant list of variables. Instead I have used more logic to iterate through creating the game’s cards and also print the board. Now the functions are defined before the main game loop and called efficiently. I have figured out how to pass the functions the correct arguments. Most of the essential features are working. Next I need to implement the minor features such as scoring, and also work out how to fix an error whereby the user inputs the same choice twice in a row, resulting in a false positive match.
