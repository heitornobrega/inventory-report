from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, stop, data):
        self.stop = stop
        self.init = 0
        self.data = data

    def __next__(self):
        if self.init >= self.stop:
            raise StopIteration
        else:
            self.init += 1
            return self.data[self.init - 1]
