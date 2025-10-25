import random
import datetime

class BaseSensor:
    # The base class for sensors
    def __init__(self, sensor_id, sensor_type, min_value, max_value, unit, interval=1):
        self.sensor_id = sensor_id
        self.sensor_type = sensor_type
        self.min_value = min_value
        self.max_value = max_value
        self.unit = unit
        self.interval = interval # Seconds between generated values

    def generate_data(self):
        """
        Generate a reading with timestamp.
        """
        
        # Generate a random float value
        value = round(random.uniform(self.min_value, self.max_value), 2)

        data = {
            "sensor_id": self.sensor_id, 
            "sensor_type": self.sensor_type, 
            "timestamp": datetime.datetime.now(datetime.timezone.utc), 
            "value": value,
            "unit": self.unit
        }

        return data
    