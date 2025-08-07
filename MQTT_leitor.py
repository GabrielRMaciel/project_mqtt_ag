import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
#BROKER = "mqtt.eclipse.org"
PORT = 1883
TOPIC = "industria/exemplo1"

def on_message(client, userdata, msg):
    print(f"[RECEBIDO] {msg.payload.decode()}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.on_message = on_message

client.connect(BROKER, PORT, keepalive=60)
client.subscribe(TOPIC)

print(f"Escutando '{TOPIC}' no broker {BROKER}:{PORT}")
client.loop_forever()

