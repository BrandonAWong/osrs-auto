from tkinter import Label

from pyautogui import position
from pynput import keyboard

from threading import Thread

from App import App
from Menus.ThreadMenu import ThreadMenu

class PointerLocationMenu(ThreadMenu):
    """ Menu for getting current cursor position """
    def __init__(self, app: App, landmark: str):
        thread: Thread = Thread(target=self.get_position, daemon=True)

        super().__init__(app, thread)
        self.label: Label = Label(self.frame, text=f"Hover over {landmark.upper()} then press SPACE")
        self.loc = [0, 0]
        
    def pack(self):
        self.app.root.geometry("250x25")
        self.label.pack()
        super().pack()
    
    def get_position(self):
        with keyboard.Events() as events:
            for event in events:
                if event.key == keyboard.Key.space:
                    self.loc[0], self.loc[1] = position()
                    self.app.root.after(0, self.destroy)
                    break
