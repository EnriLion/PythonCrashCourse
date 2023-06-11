import pygame

from pygame.sprite import Sprite
#The Bullet class inherits from Sprite with we import from the pygame.sprite module( when we use prites, we can group related elements in our game and act on all the grouped elements at once)

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position"""
        super().__init__()#to create a bulle instance __init__() needs the current instance of AlienInvasion and we call super() to intherit  properly from Sprite
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                self.settings.bullet_height)
        # We create the bullet's rect attribute. The bullet isn't based on image, so we have to build a rect from scratch using the pygame.REct() class  and also requires the x-and y-coordinates of the top-left corner of the rect, and the width and height of the rect at (0,0) we'll move it to the correct location in the next line, because the bullet's position dependes on the ship's position. We get the width and height of the bullet from the values stored in self.settings.
        self.rect.midtop = ai_game.ship.rect.midtop# We set the bullet's midtop attribute to match the ship's midtop attribute; will make the bullet emerge the top of the ship, making it look like the bullet is fired form the ship

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)#We store a decimal value fot eh bullet's y-coordinate so we can make fine adjustments to the bullet's speed

    def update(self):# Manages the bullet's position
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.settings.bullet_speed # When a bullet is fired, moves up the screen, which corresponds to a decreasing y-coordinate value and to update the position we subtract the amount store in settings.bullet_speed from self.y
        # Update the rect position.
        self.rect.y = self.y# We then use the value of self.y to set the value of selr.rect.y


    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)# We want to draw a bullet, we call draw_bullet(). The draw rect() function fills the part of the screen defined by the bullet's rect with the color stored in self.color
