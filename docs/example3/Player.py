import pygame

class SpritePlayer:
    def __init__(self, position, sprite_sheet_path, sprite_size):
        self.sprite_map = {
            "direction_down": [],
            "direction_left": [],
            "direction_right": [],
            "direction_up": [],
        }
        self.default_layout = [
            "direction_down",
            "direction_left",
            "direction_right",
            "direction_up",
        ]
        self.render_offset = {
            "direction_down": (0, 1),
            "direction_left":  (1, 0),
            "direction_right": (-1, 0),
            "direction_up": (0, -1),
        }
        self.current_action = "direction_down"
        self.current_frame = 0
        self.position = position
        self.sprite_size = sprite_size
        self.sprites = self.load_sprites(sprite_sheet_path, sprite_size)
        self.current_sprite = self.sprite_map[self.current_action][self.current_frame]

    def load_sprites(self, sprite_sheet_path, sprite_size):
        sprite_sheet = pygame.image.load(sprite_sheet_path).convert_alpha()
        width, height = sprite_sheet.get_size()
        sprites = []

        for y in range(0, height, sprite_size):
            index = int(y / sprite_size)
            current_action = (
                self.default_layout[index] if index < len(self.default_layout) else None
            )
            if current_action is not None:
                for x in range(0, width, sprite_size):
                    sprite = pygame.Surface(
                        (sprite_size, sprite_size), pygame.SRCALPHA, 32
                    )
                    sprite.blit(sprite_sheet, (0, 0), (x, y, sprite_size, sprite_size))
                    self.sprite_map[current_action].append(sprite)


    def update(self, scene, key_event):
        if key_event:
            new_x, new_y = self.position

            if key_event == pygame.K_LEFT:
                new_x -= 1
                self.current_action = "direction_left"
                # Update the current sprite to face left
                # self.current_sprite = self.sprites[1]
            elif key_event == pygame.K_RIGHT:
                new_x += 1
                self.current_action = "direction_right"
                # Update the current sprite to face right
                # self.current_sprite = self.sprites[2]
            elif key_event == pygame.K_UP:
                new_y -= 1
                self.current_action = "direction_up"
                # Update the current sprite to face up
                # self.current_sprite = self.sprites[3]
            elif key_event == pygame.K_DOWN:
                new_y += 1
                self.current_action = "direction_down"
                # Update the current sprite to face down
                # self.current_sprite = self.sprites[0]

            total_frames_of_current_action = self.sprite_map[self.current_action] or 1
            self.current_frame = (self.current_frame + 1) % len(
                total_frames_of_current_action
            )
            self.current_sprite = self.sprite_map[self.current_action][
                self.current_frame
            ]

            is_walkable = scene.is_walkable(new_x, new_y)
            is_colliding, target_asset = scene.is_colliding(new_x, new_y)
            if is_walkable and not is_colliding:
                self.position = (new_x, new_y)

            if is_colliding:
                scene.handle_interaction(self, target_asset)
            else:
                scene.clear_interaction(self)

    def render(self, screen, scene):
        min_x, min_y = scene.visible_range(self.position)
        screen.blit(
            self.current_sprite,
            (
                (self.position[0] - min_x) * scene.grid_size, # + self.render_offset[self.current_action][0] * scene.grid_size * 1/2,
                (self.position[1] - min_y) * scene.grid_size # + self.render_offset[self.current_action][1] * scene.grid_size * 1/2,
            ),
        )


class Player:
    def __init__(self, position, color):
        self.position = position
        self.color = color

    def update(self, scene, key_event):
        if key_event:
            new_x, new_y = self.position

            if key_event == pygame.K_LEFT:
                new_x -= 1
            elif key_event == pygame.K_RIGHT:
                new_x += 1
            elif key_event == pygame.K_UP:
                new_y -= 1
            elif key_event == pygame.K_DOWN:
                new_y += 1

            if scene.is_walkable(new_x, new_y):
                self.position = (new_x, new_y)

    def render(self, screen, scene):
        min_x, min_y = scene.visible_range(self.position)
        pygame.draw.rect(
            screen,
            self.color,
            (
                (self.position[0] - min_x) * scene.grid_size,
                (self.position[1] - min_y) * scene.grid_size,
                scene.grid_size,
                scene.grid_size,
            ),
        )