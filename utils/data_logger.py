import csv
import os

class DataLogger:
    """
    This utility class:
        Creates directories automatically (e.g. output/).
        Writes headers only once.
        Logs/ appends new sensor readings as they arrive.
    """

    def __init__(self, file_path):
        self.file_path = file_path
        self._initialize_file()

    def _initialize_file(self):
        """
        Create a CSV file with headers if it doesn't alread exist.
        """
        if not os.path.exists(os.path.dirname(self.file_path)):
            # create the directory if it does not exist
            os.makedirs(os.path.dirname(self.file_path))

        if not os.path.exists(self.file_path):
            # create the file
            with open(self.file_path, mode='w', newline='') as f:
                # Create the header row
                writer = csv.writer(f)
                writer.writerow([
                    "sensor_id", "sensor_type", "timestamp", "value", "unit"
                ])

    def log(self, data):
        """
        Log the data into the csv file
        """
        with open(self.file_path, mode="a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                data["sensor_id"], 
                data["sensor_type"], 
                data["timestamp"], 
                data["value"], 
                data["unit"]
            ])
