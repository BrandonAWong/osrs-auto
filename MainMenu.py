from tkinter import Button, Label

from App import App
from Menu import Menu
from StopMenu import StopMenu

from StopThread import StopThread

from chocolate import auto_chocolate

class MainMenu(Menu):
    """ Initial application menu, displays basic program information and start button """
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(MainMenu, cls).__new__(cls)
        return cls.instance

    def __init__(self, app: App):
        super().__init__(app)
        self.chocolate_button: Button = Button(self.frame, text="chocolate", command=self.start_chocolate)
        #self.time_label: Label = Label(self.frame, text=f"Time running: ")
        
    def pack(self):
        self.chocolate_button.pack()
        #self.time_label.pack() 
        self.frame.pack()

    def start_chocolate(self):
        self.pack_forget()
        chocolate_thread: StopThread = StopThread(target=auto_chocolate)
        stop_menu: StopMenu = StopMenu(self.app, chocolate_thread)
        stop_menu.pack()
        chocolate_thread.start()
