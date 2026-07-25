import json
import subprocess
import webbrowser

from pathlib import Path

from core.plugin import Plugin
from modules.logger import log


class LauncherPlugin(Plugin):

    def __init__(self):

        self.apps = {}



    def on_load(self, app):

        self.load_apps()

        app.actions.register(
            "launch",
            self.launch
        )

        log(
            "Launcher Plugin iniciado"
        )



    def load_apps(self):

        archivo = Path("config/apps.json")


        if not archivo.exists():

            log(
                "apps.json no encontrado"
            )

            return


        with open(

            archivo,

            encoding="utf-8"

        ) as f:

            self.apps = json.load(f)



    def launch(self, name):

        destino = self.apps.get(name)



        # Caso especial navegador

        if name == "operagx" and not destino:

            log(
                "Opera GX no encontrado, usando navegador predeterminado"
            )

            webbrowser.open(
                "https://www.google.com"
            )

            return



        if not destino:

            log(
                f"Aplicación no configurada: {name}"
            )

            return



        try:


            # Paginas web

            if destino.startswith("http"):

                webbrowser.open(
                    destino
                )



            # Aplicaciones Microsoft Store

            elif destino.startswith("shell:"):

                subprocess.Popen(

                    [
                        "explorer.exe",
                        destino
                    ]

                )



            # Protocolos Steam / Spotify

            elif (
                "://" in destino
                or destino.endswith(":")
            ):

                subprocess.Popen(

                    [
                        "cmd",
                        "/c",
                        "start",
                        "",
                        destino
                    ]

                )



            # Ejecutables normales

            else:

                ruta = Path(destino)


                if ruta.exists():

                    subprocess.Popen(

                        destino,

                        cwd=str(ruta.parent)

                    )


                else:

                    log(
                        f"Ruta no encontrada: {destino}"
                    )


                    if name == "operagx":

                        webbrowser.open(
                            "https://www.google.com"
                        )



            log(
                f"Abriendo: {name}"
            )



        except Exception as e:

            log(
                f"Error abriendo {name}: {e}"
            )