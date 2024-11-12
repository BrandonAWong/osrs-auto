from tkinter import Frame
from App import App

class Menu:
    """ Base class for the application's views """
    def __init__(self, app: App):
        self.frame: Frame = Frame(app.root)

    def pack(self):
        self.frame.pack()

    def destroy(self):
        self.frame.destroy()
