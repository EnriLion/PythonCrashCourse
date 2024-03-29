class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # Drizzle settings
        self.drizzle_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents above ; -1 represents below.
        self.fleet_direction = -1

