import dearpygui.dearpygui as dpg

from core.project import Project

class NewProjectWindow:
    
    # This creates a modal where the project's details are provided
    
    def __init__(self, _oncreated=None):
        
        self.on_created = _oncreated
        self.new_project_window_id = dpg.generate_uuid()

        with dpg.window(
            label="Create a new project",
            width=300,
            height=120,
            pos=[450, 300],
            tag=self.new_project_window_id,
            modal=True,
            no_title_bar=True,
            no_move=True,
            on_close=self._on_close_window
        ):
            
            dpg.add_text("Create project")
            dpg.add_separator()
            
            # Title  [               ]
            
            with dpg.group(horizontal=True, tag=f"title_parent_{self.new_project_window_id}"):
                
                dpg.add_text("Title", parent=f"title_parent_{self.new_project_window_id}")
                dpg.add_input_text(parent=f"title_parent_{self.new_project_window_id}", tag=f"title_data_{self.new_project_window_id}")
            
            # Author [               ]
            
            with dpg.group(horizontal=True, horizontal_spacing=1, tag=f"author_parent_{self.new_project_window_id}"):
                
                dpg.add_text("Author", parent=f"author_parent_{self.new_project_window_id}")
                dpg.add_input_text(parent=f"author_parent_{self.new_project_window_id}", tag=f"author_data_{self.new_project_window_id}")
            
            # [Create][Cancel]
            
            with dpg.group(horizontal=True, horizontal_spacing=3, tag=f"button_parent_{self.new_project_window_id}"):
                
                dpg.add_button(label="Create",
                               width=75,
                               callback=self._on_create_project,
                               parent=f"button_parent_{self.new_project_window_id}")
                dpg.add_button(label="Cancel", width=75, callback=self._on_close_window, parent=f"button_parent_{self.new_project_window_id}")
    
    
    def _on_create_project(self):
        title = dpg.get_value(f"title_data_{self.new_project_window_id}")
        author = dpg.get_value(f"author_data_{self.new_project_window_id}")
        project = Project(title=title, author=author)
        
        if self.on_created:
            self.on_created(project)
        
        self._on_close_window()
    
    
    def _on_close_window(self):
        dpg.delete_item(self.new_project_window_id)
