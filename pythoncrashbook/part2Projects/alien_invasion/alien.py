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

    def check_edges(self):#We need a method to check whether an alien is at either edge, and we need to modify update() to allow each alien to move in appropriate direction
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right or self.rect.left <= 0:#if the alien is at the right edge if the right attribute of its rect is greater than or equal to the right attribute of the screen's rect it's at the left edge if its left value is less than or equal to 0
            return True

    def update(self):
        """Move the alien to the right."""
        # self.x += self.settings.alien_speed# Then use the value of self.x to update the position of the alien's rect
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)#Allow motion to the left or right by multiplying the alien's speed by the value of fleet_direction(if the alien flee_direction is 1 will move to the right and if is -1 the value will be subtracted from the alien's position, movin the alien to the left
        self.rect.x = self.x# Then use the value of self.x to update the position of the alien's rect
