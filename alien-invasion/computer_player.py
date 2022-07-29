import pygame


class ComputerPlayer:
    """Computer player for Alien Invasion."""

    def __init__(self, game):
        """Initialize class attributes."""
        self.game = game

    def start_game(self):
        """Replaces the original run_game(), so we can interject our own controls."""
        # Start out in an active state, and hide the mouse.
        self.game.stats.game_active = True
        pygame.mouse.set_visible(False)

        # Start the main loop for the game.
        while True:
            # Still call game._check_events(), so we can use keyboard to quit.
            self.game._check_events()

            # Sweep the ship right and left continuously.
            ship = self.game.ship
            screen_rect = self.game.screen.get_rect()

            if not ship.moving_right and not ship.moving_left:
                # Ship hasn't started moving yet; move to the right.
                ship.moving_right = True
            elif ship.moving_right and ship.rect.right > screen_rect.right - 10:
                # Ship about to hit right edge; move left.
                ship.moving_right = False
                ship.moving_left = True
            elif ship.moving_left and ship.rect.left < 10:
                ship.moving_left = False
                ship.moving_right = True

            if self.game.stats.game_active:
                self.game.ship.update()
                self.game._update_bullets()
                self.game._update_aliens()
                self.game._fire_bullet()

            self.game._update_screen()
