import time

class FuncInFuture:
    def __init__(self, futureTime, function):
        self.futureTime = futureTime
        self.function = function

    def update(self):
        if time.time() >= self.futureTime:
            self.function()

