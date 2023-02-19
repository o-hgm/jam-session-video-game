import pygame

class PrincipalPjSprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('./jam_session/resources/characters/pj.png').convert_alpha()
        """ self.image.fill((0, 0, 0)) """
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.rect.x = x
        self.rect.y = y
        self.vel_x = 0
        self.vel_y = 0
    
    def move_right(self):
        self.rect.x += 5
    def move_left(self):
        self.rect.x -= 5
    def move_up(self):
        self.rect.y += 5
    def move_down(self):
        self.rect.x -= 5

    def update(self):
        pass
