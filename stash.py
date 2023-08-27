# random code stash

#
#



chords = {
    '5': [4, 7],   # interval values in semitones
    '5M': [4, 7],
    '5m': [3, 7],
    '5dim': [3,6],

    '6M': [3, 8],
    '6m': [4, 9],
    '64M': [5, 9],
    '64m': [5, 8],

    '7+': [4,7, 10],
    '7M': [4,7, 11],
    '7m': [3,7, 10],
    '7dim': [3,6, 9],
    '75dim': [3,6, 10],
    '9M': [4,7, 10, 14],
    '9m': [3,7, 10, 13],

    '1': []
}

notes_sharp = [
              'C2', 'C#2', 'D2', 'D#2', 'E2', 'F2', 'F#2', 'G2', 'G#2', 'A2', 'A#2', 'B2',
              'C3', 'C#3', 'D3', 'D#3', 'E3', 'F3', 'F#3', 'G3', 'G#3', 'A3', 'A#3', 'B3',
              'C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4', 'G4', 'G#4', 'A4', 'A#4', 'B4',
              'C5'
]

notes_flat = 'C Db D Eb E F Gb G Ab A Bb B'.split()

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


def save_data(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f)

def load_json(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)

    return data



def next_input():
    global start_run, note_input

    note_input = True
    start_run = False


def next_option():
    global start_run, option_run
    option_run = True
    start_run = False



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



def convert_enharmonics(chord):
    converted_chord = []

    for note in chord:
        if note in flat_enharmonics:
            converted_chord.append(FLAT_MAPPING[note])

        elif note in double_flat_enharmonics:
            converted_chord.append(DOUBLE_FLAT_MAPPING[note])

        elif note in sharp_enharmonics:
            converted_chord.append(SHARP_MAPPING[note])

        elif note in double_sharp_enharmonics:
            converted_chord.append(DOUBLE_SHARP_MAPPING[note])

        else:
            converted_chord.append(note)

    return converted_chord



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


def map_note_value(start_note):
    mapping = {}

    for i, name in enumerate(Notes_spec):
        mapping[i+1] = name

    return mapping


Notes_spec = compile_notes_list(Notes_name) | compile_notes_list(Notes_name_flat)


# mapping "value: note"
# (ex: 1:C2, 2:C#2, 3:D2 ...)
value_mapping = map_note_value('C2')


def disp_font(win):
    all_fonts = pygame.font.get_fonts()
    GRID_SIZE = 30

    for i in range(9):
        font_index = i + pos_y // 8
        font_index = min(len(all_fonts)-1, font_index)

        font_name = all_fonts[font_index]

        Font = pygame.font.SysFont(font_name, 16)
        text_surf = Font.render(str(font_name) + ': ' + str(font_index), 1, '#A09040')
        win.blit(text_surf, (30, 300 + i * GRID_SIZE))


