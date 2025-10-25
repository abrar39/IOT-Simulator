from config_loader import load_config
from sensor_factory import create_sensors_from_config
from simulator import IOTSimulator

if __name__ == "__main__":

    # Dynamically create sensors
    # Load the configuration file
    config = load_config("config.json")

    # create sensors from configuration file
    sensors = create_sensors_from_config(config=config)

    simulator = IOTSimulator(
        sensors=sensors, 
        log_to_csv=config["output"]["log_to_csv"],
        print_data=config["output"]["print_data"],
        output_file=config["output"]["file_path"]
    )
    simulator.start()