from .drawing_variables import *
from .drawing_variables import slider_pos as _slider_pos
from .settings import *
from utils import settings as sett

import pygame


class Button:
    def __init__(self, rect, color='grey', outline=1):
        self.x, self.y, self.w, self.h = rect

        self.color = color
        self.outline = outline
        self.font = pygame.font.SysFont('arial', 14)
        self.text_col = 'black'

        self.button = pygame.Rect(self.x, self.y, self.w, self.h)

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.button)
        pygame.draw.rect(win, 'black', self.button, self.outline)


class Pianokey(Button):
    def __init__(self, rect, note, color='grey'):
        super().__init__(rect)
        self.note = note
        self.color = color


class Chord_button(Button):
    def __init__(self, rect, chord, color='grey'):
        super().__init__(rect)
        self.chord = chord
        self.color = color
        self.outline = 2

    def set_chord(self):
        sett.chord = self.chord

    def write(self, win):
        x = self.x + self.w/2
        y = self.y + self.h/2

        write_text(win, self.chord, (x,y), size=14)


class Staff:
    linesize = 10

    l = linesize/2

    staffsize = linesize * 4

    note_size = linesize - 1

    offset = toolbar3_size[1]/2 - staffsize/2   # dist between TB border and staff 5th line

    POSITION_LIST = [-2*l, -1*l, 0*l, 1*l, 2*l, 3*l, 4*l, 5*l, 6*l, 7*l, 8*l, 9*l, 10*l]

    i = all_naturals.index('C3')
    POSITION_MAPPING_1 = {name: pos for name, pos in zip(all_naturals[i:], POSITION_LIST)}

    i = all_flats.index('Cb3')
    POSITION_MAPPING_2 = {name: pos for name, pos in zip(all_flats[i:], POSITION_LIST)}

    i = all_sharps.index('C#3')
    POSITION_MAPPING_3 = {name: pos for name, pos in zip(all_sharps[i:], POSITION_LIST)}

    i = all_double_flats.index('Cbb3')
    POSITION_MAPPING_4 = {name: pos for name, pos in zip(all_double_flats[i:], POSITION_LIST)}

    i = all_double_sharps.index('C##3')
    POSITION_MAPPING_5 = {name: pos for name, pos in zip(all_double_sharps[i:], POSITION_LIST)}

    POSITION_MAPPING = \
        POSITION_MAPPING_1 | POSITION_MAPPING_2 | POSITION_MAPPING_3 | POSITION_MAPPING_4 | POSITION_MAPPING_5

    def __init__(self, color ='black'):
        self.notes = []

    def draw_lines(self, win):
        for i in range(5):
            toolsize = toolbar3_size
            start = 0, self.offset + i * self.linesize
            end = toolsize[0], self.offset + i * self.linesize
            pygame.draw.line(win, 'black', start, end)

    def draw_all_notes(self, win):
        start = toolbar3_size[1] - self.offset

        for note in self.notes:
            if note:
                self.draw_note(win, note)

    def draw_note(self, win, note):
        start = toolbar3_size[1] - self.offset

        x = toolbar3_size[0]/2 - self.note_size/2
        y = start - self.POSITION_MAPPING[note] - self.note_size/2
        w = self.note_size
        h = self.note_size

        note_rect = x, y, w, h

        pygame.draw.ellipse(win, 'black', note_rect)

        if note in all_sharps:
            text_pos = x-10, y-5
            write_text(win, '#', text_pos, size=17, center=False)

        elif note in all_flats:
            pass

        if self.POSITION_MAPPING[note] % 10 == 0:
            line_x = x + self.note_size/2
            line_y = y + self.note_size/2
            pygame.draw.line(win, 'black', (line_x-10, line_y), (line_x+10, line_y))
        # pygame.draw.circle(win, 'black', (toolbar3_size[0]/2 - self.linesize + 70, pos), self.note_size/2)

    def update_notes(self, notes):
        self.notes = notes


class Note:
    def __init__(self, value):
        self.value = value

    def draw(self, win):
        pass


def create_piano_key():

    white_keys = []
    black_keys = []

    size = toolbar2_size[0]/7   # size of white keys
    size2 = size - 12     # size of black keys

    # white keys
    for i, note in enumerate('C3 D3 E3 F3 G3 A3 B3'.split() ):

        pianokey = Pianokey( (i*size, 0, size, 110), note, colors[2])
        white_keys.append(pianokey)

    # black keys
    for i, note in zip([1,2,4,5,6], 'C#3 D#3 F#3 G#3 A#3'.split() ):

        pianokey = Pianokey( (i*size - size2/2, 0, size2, 78), note, 'black')
        black_keys.append(pianokey)

    return white_keys, black_keys

def create_chord_buttons():
    size = 40
    dist_x = size + 8
    dist_y = size + 8

    chord_buttons = []

    chord1 = '5M 5m 5dim'.split()
    chord2 = '6M 6m 64M 64m'.split()
    chord3 = '7+ 7M 7m 75dim 7dim'.split()
    chord4 = '9M 9m'.split()

    for i, chord in enumerate(chord1):
        x = 0 * dist_x
        y = i * dist_y

        chord_button = Chord_button( (x, y, size, size), chord=chord, color=button_col)
        chord_buttons.append(chord_button)

    for i, chord in enumerate(chord2):
        x = 1 * dist_x
        y = i * dist_y

        chord_button = Chord_button( (x,y, size, size), chord=chord, color=button_col)
        chord_buttons.append(chord_button)

    for i, chord in enumerate(chord3):
        x = 2 * dist_x + 20
        y = i*dist_y

        chord_button = Chord_button( (x,y, size, size), chord=chord, color=button_col)
        chord_buttons.append(chord_button)

    for i, chord in enumerate(chord4):
        x = 3 * dist_x + 20
        y = i*dist_y

        chord_button = Chord_button( (x,y, size, size), chord=chord, color=button_col)
        chord_buttons.append(chord_button)

    return chord_buttons


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

    offset = toolbar4_pos
    pos = pos_x - offset[0], pos_y - offset[1]

    for button in buttons:

        if button.button.collidepoint(pos):
            return button

def write_text(win, data, pos, size=25, color='black', center=True):
    x,y = pos
    Font = pygame.font.SysFont('arial', size)
    text_surf = Font.render(str(data), 1, color)
    size = text_surf.get_size()

    if center:
        x = x - size[0]/2
        y = y - size[1]/2

    win.blit(text_surf, (x,y))


