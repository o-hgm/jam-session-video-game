import pygame
import pygame_gui

pygame.init()

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((800,600))
#ui_window = pygame_gui.elements.ui_window.UIWindow(rect=pygame.Rect((0,400),(800,200)),
#                                                   manager= manager,
#                                                   window_display_title='Hahá Its a window!',
#                                                   visible= True)
ui_panel = pygame_gui.elements.ui_panel.UIPanel(relative_rect=pygame.Rect((0,400),(800,200)),
                                                   manager= manager)

hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100,10), (100, 50)),
                                             text='Say Hello',
                                             manager=manager,
                                             container= ui_panel
                                            )

hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100,60), (100, 50)),
                                             text='Say Hello',
                                             manager=manager,
                                             container= ui_panel
                                            )

hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100,110), (100, 50)),
                                             text='Say Hello',
                                             manager=manager,
                                             container= ui_panel
                                            )

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == hello_button:
                print('Hello World!')

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()