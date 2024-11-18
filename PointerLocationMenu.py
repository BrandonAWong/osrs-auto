from tkinter import Label

from pyautogui import position
from pynput import keyboard

from App import App
from Menu import Menu

class PointerLocationMenu(Menu):
    """ Initial application menu, displays basic program information and start button """
    def __init__(self, app: App, location: str):
        super().__init__(app)
        self.label: Label = Label(text=f"Hover over {location.upper()} then press SPACE")
        
    def pack(self):
        self.app.root.geometry("250x25")
        self.label.pack()
        self.frame.pack()
    
    def get_position(self):
        def keypress_handler(key) -> bool | None:
            if key == keyboard.Key.space:
                return False

        listener: keyboard.Listener = keyboard.Listener(on_press=keypress_handler)
        listener.start()
        listener.join()

        self.pack_forget()
        x, y = position()
        return (x, y)
