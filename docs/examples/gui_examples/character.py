import pygame as pg
from settings import *

class Character(pg.sprite.Sprite):
    def __init__(self, image_path, x=0, y=0):
        super().__init__()

        # self.spritemap = []
        
        # self.spritemap = self.load_sprites(image_path,120)

        self.direction = PLAYER_FRONT
        self.animation = 0

        # self.image = self.spritemap[self.direction][self.direction]
        self.image = pg.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.position = pg.Vector2(x, y)
        self.horizontal_speed = PLAYER_SPEED
        self.vertical_speed = PLAYER_SPEED

    # def load_sprites(self, sprite_sheet_path, sprite_size):
    #     sprite_sheet = pg.image.load(sprite_sheet_path).convert_alpha()
    #     width, height = sprite_sheet.get_size()

    #     spritesheet = []

    #     for y in range(0, height, sprite_size):
    #         current_row = []
    #         for x in range(0, width, sprite_size):
    #             sprite = pg.Surface(
    #                     (sprite_size, sprite_size), pg.SRCALPHA, 32
    #                 )
    #             sprite.blit(sprite_sheet, (0, 0), (x, y, sprite_size, sprite_size))
    #             current_row.append(sprite)

    #         spritesheet.append(current_row)

    #     return spritesheet
    
    def events(self, events):
        raise NotImplementedError("events must be defined")

    def update(self, dt):
        raise NotImplementedError("update must be defined")

    def draw(self, display):
        raise NotImplementedError("draw must be defined")