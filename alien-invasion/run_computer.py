from alien_invasion import AlienInvasion
from computer_player import ComputerPlayer


def run():
    """Alien Invasion Computer Player."""
    run = AlienInvasion()
    player = ComputerPlayer(run)

    # Starting the game.
    player.start_game()


if __name__ == "__main__":
    run()
