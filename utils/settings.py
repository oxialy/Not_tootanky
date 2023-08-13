import pygame
import random
import json

from itertools import cycle

from random import randrange, choice


pygame.init()


WIDTH, HEIGHT = 600,600


pos = 0, 0
pos_x, pos_y = pos


colors = ['#AAAAAA', '#103010']
bg_color = '#08202A'
border_color = 'black'

DIRECTION = {
    -1: pygame.Vector2(0,-1),
    1: pygame.Vector2(0,1),
    -2: pygame.Vector2(-1,0),
    2: pygame.Vector2(1,0)
}

left_border = pygame.Rect(0,0, 45,HEIGHT)
right_border = pygame.Rect(WIDTH-45,0, 45,HEIGHT)

global_path = 'C:\\Users\\jingl\\Documents\\GitHub\\Not_tootanky\\notes\\'

Db_2 = pygame.mixer.Sound(global_path+'c#2_note.wav')


Notes_name = ['c2', 'c#2', 'd2', 'd#2', 'e2', 'f2', 'f#2', 'g2', 'g#2', 'a2', 'a#2', 'b2',
              'c3', 'c#3', 'd3', 'd#3', 'e3', 'f3', 'f#3', 'g3', 'g#3', 'a3', 'a#3', 'b3',
              'c4', 'c#4', 'd4', 'd#4', 'e4', 'f4', 'f#4', 'g4', 'g#4', 'a4', 'a#4', 'b4',]

Notes_path = [name + '_note.wav' for name in Notes_name]


Sound_list = [pygame.mixer.Sound(global_path + path) for path in Notes_path]


def compile_notes_list():
    notes_dict = {}
    for i, (name, sound) in enumerate(zip(Notes_name, Sound_list)):
        notes_dict[name] = {'value': i+1, 'sound': sound}

    return notes_dict

Notes_spec = compile_notes_list()


def map_note_value():
    mapping = {}

    for i, name in enumerate(Notes_spec):
        mapping[i+1] = name

    return mapping

value_mapping = map_note_value()


chords = {
    '5M': [4, 7],
    '5m': [3, 7],
    '5dim': [3,6],
    '6': [],
    '7+': [4, 7, 10],
    '7M': [4,7, 11],
    '7m': [3,7, 10],
    '7dim': [3,6, 9],
    '75dim': [3,6, 10],
    '9M': [4, 7, 10, 14]
}


def get_chord(base_note, chord_name):
    val1 = Notes_spec[base_note]['value']

    chord = [base_note]

    for val2 in chords[chord_name]:

        val_sum = val1 + val2

        chord.append(value_mapping[val_sum])

    return chord

def play_chord(chord):
    for note in chord:
        Notes_spec[note]['sound'].play()
        print(Notes_spec[note])

def play_note(note):
    Notes_spec[note]['sound'].play()

def get_random_notes(n):
    note_list = []
    for i in range(n):
        rand = random.randrange(len(Notes_spec))

        note_list.append(value_mapping[rand + 1])

    return note_list


welcome1 = get_chord('c3', 'M0')
welcome2 = get_chord('a3', 'M0')

print(Notes_spec)

for spec in Notes_spec.values():
    spec['sound'].set_volume(0.3)