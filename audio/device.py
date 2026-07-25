import sounddevice as sd

from modules.logger import log


def find_output_device():

    try:

        dispositivos = sd.query_devices()

        for i, d in enumerate(dispositivos):

            nombre = d["name"].lower()

            if (
                "cable input" in nombre
                and
                d["max_output_channels"] > 0
            ):

                log(f"VB-CABLE encontrado: {d['name']}")

                return i

    except Exception as e:

        log(f"No se pudo buscar VB-CABLE: {e}")

    log("VB-CABLE no encontrado")

    return None