from threading import Thread

class StopThread(Thread):
    """ Thread with stop flag """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.stopped : bool = False

    def stop(self):
        self.stopped = True
