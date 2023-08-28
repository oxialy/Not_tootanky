import pygame

pygame.init()


WIDTH, HEIGHT = 700,700

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Not_tootanky Chord Maker')


clock = pygame.time.Clock()
FPS = 15


MAX_VOLUME = 0.5
VOLUME = MAX_VOLUME
previous_volume = VOLUME

BPM = 120


