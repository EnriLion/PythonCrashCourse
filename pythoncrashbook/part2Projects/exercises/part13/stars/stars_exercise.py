import sys

import pygame

from settings import Settings

from star import Star


class Star_exercise:
    """A class to manage the ship."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.stars = pygame.sprite.Group()

        self._create_fleet()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Stars")

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Make an alien.
        star = Star(self)
        self.stars.add(star)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.stars.draw(self.screen)
            # Make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    s = Star_exercise()
    s.run_game()

