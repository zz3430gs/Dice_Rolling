import random
import A_die



def main():
    print('Welcome to the dice roller, have fun.')
    # BEGIN A LOOP FOR CONTINUEING THE GAME
    keep_rolling=True

    def print_main_menu():
        print('(1) Roll Some Dice'
            '\n(2) Exit Dice Roller\n')
    def display_dice_menu():
        print('Please select a die to roll!'
              '\n1) 4 Sides'
              '\n2) 6 Sides'
              '\n3) 8 Sides'
              '\n4) 10 Sides'
              '\n5) 12 Sides'
              '\n6) 20 Sides')
    def roll_die(number_of_sides):
        dice_result=random.randint(1, number_of_sides)
        print('The %s sided die rolled a :'+dice_result+'.' %(number_of_sides))

    while keep_rolling==True:
        print_main_menu()
        user_choice=int(input('Please choose an option.\n'))
        if user_choice==1:
            print("ACTIVATE DICE ROLLING MENU")
            more_dice_to_roll=True
            while more_dice_to_roll==True:
                display_dice_menu()
                dice_type_selected=int(input('Which type of die would you like to roll?\n'))
                how_many_rolls=int(input("How many times to roll that die?\n"))
                if dice_type_selected==1:
                    print('1')
                    how_many_rolls*roll_die(4)
                elif dice_type_selected==2:
                    print('2')
                    how_many_rolls * roll_die(6)
                elif dice_type_selected == 3:
                    print('3')
                    how_many_rolls * roll_die(8)
                elif dice_type_selected == 4:
                    print('4')
                    how_many_rolls * roll_die(10)
                elif dice_type_selected == 5:
                    print('5')
                    how_many_rolls * roll_die(12)
                elif dice_type_selected == 6:
                    print('6')
                    how_many_rolls * roll_die(20)
                elif dice_type_selected>6 or dice_type_selected<1:
                    print("That is not a valid dice type selection.")


        elif user_choice==2:
            print('Goodbye')
            break
        elif user_choice>2 or user_choice<1:
            print('Sorry that was not an option, please choose an available option.')


main()