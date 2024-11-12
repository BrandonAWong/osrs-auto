from tkinter import Tk
from App import App
from MainMenu import MainMenu


def main():
    app: App = App()
    main_menu: MainMenu = MainMenu(app)  
    main_menu.pack()
    app.run()

if __name__ == "__main__":
    main()
