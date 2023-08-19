

import pygame


colors = ['#020202', '#AAAAAA', '#909090']
bg_color = '#08202A'
border_color = 'black'

toolbar_col = ['#808080', '#607598', '#604001']


WIDTH, HEIGHT = 700,700
center = WIDTH//2, HEIGHT//2

#left_border = pygame.Rect(0,0, 45,HEIGHT)
#right_border = pygame.Rect(WIDTH-45,0, 45,HEIGHT)


pos = pos_x, pos_y = center

clock = pygame.time.Clock()
FPS = 15

Note_num = 24   # C3 to B3, and C4 to B4

# toolbar 1
toolSize_1 = 432, 100   # for perfect alignment, x should be a multiple of Note_num
toolbar_1 = pygame.Surface(toolSize_1)

toolPos_1 = center[0] - toolSize_1[0]/2, HEIGHT-200

toolRect_1 = toolbar_1.get_rect(topleft=toolPos_1)


toolbar2_size = 280, 130
toolbar2 = pygame.Surface(toolbar2_size)
toolbar2_pos = center[0] - toolbar2_size[0]/2, 250

toolbar2_rect = toolbar2.get_rect(topleft=toolbar2_pos)


# slider drawn on toolbar 1

slider_size = 8,20
slider_gridsize = GS = (toolSize_1[0] - 48) // Note_num

sliderbar_size = (Note_num-1) * slider_gridsize

# initial pos, check if grid dimension is even:
if Note_num % 2 == 0:
    slider_pos = toolSize_1[0]/2 + GS/2, toolSize_1[1]/2
else:
    slider_pos = toolSize_1[0]/2, toolSize_1[1]/2


slider_rect = pygame.Rect(slider_pos, slider_size)


toggle_info = True
toggle_axis = False
toggle_chosen_note = False