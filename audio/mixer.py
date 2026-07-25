import threading

import numpy as np
import sounddevice as sd

from modules.logger import log


class AudioMixer:

    def __init__(self, device):

        self.device = device

        self.sample_rate = 48000

        self.channels = 2

        self.blocksize = 512

        self.volume = 1.0

        self.gain = 1.5

        self.lock = threading.Lock()

        self.active = []

        self.stream = None


    def start(self):

        self.stream = sd.OutputStream(

            samplerate=self.sample_rate,

            channels=self.channels,

            blocksize=self.blocksize,

            latency="low",

            device=self.device,

            callback=self.callback

        )

        self.stream.start()

        log("AudioMixer iniciado")


    def stop(self):

        if self.stream:

            self.stream.stop()

            self.stream.close()

            self.stream = None


    def play(self, data):

        with self.lock:

            self.active.append(

                [data.copy(), 0]

            )


    def callback(self, outdata, frames, time, status):

        mezcla = np.zeros(

            (frames, self.channels),

            dtype=np.float32

        )


        with self.lock:

            nuevos = []


            for data, pos in self.active:

                disponibles = len(data) - pos

                cantidad = min(

                    disponibles,

                    frames

                )


                if cantidad > 0:

                    mezcla[:cantidad] += (

                        data[pos:pos + cantidad]

                        * self.volume

                        * self.gain

                    )

                    pos += cantidad


                if pos < len(data):

                    nuevos.append(

                        [data, pos]

                    )


            self.active = nuevos


        # Soft clip (mucho mejor que np.clip)

        mezcla = np.tanh(mezcla)

        outdata[:] = mezcla.astype(np.float32)


    def set_volume(self, value):

        self.volume = max(

            0,

            min(

                2,

                value

            )

        )


    def volume_up(self):

        self.set_volume(

            self.volume + 0.05

        )


    def volume_down(self):

        self.set_volume(

            self.volume - 0.05

        )


    def stop_all(self):

        with self.lock:

            self.active.clear()