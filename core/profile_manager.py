import json
from pathlib import Path

from modules.logger import log


class ProfileManager:

    def __init__(self):

        self.path = Path("profiles")

        self.current = "stream"

        self.profile = {}

        self.load(self.current)


    def load(self, name):

        archivo = self.path / f"{name}.json"

        try:

            with open(
                archivo,
                "r",
                encoding="utf-8"
            ) as f:

                self.profile = json.load(f)


            self.current = name

            log(
                f"Perfil cargado: {name}"
            )


        except Exception as e:

            log(
                f"Error cargando perfil {name}: {e}"
            )

            self.profile = {}


    def get_action(self, event):

        return self.profile.get(event)


    def next_profile(self):

        perfiles = [
            "stream",
            "normal",
            "edit"
        ]


        actual = perfiles.index(
            self.current
        )

        siguiente = (
            actual + 1
        ) % len(perfiles)


        self.load(
            perfiles[siguiente]
        )


        return self.current