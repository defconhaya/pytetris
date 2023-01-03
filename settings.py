import pygame as pg

vec = pg.math.Vector2

FPS = 60
FIELD_COLOR = (48, 39, 32)
BG_COLOR = (24, 89, 117)

SPRITE_DIR_PATH = 'sprites'
# FONTH_PATH ='fonts/ChubbyDotty.ttf'
FONTH_PATH ='fonts/HennyPenny-Regular.ttf'


ANIM_TIME_INTERVAL = 180
FAST_ANIM_TIME_INTERVAL = 15

TILE_SIZE = 30
FIELD_SIZE = FIELD_W, FIELD_H = 10, 20
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE

INIT_POS_OFFSET = vec(FIELD_W //2 -1, 0)
NEXT_POS_OFFSET = vec(FIELD_W * 1.3, FIELD_H * 0.45)

MOVE_DIRECTIONS = {'left': vec(-1,0), 'right': vec(1,0), 'down':vec(0,1)}

FIELD_SCALE_W, FIELD_SCALE_H = 1.7, 1.0
WIN_RES = WIN_W, WIN_H = FIELD_RES[0] * FIELD_SCALE_W, FIELD_RES[1] * FIELD_SCALE_H

TETROMINOES = {
    'T': [(0, 0), (-1, 0), (1, 0), (0, -1)],   # red
    'O': [(0, 0), (0, -1), (1, 0), (1, -1)],   # green
    'J': [(0, 0), (-1, 0), (0, -1), (0, -2)],  # blue
    'L': [(0, 0), (1, 0), (0, -1), (0, -2)],   # orange
    'I': [(0, 0), (0, 1), (0, -1), (0, -2)],   # black
    'S': [(0, 0), (-1, 0), (0, -1), (1, -1)],  # purple
    'Z': [(0, 0), (1, 0), (0, -1), (-1, -1)]   # pink
}

TETROMINOES_COLOR = {
'T':'red',
'O':'orange',
'J':'blue',
'L':'green',
'I':'black',
'S':'purple',
'Z':'pink'
}