import random
import A_die



def main():
    print('Welcome to the dice roller, have fun.')
    # BEGIN A LOOP FOR CONTINUEING THE GAME
    keep_rolling=True

    def print_main_menu():
        print('(1) Roll Some Dice'
            '\n(2) Exit Dice Roller')

    while keep_rolling==True:
        print_main_menu()
        user_choice=input(int('Please choose an option.'))
        if user_choice==1:
            print("ACTIVATE DICE ROLLING MENU")
        elif user_choice==2:
            print('Goodbye')
            break
        elif user_choice>2 or user_choice<1:
            print('Sorry that was not an option, please choose an available option.')


main()