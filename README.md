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

> 📸 **[INSERTAR CAPTURA 2: PUBLICACIÓN DE DATOS JSON EN WOKWI]**
>
> * **Elemento a evidenciar:** Monitor serie de Wokwi en ejecución continua.
> * **Detalles visibles:** Impresión periódica de los mensajes enviados en formato JSON hacia el tema `casa/temperatura`.

---

### 3. Recepción de datos en el cliente Python

Se implementó un script cliente en Python que establece una conexión TLS con `broker.hivemq.com` en el puerto 8883 y se suscribe al tema `casa/temperatura`. El cliente procesa las tramas JSON entrantes y desglosa los valores numéricos para mostrarlos de forma estructurada en la terminal local.

> 📸 **[INSERTAR CAPTURA 3: CONSOLA DE PYTHON RECIBIENDO LECTURAS]**
>
> * **Elemento a evidenciar:** Terminal/Consola del sistema ejecutando el script de Python en tu computadora.
> * **Detalles visibles:** Mensajes de estado de conexión exitosa y recepción continua de lecturas de temperatura y humedad parseadas desde el JSON.

---

### 4. Envío de comandos y control del LED

Desde la consola interactiva del cliente Python, se enviaron las órdenes `ON` y `OFF` hacia el tema de control `casa/led`. El ESP32 recibe estas peticiones de manera remota y conmuta el estado lógico del GPIO 2 (encendiendo o apagando el LED asignado).

> 📸 **[INSERTAR CAPTURA 4: ENVÍO DE COMANDOS Y ESTADO DEL LED]**
>
> * **Elemento a evidenciar:** Captura de pantalla dividida o combinada.
> * **Detalles visibles:** 
>   1. **Lado izquierdo (Python):** Consola mostrando el ingreso del comando (`ON` u `OFF`) y confirmación de envío al tema `casa/led`.
>   2. **Lado derecho (Wokwi):** Diagrama esquemático mostrando el estado físico del LED en GPIO 2 (encendido o apagado según el comando enviado).

---

### 5. Funcionamiento general del sistema e integración

Verificación del flujo bidireccional IoT seguro. El sistema mantiene en simultáneo la transmisión remota de telemetría y la recepción de acciones de control sin interrupciones.

> 📸 **[INSERTAR CAPTURA 5: VISTA GENERAL DEL ENTORNO EN WOKWI]**
>
> * **Elemento a evidenciar:** Espacio de trabajo completo en Wokwi.
> * **Detalles visibles:** Circuito ensamblado (ESP32, DHT22 en GPIO 15, LED con resistencia en GPIO 2) y simulación activa.

---
