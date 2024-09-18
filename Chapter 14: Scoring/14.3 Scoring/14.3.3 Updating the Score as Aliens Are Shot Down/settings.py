class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialise the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        # self.bg_colour = (230, 230, 230)      # Grey
        self.bg_colour = (0, 0, 0)  # Black

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_colour = (255, 255, 255)
        self.bullets_allowed = 6

        # Alien settings
        # self.alien_speed = 2.0
        self.fleet_drop_speed = 80
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.2
        self.initialise_dynamic_settings()

    def initialise_dynamic_settings(self):
        """Initialise settings that change throughout the game."""
        self.ship_speed = 12.0
        self.bullet_speed = 7.0
        self.alien_speed = 1.0

        # Scoring settings
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

    def set_easy_mode(self):
        """Set settings for easy mode."""
        self.ship_speed = 15.0
        self.bullet_speed = 12.0
        self.alien_speed = 0.5

        # Scoring settings
        self.alien_points = 10

    def set_medium_mode(self):
        """Set settings for medium mode."""
        self.ship_speed = 12.0
        self.bullet_speed = 7.0
        self.alien_speed = 1

        # Scoring settings
        self.alien_points = 50

    def set_hard_mode(self):
        """Set settings for hard mode."""
        self.ship_speed = 8.0
        self.bullet_speed = 4.0
        self.alien_speed = 2

        # Scoring settings
        self.alien_points = 100
