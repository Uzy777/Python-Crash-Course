class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialise statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # High score should never be reset.
        self.high_scores = {"easy": 0, "medium": 0, "hard": 0}

    def reset_stats(self):
        """Initialise statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
