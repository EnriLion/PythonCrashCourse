class Settings:
    """A class to store all the settings for Sideways Shooter Exercise"""

    def __init__(self):
        """Initialize the game, and create a game resources"""
        # Screen settings
        self.sc_width = 1000
        self.sc_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5
        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
