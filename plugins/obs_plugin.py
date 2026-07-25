import obsws_python as obs

from core.plugin import Plugin
from modules.logger import log


class OBSPlugin(Plugin):

    def __init__(self):

        self.client = None

        self.host = "localhost"
        self.port = 4455
        self.password = ""



    def on_load(self, app):

        app.actions.register(
            "obs",
            self.obs_action
        )

        log(
            "OBS Plugin iniciado"
        )



    def connect(self):

        if self.client is not None:

            return True


        try:

            self.client = obs.ReqClient(

                host=self.host,

                port=self.port,

                password=self.password

            )


            log(
                "Conectado a OBS WebSocket"
            )


            return True



        except Exception:

            self.client = None


            log(
                "OBS no disponible"
            )


            return False



    def obs_action(self, action):


        if not self.connect():

            log(
                "No se puede ejecutar acción OBS"
            )

            return



        try:


            if action == "start":

                self.client.start_stream()

                log(
                    "Stream iniciado"
                )



            elif action == "stop":

                self.client.stop_stream()

                log(
                    "Stream detenido"
                )



            elif action == "record":

                self.client.start_record()

                log(
                    "Grabación iniciada"
                )



            elif action == "toggle_stream":

                estado = self.client.get_stream_status()


                if estado.output_active:

                    self.client.stop_stream()

                    log(
                        "Stream detenido"
                    )

                else:

                    self.client.start_stream()

                    log(
                        "Stream iniciado"
                    )



            elif action == "toggle_record":

                estado = self.client.get_record_status()


                if estado.output_active:

                    self.client.stop_record()

                    log(
                        "Grabación detenida"
                    )

                else:

                    self.client.start_record()

                    log(
                        "Grabación iniciada"
                    )



        except Exception as e:

            self.client = None

            log(
                f"Error OBS: {e}"
            )