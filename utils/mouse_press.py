from .drawing_variables import *


def toolbar1_ispressed(pos):
    pos_x, pos_y = pos

    if toolbar1_pos[1] <= pos_y <= toolbar1_pos[1] + toolbar1_size[1]:
        return True
    else:
        return False









