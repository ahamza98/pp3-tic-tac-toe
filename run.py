import time
import colorama 
from colorama import Fore

# player_1 = 0
# player_2 = 0


def welcome():
    """
     A Welcome message to the game
    """

    print("\n")
    print(Fore.BLUE + "Welcome to Tic-Tac-Toe!")
    print("********************************")
    print("\n")
    time.sleep(1)
    print(Fore.LIGHTMAGENTA_EX + "Enjoy a quick game of Tic-Tac_Toe with a friend " +
                     "and see who wins the most!")
    print("********************************")
    print("\n")
    time.sleep(1)



def menu():
    """
    A function that allows the user to start game
    or look at the rules of the game
    """
    print(Fore.YELLOW + "1) Lets Play!")
    print("2) How does it work?")

    option = 0
    while True:
        option = input("Select an option: ")

        if option.isdigit():
            option = int(option)
            if option == 1 or option == 2:
                break
        print(" ")    
        print("Invalid input")
        print(" ")

    if option == 1:
        start_game()
    elif option == 2:
        rules()
    


def rules():
    
    """
    The rules of Tic Tac Toe. 
    function to return to main()
    """
    
    print(Fore.YELLOW + "Tic-Tac-Toe Rules: ")
    print("\n")
    print("The Rules of the game is simple")
    time.sleep(1)
    print("A multiplayer game")
    time.sleep(1)
    print("The game is played on a grid that's 3 squares by 3 squares")
    time.sleep(1)
    print("You are X and your friend  is O.")
    time.sleep(1)
    print("The first player to get 3 of their marks in a row"
          + "(up, down, across,or diagonally) is the winner.")
    time.sleep(1)
    print("When all 9 squares are full, the game is over.")
    time.sleep(1)
    print(" ")
    time.sleep(1)
    input("Press Enter to exit...\n")
    """
    retuns to the main menu
    """
    
    
    main()

# A board where the game takes place
# create board via list
board = ["   -   ","   -   ","   -   ",
         "   -   ","   -   ","   -   ",
         "   -   ","   -   ","   -   ",]

def display_board():
    """
    Print out the board on the terminal
    """
    print(Fore.GREEN + " ")
    print(board[0] + " | " + board[1] + " | " + board[2] + " | " )
    print("-----------------------------")
    print(board[3] + " | " + board[4] + " | " + board[5] + " | " )
    print("-----------------------------")
    print(board[6] + " | " + board[7] + " | " + board[8] + " | " )
    print("\n")
    

game_running = True

current_player = "   X   "

winner = None

def start_game():
    """
    Functions to play the game
    and display board
    """
    display_board()

    while game_running:
        """
        Functions that will be run while game is being played
        """

        choose_position(current_player)

        check_game_over()

        switch_player()

       
        

        
def choose_position(player):
    """
    Player chooses position from 1-9 via input
    Each input is decreased by 1 as position 1 
    is board[0].
    """
    
   
    position = 0
    while True:
            valid_inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            position = input("choose a position from 1-9: ")
            

            
            if position.isdigit():
                position = int(position)
                if position in valid_inputs:
                    break
                
            
            print(Fore.RED +" ")
            print("Invalid input")
            print(" ")

    if position in valid_inputs:
        board[position-1] = player
        display_board()

    
def check_game_over():
    """
    Function will check if there has been a winner or tie,
    and end the game
    """
    check_win()
        

def check_win():
    """
    function that will check if a player has won.
    """
    # access winner variable
    global winner

    vertical_winner = check_vertical()
    horizontal_winner = check_horizontal()
    diagnol_winner = check_diagnol()

    # Change the value of winner if there is a winner
    if vertical_winner:
        winner = vertical_winner
    elif horizontal_winner:
        winner = horizontal_winner
    elif diagnol_winner:
        winner = diagnol_winner



def check_vertical():
    """
    function that check if a row has three same inputs.
    """
    # Set winner to global to access
    global game_running

    vert_1 = board[0] == board[3] == board[6] != "   -   "
    vert_2 = board[1] == board[4] == board[7] != "   -   "
    vert_3 = board[2] == board[5] == board[8] != "   -   "

    # game_running will end when there is a vertical winner
    if vert_3 or vert_2 or vert_1:
        game_running = False

    # return statements (X or O) for each vertical winner
    if vert_1:
        return board[6]
    if vert_2:
        return board[7]
    if vert_3:
        return board[8]

def check_horizontal():
    """
    function that check if a column has three same inputs.
    """
    # Set winner to global to access
    global game_running

    hori_1 = board[0] == board[1] == board[2] != "   -   "
    hori_2 = board[3] == board[4] == board[5] != "   -   "
    hori_3 = board[6] == board[7] == board[8] != "   -   "

    # game_running will end when there is a horizontal winner
    if hori_3 or hori_2 or hori_1:
        game_running = False

    # return statements (X or O) for each horizontal winner
    if hori_1:
        return board[2]
    if hori_2:
        return board[5]
    if hori_3:
        return board[8]


def check_diagnol():
    """
    function that check if a diagnol has three same inputs.
    only need to diagnols
    """
    # Set winner to global to access
    global game_running

    diag_1 = board[0] == board[4] == board[8] != "   -   "
    diag_2 = board[2] == board[4] == board[6] != "   -   "
    

    # game_running will end when there is a diagnol winner
    if  diag_2 or diag_1:
        game_running = False

    # return statements (X or O) for each diagnol winner
    # Both diagnols have the common board position [4]
    if diag_1 or diag_2:
        return board[4]
    
def switch_player():
    """
    function that changes from
    player X to player O
    and O to X
    """
    # Set current player to global to access 
    global current_player
    if current_player == "   X   ":
        current_player = "   O   "
    elif current_player == "   O   ":
         current_player = "   X   "
    return
    
# check_tie()

# def updateScores
# def play_again()


def main():
    """
    Run all functions
    """
    welcome()
    menu()

main()