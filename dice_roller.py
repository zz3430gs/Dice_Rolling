import random
import A_die



def main():
    print('Welcome to the dice roller, have fun.')
    # BEGIN A LOOP FOR CONTINUEING THE GAME
    keep_rolling=True
    more_dice_to_roll = True

    def print_main_menu():
        print('(1) Roll Some Dice'
            '\n(2) Exit Dice Roller\n')
    # def make_dice_bag():
    #     d4=A_die.Die(4)
    #     dicebag.append(d4)
    #     d6=A_die.Die(6)
    #     dicebag.append(d6)
    #     d8=A_die.Die(8)
    #     dicebag.append(d8)
    #     d10=A_die.Die(10)
    #     dicebag.append(d10)
    #     d12=A_die.Die(12)
    #     dicebag.append(d12)
    #     d20=A_die.Die(20)
    #     dicebag.append(d20)
    #
    # make_dice_bag()

    def display_dice_menu():
        print('Please select a die to roll!'
              '\n1) 4 Sides'
              '\n2) 6 Sides'
              '\n3) 8 Sides'
              '\n4) 10 Sides'
              '\n5) 12 Sides'
              '\n6) 20 Sides')

    # def roll_die(number_of_sides):
    #     dice_result=random.randint(1, number_of_sides)
    #     print('The '+str(number_of_sides)+' sided die rolled a :'+str(dice_result)+'.')

    while keep_rolling==True:
        print_main_menu()
        user_choice=int(input('Please choose an option.\n'))
        if user_choice==1:
            print("ACTIVATE DICE ROLLING MENU")

            while more_dice_to_roll==True:
                display_dice_menu()
                dice_type_selected=int(input('Which type of die would you like to roll?\n'))
                how_many_rolls=int(input("How many times to roll that die?\n"))
                if dice_type_selected==1:
                    print('1')
                    d4 = A_die.Die(4)
                    for n in range(1,how_many_rolls+1):
                        d4.roll_me()
                elif dice_type_selected==2:
                    print('2')
                    d6 = A_die.Die(6)
                    for n in range(1, how_many_rolls + 1):
                        d6.roll_me()
                elif dice_type_selected == 3:
                    print('3')
                    d8 = A_die.Die(8)
                    for n in range(1, how_many_rolls + 1):
                        d8.roll_me()
                elif dice_type_selected == 4:
                    print('4')
                    d10 = A_die.Die(10)
                    for n in range(1, how_many_rolls + 1):
                        d10.roll_me()
                elif dice_type_selected == 5:
                    print('5')
                    d12 = A_die.Die(12)
                    for n in range(1, how_many_rolls + 1):
                        d12.roll_me()
                elif dice_type_selected == 6:
                    print('6')
                    d20 = A_die.Die(20)
                    for n in range(1, how_many_rolls + 1):
                        d20.roll_me()
                elif dice_type_selected>6 or dice_type_selected<1:
                    print("That is not a valid dice type selection.")
                end_of_more_dice_loop=str(input("Do you have more dice to roll? y or n."))
                if end_of_more_dice_loop.lower()=='y':
                    more_dice_to_roll=True
                elif end_of_more_dice_loop=='n':
                    more_dice_to_roll=False


        elif user_choice==2:
            print('Goodbye')
            break
        elif user_choice>2 or user_choice<1:
            print('Sorry that was not an option, please choose an available option.')


main()