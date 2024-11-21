from tkinter import Button 

from App import App
from Menus.Menu import Menu

class ChoiceMenu(Menu):
    """ Menu displaying multiple choices for user to choose from """
    def __init__(self, app: App, *args):
        super().__init__(app)
        self.app.root.geometry("200x30")

        for i, btn in enumerate(args):
            setattr(self, f"button{i}", Button(self.frame, text=btn, command=lambda btn=btn: self.set_choice(btn)))

        self.choice: str = ""
        
    def pack(self):
        count = 0
        while True:
            try:
                getattr(self, f"button{count}").pack(side="left", padx=5)
                count += 1
            except:
                break

        self.frame.pack()

    def set_choice(self, value: str) -> str:
        self.destroy()
        self.choice = value
