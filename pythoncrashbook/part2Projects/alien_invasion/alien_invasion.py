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
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Overall class to manage assets and behavior."""

    def __init__(self):
        """Initialize the game, and create a game resources"""
        pygame.init()


        self.settings = Settings()

        #--Running the Game in Fullscreen Mode--
        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)# we create the screen surface we pass a size of 0,0 and the parameter pygame.FULLSCREE( tells python to figure out a window size that will fill the screen)
        self.settings.screen_width = self.screen.get_rect().width#cause we don't know the width and the height we upate these settings in the screen using width and height attrobutes of the screen's rect to update the settings object

#Note: Make sure you can quit by pressing Q before running the game in fullscreen mode; Pygame offers no default way to quit a game while in fullscreen mode.
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        #--Drawing the Ship to the Screen--

        self.ship = Ship(self)

        #--Setting the background color--

        #Set the background color.
        # self.bg_color = (230, 230, 230)# show the variants of the RGB colors green(0, 255, 0), blue(0, 0, 255), red(255, 0, 0)

        self.bullets = pygame.sprite.Group()

        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def _create_fleet(self):
        """Create the fleet od aliens."""
        # Make an alien.
        # alien = Alien(self)
        # self.aliens.add(alien)
        # Create an alien and find the number of alines in a row.
        # Spacing between each alien is equal to one alien width.
        alien = Alien(self)# We need to know the alien's width and height to place aliens  so we create the instance before we perform calculations
        # alien_width = alien.rect.width# alien width from its rect attribute(we don't have to keep working through the rect attribute and store it to the alien_width value so we don't need to have to keep working through the rect attribute
        alien_width, alien_height = alien.rect.size# We use the attribute size, which contains a tuple with the width and hieght of a rect object

        available_space_x = self.settings.screen_width - (2 * alien_width)#We calculate the horizontal space available for aliens and the number of aliens that can fit into that space

        number_aliens_x = available_space_x // (2 * alien_width)#and the number of aliens that can fit into that space

        # Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height

        available_space_y = (self.settings.screen_height - (3 * alien_height)- ship_height)# we make our calculation right after the calcation for available_space_X; is wrapped in parentheses so the outcome can be split over lines, whcih results in of 79 characters or less as is recommended lines, which resultin in lines of 79 characters or less as ire recommended

        # number_rows = available_space_y // (2 * alien_height)
        number_rows = available_space_y // (4 * alien_height)

        # Create the full fleet of aliens.
        for row_number in range(number_rows):# we create a nested loops one outer and one inner loop(creates the aliens in one row) and the outer counts from 0 to the number of rows we want
            for alien_number in range(number_aliens_x):
                # self._create_alien(alien_number, row_number)
                self._create_alien(alien_number, row_number)


        # Create the first row of aliens.
        # for alien_number in range(number_aliens_x):#we set up  in the main body of the loop, we create a new alien and then set its x-coordinate value to place in the row
            # Create an alien and place it in the row.
            # alien = Alien(self)
            # alien.x = alien_width + 2 * alien_width * alien_number# Each line is pushed to the right one alien width from the left margin and we  multply the alien width by 2 to account for the space each alien

#Note : Depending on the screen width you've chosen, the alignment of the first row of aliens might look slighly on your system
            # alien.rect.x = alien.x
            # self.aliens.add(alien)
            # self._create_alien(alien_number)

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number# We change an alien's y-coordinate value when it's not in the first row and we create an empty space at the top of the screen
        self.aliens.add(alien)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            #--Refactoring: The _check_events() and _update_screen() methods--
            #The _check_events() Method

            self._check_events()#we call the method form inside the while loop un run_game()

            #The _update_screen() Method

            self.ship.update()# when we call update() the group automatically calls updates() for each sprite in the group. The line self.bullets.update() calls bullet.update() for each bullet we place in the group bullets.
            self.bullets.update()

            #Get rid of bullets that have disappared.
            # for bullet in self.bullets.copy():#We can't remove items from a list or group within a for loop we have to loop over a copy of the group; we use the copy() method to set up for loop(enables us to modify bullets inside the loop)
            #     if bullet.rect.bottom <= 0:#Enables us to modify bullets inside the loop. We check each bullet to see whether it has disappeared off the top of the screen at
            #         self.bullets.remove(bullet)# We remove it from bullets
            # # print(len(self.bullets))# We  insert a print to call to show how many bullets currently exist in the game and verify that they're being deleted 
            self._update_bullets()

            self._update_aliens()# In the main while lopp, we already have calls to update the ship and bullet positions, we'll add a call to update the position of each alien

            self._update_screen()







#--Refactoring: The _check_events() and _update_screen() methods--

    #def _check_events(self):#we make a method  whther the player has clicked to close the window in this new method
    #    """Respond to keypress and mouse events."""
    #    #The _check_events() Method

    #    for event in pygame.event.get():
    #        if event.type == pygame.QUIT:
    #            sys.exit()
    #        elif event.type == pygame.KEYDOWN:#Inside the _check_events we add an elif block to the event loop to respond when Pygame detects a KEYDOWN event
    #            if event.key == pygame.K_RIGHT:#The right arrow key represented by it(If the right arrow key was pressed, we move the ship to the right by increasing the value of self...
    #        #         # Move the ship to the right.
    #                # self.ship.rect.x += 5# self.ship.rect.x by 1(moves one pixel right to the x
    #                self.ship.moving_right = True# We modify how the game respons wehn the player presses the right arrow key and instad of changing the psition directly, we set moving_right to True

    #        #--Moving both left and right--
    #            elif event.key == pygame.K_LEFT:
    #                self.ship.moving_left = True

    #        #--Allowing Continuous Movement--
    #        elif event.type == pygame.KEYUP:#we add a new elif block, which responds to KEYP events. When the player releases the right arrow key (K_RIGHT) we set movingright to False and now we modify the run_game()
    #            if event.key == pygame.K_RIGHT:
    #                self.ship.moving_right = False
    #            elif event.key == pygame.K_LEFT:
    #                self.ship.moving_left = False

    #--Refactoring_check_events()--

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        #--Pressing Q to Quit--
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        # new_bullet = Bullet(self)
        # self.bullets.add(new_bullet)
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_fleet_edges(self):
        """Respond appropiately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():#We loop through the fleet and clal check_edges() on each alien
            if alien.check_edges():# if returns True check edges the whole fleet needs to change direction
                self._change_fleet_direction()#we call it and break out of the loop
                break

    def _change_fleet_direction(self):#We loop through all the aliens and drop each one using the setting fleet_drop_speed
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1#We change the value of fleet_direciton multiplying its currenvalye by -1(change the direction to the alien's vertical position) 



    def _update_bullets(self):
        """Update the positions of all aliens in the fleet."""
        self.aliens.update()
        if self.rect.right >= self.rect.left <= 0:
            return True

    def _update_aliens(self): # Is not critical to place this method and I'llplace it just after
        # """Update the positions of all aliens in the fleet."""
        """
        Check if the fleet is at an edge,
          then update the positions of all aliens in the fleet.
        """
        self._check_fleet_edges()
        self.aliens.update()

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self._update_screen()

        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))

        # Shooting Aliens

        # Check for any bullets that have hit aliens.
        #  If so, get rid of the bullet and the alien.
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)# The sprite.groupcollide() function compares the rects of each element in one group with the rects of each element in another group. In this case, it compares each bullet's rect with each alien's rect and returns a dictionary containing the bullets and aliens that have collided.


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        #--Setting the background color--
        self.screen.fill(self.settings.bg_color)
        #--Drawing the Ship to the Screen--
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ali = AlienInvasion()
    ali.run_game()
#At the end of the file we create an isntance of the game, and then call run_game()( in an if block that only runs the file is called directly.

#It is better for us breaking our coude in methods and refactoring our code.



