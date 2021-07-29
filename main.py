import random
import datetime

# from numpy import floating
    
# main game logic 
def main():
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

    # custom list of visually appealing ASCII characters
    symbs = ["@", "#", "$", "%", "<", "&", ">", "?", "@", "#", "$", "%", "<", "&", ">", "?"]

    # use imported random.shuffle to randomise card position
    random.shuffle(symbs)

    # create hidden lists of card identities
    list_a = [symbs[0], symbs[1], symbs[2], symbs[3]]
    list_b = [symbs[4], symbs[5], symbs[6], symbs[7]]
    list_c = [symbs[8], symbs[9], symbs[10], symbs[11]]
    list_d = [symbs[12], symbs[13], symbs[14], symbs[15]]

    print("Welcome to OliLand, please take a look at the board and make a selection...")

    
    printBoard()
    # print(symbs)

    count = 0

    #take user input 1 for selected coordinates (first choice)
    current_input_1 = input("Enter coordinates of first selection (a-d)(1-4): ")
    print(current_input_1)
    row_input_1 = current_input_1[0]
    column_input_1 = current_input_1[1]
    count += 1
    if row_input_1 == "a":
        row_choice_1 = list_a

    elif row_input_1 == "b":
        row_choice_1 = list_b

    elif row_input_1 == "c":
        row_choice_1 = list_c
        
    elif row_input_1 == "d":
        row_choice_1 = list_d
    else:
        print("Invalid")

    #take user input 2 for selected coordinates (second choice)
    current_input_2 = input("Enter coordinates of second selection (a-d)(1-4): ")
    print(current_input_2)
    row_input_2 = current_input_2[0]
    column_input_2 = current_input_2[1]
    count += 1
    if row_input_2 == "a":
        row_choice_2 = list_a

    elif row_input_2 == "b":
        row_choice_2 = list_b

    elif row_input_2 == "c":
        row_choice_2 = list_c
        
    elif row_input_2 == "d":
        row_choice_2 = list_d
    else:
        print("Invalid")

    # if column_input_1 == "1":
    #     row_choice_1 = list_a

    # elif column_input_1 == "2":
    #     row_choice_1 = list_b

    # elif column_input_1 == "3":
    #     row_choice_1 = list_c
        
    # elif column_input_1 == "4":
    #     row_choice_1 = list_d
    # else:
    #     print("Invalid")

    symbol_choice_1 = row_choice_1[int(column_input_1)]
    symbol_choice_2 = row_choice_2[int(column_input_2)]

    print(symbol_choice_1)
    print(symbol_choice_2)

    printBoard()


    if symbol_choice_1 == symbol_choice_2:
        print("yes you did it")

    else: 
        print("guess again")

       
main()

# def flip_card():
#    for index in row:
#        if 

# flip_card()




    

    # overwrite board coordinate '0' with card identity in order to display choice




    
    
    
#    print(count)
       


