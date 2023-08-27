from .music_variables import Notes_spec, SOUND_DICT, FLAT_AND_SHARP_MAPPING
from .music_functions import get_note_value


import pygame



# sound play:

def play_chord(chord):
    for note in chord:

        play_note(note)


def play_arpeggio(chord, bpm=120):
    for note in chord:
        value = get_note_value(note)

        play_note(value)

        print(note, end=' ')

        pygame.time.delay(round(1000*60/bpm))

    print('')

def play_note(value):
    SOUND_DICT[value].play()

    # {'C#3' : {'value': 3, 'sound': file} }




def change_volume(val):
    for spec in Notes_spec.values():
        spec['sound'].set_volume(val)

