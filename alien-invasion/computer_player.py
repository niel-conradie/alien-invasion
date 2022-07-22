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

            if self.game.stats.game_active:
                self.game.ship.update()
                self.game._update_bullets()
                self.game._update_aliens()
                self.game._fire_bullet()

            self.game._update_screen()
