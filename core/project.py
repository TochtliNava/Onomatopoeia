import dearpygui.dearpygui as dpg
from core.character import Character
from core.page import Page


class Project:

    def __init__(self, title:str, author:str):
        self.title = title
        self.author = author
        self.pages = []
        self.characters = {}

    def add_page(self):
        self.pages.append(Page())
        
    def get_characters(self):
        return list(self.characters.values())
    
    def get_character_by_name(self, name):
        return self.characters[name]

    def add_character(self, name: str = "dummy"):
        # TODO Implementar la logica de añadir {character.name+1, character}
        self.characters[name] = Character(name)
    
    def delete_character(self, character: Character):
        del self.characters[character]
        
    def remove_page(self, page_number):
        del self.pages[page_number]

    def move_page(self, from_index, to_index):
        (self.pages[to_index], self.pages[from_index]) = (self.pages[from_index], self.pages[to_index])
        
    def __str__(self):
        return f"{self.title} - {self.author}"