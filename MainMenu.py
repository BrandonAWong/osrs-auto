from tkinter import Button, Label
from App import App
from Menu import Menu

class MainMenu(Menu):
    """ Initial application menu, displays basic program information and start button """
    def __init__(self, app: App):
        super().__init__(app)
        self.start_button: Button = Button(self.frame, text="chocolate", command=self.start_chocolate)
        self.time_label: Label = Label(self.frame, text=f"Time running: ")

    def pack(self):
        self.frame.pack()
        self.start_button.pack()
        self.time_label.pack()

    def start_chocolate(self):
        pass
