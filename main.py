from utils import *

import pygame


pygame.init()


WIN = pygame.display.set_mode((WIDTH, HEIGHT))


def draw_screen(win):
    win.fill(bg_color)


    win.blit(toolbar1, toolbar1_pos)
    win.blit(toolbar2, toolbar2_pos)
    win.blit(toolbar3, toolbar3_pos)
    win.blit(toolbar4, toolbar4_pos)

    toolbar1.fill(toolbar_col[1])
    toolbar2.fill(toolbar_col[2])
    toolbar3.fill(toolbar_col[1])
    toolbar4.fill(bg_color)

    #pygame.draw.rect(win, 'grey', toolbar4_rect, 1)

    staff.draw_lines(toolbar3)
    staff.draw_all_notes(toolbar3)

    draw_chord_buttons(toolbar4)

    # slide bar and slider:
    draw_slider_bar(toolbar1)
    draw_graduation(toolbar1)
    draw_slider(toolbar1)

    if toggle_chosen_note:
        if chosen_note:
            write_text(win, chosen_note, (350,420))

            if chosen_note[:2] in all_sharps:
                write_text(win, 'Gb', (395, 420))

    draw_piano(toolbar2)


    # middle cross:
    draw_crosshair(win)

    # screen Y axis:
    if toggle_axis:
        pygame.draw.line(win,'#404040', (center[0], 0), (center[0], HEIGHT))


def write_screen_info(win):

    info_list = [
        'toggle axis: L',
        'toggle note selection : N'
    ]
    all_toggle = [toggle_axis, toggle_chosen_note]

    # dev info:
    write_text(win, 'toggle dev. control: I', (WIDTH-180, 30), size=15)

    if toggle_info:
        for i, (info, toggle) in enumerate(zip(info_list, all_toggle)):
            write_text(win, info, (WIDTH-180, 80+i*30), size=15)


    write_text(win, pos, (30,30), size=18)



def draw_slider_bar(win):

    Cx = toolbar1_size[0] / 2

    start = (Cx - sliderbar_size/2, toolbar1_size[1]/2)
    end   = (Cx + sliderbar_size/2, toolbar1_size[1]/2)

    pygame.draw.line(toolbar1, colors[0], start, end)

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
        pygame.draw.line(win, colors[0], start, end)

def draw_slider(win):
    x,y = slider_pos[0] - slider_size[0]/2, slider_pos[1] - slider_size[1]/2

    slider = pygame.Rect((x,y), slider_size)

    pygame.draw.rect(win, colors[0], slider)


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

def draw_chord_buttons(win):
    for button in chord_buttons:
        button.draw(win)
        button.write(win)




def highlight_pressed_key(win):
    if selected_key:
        button = selected_key.button
        pygame.draw.rect(win, selection_col, button)

def write_text(win, data, pos, size=25):
    x,y = pos

    Font = pygame.font.SysFont('arial', size)
    text_surf = Font.render(str(data), 1, '#A09040')
    win.blit(text_surf, (x,y))





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


        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            pos_x, pos_y = pos

            if toolbar1_pos[1] <= pos_y <= toolbar1_pos[1] + toolbar1_size[1]:

                # slider moves in x position:
                slider_pos = move_slider(pos)

                chosen_note = value_mapping[slider_pos[0] // slider_gridsize + 0]

                staff.update_notes(chord)

            if toolbar2_rect.collidepoint(pos):
                selected_key = get_pressed_key(pos, black_keys + white_keys)

                if selected_key:
                    chosen_note = selected_key.note
                else:
                    chosen_note = None

                if chosen_note:
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
                chord = []
                staff.update_notes(chord)


    clock.tick(FPS)
    pygame.display.update()