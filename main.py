import random
import datetime

from numpy import floating


# custom list of visually appealing ASCII characters
symb_lib = ["@", "#", "$", "%", "<", "&", ">", "?"]

# double each symbol to create list of card pairs
symbs = symb_lib * 2

# use imported random.shuffle to randomise card position
random.shuffle(symbs)


# create hidden lists of card identities
cards_a = [symbs[0], symbs[1], symbs[2], symbs[3]]
cards_b = [symbs[4], symbs[5], symbs[6], symbs[7]]
cards_c = [symbs[8], symbs[9], symbs[10], symbs[11]]
cards_d = [symbs[12], symbs[13], symbs[14], symbs[15]]

# create board of card 'backs' to print during game
row_a = ["0", "0", "0", "0",]
row_b = ["0", "0", "0", "0",]
row_c = ["0", "0", "0", "0",]
row_d = ["0", "0", "0", "0",]

rows = [row_a, row_b, row_c, row_d]

# define print board
def printBoard():
    print("")
    print("     1    2    3    4")
    print("")   
    print("a ", row_a)
    print("b ", row_b)
    print("c ", row_c)
    print("d ", row_d)

printBoard()

#take user input for selected coordinates
select_1a = input("Enter row coordinates of first selection (a-d): ")
select_1b = input("Enter column coordinates of first selection (1-4): ")


# for loop





# print board with first selection revealed in place of X's


#selection_1a = input("Enter row coordinates of second selection (a-d): ")
#selection_1b = input("Enter column coordinates of second selection (1-4): ")

# print board with second selection revealed in place of X's



#timer 


