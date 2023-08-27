import random
import pygame

pygame.init()

#WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#WIDTH, HEIGHT = 600,600


pygame.mixer.set_num_channels(5)

a = {1:2}
b = {3:4}
a1 = [1,2]
b1 = [3,4]

print(1 in a)

all_fonts = pygame.font.get_fonts()

c = a|b

print(c[1])