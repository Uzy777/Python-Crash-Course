class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialise the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        # self.bg_colour = (230, 230, 230)      # Grey
        self.bg_colour = (0, 0, 0)              # Black

        # Ship settings
        self.ship_speed = 12

        # Bullet settings
        self.bullet_speed = 8.0
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_colour = (255, 255, 255)
        self.bullets_allowed = 8

        # Alien settings
        self.alien_speed = 1.0