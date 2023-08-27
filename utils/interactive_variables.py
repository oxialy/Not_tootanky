from .settings import *

from .drawing_variables import *

from .sound_playing import *

from.music_functions import get_allchords

from.music_variables import *


import pygame

pygame.font.init()


class Button:
    def __init__(self, rect, color='grey', outline_width=3, outline_col=None, istextbutton=False, text=None,):
        self.x, self.y, self.w, self.h = rect

        self.color = color
        self.outline_col = outline_col
        self.outline_width = outline_width

        self.button = pygame.Rect(self.x, self.y, self.w, self.h)
        self.outline = pygame.Rect(
            self.x - self.outline_width, self.y - self.outline_width,
            self.w + 2 * self.outline_width, self.h + 2 * self.outline_width)

        self.istextbutton = istextbutton
        self.text = text
        self.text_col = 'black'
        self.font = pygame.font.SysFont('arial', 14)


    def draw(self, win):
        pygame.draw.rect(win, self.color, self.button)

        if self.outline_col:
            pygame.draw.rect(win, self.outline_col, self.button, self.outline_width)

        if self.istextbutton:
            self.write(win)

    def write(self, win):
        x = self.x + self.w/2
        y = self.y + self.h/2

        write_text(win, self.text, (x,y), size=14)

    def highlight(self, win):
        pygame.draw.rect(win, colors2['yellow'], self.button)


class Pianokey(Button):
    def __init__(self, rect, note, color, outline_col=None):
        super().__init__(rect)
        self.note = note
        self.color = color

        self.outline_width = 1
        self.outline_col = outline_col



class Chord_button(Button):
    def __init__(self, rect, chord, color='grey'):
        super().__init__(rect)
        self.chord = chord
        self.color = color

        self.text = chord


class Staff:
    linesize = 10

    l = linesize/2

    staffsize = linesize * 4

    note_size = linesize - 1

    offset = toolbar3_size[1]/2 - staffsize/2   # dist between TB border and staff 5th line

    POSITION_LIST = [-2*l, -1*l, 0*l, 1*l, 2*l, 3*l, 4*l, 5*l, 6*l, 7*l, 8*l, 9*l, 10*l]

    i = all_naturals.index('C3')
    POSITION_MAPPING_1 = {name: pos for name, pos in zip(all_naturals[i:], POSITION_LIST)}

    i = notes_flat.index('Cb3')
    POSITION_MAPPING_2 = {name: pos for name, pos in zip(notes_flat[i:], POSITION_LIST)}

    i = notes_sharp.index('C#3')
    POSITION_MAPPING_3 = {name: pos for name, pos in zip(notes_sharp[i:], POSITION_LIST)}

    i = notes_double_flat.index('Cbb3')
    POSITION_MAPPING_4 = {name: pos for name, pos in zip(notes_double_flat[i:], POSITION_LIST)}

    i = notes_double_sharp.index('C##3')
    POSITION_MAPPING_5 = {name: pos for name, pos in zip(notes_double_sharp[i:], POSITION_LIST)}

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

        if note in notes_sharp:
            text_pos = x-11, y-3
            write_text(win, '#', text_pos, size=17, center=False)

        elif note in notes_flat:
            text_pos = x - 11, y - 3
            write_text(win, 'b', text_pos, size=15, center=False)

        elif note in notes_double_flat:
            text_pos = x- 10, y-2
            write_text(win, 'bb', text_pos, size=13, center=False)

        elif note in notes_double_sharp:
            text_pos = x - 14, y - 3
            write_text(win, 'x', text_pos, size=15, center=False)

        if self.POSITION_MAPPING[note] % 10 == 0:
            line_x = x + self.note_size/2
            line_y = y + self.note_size/2
            pygame.draw.line(win, 'black', (line_x-10, line_y), (line_x+10, line_y))
        # pygame.draw.circle(win, 'black', (toolbar3_size[0]/2 - self.linesize + 70, pos), self.note_size/2)

    def update_notes(self, notes):
        self.notes = notes



def create_piano_key():

    white_keys = []
    black_keys = []

    size = toolbar2_size[0]/7   # size of white keys
    size2 = size - 12     # size of black keys

    # white keys
    for i, note in enumerate('C3 D3 E3 F3 G3 A3 B3'.split() ):

        pianokey = Pianokey( (i*size, 0, size, 110), note, colors2['light_grey'], outline_col='black')
        white_keys.append(pianokey)

    # black keys
    for i, note in zip([1,2,4,5,6], 'C#3 D#3 F#3 G#3 A#3'.split() ):

        pianokey = Pianokey( (i*size - size2/2, 0, size2, 78), note, '#101A1A')
        black_keys.append(pianokey)

    return white_keys, black_keys


def create_chord_buttons(button_text_list):

    chord_buttons = []

    for x, text_list in zip(GRID_POSITION_X, button_text_list):
        for y, text in enumerate(text_list):

            chord_rect = x * BUTTON_GRID_SIZE[0], y * 3 * BUTTON_GRID_SIZE[1],\
                         CHORD_BUTTON_SIZE[0], CHORD_BUTTON_SIZE[0]

            chord_button = Chord_button(chord_rect, text, color=colors2['light_grey'])

            chord_buttons.append(chord_button)

    return chord_buttons


def write_text(win, data, pos, size=25, color='black', center=True):
    x,y = pos

    Font = pygame.font.SysFont('calibri', size)
    text_surf = Font.render(str(data), 1, color)
    size = text_surf.get_size()

    if center:
        x = x - size[0]/2
        y = y - size[1]/2

    win.blit(text_surf, (x,y))



staff = Staff()

white_keys, black_keys = create_piano_key()

chord_buttons = create_chord_buttons(button_text_list)
#chord_buttons_B = create_chord_buttons(button_text_list_B)


# unison chord, used for single note
# Does not appear on screen
unison_chord = Chord_button( (-10,-10, 0,0), '1')


selected_key = None
selected_chord_button = unison_chord


#all_chords_test = get_allchords()

change_volume(VOLUME)


