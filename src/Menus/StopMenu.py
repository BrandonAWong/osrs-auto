from tkinter import Button, Label

from pynput import keyboard

from threading import Thread
from StopThread import StopThread

from App import App
from Menus.ThreadMenu import ThreadMenu

class StopMenu(ThreadMenu):
    """ Menu to stop current action thread """
    def __init__(self, app: App, thread: StopThread):
        super().__init__(app, thread)
        self.app.root.geometry("100x50")
        self.stop_button: Button = Button(self.frame, text="Stop", command=self.stop_thread)
        self.text: Label = Label(self.frame, text="Press 'p' to stop")

        # I'm not joining this thread anywhere, but it seems to work ok..
        self.keyboard_thread: Thread = Thread(target=self.keyboard_listener, daemon=True)
        
    def pack(self):
        self.stop_button.pack()
        self.text.pack()

        self.keyboard_thread.start()
        super().pack()

    def stop_thread(self):
        self.thread.stop()
        self.destroy()

    def keyboard_listener(self):
        with keyboard.Events() as events:
            for event in events:
                if event.key == keyboard.KeyCode.from_char("p"):
                    self.stop_thread()
                    break
