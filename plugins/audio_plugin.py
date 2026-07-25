from core.plugin import Plugin
from modules.logger import log

from audio.audio_manager import AudioManager


class AudioPlugin(Plugin):

    def __init__(self):

        self.audio = AudioManager()


    def on_load(self, app):

        self.audio.start()

        app.actions.register(
            "sound",
            self.play_sound
        )

        app.actions.register(
            "sound_stop",
            self.stop_all
        )

        app.actions.register(
            "sound_volup",
            self.volume_up
        )

        app.actions.register(
            "sound_voldown",
            self.volume_down
        )

        log("Audio Plugin iniciado")


    def play_sound(self, name):

        self.audio.play(name)


    def volume_up(self):

        self.audio.volume_up()


    def volume_down(self):

        self.audio.volume_down()


    def stop_all(self):

        self.audio.stop_all()

    def on_unload(self, app):

        self.audio.stop()

    log("Audio Plugin detenido")