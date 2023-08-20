from .settings import *

from .drawing_functions import *

from .drawing_variables import *



staff = Staff()

white_keys, black_keys = create_piano_key()
chord_buttons = create_chord_buttons()

# unisson chord, used for single note
# Does not appear on screen
chord0 = Chord_button( (-10,-10, 0,0), '1')


selected_key = None
selected_chord_button = chord0
