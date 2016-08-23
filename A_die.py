import random


class Die():

    def __init__(self, number_of_sides):
        self.number_of_sides=number_of_sides

    def roll_me(self):
        dice_result = random.randint(1, self.number_of_sides)
        print('The ' + str(self.number_of_sides) + ' sided die rolled a :' + str(dice_result) + '.')
