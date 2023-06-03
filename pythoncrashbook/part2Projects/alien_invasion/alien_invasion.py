#Creating a Pygame Window and Responding to User Input
import sys

import pygame

from settings import Settings

class AlienInvasion:
    """Overall class to manage assets and behavior."""

    def __init__(self):
        """Initialize the game, and create a game resources"""
        pygame.init() #initializes the background settings that Pygame needs to work properly

        self.settings = Settings()# We create an instance of Settions and assing it to self.settings

        # self.screen = pygame.display.set_mode((1200, 800))#we make a variable self.screen(will be available in all methods in the class) to create a display with a tuple that defines the dimensions of the game window which be 1200 pixels wide and 800 high
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))#we ccreate a screen with the attributes of the class settings
        pygame.display.set_caption("Alien Invasion")

        #--Setting the background color--

        #Set the background color.
        # self.bg_color = (230, 230, 230)# show the variants of the RGB colors green(0, 255, 0), blue(0, 0, 255), red(255, 0, 0)

    def run_game(self):#this method contains a while lopp
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():#we write an event loop to listen for events and perform appropriate tasks dependending on the kinds of events that occur any keyboard or mouse event will cause this for loop to run.
                if event.type == pygame.QUIT:# detect and respond to specific events( for ex when the player clicks the game windows; close a pygame.QUIT event is detected and we call sys.exit() to exit the game
                    sys.exit()

            #--Setting the background color--
            # Redraw the screen during each pass through the loop.
            # self.screen.fill(self.bg_color)#we fill the screen the backgroundusing the fill() method, which acts on a surface and takes only one argument: a color
            self.screen.fill(self.settings.bg_color)# instead of creating the background color in the __init__ class we make it with inheritance of the class settings accession to the variable self.bg_color()

            # Make the most recently drawn screen visible.
            pygame.display.flip()# we call it to make the most recently drawn screen visible and is simply drawn an empty screen on each pass through the while loop erasing elements around pygame.display.flip() continually updates the display to show the new positions of game elements and hides the old ones, creating the illusion of smooth movement.

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ali = AlienInvasion()
    ali.run_game()
#At the end of the file we create an isntance of the game, and then call run_game()( in an if block that only runs the file is called directly.
