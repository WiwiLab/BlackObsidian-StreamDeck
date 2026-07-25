import serial
import serial.tools.list_ports
import threading
import time

from modules.logger import log


class SerialManager:

    def __init__(self):

        self.serial = None

        self.port = None

        self.running = False

        self.callback = None



    def conectar(self):

        while self.running:

            puertos = serial.tools.list_ports.comports()

            for puerto in puertos:

                nombre = (
                    puerto.description.lower()
                    + puerto.device.lower()
                )

                if (

                    "cp210" in nombre
                    or
                    "ch340" in nombre
                    or
                    "usb serial" in nombre
                    or
                    "wch" in nombre
                    or
                    "esp32" in nombre

                ):

                    try:

                        self.serial = serial.Serial(

                            puerto.device,

                            115200,

                            timeout=0.02

                        )

                        self.port = puerto.device

                        log(
                            f"ESP32 conectado en {self.port}"
                        )

                        time.sleep(2)

                        return

                    except Exception:

                        pass

            log(
                "Esperando ESP32..."
            )

            time.sleep(2)



    def leer(self):

        if self.serial is None:

            return None

        try:

            if self.serial.in_waiting:

                return (

                    self.serial.readline()

                    .decode(errors="ignore")

                    .strip()

                )

        except Exception:

            log(
                "ESP32 desconectado"
            )

            self.serial = None

            self.conectar()

        return None



    def loop(self):

        self.conectar()

        while self.running:

            evento = self.leer()

            if evento and self.callback:

                self.callback(evento)



    def iniciar(self, callback):

        self.callback = callback

        self.running = True

        threading.Thread(

            target=self.loop,

            daemon=True

        ).start()



    def detener(self):

        self.running = False

        if self.serial:

            self.serial.close()



    def enviar(self, mensaje):

        if self.serial:

            try:

                self.serial.write(

                    (mensaje + "\n").encode()

                )

            except Exception:

                pass