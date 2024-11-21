from tkinter import Tk

class App:
    """ Host for root and initialization of main menu """
    def __init__(self):
        self.root: Tk = Tk()
        self.root.title("OSRS autorun")
        self.root.geometry("400x300")

    def run(self):
        self.root.mainloop()
