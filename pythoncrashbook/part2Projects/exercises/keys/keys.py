import sys

import pygame

class Keys:
    """A class to manage the  display"""

    def __init__(self):
        """Initialize the background """
        pygame.init()

        self.screen = pygame.display.set_mode((1000, 400))
        pygame.display.set_caption("Keys")

        # Set the background color.
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()

            # Redraw the screen during each pass throught the loop.
            self.screen.fill(self.bg_color)

            # Make the most recently drawn screen visible
            pygame.display.flip()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)



if __name__ == '__main__':
    # Make a game instance, and run the game.
    key = Keys()
    key.run_game()

##--OUTPUT-----
#Key | ID
#-------|-------
#A | 97
#B | 98
#C | 99
#D | 100
#E | 101
#F | 102
#G | 103
#H | 104
#I | 105
#J | 106
#K | 107
#L | 108
#M | 109
#N | 110
#O | 111
#P | 112
#Q | 113
#R | 114
#S | 115
#T | 116
#U | 117
#V | 118
#W | 119
#X | 120
#Y | 121
#Z | 122

