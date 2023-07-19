import pygame_gui as pg_gui
import pygame as pg
from pygame_gui.elements import UITextEntryLine, UITextBox
from pygame_gui.core import ObjectID


class UIManager:
    def __init__(self, display):
        self.display = display
        self.manager = pg_gui.UIManager(
            (self.display.get_width(), self.display.get_height())
        )

    def update(self, dt):
        self.manager.update(dt)
        self.manager.draw_ui(self.display)

class UiPanel:
    def __init__(self, display, ui):
        self.height = int(display.get_height() * 1 / 3)
        self.width = display.get_width()
        self.ui_panel = pg_gui.elements.UIPanel(
            relative_rect=pg.Rect(
                (0, int(display.get_height() * 2 / 3)),
                (
                    self.width,
                    self.height,
                ),
            ),
            #starting_layer_height=1,
            manager=ui,
            )
        self.ui_panel.hide()
        self.show_panel = False

    def update(self):
        if self.show_panel:
            self.ui_panel.show()
        else:
            self.ui_panel.hide()

class NarratorPanel(UiPanel):
    def __init__(self, display, ui) -> None:
        super().__init__(display, ui)
        self.create_text_box(ui)

    def create_text_box(self, ui):
        htm_text_block = UITextBox('<b><i>LATE AGAIN: THE GAME</b></i>'
                                    '<br><br>'
                                    '1. Nos encontramos en Late Again, un video-juego que simula el funcionamiento de una empresa de consultoría. '
                                    '<br>'
                                    '2. En dicha simulación, GPT-4 toma el papel de un NPC (Non Playable Character). '
                                    '<br>'
                                    '3. Dicho NPC interactuará con el entorno (Player, Objetos, otros NPC) y actuará '
                                    'en base a las caracteristicas definidas en las secciones correspondientes.'
                                    '<br>'
                                    '4. La acciones realizables en la simulación se limitan a:'
                                    '<br>'
                                        '4.1 talk_to_player: Hablar con el jugador'
                                        '<br>'
                                        '4.2 talk_to_npc: Hablar con otro NPC'
                                        '<br>'
                                        '4.3 go_to_place: Ir a una localización'
                                        '<br>'
                                        '4.4 interact_with_asset: Interactuar con un objeto de la simulación'
                                        '<br>'
                                        '4.5 do_work: Avanzar en las tareas asignadas'
                                        '<br>'
                                        '4.6 do_idle: No hacer nada'
                                        '<br>'
                                        '4.7 do_wander: Deambular por el espacio de la simulación'
                                        '<br>'
                                    '5. Todas las acciones deben incluir:'
                                    '<br>'
                                        '5.1 target_id: Identificador único del objetivo de la acción'
                                        '<br>'
                                        '5.2 dialog_msg: Mensajes de dialogo asociados a la acción'
                                        '<br>'
                                        '5.3 action_args: Argumentos de interes para la ejecución de la acción.'
                                        '<br>'
                                    '6. El NPC dispone de las siguientes stats:'
                                    '<br>'
                                        '6.1 Energia - Indica la capacidad de realizar acciones por parte del NPC'
                                        '<br>'
                                        '6.2 Motivación - Indica la propensión a realizar tareas útiles (do_work) o perder el tiempo'
                                        '<br>'
                                    '7. El comportamiento del NPC se define en la sección [Background Story]'
                                    '<br>'
                                    '8. La interacción con el NPC se realiza mediante las siguientes etiquetas:'
                                    '<br>'
                                        '8.1 [Sistema] Permite la adaptación del funcionamiento de la simulación o el NPC'
                                        '<br>'
                                        '8.2 [Narrador] Actua como voz en off que permite avanzar en la historia'
                                        '<br>'
                                        '8.3 [Jugador] Es el jugador humano'
                                        '<br>'
                                        '8.4 [<Nombre de NPC>] Indica el resto de jugadores no humanos'
                                        '<br>'
                                    '9. En cada interacción, el NPC produce una respuesta en formato YAML con la siguiente estructura:'
                                    ,
                                    pg.Rect((20, 20), (int(self.width) - 40, int(self.height) - 40)),
                                    manager=ui,
                                    container=self.ui_panel,
                                    object_id=ObjectID(class_id="@white_text_box",
                                                        object_id="#narrator_box"))
        htm_text_block.set_active_effect(pg_gui.TEXT_EFFECT_TYPING_APPEAR, params={'time_per_letter': 0.01})

class PlayerPanel(UiPanel):
    def __init__(self, display, ui):
        super().__init__(display, ui)
        self.create_text_box(ui)
        self.test_text_entry = UITextEntryLine(
            relative_rect=pg.Rect((20, self.height - 60), (int(self.width) - 40, 40)),
            initial_text="",
            container=self.ui_panel,
            manager=ui,
            object_id='#player_text_entry'
        )
        self.test_text_entry.set_forbidden_characters('numbers')

    def create_text_box(self, ui):
        htm_text_block = UITextBox('<b><i>LATE AGAIN: THE GAME</b></i>'
                                    '<br><br>'
                                    'This time is the player panel, supposed to have at minimum a text box and text input'
                                    '<br><br>'
                                    'Some stat bars would be ideal'
                                    '<br><br>'
                                    'Or maybe for another panel, who knows...'
                                    ,
                                    pg.Rect((20, 20), (int(self.width) - 40, int(self.height) - 80)),
                                    manager=ui,
                                    container=self.ui_panel,
                                    object_id=ObjectID(class_id="@white_text_box",
                                                        object_id="#player_box"))
        htm_text_block.set_active_effect(pg_gui.TEXT_EFFECT_TYPING_APPEAR, params={'time_per_letter': 0.01})

    def update(self):
        super().update()

        text_input = self.test_text_entry.get_text()
        if (text_input != ""):
            print(self.test_text_entry.get_text())
