from alien_invasion import AlienInvasion
from computer_player import ComputerPlayer


if __name__ == "__main__":
    run = AlienInvasion()
    player = ComputerPlayer(run)

    try:
        # Starting the application.
        player.start_game()
    except KeyboardInterrupt:
        # Stopping the application.
        quit("\n\nProgram Terminated")
