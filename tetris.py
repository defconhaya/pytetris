from settings import *
import math
from tetromino import Tetromino
import pygame.freetype as ft


class Text:
    def __init__(self, app) -> None:
        self.app = app
        self.font = ft.Font(FONTH_PATH)

    def draw(self):
        self.font.render_to(self.app.screen, (WIN_W * 0.595, WIN_H * 0.02), text= "Tetris", fgcolor = 'white', size = TILE_SIZE * 2.25, bgcolor =BG_COLOR)
        self.font.render_to(self.app.screen, (WIN_W * 0.65, WIN_H * 0.22), text= "Next", fgcolor = 'orange', size = TILE_SIZE * 1.4, bgcolor =BG_COLOR)
        self.font.render_to(self.app.screen, (WIN_W * 0.6, WIN_H * 0.67), text= "Score", fgcolor = 'orange', size = TILE_SIZE * 2.25, bgcolor =BG_COLOR)
        self.font.render_to(self.app.screen, (WIN_W * 0.64, WIN_H * 0.8), text= f"{self.app.tetris.score}", fgcolor = 'white', size = TILE_SIZE * 2.25, bgcolor =BG_COLOR)

class Tetris:

    def __init__(self, app) -> None:
        self.app = app
        self.sprite_group = pg.sprite.Group()
        self.field_array = self.get_field_array()
        self.tetromino = Tetromino(self)
        self.next_tetromino = Tetromino(self, current = False)
        self.speedup = False
        self.score = 0
        self.full_lines = 0
        self.points_per_lines = {0:0, 1: 100, 2:300, 3:700, 4:1500}

    def get_score(self):
        self.score += self.points_per_lines[self.full_lines]
        self.full_lines = 0

    def check_full_lines(self):
        row = FIELD_H -1
        for y in range(FIELD_H - 1, -1, -1):
            for x in range (FIELD_W):
                self.field_array[row][x] = self.field_array[y][x]

                if self.field_array[y][x]:
                    self.field_array[row][x].pos = vec(x, y)

            if sum(map(bool, self.field_array[y])) < FIELD_W:
                row -= 1
            else:
                for x in range(FIELD_W):
                    self.field_array[row][x].alive = False
                    self.field_array[row][x] = 0
                self.full_lines += 1

    def put_tetromino_block_in_array(self):
        for block in self.tetromino.blocks:
            x, y = int(block.pos.x), int(block.pos.y)
            self.field_array[y][x] = block

    def get_field_array(self):
        return [[0 for x in range(FIELD_W)] for y in range(FIELD_H)]

    def is_game_over(self):
        if self.tetromino.blocks[0].pos.y == INIT_POS_OFFSET[1]:
            pg.time.wait(300)
            return True

    def check_tetromino_landing(self ):
        if self.tetromino.landing:
            if self.is_game_over():
                self.__init__(self.app)
            else:
                self.speedup = False
                self.put_tetromino_block_in_array()
                self.next_tetromino.current = True
                self.tetromino = self.next_tetromino
                self.next_tetromino = Tetromino(self, current=False)

    def control(self, key_pressed):
        if key_pressed == pg.K_LEFT:
            self.tetromino.move(direction='left')
        elif key_pressed == pg.K_RIGHT:
            self.tetromino.move(direction='right')
        elif key_pressed == pg.K_UP:
            self.tetromino.rotate()
        elif key_pressed == pg.K_DOWN:
            self.speedup = True


    def draw_grid(self):
        for x in range(FIELD_W):
            for y in range (FIELD_H):
                pg.draw.rect(self.app.screen, 'black',
                (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

    def update(self):
        trigger = [self.app.anim_trigger, self.app.fast_anim_trigger][self.speedup]
        trigger = [self.app.anim_trigger, self.app.fast_anim_trigger][self.speedup]
        if trigger:
            self.check_full_lines()
            self.tetromino.update()
            self.check_tetromino_landing()
            self.get_score()
        self.sprite_group.update()


    def draw(self):
        self.draw_grid()
        self.sprite_group.draw(self.app.screen)

     