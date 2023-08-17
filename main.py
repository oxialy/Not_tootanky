from src import settings
from src.settings import * 

import pygame.mouse
import random
import json


pygame.init()

JINGLE = False

if JINGLE:
    play_jingle()


#WIN = pygame.display.set_mode((WIDTH, HEIGHT))


def save_data(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f)

def load_json(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)

    return data


# future functions for displaying items on screen
# using Pygame

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


# Check user input:
# - choose_start
# - choose_option
# - choose_note
# - choose_chord

def choose_start(inp):
    def next_input():
        global start_run, note_input

        note_input = True
        start_run = False

    def next_option():
        global start_run, option_run

        option_run = True
        start_run = False


    # prompt:
    # "1. Play chord - 2. Option - \'Q\' to quit \n"

    if inp == '1':
        next_input()

    elif inp == '2':
        next_option()

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
    global note_input
    def next_():
        global note_input, chord_input

        chord_input = True
        note_input = False


    inp = inp.upper()

    if inp in Notes_name:
        note = inp

        next_()
        return note

    elif inp in Flat_enharmonics + Sharp_enharmonics:
        note = get_enharmonic(inp)

        next_()
        return note

    elif inp in scale:    # ex: turn 'C#' into 'C#3'
        note = inp + '3'
        print(note)

        if note in Flat_enharmonics + Sharp_enharmonics:
            print(31)
            note = get_enharmonic(note)
        else:
            print(32)

        next_()
        return note

    elif inp == 'Q':
        note_input = False

    else:
        print('Invalid note. (try: C#2 or Bb3) ')


def choose_chord(note, inp):
    global chord_input

    def next_():
        global chord_input, playing_sound

        playing_sound = True
        chord_input = False


    if inp in chords:
        chord = get_chord(note, inp)  # old chord func

        chord = Chord()     # trying new class Chord
        chord.create_chord(note, inp)

        next_()
        return chord

    elif inp.lower() == 'q':
        chord_input = False

    else:
        print('Invalid chord')


clock = pygame.time.Clock()

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
            # NotImplemented

            inp = input("1. Set BPM - 2. Set volume - 'Q' to quit \n")
            choose_option()

        while note_input:
            inp = input('note: ' + '\n')
            chosen_note = choose_note(inp)

            while chord_input:
                inp = input('chord:  (5M, dim, 7+, 7m, 75dim, ...)' + '\n')
                chord = choose_chord(chosen_note, inp)

    if playing_sound:
        timer = round(1000*60/BPM)

        # trigger PLAYSOUND event every -timer- ms:
        pygame.time.set_timer(PLAYSOUND, timer)

        print('~~~~')
        print('playing: ', end=' ')

    while playing_sound:

        clock.tick(FPS)  # rewrite FPS as settings.FPR ?

        i = chord.index

        for event in pygame.event.get():

            if event.type == PLAYSOUND:
                played_note = chord.chord[i]
                play_note(chord.chord[i])

                chord.index += 1

        if chord.index > len(chord.chord) - 1:   # if chord list exhausted
            pygame.time.set_timer(PLAYSOUND, 0)  # disable PLAYSOUND event
            playing_sound = False

        # random debug print:
        t100 = pygame.time.get_ticks()
        if t100 % 100 < 3:
            print('debug 4: executing "playing_sound" loop', t100)

    pygame.time.wait(700)