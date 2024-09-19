class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialise statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # High score should never be reset.
        # self.easy_highscore = open("Projects/alien_invasion/highscores/easy_highscore.txt", "w")
        self.high_scores = {"easy": 0, "medium": 0, "hard": 0}
        self.load_high_scores()  # Load high scores for all modes

    def reset_stats(self):
        """Initialise statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def saving_high_score(self, mode):
        """Save the high score to a file specific to the game mode."""
        filename = f"Projects/alien_invasion/highscores/{mode}_highscore.txt"
        with open(filename, "w") as file:
            file.write(str(self.high_scores[mode]))

    def load_high_scores(self):
        """Load the high scores from files for all modes."""
        for mode in self.high_scores:
            filename = f"Projects/alien_invasion/highscores/{mode}_highscore.txt"
            try:
                with open(filename) as file:
                    content = file.read().strip()
                    if content:
                        self.high_scores[mode] = int(content)
            except FileNotFoundError:
                self.high_scores[mode] = 0
