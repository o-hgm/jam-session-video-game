class Asset:
    pass

class AnimatedAsset(Asset):
    pass

"""
 asset_scene_start_game_title = pygame.image.load('./jam_session/resources/sprites/scene_start_game_title.png')
    asset_scene_start_game_new_game = pygame.image.load('./jam_session/resources/sprites/scene_start_game_new_game.png')

    asset_position_title_x = (WINDOW_WIDTH - asset_scene_start_game_title.get_width())/2
    asset_position_title_y = (WINDOW_WIDTH - asset_scene_start_game_title.get_height())/2

    game_surface.blit(asset_scene_start_game_title, (asset_position_title_x, asset_position_title_y))

    asset_offset_y = 100
    asset_position_x = (WINDOW_WIDTH - asset_scene_start_game_new_game.get_width())/2
    asset_position_y = asset_offset_y + (WINDOW_WIDTH - asset_scene_start_game_new_game.get_height())/2

    game_surface.blit(asset_scene_start_game_new_game, (asset_position_x, asset_position_y))

    game_surface.blit(asset_scene_start_game_title, (asset_position_x, asset_position_y))

    from jam_session.lib.entities import asset
    asset_example = asset.from_image_resource('./jam_session/resources/sprites/scene_start_game_title.png', y_origin=200)
    asset_groups = pygame.sprite.Group()
    
    asset_groups.add(asset_example)

    while True:
        keyboard_event_loop()
        game_surface.fill((0,0,0))
        
        asset_groups.update()
        asset_groups.draw(game_surface)

        game_clock.tick(4)
        pygame.display.update()


    while True:
         game_surface.fill(), rect=None, special_flags=0)
        game_clock.tick(60)
        keyboard_event_loop()
        pygame.display.update()
        asset_position_x, asset_position_y = pj_move(game_surface, asset_position_x, asset_position_y)
    from itertools import cycle

    asset_animation = [asset_scene_start_game_new_game, None]
    asset_animation_iterator = cycle(asset_animation)
"""
