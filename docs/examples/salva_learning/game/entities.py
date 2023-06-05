import pygame as pg


class Player(pg.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()

        self.boy_down = [pg.image.load(
            f"res/images/boy/down_{i}.png").convert_alpha() for i in range(1, 5)]
        self.boy_up = [pg.image.load(
            f"res/images/boy/up_{i}.png").convert_alpha() for i in range(1, 5)]
        self.boy_left = [pg.image.load(
            f"res/images/boy/left_{i}.png").convert_alpha() for i in range(1, 5)]
        self.boy_right = [pg.image.load(
            f"res/images/boy/right_{i}.png").convert_alpha() for i in range(1, 5)]

        self.animation = self.boy_down
        self.animation_sprite = 0
        self.animation_speed = 6

        self.image = self.animation[self.animation_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.position = pg.Vector2(x, y)
        self.horizontal_speed = 175
        self.vertical_speed = 100

    def update(self, dt):
        keys = pg.key.get_pressed()

        prev_position = self.position.copy()

        if keys[pg.K_LEFT]:
            self.animation = self.boy_left
            self.position.x -= self.horizontal_speed * dt
        elif keys[pg.K_RIGHT]:
            self.animation = self.boy_right
            self.position.x += self.horizontal_speed * dt
        if keys[pg.K_UP]:
            self.animation = self.boy_up
            self.position.y -= self.vertical_speed * dt
        elif keys[pg.K_DOWN]:
            self.animation = self.boy_down
            self.position.y += self.vertical_speed * dt

        if self.position == prev_position:
            self.animation_sprite = 0
        else:
            self.animation_sprite += self.animation_speed * dt
            if self.animation_sprite >= len(self.animation):
                self.animation_sprite = 0

        self.image = self.animation[int(self.animation_sprite)]

        self.rect = int(self.position.x), int(self.position.y)