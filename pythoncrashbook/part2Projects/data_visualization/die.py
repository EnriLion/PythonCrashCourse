from random import randint


class Die:
    """A clas representing a single die."""

    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        # The init method takes one optional argument is included
        # The number of sides will always be six if no argument is included. If an argument is included, that value will set th enumber of sides on the die
        # The six-sided die is a D6  eight-sided D8,etc
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and number of sides."""
        # Can return the starting value(1), the ending value(num_sides)
        # or any integer between the two
        return randint(1, self.num_sides)
        # The init method takes one optional argument is included
