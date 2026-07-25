from audio.device import find_output_device
from audio.cache import AudioCache
from audio.resampler import resample, TARGET_RATE
from audio.mixer import AudioMixer

from modules.logger import log


class AudioManager:

    def __init__(self):

        self.cache = AudioCache()

        self.device = find_output_device()

        self.mixer = AudioMixer(
            self.device
        )


    def start(self):

        self.mixer.start()


    def stop(self):

        self.mixer.stop()


    def play(self, name):

        sonido = self.cache.get(name)

        if sonido is None:

            return


        data, fs = sonido


        if fs != TARGET_RATE:

            data = resample(
                data,
                fs
            )


        self.mixer.play(data)


    def volume_up(self):

        self.mixer.volume_up()

        log(
            f"Volumen efectos: {self.mixer.volume:.2f}"
        )


    def volume_down(self):

        self.mixer.volume_down()

        log(
            f"Volumen efectos: {self.mixer.volume:.2f}"
        )


    def stop_all(self):

        self.mixer.stop_all()