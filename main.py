from sensors.temperature_sensor import TemperatureSensor
from sensors.vibration_sensor import VibrationSensor
from simulator import IOTSimulator

if __name__ == "__main__":
    # Instantiate the sensors
    temp_sensor_1 = TemperatureSensor("T-001")
    vib_sensor_1 = VibrationSensor("V-001")

    # Simulate the data
    simulator = IOTSimulator([
        temp_sensor_1, 
        vib_sensor_1
    ])

    simulator.start()