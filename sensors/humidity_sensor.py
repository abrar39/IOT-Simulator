from sensors.base_sensor import BaseSensor

class HumiditySensor(BaseSensor):
    def __init__(self, sensor_id):
        super().__init__(
            sensor_id=sensor_id, 
            sensor_type="humidity", #the type of sensor
            min_value=10.0,
            max_value=90.0, 
            unit="%",
            interval=30
        )