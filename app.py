import dearpygui.dearpygui as dpg

from ui.ui_manager import UIManager

dpg.create_context()

ui_manager = UIManager()

ui_manager.splash_screen(_oncreated=ui_manager)

dpg.create_viewport(title='Onomatopeia', width=1280, height=720)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()