from platform import system
from tkinter import Tk
from subprocess import run

from App import App
from MainMenu import MainMenu


def main():
    if system() == "Linux":
        run(["sudo modprobe -i uinput"], shell=True)
    app: App = App()
    main_menu: MainMenu = MainMenu(app)  
    main_menu.pack()
    app.run()

if __name__ == "__main__":
    main()
