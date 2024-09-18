# 14-3. Challenging Target Practice:        Start with your work from Exercise 14-2. Make the target move faster as
#                                           the game progresses, and restart the target at the original speed when the player clicks Play.


import pygame
import sys
from time import sleep


# Settings class to store game settings.
class Settings:
    def __init__(self):
        """Initialise the game's settings."""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (230, 230, 230)

        # Ship settings
        self.ship_speed = 5.0

        # Bullet settings
        self.bullet_speed = 6.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_colour = (60, 60, 60)
        self.bullets_allowed = 5

        # Target settings
        self.target_width = 50
        self.target_height = 200
        self.target_colour = (255, 0, 0)

        # Game settings
        self.misses_allowed = 3

        # How quickly the game speeds up
        self.speedup_scale = 1.5
        self.initialise_dynamic_settings()

    def initialise_dynamic_settings(self):
        """Initialise settings that change throughout the game."""
        self.target_speed = 1.0

    def increase_speed(self):
        """Increase speed settings."""
        self.target_speed *= self.speedup_scale


# Ship class to manage the player's ship.
class Ship:
    def __init__(self, ai_game):
        """Initialise the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Set up the ship's size and position
        self.image = pygame.Surface((50, 150))  # A rectangle representing the ship
        self.image.fill((0, 0, 255))  # Blue ship
        self.rect = self.image.get_rect()
        self.rect.left = self.screen_rect.left + 20
        self.rect.centery = self.screen_rect.centery

        self.y = float(self.rect.y)
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on movement flags."""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # Update rect object from self.y.
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)


# Bullet class for managing fired bullets.
class Bullet(pygame.sprite.Sprite):
    def __init__(self, ai_game):
        """Create a bullet object."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.colour = self.settings.bullet_colour

        # Create a bullet rect at (0, 0) and set the correct position.
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height
        )
        self.rect.midright = ai_game.ship.rect.midright
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet across the screen."""
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.colour, self.rect)


# Target class for the moving rectangle.
class Target:
    def __init__(self, ai_game):
        """Initialise the target."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Create a target
        self.rect = pygame.Rect(
            self.screen_rect.right - self.settings.target_width,
            0,
            self.settings.target_width,
            self.settings.target_height,
        )
        self.rect.centery = self.screen_rect.centery

        self.y = float(self.rect.y)
        self.moving_down = True

    def update(self):
        """Move the target up and down the screen."""
        if self.moving_down:
            self.y += self.settings.target_speed
            if self.rect.bottom >= self.screen_rect.bottom:
                self.moving_down = False
        else:
            self.y -= self.settings.target_speed
            if self.rect.top <= 0:
                self.moving_down = True

        self.rect.y = self.y

    def draw_target(self):
        """Draw the target to the screen."""
        pygame.draw.rect(self.screen, self.settings.target_colour, self.rect)


# Button class for the Play button.
class Button:
    def __init__(self, ai_game, msg):
        """Initialise button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set button properties.
        self.width, self.height = 200, 50
        self.button_colour = (0, 135, 0)
        self.text_colour = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Prepare the button message.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(
            msg, True, self.text_colour, self.button_colour
        )
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw the button and the message."""
        self.screen.fill(self.button_colour, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


# Main game class
class TargetPractice:
    def __init__(self):
        """Initialise the game and create resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Target Practice")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.target = Target(self)

        # Create game statistics.
        self.misses_left = self.settings.misses_allowed
        self.game_active = False

        # Create the play button.
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start the main game loop."""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self.bullets.update()
                self.target.update()
                self._check_bullet_target_collisions()
                self._check_misses()

            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
        """Handle keypresses."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Handle key releases."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Fire a bullet if limit not reached."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_bullet_target_collisions(self):
        """Check if any bullets have hit the target."""
        collisions = pygame.sprite.spritecollideany(self.target, self.bullets)
        if collisions:
            self.bullets.empty()
            self.target = Target(self)  # Reset target

            self.settings.increase_speed()

    def _check_misses(self):
        """Check if bullets have missed the target."""
        for bullet in self.bullets.copy():
            if bullet.rect.left > self.screen.get_rect().right:
                self.bullets.remove(bullet)
                self.misses_left -= 1
                if self.misses_left == 0:
                    self.game_active = False
                    self.misses_left = self.settings.misses_allowed

    def _check_play_button(self, mouse_pos):
        """Start the game when the Play button is clicked."""
        if self.play_button.rect.collidepoint(mouse_pos) and not self.game_active:
            self.game_active = True
            self.bullets.empty()
            self.target = Target(self)
            self.ship.rect.centery = self.screen.get_rect().centery

            self.settings.initialise_dynamic_settings()

    def _update_screen(self):
        """Update the screen and flip to the new screen."""
        self.screen.fill(self.settings.bg_colour)

        if self.game_active:
            self.ship.blitme()
            self.target.draw_target()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
        else:
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == "__main__":
    # Start the game.
    ai = TargetPractice()
    ai.run_game()
