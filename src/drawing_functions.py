from src.settings import WIDTH, HEIGHT
from src.drawing_variables import colors, bg_color, FONT15, FONT20
from src import interactive_variables as inter

import pygame


def draw_screen(win):
    win.fill(bg_color)

    disp_mouse_pos(win, inter.pos)




def disp_mouse_pos(win, mouse_pos):
    text_pos = WIDTH - 50, HEIGHT - 30

    write_text(win, mouse_pos, text_pos, FONT15)




def write_text(win, data, pos, text_font=FONT20, col=colors['light_grey'], center=True):

    text_surf = text_font.render(str(data), 1, col)
    size = text_surf.get_size()

    if center:
        x = pos[0] - size[0]/2
        y = pos[1] - size[1]/2
    else:
        x = pos[0]
        y = pos[1]

    win.blit(text_surf, (x,y))
