import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, side_game):
        """Initialize the ship and set its startip position."""
        self.sc = side_game.sc
        self.sc_rect =  side_game.sc.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.sc_rect.midbottom

        # Movement flag
        self.moving_up = False
        self.moving_down = False

    def update(self):
        # """Update the ship's position based on the movement flag."""
        if self.moving_up:
            self.rect.y -= 1
        if self.moving_down:
            self.rect.y += 1

    def blitme(self):
        """Draw the ship at its current location."""
        self.sc.blit(self.image, self.rect)
