import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings#Then use this setting to implement update():

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width # we plase alien in the left corner
        self.rect.y = self.rect.height # we plase alien in the left corner


        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x) #we'll track the horizontal position of each alien precisely

        #Doesn't need a method for drawing it to the screen; we'll use a Pygame group method tha automatically draws all the elements of a group to the screen

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = sel.screen.get_rect()

        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien to the right."""
        self.x += self.settings.alien_speed# Then use the value of self.x to update the position of the alien's rect
        self.rect.x = self.x# Then use the value of self.x to update the position of the alien's rect
