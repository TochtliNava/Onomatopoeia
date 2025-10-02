import dearpygui.dearpygui as dpg

from core.character import Character


class CharacterWidget:
    
    def __init__(self, character: Character):
        
        with dpg.window(label=character.name):
            dpg.add_text(f"Test Character {character.name} window")