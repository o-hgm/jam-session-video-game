import pygame
import math

class Player(pygame.sprite.Sprite):
    MOVE_SPEED = 5

    MOVE_UP = (0,-1)
    MOVE_DOWN = (0,1)
    MOVE_LEFT = (-1, 0)
    MOVE_RIGHT = (1, 0)

    STATUS_MOVE_IDLE = 0
    STATUS_MOVE_ACTIVE = 1

    def set_move_direction(self, direction):
        self.move_direction = direction
        self.current_frame = self.move_status

    def set_move_status(self, status):
        self.move_status =  status
        if self.move_status:
            self.current_frame = self.STATUS_MOVE_IDLE
    
    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT):
        super().__init__()

        self.image = pygame.image.load("./jam_session/resources/characters/adventurer_sprite_sheet_v1.1.png").convert_alpha()


        # Cargar los frames del personaje desde el sprite sheet
        self.frames = []
        self.frames.append(self.image.subsurface((0, 0, 32, 32)))
        self.frames.append(self.image.subsurface((32, 0, 32, 32)))
        self.frames.append(self.image.subsurface((64, 0, 32, 32)))
        # Continuar cargando más frames según corresponda

        self.current_frame = 0

        # Definir la posición y velocidad inicial del personaje
        self.rect = self.frames[self.current_frame].get_rect()
        self.rect.x = WINDOW_WIDTH / 2
        self.rect.y = WINDOW_HEIGHT / 2
        self.velocity = 5
        self.move_direction = Player.MOVE_UP
        self.move_status = Player.STATUS_MOVE_IDLE

    def update(self):
        # Actualizar la posición del personaje en función de su velocidad
        if self.move_status == Player.STATUS_MOVE_ACTIVE:
            self.rect.x += self.move_direction[0] * self.velocity
            self.rect.y += self.move_direction[1] * self.velocity
            # Cambiar al siguiente frame del personaje
            self.current_frame = (self.current_frame + 1) % len(self.frames)
        else:
            self.current_frame = Player.STATUS_MOVE_IDLE
        

    def move(self, direction):
        angle = math.radians(direction)
        self.velocity_x = self.velocity * math.cos(angle)

    def stop_moving(self):
        # Detener el movimiento horizontal del personaje
        self.velocity_x = 0

    def draw(self, surface):
        surface.blit(self.image, self.rect)