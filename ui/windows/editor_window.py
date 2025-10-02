import dearpygui.dearpygui as dpg

from core.project import Project
from ui.windows.character_window import CharacterWindow

class EditorWindow:
    
    def __init__(self, project: Project=None):
        
        self.project = project
        
        with dpg.window(label=self.project.title, no_title_bar=True, width=300, height=600) as self.editor_window:
            
            with dpg.menu_bar():
            
                with dpg.menu(label="Project"):
                
                    dpg.add_menu_item(label="New")
                    dpg.add_menu_item(label="Save")
                    dpg.add_menu_item(label="Load")
                    dpg.add_separator()
                    dpg.add_menu_item(label="Close", callback=self._warning_on_close)
                
                with dpg.menu(label="Windows"):
                
                    dpg.add_menu_item(label="Characters", callback=lambda: CharacterWindow(self.project))
            
            # Pages widget
            CharacterWindow(self.project)
            
            dpg.add_button(label="+", width=20, callback=project.add_page)
    
    def _warning_on_close(self):
        with dpg.window(label="Warning", 
                        width=500, 
                        height=100,
                        pos=[350, 310],
                        no_move=True,
                        modal=True, 
                        no_resize=True, 
                        tag="warning_on_exit",
                        on_close=lambda: dpg.delete_item("warning_on_exit")):
            
            dpg.add_text("Changes Are not saved.")
            dpg.add_text("Are you sure do you want to close the program?")
            
            with dpg.group(horizontal=True):
            
                dpg.add_button(label="Yes", callback=dpg.destroy_context)
                dpg.add_button(label="No", callback=lambda: dpg.delete_item("warning_on_exit"))