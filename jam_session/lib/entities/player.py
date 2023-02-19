import pygame

class Player(pygame.sprite.Sprite):
    MOVE_SPEED = 5
    
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
        self.velocity_x = 0
        self.velocity_y = 0

    def update(self):
        # Actualizar la posición del personaje en función de su velocidad
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

        # Cambiar al siguiente frame del personaje
        self.current_frame = (self.current_frame + 1) % len(self.frames)

    def move_left(self):
        # Mover el personaje a la izquierda
        self.velocity_x = -self.MOVE_SPEED

    def move_right(self):
        # Mover el personaje a la derecha
        self.velocity_x = self.MOVE_SPEED

    def stop_moving(self):
        # Detener el movimiento horizontal del personaje
        self.velocity_x = 0

    def draw(self, surface):
        surface.blit(self.image, self.rect)