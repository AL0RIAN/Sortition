import threading


class SharedVariable:
    def __init__(self, value):
        self.value = value
        self.lock = threading.Lock()


COUNT = SharedVariable(-1)