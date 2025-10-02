import dearpygui.dearpygui as dpg
from core.project import Project
from ui.windows.editor_window import EditorWindow
from ui.windows.new_project_window import NewProjectWindow
from ui.windows.splashscreen_window import SplashScreenWindow


class UIManager:

    def __init__(self):
        self.current_project = None
    
    def splash_screen(self, _oncreated=None):
        SplashScreenWindow(_oncreated)
    
    def set_project(self, project: Project):
        self.current_project = project
        dpg.set_primary_window(EditorWindow(self.current_project).editor_window, True)
        dpg.delete_item("main_window")

    def new_project(self):
        NewProjectWindow(_oncreated=self.set_project)
        