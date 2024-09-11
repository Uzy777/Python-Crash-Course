# 12-1. Blue Sky:       Make a Pygame window with a blue background.

import sys
import pygame


class Game:
    def __init__(self):
        """Initialise the game, and create game resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))

        self.bg_colour = 135, 206, 235

    def run_game(self):
        while True:
            self._update_bg_colour()
            self.quit_game()

    def quit_game(self):
        """Respond to keypresses and mouse events."""
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_bg_colour(self):
        self.screen.fill(self.bg_colour)
        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game.
    game = Game()
    game.run_game()
