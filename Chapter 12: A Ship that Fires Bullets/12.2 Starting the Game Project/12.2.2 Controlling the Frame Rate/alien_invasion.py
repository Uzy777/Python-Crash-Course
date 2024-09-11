# A Ship that Fires Bullets - Starting the Game Project - Controlling the Frame Rate

import sys
import pygame

class AlienInvasion:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialise the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1200, 800))      # Standard res (look to add ultrawide res)
        pygame.display.set_caption("Alien Invasion")


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()