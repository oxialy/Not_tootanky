from .drawing_variables import *
from .drawing_variables import slider_pos as _slider_pos

from .music_variables import *
from .music_functions import get_note_value

from .interactive_variables import selected_key, selected_chord_button

from utils import settings as sett

import pygame


def highlight_pressed_button(win):
    if selected_chord_button:
        button = selected_chord_button.button
        pygame.draw.rect(win, colors2['light_blue1'], button)


def get_slider_pos(pos):
    offset = (toolbar1_size[0] - sliderbar_size) / 2

    x1,y1 = pos
    x2,y2 = toolbar1_pos[0] + offset, toolbar1_pos[1]

    max_pos = WIDTH/2 + sliderbar_size/2
    min_pos = WIDTH/2 - sliderbar_size/2

    x1 = max(min_pos, min(max_pos, x1))

    pos_x = x1-x2
    pos_y = y1-y2

    slider_pos = pos_x, pos_y

    return slider_pos

def get_grid_pos(pos, gridsize):  # grid won't be visually aligned with even dimensions
    x1,y1 = pos

    X2 = ((x1+gridsize/2) // gridsize + 2) * gridsize
    Y2 = ((y1+gridsize/2) // gridsize + 2) * gridsize

    return X2, Y2

def move_slider(slider_pos):
    slider_pos = get_slider_pos(slider_pos)[0], _slider_pos[1]
    slider_pos = get_grid_pos(slider_pos, slider_gridsize)[0], _slider_pos[1]

    return slider_pos

def get_pressed_key(pos, keys):
    pos_x, pos_y = pos

    offset = toolbar2_pos
    pos = pos_x - offset[0], pos_y - offset[1]

    for key in keys:

        if key.button.collidepoint(pos):
            return key

def get_pressed_chord(pos, buttons):
    pos_x, pos_y = pos

    offset = CHORD_POSITION
    pos = pos_x - offset[0], pos_y - offset[1]

    for button in buttons:

        if button.button.collidepoint(pos):
            return button

def deselect_all(buttons):
    for button in buttons:
        button.selected = False


def write_text(win, data, pos, size=25, color='black', center=True):
    x,y = pos

    Font = pygame.font.SysFont('calibri', size)
    text_surf = Font.render(str(data), 1, color)
    size = text_surf.get_size()

    if center:
        x = x - size[0]/2
        y = y - size[1]/2

    win.blit(text_surf, (x,y))


