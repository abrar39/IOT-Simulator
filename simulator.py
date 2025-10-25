import threading
import time
import random
from utils.data_logger import DataLogger

class IOTSimulator:
    """
    Threads allow a program to handle multiple tasks seemingly simultaneously by switching between them. This simulator
    simulates process conditions and logs the data into a csv
    if required.
    """
    def __init__(self, sensors, log_to_csv=True, print_data=False, output_file="output/data_log.csv"):
        self.sensors = sensors
        self.log_to_csv = log_to_csv
        self.print_data = print_data
        self.logger = DataLogger(output_file) if log_to_csv else None

    def _stream_with_logging(self, sensor):
        """
        Stream sensor data and optionally log to CSV
        """
        while True:
            data = sensor.generate_data()
            if self.print_data:
                print(data) # for live view, comment if not required
            if self.logger:
                self.logger.log(data=data)
            
            # Log with interval and a jitter to simulate real life data
            time.sleep(sensor.interval + random.uniform(-0.1, 0.1))

    def start(self):
        threads = []
        for sensor in self.sensors:
            t = threading.Thread(
                target=self._stream_with_logging, 
                args=(sensor, )
            )
            t.daemon = True #allows program to exit even if threads are running
            threads.append(t)
            t.start()

        # Keep main thread alive
        for t in threads:
            t.join()

