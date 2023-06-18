import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width # we plase alien in the left corner
        self.rect.y = self.rect.height # we plase alien in the left corner


        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x) #we'll track the horizontal position of each alien precisely

        #Doesn't need a method for drawing it to the screen; we'll use a Pygame group method tha automatically draws all the elements of a group to the screen
