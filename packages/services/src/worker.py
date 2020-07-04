import time

class Worker:
    id = None
    time = 10

    def __init__(self, id, time):
        self.id = id
        self.time = time

    def _fire_progress(self, progress):
        print('{}% completed'.format(progress))

    def work(self):
        threshold = self.time/100
        i = 0
        while i<100:
            time.sleep(threshold)
            self._fire_progress(i)
            i += 1
        self._fire_progress(i)
        return 'Work: {} finished in {} seconds'.format(self.id, self.time)
