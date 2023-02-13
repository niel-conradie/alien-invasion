from alien_invasion import AlienInvasion


if __name__ == "__main__":
    run = AlienInvasion()

    try:
        # Starting the application.
        run.start_game()
    except KeyboardInterrupt:
        # Stopping the application.
        quit("\n\nProgram Terminated")
