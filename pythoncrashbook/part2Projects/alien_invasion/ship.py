#Creating the Ship Class
import pygame

#We import  the pygame module before defining the class. The__init__() method of Ship takes two parameters: the self reference and a reference to the current instance of the alienInvasion.
class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set it s starting position."""
        self.screen = ai_game.screen#we assign the screen to an attribute of Ship, so we can access it eaily in all  the methods in this class
        self.screen_rect = ai_game.screen.get_rect()# we access the screen's rect attribute using the get_rect() method and assign it to self.screen_rect. Doing so allow us to place the ship in the correct location on the scren

        #Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp') #we call the method load pygame.image.load() and give the location of our image and we assgin it to a variable self.image
        self.rect = self.image.get_rect()#we call get_rect() to access the ship surface's rect attribute so we can later use it to place the ship

        #Load the ship image and get its rect.
        self.rect.midbottom = self.screen_rect.midbottom# We position the ship at the bottom center of the screen to do we make the value self.rect.midbottom match the midbootom attribute of the screen'srect

        #--Allowing Continuous Movement--

        # Movement flag
        self.moving_right = False #We add a self.moving_right attribute in the __init__() method and set ti to False initially

        #--Moving Both Left and Right--
        self.moving_left = False

        #--Allowing Continuous Movement--

    def update(self):#We add update() which moves the ship right if the flash is True(The upadte() method method will be called through an instance of Ship, so it's not considered a helper method. and we go to alien_invasion to modify _check_events
        """Update the ship's position based on the movenet flag."""
        if self.moving_right:
            self.rect.x += 1

        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):#we define the blime() mehtod, which draws the image to the scren at the positino specified by self.rect
        """Draw the ship at its curren tlocation."""
        self.screen.blit(self.image, self.rect)

#Pygame is efficient because it lets you treat all game elements like rectangles(rect)

#When we are working with a rect object we can use the x-and y-coordinates of the top, bottom. left and right edges of the rectangle as well as the center( we coul add values as center, centerx, cetnery attributes or if we are working at an edge of the screen as top, bottom, left or right) and also are attributes that combine those properties as midbottom, midtop, midleft and midright). These attributes spare us from having to do calculations that game developers formerly had to do manually, and you'll use them often.

#Note: Pygame the origin(0, 0)is at the top-left corner of the screen, and coordinates increase as you go down and to the right. On a 1200 by 800 screen, the origin is at the top-left corner, and the bottom-right corner has the coordinates(1200, 800). These coordiantes refer to the game window, now the physical screen.
