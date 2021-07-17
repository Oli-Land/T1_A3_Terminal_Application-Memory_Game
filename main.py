import random
import datetime

# from numpy import floating

# custom list of visually appealing ASCII characters
symb_lib = ["@", "#", "$", "%", "<", "&", ">", "?"]

# double each symbol to create list of card pairs
symbs = symb_lib * 2

# card_rows = [a, b, c, d]

# create board of card 'backs' to print during game

row_a = ["0", "0", "0", "0",]
row_b = ["0", "0", "0", "0",]
row_c = ["0", "0", "0", "0",]
row_d = ["0", "0", "0", "0",]

def printBoard():
    print("")
    print("     1    2    3    4")
    print("")   
    print("a ", row_a)
    print("b ", row_b)
    print("c ", row_c)
    print("d ", row_d)



# main game logic 
def main():

    # use imported random.shuffle to randomise card position
    random.shuffle(symbs)
    
    # create hidden lists of card identities
    list_a = [symbs[0], symbs[1], symbs[2], symbs[3]]
    list_b = [symbs[4], symbs[5], symbs[6], symbs[7]]
    list_c = [symbs[8], symbs[9], symbs[10], symbs[11]]
    list_d = [symbs[12], symbs[13], symbs[14], symbs[15]]


    print("Welcome to OliLand, please take a look at the board and make a selection...")

   
    printBoard()


    count = 0

     # turn starts



    
    # take user input for selected coordinates
    initial_input = input("Enter row coordinates of first selection (a-d) Enter column coordinates of first selection (1-4): ")

    # turn counter, to be displayed as score upon game win
    count += 1
    select_1a = initial_input[0]
    select_1b = initial_input[1]

    # select_1b = input("Enter column coordinates of first selection (1-4): ")
    # select_1a = input("Enter row coordinates of first selection (a-d): ")
    # select_1b = input("Enter column coordinates of first selection (1-4): ")

    if select_1a == "a":
        list = list_a
        row = row_a

    elif select_1a == "b":
        list = list_b
        row = row_b

    elif select_1a == "c":
        list = list_c
        row = row_c
        
    elif select_1a == "d":
        list = list_d
        row = row_d
    else:
        print("Invalid")

    
    # choice variable == card identity
    choice = list[int(select_1b)]
    print(select_1a, select_1b)
    print(choice)

    # selected board position variable
    choice_position = row[int(select_1b)]
    print(choice_position)
    # overwrite board coordinate '0' with card identity in order to display choice



    
    
    
    print(count)
       


main()
