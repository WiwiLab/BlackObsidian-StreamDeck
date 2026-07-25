import json
from pathlib import Path

from modules.logger import log


class ConfigManager:

    def __init__(self):

        self.path = Path("config.json")

        self.data = {}

        self.reload()


    def reload(self):

        try:

            with open(
                self.path,
                "r",
                encoding="utf-8"
            ) as f:

                self.data = json.load(f)

            log("Configuración cargada")

        except Exception as e:

            log(f"Error cargando config: {e}")

            self.data = {}


    def get(self, *keys, default=None):

        value = self.data

        for key in keys:

            if not isinstance(value, dict):

                return default

            value = value.get(key)

            if value is None:

                return default

        return value