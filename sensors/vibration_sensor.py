from sensors.base_sensor import BaseSensor

class VibrationSensor(BaseSensor):
    def __init__(self, sensor_id):
        super().__init__(
            sensor_id=sensor_id, 
            sensor_type="vibration", #the type of sensor
            min_value=0.1,
            max_value=10.0, 
            unit="mm/s (RMS)",
            interval=1
        )