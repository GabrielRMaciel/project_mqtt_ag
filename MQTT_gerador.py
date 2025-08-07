import paho.mqtt.client as mqtt
import time
import random
from datetime import datetime

BROKER = "test.mosquitto.org"
#BROKER = "mqtt.eclipse.org"
PORT = 1883
TOPIC = "industria/exemplo1"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

def conectar():
	try:
		client.connect(BROKER, PORT, keepalive=60)
		print(f"Conectado em {BROKER}:{PORT}")
	except Exception as e:
		print("Erro ao conectar:", e)

def publicar_valor():
	while True:
		valor = random.randint(0, 100)
		timestamp = datetime.now().isoformat()
		payload = {
			"valor": valor,
			"timestamp": timestamp
		}

		mensagem = f'{{"valor": {valor}, "timestamp": "{timestamp}"}}'

		result = client.publish(TOPIC, mensagem)
		status = result[0]

		if status == 0:
			print(f"[{timestamp}] {mensagem}")
		else:
			print("Falha ao enviar mensagem.")

		time.sleep(0.1)

if __name__ == "__main__":
	conectar()
	publicar_valor()
