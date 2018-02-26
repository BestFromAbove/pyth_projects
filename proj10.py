
# Kristjan von Bulow

##############################################################################
#  Bakers game imitiation
# 
#    Below is method on how program works:
# 1. User is explained how the game works
# 2.User is showed the deck and asked to make an input  
# 3. input will go to functions and will change the cards in the deck 
# 4. Objective is to get all cards into Foundations until they are all King
# 5.When the user wins, they receive the BANNER text and can quit
#############################################################################

import cards #This is necessary for the project


BANNER = """
    __        _____ _   _ _   _ _____ ____  _ _ _ 
    \ \      / /_ _| \ | | \ | | ____|  _ \| | | |
     \ \ /\ / / | ||  \| |  \| |  _| | |_) | | | |
      \ V  V /  | || |\  | |\  | |___|  _ <|_|_|_|
       \_/\_/  |___|_| \_|_| \_|_____|_| \_(_|_|_)

"""


RULES = """
     ____        _             _        ____
    | __ )  __ _| | _____ _ __( )___   / ___| __ _ _ __ ___   ___
    |  _ \ / _` | |/ / _ \ '__|// __| | |  _ / _` | '_ ` _ \ / _ \\
    | |_) | (_| |   <  __/ |    \__ \ | |_| | (_| | | | | | |  __/
    |____/ \__,_|_|\_\___|_|    |___/  \____|\__,_|_| |_| |_|\___|

    Cells:       Cells are numbered 1 through 4. They can hold a
                 single card each.

    Foundations: Foundations are numbered 1 through 4. They are
                 built up by rank from Ace to King for each suit.
                 All cards must be in the foundations to win.

    Tableaus:    Tableaus are numbered 1 through 8. They are dealt
                 to at the start of the game from left to right
                 until all cards are dealt. Cards can be moved one
                 at a time from tableaus to cells, foundations, or
                 other tableaus. Tableaus are built down by rank
                 and cards must be of the same suit.

"""


MENU = """

    Game commands:
    
    TC x y    Move card from tableau x to cell y
    TF x y    Move card from tableau x to foundation y
    TT x y    Move card from tableau x to tableau y
    CF x y    Move card from cell x to foundation y
    CT x y    Move card from cell x to tableau y
    R         Restart the game with a re-shuffle
    H         Display this menu of commands
    Q         Quit the game
    
"""
   
     
def valid_fnd_move(src_card, dest_card):
    """
    Checks to see if card can move into "Foundations" space
    Input: src_card, dest_card
    Output: x = 1 (true) or x = 0 (false)
    """
    x = 0 
    if dest_card == []:
        if src_card.rank() == 1: # if card rank is an ace
            x = 1
            return x # returns true
        else:
            return x # returns false
    else:
        dest_card = dest_card[-1] # takes the last card of the list
        if dest_card.rank() + 1 == src_card.rank(): # if its greater than card
            if src_card.rank() == dest_card.suit(): # puts card in front
                x = 1
                return x # returns true
            else: 
                return x # returns false
            
           
       
  
      
def valid_tab_move(src_card, dest_card):
    """
    Checks to see if card can move into "Tableaus" space
    Input: src_card, dest_card
    Output: x = 1 (true) or x = 0 (false)
    """    
    x = 0
    if dest_card == "": # if there is no card in place, card will move there
        x = 1
        return x # returns true
    else:
        if dest_card.rank() - 1 == src_card.rank(): # if card in place is
        # less than the card input moves
            if src_card.rank() == dest_card.suit(): # if cards are same suit
                x = 1 
                return x # returns true
            else:
                return x # returns false
    
    
def tableau_to_cell(tab, cell):
    """
    Moves a cart from tableau to cell, will go through function (valid_fnd_mo
    ve) to make sure the move is valid
    Input: tab, cell
    output: none
    """    
    i1 = -1 # variable set for last card in list
    temp = tabs[tab][i1] # temp variable is the last card index of list
    if temp == "":
        while temp == "":
            i1 -= 1 # go back through list of cards
            temp = tabs[tab][i1] 
    if cells[cell] == []: # if the cell is empty
        tabs[tab].remove(temp) # removes card from tableau
        cells[cell].append(temp) # adds card to cell
    else:
        raise RuntimeError # will raise an error if user cannot make move
    
            
            
def tableau_to_foundation(tab, fnd):
    """
    This will move a card from tableau to foundation, will go through function
    (valid_fnd_move) to make sure the move is valid
    Input: tab, fnd
    output: none
    """    
    i1 = -1 # variable set for last card in list
    src_card = tabs[tab][i1] # the source card is the last card in list
    if src_card == "":
        while src_card == "":
            i1 -= 1 # goes back through list of cards
            src_card = tabs[tab][i1]
    dest_card = fnds[fnd] # destination location is placed where user  wants
    x = valid_fnd_move(src_card, dest_card) # check if move is valid
    if x == 1: # if true
        temp = tabs[tab][i1] #temp is the card that input wants to move
        tabs[tab].remove(temp) # removes card from tabeau
        fnds[fnd].append(temp) # adds card to foundations
    else:
        raise RuntimeError # will raise an error if x = 0 (invalid move)
            
            
def tableau_to_tableau(tab1, tab2):
    """
    This will move a card from tableau to tableau, will go through function
    (valid_fnd_move) to make sure the move is valid
    Input: tab1, tab2
    output: none
    """    
    i1 = -1 # both variables are set to last position
    i2 = -1
    src_card = tabs[tab1][-1]
    if src_card == "": # same idea going through function above
        while src_card == "":
            i1 -= 1
            src_card = tabs[tab1][i1]
    dest_card = tabs[tab2][i2]
    if dest_card == "":
        i2 -= 1
        dest_card = tabs[tab2][i2]
    x = valid_tab_move(src_card, dest_card) # checks to see if move is valid
    if x == 1:
        temp = tabs[tab1][i1]
        tabs[tab1].remove(temp)
        if i2+1 == 0: #if there is no whitespace,add to top of foundation
            tabs[tab2].append(temp)
        else:
            tabs[tab2][i2+1] = temp
    else:
        raise RuntimeError

def cell_to_foundation(cell, fnd):
    """
    This will move a card from cell to foundation, will go through function
    (valid_fnd_move) to make sure the move is valid
    Input : cell, fnd
    output: none
    """    
    src_card = cells[cell][-1] # will pick last card in list
    dest_card = fnds[fnd][-1] 
    x = valid_fnd_move(src_card, dest_card) # checks to see if valid move
    if x == 1:
        temp = cells[cell].pop() #takes last card in list from cells
        fnds[fnd].append(temp) # appends to foundations
    else:
        raise RuntimeError # will raise error if x = 0 (illegal move)


def cell_to_tableau(cell, tab):
    """
    Will move card from cells to tableaus. will go through function
    (valid_tab_move) to make sure move is valid
    Input: cell, tab
    output: none
    """
    i2 = -1
    src_card = cells[cell][-1]
    dest_card = tabs[tab][i2]
    if dest_card == "":
        while dest_card == "":
            i2 -= 1
            dest_card = tabs[tab][i2]
    x = valid_tab_move(src_card, dest_card) # will make sure move is valid
    if x == 1:
        temp = cells[cell].pop()
        if i2 + 1 == 0: # if there is no whitespace, top of foundation
            tabs[tab].append(temp)
        else:
            tabs[tab][i2+1] = temp
    else:
        raise RuntimeError
              
              
def is_winner(foundations):
    """
    Functions looks at different cards in foundation list, if the cards are
    king in each list, then win = True, if one of them is not a king, 
    win = false
    Input: foundations list
    output: win = true or win = false
    """    
    win = True # default set to true
    for i in range(4):   # looks through four cards in foundation list
        if foundations[i][0].rank() != 13: # if one card is NOT a king
            win = False # user did not win the game yet
    return win # return if user won the game or not



def setup_game():
    """
    The game setup function. It has 4 cells, 4 foundations, and 8 tableaus. All
    of these are currently empty. This function populates the tableaus from a
    standard card deck. 

    Tableaus: All cards are dealt out from left to right (meaning from tableau
    1 to 8). Thus we will end up with 7 cards in tableaus 1 through 4, and 6
    cards in tableaus 5 through 8 (52/8 = 6 with remainder 4).

    This function will return a tuple: (cells, foundations, tableaus)
    """
    
    #You must use this deck for the entire game.
    #We are using our cards.py file, so use the Deck class from it.
    stock = cards.Deck() # takes cards from deck
    stock.shuffle() # shuffle cards every time setup_game() function is called
    
    
    #The game piles are here, you must use these.
    cells = [[], [], [], []]                    #list of 4 lists
    foundations = [[], [], [], []]              #list of 4 lists
    tableaus = [[], [], [], [], [], [], [], []] #list of 8 lists
    
    """ YOUR SETUP CODE GOES HERE """
    
    while len(stock) > 0: # deals the deck into tableaus
        for item in tableaus:
            item.append(stock.deal())
            if len(stock) == 0:
                break
            
        
        
    
    
    return cells, foundations, tableaus


def display_game(cells, foundations, tableaus):
    """
    This will display the updated version of the game with the Cells,
    Foundations, and Tableaus.
    Input: cells, foundations, tableaus
    Output: none
    """
    #Labels for cells and foundations
    print("    =======Cells========  ====Foundations=====")
    print("     --1----2----3----4--  --1----2----3----4--")
    print("    ", end="")

    # to print a card using formatting, convert it to string:
    # print("{}".format(str(card)))
    format_list = []
    
    for item in cells:
        if item == []: 
            format_list.append("[ ]")
        else:
            format_list.append("[" + str(item[-1]) + "]")
    foundation_list = []
    for item in foundations:
        if item == []:
            foundation_list.append("[ ]")
        else:
            foundation_list.append("[" + str(item[-1]) + "]")
    print("{:>5}{:>5}{:>5}{:>5}{:>7}{:>5}{:>5}{:>5} \
    ".format(*format_list, *foundation_list))
    
    print()
    #Labels for tableaus
    print("    =================Tableaus=================")
    print("    ---1----2----3----4----5----6----7----8---")
    
    length = 0
    format1_list = []
    
    for item in tableaus: # will check the max length of tableaus 
        if len(item) > length:
            length = len(item)
            
    for i in range(length): # will set up [] for the max length
        format1_list.append([]) 
    
    for item in tableaus:
        if len(item) < length: 
            while len(item) < length:
                item.append("") # if empty cards, will add whitespace to spot
                
    for item in tableaus:
        for i,ch in enumerate(item): #this will place the items in place
            format1_list[i].append(str(item[i]))
            
    for item in format1_list: # this formats the cards to be in line
        print("{:>9}{:>5}{:>5}{:>5}{:>5}{:>5}{:>5}{:>5}".format(*item))
    
            
    

#HERE IS THE MAIN BODY OF OUR CODE
print(RULES) # prints rules
cells, fnds, tabs = setup_game()
display_game(cells, fnds, tabs)
print(MENU) # prints menu
command = input("prompt :> ").strip().lower()
while command != 'q': # if user does not want to quit
    try:
        if "tc" in command: # if there contains tc in the input
            command_list = command.split()
            tab = int(command_list[1]) - 1 # the -1 takes care of index 0
            cell = int(command_list[2]) - 1
            tableau_to_cell(tab,cell) # goes to function
        elif "tf" in command:
            command_list = command.split() # takes input and splits to list
            tab = int(command_list[1]) - 1 # takes x and makes into tab
            fnd= int(command_list[2]) - 1 # takes y and makes into fnd
            tableau_to_foundation(tab,fnd) # goes to function
        elif "tt" in command:
            command_list = command.split()
            tab1 = int(command_list[1]) - 1
            tab2= int(command_list[2]) - 1
            tableau_to_tableau(tab1,tab2)
        elif "cf" in command: # same idea with above if statements
            command_list = command.split()
            cell = int(command_list[1]) - 1
            fnd = int(command_list[2]) - 1
            cell_to_foundation(cell,fnd)
        elif "ct" in command:
            command_list = command.split()
            cell = int(command_list[1]) - 1
            tab = int(command_list[2]) - 1
            cell_to_tableau(cell,tab)
        elif "r" in command: # restarts game
            cells, fnds, tabs = setup_game()
        elif "h" in command: # prints MENU 
            print(MENU)
        else: # if user inputs other than above inputs
            raise RuntimeError
        
    #Any RuntimeError you raise lands here
    except RuntimeError as error_message: # this is basic error message
        print("{:s}\nTry again.".format(str(error_message)))
        display_game(cells, fnds, tabs)                
    command = input("prompt :> ").strip().lower()


