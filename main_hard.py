# This is a duplicate of main.py with a larger board of cards. Must be initialised by adding an argument on application startup ie. run this in terminal: ./wrapper.sh hard

import random
from os import system
import time


def init_board():
    board = {}
    symb_lib = ["@", "#", "$", "%", "<", "&", ">", "?", "=", "[", "]", "{", "}", "+", "^", "~", "*", "-"]
    symbs = symb_lib * 2
    random.shuffle(symbs)
    # iterative card generator
    for letter in ['a', 'b', 'c', 'd', 'e', 'f']:        
        for number in ['1', '2', '3', '4', '5', '6']:
            # each card is a nested dictionary named after a board coordinate 
            board[letter + number] = {}
            # a symbol value           
            board[letter + number]['Value'] = symbs.pop()
            # a boolean for its matched status
            board[letter + number]['Matched'] = False

    return board


# Print board function prints a 4x4 grid of cards from the board dictionary. Each 'card' shows up blank by default.
# Prints a card's value when the function is handed a card's name as an argument, or when the card's matched status equals True
def print_board(board, flipped_cards = []):
    print(f"Selected: {flipped_cards}")
    print("    1   2   3   4   5   6")
    print("  -------------------------")
    for letter in ['a', 'b', 'c', 'd', 'e', 'f']:
        print(letter + ' | ', end= "")
        for number in ['1', '2', '3', '4', '5', '6']:            
            if (letter + number) in flipped_cards:
                print(board[letter + number]['Value'] + " | ", end= "")
            elif board[letter + number]['Matched'] == True:
                print(board[letter + number]['Value'] + " | ", end= "")
            else:
                print(" " + " | ", end= "")
        print("")
        print("  -------------------------")


# Function checks for the game win condition: returns True when all cards have Matched == True
def is_game_finished(board):
    for letter in ['a', 'b', 'c', 'd', 'e', 'f']:        
        for number in ['1', '2', '3', '4', '5', '6']:
            if board[letter + number]['Matched'] == False:
                return False
    return True


# Error checking function: checks input for each turn is valid. Returns False on valid input to break loop
def is_invalid_input(input, previous_input = ""):
    # default string to enter loop. 
    if input == "catch":
        return True

    # exit game if player inputs "exit"    
    if input == "exit":
        return False

    # check for valid input
    if len(input) != 2:
        print("Please enter coordinates as 2 digits (letter,number)")
        return True
    elif input[0] not in ['a', 'b', 'c', 'd', 'e', 'f']:
        print("Please enter a valid row (a-f)")
        return True
    elif input[1] not in ['1', '2', '3', '4', '5', '6']:
        print("Please enter a valid column (1-6)")
        return True

    # check that input 2 doesn't equal input 1
    if input == previous_input:
        print("Please select a different card for Turn 2")
        return True
        
    return False


# main game logic
def main():


    # while play loops whole game unless player enters "no" after finishing
    play = True
    while play:

        board = init_board()

        print("""Welcome to OliLand!

        This is a game of memory
        Choose a card on the board to view its symbol
        Input board coordinates for card choice as (row)(column) eg. b3
        Try to match pairs of cards
        Scoring is based on speed and accuracy
        Have fun!
        (Type "exit" to exit game)        


        """)

        print_board(board)

        input("Press the Enter key to start game...")

        round_count = 0
        start_time = time.perf_counter()

        # while loop for Turns starts here: Turns loop until is_game_finished(board) == True
        # each Turn: take user input coordinates and print a board with the selected card(s) flipped

        while not is_game_finished(board):

            # imported os system function clears the terminal window before each print board
            system('clear')
            print_board(board)

            # -- Turn 1 --
            current_input_1 = "catch"
            # input stage loops until valid input entered. Hands input to error checking function
            while is_invalid_input(current_input_1):
                current_input_1 = input("Enter coordinates of first selection (a-d)(1-4): ")
            if current_input_1 == "exit":
                break

            system('clear')
            print_board(board, flipped_cards=[current_input_1])

            # -- Turn 2 --
            current_input_2 = "catch"
            while is_invalid_input(current_input_2, current_input_1):
                current_input_2 = input("Enter coordinates of second selection (a-d)(1-4): ")
            if current_input_1 == "exit":
                break

            system('clear')
            # second Turn print board shows both selected cards revealed
            print_board(board, flipped_cards=[current_input_1, current_input_2])

            # add one to score variable per round of 2 turns
            round_count += 1

            # conditional structure tests for matched pairs and sets their Matched boolean to True
            if board[current_input_1]['Value'] == board[current_input_2]['Value']:
                board[current_input_1]['Matched'] = True
                board[current_input_2]['Matched'] = True
                print("Correct match!")
            else:
                print("No match, please try again")

            # timer gives 2 seconds to view both cards flipped together before next Round
            time.sleep(2)

        # end game score
        end_time = time.perf_counter()
        game_time = round(end_time - start_time, 2)


        print(f"You finished the game in {round_count} turns, taking {game_time} seconds!")

        # play again loop
        again = str(input('Do you want to play again? Enter "no" to exit: '))
        if again == "no":
            play = False


main()
