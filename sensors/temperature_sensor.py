from sensors.base_sensor import BaseSensor

class TemperatureSensor(BaseSensor):
    def __init__(self, sensor_id):
        super().__init__(
            sensor_id=sensor_id, 
            sensor_type="temperature", #the type of sensor
            min_value=18.0,
            max_value=35.0, 
            unit="°C",
            interval=1
        )