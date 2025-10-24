import threading


class IOTSimulator:
    """
    Threads allow a program to handle multiple tasks seemingly simultaneously by switching between them
    """
    def __init__(self, sensors):
        self.sensors = sensors

    def start(self):
        threads = []
        for sensor in self.sensors:
            t = threading.Thread(target=sensor.stream_data)
            t.daemon = True #allows program to exit even if threads are running
            threads.append(t)
            t.start()

        # Keep main thread alive
        for t in threads:
            t.join()

