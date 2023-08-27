from src.settings import WIN, clock, FPS
from src.drawing_variables import bg_color, colors
from src.drawing_functions import draw_screen, disp_mouse_pos

from src import interactive_variables as interact

import pygame


main_run = True


# pygame main loop

while main_run:

    draw_screen(WIN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                main_run = False

        if pygame.mouse.get_pressed()[0]:   # 0 = left mouse button
            interact.pos = pygame.mouse.get_pos()



    clock.tick(FPS)
    pygame.display.update()