import pygame as pg
from settings import *
from character import Character

class Player(Character):
    def __init__(self, image_path, game):
        super().__init__(image_path)
        self.game = game
        self.mask = pg.mask.from_surface(self.image)
    
    def update(self, dt):
        keys = pg.key.get_pressed()
        # playercolliders = pg.sprite.groupcollide(self.game.playergroup, self.game.npcgroup,0,0)
        # maskcolliders =  pg.sprite.spritecollide(self, self.game.npcgroup, False, pg.sprite.collide_rect_ratio(1.5))

        # if not playercolliders:

        if keys[pg.K_LEFT] and self.rect.left > 0:
                self.direction = 'left'
                self.position.x -= self.horizontal_speed * dt
        if keys[pg.K_RIGHT] and self.rect.right < WIDTH:
            self.direction = 'right'
            self.position.x += self.horizontal_speed * dt
        if keys[pg.K_UP] and self.rect.top > 0 :
            self.direction = 'up'
            self.position.y -= self.vertical_speed * dt
        if keys[pg.K_DOWN] and self.rect.bottom < HEIGHT:
            self.direction = 'down'
            self.position.y += self.vertical_speed * dt
        # else :
        # if self.direction == 'left':
        #     self.position.x += self.horizontal_speed * dt
        # if self.direction == 'right':
        #     self.position.x -= self.horizontal_speed * dt
        # if self.direction == 'up':
        #     self.position.y += self.horizontal_speed * dt
        # if self.direction == 'down':
        #     self.position.y += self.horizontal_speed * dt

        # if maskcolliders:
        #     self.game.ui.show_panel = True
        # else:
        #     self.game.ui.show_panel = False

        self.rect.x = int(self.position.x)
        self.rect.y= int(self.position.y)


