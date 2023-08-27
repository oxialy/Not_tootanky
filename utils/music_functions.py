from .music_variables import *

import pygame



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



def get_chord(base_note, chord_name):

    nat_base_note = base_note[0] + base_note[len(base_note)-1]
    base_index = all_naturals.index(nat_base_note)

    chordA = chords[chord_name]
    chordB = [base_note]

    # construct natural chord
    natural_chord = [nat_base_note]
    for interval in chordA:

        if interval in ['2M', '2m']:
            j = 1
        elif interval in ['3m', '3M']:
            j = 2
        elif interval in ['4J', '4aug']:
            j = 3
        elif interval in ['5dim', '5J', '5aug']:
            j = 4
        elif interval in ['6m', '6M']:
            j = 5
        elif interval in ['7dim', '7m', '7M']:
            j = 6
        elif interval in ['9m', '9m']:
            j = 8

        natural_chord.append(all_naturals[base_index + j])

    for i, interval in enumerate(chordA):
        noteB = natural_chord[i+1]

        interval_val1 = get_note_value(noteB) - get_note_value(base_note)
        interval_val2 = INTERVAL_VALUE_MAPPING[interval]
        diff = interval_val2 - interval_val1

        if diff == -2:
            noteB = get_double_flat_from_natural(noteB)
            chordB.append(noteB)

        elif diff == -1:
            noteB = get_flat_from_natural(noteB)
            chordB.append(noteB)

        elif diff == 0:
            chordB.append(noteB)

        elif diff == 1:
            noteB = get_sharp_from_natural(noteB)
            chordB.append(noteB)

        elif diff == 2:
            noteB = get_double_sharp_from_natural(noteB)
            chordB.append(noteB)


    return chordB


def get_flat_from_natural(note):

    value = MAP_NOTE_TO_VALUE_NATURAL[note]

    note = MAP_VALUE_TO_NOTE_FLAT[value-1]

    return note

def get_sharp_from_natural(note):

    value = MAP_NOTE_TO_VALUE_NATURAL[note]

    note = MAP_VALUE_TO_NOTE_SHARP[value+1]

    return note

def get_double_flat_from_natural(note):

    value = MAP_NOTE_TO_VALUE_NATURAL[note]

    note = MAP_VALUE_TO_NOTE_DOUBLE_FLAT[value-2]

    return note


def get_double_sharp_from_natural(note):

    value = MAP_NOTE_TO_VALUE_NATURAL[note]

    note = MAP_VALUE_TO_NOTE_DOUBLE_SHARP[value+2]

    return note



def get_note_value(note):
    if note in all_naturals:
        return MAP_NOTE_TO_VALUE_NATURAL[note]

    elif note in notes_flat:
        return MAP_NOTE_TO_VALUE_FLAT[note]

    elif note in notes_sharp:
        return MAP_NOTE_TO_VALUE_SHARP[note]

    elif note in notes_double_flat:
        return MAP_NOTE_TO_VALUE_DOUBLE_FLAT[note]

    elif note in notes_double_sharp:
        return MAP_NOTE_TO_VALUE_DOUBLE_SHARP[note]



def get_allchords():
    all_chords = []

    for note in notes_name[:len(notes_name)-13]:
        all_chords.append(get_chord(note, '7+'))

    return all_chords



