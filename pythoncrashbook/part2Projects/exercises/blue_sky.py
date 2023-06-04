import sys

import pygame

from character import Character

class BlueSky:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((500, 700))
        pygame.display.set_caption("Blue Sky")
        self.bg_color = (225, 220, 90)

        self.ch = Character(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.bg_color)
            self.ch.blitme()

            # Watch for keyboard and mouse events.
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    blue = BlueSky()
    blue.run_game()

