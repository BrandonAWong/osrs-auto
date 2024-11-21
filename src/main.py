from platform import system
from tkinter import Tk
from subprocess import run

from App import App
from Menus.MainMenu import MainMenu


def main():
    if system() == "Linux":
        run(["sudo modprobe -i uinput"], shell=True)
    app: App = App()
    MainMenu(app).pack()
    app.run()

if __name__ == "__main__":
    main()
