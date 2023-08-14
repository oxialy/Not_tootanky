from utils import *

import pygame.mouse
import random
import json


pygame.init()

JINGLE = False

all_chords = get_allchords()

if JINGLE:
    for chord in all_chords:
        play_arpeggio(chord, 240)

        pygame.mixer.stop()



#WIN = pygame.display.set_mode((WIDTH, HEIGHT))


def save_data(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f)

def load_json(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)

    return data

def draw_screen(win):
    win.fill(bg_color)

    #pygame.draw.rect(win, border_color, left_border)
    #pygame.draw.rect(win, border_color, right_border)

    # screen middle crossbar:
    pygame.draw.rect(win, 'purple', (WIDTH/2-4, HEIGHT/2, 8,1))
    pygame.draw.rect(win, 'purple', (WIDTH / 2, HEIGHT / 2 - 4, 1, 8))



def write_text(win, data, x,y, size =25):
    Font = pygame.font.SysFont('arial', size)
    text_surf = Font.render(str(data), 1, '#A09040')
    win.blit(text_surf, (x,y))


running = True
stop = False
clock = pygame.time.Clock()
FPS = 30

while running:
    inp = input('note: ')

    if inp in Notes_name:
        note = inp
        running = False
    if inp in scale_mapping:
        note = scale_mapping[inp][1]
        running = False
    elif inp == 'q':
        quit()
    else:
        print('Invalid note: ')

if not stop:
    running = True

while running:
    inp = input('Choose a chord: ')

    if inp in chords:
        final_chord = get_chord(note, inp)
        running = False
    else:
        print('Invalid chord')

while running:
    pass


print(final_chord)

play_arpeggio(final_chord)

pygame.time.wait(1000)