from threading import Thread
from StopThread import StopThread

from App import App
from Menus.Menu import Menu

class ThreadMenu(Menu):
    """ Base class for the application's views that require a separate thread """
    def __init__(self, app: App, thread: Thread | StopThread):
        super().__init__(app)
        self.thread = thread

    def pack(self):
        super().pack()
        self.thread.start()

    def destroy(self):
        super().destroy()
        self.thread.join()