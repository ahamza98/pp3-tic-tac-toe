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

    option = int(input("Select an option: "))

    if option == 1:
        print("playGame")
    elif option == 2:
        rules()
    else:
        print("\n")
        print("Invalid choice. Enter 1 or 2")
        print(" ")
        menu()
    
# Option of Rules
# Play Game
# def rules ()

# def play_game()
# board
# def display_board()

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