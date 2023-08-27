# Class: buttons, piano keys, staff
# miscellaneous functions



def create_sound_dict(sound_list):
    sound_dict = {}
    for i, sound in enumerate(sound_list):
        sound_dict[i+1] = sound

    return sound_dict


