import ssl
import json
import time
import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORT = 8883
TOPIC_TEMP = "casa/temperatura"
TOPIC_LED = "casa/led"

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("\n[OK] Conectado exitosamente al Broker MQTT con TLS.")
        client.subscribe(TOPIC_TEMP)
        print(f"[OK] Suscrito a: {TOPIC_TEMP}\n")
    else:
        print(f"[ERROR] Codigo de conexion fallida: {rc}")

def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode('utf-8')
        data = json.loads(payload)
        temp = data.get("temp")
        hum = data.get("hum")
        print(f"\n[DATO RECIBIDO] Temperatura: {temp} °C | Humedad: {hum} %")
    except Exception:
        print(f"\n[Mensaje Raw] {msg.topic}: {msg.payload.decode('utf-8')}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.tls_set(cert_reqs=ssl.CERT_NONE)
client.tls_insecure_set(True)

print("Conectando al Broker seguro:")
client.connect(BROKER, PORT, 60)
client.loop_start()

try:
    time.sleep(1)
    print(" Control de LED ESP32")
    while True:
        cmd = input("Comando > ").strip().upper()
        if cmd in ["ON", "OFF"]:
            client.publish(TOPIC_LED, cmd)
            print(f"-> Comando '{cmd}' enviado a '{TOPIC_LED}'")
        elif cmd == "SALIR":
            break
        else:
            print("Comando invalido. Usa 'ON' u 'OFF'")
except KeyboardInterrupt:
    pass
finally:
    client.loop_stop()
    client.disconnect()
    print("Cliente desconectado")