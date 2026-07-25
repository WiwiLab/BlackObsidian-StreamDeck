from pathlib import Path

import soundfile as sf
import numpy as np

from modules.logger import log


class AudioCache:

    def __init__(self):

        self.folder = Path("sounds")

        self.cache = {}

        self.extensions = [
            ".wav",
            ".mp3",
            ".ogg",
            ".flac"
        ]


    def get(self, name):

        if name in self.cache:

            data, fs = self.cache[name]

            return (
                data.copy(),
                fs
            )


        archivo = None

        for ext in self.extensions:

            posible = self.folder / f"{name}{ext}"

            if posible.exists():

                archivo = posible

                break


        if archivo is None:

            log(f"Sonido no encontrado: {name}")

            return None


        data, fs = sf.read(
            str(archivo),
            dtype="float32"
        )


        # Mono → Stereo
        if data.ndim == 1:

            data = np.column_stack(
                (
                    data,
                    data
                )
            )


        self.cache[name] = (
            data,
            fs
        )

        log(f"Cargado en caché: {archivo.name}")

        return (
            data.copy(),
            fs
        )