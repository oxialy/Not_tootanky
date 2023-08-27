import pygame

pygame.mixer.init()


global_path = './data/notes/'


INTERVAL_VALUE_MAPPING = {
    '2m': 1,
    '2M': 2,
    '3m': 3,
    '3M': 4,
    '4J': 5,
    '4aug': 6,
    '5dim': 6,
    '5J': 7,
    '5aug': 8,
    '6m': 8,
    '6M': 9,
    '7dim': 9,
    '7m': 10,
    '7M': 11,
    '9m': 13,
    '9M': 14
}


chords = {
    '5M': ['3M', '5J'],   # interval values in semitones
    '5m': ['3m', '5J'],
    '5dim': ['3m', '5dim'],
    '5aug': ['3M', '5aug'],

    '6M': ['3m', '6m'],
    '6m': ['3M', '6M'],
    '64M': ['4J', '6M'],
    '64m': ['4J', '6m'],

    '7+': ['3M', '5J', '7m'],
    '65dim': ['3m', '5dim', '6m'],
    '+6': ['3m', '4J', '6M'],
    '+4': ['2M', '4aug', '6M'],
    '7M': ['3M', '5J', '7M'],
    '7m': ['3m', '5J', '7m'],
    '7dim': ['3m', '5dim', '7dim'],
    '75dim': ['3m', '5dim', '7m'],
    '9M': ['3M', '5J', '7m', '9M'],
    '9m': ['3m', '5J', '7m', '9m'],

    '1': []
}



all_naturals = 'C2 D2 E2 F2 G2 A2 B2 C3 D3 E3 F3 G3 A3 B3 C4 D4 E4 F4 G4 A4 B4'.split()

notes_flat  = [note[0] + 'b' + note[1] for note in all_naturals]
notes_sharp = [note[0] + '#' + note[1] for note in all_naturals]

notes_double_flat  = [note[0] + 'bb' + note[1] for note in all_naturals]
notes_double_sharp = [note[0] + '##' + note[1] for note in all_naturals]


FLAT_MAPPING  = {flat: sharp for flat, sharp in zip(notes_flat[1:], notes_sharp)}
SHARP_MAPPING = {sharp: flat for sharp, flat in zip(notes_sharp, notes_flat[1:])}
FLAT_AND_SHARP_MAPPING = FLAT_MAPPING | SHARP_MAPPING

scale_value = [1,  3,  5,  6,  8,  10, 12,  # C:1, D:3, E:5 ...
               13, 15, 17, 18, 20, 22, 24,  # semi-tone value
               25, 27, 29, 30, 32, 34, 36]

MAP_VALUE_TO_NOTE_NATURAL = {value: note for value, note in zip(scale_value, all_naturals)}
MAP_VALUE_TO_NOTE_FLAT    = {value-1: note for value, note in zip(scale_value, notes_flat)}
MAP_VALUE_TO_NOTE_SHARP   = {value+1: note for value, note in zip(scale_value, notes_sharp)}

MAP_VALUE_TO_NOTE_DOUBLE_FLAT  = {value-2: note for value, note in zip(scale_value, notes_double_flat)}
MAP_VALUE_TO_NOTE_DOUBLE_SHARP = {value+2: note for value, note in zip(scale_value, notes_double_sharp)}


MAP_NOTE_TO_VALUE_NATURAL = {note: value for value, note in zip(scale_value, all_naturals)}
MAP_NOTE_TO_VALUE_FLAT    = {note: value-1 for value, note in zip(scale_value, notes_flat)}
MAP_NOTE_TO_VALUE_SHARP   = {note: value+1 for value, note in zip(scale_value, notes_sharp)}

MAP_NOTE_TO_VALUE_DOUBLE_FLAT = {note: value-2 for value, note in zip(scale_value, notes_double_flat)}
MAP_NOTE_TO_VALUE_DOUBLE_SHARP = {note: value-2 for value, note in zip(scale_value, notes_double_sharp)}


# create sound file name and sound file

notes_name = ['C2', 'C#2', 'D2', 'D#2', 'E2', 'F2', 'F#2', 'G2', 'G#2', 'A2', 'A#2', 'B2',
              'C3', 'C#3', 'D3', 'D#3', 'E3', 'F3', 'F#3', 'G3', 'G#3', 'A3', 'A#3', 'B3',
              'C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4', 'G4', 'G#4', 'A4', 'A#4', 'B4'
              ]

Sound_path = [name.lower() + '_note.wav' for name in notes_name]
Sound_list = [pygame.mixer.Sound(global_path + path) for path in Sound_path]

def compile_notes_list(notes):
    notes_dict = {}
    for i, (name, sound) in enumerate(zip(notes, Sound_list)):
        notes_dict[name] = {'value': i+1, 'sound': sound}

    return notes_dict

def create_sound_dict(sound_list):
    sound_dict = {}
    for i, sound in enumerate(sound_list):
        sound_dict[i+1] = sound

    return sound_dict


def map_note_value(start_note):
    mapping = {}

    for i, name in enumerate(Notes_spec):
        mapping[i+1] = name

    return mapping

Notes_spec = compile_notes_list(notes_name)

SOUND_DICT = create_sound_dict(Sound_list)


# mapping "value: note"
# (ex: 1:C2, 2:C#2, 3:D2 ...)
value_mapping = map_note_value('C2')




