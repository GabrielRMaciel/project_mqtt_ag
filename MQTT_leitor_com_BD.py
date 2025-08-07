import paho.mqtt.client as mqtt
import json
from db import conectar, inserir_dado, criar_banco

criar_banco()

BROKER = "test.mosquitto.org"
#BROKER = "mqtt.eclipse.org"
PORT = 1883
TOPIC = "industria/exemplo1"

def on_message(client, userdata, msg):
	try:
		payload = json.loads(msg.payload.decode())
		valor = int(payload["valor"])
		timestamp = payload["timestamp"]

		print(f"[RECEBIDO] {timestamp} - {valor}")
		
		conn = conectar()
		try:
			inserir_dado(conn, timestamp, valor)
		finally:
			conn.close()
	except Exception as e:
		print("Erro ao processar mensagem:", e)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.on_message = on_message

client.connect(BROKER, PORT, keepalive=60)
client.subscribe(TOPIC)

print(f"Escutando '{TOPIC}' no broker {BROKER}:{PORT}")
client.loop_forever()

