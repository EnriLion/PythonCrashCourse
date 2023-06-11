import pygame

class Rocket:
    """A class to manage the rocket."""

    def __init__(self, re_game):
        """Initialize the rocket and set its starting position."""
        self.screen = re_game.screen
        self.screen_rect = re_game.screen.get_rect()
        self.settings = re_game.settings

        # Load the rocket image and get its rect.
        self.image = pygame.image.load('images/rocketland.bmp')
        self.rect = self.image.get_rect()

        # Start each new rocket at the bottom center of the screen.
        # self.rect.midbottom = self.screen_rect.midbottom#1
        self.rect.center = self.screen_rect.center

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down= False

    def update(self):
        """Update the rocket position based on the movement flag."""
        #Update the rocket's x value, not the rect.
        # if self.moving_right:
        #     self.x += self.settings.rocket_speed
        # if self.moving_left:
        #     self.x -= self.settings.rocket_speed
        # if self.moving_up:
        #     self.y -= self.settings.rocket_speed
        # if self.moving_down:
        #     self.y += self.settings.rocket_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > self.screen_rect.left: #self.moving_left and self.rect.left > 0
            self.x -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed
        if self.moving_up and self.rect.top > -1:
            self.y -= self.settings.rocket_speed

        # Update rect object from self.x.
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the rocket at its current location."""
        self.screen.blit(self.image, self.rect)

