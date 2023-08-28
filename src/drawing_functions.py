from src import settings as sett

from src.drawing_variables import colors, bg_color, FONT15, FONT20

from src.interactive_variables import TOGGLES
from src import interactive_variables as inter

import pygame


def draw_screen(win):

    win.fill(bg_color)


    write_screen_info(win)

    display_mouse_pos(win, inter.pos)

    draw_axis(win)

    disp_mute(win)


def draw_axis(win):

    if TOGGLES['AXIS']:
        pygame.draw.line(win, colors['grey_blue'], (0, sett.HEIGHT/2), (sett.WIDTH, sett.HEIGHT/2))
        pygame.draw.line(win, colors['grey_blue'], (sett.WIDTH/2, 0), (sett.WIDTH/2, sett.HEIGHT))


def display_mouse_pos(win, mouse_pos):

    if TOGGLES['POS']:
        text_pos = sett.WIDTH - 50, sett.HEIGHT - 30
        write_text(win, mouse_pos, text_pos, FONT15)

def disp_mute(win):
    
    if TOGGLES['MUTE']:
        text_color = colors['red']
    else:
        text_color = colors['light_grey']

    text_pos = sett.WIDTH - 70, sett.HEIGHT - 100
    write_text(win, 'volume', text_pos, FONT20, col=text_color)


def write_screen_info(win):

    info_list = [
        'show / hide all:   .  .  .   S',
        'toggle axis:      .  .  .  .   L',
        'toggle chosen note :   N',
        'toggle mouse pos:      P',
        'toggle # / b (bass):      F',
        'toggle window size:    W',
        'toggle mute:    .  .  .  .   M',
    ]

    if TOGGLES['CONTROLS']:
        write_text(win, 'toggle dev. control:      I', (sett.WIDTH-170, 45), FONT15, center=False)

    if TOGGLES['INFO']:
        for i, info in enumerate(info_list):
            write_text(win, info, (sett.WIDTH-170, 85+i*25), FONT15, center=False)



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
