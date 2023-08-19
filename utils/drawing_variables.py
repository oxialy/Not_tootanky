

import pygame


colors = ['#020202', '#AAAAAA', '#909090']
bg_color = '#08202A'
border_color = 'black'

toolbar_col = ['#808080', '#607579', '#604001', '#604001']
button_col = '#808080'

selection_col = '#1B4510'

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
toolbar4_size = 230, 240
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


toggle_info = True
toggle_axis = False
toggle_chosen_note = False