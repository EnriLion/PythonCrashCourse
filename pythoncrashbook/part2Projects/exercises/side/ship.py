import pygame

from settings import Settings

class Ship:
    """A class to manage the ship."""

    def __init__(self, side_game):
        """Initialize the ship and set its startip position."""
        self.sc = side_game.sc
        self.settings = side_game.settings
        self.sc_rect =  side_game.sc.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.bottomleft = self.sc_rect.bottomleft

        # Store a decimal value for the ship's horizontal position.
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_up and self.rect.top > -1:
            # self.rect.y -= 1
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.sc_rect.bottom:
            # self.rect.y += 1
            self.y += self.settings.ship_speed

        # Update rect object from self.x
        self.rect.y = self.y


    def blitme(self):
        """Draw the ship at its current location."""
        self.sc.blit(self.image, self.rect)
