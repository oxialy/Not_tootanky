import random
import pygame

pygame.init()

#WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#WIDTH, HEIGHT = 600,600


pygame.mixer.set_num_channels(5)

a = {1:2}
b = {3:4}

print(1 in a)

all_fonts = pygame.font.get_fonts()

print(all_fonts)

font1 = random.choice(all_fonts)
font2 = random.choice(all_fonts)
font3 = random.choice(all_fonts)

