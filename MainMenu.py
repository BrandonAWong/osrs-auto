from tkinter import Button, Label

from pyscreeze import Point

from App import App
from Menu import Menu
from PointerLocationMenu import PointerLocationMenu
from StopMenu import StopMenu

from StopThread import StopThread

from chocolate import auto_chocolate

class MainMenu(Menu):
    """ Initial application menu, displays basic program information and start button """
    def __new__(cls, *args):
        if not hasattr(cls, "instance"):
            cls.instance = super(MainMenu, cls).__new__(cls)
        return cls.instance

    def __init__(self, app: App):
        super().__init__(app)
        self.chocolate_button: Button = Button(self.frame, text="chocolate", command=self.start_chocolate)
        self.autorun_button: Button = Button(self.frame, text="autorun")
        
    def pack(self):
        self.app.root.geometry("400x300")
        self.chocolate_button.pack()
        self.frame.pack()

    def start_chocolate(self):
        self.pack_forget()

        pointer_menu: PointerLocationMenu = PointerLocationMenu(self.app, "banker")
        pointer_menu.pack()
        loc = pointer_menu.get_position()

        chocolate_thread: StopThread = StopThread(target=auto_chocolate, args=[loc])
        stop_menu: StopMenu = StopMenu(self.app, chocolate_thread)
        stop_menu.pack()

        chocolate_thread.start()

