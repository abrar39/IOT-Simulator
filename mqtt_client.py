import json
import paho.mqtt.client as mqtt
from datetime import datetime

class MQTTClient:
    def __init__(self, broker, port, topic_prefix, keepalive=60, username=None, password=None):
        self.broker = broker
        self.port = port
        self.topic_prefix = topic_prefix
        self.keepalive = keepalive
        self.username = username
        self.password = password
        self.client = mqtt.Client()

        if username and password:
            self.client.username_pw_set(username, password)

    def connect(self):
        self.client.connect(self.broker, self.port, self.keepalive)
        print(f"[MQTT] Connected to broker {self.broker}:{self.port}")

    def publish(self, topic_suffix, message):
        # convert datetime objects to string (ISO 8601 Format)
        # to avoid serialization issue with json.dumps method
        def convert(o):
            if isinstance(o, datetime):
                return o.isoformat()
            raise TypeError(f"Type {type(o)} not serializable!!")

        topic = f"{self.topic_prefix}/{topic_suffix}"
        json_message = json.dumps(message, default=convert)
        self.client.publish(topic, json_message)
        print(f"[MQTT] Published to {topic}: {json_message}")

    def disconnect(self):
        self.client.disconnect()
        print("[MQTT] Disconnected")