# A Video Games Jam Session

This repository contains the artifacts generated during our custom jam session on 04/02/2023.

## Goals

Given a basic description of a character and story background provided by a ChatGPT session, 
implement the stories, assets and code to provide a first prototype of a game.


## Requirements

> To be done

## Getting Started

### Game Architecture


```mermaid
---
title: Late Again
---
classDiagram
    Main <|-- GameEngine
    GameEngine <|-- UserInterfaceInteractive
    UserInterfaceInteractive <|-- SpritePlayer
    UserInterfaceInteractive <|-- Scene
    Main : GameEngine game_engine
    Main : UserInterfaceInteractive user_interface
    Main: Player player
    Main: Scene scene
    class GameEngine{
        
        Surface screen
        Boolean running
        UI user_interface
        init(GAME_WIDTH, GAME_HEIGHT, FPS)
        handleEvents()
        main_loop()
    }
    class UserInterfaceInteractive{
        Object actions
        String bg_color
        UIManager manager
        GameEngine game_engine
        init(bg_color, game_engine)
        build_user_interface()
        handle_text_input(event)
        enable_action_buttons(actions)
        update_dialog(text)
        draw()
    }

    class Scene{
        TiledMapObject map_data
        UserInterfaceInteractive user_interface
        Int grid_size
        Int drawable_surface_x
        Int drawable_surface_y
        String map_file
        init(grid_size, drawable_surface_x, drawable_surface_y, user_interface, map_file)
        is_walkable(x, y)
        is_colliding(x, y)
        visible_range(player_position)
        render(screen, player_position)
        handle_interaction(player, asset)
        clear_interaction(self, player)
    }
    class SpritePlayer{
        Dict sprite_map
        Array default_layout
        Dict render_offset
        String current_action
        Int current_frame
        Tuple position
        Int sprite_size
        sprites
        Image current_sprite
        init(position, sprite_sheet_path, sprite_size)
        load_sprites(sprite_sheet_path, sprite_size)
        update(scene, key_event)
        render(screen, scene)
    }
    class UserInterface{
        init(bg_color)
        draw(screen, scene, player)
    }
    class Player{
        Tuple position
        String color
        init(position, color)
        update(scene, key_event)
        render(screen, scene)
    }
```

#### How it works

##### Función Main (lanzamiento del juego)
La aplicación comienza la ejecución en la función `main()` donde se inicializan `game_engine`, `user_interface`, `player` y `scene` para luego asginar estos `user_interface`, `player` y `scene` al `main_loop`.

> `main_loop` es una propiedad que pertenece a `game_engine`, es el bucle de ejecución principal aka event loop

#### Game Engine
El game engine se inicializa pasando los parámetros `GAME_WIDTH`, `GAME_HEIGHT` y `FPS` a través del constructor, mientras que `screen` y `clock` se setean a la surface principal (`set_mode()`) y al reloj del juego directamente, las propiedades `running` y `user_interface` se setean a `false` y  `true`  respectivamente, `running` controla la salida del bucle para terminar la ejecución y `user_interface` se asignará más tarde a la correspondiente clase que maneje la interfaz.

Game Engine tiene disponibles 2 métodos `handle_events` y `main_loop`:
- `handle_events()` gestiona los eventos, por ahora no está abierto a ampliación.
- `main_loop(scene: "Scene", player: "SpritePlayer", user_interface: "UserInterfaceInteractive")` bucle de ejecución principal del juego, yendo a lo más básico este evento se debe encargar secuencialmente de recoger los eventos, actualizar los datos y renderizar el frame.
    ```python
    while self.running:
            self.clock.tick(self.fps)
            # Recoger eventos
            key_event = self.handle_events()

            # Actualizar datos
            scene.update(player, key_event)
            player.update(scene, key_event)

            # Renderizar frame
            user_interface.draw(self.screen, scene, player)
            pygame.display.flip()
    ```

##### UserInterfaceInteractive
Esta clase se encarga de:
- Establecer el color de fondo
- La creación, manejo de eventos de entrada y actualización de la interfaz usando `pygame_gui`
- Exponer el game engine para delegar el renderizado de `Player` y  `Scene` a esta clase, aunque sigue ejecutándose en `GameEngine` a través del método `draw()` de `UserInterfaceInteractive`.