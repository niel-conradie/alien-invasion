import pygame


# Initialize pygame mixer.
pygame.mixer.init()

# Loading audio files into variables.
explosion = pygame.mixer.Sound("alien-invasion/assets/audio/sfx_explosion.wav")
laser = pygame.mixer.Sound("alien-invasion/assets/audio/sfx_laser.wav")
