from tkinter import Label

from pyautogui import position
from pynput import keyboard

from threading import Thread

from App import App
from Menu import Menu

class PointerLocationMenu(Menu):
    """ Initial application menu, displays basic program information and start button """
    def __init__(self, app: App, thread: Thread, landmark: str):
        super().__init__(app)
        self.thread = thread
        self.label: Label = Label(self.frame, text=f"Hover over {landmark.upper()} then press SPACE")
        
    def pack(self):
        self.app.root.geometry("250x25")
        self.label.pack()
        self.frame.pack()
    
    def get_position(self, loc):
        with keyboard.Events() as events:
            for event in events:
                if event.key == keyboard.Key.space:
                    loc[0], loc[1] = position()
                    self.destroy()
                    return
