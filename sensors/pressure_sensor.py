from sensors.base_sensor import BaseSensor

class PressureSensor(BaseSensor):
    def __init__(self, sensor_id):
        super().__init__(
            sensor_id=sensor_id, 
            sensor_type="pressure", #the type of sensor
            min_value=0,
            max_value=200, 
            unit="bar",
            interval=1
        )