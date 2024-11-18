from tkinter import Button 

from StopThread import StopThread

from App import App
from Menu import Menu

class StopMenu(Menu):
    """ Initial application menu, displays basic program information and start button """
    def __init__(self, app: App, thread: StopThread):
        super().__init__(app)
        self.app.root.geometry("100x50")
        self.stop_button: Button = Button(self.frame, text="Stop", command=self.stop_thread)
        self.thread = thread
        
    def pack(self):
        self.stop_button.pack()
        self.frame.pack()

    def stop_thread(self):
        self.destroy()
        self.thread.stop()
        # show mainmenu
