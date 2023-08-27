

import pygame


colors = ['#020202', '#AAAAAA', '#808080']

colors2 = {
    'light_grey': '#788080',
    'green': '#405700',
    'dark_green': '#1B4510',
    'warm_yellow': '#806010',
    'green1': '#007030',
    'light_blue1': '#606885',
    'light_blue2': '#607579',
    'brown': '#604000'
}

bg_color = '#112730'
bg_color = '#00222A'


WIDTH, HEIGHT = 700,700
center = WIDTH//2, HEIGHT//2

#left_border = pygame.Rect(0,0, 45,HEIGHT)
#right_border = pygame.Rect(WIDTH-45,0, 45,HEIGHT)


pos = pos_x, pos_y = center

clock = pygame.time.Clock()
FPS = 15

Note_num = 24   # C3 to B3, and C4 to B4


# toolbar3
toolbar3_size = 170, 84
toolbar3 = pygame.Surface(toolbar3_size)
toolbar3_pos = center[0] - toolbar3_size[0]/2, 90

toolbar3_rect = toolbar3.get_rect(topleft=toolbar3_pos)


# toolbar2
toolbar2_size = 230, 118
toolbar2 = pygame.Surface(toolbar2_size)
toolbar2_pos = center[0] - toolbar2_size[0]/2, HEIGHT-225

toolbar2_rect = toolbar2.get_rect(topleft=toolbar2_pos)


# toolbar4
toolbar4_size = 230, 260
toolbar4 = pygame.Surface(toolbar4_size)
toolbar4_pos = 90, center[1] - toolbar4_size[1]/2 - 20

toolbar4_rect = toolbar4.get_rect(topleft=toolbar4_pos)


# toolbar 1
toolbar1_size = 432, 60   # for perfect alignment, x should be a multiple of Note_num
toolbar1 = pygame.Surface(toolbar1_size)

toolbar1_pos = center[0] - toolbar1_size[0]/2, HEIGHT-70

toolbar1_rect = toolbar1.get_rect(topleft=toolbar1_pos)


# slider drawn on toolbar 1

slider_size = 8,20
slider_gridsize = GS = (toolbar1_size[0] - 48) // Note_num

sliderbar_size = (Note_num-1) * slider_gridsize

# initial pos, check if grid dimension is even:
if Note_num % 2 == 0:
    slider_pos = toolbar1_size[0]/2 + GS/2, toolbar1_size[1]/2
else:
    slider_pos = toolbar1_size[0]/2, toolbar1_size[1]/2


slider_rect = pygame.Rect(slider_pos, slider_size)


# surface button will be drawn on:

CHORD_SURFACE = pygame.Surface((272,192))
CHORD_POSITION = 70, HEIGHT / 2 - CHORD_SURFACE.get_height()/2 - 20


# chord buttons

BUTTON_GRID_SIZE = 16, 16

CHORD_BUTTON_SIZE = 41, 41

# button text
CHORD_BUTTON_TEXT_1 = ['5M', '5m', '5dim', '5aug']
CHORD_BUTTON_TEXT_2 = ['6M', '6m', '64M', '64m']

CHORD_BUTTON_TEXT_3 = ['7+', '65dim', '+6', '+4']
CHORD_BUTTON_TEXT_4 = ['7M', '7m', '75dim', '7dim']

CHORD_BUTTON_TEXT_5 = ['9M', '9m']


button_text_list = \
    [CHORD_BUTTON_TEXT_1, CHORD_BUTTON_TEXT_2, CHORD_BUTTON_TEXT_3, CHORD_BUTTON_TEXT_4, CHORD_BUTTON_TEXT_5]


GRID_POSITION_X = [0, 3, 7, 10, 14]

#GRID_POSITION_X = [0, 4, 9, 13, 18]




toggle_info = False
toggle_axis = False
toggle_chosen_note = False
toggle_font = False
toggle_flat = False
toggle_pos = True