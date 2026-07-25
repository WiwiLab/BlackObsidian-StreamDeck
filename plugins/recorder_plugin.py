import threading

import numpy as np
import sounddevice as sd
import soundfile as sf

from pathlib import Path

from core.plugin import Plugin
from modules.logger import log


class RecorderPlugin(Plugin):

    def __init__(self):

        self.recording = False

        self.audio = []

        self.sample_rate = 44100

        self.file = Path("sounds") / "B6.wav"



    def on_load(self, app):

        app.actions.register(

            "record_audio",

            self.toggle_record

        )

        log(

            "Recorder Plugin iniciado"

        )



    def callback(self, indata, frames, time, status):

        if status:

            log(status)

        self.audio.append(

            indata.copy()

        )



    def toggle_record(self, action):

        if action != "toggle":

            return


        if not self.recording:

            self.start_record()

        else:

            self.stop_record()



    def start_record(self):

        self.audio.clear()

        self.recording = True


        self.stream = sd.InputStream(

            samplerate=self.sample_rate,

            channels=1,

            callback=self.callback

        )

        self.stream.start()


        log(

            "🔴 Grabando..."

        )



    def stop_record(self):

        self.recording = False

        self.stream.stop()

        self.stream.close()


        audio = np.concatenate(

            self.audio,

            axis=0

        )


        sf.write(

            self.file,

            audio,

            self.sample_rate

        )


        segundos = len(audio) / self.sample_rate


        log(

            f"💾 Grabación guardada ({segundos:.1f} s)"

        )