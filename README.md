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

## Ejecución 
### 1. Conexión segura MQTT + TLS en el ESP32

Se configuró el microcontrolador ESP32 en el entorno Wokwi para conectarse a la red WiFi simulada y entablar una comunicación cifrada vía TLS (puerto 8883) con el broker público `broker.hivemq.com`. Se realizó la sincronización horaria previa por NTP para validar de forma correcta el certificado de seguridad.

<img width="832" height="770" alt="image" src="https://github.com/user-attachments/assets/281d4caa-62a6-45cd-a48f-3884e192c99f" />

---

### 2. Publicación de datos de temperatura (JSON)

El ESP32 realiza lecturas periódicas de temperatura y humedad a través del sensor DHT22 conectado al GPIO 15. Cada 5 segundos, la información es empaquetada en una estructura JSON (`{"temp": xx.x, "hum": xx.x}`) y publicada en el tema `casa/temperatura` empleando el canal seguro TLS.

<img width="839" height="790" alt="image" src="https://github.com/user-attachments/assets/8a73faf7-f798-4975-9216-282a82486354" />

---

### 3. Recepción de datos en el cliente Python

Se implementó un script cliente en Python que establece una conexión TLS con `broker.hivemq.com` en el puerto 8883 y se suscribe al tema `casa/temperatura`. El cliente procesa las tramas JSON entrantes y desglosa los valores numéricos para mostrarlos de forma estructurada en la terminal local.

<img width="877" height="934" alt="image" src="https://github.com/user-attachments/assets/17a39045-f8bf-4a0a-860a-68f5c5bb0082" />

<img width="866" height="227" alt="image" src="https://github.com/user-attachments/assets/a4764d8e-8c9d-4c28-bc04-323a5ad8abb4" />

---

### 4. Envío de comandos y control del LED

Desde la consola interactiva del cliente Python, se enviaron las órdenes `ON` y `OFF` hacia el tema de control `casa/led`. El ESP32 recibe estas peticiones de manera remota y conmuta el estado lógico del GPIO 2 (encendiendo o apagando el LED asignado).

<img width="857" height="215" alt="image" src="https://github.com/user-attachments/assets/40a9fe09-404a-4da2-9f6e-73715f172478" /> <img width="944" height="790" alt="image" src="https://github.com/user-attachments/assets/c8c1611b-214a-4366-9c78-c0ac4c93d712" />

<img width="337" height="71" alt="image" src="https://github.com/user-attachments/assets/46fbdfae-5943-4d72-8c7f-5acf222bdae4" /> <img width="955" height="794" alt="image" src="https://github.com/user-attachments/assets/04c0ccc6-4a50-4b3d-8df1-6e3f0aad0441" />

---

### 5. Funcionamiento general del sistema e integración

Verificación del flujo bidireccional IoT seguro. El sistema mantiene en simultáneo la transmisión remota de telemetría y la recepción de acciones de control sin interrupciones.

<img width="1919" height="884" alt="image" src="https://github.com/user-attachments/assets/ffab350d-3530-45a9-9272-a4bc6ec6d032" />

