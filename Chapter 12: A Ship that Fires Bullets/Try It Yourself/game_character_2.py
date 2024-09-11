# 12-2. Game Character:     Find a bitmap image of a game character you like or convert an image to a bitmap.
#                           Make a class that draws the character at the center of the screen, then match the background
#                           colour of the image to the background colour of the screen or vice versa.


import sys
import pygame


class Game:
    def __init__(self):
        """Initialise the game, and create game resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))

        self.bg_colour = 135, 206, 235

        self.character = pygame.image.load(
            "Chapter 12: A Ship that Fires Bullets/Try It Yourself/bad_man.bmp"
        )
        self.character = pygame.transform.scale(self.character, (100, 100))
        self.character_rect = self.character.get_rect()
        self.character_rect.center = self.screen.get_rect().center

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
        self.screen.blit(self.character, self.character_rect)
        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game.
    game = Game()
    game.run_game()
