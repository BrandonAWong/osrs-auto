from tkinter import Frame
from App import App

class Menu:
    """ Base class for the application's views """
    def __init__(self, app: App):
        self.app = app
        self.frame: Frame = Frame(app.root)

    def pack(self):
        self.frame.pack()

    def pack_forget(self):
        self.frame.pack_forget()

    def destroy(self):
        self.frame.destroy()
