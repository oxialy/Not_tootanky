import pygame
import random
import json

from itertools import cycle

from random import randrange, choice


pygame.init()


colors = ['#AAAAAA', '#103010']
bg_color = '#08202A'
border_color = 'black'


#left_border = pygame.Rect(0,0, 45,HEIGHT)
#right_border = pygame.Rect(WIDTH-45,0, 45,HEIGHT)

BPM = 120
VOLUME = 0.3


global_path = 'C:\\Users\\jingl\\Documents\\GitHub\\Not_tootanky\\notes\\'

scale = ['c','d','e','f','g','a','b']

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

def map_note_value():
    mapping = {}

    for i, name in enumerate(Notes_spec):
        mapping[i+1] = name

    return mapping

def map_scale():
    mapping = {}

    for i, scale_note in enumerate(scale):
        #       dict format:
        # {'c': ['c#2', 'c#3', 'c#4']}
        mapping[scale_note] = [Notes_name[i], Notes_name[i + 12], Notes_name[i + 24]]

    return mapping


Notes_spec = compile_notes_list()

value_mapping = map_note_value()

scale_mapping = map_scale()


chords = {
    '5M': [4, 7],
    '5m': [3, 7],
    '5dim': [3,6],
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

def play_arpeggio(chord, bpm=60):
    for note in chord:
        Notes_spec[note]['sound'].play()
        pygame.time.delay(round(1000*60/bpm))

def play_note(note):
    Notes_spec[note]['sound'].play()

def get_random_notes(n):
    note_list = []
    for i in range(n):
        rand = random.randrange(len(Notes_spec))

        note_list.append(value_mapping[rand + 1])

    return note_list

def get_allchords():
    all_chords = []

    for note in Notes_name[:len(Notes_name)-13]:
        all_chords.append(get_chord(note, '7+'))

    return all_chords

def change_volume(val):
    for spec in Notes_spec.values():
        spec['sound'].set_volume(val)


welcome1 = get_chord('c3', '5m')
welcome2 = get_chord('a3', '5M')

print(Notes_spec)

change_volume(VOLUME)