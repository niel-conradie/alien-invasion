import pygame


class Ship:
    """A class to manage the ship."""

    def __init__(self, game):
        """Initialize the ship and set it's starting position."""
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        # Load the ship image and get it's rect.
        self.image = pygame.image.load("alien-invasion/assets/ship.bmp")
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        # Moving flag.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's x value, not the rect.
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at it's current location."""
        self.screen.blit(self.image, self.rect)
