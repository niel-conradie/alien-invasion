import pygame


class Ship:
    """A class to manage the ship."""

    def __init__(self, game):
        """Initialize the ship and set it's starting position."""
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # Load the ship image and get it's rect.
        self.image = pygame.image.load("alien-invasion/assets/ship.bmp")
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Moving flag.
        self.moving_right = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right:
            self.rect.x += 1

    def blitme(self):
        """Draw the ship at it's current location."""
        self.screen.blit(self.image, self.rect)
