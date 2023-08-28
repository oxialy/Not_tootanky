from src.settings import WIN, clock, FPS

from src.drawing_functions import draw_screen

from src.interactive_variables import TOGGLES
from src.interactive_functions import toggle_mute, toggle_all_info, toggle_resize

from src import interactive_variables as inter

import pygame
from pygame.locals import *


main_run = True



# pygame main loop

while main_run:

    draw_screen(WIN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_run = False

        if event.type == pygame.KEYDOWN:    # Keyboard press
            if event.key == pygame.K_ESCAPE:
                main_run = False

            elif event.key == pygame.K_s:
                inter.HIDE_ALL_INFO = not inter.HIDE_ALL_INFO
                toggle_all_info(TOGGLES)

            elif event.key in [K_i, K_p, K_l]:
                inter.HIDE_ALL_INFO = False


            if event.key == pygame.K_i:
                TOGGLES['INFO'] = not TOGGLES['INFO']
                TOGGLES['CONTROLS'] = True

            elif event.key == pygame.K_p:
                TOGGLES['POS'] = not TOGGLES['POS']

            elif event.key == pygame.K_l:
                TOGGLES['AXIS'] = not TOGGLES['AXIS']

            elif event.key == pygame.K_m:
                TOGGLES['MUTE'] = not TOGGLES['MUTE']
                toggle_mute()

            elif event.key == pygame.K_w:
                TOGGLES['RESIZE'] = not TOGGLES['RESIZE']
                WIN = toggle_resize()



        if pygame.mouse.get_pressed()[0]:   # 0 = left mouse button
            inter.pos = pygame.mouse.get_pos()



    clock.tick(FPS)
    pygame.display.update()