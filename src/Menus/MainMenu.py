from tkinter import Button, Label

from App import App
from Menus.Menu import Menu
from Menus.ChoiceMenu import ChoiceMenu
from Menus.PointerLocationMenu import PointerLocationMenu
from Menus.StopMenu import StopMenu

from StopThread import StopThread

from GameActions.chocolate import auto_chocolate

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
        self.app.root.geometry("100x25")
        self.chocolate_button.pack()
        self.frame.pack()

    def start_chocolate(self):
        self.pack_forget()

        choice_menu: ChoiceMenu = ChoiceMenu(self.app, "random", "slow", "fast")
        choice_menu.pack()
        choice_menu.frame.wait_window()

        pointer_menu: PointerLocationMenu = PointerLocationMenu(self.app, "banker")
        pointer_menu.pack()
        pointer_menu.frame.wait_window()

        chocolate_thread: StopThread = StopThread(target=auto_chocolate, args=[pointer_menu.loc, choice_menu.choice], daemon=True)
        stop_menu: StopMenu = StopMenu(self.app, chocolate_thread)
        stop_menu.pack()
        stop_menu.frame.wait_window()

        self.pack()