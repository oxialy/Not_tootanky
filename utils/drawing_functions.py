from .drawing_variables import *
from .drawing_variables import slider_pos as _slider_pos
from .settings import *
from utils import settings as sett

import pygame


class Button:
    def __init__(self, x,y, w,h, color='grey'):
        self.pos = x, y
        self.x, self.y = self.pos
        self.w, self.h = w,h

        self.color = color

        self.button = pygame.Rect(self.x, self.y, self.w, self.h)

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.button)
        pygame.draw.rect(win, 'black', self.button, 1)


class Pianokey(Button):
    def __init__(self, x,y, w,h, note, color='grey'):
        super().__init__(x,y, w,h)
        self.note = note
        self.color = color

    def set_chosen_note(self):
        sett.chosen_note = self.note


def create_piano_key():

    white_keys = []
    black_keys = []

    size = toolbar2_size[0]/7
    size2 = size - 12

    # white keys
    for i, note in enumerate(['C3','D3','E3','F3','G3','A3','B3']):

        pianokey = Pianokey(i*size, 0, size, 150, note, colors[2])
        white_keys.append(pianokey)

    # black keys
    for i, note in zip([1,2,4,5,6], ['C#3', 'D#3', 'F#3', 'G#3', 'A#3']):

        pianokey = Pianokey(i*size - size2/2, 0, size2, 96, note, 'black')
        black_keys.append(pianokey)

    return white_keys, black_keys



def get_slider_pos(pos):
    offset = (toolSize_1[0] - sliderbar_size) / 2

    x1,y1 = pos
    x2,y2 = toolPos_1[0] + offset, toolPos_1[1]

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




