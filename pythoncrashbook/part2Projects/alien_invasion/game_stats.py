class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):# We call this method from __init__ so the statistics are ste properly when the GameStats instance is first created
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        # Start Alien Invasio in an active state.
        # self.game_active = True
        self.game_active = False
        self.high_score = 0
        #the game should start in an inactive state with no way for the player to start it until we make a Play button.
        # Prepare the initial score images.

    def reset_stats(self):# We also be able to call reset_stats() any time the player starts a new game.
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0 # each time a new game starts, we initialize score in reset_stats() rather than __init__()
