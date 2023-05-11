from random import randint
class Dice:
    """A class that can be used with the sides of a dice"""
    def __init__(self):
        """A method to write th attributes sides, and the default value"""
        self.sides = 6
    def roll_dice(self):
        """
        Initialize the roll dice 1 to 6 the dice
        """
        random = randint(1, self.sides)
        print(f"Side: {random}")

dice = Dice()
dice.roll_dice()

