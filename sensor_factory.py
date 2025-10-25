from sensors.base_sensor import BaseSensor

def create_sensors_from_config(config):
    sensors = []
    for s in config["sensors"]:
        sensor = BaseSensor(
            sensor_id=s["id"], 
            sensor_type=s["type"], 
            min_value=s["min_value"], 
            max_value=s["max_value"],
            unit=s["unit"],
            interval=s.get("interval", 1)
        )

        sensors.append(sensor)

    return sensors