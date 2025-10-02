import dearpygui.dearpygui as dpg

from core.project import Project
from ui.widgets.character_widget import CharacterWidget


class CharacterWindow:
    
    def __init__(self, project: Project):
        
        # TODO: No deberiamos estar a nivel de Project()?? entonces para que
        # putas traemos explicitamente a nivel de Character..? mierda, honestamente
        # no se de arquitectura.
        
        # Si eso es asi entonces estoy jodido ya que necesito traer a nivel de
        # Project() en TODO lo que se este rompiendo el encapsulamiento a nivel de proyecto.
        
        # BUG: No se porque no deja añadir mas characters, creo que mi duda es que es el nombre
        # que estoy usando como key y por eso no pueden repetirse.
        # TODO: implementar la logica de dummy, dummy1 ... y si se renombra a dummy el dummy1 
        # que este no lo permita.
        
        self.project = project 
        
        with dpg.window(label="Characters", 
                        tag="character_window",
                        width=200,
                        height=300, 
                        on_close=dpg.delete_item("character_window")):
            
            self.charaters = dpg.add_listbox(items=self.project.get_characters(), 
                                             callback=self._on_select_character,
                                             tag="characters_listbox")
            
            with dpg.popup(dpg.last_item()):
                
                dpg.add_button(label="Edit")
                dpg.add_button(label="Delete", callback=self._delete_character, user_data=dpg.last_item())
                dpg.add_button(label="Copy")
            
            dpg.add_button(label="+", callback=self._create_new_character)
    
    
    
    def _on_select_character(self, sender):
        character = dpg.get_value(sender)
        CharacterWidget(self.project.get_character_by_name(character))
        # with dpg.popup():
        #     dpg.add_button(label="Edit")
        #     dpg.add_button(label="Delete", callback=self._delete_character, user_data=context)
        #     dpg.add_button(label="Copy")
        
    def _create_new_character(self):
        self.project.add_character()
        self._refresh_characters_table()
    
    def _delete_character(self, sender, user_data):
        print(dpg.get_value(sender))
        pass
        # self.project.delete_character()
        # self._refresh_characters_table()
    
    def _refresh_characters_table(self):
        dpg.configure_item(self.charaters, items=self.project.get_characters())