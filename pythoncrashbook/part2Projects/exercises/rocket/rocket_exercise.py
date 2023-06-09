import sys

import pygame

from settings import Settings
from rocket import Rocket

class RocketExercise:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create gam resources."""
        pygame.init()
        self.settings = Settings()

        # self.screen = pygame.display.set_mode((1200, 800))
        self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Rocket Exercise")

        self.rocket = Rocket(self)

        # self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            self.rocket.update()



    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move the ship to the right.
                    # self.rocket.rect.x += 1
                    self.rocket.moving_right = True
                elif event.key == pygame.K_LEFT:
                    # Move the ship to the up
                    # self.rocket.rect.x -= 1
                    self.rocket.moving_left = True
                elif event.key == pygame.K_UP:
                    # Move the ship to the up
                    # self.rocket.rect.y -= 1
                    self.rocket.moving_up = True
                elif event.key == pygame.K_DOWN:
                    # Move the ship to the up
                    # self.rocket.rect.y += 1
                    self.rocket.moving_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.rocket.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.rocket.moving_left = False
                elif event.key == pygame.K_UP:
                    self.rocket.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.rocket.moving_down = False


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()

        # Make the  most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    re = RocketExercise()
    re.run_game()
