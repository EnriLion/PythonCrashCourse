class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):# We call this method from __init__ so the statistics are ste properly when the GameStats instance is first created
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):# We also be able to call reset_stats() any time the player starts a new game.
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
