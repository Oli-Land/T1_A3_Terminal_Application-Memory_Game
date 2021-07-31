import random
import datetime



def init_board():
    board = {}
    # the cards that go into the board
    symb_lib = ["@", "#", "$", "%", "<", "&", ">", "?"]
    symbs = symb_lib * 2
    random.shuffle(symbs)
    # iterate through board
    for letter in ['a', 'b', 'c', 'd']:        
        for number in ['1', '2', '3', '4']:
            board[letter + number] = {}
            board[letter + number]['Value'] = symbs.pop()
            board[letter + number]['Matched'] = False

    return board


def print_board(board, flipped_cards = []):
    print(flipped_cards)
    print("    1   2   3   4")
    print("  -----------------")
    for letter in ['a', 'b', 'c', 'd']:
        print(letter + ' | ', end= "")
        for number in ['1', '2', '3', '4']:            
            if (letter + number) in flipped_cards:
                print(board[letter + number]['Value'] + " | ", end= "")
            elif board[letter + number]['Matched'] == True:
                print(board[letter + number]['Value'] + " | ", end= "")
            else:
                print("." + " | ", end= "")
        print("")
        print("  -----------------")

def is_game_finished(board):
    for letter in ['a', 'b', 'c', 'd']:        
        for number in ['1', '2', '3', '4']:
            if board[letter + number]['Matched'] == False:
                return False
    return True



# main game logic 
def main():

    board = init_board()

    # while loop for turns here
    while not is_game_finished(board):
        
        # Flip 1
        current_input_1 = input("Enter coordinates of first selection (a-d)(1-4): ")

        print_board(board, flipped_cards = [current_input_1])

        # Flip 2
        current_input_2 = input("Enter coordinates of second selection (a-d)(1-4): ")

        print_board(board, flipped_cards = [current_input_1, current_input_2])

        if board[current_input_1]['Value'] == board[current_input_2]['Value']:
            board[current_input_1]['Matched'] = True
            board[current_input_2]['Matched'] = True
            print("Correct match!")
        else:
            print("No match, please try again")







main()
