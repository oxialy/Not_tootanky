from utils import *

import pygame.mouse
import random
import json


pygame.init()

JINGLE = False

all_chords = get_allchords()

if JINGLE:
    for chord in all_chords:
        play_arpeggio(chord, 130)

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


def choose_start(inp):

    global main_run, start_run, option_run, note_input, chord_input

    # prompt:
    # "1. Play chord - 2. Option - \'Q\' to quit \n"

    if inp == '1':
        note_input = True
        chord_input = True
        start_run = False

    elif inp == '2':
        option_run = True
        start_run = False

    elif inp.lower() == 'q':
        quit()

    else:
        print('Invalid choice')

def choose_option(inp):

    global main_run, option_run

    # prompt
    # "1. Set BPM - 2. Set volume - 'Q' to quit \n"

    if inp == '1':

        while True:
            inp = input('BPM (40-250): ')

            if inp.isdigit() and 1 <= int(inp) <= 250:
                settings.BPM = int(inp)
                option_run = False

            break

    elif inp == '2':

        if inp.isdigit() and 0 <= int(inp) <= 100:
            settings.VOLUME = int(inp)

            option_run = False

    elif inp.lower() == 'q':
        option_run = False

    else:
        print('Invalid option')

def choose_note(inp):
    global main_run, note_input

    if inp in Notes_name:
        note = inp

        note_input = False
        return note

    if inp in scale_mapping:
        note = scale_mapping[inp][1]

        note_input = False
        return note

    elif inp.lower() == 'q':
        quit()

    else:
        print('Invalid note: ')


def choose_chord(note, inp):
    global main_run, chord_input, playing_sound

    if inp in chords:
        chord = get_chord(note, inp)

        playing_sound = True
        chord_input = False
        return chord

    elif inp.lower() == 'q':
        quit()

    else:
        print('Invalid chord')


clock = pygame.time.Clock()
FPS = 30

main_run = True

option_run = False
note_input = False
chord_input = False

while main_run:

    start_run = True

    playing_sound = False

    while start_run:
        inp = input("1. Play chord - 2. Option - 'Q' to quit \n")
        choose_start(inp)

        while option_run:
            inp = input("1. Set BPM - 2. Set volume - 'Q' to quit \n")
            choose_option()

        while note_input:
            inp = input('note: ')
            chosen_note = choose_note(inp)

            while chord_input:
                inp = input('chord: ')
                final_chord = choose_chord(chosen_note, inp)

    if playing_sound:
        play_arpeggio(final_chord, settings.BPM)