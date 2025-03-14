import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
TOPIC = "/student_group/light_control"

# Callback when a message is received
def on_message(client, userdata, message):
    command = message.payload.decode("utf-8")
    if command == "ON":
        print("💡 Light is TURNED ON")
    elif command == "OFF":
        print("💡 Light is TURNED OFF")

# MQTT Client setup
client = mqtt.Client()
client.on_message = on_message

# Connect to the MQTT broker
client.connect(BROKER, 1883, 60)
client.subscribe(TOPIC)

print("📡 Listening for MQTT messages...")
client.loop_forever()
