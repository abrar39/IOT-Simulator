import threading
import time
import random
import csv
from utils.data_logger import DataLogger
from mqtt_client import MQTTClient

class IOTSimulator:
    """
    Threads allow a program to handle multiple tasks seemingly simultaneously by switching between them. This simulator
    simulates process conditions and logs the data into a csv
    if required.
    """
    def __init__(self, sensors, log_to_csv=True, print_data=False, output_file="output/data_log.csv", mqtt_config=None):
        self.sensors = sensors
        self.log_to_csv = log_to_csv
        self.print_data = print_data
        self.output_file = output_file
        self.logger = DataLogger(output_file) if log_to_csv else None
        self.mqtt_config = mqtt_config
        self.mqtt_client = None

        if mqtt_config and mqtt_config.get("enabled", False):
            # check if mqtt is enabled in config.json
            # then define a mqtt client
            self.mqtt_client = MQTTClient(
                broker=mqtt_config["broker"],
                port=mqtt_config["port"],
                topic_prefix=mqtt_config["topic_prefix"],
                keepalive=mqtt_config.get("keepalive", 60),
                username=mqtt_config["username"],
                password=mqtt_config["password"]
            )
            
            # connect to the client
            self.mqtt_client.connect()

        if log_to_csv:
            with open(self.output_file, "w", newline="") as f:
                writer = csv.DictWriter(
                    f,
                    fieldnames=[
                        "timestamp", 
                        "sensor_id", 
                        "sensor_type", 
                        "value", 
                        "unit"
                    ]
                )
                writer.writeheader()

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

            if self.mqtt_client:
                self.mqtt_client.publish(sensor.sensor_type, data)
            
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

