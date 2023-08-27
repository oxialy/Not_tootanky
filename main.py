from utils import *
from utils.settings import chosen_note
from utils.drawing_functions import move_slider, get_pressed_chord, get_pressed_key, highlight_pressed_button
from utils.music_functions import get_chord, get_note_value

from utils.mouse_press import toolbar1_ispressed

from utils.interactive_variables import selected_key, selected_chord_button


import pygame


pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))


def draw_screen(win):

    win.fill(bg_color)


    win.blit(toolbar1, toolbar1_pos)
    win.blit(toolbar2, toolbar2_pos)
    win.blit(toolbar3, toolbar3_pos)
    win.blit(CHORD_SURFACE, CHORD_POSITION)

    toolbar1.fill(colors2['light_blue2'])
    toolbar2.fill(colors2['brown'])
    toolbar3.fill(colors2['light_blue2'])
    CHORD_SURFACE.fill(bg_color)


    staff.draw_lines(toolbar3)
    staff.draw_all_notes(toolbar3)

    draw_chord_buttons(CHORD_SURFACE, chord_buttons)
    draw_piano(toolbar2)

    # slide bar and slider:
    draw_slider_bar(toolbar1)
    draw_graduation(toolbar1)
    draw_slider(toolbar1)


    if toggle_chosen_note:
        show_chosen_note(win, chosen_note)

    if toggle_pos:
        write_text(win, pos, (30,30), size=15)

    # middle cross:
    draw_crosshair(win)

    # screen Y axis:
    if toggle_axis:
        pygame.draw.line(win,'#404040', (center[0], 0), (center[0], HEIGHT))

    # just a random font test; delete later
    if toggle_font:
        disp_font(win)


def write_screen_info(win):

    info_list = [
        'toggle axis:  L',
        'toggle note selection :  N',
        'toggle font test:  F',
        'toggle mouse pos:  P',
        'toggle flat/sharp bass note:  A'
    ]
    all_toggle = [toggle_axis, toggle_chosen_note, toggle_font, toggle_pos, toggle_flat]

    # dev info:
    write_text(win, 'toggle dev. control: I', (WIDTH-180, 30), size=15)

    if toggle_info:
        for i, (info, toggle) in enumerate(zip(info_list, all_toggle)):
            write_text(win, info, (WIDTH-180, 80+i*30), size=15)




def draw_slider_bar(win):

    Cx = toolbar1_size[0] / 2

    start = (Cx - sliderbar_size/2, toolbar1_size[1]/2)
    end   = (Cx + sliderbar_size/2, toolbar1_size[1]/2)

    pygame.draw.line(toolbar1, 'black', start, end)

def draw_graduation(win):
    S = slider_gridsize

    Cx = toolbar1_size[0]/2
    Cy = toolbar1_size[1]/2

    # offset from toolbar left side because slider bar is shorter
    offset2 = Cx - sliderbar_size/2

    # offset if grid dim is even
    if Note_num % 2 == 0:
        offset = 0
    else:
        offset = 0

    for i in range(Note_num):
        start = i*S + offset + offset2, Cy-6
        end   = i*S + offset + offset2, Cy+6
        pygame.draw.line(win, 'black', start, end)

def draw_slider(win):
    x,y = slider_pos[0] - slider_size[0]/2, slider_pos[1] - slider_size[1]/2

    slider = pygame.Rect((x,y), slider_size)

    pygame.draw.rect(win, 'black', slider)


def draw_crosshair(win):   # screen middle crossbar

    pygame.draw.rect(win, 'purple', (WIDTH/2-4, HEIGHT/2, 8,1))
    pygame.draw.rect(win, 'purple', (WIDTH / 2, HEIGHT / 2 - 4, 1, 8))

def draw_piano(win):

    # draw white keys + highlight selected key:
    for key in white_keys:
        key.draw(win)

    if selected_key:
        highlight_pressed_key(win)

   # draw black keys + highlight selected key
    for key in black_keys:
        key.draw(win)

    if selected_key in black_keys:
        highlight_pressed_key(win)

def draw_chord_buttons(win, buttons):
    for button in buttons:
        button.draw(win)

    if selected_chord_button:
        highlight_pressed_button(win)

    for button in buttons:
        button.write(win)


def highlight_pressed_key(win):
    if selected_key:
        button = selected_key.button
        pygame.draw.rect(win, colors2['dark_green'], button)



def show_chosen_note(win, chosen_note):
    if chosen_note:
        if toggle_flat:
            chosen_note_val = get_note_value(chosen_note)
            converted_note = MAP_VALUE_TO_NOTE_FLAT[chosen_note_val]

            write_text(win, converted_note, (395, 420))

        else:
            write_text(win, chosen_note, (350, 420))



def write_text(win, data, pos, size=25):
    x,y = pos

    Font = pygame.font.SysFont('arial', size)
    text_surf = Font.render(str(data), 1, '#A09040')
    win.blit(text_surf, (x,y))

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


main_run = True

option_run = False
note_input = False
chord_input = False
playing_sound = False



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

            if event.key == pygame.K_n:
                toggle_chosen_note = not toggle_chosen_note

            if event.key == pygame.K_f:
                toggle_font = not toggle_font

            if event.key == pygame.K_p:
                toggle_pos = not toggle_pos

            if event.key == pygame.K_a:
                toggle_flat = not toggle_flat

                if chosen_note and chosen_note not in all_naturals:
                    chosen_note = FLAT_AND_SHARP_MAPPING[chosen_note]

                chord = get_chord(chosen_note, selected_chord_button.chord)
                staff.update_notes(chord)

            if event.key == pygame.K_SPACE:
                if chord:
                    play_arpeggio(chord)

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            pos_x, pos_y = pos

            if toolbar1_ispressed(pos):

                # slider moves in x position:
                slider_pos = move_slider(pos)

                chosen_note = value_mapping[slider_pos[0] // slider_gridsize + 0]

                staff.update_notes(chord)

            if toolbar2_rect.collidepoint(pos):
                selected_key = get_pressed_key(pos, black_keys + white_keys)

                if selected_key:
                    chosen_note = selected_key.note
                    if toggle_flat:
                        if chosen_note in notes_sharp:
                            chosen_note = SHARP_MAPPING[chosen_note]
                else:
                    chosen_note = None

                if chosen_note and selected_chord_button:
                    chord = get_chord(chosen_note, selected_chord_button.chord)

                    staff.update_notes(chord)


            elif toolbar4_rect.collidepoint(pos):
                selected_chord_button = get_pressed_chord(pos, chord_buttons)

                if selected_chord_button and chosen_note:
                    chord = get_chord(chosen_note, selected_chord_button.chord)
                else:
                    chord = []

                staff.update_notes(chord)

            else:
                selected_key = None
                selected_chord_button = unison_chord
                chord = []
                staff.update_notes(chord)


    clock.tick(FPS)
    pygame.display.update()