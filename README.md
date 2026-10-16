# IoT_PracticaDirigida1_RosadoManzur
## **Objetivo**
Implementar un sistema IoT en el que un ESP32 lea la temperatura de un sensor DHT22 y la publique en un broker MQTT seguro (con TLS), y desde un cliente Python se reciban los datos y se pueda enviar un comando para encender o apagar un LED del ESP32
## **Diagrama del Sistema**
<img width="606" height="200" alt="image" src="https://github.com/user-attachments/assets/6e198742-a0fa-4afc-b340-fedf974ac842" />
## Temas y Recursos 
* ESP32 con WiFi y DHT22

* MQTT sobre TLS (puerto 8883)

* Certificado CA del broker público

* Librería pubsubClient (ESP32)

* Librerías en Python: paho-mqtt, ssl

* Temas: casa/temperatura y casa/led

* Formato de datos: JSON

* Comando de control: ON / OFF
