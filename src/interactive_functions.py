import pygame.display

from src import settings

from src.sound_variables import unmute_effect, set_all_channels_volume
from src.sound_variables import channel0, channel1, channel2, channel3, channel4, channel5, channel6, channel7

from src.interactive_variables import TOGGLES
from src import interactive_variables as inter



# mouse input
# button hitbox check



def toggle_mute():

    if TOGGLES['MUTE']:
        settings.VOLUME = 0

    else:
        settings.VOLUME = settings.MAX_VOLUME
        channel0.play(unmute_effect)

    set_all_channels_volume(settings.VOLUME)


def toggle_all_info(toggles):
    for toggle in toggles.keys():
        if toggle in ['MUTE', 'RESIZE']:
            pass
        else:
            if inter.HIDE_ALL_INFO:
                toggles[toggle] = False
            else:
                toggles[toggle] = True

def toggle_resize():    # window resize
    if TOGGLES['RESIZE']:
        settings.WIDTH  = 550
        settings.HEIGHT = 550
    else:
        settings.WIDTH  = 700
        settings.HEIGHT = 700

    return pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))



