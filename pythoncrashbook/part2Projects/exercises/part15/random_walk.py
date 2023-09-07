from random import choice


class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0,0).
        self.x_values = [0]
        # We make two lists to hold the x-and y-values
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches desired length.
        while len(self.x_values) < self.num_points:

            # Decide which direction to go and how far to go in that direction.
            x_direction = choice([1, -1])
            # The choose value return 1 for right movenet or -1 for left
            x_distance = choice([0, 1, 2, 3, 4])
            # x_distance select randomly 0 or 4(distance)
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # x and y_step = the length of each step x and y direction

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue
            # The walk doesn't go anywhere if is 0

            # Calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            # To get to the next x-value for the walk we add the value x... to the last value stored

            self.x_values.append(x)
            self.y_values.append(y)

            # When we have these values we append them to x_values and y_values
