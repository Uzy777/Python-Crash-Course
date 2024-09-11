# A Ship that Fires Bullets - Starting the Game Project - Creating a Settings Class

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialise the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        # self.bg_colour = (230, 230, 230)      # Grey
        self.bg_colour = (0, 0, 0)              # Black