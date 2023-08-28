from src import settings

import pygame

pygame.mixer.init()


unmute_effect = pygame.mixer.Sound('./sound_effects/notif1.wav')
unmute_effect.set_volume(settings.MAX_VOLUME)

# test sounds
sineC = pygame.mixer.Sound('./sound_effects/sineC.wav')
sineF = pygame.mixer.Sound('./sound_effects/sineF.wav')



def set_all_channels_volume(vol):

    vol = min(settings.MAX_VOLUME, vol)

    for channel in all_channels:
        channel.set_volume(vol)



# pygame mixer channels

channel0 = pygame.mixer.Channel(0)
channel1 = pygame.mixer.Channel(1)
channel2 = pygame.mixer.Channel(2)
channel3 = pygame.mixer.Channel(3)

channel4 = pygame.mixer.Channel(4)
channel5 = pygame.mixer.Channel(5)
channel6 = pygame.mixer.Channel(6)
channel7 = pygame.mixer.Channel(7)

all_channels = [channel0, channel1, channel2, channel3, channel4, channel5, channel6, channel7]

set_all_channels_volume(settings.VOLUME)

