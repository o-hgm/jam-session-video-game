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
        playercolliders = pg.sprite.groupcollide(self.game.playergroup, self.game.npcgroup,0,0)
        maskcolliders =  pg.sprite.spritecollide(self, self.game.npcgroup, False, pg.sprite.collide_rect_ratio(1.5))

        if not playercolliders:

            if keys[pg.K_LEFT] and self.rect.left > 0:
                    # self.direction = PLAYER_LEFT
                    self.direction = 'left'
                    self.position.x -= self.horizontal_speed * dt
            if keys[pg.K_RIGHT] and self.rect.right < WIDTH:
                # self.direction = PLAYER_RIGHT
                self.direction = 'right'
                self.position.x += self.horizontal_speed * dt
            if keys[pg.K_UP] and self.rect.top > 0 :
                # self.direction = PLAYER_BACK
                self.direction = 'up'
                self.position.y -= self.vertical_speed * dt
            if keys[pg.K_DOWN] and self.rect.bottom < HEIGHT:
                # self.direction = PLAYER_FRONT
                self.direction = 'down'
                self.position.y += self.vertical_speed * dt
        else :
            if self.direction == 'left':
            # if self.direction == PLAYER_LEFT:
                self.position.x += self.horizontal_speed * dt
            if self.direction == 'right':
            # if self.direction == PLAYER_RIGHT:
                self.position.x -= self.horizontal_speed * dt
            if self.direction == 'up':
            # if self.direction == PLAYER_BACK:
                self.position.y += self.horizontal_speed * dt
            if self.direction == 'down':
            # if self.direction == PLAYER_FRONT:
                self.position.y += self.horizontal_speed * dt

        if maskcolliders:
            self.game.ui.show_panel = True
        else:
            self.game.ui.show_panel = False

        self.rect.x = int(self.position.x)
        self.rect.y= int(self.position.y)

        # if not self.mask.overlap():
            # if keys[pg.K_LEFT] | keys[pg.K_RIGHT] | keys[pg.K_UP] | keys[pg.K_DOWN]:
            #     self.update_current_animation_frame()
            # self.game.ui.show_panel = False
            
        # else:
            # if self.direction == 'left':
            # # if self.direction == PLAYER_LEFT:
            #     self.position.x += self.horizontal_speed * dt
            # if self.direction == 'right':
            # # if self.direction == PLAYER_RIGHT:
            #     self.position.x -= self.horizontal_speed * dt
            # if self.direction == 'up':
            # # if self.direction == PLAYER_BACK:
            #     self.position.y += self.horizontal_speed * dt
            # if self.direction == 'down':
            # # if self.direction == PLAYER_FRONT:
            #     self.position.y += self.horizontal_speed * dt
            # npc = maskcolliders.items()

            # if npc:
                # self.game.ui.show_panel = True

        # self.image = self.spritemap[self.direction][self.animation]

    # def update_current_animation_frame(self):
    #     if self.animation < len(self.spritemap[self.direction] ) -1:
    #         self.animation +=1
    #     else:
    #         self.animation = 0

