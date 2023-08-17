from src import settings as sett
from src.settings import *

import pygame.mouse
import random
import json


pygame.init()


JINGLE = False


WIN = pygame.display.set_mode((WIDTH, HEIGHT))


def save_data(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f)

def load_json(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)

    return data


# future function for displaying items on screen

def draw_screen(win):
    win.fill(bg_color)


    win.blit(toolbar_1, toolPos_1)
    toolbar_1.fill(toolbar_col[1])
    #pygame.draw.rect(win, 'grey',  toolRect_1, 1)


    #pygame.draw.rect(win, border_color, left_border)
    #pygame.draw.rect(win, border_color, right_border)

    # middle cross:
    draw_crosshair(win)

    # screen Y axis:
    if toggle_axis:
        pygame.draw.line(win,'#404040', (center[0], 0), (center[0], HEIGHT))

    # slide bar and slider:
    draw_slider_bar(toolbar_1)
    draw_graduation(toolbar_1)
    draw_slider(toolbar_1)


    write_text(win, chosen_note, 350,420)


def write_screen_info(win):

    info_list = [
        'Show axis: L'
    ]

    # dev info:
    write_text(win, 'toggle dev. control: I', WIDTH-180, 30, size=17)

    if toggle_info:
        write_text(win, 'toggle axis : L', WIDTH-180, 80, size=17)


    write_text(win, pos, 30,30, size=18)



def draw_slider_bar(win):
    start = (0, toolSize_1[1]/2)
    end   = (toolSize_1[0], toolSize_1[1]/2)

    pygame.draw.line(toolbar_1, colors[0], start, end)

def draw_graduation(win):
    S = slider_gridsize
    Cy = toolSize_1[1]/2

    if Note_num % 2 == 0:
        offset = S/2
    else:
        offset = 0


    for i in range(Note_num):
        pygame.draw.line(win, colors[0], (i*S+offset, Cy-6), (i*S+offset, Cy+6))

def draw_slider(win):
    x,y = slider_pos[0] - slider_size[0]/2, slider_pos[1] - slider_size[1]/2

    slider = pygame.Rect((x,y), slider_size)

    pygame.draw.rect(win, colors[0], slider)


def draw_crosshair(win):   # screen middle crossbar

    pygame.draw.rect(win, 'purple', (WIDTH/2-4, HEIGHT/2, 8,1))
    pygame.draw.rect(win, 'purple', (WIDTH / 2, HEIGHT / 2 - 4, 1, 8))



def write_text(win, data, x,y, size=25):
    Font = pygame.font.SysFont('arial', size)
    text_surf = Font.render(str(data), 1, '#A09040')
    win.blit(text_surf, (x,y))


main_run = True

option_run = False
note_input = False
chord_input = False
playing_sound = False


def get_slider_pos(pos):
    x1,y1 = pos
    x2,y2 = toolPos_1

    slider_pos = x1 - x2, y1 - y2

    return slider_pos

def get_grid_pos(pos, gridsize):  # grid won't be visually aligned with even dimensions
    x1,y1 = pos

    x2 = (x1 // gridsize + 1/2) * gridsize

    #x2 = (x1) // gridsize * gridsize
    y2 = (y1 // gridsize + 1/2) * gridsize

    return x2, y2

def move_slider(pos):
    sett.slider_pos = pos


while main_run:

    draw_screen(WIN)
    write_screen_info(WIN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit()
            if event.key == pygame.K_i:
                toggle_info = not toggle_info
            if event.key == pygame.K_l:
                toggle_axis = not toggle_axis

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            pos_x, pos_y = pos

            # slider moves in x position:
            slider_pos = get_slider_pos(pos)[0], slider_pos[1]
            slider_pos = get_grid_pos(slider_pos, slider_gridsize)[0], slider_pos[1]

            chosen_note = value_mapping[slider_pos[0] // slider_gridsize + 2]



    if playing_sound:
        print('~~~~')
        print('playing: ', end=' ')

        play_arpeggio(final_chord, settings.BPM)

        print('~~~~')

        pygame.time.wait(700)

    clock.tick(FPS)
    pygame.display.update()