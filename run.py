import time
import colorama 
from colorama import Fore

# player_1 = 0
# player_2 = 0
# winner = none

def welcome():
    """
     A Welcome message to the game
    """

    print("\n")
    print(Fore.BLUE + "Welcome to Tic-Tac-Toe!")
    print("********************************")
    print("\n")
    time.sleep(1)
    print(Fore.RED + "Enjoy a quick game of Tic-Tac_Toe with a friend " +
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

    while True:
        try:
            option = int(input("Select an option: "))

            if option == 1:
                start_game()
                break
            elif option == 2:
                rules()
                break
            else:
                print("\n")
                print("Invalid choice. Enter 1 or 2")
                print(" ")
                menu()
        except ValueError:
            print("\n")
            print("Invalid choice. Enter 1 or 2")
            print(" ")
            menu()
    exit
    

# Play Game
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
    input("Enter any key to exit...\n")
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
    



def start_game():
    """
    Functions to play the game
    and display board
    """
    display_board()

# def switch_player()

# def check_win()

# def check_vertical()
# def check_horizontal()
# def check_diagnol()

# def updateScores

# def play_again()


def main():
    """
    Run all functions
    """
    welcome()
    menu()

main()