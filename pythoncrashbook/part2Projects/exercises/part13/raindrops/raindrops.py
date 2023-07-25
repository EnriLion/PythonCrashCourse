import sys

import pygame

from settings import Settings

from drizzle import Drizzle

class Raindrops:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Drizzle Exercise")
        self.drizzles = pygame.sprite.Group()
        self._create_fleet()


    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create a star and find the number of stars in a row.
        # Spacing between each star is equal to one star width
        drizzle = Drizzle(self)
        # star_width = star.rect.width
        drizzle_width, drizzle_height = drizzle.rect.size
        available_space_x = self.settings.screen_width - (2 * drizzle_width)
        number_drizzles_x = available_space_x // (2 * drizzle_width)

        # Determine the number of rows of stars that fit on the screen.
        available_space_y = (self.settings.screen_height - (3 * drizzle_height))
        number_rows = available_space_y // (2 * drizzle_height)


        # # Create the first row of stars
        # for star_number in range(number_stars_x):
        #     self._create_star(star_number)

        # Create the full fleet of stars.
        for row_number in range(number_rows):
            for drizzle_number in range(number_drizzles_x):
                self._create_drizzle(drizzle_number, row_number)

    def _create_drizzle(self, drizzle_number, row_number):
        # Create a star and place it in the row.
        drizzle = Drizzle(self)
        drizzle_width, drizzle_height = drizzle.rect.size
        drizzle.x = drizzle_width + 2 * drizzle_width * drizzle_number
        drizzle.rect.x = drizzle.x
        drizzle.rect.y = drizzle.rect.height + 2 * drizzle.rect.height * row_number
        self.drizzles.add(drizzle)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyabord and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)

            # Make the most recently drawn screen visible.
            self.drizzles.draw(self.screen)
            pygame.display.flip()
            self._update_drizzles()

    def _update_drizzles(self):
        """Update the positions fo all aliens in the fleet."""
        self.drizzles.update()


if __name__== '__main__':
    # Make a game instance, and run the game.
    rs = Raindrops()
    rs.run_game()
