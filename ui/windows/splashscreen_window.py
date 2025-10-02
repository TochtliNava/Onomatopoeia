import dearpygui.dearpygui as dpg


class SplashScreenWindow:
    
    def __init__(self, ui_manager=None):
        self.width, self.height, self.channels, self.data = dpg.load_image("resources/logo.png")

        with dpg.window(label="Welcome to Onomatopeia", 
                        width=250, 
                        height=320,
                        pos=[475,200],
                        no_resize=True,
                        no_move=True,
                        no_title_bar=True,
                        tag="main_window"):
            
            dpg.add_text("Onomatopeia")
            dpg.add_separator()

            with dpg.texture_registry(show=False):
                
                dpg.add_static_texture(width=200, height=200, default_value=self.data, tag="logo_tag")

            dpg.add_image(texture_tag="logo_tag")

            with dpg.group(horizontal=True, tag="main_window_buttons"):
                
                dpg.add_button(label="New", width=90, callback=ui_manager.new_project, parent="main_window_buttons")
                dpg.add_button(label="Load", width=90, callback=None, parent="main_window_buttons")

            dpg.add_text(default_value="Onomatopeia TochtliNava (2025)", color=(180, 180, 180))