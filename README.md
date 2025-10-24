# 🛰️ IoT Data Simulator

A Python-based **IoT Data Simulator** designed to generate continuous, realistic, and customizable sensor data streams.
This tool helps developers, data engineers, and dashboard designers simulate real-time IoT environments without needing physical hardware.

---

## 🌟 Features

* 🔄 **Continuous Data Streaming** — Simulates live sensor data in real time.
* ⚙️ **Multiple Sensors Support** — Run multiple virtual sensors simultaneously.
* 🎛️ **Configurable Parameters** — Control sensor ranges, units, and stream intervals.
* 🧠 **Extensible Design** — Easily add custom sensor types.
* 💾 **Dashboard Ready** — Ideal for testing data ingestion, dashboards, or analytics pipelines.

---

## 🧱 Project Structure

```
iot-data-simulator/
├── sensors/
│   ├── base_sensor.py          # Generic sensor class
│   ├── temperature_sensor.py   # Simulated temperature sensor
│   ├── humidity_sensor.py      # Simulated humidity sensor
│   └── ...                     # Add your own sensors here
├── simulator.py                # Multi-sensor orchestration
├── main.py                     # Entry point to start streaming
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/abrar39/IOT-Simulator.git
cd IOT-Simulator
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Simulator

```bash
python main.py
```

You’ll see simulated sensor data streaming in real time, like this:

```
{'sensor_id': 'T-001', 'sensor_type': 'temperature', 'timestamp': '2025-10-24T17:00:00Z', 'value': 27.31, 'unit': '°C'}
{'sensor_id': 'H-001', 'sensor_type': 'humidity', 'timestamp': '2025-10-24T17:00:01Z', 'value': 45.62, 'unit': '%'}
```

---

## 🧩 How It Works

* Each sensor is an instance of `BaseSensor`, which defines:

  * A data generation range (`min_value`, `max_value`)
  * A measurement unit (°C, %, etc.)
  * A configurable data emission interval

* `IoTSimulator` (in `simulator.py`) uses Python threads to run multiple sensors concurrently.

---

## 🧠 Extending the Simulator

To create a new sensor:

1. Add a new file under `sensors/`, e.g. `pressure_sensor.py`
2. Inherit from `BaseSensor`:

   ```python
   from sensors.base_sensor import BaseSensor

   class PressureSensor(BaseSensor):
       def __init__(self, sensor_id):
           super().__init__(sensor_id, "pressure", min_value=950, max_value=1050, unit="hPa", interval=1)
   ```
3. Import it into `main.py` and include it in the simulator list.

---

## 📊 Use Cases

* Building and testing IoT dashboards (Power BI, Grafana, etc.)
* Simulating streaming data pipelines (Kafka, MQTT, WebSocket)
* Experimenting with time-series databases (InfluxDB, TimescaleDB)
* Machine learning experiments for anomaly detection or forecasting

---

## 🔮 Future Enhancements

* 🌐 MQTT / WebSocket data publishing
* 📈 Realistic temporal variations
* 💾 CSV / database output
* ⚡ Async streaming using `asyncio`

---

## 🤝 Contributing

Contributions are welcome!
If you’d like to add new sensor types or output integrations, please open a pull request.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/new-sensor`)
3. Commit your changes (`git commit -m "Added pressure sensor"`)
4. Push to the branch (`git push origin feature/new-sensor`)
5. Open a Pull Request

---

## 🪪 License

This project is licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Abrar Asghar**
Data & AI Developer | IoT Enthusiast
