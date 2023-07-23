#Creating a Settings Class

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 700 #600
        self.bg_color = (230, 230, 230)
        # Ship settings speed
        self.ship_spped = 1.5
        self.ship_limit = 3
        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        # self.bullet_width = 300
        # self.bullet_width = 3000
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        # Alien Settings
        self.alien_speed = 1.5
        # self.alien_speed = 1
        self.fleet_drop_speed = 10# controls how quickly the fleet frops down the screen each time an alien reaches either edge
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1# we could use a text value such as 'left' o ' right' but  the values as if-elif statements testing for fellet directions using values as numbers

        # These settings creat dark gray bullets with a 3 pixels and a hieght of 15 pixels. The bullets will travel slightly slower than the ship.

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
