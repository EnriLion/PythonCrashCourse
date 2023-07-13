import sys

import pygame

from settings import Settings

from ship import Ship

from bullet import Bullet

class Sideways:
    """Overall to ship game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create a game resources"""
        pygame.init()
        self.settings = Settings()
        self.sc = pygame.display.set_mode((1200, 800))
        self.sc = pygame.display.set_mode((self.settings.sc_width, self.settings.sc_height))
        pygame.display.set_caption("Sideways Shooter Exercise")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        # Set the background color.
        # self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
              # # Watch for keyboard and mouse events.
             # for event in pygame.event.get():
             #     if event.type == pygame.QUIT:
             #         sys.exit()
             # Redraw the screen during each pass through the loop.
             # self.sc.fill(self.bg_color)
             # self.sc.fill(self.settings.bg_color)
             # self.ship.blitme()
             # pygame.display.flip()

             # # Watch for keyboard and mouse events.
             self._check_events()
             self.ship.update()
             self.bullets.update()

             #Get rid of bullets that have disappeared.
             for bullet in self.bullets.copy():
                 if bullet.rect.left >= 1000:
                     self.bullets.remove(bullet)
             print(len(self.bullets))

             self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_UP:
                #     # Move the ship to the up.
                #     # self.ship.rect.y -= 1
                #     self.ship.moving_up = True
                # elif event.key == pygame.K_DOWN:
                #     self.ship.moving_down = True
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                # if event.key == pygame.K_UP:
                #     self.ship.moving_up = False
                # elif event.key == pygame.K_DOWN:
                #     self.ship.moving_down = False
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        """Start the main loop for the game."""
        self.sc.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    side = Sideways()
    side.run_game()
