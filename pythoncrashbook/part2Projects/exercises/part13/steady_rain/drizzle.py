import pygame

from pygame.sprite import Sprite

class Drizzle(Sprite):
    """A class to represent a single raindrop in the fleet."""

    def __init__(self, rs_game):
        """Initialize the star and set its starting position."""
        super().__init__()
        self.screen = rs_game.screen
        self.settings = rs_game.settings
        self.screen_rect =  rs_game.screen.get_rect()

        # Load the raindrop image and set its rect attribute.
        self.image = pygame.image.load('images/raindrop.bmp')
        self.rect = self.image.get_rect()

        # Start each new star near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height



        # Store the star's exact horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Move the drizzle to the bottom."""
        self.y -=  (self.settings.drizzle_speed * self.settings.fleet_direction)
        self.rect.y = self.y

