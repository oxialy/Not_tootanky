

import pygame
import random
import json

from itertools import cycle

from random import randrange, choice

from .formatting import pretty_print_note


pygame.init()


chosen_note = 'C3'
chord = []

BPM = 120
VOLUME = 0.3



global_path = './data/notes/'

scale_natural = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

scale_sharp_only = [note + '#' for note in scale_natural]
scale_flat_only = [note + 'b' for note in scale_natural]
scale = scale_natural + scale_sharp_only + scale_flat_only


Notes_name = ['B1',
              'C2', 'C#2', 'D2', 'D#2', 'E2', 'F2', 'F#2', 'G2', 'G#2', 'A2', 'A#2', 'B2',
              'C3', 'C#3', 'D3', 'D#3', 'E3', 'F3', 'F#3', 'G3', 'G#3', 'A3', 'A#3', 'B3',
              'C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4', 'G4', 'G#4', 'A4', 'A#4', 'B4',
              'C5'
]

chromatic_scale_c3 = ['C3', 'C#3', 'D3', 'D#3', 'E3', 'F3', 'F#3', 'G3', 'G#3', 'A3', 'A#3', 'B3']

Flat_enharmonics = ['Cb2', 'Db2', 'Eb2', 'Fb2', 'Gb2', 'Ab2', 'Bb2',
                    'Cb3', 'Db3', 'Eb3', 'Fb3', 'Gb3', 'Ab3', 'Bb3',
                    'Cb4', 'Db4', 'Eb4', 'Fb4', 'Gb4', 'Ab4', 'Bb4']

Sharp_enharmonics = ['E#2', 'B#2', 'E#3', 'B#3', 'E#4', 'B#4']


Sound_path = [name.lower() + '_note.wav' for name in Notes_name]
Sound_list = [pygame.mixer.Sound(global_path + path) for path in Sound_path]


PLAYSOUND = pygame.USEREVENT    # sound playing event


# NotImplemented, Chord class
class Chord:
    def __init__(self):
        self.list = []
        self.index = 0

    def create_chord(self, base_note, chord):

        val1 = Notes_spec[base_note]['value']

        self.list = [base_note]

        for val2 in chord:
            sum_val = val1 + val2

        self.list.append(value_mapping[sum_val])


def play_jingle():
    for chord in all_chords:
        play_arpeggio(chord, 120)

        pygame.mixer.stop()

def compile_notes_list():
    notes_dict = {}
    for i, (name, sound) in enumerate(zip(Notes_name, Sound_list)):
        notes_dict[name] = {'value': i+1, 'sound': sound}

    return notes_dict

def map_note_value(start_note):
    mapping = {}

    for i, name in enumerate(Notes_spec):
        mapping[i+1] = name

    return mapping

def map_scale():    # obsolete
    mapping = {}

    for CX in ['C1', 'C2', 'C3']:
        try:
            C_pos = Notes_name.index(CX)
            break
        except ValueError:
            pass

    for i, scale_note in enumerate(scale):
        #       dict format:
        # {'c': ['c2', 'c3', 'c4']}
        mapping[scale_note] = [Notes_name[i + C_pos], Notes_name[i + C_pos + 12], Notes_name[i + C_pos + 24]]

    return mapping


Notes_spec = compile_notes_list()

# mapping "value: note"
# (ex: 1:C2, 2:C#2, 3:D2 ...)
value_mapping = map_note_value('C2')

#obsolete
#scale_mapping = map_scale()


chords = {
    '5': [4, 7],
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


# enharmonics check and adjusting functions

def augment_flat_enharmonic(note):

    if len(note) == 3:
        augmented = note[0] + note[2]

        return augmented

    else:
        print('error')

def dim_sharp_enharmonic(note):

    if len(note) == 3:
        dim = note[0] + note[2]

        return dim

def get_enharmonic(note):
    if note in scale_sharp_only + Sharp_enharmonics:

        diminished_note = dim_sharp_enharmonic(note)

        val_dim = Notes_spec[diminished_note]['value']

        enharmonic = value_mapping[val_dim + 1]

        return enharmonic

    else:
        augmented_note = augment_flat_enharmonic(note)

        val_aug = Notes_spec[augmented_note]['value']

        enharmonic = value_mapping[val_aug-1]

        return enharmonic


# sound play:

def play_chord(chord):
    for note in chord:

        play_note(note)

        print(Notes_spec[note])

def play_arpeggio(chord, bpm=60):
    for note in chord:

        play_note(note)

        print(note, end=' ')

        pygame.time.delay(round(1000*60/bpm))

    print('')

def play_note(note):
    Notes_spec[note]['sound'].play()

    # {'C#3' : {'value': 3, 'sound': file} }




def change_volume(val):
    for spec in Notes_spec.values():
        spec['sound'].set_volume(val)



# other functions

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



welcome1 = get_chord('C3', '5m')
welcome2 = get_chord('A3', '5M')

all_chords = get_allchords()

print(Notes_spec)

change_volume(VOLUME)