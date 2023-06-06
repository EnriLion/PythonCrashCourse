##Creating a Pygame Window and Responding to User Input
#import sys

#import pygame

#from settings import Settings
#from ship import Ship

#class AlienInvasion:
#    """Overall class to manage assets and behavior."""

#    def __init__(self):
#        """Initialize the game, and create a game resources"""
#        pygame.init() #initializes the background settings that Pygame needs to work properly

#        self.settings = Settings()# We create an instance of Settions and assing it to self.settings

#        # self.screen = pygame.display.set_mode((1200, 800))#we make a variable self.screen(will be available in all methods in the class) to create a display with a tuple that defines the dimensions of the game window which be 1200 pixels wide and 800 high
#        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))#we ccreate a screen with the attributes of the class settings
#        pygame.display.set_caption("Alien Invasion")
#        #--Drawing the Ship to the Screen--

#        self.ship = Ship(self)#the call to Ship() requires one argument, an instance of AlienInvasion and the self argument here refers to the current instance of AlienInvasion with this parameter that gives Ship acces to the game's resouces, such as the screen object. We assign this Ship instance of self.ship

#        #--Setting the background color--

#        #Set the background color.
#        # self.bg_color = (230, 230, 230)# show the variants of the RGB colors green(0, 255, 0), blue(0, 0, 255), red(255, 0, 0)

#    def run_game(self):#this method contains a while lopp
#        """Start the main loop for the game."""
#        while True:
#            # Watch for keyboard and mouse events.
#            for event in pygame.event.get():#we write an event loop to listen for events and perform appropriate tasks dependending on the kinds of events that occur any keyboard or mouse event will cause this for loop to run.
#                if event.type == pygame.QUIT:# detect and respond to specific events( for ex when the player clicks the game windows; close a pygame.QUIT event is detected and we call sys.exit() to exit the game
#                    sys.exit()

#            #--Setting the background color--
#            # Redraw the screen during each pass through the loop.
#            # self.screen.fill(self.bg_color)#we fill the screen the backgroundusing the fill() method, which acts on a surface and takes only one argument: a color
#            self.screen.fill(self.settings.bg_color)# instead of creating the background color in the __init__ class we make it with inheritance of the class settings accession to the variable self.bg_color()

#            #--Drawing the Ship to the Screen--

#            self.ship.blitme()#After the filling the background, we draw the ship on the screen by calling ship.blitme() so the ship appears on top of the background

#            # Make the most recently drawn screen visible.
#            pygame.display.flip()# we call it to make the most recently drawn screen visible and is simply drawn an empty screen on each pass through the while loop erasing elements around pygame.display.flip() continually updates the display to show the new positions of game elements and hides the old ones, creating the illusion of smooth movement.

#if __name__ == '__main__':
#    # Make a game instance, and run the game.
#    ali = AlienInvasion()
#    ali.run_game()
##At the end of the file we create an isntance of the game, and then call run_game()( in an if block that only runs the file is called directly.

#Creating a Pygame Window and Responding to User Input
import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage assets and behavior."""

    def __init__(self):
        """Initialize the game, and create a game resources"""
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        #--Drawing the Ship to the Screen--

        self.ship = Ship(self)

        #--Setting the background color--

        #Set the background color.
        # self.bg_color = (230, 230, 230)# show the variants of the RGB colors green(0, 255, 0), blue(0, 0, 255), red(255, 0, 0)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            #--Refactoring: The _check_events() and _update_screen() methods--
            #The _check_events() Method

            self._check_events()#we call the method form inside the while loop un run_game()

            #The _update_screen() Method

            self.ship.update()

            self._update_screen()




#--Refactoring: The _check_events() and _update_screen() methods--

    def _check_events(self):#we make a method  whther the player has clicked to close the window in this new method
        """Respond to keypress and mouse events."""
        #The _check_events() Method

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:#Inside the _check_events we add an elif block to the event loop to respond when Pygame detects a KEYDOWN event
                if event.key == pygame.K_RIGHT:#The right arrow key represented by it(If the right arrow key was pressed, we move the ship to the right by increasing the value of self...
            #         # Move the ship to the right.
                    # self.ship.rect.x += 5# self.ship.rect.x by 1(moves one pixel right to the x
                    self.ship.moving_right = True# We modify how the game respons wehn the player presses the right arrow key and instad of changing the psition directly, we set moving_right to True

            #--Moving both left and right--
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True

            #--Allowing Continuous Movement--
            elif event.type == pygame.KEYUP:#we add a new elif block, which responds to KEYP events. When the player releases the right arrow key (K_RIGHT) we set movingright to False and now we modify the run_game()
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):#
        """Update images on the screen, and flip to the new screen."""
        #--Setting the background color--
        self.screen.fill(self.settings.bg_color)
        #--Drawing the Ship to the Screen--
        self.ship.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ali = AlienInvasion()
    ali.run_game()
#At the end of the file we create an isntance of the game, and then call run_game()( in an if block that only runs the file is called directly.

#It is better for us breaking our coude in methods and refactoring our code.



